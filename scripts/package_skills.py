#!/usr/bin/env python3
"""
package_skills.py — build downloadable .skill archives for every skill.

Writes to dist/ (git-ignored):
  dist/<name>.skill                 one zip per skill, the skill folder at the top level
  dist/behav-sci-skills-all.skill   every skill folder in one zip
  dist/manifest.json                name, version, sha256, size for each archive

A .skill file is a plain zip; Claude Desktop and claude.ai accept it as an upload.
CI runs this on every PR (to prove packaging works) and the release workflow
attaches the output to a GitHub Release.

Usage: uv run scripts/package_skills.py [--out dist] [--skills skills]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import zipfile
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import besci_validate as bv  # noqa: E402
import skillzip  # noqa: E402


def sha256_of(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Package skills into .skill zip archives.")
    ap.add_argument("--out", default=os.path.join(ROOT, "dist"))
    ap.add_argument("--skills", default=os.path.join(ROOT, "skills"))
    args = ap.parse_args(argv)

    folders = bv.discover_skills(args.skills)
    if not folders:
        print(f"No skills found under {args.skills}", file=sys.stderr)
        return 2
    os.makedirs(args.out, exist_ok=True)
    taxonomy = bv.load_taxonomy(os.path.join(ROOT, "taxonomy.yaml"))

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "skills": [],
    }
    all_path = os.path.join(args.out, "behav-sci-skills-all.skill")
    with zipfile.ZipFile(all_path, "w", zipfile.ZIP_DEFLATED) as bundle:
        for folder in folders:
            skill = bv.parse_skill(folder)
            name = skill.name or os.path.basename(folder)
            out = os.path.join(args.out, f"{name}.skill")
            members = skillzip.pack_folder(folder, out)
            # Verify exactly one top-level folder.
            tops = {m.split("/")[0] for m in members}
            if tops != {name}:
                print(f"{name}: archive top-level entries are {sorted(tops)}, expected only '{name}'", file=sys.stderr)
                return 1
            # Add the same files to the bundle.
            with zipfile.ZipFile(out) as zf:
                for info in zf.infolist():
                    bundle.writestr(info, zf.read(info))
            size = os.path.getsize(out)
            manifest["skills"].append({
                "name": name,
                "version": str(skill.metadata.get("version", "")),
                "status": str(skill.metadata.get("status", "")),
                "file": os.path.basename(out),
                "size": size,
                "sha256": sha256_of(out),
                "files": len(members),
                "structure_ok": not bv.validate_skill(skill, taxonomy).errors,
            })
            print(f"packed {name} -> {os.path.relpath(out, ROOT)} ({size} bytes, {len(members)} files)")

    manifest["bundle"] = {
        "file": os.path.basename(all_path),
        "size": os.path.getsize(all_path),
        "sha256": sha256_of(all_path),
    }
    with open(os.path.join(args.out, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)
    print(f"wrote {os.path.relpath(all_path, ROOT)} and manifest.json ({len(manifest['skills'])} skills)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
