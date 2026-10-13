"""
api/ratings.py: star ratings and public comments on skills.

  GET    ?skill=<name>          public summary and comments (CDN-cached for a minute)
  GET    ?skill=<name>&mine=1   the signed-in person's own rating (not cached)
  GET    ?skill=<name>&admin=1  for admins: the same list, plus hidden comments (not cached)
  POST   {"skill", "stars", "comment", "anonymous"}   rate a skill, or change your rating
  DELETE {"skill"}              remove your own rating
  DELETE {"id"}                 admins: delete any rating
  PATCH  {"id", "hidden"}       admins: hide or show a comment

Anyone signed in with Google may rate (api/auth.py), once per skill; rating
again replaces the old rating. "anonymous" hides the name on the site, but the
database keeps who posted, so maintainers can stop duplicates and abuse. A
hidden comment leaves the page but its stars still count; deleting removes both.
"""
from __future__ import annotations

import os
import sys
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402
import _review_issue as R  # noqa: E402

MAX_COMMENT = 2000
PER_DAY = 30
PUBLIC_CACHE = "public, max-age=0, s-maxage=60, stale-while-revalidate=300"
BADGES = {"TAF": "TAF staff", "IL": "IL staff"}


def ensure_user(db, session: Dict) -> Optional[int]:
    """The person's row id. Looked up by Google account, not trusted from the cookie."""
    rows = db.select("besci_users", {"google_sub": f"eq.{session['sub']}", "select": "id"})
    if rows:
        return rows[0]["id"]
    uid, _ = c.record_sign_in(db, {"sub": session["sub"], "email": session["email"], "name": session.get("name", "")})
    return uid


def entry(row: Dict, with_hidden: bool = False) -> Dict:
    anon = bool(row.get("anonymous"))
    out = {
        "id": row["id"],
        "stars": int(row["stars"]),
        "comment": row.get("comment") or "",
        "name": "Anonymous" if anon else (row.get("display_name") or "A reader"),
        "badge": "" if anon else BADGES.get(row.get("org") or "", ""),
        "version": row.get("skill_version", ""),
        "date": row.get("updated_at") or row.get("created_at") or "",
    }
    if with_hidden:
        out["hidden"] = bool(row.get("hidden"))
    return out


def summarize(rows: List[Dict], with_hidden: bool = False) -> Dict:
    """Average, count, and distribution over every rating; comments newest first."""
    dist = {str(i): 0 for i in range(1, 6)}
    for r in rows:
        dist[str(int(r["stars"]))] += 1
    count = len(rows)
    average = round(sum(int(r["stars"]) for r in rows) / count, 1) if count else None
    newest = sorted(rows, key=lambda r: str(r.get("updated_at") or r.get("created_at") or ""), reverse=True)
    comments = [entry(r, with_hidden) for r in newest
                if (r.get("comment") or "").strip() and (with_hidden or not r.get("hidden"))]
    return {"average": average, "count": count, "distribution": dist, "comments": comments}


def is_admin(session: Optional[Dict]) -> bool:
    return bool(session) and c.is_admin(session.get("email", ""), session.get("db_admin", False))


def get_ratings(query: Dict, session: Optional[Dict], db) -> Tuple[int, Dict, str]:
    """Returns (status, payload, Cache-Control)."""
    skill = query.get("skill", "")
    if not c.SKILL_NAME.match(skill):
        return 400, {"ok": False, "error": "Say which skill: ?skill=<name>."}, "no-store"
    if not db.configured:
        return 503, {"ok": False, "error": "Ratings aren't set up on this server yet."}, "no-store"
    if query.get("mine"):
        if not session:
            return 200, {"ok": True, "mine": None}, "private, no-store"
        rows = db.select("besci_users", {"google_sub": f"eq.{session['sub']}", "select": "id"})
        mine = None
        if rows:
            found = db.select("besci_ratings", {"skill": f"eq.{skill}", "user_id": f"eq.{rows[0]['id']}"})
            if found:
                r = found[0]
                mine = {"stars": int(r["stars"]), "comment": r.get("comment") or "", "anonymous": bool(r.get("anonymous")),
                        "version": r.get("skill_version", ""), "hidden": bool(r.get("hidden"))}
        return 200, {"ok": True, "mine": mine}, "private, no-store"
    rows = db.select("besci_ratings", {"skill": f"eq.{skill}"})
    if query.get("admin"):
        if not is_admin(session):
            return 403, {"ok": False, "error": "Only maintainers can see hidden comments."}, "no-store"
        return 200, dict(summarize(rows, with_hidden=True), ok=True, skill=skill), "private, no-store"
    return 200, dict(summarize(rows), ok=True, skill=skill), PUBLIC_CACHE


def save_rating(session: Optional[Dict], data: Dict, db) -> Tuple[int, Dict]:
    if not session:
        return 401, {"ok": False, "error": "Sign in to rate."}
    if not db.configured:
        return 503, {"ok": False, "error": "Ratings aren't set up on this server yet."}
    info = c.skill_info(str(data.get("skill", "")))
    if not info:
        return 400, {"ok": False, "error": "There is no skill by that name."}
    stars = data.get("stars")
    if isinstance(stars, bool) or not isinstance(stars, int) or not 1 <= stars <= 5:
        return 400, {"ok": False, "error": "Choose from one to five stars."}
    comment = str(data.get("comment") or "").strip()
    if len(comment) > MAX_COMMENT:
        return 400, {"ok": False, "error": f"Comments are limited to {MAX_COMMENT:,} characters."}
    anonymous = bool(data.get("anonymous"))
    try:
        uid = ensure_user(db, session)
        since = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
        recent = db.select("besci_events", {"name": "eq.rating_saved", "user_id": f"eq.{uid}", "created_at": f"gte.{since}",
                                            "select": "id", "limit": str(PER_DAY)})
        if len(recent) >= PER_DAY:
            return 429, {"ok": False, "error": "That's a lot of ratings for one day. Try again tomorrow."}
        code, _ = c.org_for(session["email"])
        row = db.upsert("besci_ratings", {
            "user_id": uid, "skill": info["name"], "skill_version": info["version"], "stars": stars,
            "comment": comment or None, "anonymous": anonymous, "display_name": R.clean_line(session.get("name", "")),
            "org": code, "updated_at": c.now_iso(),
        }, on_conflict="skill,user_id")
    except RuntimeError as exc:
        sys.stderr.write(f"ratings: {exc}\n")
        return 502, {"ok": False, "error": "The rating couldn't be saved. Please try again in a minute."}
    c.log_event(db, "rating_saved", uid, info["name"], {"stars": stars, "anonymous": anonymous, "comment": bool(comment)})
    return 200, {"ok": True, "rating": entry(row) if row else None}


def delete_rating(session: Optional[Dict], data: Dict, db) -> Tuple[int, Dict]:
    if not session:
        return 401, {"ok": False, "error": "Sign in first."}
    if not db.configured:
        return 503, {"ok": False, "error": "Ratings aren't set up on this server yet."}
    if data.get("id") is not None:
        if not is_admin(session):
            return 403, {"ok": False, "error": "Only maintainers can delete other people's ratings."}
        try:
            rid = int(data["id"])
        except (TypeError, ValueError):
            return 400, {"ok": False, "error": "Say which rating."}
        db.delete("besci_ratings", {"id": f"eq.{rid}"})
        c.log_event(db, "rating_deleted", None, "", {"id": rid, "by_admin": True})
        return 200, {"ok": True}
    skill = str(data.get("skill", ""))
    if not c.SKILL_NAME.match(skill):
        return 400, {"ok": False, "error": "Say which skill."}
    uid = ensure_user(db, session)
    db.delete("besci_ratings", {"skill": f"eq.{skill}", "user_id": f"eq.{uid}"})
    return 200, {"ok": True}


def moderate(session: Optional[Dict], data: Dict, db) -> Tuple[int, Dict]:
    if not is_admin(session):
        return 403, {"ok": False, "error": "Only maintainers can hide comments."}
    if not db.configured:
        return 503, {"ok": False, "error": "Ratings aren't set up on this server yet."}
    try:
        rid = int(data.get("id"))
    except (TypeError, ValueError):
        return 400, {"ok": False, "error": "Say which rating."}
    hidden = bool(data.get("hidden"))
    if not db.update("besci_ratings", {"id": f"eq.{rid}"}, {"hidden": hidden}):
        return 404, {"ok": False, "error": "No such rating."}
    c.log_event(db, "rating_hidden" if hidden else "rating_shown", None, "", {"id": rid})
    return 200, {"ok": True, "id": rid, "hidden": hidden}


class handler(c.JSONHandler):  # noqa: N801 (Vercel requires this name)
    log_name = "ratings"

    def do_GET(self) -> None:  # noqa: N802
        try:
            status, payload, cache = get_ratings(self.query(), self.session(), c.Supabase())
        except RuntimeError:
            status, payload, cache = 502, {"ok": False, "error": "Ratings are unavailable right now."}, "no-store"
        self.send_json(status, payload, cache=cache)

    def _write(self, fn) -> None:
        if not self.write_allowed():
            return
        try:
            data = self.read_json()
        except ValueError as exc:
            self.send_json(400, {"ok": False, "error": str(exc)})
            return
        try:
            status, payload = fn(self.session(), data, c.Supabase())
        except RuntimeError:
            status, payload = 502, {"ok": False, "error": "The database didn't answer. Please try again in a minute."}
        self.send_json(status, payload)

    def do_POST(self) -> None:  # noqa: N802
        self._write(save_rating)

    def do_DELETE(self) -> None:  # noqa: N802
        self._write(delete_rating)

    def do_PATCH(self) -> None:  # noqa: N802
        self._write(moderate)
