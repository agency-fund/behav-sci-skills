#!/usr/bin/env python3
"""
unpack_inbox.py — move .skill/.zip archives dropped in inbox/ into skills/<name>/.

Used by .github/workflows/inbox.yml on pull requests that touch inbox/.
Same safety rules as the website upload (scripts/skillzip.py). Prints a
plain-language summary and writes a machine-readable result to --result.

Exit 0 when every archive unpacked (or there was nothing to do), 1 when any
archive was rejected. The workflow commits the unpacked folders and removes
the archives it consumed.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import skillzip  # noqa: E402


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--inbox", default=os.path.join(ROOT, "inbox"))
    ap.add_argument("--skills", default=os.path.join(ROOT, "skills"))
    ap.add_argument("--result", default=None, help="Write JSON summary here.")
    args = ap.parse_args(argv)

    archives = sorted(
        f for f in os.listdir(args.inbox)
        if f.lower().endswith((".skill", ".zip")) and os.path.isfile(os.path.join(args.inbox, f))
    ) if os.path.isdir(args.inbox) else []

    summary = {"unpacked": [], "rejected": [], "removed": []}
    if not archives:
        print("inbox: nothing to unpack")
    for name in archives:
        path = os.path.join(args.inbox, name)
        try:
            res = skillzip.unpack_archive(path, args.skills)
        except skillzip.SkillZipError as exc:
            print(f"REJECTED {name}: {exc}")
            summary["rejected"].append({"archive": name, "reason": str(exc)})
            continue
        print(f"unpacked {name} -> skills/{res.skill_name}/ ({len(res.files)} files)")
        summary["unpacked"].append({"archive": name, "skill": res.skill_name, "files": res.files})
        os.remove(path)
        summary["removed"].append(name)

    if args.result:
        with open(args.result, "w", encoding="utf-8") as fh:
            json.dump(summary, fh, indent=2)
    return 1 if summary["rejected"] else 0


if __name__ == "__main__":
    sys.exit(main())
