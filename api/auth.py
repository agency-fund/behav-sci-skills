"""
api/auth.py: sign in with Google, see who is signed in, sign out.

  POST   {"credential": "<ID token from the Google button>", "purpose": "review" | "rate"}
         Checks the token, records the person in besci_users, sets the session cookie.
  GET    Who is signed in: {"signed_in": false} or their name, organization, and
         whether they may file expert reviews.
  DELETE Signs out.

Anyone with a Google account can sign in (ratings are open to all); whether they
may file an expert review is decided per request in api/_common.py.
"""
from __future__ import annotations

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

PURPOSES = {"review", "rate"}


def sign_in(credential: str, purpose: str, db=None) -> Tuple[int, dict, List[str]]:
    """Everything after the HTTP layer. Returns (status, payload, cookies to set)."""
    if not credential or not isinstance(credential, str):
        return 400, {"ok": False, "error": "No sign-in credential was sent."}, []
    try:
        claims = c.verify_google_credential(credential)
    except ValueError as exc:
        return 401, {"ok": False, "error": f"Sign-in failed: {exc}"}, []
    except Exception:  # noqa: BLE001 (google-auth raises several types; none should leak)
        return 401, {"ok": False, "error": "Sign-in failed. Please try again."}, []

    db = db or c.Supabase()
    uid, db_admin = None, False
    if db.configured:
        try:
            uid, db_admin = c.record_sign_in(db, claims)
        except Exception as exc:  # noqa: BLE001 (signing in still works; the record is for analytics)
            sys.stderr.write(f"auth: could not record sign-in: {type(exc).__name__}\n")
    session = {"sub": claims["sub"], "email": claims["email"],
               "name": claims.get("name") or claims["email"].split("@")[0], "uid": uid, "db_admin": db_admin}
    try:
        token = c.sign_session(session)
    except RuntimeError as exc:
        return 500, {"ok": False, "error": str(exc)}, []

    view = c.user_view(session)
    purpose = purpose if purpose in PURPOSES else ""
    c.log_event(db, "sign_in", uid, props={"can_review": view["can_review"], "purpose": purpose})
    if purpose == "review" and not view["can_review"]:
        c.log_event(db, "review_denied_domain", uid, props={"domain": c.email_domain(claims["email"])})
    return 200, dict(view, ok=True), [c.session_cookie(token)]


class handler(c.JSONHandler):  # noqa: N801 (Vercel requires this name)
    log_name = "auth"

    def do_GET(self) -> None:  # noqa: N802
        self.send_json(200, c.user_view(self.session()))

    def do_POST(self) -> None:  # noqa: N802
        if not self.write_allowed():
            return
        try:
            data = self.read_json()
        except ValueError as exc:
            self.send_json(400, {"ok": False, "error": str(exc)})
            return
        status, payload, cookies = sign_in(data.get("credential", ""), str(data.get("purpose", "")))
        self.send_json(status, payload, cookies=cookies)

    def do_DELETE(self) -> None:  # noqa: N802
        if not self.write_allowed():
            return
        self.send_json(200, {"ok": True, "signed_in": False}, cookies=[c.clear_cookie()])
