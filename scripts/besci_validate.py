#!/usr/bin/env python3
"""
besci_validate.py — the one validator for the Behavioral Science Skills Library.

The same file runs in four places, unchanged:
  - CI, on every pull request
  - inside besci-skill-creator, so authors check locally before submitting
  - inside besci-eval, as its structural check
  - inside the site's upload function, before a pull request is opened

Usage:
  python besci_validate.py                      # validate every skill under skills/
  python besci_validate.py path/to/skill-folder # validate one skill
  python besci_validate.py --json               # machine-readable output
  python besci_validate.py --taxonomy FILE      # use a specific taxonomy.yaml

Exit codes: 0 no errors (warnings allowed), 1 errors found, 2 usage problem.

Dependencies: PyYAML only. Python 3.8+.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write("besci_validate.py needs PyYAML: pip install pyyaml\n")
    sys.exit(2)

# ---------------------------------------------------------------------------
# The spec, as constants. docs/skill-spec.md is the prose version of this.
# ---------------------------------------------------------------------------

SPEC_TOP_LEVEL_KEYS = {"name", "description", "license", "compatibility", "allowed-tools", "metadata"}
ALLOWED_LICENSES = {"CC-BY-4.0", "MIT"}

REQUIRED_SECTIONS = [
    "What it does",
    "When to use it",
    "Before you start",
    "What it draws on",
    "How to do it",
    "Output template",
    "Where it goes wrong",
    "When to bring in a specialist",
]
NA_ALLOWED_SECTIONS = {"Before you start", "When to bring in a specialist"}
NA_PREFIX = "not applicable:"
NA_MIN_REASON_CHARS = 20

USE_WHEN_SUBHEADING = "Use it when"
DONT_USE_WHEN_SUBHEADING = "Do not use it when"
MIN_USE_WHEN_BULLETS = 3
MIN_DONT_USE_BULLETS = 2

REQUIRED_METADATA = ["type", "stage", "version", "status", "authors", "org"]
KNOWN_METADATA = set(REQUIRED_METADATA) | {
    "title", "weird", "tags", "consumes", "produces", "reviewed_by",
    "created", "updated", "catalog_snapshot",
}
MIN_EVALS = 3
MAX_SKILL_MD_LINES = 500
MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_FOLDER_BYTES = 10 * 1024 * 1024
ALLOWED_EXTENSIONS = {
    ".md", ".txt", ".json", ".yaml", ".yml", ".csv", ".tsv",
    ".py", ".r", ".sh", ".html", ".css", ".js",
    ".png", ".jpg", ".jpeg", ".svg", ".gif",
}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
CITATION_HINT_RE = re.compile(r"(https?://|doi\.org|\b(19|20)\d{2}\b)")


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Finding:
    level: str  # "error" | "warning"
    code: str
    message: str
    file: str = "SKILL.md"

    def as_dict(self) -> dict:
        return {"level": self.level, "code": self.code, "message": self.message, "file": self.file}


@dataclass
class Skill:
    path: str
    folder: str
    frontmatter: dict = field(default_factory=dict)
    metadata: dict = field(default_factory=dict)
    body: str = ""
    sections: "Dict[str, str]" = field(default_factory=dict)  # heading -> text, in file order
    evals: Optional[dict] = None
    changelog: Optional[str] = None
    files: List[str] = field(default_factory=list)
    findings: List[Finding] = field(default_factory=list)

    @property
    def name(self) -> str:
        return str(self.frontmatter.get("name", "")) if isinstance(self.frontmatter, dict) else ""

    @property
    def errors(self) -> List[Finding]:
        return [f for f in self.findings if f.level == "error"]

    @property
    def warnings(self) -> List[Finding]:
        return [f for f in self.findings if f.level == "warning"]

    def error(self, code: str, message: str, file: str = "SKILL.md") -> None:
        self.findings.append(Finding("error", code, message, file))

    def warn(self, code: str, message: str, file: str = "SKILL.md") -> None:
        self.findings.append(Finding("warning", code, message, file))


# ---------------------------------------------------------------------------
# Taxonomy
# ---------------------------------------------------------------------------

def find_repo_root(start: str) -> Optional[str]:
    """Walk upward until a taxonomy.yaml is found."""
    cur = os.path.abspath(start)
    while True:
        if os.path.exists(os.path.join(cur, "taxonomy.yaml")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            return None
        cur = parent


def load_taxonomy(path: Optional[str] = None) -> dict:
    """Load taxonomy.yaml. Falls back to a copy next to this script, then to built-in minimums."""
    candidates = []
    if path:
        candidates.append(path)
    root = find_repo_root(os.getcwd())
    if root:
        candidates.append(os.path.join(root, "taxonomy.yaml"))
    here = os.path.dirname(os.path.abspath(__file__))
    candidates.append(os.path.join(here, "taxonomy.yaml"))
    candidates.append(os.path.join(os.path.dirname(here), "taxonomy.yaml"))
    for c in candidates:
        if os.path.exists(c):
            with open(c, "r", encoding="utf-8") as fh:
                return yaml.safe_load(fh) or {}
    # Built-in minimum so the bundled copy still works without the file.
    return {
        "stages": [{"id": s} for s in ["define", "diagnose", "design", "measure", "test", "analyze", "implement", "other"]],
        "types": ["atomic", "meta"],
        "statuses": ["draft", "published", "deprecated"],
        "weird_statuses": [{"id": s} for s in ["weird-only", "mixed-evidence", "likely-generalizes", "untested-outside-weird", "not-applicable"]],
        "verbs": [],
        "io_types": [],
    }


def _ids(items) -> List[str]:
    out = []
    for it in items or []:
        if isinstance(it, dict):
            out.append(str(it.get("id", "")))
        else:
            out.append(str(it))
    return out


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def split_frontmatter(text: str) -> Tuple[Optional[str], str]:
    """Return (yaml_text, body). yaml_text is None when no frontmatter block exists."""
    if not text.startswith("---"):
        return None, text
    lines = text.splitlines(keepends=True)
    if lines[0].strip() != "---":
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "".join(lines[1:i]), "".join(lines[i + 1:])
    return None, text


def split_sections(body: str) -> Dict[str, str]:
    """Split a markdown body on level-2 headings. Keeps order. Ignores headings inside fenced code."""
    sections: Dict[str, str] = {}
    current: Optional[str] = None
    buf: List[str] = []
    in_fence = False
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("## "):
            if current is not None:
                sections[current] = "\n".join(buf).strip()
            current = line[3:].strip()
            buf = []
            continue
        if current is not None:
            buf.append(line)
    if current is not None:
        sections[current] = "\n".join(buf).strip()
    return sections


def split_subsections(text: str) -> Dict[str, str]:
    """Split a section on level-3 headings."""
    subs: Dict[str, str] = {}
    current: Optional[str] = None
    buf: List[str] = []
    for line in text.splitlines():
        if line.startswith("### "):
            if current is not None:
                subs[current] = "\n".join(buf).strip()
            current = line[4:].strip()
            buf = []
            continue
        if current is not None:
            buf.append(line)
    if current is not None:
        subs[current] = "\n".join(buf).strip()
    return subs


def bullets(text: str) -> List[str]:
    return [ln.strip()[2:].strip() for ln in text.splitlines() if ln.strip().startswith(("- ", "* "))]


def split_list(value: Optional[str]) -> List[str]:
    """Metadata lists are comma-separated strings (the spec allows strings only)."""
    if not value:
        return []
    return [v.strip() for v in str(value).split(",") if v.strip()]


def parse_skill(folder: str) -> Skill:
    """Read a skill folder into a Skill. Parsing problems are recorded as findings."""
    folder = os.path.abspath(folder.rstrip("/"))
    skill = Skill(path=folder, folder=os.path.basename(folder))
    md_path = os.path.join(folder, "SKILL.md")
    if not os.path.exists(md_path):
        skill.error("E001", "SKILL.md is missing. The file must be named exactly SKILL.md, uppercase.")
        return skill
    with open(md_path, "r", encoding="utf-8") as fh:
        text = fh.read()
    yaml_text, body = split_frontmatter(text)
    if yaml_text is None:
        skill.error("E002", "SKILL.md has no YAML frontmatter. It must start with a line '---', the fields, then '---'.")
        skill.body = text
    else:
        try:
            fm = yaml.safe_load(yaml_text)
        except yaml.YAMLError as exc:  # pragma: no cover
            skill.error("E002", f"Frontmatter is not valid YAML: {exc}")
            fm = {}
        if not isinstance(fm, dict):
            skill.error("E002", "Frontmatter must be a mapping of field: value.")
            fm = {}
        skill.frontmatter = fm
        md = fm.get("metadata")
        skill.metadata = md if isinstance(md, dict) else {}
        skill.body = body
    skill.sections = split_sections(skill.body)

    evals_path = os.path.join(folder, "evals", "evals.json")
    if os.path.exists(evals_path):
        try:
            with open(evals_path, "r", encoding="utf-8") as fh:
                skill.evals = json.load(fh)
        except json.JSONDecodeError as exc:
            skill.error("E029", f"evals/evals.json is not valid JSON: {exc}", file="evals/evals.json")
            skill.evals = None
    changelog_path = os.path.join(folder, "CHANGELOG.md")
    if os.path.exists(changelog_path):
        with open(changelog_path, "r", encoding="utf-8") as fh:
            skill.changelog = fh.read()
    for root, _dirs, files in os.walk(folder):
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), folder)
            if rel.startswith(".") or "/." in rel or "__pycache__" in rel:
                continue
            skill.files.append(rel)
    skill.files.sort()
    return skill


# ---------------------------------------------------------------------------
# Rules
# ---------------------------------------------------------------------------

def validate_skill(skill: Skill, taxonomy: dict) -> Skill:
    if any(f.code in ("E001",) for f in skill.findings):
        return skill
    fm, md = skill.frontmatter, skill.metadata
    stages = _ids(taxonomy.get("stages"))
    types = _ids(taxonomy.get("types"))
    statuses = _ids(taxonomy.get("statuses"))
    weird = _ids(taxonomy.get("weird_statuses"))
    verbs = [str(v) for v in taxonomy.get("verbs") or []]
    io_types = _ids(taxonomy.get("io_types"))

    # --- frontmatter: spec compliance -------------------------------------
    for key in fm.keys():
        if key not in SPEC_TOP_LEVEL_KEYS:
            skill.error("E035", f"Frontmatter key '{key}' is not in the Agent Skills spec. Move it under 'metadata:' as a string.")

    name = skill.name
    if not name:
        skill.error("E003", "Frontmatter needs a 'name'.")
    else:
        if len(name) > 64 or not NAME_RE.match(name):
            skill.error("E003", f"name '{name}' must be 1-64 chars of lowercase letters, digits, and single hyphens, not starting or ending with a hyphen.")
        if name != skill.folder:
            skill.error("E004", f"name '{name}' must match the folder name '{skill.folder}'.")

    desc = fm.get("description")
    if not isinstance(desc, str) or not desc.strip():
        skill.error("E006", "Frontmatter needs a 'description'. It is the trigger rule the AI reads before loading the skill.")
    else:
        d = desc.strip()
        if len(d) > 1024:
            skill.error("E006", f"description is {len(d)} characters; the spec caps it at 1024.")
        if "<" in d or ">" in d:
            skill.error("E006", "description must not contain '<' or '>' characters.")
        low = d.lower()
        if "use when" not in low and "use it when" not in low and "use this when" not in low:
            skill.error("E007", "description must say when to fire: include a 'Use when ...' clause.")
        if not re.search(r"(do not use|don't use|not for|do not invoke|not when)", low):
            skill.error("E008", "description must name the nearest adjacent intent it should NOT handle: include a 'Do not use when ...' clause.")

    lic = fm.get("license")
    if not lic:
        skill.error("E009", "Frontmatter needs 'license'. Use CC-BY-4.0 for skill content (MIT is for code-only skills).")
    elif str(lic) not in ALLOWED_LICENSES:
        skill.error("E009", f"license '{lic}' is not one of {sorted(ALLOWED_LICENSES)}.")

    # --- metadata ----------------------------------------------------------
    if not isinstance(fm.get("metadata"), dict):
        skill.error("E010", "Frontmatter needs a 'metadata:' mapping with type, stage, version, status, authors, org.")
    else:
        for k, v in md.items():
            if not isinstance(v, (str, int, float)) or isinstance(v, bool):
                skill.error("E010", f"metadata.{k} must be a plain string (the spec allows strings only). Lists go in as comma-separated text.")
            if k not in KNOWN_METADATA:
                skill.warn("W036", f"metadata.{k} is not a field the catalog knows about. It will be kept but not shown.")
        for k in REQUIRED_METADATA:
            if not str(md.get(k, "")).strip():
                skill.error("E010", f"metadata.{k} is required.")

    mtype = str(md.get("type", "")).strip()
    if mtype and types and mtype not in types:
        skill.error("E011", f"metadata.type '{mtype}' must be one of {types}.")
    stage = str(md.get("stage", "")).strip()
    if stage and stages and stage not in stages:
        skill.error("E012", f"metadata.stage '{stage}' must be one of {stages}.")
    elif stage == "other" and mtype == "atomic":
        skill.warn("W013", "metadata.stage is 'other'. Fine if nothing fits; a maintainer will look at whether the stage list needs extending.")
    version = str(md.get("version", "")).strip()
    if version and not SEMVER_RE.match(version):
        skill.error("E014", f"metadata.version '{version}' must be semver like 0.1.0 (quote it in YAML: version: \"0.1.0\").")
    status = str(md.get("status", "")).strip()
    if status and statuses and status not in statuses:
        skill.error("E015", f"metadata.status '{status}' must be one of {statuses}.")
    if mtype == "atomic":
        w = str(md.get("weird", "")).strip()
        if not w:
            skill.error("E018", "metadata.weird is required for atomic skills: how far the evidence has been tested outside WEIRD samples.")
        elif weird and w not in weird:
            skill.error("E018", f"metadata.weird '{w}' must be one of {weird}.")
    if mtype == "atomic" and name and verbs:
        first = name.split("-")[0]
        if first not in verbs:
            skill.error("E005", f"name must start with a verb from taxonomy.yaml (got '{first}'). Verb-first names are the atomicity test; add the verb to the taxonomy in the same PR if it is missing.")
    for key in ("consumes", "produces"):
        for t in split_list(md.get(key)):
            if io_types and t not in io_types:
                skill.warn("W019", f"metadata.{key} names '{t}', which is not in taxonomy.yaml io_types. Add it there in this PR, or use an existing id, so skills can chain.")

    # --- body sections -----------------------------------------------------
    present = list(skill.sections.keys())
    missing = [s for s in REQUIRED_SECTIONS if s not in present]
    for s in missing:
        skill.error("E020", f"Required section '## {s}' is missing.")
    order = [s for s in present if s in REQUIRED_SECTIONS]
    expected = [s for s in REQUIRED_SECTIONS if s in present]
    if order != expected:
        skill.error("E021", f"Sections must appear in this order: {' -> '.join(REQUIRED_SECTIONS)}.")
    for s in REQUIRED_SECTIONS:
        if s not in skill.sections:
            continue
        txt = skill.sections[s].strip()
        if not txt:
            skill.error("E022", f"Section '## {s}' is empty." + (" Write 'Not applicable: <reason>' if it truly does not apply." if s in NA_ALLOWED_SECTIONS else ""))
            continue
        if txt.lower().startswith(NA_PREFIX):
            reason = txt[len(NA_PREFIX):].strip()
            if s not in NA_ALLOWED_SECTIONS:
                skill.error("E023", f"Section '## {s}' cannot be 'Not applicable'. Only '{'/'.join(sorted(NA_ALLOWED_SECTIONS))}' can.")
            elif len(reason) < NA_MIN_REASON_CHARS:
                skill.error("E023", f"Section '## {s}' says 'Not applicable' but gives no real reason. Explain why this skill does not need it.")

    what = skill.sections.get("What it does", "")
    if what:
        first_sentence = re.split(r"(?<=[.!?])\s", what.strip(), maxsplit=1)[0]
        if re.search(r"\band\b", first_sentence, flags=re.IGNORECASE):
            skill.warn("W024", "The first sentence of 'What it does' contains 'and'. The atomicity rule is one thing, no 'and'. Split the skill or reword.")

    when = skill.sections.get("When to use it", "")
    if when:
        subs = split_subsections(when)
        use = bullets(subs.get(USE_WHEN_SUBHEADING, ""))
        dont = bullets(subs.get(DONT_USE_WHEN_SUBHEADING, ""))
        if len(use) < MIN_USE_WHEN_BULLETS:
            skill.error("E025", f"'## When to use it' needs a '### {USE_WHEN_SUBHEADING}' list with at least {MIN_USE_WHEN_BULLETS} bullets of user intents or phrasings (found {len(use)}).")
        if len(dont) < MIN_DONT_USE_BULLETS:
            skill.error("E026", f"'## When to use it' needs a '### {DONT_USE_WHEN_SUBHEADING}' list with at least {MIN_DONT_USE_BULLETS} bullets of adjacent intents (found {len(dont)}).")

    draws = skill.sections.get("What it draws on", "")
    if draws and mtype == "atomic" and not CITATION_HINT_RE.search(draws):
        skill.warn("W027", "'## What it draws on' has nothing that looks like a citation (no year, DOI, or URL). Name the framework or paper.")

    out = skill.sections.get("Output template", "")
    if out and "```" not in out:
        skill.warn("W028", "'## Output template' has no fenced code block. Show the exact shape of the response in a ```markdown block.")

    # --- evals -------------------------------------------------------------
    if skill.evals is None and not any(f.code == "E029" for f in skill.findings):
        skill.error("E029", "evals/evals.json is missing. Every skill ships at least three realistic test prompts.", file="evals/evals.json")
    elif isinstance(skill.evals, dict):
        if skill.evals.get("skill_name") != name:
            skill.error("E029", f"evals.json 'skill_name' must be '{name}'.", file="evals/evals.json")
        cases = skill.evals.get("evals")
        if not isinstance(cases, list) or len(cases) < MIN_EVALS:
            skill.error("E029", f"evals.json needs at least {MIN_EVALS} cases under 'evals' (found {len(cases) if isinstance(cases, list) else 0}).", file="evals/evals.json")
        else:
            for i, c in enumerate(cases):
                for k in ("id", "prompt", "expected_output"):
                    if not isinstance(c, dict) or not str(c.get(k, "")).strip():
                        skill.error("E029", f"evals.json case {i} is missing '{k}'.", file="evals/evals.json")

    # --- changelog ---------------------------------------------------------
    if skill.changelog is None:
        skill.error("E030", "CHANGELOG.md is missing. Add '## 0.1.0 - YYYY-MM-DD' with one line on what this version is.", file="CHANGELOG.md")
    else:
        heads = [ln for ln in skill.changelog.splitlines() if ln.startswith("## ")]
        if not heads:
            skill.error("E030", "CHANGELOG.md has no '## <version>' entry.", file="CHANGELOG.md")
        elif version and version not in heads[0]:
            skill.error("E030", f"CHANGELOG.md top entry '{heads[0]}' does not mention the current version {version}. Bump both together.", file="CHANGELOG.md")

    # --- files -------------------------------------------------------------
    md_lines = skill.body.count("\n") + 1
    if md_lines > MAX_SKILL_MD_LINES:
        skill.warn("W031", f"SKILL.md is {md_lines} lines; keep it under {MAX_SKILL_MD_LINES} and move detail into references/.")
    if "README.md" in skill.files:
        skill.warn("W033", "Skill folders should not contain README.md. Put instructions in SKILL.md or references/.", file="README.md")
    total = 0
    for rel in skill.files:
        full = os.path.join(skill.path, rel)
        size = os.path.getsize(full)
        total += size
        ext = os.path.splitext(rel)[1].lower()
        if rel in ("SKILL.md", "CHANGELOG.md") or rel.startswith("evals/"):
            pass
        if ext not in ALLOWED_EXTENSIONS and not rel.endswith("LICENSE"):
            skill.error("E034", f"File type '{ext or rel}' is not allowed in a skill folder.", file=rel)
        if size > MAX_FILE_BYTES:
            skill.error("E034", f"File is {size // 1024} KB; the cap is {MAX_FILE_BYTES // 1024} KB.", file=rel)
    if total > MAX_FOLDER_BYTES:
        skill.error("E034", f"Skill folder is {total // 1024} KB; the cap is {MAX_FOLDER_BYTES // 1024} KB.")
    # referenced files must exist (relative links and backticked paths into references/, scripts/, assets/)
    for ref in set(re.findall(r"(?:\]\(|`)((?:references|scripts|assets|evals)/[A-Za-z0-9_./-]+)", skill.body)):
        if not os.path.exists(os.path.join(skill.path, ref)):
            skill.error("E032", f"SKILL.md refers to '{ref}' but that file does not exist.")
    return skill


# ---------------------------------------------------------------------------
# Helpers other tools import
# ---------------------------------------------------------------------------

def trigger_phrases(skill: Skill) -> Tuple[List[str], List[str]]:
    """(should_fire, should_not_fire) phrasings from '## When to use it'."""
    subs = split_subsections(skill.sections.get("When to use it", ""))
    return bullets(subs.get(USE_WHEN_SUBHEADING, "")), bullets(subs.get(DONT_USE_WHEN_SUBHEADING, ""))


def latest_changelog_entry(skill: Skill) -> str:
    if not skill.changelog:
        return ""
    parts = re.split(r"^## ", skill.changelog, flags=re.MULTILINE)
    return ("## " + parts[1]).strip() if len(parts) > 1 else ""


def catalog_entry(skill: Skill) -> dict:
    """The record the site, the navigator snapshot, and besci-eval all read."""
    md = skill.metadata
    should, should_not = trigger_phrases(skill)
    return {
        "name": skill.name,
        "title": str(md.get("title") or skill.name.replace("-", " ").capitalize()),
        "description": str(skill.frontmatter.get("description", "")).strip(),
        "license": str(skill.frontmatter.get("license", "")),
        "type": str(md.get("type", "")),
        "stage": str(md.get("stage", "")),
        "version": str(md.get("version", "")),
        "status": str(md.get("status", "")),
        "authors": split_list(md.get("authors")),
        "org": str(md.get("org", "")),
        "weird": str(md.get("weird", "")),
        "tags": split_list(md.get("tags")),
        "consumes": split_list(md.get("consumes")),
        "produces": split_list(md.get("produces")),
        "reviewed_by": split_list(md.get("reviewed_by")),
        "sections": {k: v for k, v in skill.sections.items()},
        "what_it_does": skill.sections.get("What it does", "").strip().split("\n")[0],
        "use_when": should,
        "do_not_use_when": should_not,
        "eval_count": len(skill.evals.get("evals", [])) if isinstance(skill.evals, dict) else 0,
        "latest_change": latest_changelog_entry(skill),
        "files": skill.files,
        "path": os.path.relpath(skill.path, find_repo_root(skill.path) or os.getcwd()),
        "errors": [f.as_dict() for f in skill.errors],
        "warnings": [f.as_dict() for f in skill.warnings],
    }


def discover_skills(root: str) -> List[str]:
    """Every folder directly under root that holds a SKILL.md."""
    out = []
    if not os.path.isdir(root):
        return out
    for entry in sorted(os.listdir(root)):
        p = os.path.join(root, entry)
        if os.path.isdir(p) and os.path.exists(os.path.join(p, "SKILL.md")):
            out.append(p)
    return out


def validate_path(path: str, taxonomy: dict) -> List[Skill]:
    """Validate one skill folder, or every skill under a folder of skills."""
    if os.path.exists(os.path.join(path, "SKILL.md")):
        return [validate_skill(parse_skill(path), taxonomy)]
    return [validate_skill(parse_skill(p), taxonomy) for p in discover_skills(path)]


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def report_text(skills: List[Skill]) -> str:
    lines = []
    n_err = n_warn = 0
    for s in skills:
        label = s.name or s.folder
        if not s.findings:
            lines.append(f"PASS  {label}")
            continue
        lines.append(f"{'FAIL' if s.errors else 'WARN'}  {label}")
        for f in s.findings:
            mark = "  x " if f.level == "error" else "  ! "
            lines.append(f"{mark}[{f.code}] {f.file}: {f.message}")
        n_err += len(s.errors)
        n_warn += len(s.warnings)
    lines.append("")
    lines.append(f"{len(skills)} skill(s) checked: {n_err} error(s), {n_warn} warning(s).")
    if n_err == 0:
        lines.append("Structure OK. Content review by a maintainer is still required before merge.")
    return "\n".join(lines)


def report_json(skills: List[Skill]) -> dict:
    return {
        "ok": all(not s.errors for s in skills),
        "skills": [
            {
                "name": s.name or s.folder,
                "path": s.path,
                "errors": [f.as_dict() for f in s.errors],
                "warnings": [f.as_dict() for f in s.warnings],
            }
            for s in skills
        ],
    }


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Validate Behavioral Science Skills Library skill folders.")
    ap.add_argument("paths", nargs="*", help="Skill folder(s) or a folder of skills. Default: skills/ under the repo root.")
    ap.add_argument("--json", action="store_true", help="Machine-readable output.")
    ap.add_argument("--taxonomy", help="Path to taxonomy.yaml.")
    ap.add_argument("--warnings-as-errors", action="store_true")
    args = ap.parse_args(argv)

    taxonomy = load_taxonomy(args.taxonomy)
    paths = args.paths
    if not paths:
        root = find_repo_root(os.getcwd())
        if not root:
            sys.stderr.write("No skill path given and no taxonomy.yaml found upward from here.\n")
            return 2
        paths = [os.path.join(root, "skills")]
    skills: List[Skill] = []
    for p in paths:
        if not os.path.exists(p):
            sys.stderr.write(f"Path not found: {p}\n")
            return 2
        skills.extend(validate_path(p, taxonomy))
    if not skills:
        sys.stderr.write("No skills found (a skill is a folder containing SKILL.md).\n")
        return 2
    if args.json:
        print(json.dumps(report_json(skills), indent=2))
    else:
        print(report_text(skills))
    failed = any(s.errors for s in skills) or (args.warnings_as_errors and any(s.warnings for s in skills))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
