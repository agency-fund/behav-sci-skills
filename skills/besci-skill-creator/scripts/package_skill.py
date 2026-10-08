#!/usr/bin/env python3
"""
package_skill.py — zip one skill folder into <name>.skill for Claude Desktop / claude.ai upload.

Usage:
  python package_skill.py path/to/skill-folder [--out DIR]

A .skill file is a plain zip whose single top-level folder is the skill folder.
Excludes __pycache__, .DS_Store, hidden files, and *-workspace directories.
No dependencies beyond the standard library.
"""
import argparse
import os
import sys
import zipfile

SKIP_DIRS = {"__pycache__", ".git"}


def should_skip(rel: str) -> bool:
    parts = rel.split(os.sep)
    if any(p in SKIP_DIRS or p.startswith(".") or p.endswith("-workspace") for p in parts):
        return True
    return False


def package(folder: str, out_dir: str) -> str:
    folder = os.path.abspath(folder.rstrip("/"))
    name = os.path.basename(folder)
    if not os.path.exists(os.path.join(folder, "SKILL.md")):
        raise SystemExit(f"{folder} has no SKILL.md")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{name}.skill")
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(folder):
            dirs[:] = [d for d in dirs if not should_skip(os.path.relpath(os.path.join(root, d), folder))]
            for f in sorted(files):
                full = os.path.join(root, f)
                rel = os.path.relpath(full, folder)
                if should_skip(rel):
                    continue
                zf.write(full, os.path.join(name, rel))
    return out_path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--out", default=".", help="Output directory (default: current directory)")
    args = ap.parse_args()
    path = package(args.folder, args.out)
    print(f"Wrote {path} ({os.path.getsize(path) // 1024} KB)")
    print("Upload it in Claude: Settings > Capabilities > Skills > Upload skill.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
