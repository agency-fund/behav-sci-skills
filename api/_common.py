"""
api/_common.py: what the site's server functions share.

Vercel does not turn files starting with "_" into routes. api/submit.py,
api/auth.py, api/review.py, api/reviews.py, api/ratings.py and api/health.py
import this module.

- Policy: who may file expert reviews and who may moderate ratings. Worked out
  from the email address on every request, never stored in the cookie.
- Sessions: an HMAC-signed cookie, set after Google sign-in.
- Google: checks the ID token from the "Sign in with Google" button.
- Supabase: the database, reached over its REST API with the secret key.
  Only these functions talk to it; the browser never does.
- GitHub: the REST client (urllib only).
- JSONHandler: the HTTP base class, with a same-origin check on writes.

Environment variables (docs/deployment.md):
  SITE_URL             the site's origin; writes from any other origin are refused
  SESSION_SECRET       signs the session cookie (at least 16 characters)
  GOOGLE_CLIENT_ID     the OAuth client behind the sign-in button
  REVIEW_DOMAINS       email domains whose staff may file expert reviews
                       (default agency.fund,irrationallabs.com)
  REVIEWER_EMAILS      extra individual reviewers, comma-separated
  ADMIN_EMAILS         people who may hide or delete ratings
  SUPABASE_URL, SUPABASE_SECRET_KEY
  GITHUB_TOKEN, GITHUB_REPO

Standard library, plus google-auth (imported only when a token is checked).
"""
from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from http.cookies import CookieError, SimpleCookie
from http.server import BaseHTTPRequestHandler
from typing import Dict, Iterable, List, Optional, Tuple

_HERE = os.path.dirname(os.path.abspath(__file__))
_CANDIDATE_ROOTS = [os.path.dirname(_HERE), os.getcwd(), "/var/task"]
REPO_ROOT = next((r for r in _CANDIDATE_ROOTS if os.path.exists(os.path.join(r, "taxonomy.yaml"))), os.path.dirname(_HERE))
for _p in (REPO_ROOT, os.path.join(REPO_ROOT, "scripts")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

SESSION_COOKIE = "besci_session"
SESSION_DAYS = 30
DEFAULT_REVIEW_DOMAINS = "agency.fund,irrationallabs.com"
# Email domain -> (short org code used in issue titles and labels, full name)
ORGS = {"agency.fund": ("TAF", "The Agency Fund"), "irrationallabs.com": ("IL", "Irrational Labs")}
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def env_list(name: str, default: str = "") -> List[str]:
    return [x.strip().lower() for x in os.environ.get(name, default).split(",") if x.strip()]


# ---------------------------------------------------------------------------
# Policy
# ---------------------------------------------------------------------------

def email_domain(email: str) -> str:
    return email.rsplit("@", 1)[1].strip().lower() if "@" in email else ""


def can_review(email: str) -> bool:
    """Exact domain match only: x@sub.agency.fund and x@agency.fund.example.com do not count."""
    e = email.strip().lower()
    return email_domain(e) in env_list("REVIEW_DOMAINS", DEFAULT_REVIEW_DOMAINS) or e in env_list("REVIEWER_EMAILS")


def org_for(email: str) -> Tuple[str, str]:
    """(code, name) for an email address; ("", "") for people outside the two organizations."""
    domain = email_domain(email)
    if domain in ORGS:
        return ORGS[domain]
    if can_review(email):
        return "Guest", "Invited reviewer"
    return "", ""


def is_admin(email: str, db_flag: bool = False) -> bool:
    return bool(db_flag) or email.strip().lower() in env_list("ADMIN_EMAILS")


# ---------------------------------------------------------------------------
# Sessions: base64url(json) "." base64url(hmac-sha256)
# ---------------------------------------------------------------------------

def _b64e(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode("ascii")


def _b64d(text: str) -> bytes:
    return base64.urlsafe_b64decode(text + "=" * (-len(text) % 4))


def _secret() -> bytes:
    secret = os.environ.get("SESSION_SECRET", "")
    if len(secret) < 16:
        raise RuntimeError("SESSION_SECRET is missing or shorter than 16 characters.")
    return secret.encode("utf-8")


def sign_session(data: Dict, now: Optional[float] = None) -> str:
    payload = dict(data)
    payload["exp"] = int((now if now is not None else time.time()) + SESSION_DAYS * 86400)
    body = _b64e(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
    sig = _b64e(hmac.new(_secret(), body.encode("ascii"), hashlib.sha256).digest())
    return f"{body}.{sig}"


def read_session(token: str, now: Optional[float] = None) -> Optional[Dict]:
    """The session's data, or None if the token is missing, forged, or expired."""
    if not token or token.count(".") != 1:
        return None
    body, sig = token.split(".")
    try:
        expected = _b64e(hmac.new(_secret(), body.encode("ascii"), hashlib.sha256).digest())
    except (RuntimeError, UnicodeEncodeError):
        return None
    if not hmac.compare_digest(sig, expected):
        return None
    try:
        data = json.loads(_b64d(body))
    except ValueError:
        return None
    if not isinstance(data, dict) or data.get("exp", 0) < (now if now is not None else time.time()):
        return None
    return data


def session_cookie(token: str) -> str:
    return f"{SESSION_COOKIE}={token}; Path=/api; Max-Age={SESSION_DAYS * 86400}; HttpOnly; Secure; SameSite=Lax"


def clear_cookie() -> str:
    return f"{SESSION_COOKIE}=; Path=/api; Max-Age=0; HttpOnly; Secure; SameSite=Lax"


def user_view(session: Optional[Dict]) -> Dict:
    """What the browser is told about the signed-in person. Policy is recomputed here."""
    if not session:
        return {"signed_in": False}
    email = session.get("email", "")
    code, org_name = org_for(email)
    return {
        "signed_in": True,
        "email": email,
        "name": session.get("name", ""),
        "org": code,
        "org_name": org_name,
        "can_review": can_review(email),
        "is_admin": is_admin(email, session.get("db_admin", False)),
    }


# ---------------------------------------------------------------------------
# Google sign-in
# ---------------------------------------------------------------------------

def verify_google_credential(credential: str) -> Dict:
    """Check the ID token from the sign-in button: signature, audience, issuer,
    expiry, and a verified email. Returns the claims or raises ValueError."""
    client_id = os.environ.get("GOOGLE_CLIENT_ID", "")
    if not client_id:
        raise ValueError("Sign-in is not set up on this server (GOOGLE_CLIENT_ID).")
    from google.auth.transport import requests as google_requests
    from google.oauth2 import id_token

    claims = id_token.verify_oauth2_token(credential, google_requests.Request(), client_id)
    if not claims.get("email_verified") or not claims.get("email"):
        raise ValueError("Google has not verified this account's email address.")
    return claims


# ---------------------------------------------------------------------------
# Supabase (PostgREST over HTTPS)
# ---------------------------------------------------------------------------

class Supabase:
    def __init__(self, url: Optional[str] = None, key: Optional[str] = None, opener=None):
        self.url = (url if url is not None else os.environ.get("SUPABASE_URL", "")).rstrip("/")
        self.key = key if key is not None else os.environ.get("SUPABASE_SECRET_KEY", "")
        self.opener = opener or urllib.request.urlopen

    @property
    def configured(self) -> bool:
        return bool(self.url and self.key)

    def request(self, method: str, table: str, params: Optional[Dict] = None, payload=None, prefer: str = "") -> Tuple[int, object]:
        if not self.configured:
            raise RuntimeError("The database is not set up on this server (SUPABASE_URL, SUPABASE_SECRET_KEY).")
        url = f"{self.url}/rest/v1/{table}" + ("?" + urllib.parse.urlencode(params) if params else "")
        data = json.dumps(payload).encode("utf-8") if payload is not None else None
        req = urllib.request.Request(url, data=data, method=method)
        # New secret keys (sb_secret_...) go only in apikey; a legacy service_role key is a JWT and also goes in Authorization.
        req.add_header("apikey", self.key)
        if not self.key.startswith("sb_"):
            req.add_header("Authorization", f"Bearer {self.key}")
        req.add_header("Accept", "application/json")
        if data is not None:
            req.add_header("Content-Type", "application/json")
        if prefer:
            req.add_header("Prefer", prefer)
        try:
            with self.opener(req, timeout=10) as resp:
                raw = resp.read()
                return resp.status, (json.loads(raw) if raw else None)
        except urllib.error.HTTPError as exc:
            raw = exc.read()
            try:
                body = json.loads(raw) if raw else None
            except ValueError:
                body = {"message": raw[:300].decode("utf-8", errors="replace")}
            return exc.code, body

    def _check(self, what: str, status: int, body, ok: Iterable[int] = (200, 201)):
        if status not in ok:
            msg = body.get("message", "") if isinstance(body, dict) else ""
            raise RuntimeError(f"Database {what} failed ({status}) {msg}".strip())
        return body

    def select(self, table: str, params: Dict) -> List[Dict]:
        return self._check(f"read of {table}", *self.request("GET", table, params)) or []

    def insert(self, table: str, row: Dict) -> Dict:
        body = self._check(f"insert into {table}", *self.request("POST", table, None, row, "return=representation"))
        return body[0] if isinstance(body, list) and body else {}

    def upsert(self, table: str, row: Dict, on_conflict: str) -> Dict:
        body = self._check(f"upsert into {table}", *self.request(
            "POST", table, {"on_conflict": on_conflict}, row, "resolution=merge-duplicates,return=representation"))
        return body[0] if isinstance(body, list) and body else {}

    def update(self, table: str, params: Dict, patch: Dict) -> List[Dict]:
        return self._check(f"update of {table}", *self.request("PATCH", table, params, patch, "return=representation")) or []

    def delete(self, table: str, params: Dict) -> None:
        self._check(f"delete from {table}", *self.request("DELETE", table, params), ok=(200, 204))


def record_sign_in(db: Supabase, claims: Dict) -> Tuple[Optional[int], bool]:
    """Add or update the person in besci_users. Returns (user id, admin flag from the database)."""
    email = claims["email"]
    code, _ = org_for(email)
    fields = {
        "email": email, "name": claims.get("name") or email.split("@")[0], "domain": email_domain(email),
        "org": code, "can_review": can_review(email), "last_seen": now_iso(),
    }
    rows = db.select("besci_users", {"google_sub": f"eq.{claims['sub']}", "select": "id,sign_ins,is_admin"})
    if rows:
        row = rows[0]
        db.update("besci_users", {"id": f"eq.{row['id']}"}, dict(fields, sign_ins=int(row.get("sign_ins") or 0) + 1))
        return row["id"], bool(row.get("is_admin"))
    row = db.insert("besci_users", dict(fields, google_sub=claims["sub"]))
    return row.get("id"), bool(row.get("is_admin"))


def log_event(db: Supabase, name: str, user_id: Optional[int] = None, skill: str = "", props: Optional[Dict] = None) -> None:
    """Best effort: analytics must never break a request."""
    if not db.configured:
        return
    try:
        db.insert("besci_events", {"name": name, "user_id": user_id, "skill": skill or None, "props": props or {}})
    except Exception:  # noqa: BLE001
        pass


# ---------------------------------------------------------------------------
# Skills on disk
# ---------------------------------------------------------------------------

def skill_info(name: str) -> Optional[Dict]:
    """name, version, stage, and title of a skill in this deploy, or None if there's no such skill."""
    if not SKILL_NAME.match(name or ""):
        return None
    folder = os.path.join(REPO_ROOT, "skills", name)
    if not os.path.isfile(os.path.join(folder, "SKILL.md")):
        return None
    import besci_validate as bv  # noqa: WPS433 (heavy-ish; only when needed)

    sk = bv.parse_skill(folder)
    meta = sk.metadata if isinstance(sk.metadata, dict) else {}
    return {"name": name, "version": str(meta.get("version", "")), "stage": str(meta.get("stage", "")),
            "title": str(meta.get("title", "") or name)}


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
        req.add_header("User-Agent", "besci-skills-site")
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

    # --- used by the upload function (api/submit.py) ---
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
        # Best effort: labels are cosmetic; callers ignore failures.
        self._req("POST", f"/issues/{number}/labels", {"labels": labels})

    # --- used by expert reviews (api/review.py, api/reviews.py) ---
    def ensure_label(self, name: str, color: str, description: str = "") -> None:
        status, _ = self._req("GET", f"/labels/{urllib.parse.quote(name, safe='')}")
        if status == 404:
            self._req("POST", "/labels", {"name": name, "color": color, "description": description[:100]})

    def create_issue(self, title: str, body_md: str, labels: List[str]) -> dict:
        status, body = self._req("POST", "/issues", {"title": title, "body": body_md, "labels": labels})
        if status not in (200, 201):
            raise RuntimeError(f"Could not open the issue: {body.get('message', status)}")
        return body

    def list_issues(self, label: str, max_pages: int = 5) -> List[dict]:
        """Every issue (open and closed, newest first) with a label. Pull requests are skipped."""
        out: List[dict] = []
        for page in range(1, max_pages + 1):
            q = urllib.parse.urlencode({"labels": label, "state": "all", "per_page": 100, "page": page})
            status, body = self._req("GET", f"/issues?{q}")
            if status != 200:
                raise RuntimeError(f"Could not list issues: {body.get('message', status) if isinstance(body, dict) else status}")
            out.extend(i for i in body if "pull_request" not in i)
            if len(body) < 100:
                break
        return out


def github_from_env() -> GitHub:
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        raise RuntimeError("The server is missing GITHUB_TOKEN; ask a maintainer to set it up.")
    return GitHub(token, os.environ.get("GITHUB_REPO", "agency-fund/besci-skills"))


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

def allowed_origins() -> List[str]:
    out = [os.environ.get("SITE_URL", "").rstrip("/")]
    if os.environ.get("VERCEL_URL"):
        out.append("https://" + os.environ["VERCEL_URL"])  # this deployment's own URL (previews)
    return [o for o in out if o]


def origin_ok(origin: str) -> bool:
    if origin in allowed_origins():
        return True
    # `vercel dev` on this machine
    return os.environ.get("VERCEL_ENV", "development") == "development" and bool(
        re.match(r"^http://(localhost|127\.0\.0\.1)(:\d+)?$", origin or ""))


class JSONHandler(BaseHTTPRequestHandler):
    """Base for the JSON functions. Subclasses implement do_GET / do_POST / ...
    Vercel needs each function module to expose a class named `handler`."""

    log_name = "api"
    max_body = 64 * 1024

    def send_json(self, status: int, payload, cache: str = "no-store", cookies: Iterable[str] = ()) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", cache)
        self.send_header("X-Content-Type-Options", "nosniff")
        for c in cookies:
            self.send_header("Set-Cookie", c)
        self.end_headers()
        self.wfile.write(body)

    def read_json(self) -> Dict:
        length = int(self.headers.get("Content-Length", "0") or 0)
        if length <= 0:
            return {}
        if length > self.max_body:
            raise ValueError("Request too large.")
        data = json.loads(self.rfile.read(length) or b"{}")
        if not isinstance(data, dict):
            raise ValueError("Expected a JSON object.")
        return data

    def query(self) -> Dict[str, str]:
        return {k: v[0] for k, v in urllib.parse.parse_qs(urllib.parse.urlsplit(self.path).query).items()}

    def session(self) -> Optional[Dict]:
        raw = self.headers.get("Cookie", "")
        if not raw:
            return None
        try:
            jar = SimpleCookie(raw)
        except CookieError:
            return None
        morsel = jar.get(SESSION_COOKIE)
        return read_session(morsel.value) if morsel else None

    def write_allowed(self) -> bool:
        """Writes must come from the site itself (the session cookie is also SameSite=Lax)."""
        if origin_ok(self.headers.get("Origin", "")):
            return True
        self.send_json(403, {"ok": False, "error": "Requests must come from the site."})
        return False

    def log_message(self, fmt: str, *args) -> None:  # noqa: D401
        # Method and status only; never paths, bodies, cookies, or tokens.
        status = args[1] if fmt.startswith('"%s"') and len(args) > 1 else "error"
        sys.stderr.write(f"{self.log_name}: {getattr(self, 'command', '?')} {status}\n")
