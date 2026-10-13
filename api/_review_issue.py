"""
api/_review_issue.py: the format of an expert-review GitHub issue.

One place defines the title, labels, and body of an expert review, and parses
them back. api/review.py renders issues with it; api/reviews.py parses them for
the skill pages; .github/ISSUE_TEMPLATE/expert-review.yml uses the same field
labels, so issues filed by hand on GitHub parse the same way.

The body is `### Field` sections in the layout GitHub issue forms produce, with a
machine-readable JSON comment at the end for AI agents and scripts. Pure
functions, standard library only (tested in scripts/test_feedback.py).
"""
from __future__ import annotations

import json
import re
from typing import Dict, List, Optional

TITLE_PREFIX = "[Expert review]"
LABEL = "expert-review"
JSON_MARK = "besci-review v1"

# key -> (label shown to reviewers, label suffix)
VERDICTS = {
    "ready": "Ready to publish",
    "small-changes": "Publish after small changes",
    "needs-revision": "Needs substantial revision",
    "not-suitable": "Not suitable for the library",
}

# The parts of a skill a review can concern: the eight SKILL.md sections, then the files.
PARTS = [
    "What it does", "When to use it", "Before you start", "What it draws on",
    "How to do it", "Output template", "Where it goes wrong", "When to bring in a specialist",
    "Test cases", "References", "Scripts", "Whole skill",
]

# (field id, heading). The ids match the issue form's field ids.
FIELDS = [
    ("skill", "Skill"),
    ("version", "Version reviewed"),
    ("content", "Content reviewed"),
    ("verdict", "Verdict"),
    ("parts", "Parts this concerns"),
    ("review", "Review"),
    ("evidence", "Evidence or sources"),
    ("reviewer", "Reviewer"),
    ("submitted", "Submitted"),
]
HEADING_TO_ID = {h.lower(): i for i, h in FIELDS}

# Fixed label colors, so labels the server creates look the same every time.
LABEL_COLORS = {
    LABEL: ("F1B505", "Expert review of a skill version, filed from the website or the expert-review form"),
    "verdict:ready": ("0E8A16", "Expert verdict: ready to publish"),
    "verdict:small-changes": ("C2E0C6", "Expert verdict: publish after small changes"),
    "verdict:needs-revision": ("E99695", "Expert verdict: needs substantial revision"),
    "verdict:not-suitable": ("B60205", "Expert verdict: not suitable for the library"),
}
PREFIX_COLORS = {"skill:": "C5DEF5", "stage:": "BFDADC", "org:": "EDEDED"}

SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
VERSION = re.compile(r"^\d+\.\d+\.\d+$")
GITHUB_USER = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9]|-(?=[A-Za-z0-9])){0,38}$")
NO_RESPONSE = "_No response_"


def label_color(name: str) -> tuple:
    if name in LABEL_COLORS:
        return LABEL_COLORS[name]
    for prefix, color in PREFIX_COLORS.items():
        if name.startswith(prefix):
            return color, ""
    return "EDEDED", ""


def clean_line(text: str, limit: int = 80) -> str:
    """One line of plain text for a title or name: no newlines, no @-mentions, trimmed."""
    text = " ".join(str(text or "").split()).replace("@", "")
    return text[:limit].strip()


def title(skill: str, version: str, name: str, org: str) -> str:
    return f"{TITLE_PREFIX} {skill} v{version} by {clean_line(name)} ({org})"


def labels(skill: str, stage: str, verdict: str, org: str) -> List[str]:
    out = [LABEL, f"skill:{skill}"]
    if stage:
        out.append(f"stage:{stage}")
    if verdict in VERDICTS:
        out.append(f"verdict:{verdict}")
    if org:
        out.append(f"org:{org}")
    return out


def body(r: Dict) -> str:
    """Render a review. r has skill, version, commit, repo, verdict (key), parts (list),
    review, evidence, name, org_name, org, github, submitted (ISO 8601 UTC)."""
    content = ""
    if r.get("commit") and r.get("repo"):
        content = f"https://github.com/{r['repo']}/blob/{r['commit']}/skills/{r['skill']}/SKILL.md"
    reviewer = f"{clean_line(r['name'])}, {r['org_name']}"
    if r.get("github"):
        reviewer += f" (@{r['github']})"
    values = {
        "skill": r["skill"],
        "version": r["version"],
        "content": content,
        "verdict": VERDICTS.get(r["verdict"], r["verdict"]),
        "parts": ", ".join(r.get("parts") or []),
        "review": str(r.get("review", "")).strip(),
        "evidence": str(r.get("evidence", "")).strip(),
        "reviewer": reviewer,
        "submitted": f"{r['submitted']} via the website, signed in with Google",
    }
    sections = [f"### {heading}\n\n{values[fid] or NO_RESPONSE}" for fid, heading in FIELDS]
    record = {
        "skill": r["skill"], "version": r["version"], "commit": r.get("commit") or "",
        "verdict": r["verdict"], "parts": list(r.get("parts") or []),
        "name": clean_line(r["name"]), "org": r["org"], "org_name": r["org_name"],
        "github": r.get("github") or "", "submitted": r["submitted"],
    }
    sections.append(f"<!-- {JSON_MARK} {json.dumps(record, separators=(',', ':'))} -->")
    return "\n\n".join(sections) + "\n"


def _verdict_key(text: str) -> str:
    t = text.strip().lower()
    for key, label in VERDICTS.items():
        if t in (key, label.lower()):
            return key
    return ""


def _parts(text: str) -> List[str]:
    if "- [" in text:  # an issue form's checkboxes: "- [X] How to do it"
        return [m.group(1).strip() for m in re.finditer(r"^- \[[xX]\] (.+)$", text, re.M)]
    return [p.strip() for p in text.split(",") if p.strip()]


def parse(text: str) -> Optional[Dict]:
    """Read an expert-review issue body back into fields. None if it isn't one.
    Works for bodies from api/review.py and from the issue form."""
    text = (text or "").replace("\r\n", "\n")
    record: Dict = {}
    mark = text.rfind(f"<!-- {JSON_MARK} ")
    if mark != -1:
        end = text.find(" -->", mark)
        try:
            record = json.loads(text[mark + len(JSON_MARK) + 6:end])
        except (ValueError, TypeError):
            record = {}
        text = text[:mark]
    fields: Dict[str, str] = {}
    chunks = re.split(r"^### (.+?)\s*$", text, flags=re.M)
    for i in range(1, len(chunks) - 1, 2):
        fid = HEADING_TO_ID.get(chunks[i].strip().lower())
        if fid:
            val = chunks[i + 1].strip()
            fields[fid] = "" if val == NO_RESPONSE else val
    skill = str(record.get("skill") or fields.get("skill", "")).strip().strip("`")
    if not SKILL_NAME.match(skill):
        return None
    version = str(record.get("version") or fields.get("version", "")).strip().lstrip("v")
    reviewer = fields.get("reviewer", "")
    m = re.match(r"^(.*?),\s*(.+?)(?:\s+\(@([A-Za-z0-9-]+)\))?$", reviewer)
    name, org_name, github = (m.group(1), m.group(2), m.group(3) or "") if m else (reviewer, "", "")
    return {
        "skill": skill,
        "version": version if VERSION.match(version) else "",
        "verdict": record.get("verdict") or _verdict_key(fields.get("verdict", "")),
        "parts": record.get("parts") or _parts(fields.get("parts", "")),
        "review": fields.get("review", ""),
        "evidence": fields.get("evidence", ""),
        "name": record.get("name") or name.strip(),
        "org_name": record.get("org_name") or org_name.strip(),
        "org": record.get("org", ""),
        "github": record.get("github") or github,
        "commit": record.get("commit", ""),
        "submitted": record.get("submitted", ""),
    }


def excerpt(markdown_text: str, limit: int = 600) -> str:
    """Plain-text start of a review for the skill page (the full text stays on GitHub)."""
    t = re.sub(r"```.*?```", " ", markdown_text, flags=re.S)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"^\s{0,3}(#{1,6}\s+|>\s?|[-*+]\s+|\d+\.\s+)", "", t, flags=re.M)
    t = t.replace("**", "").replace("__", "").replace("`", "")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t).strip()
    return t if len(t) <= limit else t[:limit].rsplit(" ", 1)[0] + "…"
