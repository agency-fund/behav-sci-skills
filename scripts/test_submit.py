#!/usr/bin/env python3
"""
test_submit.py — local checks for the upload path, without touching GitHub.

Covers: packing the seed skill into a .skill, unpacking it safely, running the
validator on the unpacked folder, building the git tree payload, parsing a
multipart form, the contributor-key gate, and rejection of hostile archives.

Run: uv run python scripts/test_submit.py
"""
from __future__ import annotations

import io
import os
import sys
import tempfile
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "api"))
sys.path.insert(0, ROOT)

import besci_validate as bv  # noqa: E402
import skillzip  # noqa: E402

os.environ.setdefault("CONTRIBUTOR_KEY", "test-key-123")
import submit  # noqa: E402  (api/submit.py)

SEED = os.path.join(ROOT, "skills", "draft-cognitive-interview-script")
checks = 0


def ok(cond: bool, msg: str) -> None:
    global checks
    checks += 1
    if not cond:
        print(f"FAIL: {msg}")
        sys.exit(1)
    print(f"ok   {msg}")


def multipart(fields: dict, filename: str, data: bytes) -> tuple:
    boundary = "----besciTestBoundary"
    buf = io.BytesIO()
    for k, v in fields.items():
        buf.write(f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode())
    buf.write(f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{filename}\"\r\nContent-Type: application/zip\r\n\r\n".encode())
    buf.write(data)
    buf.write(f"\r\n--{boundary}--\r\n".encode())
    return f"multipart/form-data; boundary={boundary}", buf.getvalue()


def main() -> int:
    assert os.path.isdir(SEED), "seed skill folder missing"
    with tempfile.TemporaryDirectory() as tmp:
        # 1. pack -> unpack round trip
        archive = os.path.join(tmp, "seed.skill")
        members = skillzip.pack_folder(SEED, archive)
        ok(all(m.startswith("draft-cognitive-interview-script/") for m in members), "packed archive has the folder at top level")
        dest = os.path.join(tmp, "out")
        os.makedirs(dest)
        res = skillzip.unpack_archive(archive, dest)
        ok(res.skill_name == "draft-cognitive-interview-script", "unpacked folder name matches")
        ok("SKILL.md" in res.files and "evals/evals.json" in res.files, "unpacked files include SKILL.md and evals")

        # 2. validator on unpacked folder
        skill = bv.validate_skill(bv.parse_skill(res.skill_dir), bv.load_taxonomy(os.path.join(ROOT, "taxonomy.yaml")))
        ok(not skill.errors, f"validator passes on unpacked seed ({len(skill.warnings)} warning(s))")

        # 3. tree payload
        entries = submit.build_tree_entries(res.skill_dir, skill.name)
        paths = {e["path"] for e in entries}
        ok(f"skills/{skill.name}/SKILL.md" in paths, "tree payload contains SKILL.md at skills/<name>/")
        ok(all(e["mode"] == "100644" and e["type"] == "blob" for e in entries), "tree entries are regular blobs")
        ok(all("content" in e for e in entries), "seed skill files are all text blobs")

        # 4. unpack_and_validate via submit's own helper
        with open(archive, "rb") as fh:
            data = fh.read()
        wd = os.path.join(tmp, "wd")
        os.makedirs(wd)
        s2, r2 = submit.unpack_and_validate(data, wd)
        ok(not s2.errors, "submit.unpack_and_validate passes on the seed archive")
        body = submit.pr_body(s2, {"author_name": "Test Person", "author_github": "tester", "org": "TAF"}, bv.report_text([s2]))
        ok("Reviewer checklist" in body and "Disclosure acknowledged: yes." in body, "PR body carries checklist and disclosure line")
        ok(submit.branch_name_for("x-y").startswith("submit/x-y-"), "branch name format")

        # 5. multipart + gate (no GitHub call: wrong key short-circuits before any network)
        ct, raw = multipart({"contributor_key": "wrong", "author_name": "T", "org": "TAF", "disclosure_ack": "yes"}, "seed.skill", data)
        status, payload = submit.handle_submission(ct, raw)
        ok(status == 401 and not payload["ok"], "wrong contributor key -> 401")
        fields, upload = submit.parse_multipart(ct, raw)
        ok(fields["org"] == "TAF" and upload and upload[0] == "seed.skill" and upload[1] == data, "multipart parse recovers fields and file bytes")
        ok(submit.check_contributor_key("test-key-123") and not submit.check_contributor_key(""), "contributor key compare")

        # 6. right key but GITHUB_TOKEN unset -> validation passes, PR step fails cleanly with 502
        os.environ.pop("GITHUB_TOKEN", None)
        ct, raw = multipart({"contributor_key": "test-key-123", "author_name": "T", "org": "TAF", "disclosure_ack": "yes"}, "seed.skill", data)
        status, payload = submit.handle_submission(ct, raw)
        ok(status == 502 and "GITHUB_TOKEN" in payload["error"] and "Structure OK" in payload.get("report", ""), "valid archive without token -> 502 with report (no GitHub call made)")

        # 7. hostile archives are rejected
        bad = os.path.join(tmp, "bad.skill")
        with zipfile.ZipFile(bad, "w") as zf:
            zf.writestr("../evil/SKILL.md", "x")
        try:
            skillzip.inspect_archive(bad)
            ok(False, "path traversal rejected")
        except skillzip.SkillZipError:
            ok(True, "path traversal rejected")
        flat = os.path.join(tmp, "flat.skill")
        with zipfile.ZipFile(flat, "w") as zf:
            zf.writestr("SKILL.md", "x")
        try:
            skillzip.inspect_archive(flat)
            ok(False, "flat archive (no folder) rejected")
        except skillzip.SkillZipError as exc:
            ok("Zip the skill FOLDER" in str(exc), "flat archive (no folder) rejected with helpful message")
        two = os.path.join(tmp, "two.skill")
        with zipfile.ZipFile(two, "w") as zf:
            zf.writestr("a/SKILL.md", "x")
            zf.writestr("b/SKILL.md", "x")
        try:
            skillzip.inspect_archive(two)
            ok(False, "two top-level folders rejected")
        except skillzip.SkillZipError:
            ok(True, "two top-level folders rejected")
        mac = os.path.join(tmp, "mac.skill")
        with zipfile.ZipFile(mac, "w") as zf:
            zf.writestr("__MACOSX/._x", "x")
            zf.writestr("good/.DS_Store", "x")
            zf.writestr("good/SKILL.md", "x")
        ok(skillzip.inspect_archive(mac) == "good", "__MACOSX and .DS_Store are ignored")
        # a non-skill archive that passes zip checks but fails validation -> 422 from handle_submission
        with open(mac, "rb") as fh:
            macdata = fh.read()
        ct, raw = multipart({"contributor_key": "test-key-123", "author_name": "T", "org": "IL", "disclosure_ack": "yes"}, "mac.skill", macdata)
        status, payload = submit.handle_submission(ct, raw)
        ok(status == 422 and payload["error"] == "Validation failed" and "E002" in payload["report"], "structurally bad skill -> 422 with validator report")

    print(f"\n{checks} checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
