"""
api/submit.py — Vercel Python serverless function behind the website's
"Upload a skill" form.

Flow:
  1. Check the shared contributor key (Phase 1 gate; swap for GitHub login in Phase 3).
  2. Accept one .skill/.zip (max 10 MB), unpack it safely (scripts/skillzip.py).
  3. Run the shared validator (scripts/besci_validate.py) on the unpacked folder.
  4. If structure passes, open a pull request on GitHub via the REST API using a
     fine-grained token with Contents + Pull requests write on the repo.
  5. Return JSON the form can show: the PR link or the plain-language report.

Environment variables (set in Vercel project settings, see docs/deployment.md):
  CONTRIBUTOR_KEY   shared secret handed to TAF and IL staff
  GITHUB_TOKEN      fine-grained PAT (or GitHub App installation token)
  GITHUB_REPO       default "agency-fund/behav-sci-skills"
  GITHUB_BASE       default "main"
  SITE_URL          used only in the PR body for the contribute page link

Nothing sensitive is logged or echoed. Standard library + PyYAML (via the validator).
"""
from __future__ import annotations

import base64
import hmac
import io
import json
import os
import re
import shutil
import sys
import tempfile
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from email.parser import BytesParser
from email.policy import default as email_default_policy
from http.server import BaseHTTPRequestHandler
from typing import Dict, List, Optional, Tuple

# --- locate the repo root so the shared scripts import in Vercel and locally ---
_HERE = os.path.dirname(os.path.abspath(__file__))
_CANDIDATE_ROOTS = [os.path.dirname(_HERE), os.getcwd(), "/var/task"]
REPO_ROOT = next((r for r in _CANDIDATE_ROOTS if os.path.exists(os.path.join(r, "taxonomy.yaml"))), os.path.dirname(_HERE))
for p in (REPO_ROOT, os.path.join(REPO_ROOT, "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import besci_validate as bv  # noqa: E402
import skillzip  # noqa: E402

TAXONOMY_PATH = os.path.join(REPO_ROOT, "taxonomy.yaml")
MAX_UPLOAD_BYTES = skillzip.MAX_ARCHIVE_BYTES
ALLOWED_ORGS = {"TAF", "IL", "community"}
TEXT_EXTENSIONS = {".md", ".txt", ".json", ".yaml", ".yml", ".csv", ".tsv", ".py", ".r", ".sh", ".html", ".css", ".js", ".svg"}

# Light rate limit: per warm instance, at most N submissions per window. Vercel
# instances are ephemeral, so this is a speed bump, not a guarantee. The
# contributor key is the real gate in Phase 1.
_RATE_WINDOW_SECONDS = 600
_RATE_MAX = 10
_recent: List[float] = []

REVIEWER_CHECKLIST = """\
### Reviewer checklist
- [ ] Atomic: one thing a behavioral scientist does, no "and"
- [ ] Trigger rule (`description` + "When to use it") is precise and names adjacent intents
- [ ] "Before you start" asks the right questions, or its "Not applicable" reason holds up
- [ ] Evidence is real, cited correctly, with WEIRD skew and replication status
- [ ] Output template is complete enough to judge a run by
- [ ] Failure modes are honest and specific
- [ ] Escalation point is concrete, or its "Not applicable" reason holds up
- [ ] Evals are realistic prompts, at least three
- [ ] At merge: set `status: published`, fill `reviewed_by`, confirm CHANGELOG entry
"""


# ---------------------------------------------------------------------------
# Pure helpers (unit-tested in scripts/test_submit.py)
# ---------------------------------------------------------------------------

def check_contributor_key(provided: Optional[str]) -> bool:
    expected = os.environ.get("CONTRIBUTOR_KEY", "")
    if not expected or not provided:
        return False
    return hmac.compare_digest(provided.strip().encode("utf-8"), expected.strip().encode("utf-8"))


def rate_limited() -> bool:
    now = time.time()
    while _recent and now - _recent[0] > _RATE_WINDOW_SECONDS:
        _recent.pop(0)
    if len(_recent) >= _RATE_MAX:
        return True
    _recent.append(now)
    return False


def parse_multipart(content_type: str, body: bytes) -> Tuple[Dict[str, str], Optional[Tuple[str, bytes]]]:
    """Return (fields, (filename, bytes) or None). Uses the stdlib email parser."""
    if not content_type or "multipart/form-data" not in content_type:
        raise ValueError("Expected multipart/form-data.")
    header = f"Content-Type: {content_type}\r\nMIME-Version: 1.0\r\n\r\n".encode("utf-8")
    msg = BytesParser(policy=email_default_policy).parsebytes(header + body)
    fields: Dict[str, str] = {}
    upload: Optional[Tuple[str, bytes]] = None
    for part in msg.iter_parts():
        name = part.get_param("name", header="content-disposition")
        if not name:
            continue
        filename = part.get_filename()
        payload = part.get_payload(decode=True) or b""
        if filename:
            upload = (os.path.basename(filename), payload)
        else:
            fields[str(name)] = payload.decode("utf-8", errors="replace").strip()
    return fields, upload


def unpack_and_validate(archive_bytes: bytes, workdir: str) -> Tuple[bv.Skill, skillzip.UnpackResult]:
    """Write the upload to disk, unpack it, run the validator. Raises SkillZipError for bad archives."""
    archive_path = os.path.join(workdir, "upload.skill")
    with open(archive_path, "wb") as fh:
        fh.write(archive_bytes)
    dest = os.path.join(workdir, "unpacked")
    os.makedirs(dest, exist_ok=True)
    result = skillzip.unpack_archive(archive_path, dest)
    taxonomy = bv.load_taxonomy(TAXONOMY_PATH)
    skill = bv.validate_skill(bv.parse_skill(result.skill_dir), taxonomy)
    return skill, result


def build_tree_entries(skill_dir: str, skill_name: str) -> List[Dict[str, str]]:
    """Git tree entries for every file under skills/<name>/. Text as utf-8 content, binaries as base64 blobs (resolved later)."""
    entries: List[Dict[str, str]] = []
    for root, dirs, files in os.walk(skill_dir):
        dirs[:] = sorted(d for d in dirs if d not in skillzip.IGNORED_PARTS)
        for f in sorted(files):
            if f in skillzip.IGNORED_PARTS:
                continue
            full = os.path.join(root, f)
            rel = os.path.relpath(full, skill_dir).replace(os.sep, "/")
            path = f"skills/{skill_name}/{rel}"
            with open(full, "rb") as fh:
                data = fh.read()
            ext = os.path.splitext(f)[1].lower()
            if ext in TEXT_EXTENSIONS:
                try:
                    entries.append({"path": path, "mode": "100644", "type": "blob", "content": data.decode("utf-8")})
                    continue
                except UnicodeDecodeError:
                    pass
            entries.append({"path": path, "mode": "100644", "type": "blob", "_binary_b64": base64.b64encode(data).decode("ascii")})
    return entries


def branch_name_for(skill_name: str, now: Optional[datetime] = None) -> str:
    now = now or datetime.now(timezone.utc)
    return f"submit/{skill_name}-{now.strftime('%Y%m%d-%H%M')}"


def pr_body(skill: bv.Skill, fields: Dict[str, str], report: str) -> str:
    md = skill.metadata
    handle = fields.get("author_github", "").strip().lstrip("@")
    site = os.environ.get("SITE_URL", "").rstrip("/")
    lines = [
        f"## Add skill: `{skill.name}` v{md.get('version', '?')}",
        "",
        f"**Author:** {fields.get('author_name', '').strip() or '(not given)'}" + (f" (@{handle})" if handle else ""),
        f"**Org:** {fields.get('org', '').strip()}",
        f"**Stage:** {md.get('stage', '?')}  **Type:** {md.get('type', '?')}  **Status:** {md.get('status', '?')}",
        "",
        "**What it does:** " + (skill.sections.get("What it does", "").strip().split("\n")[0] or "(see SKILL.md)"),
        "",
        "<details><summary>Validator report (structure only)</summary>",
        "",
        "```",
        report,
        "```",
        "</details>",
        "",
        REVIEWER_CHECKLIST,
        "",
        "Submitted via the website upload form. Disclosure acknowledged: yes.",
    ]
    if site:
        lines.append(f"Contribution guide: {site}/contribute")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# GitHub REST client (urllib only)
# ---------------------------------------------------------------------------

class GitHub:
    def __init__(self, token: str, repo: str):
        self.token = token
        self.repo = repo
        self.base = f"https://api.github.com/repos/{repo}"

    def _req(self, method: str, path: str, payload: Optional[dict] = None, absolute: bool = False) -> Tuple[int, dict]:
        url = path if absolute else self.base + path
        data = json.dumps(payload).encode("utf-8") if payload is not None else None
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("Authorization", f"Bearer {self.token}")
        req.add_header("Accept", "application/vnd.github+json")
        req.add_header("X-GitHub-Api-Version", "2022-11-28")
        req.add_header("User-Agent", "behav-sci-skills-submit")
        if data is not None:
            req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=25) as resp:
                raw = resp.read()
                return resp.status, (json.loads(raw) if raw else {})
        except urllib.error.HTTPError as exc:
            raw = exc.read()
            try:
                body = json.loads(raw) if raw else {}
            except json.JSONDecodeError:
                body = {"message": raw.decode("utf-8", errors="replace")[:500]}
            return exc.code, body

    def base_sha(self, branch: str) -> str:
        status, body = self._req("GET", f"/git/ref/heads/{branch}")
        if status != 200:
            raise RuntimeError(f"Could not read base branch '{branch}': {body.get('message', status)}")
        return body["object"]["sha"]

    def branch_exists(self, name: str) -> bool:
        status, _ = self._req("GET", f"/git/ref/heads/{name}")
        return status == 200

    def create_branch(self, name: str, sha: str) -> None:
        status, body = self._req("POST", "/git/refs", {"ref": f"refs/heads/{name}", "sha": sha})
        if status not in (200, 201):
            raise RuntimeError(f"Could not create branch: {body.get('message', status)}")

    def create_blob_b64(self, b64: str) -> str:
        status, body = self._req("POST", "/git/blobs", {"content": b64, "encoding": "base64"})
        if status not in (200, 201):
            raise RuntimeError(f"Could not upload a file: {body.get('message', status)}")
        return body["sha"]

    def create_tree(self, base_tree: str, entries: List[Dict[str, str]]) -> str:
        resolved = []
        for e in entries:
            if "_binary_b64" in e:
                resolved.append({"path": e["path"], "mode": e["mode"], "type": "blob", "sha": self.create_blob_b64(e["_binary_b64"])})
            else:
                resolved.append({"path": e["path"], "mode": e["mode"], "type": "blob", "content": e["content"]})
        status, body = self._req("POST", "/git/trees", {"base_tree": base_tree, "tree": resolved})
        if status not in (200, 201):
            raise RuntimeError(f"Could not build the commit tree: {body.get('message', status)}")
        return body["sha"]

    def create_commit(self, message: str, tree: str, parent: str) -> str:
        status, body = self._req("POST", "/git/commits", {"message": message, "tree": tree, "parents": [parent]})
        if status not in (200, 201):
            raise RuntimeError(f"Could not create the commit: {body.get('message', status)}")
        return body["sha"]

    def update_ref(self, branch: str, sha: str) -> None:
        status, body = self._req("PATCH", f"/git/refs/heads/{branch}", {"sha": sha, "force": False})
        if status != 200:
            raise RuntimeError(f"Could not move the branch: {body.get('message', status)}")

    def open_pr(self, title: str, head: str, base: str, body_md: str) -> dict:
        status, body = self._req("POST", "/pulls", {"title": title, "head": head, "base": base, "body": body_md})
        if status not in (200, 201):
            raise RuntimeError(f"Could not open the pull request: {body.get('message', status)}")
        return body

    def add_labels(self, number: int, labels: List[str]) -> None:
        # Best effort: missing labels are created lazily by GitHub only for repo admins; ignore failures.
        self._req("POST", f"/issues/{number}/labels", {"labels": labels})


def open_pull_request(skill: bv.Skill, skill_dir: str, fields: Dict[str, str], report: str) -> str:
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        raise RuntimeError("Server is missing GITHUB_TOKEN; ask a maintainer to configure the upload endpoint.")
    repo = os.environ.get("GITHUB_REPO", "agency-fund/behav-sci-skills")
    base = os.environ.get("GITHUB_BASE", "main")
    gh = GitHub(token, repo)
    base_sha = gh.base_sha(base)
    branch = branch_name_for(skill.name)
    suffix = 1
    while gh.branch_exists(branch):
        suffix += 1
        branch = f"{branch_name_for(skill.name)}-{suffix}"
    gh.create_branch(branch, base_sha)
    entries = build_tree_entries(skill_dir, skill.name)
    tree_sha = gh.create_tree(base_sha, entries)
    author = fields.get("author_name", "").strip() or "a contributor"
    handle = fields.get("author_github", "").strip().lstrip("@")
    trailer = f"\n\nCo-authored-by: {author} <{handle}@users.noreply.github.com>" if handle else ""
    commit_sha = gh.create_commit(
        f"Add skill: {skill.name} (v{skill.metadata.get('version', '?')})\n\nSubmitted by {author} via the website upload form.{trailer}",
        tree_sha,
        base_sha,
    )
    gh.update_ref(branch, commit_sha)
    pr = gh.open_pr(
        title=f"Add skill: {skill.name} (v{skill.metadata.get('version', '?')})",
        head=branch,
        base=base,
        body_md=pr_body(skill, fields, report),
    )
    try:
        gh.add_labels(int(pr["number"]), ["skill", "submitted-via-site"])
    except Exception:  # noqa: BLE001 — labels are cosmetic
        pass
    return pr["html_url"]


# ---------------------------------------------------------------------------
# Request handling
# ---------------------------------------------------------------------------

def handle_submission(content_type: str, body: bytes) -> Tuple[int, dict]:
    """Everything after the HTTP layer. Returns (status, json_payload)."""
    try:
        fields, upload = parse_multipart(content_type, body)
    except Exception as exc:  # noqa: BLE001
        return 400, {"ok": False, "error": f"Could not read the form: {exc}"}

    if not check_contributor_key(fields.get("contributor_key")):
        return 401, {"ok": False, "error": "Contributor key missing or incorrect. Ask a maintainer for the Phase 1 key."}
    if rate_limited():
        return 429, {"ok": False, "error": "Too many submissions right now. Try again in a few minutes."}
    if fields.get("disclosure_ack", "").lower() != "yes":
        return 400, {"ok": False, "error": "You must acknowledge DISCLOSURE.md before submitting."}
    org = fields.get("org", "").strip()
    if org not in ALLOWED_ORGS:
        return 400, {"ok": False, "error": f"org must be one of {sorted(ALLOWED_ORGS)}."}
    if not fields.get("author_name", "").strip():
        return 400, {"ok": False, "error": "author_name is required."}
    if upload is None:
        return 400, {"ok": False, "error": "No file uploaded. Attach your .skill file."}
    filename, data = upload
    if not filename.lower().endswith((".skill", ".zip")):
        return 400, {"ok": False, "error": "Upload a .skill or .zip file."}
    if len(data) > MAX_UPLOAD_BYTES:
        return 413, {"ok": False, "error": f"File is larger than {MAX_UPLOAD_BYTES // (1024 * 1024)} MB."}

    workdir = tempfile.mkdtemp(prefix="besci-submit-")
    try:
        try:
            skill, result = unpack_and_validate(data, workdir)
        except skillzip.SkillZipError as exc:
            return 422, {"ok": False, "error": "Archive rejected", "report": str(exc)}
        report = bv.report_text([skill])
        if skill.errors:
            return 422, {"ok": False, "error": "Validation failed", "report": report}
        if skill.metadata.get("org") and skill.metadata.get("org") != org:
            report += f"\nNote: the form says org={org} but SKILL.md says org={skill.metadata.get('org')}. The reviewer will reconcile."
        try:
            pr_url = open_pull_request(skill, result.skill_dir, fields, report)
        except RuntimeError as exc:
            return 502, {"ok": False, "error": str(exc), "report": report}
        return 200, {"ok": True, "pr_url": pr_url, "report": report}
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


class handler(BaseHTTPRequestHandler):  # noqa: N801 — Vercel requires this name
    def _send(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self) -> None:  # noqa: N802
        # Same-origin form posts need no CORS, but browsers may preflight. Allow only our own origin.
        origin = self.headers.get("Origin", "")
        site = os.environ.get("SITE_URL", "").rstrip("/")
        self.send_response(204)
        if site and origin == site:
            self.send_header("Access-Control-Allow-Origin", site)
            self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self) -> None:  # noqa: N802
        self._send(405, {"ok": False, "error": "POST a multipart form with your .skill file to this endpoint."})

    def do_POST(self) -> None:  # noqa: N802
        length = int(self.headers.get("Content-Length", "0") or 0)
        if length <= 0:
            self._send(400, {"ok": False, "error": "Empty request."})
            return
        if length > MAX_UPLOAD_BYTES + 64 * 1024:
            self._send(413, {"ok": False, "error": f"Request larger than {MAX_UPLOAD_BYTES // (1024 * 1024)} MB."})
            return
        body = self.rfile.read(length)
        status, payload = handle_submission(self.headers.get("Content-Type", ""), body)
        self._send(status, payload)

    def log_message(self, fmt: str, *args) -> None:  # noqa: D401
        # Only method and status; never form contents.
        sys.stderr.write("submit: %s\n" % (fmt % args).split('"')[0])
