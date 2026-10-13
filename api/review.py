"""
api/review.py: file an expert review as a GitHub issue.

  POST {"skill", "verdict", "parts", "review", "evidence", "name", "github", "commit"}

The reviewer must be signed in (api/auth.py) with an address that may review
(REVIEW_DOMAINS or REVIEWER_EMAILS). The issue is opened with the server's
GITHUB_TOKEN, so reviewers need no GitHub account; the body names them, and an
optional GitHub username @mentions them so they hear about replies. Title,
labels, and body come from api/_review_issue.py. Returns {"ok", "number", "url"}.
"""
from __future__ import annotations

import os
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402
import _review_issue as R  # noqa: E402

MAX_REVIEW = 20000
MAX_EVIDENCE = 5000
MIN_REVIEW = 20
PER_DAY = 10
_recent: Dict[str, List[float]] = {}  # fallback limiter when there is no database


def _over_limit(db, uid: Optional[int], email: str) -> bool:
    if db.configured and uid:
        since = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
        rows = db.select("besci_expert_reviews", {"user_id": f"eq.{uid}", "created_at": f"gte.{since}", "select": "id", "limit": str(PER_DAY)})
        return len(rows) >= PER_DAY
    now = time.time()
    times = [t for t in _recent.get(email, []) if now - t < 86400]
    _recent[email] = times
    return len(times) >= PER_DAY


def validate(data: Dict) -> Tuple[Optional[str], Dict]:
    """(error message or None, cleaned fields)."""
    verdict = str(data.get("verdict", ""))
    if verdict not in R.VERDICTS:
        return "Choose a verdict.", {}
    parts = data.get("parts") or []
    if not isinstance(parts, list):
        return "Parts must be a list.", {}
    review = str(data.get("review", "")).strip()
    if len(review) < MIN_REVIEW:
        return "The review is too short. Say what works, what doesn't, and what you'd change.", {}
    if len(review) > MAX_REVIEW:
        return f"The review is longer than {MAX_REVIEW:,} characters. Put the rest in a comment on the issue once it's filed.", {}
    evidence = str(data.get("evidence", "")).strip()
    if len(evidence) > MAX_EVIDENCE:
        return f"Evidence or sources is longer than {MAX_EVIDENCE:,} characters.", {}
    github = str(data.get("github", "")).strip().lstrip("@")
    if github and not R.GITHUB_USER.match(github):
        return "That isn't a valid GitHub username. Leave it blank if you don't have one.", {}
    commit = os.environ.get("VERCEL_GIT_COMMIT_SHA", "") or str(data.get("commit", ""))
    return None, {
        "verdict": verdict,
        "parts": [p for p in R.PARTS if p in parts],
        "review": review,
        "evidence": evidence,
        "github": github,
        "commit": commit if re.match(r"^[0-9a-f]{7,40}$", commit) else "",
    }


def file_review(session: Optional[Dict], data: Dict, gh=None, db=None) -> Tuple[int, Dict]:
    """Everything after the HTTP layer. Returns (status, payload)."""
    if not session:
        return 401, {"ok": False, "error": "Sign in first."}
    email = session.get("email", "")
    if not c.can_review(email):
        return 403, {"ok": False, "error": "Expert reviews are limited to staff at The Agency Fund and Irrational Labs for now."}
    info = c.skill_info(str(data.get("skill", "")))
    if not info:
        return 400, {"ok": False, "error": "There is no skill by that name."}
    error, fields = validate(data)
    if error:
        return 400, {"ok": False, "error": error}
    name = R.clean_line(data.get("name") or session.get("name", ""))
    if not name:
        return 400, {"ok": False, "error": "Add your name; it appears on the review."}

    db = db or c.Supabase()
    uid = session.get("uid")
    try:
        if _over_limit(db, uid, email):
            return 429, {"ok": False, "error": f"That's {PER_DAY} reviews in a day, the most the site files per person. Try again tomorrow, or post on GitHub."}
    except RuntimeError:
        pass  # the database being down shouldn't block a review

    try:
        gh = gh or c.github_from_env()
    except RuntimeError as exc:
        return 502, {"ok": False, "error": str(exc), "fallback": True}
    code, org_name = c.org_for(email)
    record = dict(fields, skill=info["name"], version=info["version"], repo=gh.repo, name=name,
                  org=code, org_name=org_name, submitted=c.now_iso())
    labels = R.labels(info["name"], info["stage"], fields["verdict"], code)
    for label in labels:
        try:
            gh.ensure_label(label, *R.label_color(label))
        except Exception:  # noqa: BLE001 (labels are a convenience; the issue matters)
            pass
    try:
        issue = gh.create_issue(R.title(info["name"], info["version"], name, code), R.body(record), labels)
    except RuntimeError as exc:
        return 502, {"ok": False, "error": f"GitHub didn't accept the review: {exc}", "fallback": True}
    number = int(issue["number"])
    # Labels set at creation are dropped silently if the token's account lacks triage rights.
    if len(issue.get("labels") or []) < len(labels):
        try:
            gh.add_labels(number, labels)
        except Exception:  # noqa: BLE001
            pass
    if db.configured and uid:
        try:
            db.insert("besci_expert_reviews", {"user_id": uid, "skill": info["name"], "skill_version": info["version"],
                                               "verdict": fields["verdict"], "issue_number": number})
        except Exception:  # noqa: BLE001
            pass
    else:
        _recent.setdefault(email, []).append(time.time())
    c.log_event(db, "review_filed", uid, info["name"], {"issue": number, "verdict": fields["verdict"]})
    return 200, {"ok": True, "number": number, "url": issue.get("html_url", "")}


class handler(c.JSONHandler):  # noqa: N801 (Vercel requires this name)
    log_name = "review"

    def do_POST(self) -> None:  # noqa: N802
        if not self.write_allowed():
            return
        try:
            data = self.read_json()
        except ValueError as exc:
            self.send_json(400, {"ok": False, "error": str(exc)})
            return
        status, payload = file_review(self.session(), data)
        self.send_json(status, payload)

    def do_GET(self) -> None:  # noqa: N802
        self.send_json(405, {"ok": False, "error": "POST a review to this endpoint."})
