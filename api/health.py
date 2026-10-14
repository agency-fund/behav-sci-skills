"""
api/health.py: a cheap check that the database answers.

  GET -> {"ok": true, "db": true}

.github/workflows/keepalive.yml calls this every few days. Supabase pauses
free-plan projects after about a week without requests, and a paused project
would break sign-in records and ratings until someone restores it by hand.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402


class handler(c.JSONHandler):  # noqa: N801 (Vercel requires this name)
    log_name = "health"

    def do_GET(self) -> None:  # noqa: N802
        db = c.Supabase()
        if not db.configured:
            self.send_json(200, {"ok": True, "db": False})
            return
        try:
            db.select("besci_users", {"select": "id", "limit": "1"})
        except Exception:  # noqa: BLE001
            self.send_json(503, {"ok": False, "db": False})
            return
        self.send_json(200, {"ok": True, "db": True})
