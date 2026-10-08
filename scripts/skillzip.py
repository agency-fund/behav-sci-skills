#!/usr/bin/env python3
"""
skillzip.py — safe extraction of a `.skill` (zip) archive into a skill folder.

Shared by api/submit.py (website upload), scripts/unpack_inbox.py (GitHub web
upload into inbox/), and scripts/test_submit.py. One implementation so the
three paths accept exactly the same archives.

Rules enforced:
  - archive at most MAX_ARCHIVE_BYTES; at most MAX_FILES entries;
    extracted total at most MAX_EXTRACTED_BYTES
  - no absolute paths, no "..", no symlinks, no device/special entries
  - __MACOSX/ and .DS_Store are ignored
  - exactly one top-level folder, and it must contain SKILL.md

Dependencies: standard library only. Python 3.8+.
"""
from __future__ import annotations

import os
import posixpath
import stat
import zipfile
from dataclasses import dataclass
from typing import List, Optional

MAX_ARCHIVE_BYTES = 10 * 1024 * 1024
MAX_EXTRACTED_BYTES = 10 * 1024 * 1024
MAX_FILES = 200
IGNORED_PARTS = {"__MACOSX", ".DS_Store", "__pycache__", "Thumbs.db"}


class SkillZipError(ValueError):
    """Raised for any archive the library refuses. The message is safe to show to the submitter."""


@dataclass
class UnpackResult:
    skill_name: str
    skill_dir: str
    files: List[str]


def _clean_member_name(name: str) -> Optional[str]:
    """Return a normalized, safe relative path or None if the entry should be skipped."""
    name = name.replace("\\", "/")
    if not name or name.endswith("/"):
        return None
    parts = [p for p in name.split("/") if p not in ("", ".")]
    if not parts:
        return None
    if any(p in IGNORED_PARTS for p in parts):
        return None
    if any(p.startswith("._") for p in parts):  # AppleDouble resource forks
        return None
    return "/".join(parts)


def _reject_if_unsafe(info: zipfile.ZipInfo, cleaned: str) -> None:
    raw = info.filename.replace("\\", "/")
    if raw.startswith("/") or (len(raw) > 1 and raw[1] == ":"):
        raise SkillZipError(f"Archive entry uses an absolute path: {raw}")
    if ".." in raw.split("/"):
        raise SkillZipError(f"Archive entry tries to escape its folder: {raw}")
    mode = (info.external_attr >> 16) & 0xFFFF
    fmt = stat.S_IFMT(mode)  # zero when the archiver stored no file-type bits
    if fmt == stat.S_IFLNK:
        raise SkillZipError(f"Archive contains a symbolic link, which is not allowed: {raw}")
    if fmt not in (0, stat.S_IFREG, stat.S_IFDIR):
        raise SkillZipError(f"Archive contains a special file, which is not allowed: {raw}")
    if posixpath.normpath(cleaned) != cleaned:
        raise SkillZipError(f"Archive entry has an unusual path: {raw}")


def inspect_archive(archive_path: str) -> str:
    """Validate the archive without extracting. Returns the single top-level folder name."""
    size = os.path.getsize(archive_path)
    if size > MAX_ARCHIVE_BYTES:
        raise SkillZipError(f"Archive is {size // 1024} KB; the limit is {MAX_ARCHIVE_BYTES // 1024} KB.")
    if not zipfile.is_zipfile(archive_path):
        raise SkillZipError("File is not a zip archive. A .skill file is a zip of the skill folder.")
    with zipfile.ZipFile(archive_path) as zf:
        members = zf.infolist()
        if len(members) > MAX_FILES:
            raise SkillZipError(f"Archive has {len(members)} entries; the limit is {MAX_FILES}.")
        total = 0
        tops = set()
        has_skill_md = False
        for info in members:
            cleaned = _clean_member_name(info.filename)
            if cleaned is None:
                continue
            _reject_if_unsafe(info, cleaned)
            total += info.file_size
            if total > MAX_EXTRACTED_BYTES:
                raise SkillZipError(f"Archive expands past {MAX_EXTRACTED_BYTES // 1024} KB.")
            parts = cleaned.split("/")
            tops.add(parts[0])
            if len(parts) == 2 and parts[1] == "SKILL.md":
                has_skill_md = True
            if len(parts) == 1:
                raise SkillZipError(
                    f"'{cleaned}' sits at the top of the archive. Zip the skill FOLDER, so the archive "
                    "contains one folder named after the skill with SKILL.md inside it."
                )
        if not tops:
            raise SkillZipError("Archive is empty.")
        if len(tops) > 1:
            raise SkillZipError(
                f"Archive must contain exactly one top-level folder, found {len(tops)}: {sorted(tops)}."
            )
        if not has_skill_md:
            raise SkillZipError("The top-level folder has no SKILL.md.")
        top = next(iter(tops))
        return top


def unpack_archive(archive_path: str, dest_root: str) -> UnpackResult:
    """Extract the single skill folder into dest_root/<skill_name>/. dest_root must exist."""
    top = inspect_archive(archive_path)
    dest_root = os.path.abspath(dest_root)
    skill_dir = os.path.join(dest_root, top)
    if os.path.exists(skill_dir):
        raise SkillZipError(f"A folder named '{top}' already exists at the destination.")
    written: List[str] = []
    with zipfile.ZipFile(archive_path) as zf:
        for info in zf.infolist():
            cleaned = _clean_member_name(info.filename)
            if cleaned is None:
                continue
            target = os.path.join(dest_root, *cleaned.split("/"))
            if not os.path.abspath(target).startswith(skill_dir + os.sep):
                raise SkillZipError(f"Archive entry resolves outside the skill folder: {info.filename}")
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with zf.open(info) as src, open(target, "wb") as dst:
                dst.write(src.read())
            written.append(os.path.relpath(target, skill_dir))
    written.sort()
    return UnpackResult(skill_name=top, skill_dir=skill_dir, files=written)


def pack_folder(folder: str, archive_path: str) -> List[str]:
    """Zip a skill folder so the folder itself is the single top-level entry. Returns the member list."""
    folder = os.path.abspath(folder.rstrip(os.sep))
    top = os.path.basename(folder)
    members: List[str] = []
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(folder):
            dirs[:] = sorted(d for d in dirs if d not in IGNORED_PARTS and not d.endswith("-workspace"))
            for f in sorted(files):
                if f in IGNORED_PARTS or f.endswith(".pyc"):
                    continue
                full = os.path.join(root, f)
                rel = os.path.relpath(full, folder)
                arcname = posixpath.join(top, rel.replace(os.sep, "/"))
                zf.write(full, arcname)
                members.append(arcname)
    return members
