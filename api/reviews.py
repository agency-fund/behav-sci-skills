"""
api/reviews.py: every expert review, grouped by skill, for the skill pages.

  GET -> {"ok": true, "generated_at": "...", "skills": {"<skill>": [review, ...]}}

Reads all issues labeled expert-review (open and closed) and groups them by the
"Skill" field of the body, so reviews filed by hand on GitHub show up too. One
response serves every skill page, and Vercel's CDN caches it for two minutes.
Each review carries its issue's state and review:* labels; the page works out
"answered in vX" from the skill's CHANGELOG.
"""
from __future__ import annotations

import os
import sys
from typing import Dict, List

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402
import _review_issue as R  # noqa: E402

CACHE = "public, max-age=0, s-maxage=120, stale-while-revalidate=600"


def collect(issues: List[dict]) -> Dict[str, List[dict]]:
    skills: Dict[str, List[dict]] = {}
    for issue in issues:
        r = R.parse(issue.get("body") or "")
        if not r:
            continue
        skills.setdefault(r["skill"], []).append({
            "number": issue.get("number"),
            "url": issue.get("html_url", ""),
            "state": issue.get("state", "open"),
            "state_reason": issue.get("state_reason") or "",
            "created_at": issue.get("created_at", ""),
            "closed_at": issue.get("closed_at") or "",
            "comments": issue.get("comments", 0),
            "labels": [lb["name"] for lb in issue.get("labels", []) if lb.get("name", "").startswith("review:")],
            "name": r["name"] or (issue.get("user") or {}).get("login", ""),
            "org": r["org"],
            "org_name": r["org_name"],
            "version": r["version"],
            "verdict": r["verdict"],
            "verdict_label": R.VERDICTS.get(r["verdict"], ""),
            "parts": r["parts"],
            "excerpt": R.excerpt(r["review"]),
        })
    return skills


class handler(c.JSONHandler):  # noqa: N801 (Vercel requires this name)
    log_name = "reviews"

    def do_GET(self) -> None:  # noqa: N802
        try:
            issues = c.github_from_env().list_issues(R.LABEL)
        except RuntimeError as exc:
            self.send_json(502, {"ok": False, "error": str(exc)})
            return
        self.send_json(200, {"ok": True, "generated_at": c.now_iso(), "skills": collect(issues)}, cache=CACHE)
