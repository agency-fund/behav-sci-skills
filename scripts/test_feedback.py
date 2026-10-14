#!/usr/bin/env python3
"""
test_feedback.py: local checks for sign-in and expert reviews, with no network.

Covers: who may review (domain allowlist edge cases), session cookies (signing,
tampering, expiry), the expert-review issue format (title, labels, body, and
parsing it back, including issues filed with the GitHub form), CHANGELOG issue
references, the browser's copies of the verdicts and parts, the issue form's
field ids, and the api/auth.py, api/review.py and api/reviews.py logic
against in-memory stand-ins for Google, Supabase, and GitHub. Ends with a real
HTTP round trip through the handlers, to check the same-origin rule.

Run: uv run python scripts/test_feedback.py
"""
from __future__ import annotations

import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from typing import Dict, List

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "api"))

for k in ("SITE_URL", "VERCEL_URL", "VERCEL_ENV", "REVIEW_DOMAINS", "REVIEWER_EMAILS", "ADMIN_EMAILS",
          "SUPABASE_URL", "SUPABASE_SECRET_KEY", "GITHUB_TOKEN", "VERCEL_GIT_COMMIT_SHA"):
    os.environ.pop(k, None)
os.environ["SESSION_SECRET"] = "test-secret-0123456789abcdef"
os.environ["GOOGLE_CLIENT_ID"] = "test-client.apps.googleusercontent.com"

import _common as c  # noqa: E402
import _review_issue as R  # noqa: E402
import auth  # noqa: E402
import review  # noqa: E402
import reviews  # noqa: E402
import build_site  # noqa: E402

checks = 0


def ok(cond: bool, msg: str) -> None:
    global checks
    checks += 1
    if not cond:
        print(f"FAIL: {msg}")
        sys.exit(1)
    print(f"ok   {msg}")


# ---------------------------------------------------------------------------
# Stand-ins
# ---------------------------------------------------------------------------

def fake_verify(credential: str) -> Dict:
    """'fake:<email>' signs in as that address; anything else is refused."""
    if not credential.startswith("fake:"):
        raise ValueError("Wrong number of segments in token")
    email = credential[5:]
    return {"sub": "sub-" + email, "email": email, "email_verified": True, "name": email.split("@")[0].title()}


class FakeSupabase:
    """The slice of PostgREST that api/*.py uses: eq./gte. filters, order, limit."""

    DEFAULTS = {
        "besci_users": {"is_admin": False, "sign_ins": 1},
        "besci_ratings": {"hidden": False, "anonymous": False, "comment": None},
    }

    def __init__(self):
        self.tables: Dict[str, List[Dict]] = {}
        self.next_id = 1
        self.configured = True

    def _match(self, row: Dict, params: Dict) -> bool:
        for k, v in params.items():
            if k in ("select", "order", "limit"):
                continue
            op, _, val = str(v).partition(".")
            have = row.get(k)
            if op == "eq" and str(have).lower() != val.lower():
                return False
            if op == "gte" and not (have is not None and str(have) >= val):
                return False
            if op == "in" and str(have) not in val.strip("()").split(","):
                return False
        return True

    def select(self, table: str, params: Dict) -> List[Dict]:
        rows = [dict(r) for r in self.tables.get(table, []) if self._match(r, params)]
        order = params.get("order", "")
        if order:
            col, _, direction = order.partition(".")
            rows.sort(key=lambda r: str(r.get(col)), reverse=direction == "desc")
        if params.get("limit"):
            rows = rows[: int(params["limit"])]
        return rows

    def insert(self, table: str, row: Dict) -> Dict:
        now = c.now_iso()
        full = dict(self.DEFAULTS.get(table, {}))
        full.update({"id": self.next_id, "created_at": now, "updated_at": now, "first_seen": now})
        full.update(row)
        self.next_id += 1
        self.tables.setdefault(table, []).append(full)
        return dict(full)

    def upsert(self, table: str, row: Dict, on_conflict: str) -> Dict:
        keys = on_conflict.split(",")
        for r in self.tables.get(table, []):
            if all(str(r.get(k)) == str(row.get(k)) for k in keys):
                r.update(row)
                return dict(r)
        return self.insert(table, row)

    def update(self, table: str, params: Dict, patch: Dict) -> List[Dict]:
        out = []
        for r in self.tables.get(table, []):
            if self._match(r, params):
                r.update(patch)
                out.append(dict(r))
        return out

    def delete(self, table: str, params: Dict) -> None:
        self.tables[table] = [r for r in self.tables.get(table, []) if not self._match(r, params)]


class FakeGitHub:
    def __init__(self, repo: str = "agency-fund/besci-skills", label_on_create: bool = True):
        self.repo = repo
        self.issues: List[Dict] = []
        self.labels: Dict[str, str] = {}
        self.label_on_create = label_on_create

    def ensure_label(self, name: str, color: str, description: str = "") -> None:
        self.labels.setdefault(name, color)

    def create_issue(self, title: str, body_md: str, labels: List[str]) -> Dict:
        n = 100 + len(self.issues)
        issue = {"number": n, "title": title, "body": body_md, "html_url": f"https://github.com/{self.repo}/issues/{n}",
                 "state": "open", "state_reason": None, "comments": 0, "created_at": c.now_iso(), "closed_at": None,
                 "user": {"login": "besci-bot"},
                 "labels": [{"name": x} for x in labels] if self.label_on_create else []}
        self.issues.append(issue)
        return dict(issue)

    def add_labels(self, number: int, labels: List[str]) -> None:
        for i in self.issues:
            if i["number"] == number:
                i["labels"] = [{"name": x} for x in labels]

    def list_issues(self, label: str, max_pages: int = 5) -> List[Dict]:
        return [i for i in reversed(self.issues) if any(lb["name"] == label for lb in i["labels"])]


def session_for(email: str, db: FakeSupabase = None) -> Dict:
    status, payload, cookies = auth.sign_in("fake:" + email, "review", db or FakeSupabase())
    assert status == 200, payload
    return c.read_session(cookies[0].split(";")[0].split("=", 1)[1])


GOOD_REVIEW = {
    "skill": "define-key-behavior", "verdict": "needs-revision", "parts": ["How to do it", "Test cases", "Bogus part"],
    "review": "The scoring table needs a column for cost. **Step 3** asks for eight scores at once.",
    "evidence": "Michie et al. 2011", "name": "Jane @Doe", "github": "@janedoe", "commit": "abc1234",
}


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_policy() -> None:
    ok(c.can_review("michael@agency.fund") and c.can_review("a.b@irrationallabs.com"), "TAF and IL addresses may review")
    ok(c.can_review("Someone@AGENCY.FUND"), "domain check ignores case")
    ok(not c.can_review("x@sub.agency.fund") and not c.can_review("x@agency.fund.evil.com"), "subdomains and lookalikes may not review")
    ok(not c.can_review("x@gmail.com") and not c.can_review("agency.fund") and not c.can_review(""), "other and malformed addresses may not review")
    ok(c.org_for("x@irrationallabs.com") == ("IL", "Irrational Labs") and c.org_for("x@gmail.com") == ("", ""), "org from domain")
    os.environ["REVIEWER_EMAILS"] = "Expert@University.edu"
    ok(c.can_review("expert@university.edu") and c.org_for("expert@university.edu")[0] == "Guest", "REVIEWER_EMAILS adds individual reviewers")
    os.environ.pop("REVIEWER_EMAILS")
    os.environ["ADMIN_EMAILS"] = "michael@agency.fund"
    ok(c.is_admin("Michael@agency.fund") and not c.is_admin("x@agency.fund") and c.is_admin("x@agency.fund", True), "admins from ADMIN_EMAILS or the database flag")
    os.environ.pop("ADMIN_EMAILS")


def test_sessions() -> None:
    token = c.sign_session({"email": "a@agency.fund", "name": "A"})
    ok(c.read_session(token)["email"] == "a@agency.fund", "a signed session reads back")
    body, sig = token.split(".")
    forged = c._b64e(json.dumps({"email": "x@agency.fund", "exp": 9999999999}).encode()) + "." + sig
    ok(c.read_session(forged) is None, "a changed payload is rejected")
    ok(c.read_session(body + "." + sig[:-2] + "AA") is None, "a changed signature is rejected")
    ok(c.read_session(c.sign_session({"email": "a"}, now=time.time() - 31 * 86400)) is None, "an expired session is rejected")
    ok(c.read_session("") is None and c.read_session("a.b.c") is None, "malformed tokens are rejected")
    os.environ["SESSION_SECRET"] = "other-secret-0123456789abcdef"
    ok(c.read_session(token) is None, "a token from another secret is rejected")
    os.environ["SESSION_SECRET"] = "short"
    ok(c.read_session(token) is None, "a too-short secret fails closed")
    os.environ["SESSION_SECRET"] = "test-secret-0123456789abcdef"
    cookie = c.session_cookie(token)
    ok(all(x in cookie for x in ("HttpOnly", "Secure", "SameSite=Lax", "Path=/api")), "session cookie flags")


def test_issue_format() -> None:
    t = R.title("define-key-behavior", "0.1.0", "Jane @Doe\n", "IL")
    ok(t == "[Expert review] define-key-behavior v0.1.0 by Jane Doe (IL)", f"title format: {t}")
    ok(R.labels("define-key-behavior", "define", "needs-revision", "IL") ==
       ["expert-review", "skill:define-key-behavior", "stage:define", "verdict:needs-revision", "org:IL"], "labels")
    r = {"skill": "define-key-behavior", "version": "0.1.0", "commit": "abc1234", "repo": "agency-fund/besci-skills",
         "verdict": "needs-revision", "parts": ["How to do it", "Test cases"], "review": "Line one.\n\n### Not a field\n\nMore.",
         "evidence": "", "name": "Jane Doe", "org": "IL", "org_name": "Irrational Labs", "github": "janedoe",
         "submitted": "2026-10-13T15:04:05Z"}
    b = R.body(r)
    ok(b.index("### Skill") < b.index("### Verdict") < b.index("### Review") < b.index("### Reviewer"), "body sections in order")
    ok("/blob/abc1234/skills/define-key-behavior/SKILL.md" in b, "body links SKILL.md at the reviewed commit")
    ok("### Evidence or sources\n\n_No response_" in b, "empty fields read _No response_, as on issue forms")
    ok("Jane Doe, Irrational Labs (@janedoe)" in b, "reviewer line with GitHub mention")
    p = R.parse(b)
    ok(p and p["skill"] == "define-key-behavior" and p["version"] == "0.1.0" and p["verdict"] == "needs-revision", "parse reads skill, version, verdict")
    ok(p["parts"] == ["How to do it", "Test cases"] and p["github"] == "janedoe" and p["org"] == "IL", "parse reads parts, GitHub, org")
    ok(p["name"] == "Jane Doe" and p["org_name"] == "Irrational Labs", "parse reads the reviewer")
    # A reviewer pasting a fake record into their text doesn't override the real one, which comes last.
    r2 = dict(r, review='<!-- besci-review v1 {"skill":"other-skill","version":"9.9.9"} -->')
    ok(R.parse(R.body(r2))["skill"] == "define-key-behavior", "the server's record wins over one pasted into the review")
    form_body = ("### Skill\n\nselect-messenger\n\n### Version reviewed\n\nv0.1.0\n\n### Content reviewed\n\n_No response_\n\n"
                 "### Verdict\n\nPublish after small changes\n\n### Parts this concerns\n\n- [X] What it does\n- [ ] When to use it\n- [x] References\n\n"
                 "### Review\n\nGood skill.\n\n### Evidence or sources\n\n_No response_\n\n### Reviewer\n\nAmy Lee, The Agency Fund\n")
    f = R.parse(form_body)
    ok(f and f["skill"] == "select-messenger" and f["version"] == "0.1.0" and f["verdict"] == "small-changes", "parse reads an issue-form body")
    ok(f["parts"] == ["What it does", "References"] and f["name"] == "Amy Lee" and f["org_name"] == "The Agency Fund", "issue-form checkboxes and reviewer")
    ok(R.parse("### Skill\n\nNot A Skill Name\n") is None and R.parse("") is None, "non-review bodies parse to None")
    ex = R.excerpt("## Heading\n\n**Bold** and [a link](http://x) and `code`.\n\n```\nblock\n```\n" + "word " * 300)
    ok(ex.startswith("Heading\n\nBold and a link and code.") and ex.endswith("…") and len(ex) <= 601, "excerpt strips markdown and truncates")


def test_changelog_refs() -> None:
    log = ("# Changelog\n\n## 0.3.0 - 2026-12-01\nAddresses expert review #42 again. Unrelated sentence.\n\n"
           "## 0.2.0 - 2026-11-01\nAddresses expert review #42 (Jane Doe): added a cost column. Also fixes #7.\n"
           "See `#99` and [#5](x) and &#39;.\n\n## 0.1.0 - 2026-10-08\nFirst version.\n")
    refs = build_site.changelog_refs(log)
    ok(refs["42"]["version"] == "0.2.0" and "cost column" in refs["42"]["text"], "an issue cited twice maps to the earliest version")
    ok(refs["7"]["version"] == "0.2.0" and "99" not in refs and "5" not in refs and "39" not in refs, "code, existing links, and entities are skipped")
    linked = build_site.link_issue_refs("Fixes #12. Not `#13`, [#14](u), or &#15;.")
    ok("[#12](https://github.com/agency-fund/besci-skills/issues/12)" in linked and linked.count("issues/") == 1, "#N becomes an issue link")


def test_browser_and_form_match() -> None:
    js = open(os.path.join(ROOT, "site", "src", "feedback.js"), encoding="utf-8").read()
    js_verdicts = re.findall(r'\["([a-z-]+)", "([^"]+)"\]', js.split("var VERDICTS")[1].split("];")[0])
    ok(dict(js_verdicts) == R.VERDICTS, "feedback.js VERDICTS match api/_review_issue.py")
    js_parts = re.findall(r'"([^"]+)"', js.split("var PARTS")[1].split("];")[0])
    ok(js_parts == R.PARTS, "feedback.js PARTS match api/_review_issue.py")
    import yaml
    form = yaml.safe_load(open(os.path.join(ROOT, ".github", "ISSUE_TEMPLATE", "expert-review.yml"), encoding="utf-8"))
    fields = {b["id"]: b for b in form["body"] if "id" in b}
    ok(set(fields) == {fid for fid, _ in R.FIELDS} - {"submitted"}, "issue form field ids match the body fields")
    ok(all(fields[fid]["attributes"]["label"] == heading for fid, heading in R.FIELDS if fid in fields), "issue form labels match the body headings")
    ok(fields["verdict"]["attributes"]["options"] == list(R.VERDICTS.values()), "issue form verdicts match")
    ok([o["label"] for o in fields["parts"]["attributes"]["options"]] == R.PARTS, "issue form parts match")
    ok(form["labels"] == [R.LABEL], "issue form applies the expert-review label")


def test_auth() -> None:
    c.verify_google_credential = fake_verify
    db = FakeSupabase()
    status, payload, cookies = auth.sign_in("fake:jane@irrationallabs.com", "review", db)
    ok(status == 200 and payload["can_review"] and payload["org"] == "IL" and cookies, "a TAF/IL sign-in may review and gets a cookie")
    auth.sign_in("fake:jane@irrationallabs.com", "review", db)
    users = db.tables["besci_users"]
    ok(len(users) == 1 and users[0]["sign_ins"] == 2 and users[0]["can_review"], "sign-ins are recorded once per person and counted")
    status, payload, _ = auth.sign_in("fake:pat@gmail.com", "review", db)
    ok(status == 200 and not payload["can_review"], "anyone can sign in; only staff may review")
    names = [e["name"] for e in db.tables["besci_events"]]
    ok(names.count("sign_in") == 3 and names.count("review_denied_domain") == 1, "sign-in and denied-review events are logged")
    ok(auth.sign_in("not-a-token", "review", db)[0] == 401 and auth.sign_in("", "", db)[0] == 400, "bad or missing credentials are refused")
    os.environ["SESSION_SECRET"] = ""
    ok(auth.sign_in("fake:jane@irrationallabs.com", "review", db)[0] == 500, "no SESSION_SECRET: sign-in fails closed")
    os.environ["SESSION_SECRET"] = "test-secret-0123456789abcdef"
    unconfigured = c.Supabase(url="", key="")
    ok(auth.sign_in("fake:jane@irrationallabs.com", "review", unconfigured)[0] == 200, "sign-in works without a database")


def test_review() -> None:
    db, gh = FakeSupabase(), FakeGitHub()
    staff = session_for("jane@irrationallabs.com", db)
    ok(review.file_review(None, GOOD_REVIEW, gh, db)[0] == 401, "signed out: 401")
    ok(review.file_review(session_for("pat@gmail.com", db), GOOD_REVIEW, gh, db)[0] == 403, "not staff: 403")
    ok(review.file_review(staff, dict(GOOD_REVIEW, skill="no-such-skill"), gh, db)[0] == 400, "unknown skill: 400")
    ok(review.file_review(staff, dict(GOOD_REVIEW, skill="../etc"), gh, db)[0] == 400, "path-like skill name: 400")
    ok(review.file_review(staff, dict(GOOD_REVIEW, verdict="great"), gh, db)[0] == 400, "unknown verdict: 400")
    ok(review.file_review(staff, dict(GOOD_REVIEW, review="Too short"), gh, db)[0] == 400, "too-short review: 400")
    ok(review.file_review(staff, dict(GOOD_REVIEW, github="not a user!"), gh, db)[0] == 400, "bad GitHub username: 400")
    ok(not gh.issues, "nothing filed for rejected reviews")

    status, payload = review.file_review(staff, GOOD_REVIEW, gh, db)
    ok(status == 200 and payload["number"] == 100 and payload["url"].endswith("/issues/100"), "a valid review is filed")
    issue = gh.issues[0]
    version = c.skill_info("define-key-behavior")["version"]
    ok(issue["title"] == f"[Expert review] define-key-behavior v{version} by Jane Doe (IL)", f"issue title: {issue['title']}")
    ok([lb["name"] for lb in issue["labels"]] == ["expert-review", "skill:define-key-behavior", "stage:define", "verdict:needs-revision", "org:IL"], "issue labels")
    ok(set(gh.labels) >= {"expert-review", "skill:define-key-behavior"} and gh.labels["expert-review"] == "F1B505", "labels created with fixed colors")
    parsed = R.parse(issue["body"])
    ok(parsed["parts"] == ["How to do it", "Test cases"] and parsed["github"] == "janedoe" and parsed["commit"] == "abc1234", "unknown parts dropped; @ stripped; commit kept")
    ok("jane@irrationallabs.com" not in issue["body"] and "jane@" not in issue["title"], "the email address is not published")
    ok(db.tables["besci_expert_reviews"][0]["issue_number"] == 100 and any(e["name"] == "review_filed" for e in db.tables["besci_events"]), "review recorded and logged")

    for _ in range(9):
        review.file_review(staff, GOOD_REVIEW, gh, db)
    ok(review.file_review(staff, GOOD_REVIEW, gh, db)[0] == 429 and len(gh.issues) == 10, "ten reviews a day, then 429")

    gh2 = FakeGitHub(label_on_create=False)
    review.file_review(session_for("amy@agency.fund"), GOOD_REVIEW, gh2, FakeSupabase())
    ok(len(gh2.issues[0]["labels"]) == 5, "labels added afterwards if GitHub dropped them at creation")
    status, payload = review.file_review(session_for("amy@agency.fund"), GOOD_REVIEW, None, FakeSupabase())
    ok(status == 502 and payload.get("fallback"), "no GITHUB_TOKEN: 502 with the GitHub-form fallback")


def test_reviews_listing() -> None:
    gh = FakeGitHub()
    review.file_review(session_for("jane@irrationallabs.com"), GOOD_REVIEW, gh, FakeSupabase())
    review.file_review(session_for("amy@agency.fund"), dict(GOOD_REVIEW, skill="select-messenger", verdict="ready"), gh, FakeSupabase())
    gh.issues[0].update(state="closed", state_reason="completed", labels=gh.issues[0]["labels"] + [{"name": "review:addressed"}])
    gh.issues.append({"number": 999, "body": "Just a question", "labels": [{"name": "expert-review"}], "html_url": "", "user": {"login": "x"}})
    out = reviews.collect(gh.list_issues(R.LABEL))
    ok(set(out) == {"define-key-behavior", "select-messenger"}, "reviews grouped by skill; unparseable issues skipped")
    first = out["define-key-behavior"][0]
    ok(first["state"] == "closed" and first["labels"] == ["review:addressed"] and first["name"] == "Jane Doe", "state, review:* labels, reviewer")
    ok(first["verdict_label"] == "Needs substantial revision" and "**" not in first["excerpt"], "verdict label and plain excerpt")


def test_http_round_trip() -> None:
    """Run auth.handler on a local port: GET, a cross-origin POST, and sign-in from the site."""
    os.environ["SITE_URL"] = "https://skills.example.org"
    os.environ["VERCEL_ENV"] = "production"
    c.verify_google_credential = fake_verify
    server = ThreadingHTTPServer(("127.0.0.1", 0), auth.handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_address[1]}"

    def call(method: str, origin: str = "", body=None, cookie: str = ""):
        req = urllib.request.Request(base + "/api/auth", method=method, data=json.dumps(body).encode() if body is not None else None)
        req.add_header("Content-Type", "application/json")
        if origin:
            req.add_header("Origin", origin)
        if cookie:
            req.add_header("Cookie", cookie)
        try:
            with urllib.request.urlopen(req, timeout=5) as resp:
                return resp.status, json.loads(resp.read()), resp.headers
        except urllib.error.HTTPError as exc:
            return exc.code, json.loads(exc.read() or b"{}"), exc.headers

    try:
        status, payload, _ = call("GET")
        ok(status == 200 and payload == {"signed_in": False}, "GET /api/auth signed out")
        ok(call("POST", "https://evil.example", {"credential": "fake:a@agency.fund"})[0] == 403, "POST from another origin: 403")
        ok(call("POST", "http://localhost:3000", {"credential": "fake:a@agency.fund"})[0] == 403, "localhost refused in production")
        status, payload, headers = call("POST", "https://skills.example.org", {"credential": "fake:a@agency.fund", "purpose": "review"})
        cookie = headers.get("Set-Cookie", "").split(";")[0]
        ok(status == 200 and payload["can_review"] and cookie.startswith("besci_session="), "POST from the site signs in and sets the cookie")
        status, payload, _ = call("GET", cookie=cookie)
        ok(payload.get("signed_in") and payload["email"] == "a@agency.fund", "GET with the cookie shows who is signed in")
        status, _, headers = call("DELETE", "https://skills.example.org", cookie=cookie)
        ok(status == 200 and "Max-Age=0" in headers.get("Set-Cookie", ""), "DELETE signs out")
    finally:
        server.shutdown()
        os.environ.pop("SITE_URL")
        os.environ.pop("VERCEL_ENV")


def main() -> int:
    c.verify_google_credential = fake_verify
    test_policy()
    test_sessions()
    test_issue_format()
    test_changelog_refs()
    test_browser_and_form_match()
    test_auth()
    test_review()
    test_reviews_listing()
    test_http_round_trip()
    print(f"\n{checks} checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
