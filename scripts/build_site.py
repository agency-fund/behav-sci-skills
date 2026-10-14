#!/usr/bin/env python3
"""
build_site.py: builds the static catalog site into site/dist/.

Reads:  skills/*/ (SKILL.md, CHANGELOG.md, evals/, references/, scripts/, assets/),
        workflows/*.md, taxonomy.yaml, site/src/
Writes: site/dist/ (gitignored): HTML pages, data/catalog.json, data/skills.json, llms.txt,
        feed.xml, sitemap.xml, and a verbatim copy of site/src/.

Usage:
  uv run scripts/build_site.py
  SITE_URL=https://example.org uv run scripts/build_site.py

No framework. Two dependencies: PyYAML (via besci_validate) and markdown-it-py.
"""
from __future__ import annotations

import datetime as dt
import html
import json
import os
import re
import shutil
import subprocess
import sys
from typing import Dict, List, Optional
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import besci_validate as v  # noqa: E402

from markdown_it import MarkdownIt  # noqa: E402

ROOT = v.find_repo_root(os.path.dirname(os.path.abspath(__file__))) or os.getcwd()
SITE_URL = os.environ.get("SITE_URL", "https://besci-skills.vercel.app").rstrip("/")
REPO = "agency-fund/besci-skills"
GITHUB = f"https://github.com/{REPO}"
PLUGIN = "besci-skills"
SITE_NAME = "Behavioral Science Skills"
# The one-sentence description: home lede, footer, meta description, llms.txt.
TAGLINE = "An open-source library of atomic AI skills that bring actionable behavioral-science methods into your everyday work."
SRC = os.path.join(ROOT, "site", "src")
DIST = os.path.join(ROOT, "site", "dist")
SKILLS_DIR = os.path.join(ROOT, "skills")
WORKFLOWS_DIR = os.path.join(ROOT, "workflows")
NON_WORKFLOW_FILES = {"README.md", "WORKFLOW-TEMPLATE.md"}
# The OAuth client behind the "Sign in with Google" button on skill pages (public, not a secret).
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", "")
# Vercel Web Analytics counts page views (docs/analytics.md). Its script exists only on
# Vercel, so local builds leave it out; BESCI_ANALYTICS=1 forces it in for checking the output.
ANALYTICS = os.environ.get("VERCEL") == "1" or os.environ.get("BESCI_ANALYTICS") == "1"
FONTS = "https://fonts.googleapis.com/css2?family=Geist:wght@400..700&family=Geist+Mono:wght@400;500&display=swap"

MD = MarkdownIt("commonmark", {"html": True, "linkify": False}).enable(["table", "strikethrough"])

E = html.escape

# Icons are Phosphor (regular weight, MIT), one SVG per file in site/src/assets/icons/.
ICON_DIR = os.path.join(SRC, "assets", "icons")
_ICON_CACHE: Dict[str, str] = {}


def icon_paths(name: str) -> str:
    """The inner markup of one icon file."""
    if name not in _ICON_CACHE:
        try:
            with open(os.path.join(ICON_DIR, name + ".svg"), "r", encoding="utf-8") as fh:
                text = fh.read()
        except OSError:
            text = ""
        m = re.search(r"<svg[^>]*>(.*)</svg>", text, flags=re.DOTALL)
        _ICON_CACHE[name] = m.group(1).strip() if m else ""
    return _ICON_CACHE[name]


def icon(name: str, cls: str = "") -> str:
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} viewBox="0 0 256 256" fill="currentColor" aria-hidden="true">{icon_paths(name)}</svg>'


ICONS = {
    "github": icon("github-logo"),
    "sun": icon("sun", "ic-sun"),
    "moon": icon("moon", "ic-moon"),
    "menu": icon("list"),
    "search": icon("magnifying-glass"),
    "copy": icon("copy", "ic-copy"),
    "check": icon("check", "ic-check"),
    "map": icon("graph"),
    "arrow": icon("arrow-right"),
    "download": icon("download-simple"),
    "clip": icon("paperclip"),
    "replay": icon("arrow-counter-clockwise"),
    "plus": icon("plus"),
    "pencil": icon("pencil-simple"),
    "star": icon("star"),
}

# One icon per stage, drawn in the stage's color.
STAGE_ICON_NAMES = {
    "define": "target",
    "diagnose": "stethoscope",
    "design": "lightbulb",
    "measure": "ruler",
    "test": "flask",
    "analyze": "chart-bar",
    "implement": "plant",
    "other": "compass",
}

# Icons app.js and workflow.js draw at runtime, as <use href="#i-name">.
SPRITE_ICONS = ["plus", "check", "x", "star", "star-fill", "caret-up", "caret-down", "dots-six-vertical", "arrow-right", "link-simple", "copy", "download-simple"]


# The chain drawn on the home page's map teaser: the first five skills of diagnose-to-pilot.
TEASER_CHAIN = ["define-key-behavior", "decompose-comb-barriers", "draft-tdf-interview-guide", "synthesize-interview-findings", "select-intervention-levers"]

# Skills shown on the home page's stage chart; any that no longer exist are
# skipped and the stage's other skills fill in.
FEATURED = {
    "define": ["define-key-behavior", "build-user-funnel", "draft-theory-of-change", "assess-evidence-base"],
    "diagnose": ["decompose-comb-barriers", "diagnose-funnel-weak-link", "identify-positive-deviants", "diagnose-social-norm"],
    "design": ["select-intervention-levers", "design-reminder-schedule", "select-default-option", "write-social-norm-message"],
    "measure": ["draft-survey-items", "plan-agency-measurement", "design-list-experiment", "translate-survey-instrument"],
    "test": ["design-pilot-feasibility-study", "estimate-sample-size", "choose-trial-design", "write-pre-analysis-plan"],
    "analyze": ["synthesize-interview-findings", "analyze-heterogeneous-effects", "adjust-for-multiple-comparisons", "estimate-cost-effectiveness"],
    "implement": ["plan-scale-up-strategy", "design-fidelity-monitoring", "draft-intervention-description", "assess-scalability"],
}


def stage_icon(stage: str) -> str:
    return icon(STAGE_ICON_NAMES.get(stage, "compass"), "stage-ic")


def sprite() -> str:
    names = SPRITE_ICONS + [f"st-{k}" for k in STAGE_ICON_NAMES]
    symbols = []
    for n in names:
        src = STAGE_ICON_NAMES[n[3:]] if n.startswith("st-") else n
        symbols.append(f'<symbol id="i-{n}" viewBox="0 0 256 256">{icon_paths(src)}</symbol>')
    return f'<svg class="sprite" aria-hidden="true" focusable="false">{"".join(symbols)}</svg>'


# Saved choice first, then the system setting. app.js keeps following the
# system until the reader picks a theme.
THEME_SCRIPT = (
    "<script>(function(){var t=null;try{t=localStorage.getItem('theme')}catch(e){}"
    "if(t!=='light'&&t!=='dark'){t=window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';}"
    "document.documentElement.setAttribute('data-theme',t);document.documentElement.classList.add('js');})()</script>"
)

# Page views only: no cookies, no custom events (the free plan has none). Visiting any
# page with ?notrack=1 stops counting this browser's visits, so maintainers don't inflate
# the numbers; ?notrack=0 undoes it. Vercel's script counts a page view on load and on
# pushState, not on the replaceState calls that tabs and catalog search make.
ANALYTICS_SCRIPT = (
    "<script>window.va=window.va||function(){(window.vaq=window.vaq||[]).push(arguments)};"
    "(function(){var k='besci-notrack',p=new URLSearchParams(location.search).get('notrack');"
    "try{if(p==='1')localStorage.setItem(k,'1');if(p==='0')localStorage.removeItem(k)}catch(e){}"
    "window.va('beforeSend',function(ev){try{if(localStorage.getItem(k))return null}catch(e){}"
    "try{var u=new URL(ev.url);u.searchParams.delete('notrack');return Object.assign({},ev,{url:u.toString()})}catch(e){return ev}})})()</script>\n"
    '<script defer src="/_vercel/insights/script.js"></script>'
)


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def inline_svg(name: str) -> str:
    """Read an asset SVG and return its markup for inlining (so currentColor works)."""
    path = os.path.join(SRC, "assets", name)
    try:
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return ""
    text = re.sub(r"<\?xml[^>]*\?>", "", text)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    return text.strip()


def file_anchor(rel: str) -> str:
    """The id a skill file gets on its skill page, e.g. references/worked-example.md -> ref-worked-example."""
    top, _, rest = rel.partition("/")
    if top == "evals":
        return "test-cases"
    if top == "references":
        return "ref-" + slugify(rest[:-3] if rest.endswith(".md") else rest)
    if top == "scripts":
        return "script-" + slugify(rest)
    return "assets"


def md_to_html(text: str, skill_name: Optional[str] = None, local: Optional[set] = None, sibling_dir: str = "") -> str:
    """Render markdown. Relative links into a skill's own files go to the file's
    place on the skill page when it is shown there (``local``), else to GitHub.
    ``sibling_dir`` lets a reference file mention a sibling by its bare name."""
    local = local or set()

    def href(rel: str) -> str:
        if rel in local:
            return "#" + file_anchor(rel)
        return f"{GITHUB}/blob/main/skills/{skill_name}/{rel}"

    if skill_name:
        text = re.sub(
            r"\]\(((?:references|scripts|assets|evals)/[^)\s]+)\)",
            lambda m: f"]({href(m.group(1))})",
            text,
        )
    out = MD.render(text)
    if skill_name:
        def code_link(m: "re.Match") -> str:
            rel = m.group(1)
            if rel is None:  # an existing link: leave it alone
                return m.group(0)
            if not re.match(r"(references|scripts|assets|evals)/", rel):
                if not sibling_dir or f"{sibling_dir}/{rel}" not in local:
                    return m.group(0)
                rel = f"{sibling_dir}/{rel}"
            ext = "" if rel in local else ' rel="noopener"'
            return f'<a href="{E(href(rel))}"{ext}><code>{m.group(1)}</code></a>'
        out = re.sub(r"<a\b[^>]*>.*?</a>|<code>([A-Za-z0-9_./-]+)</code>", code_link, out, flags=re.S)
    return out


def link_issue_refs(text: str) -> str:
    """Turn #42 in markdown into a link to issue 42 (CHANGELOG entries cite the reviews they answer)."""
    return re.sub(r"(?<![\w/&#`\[])#(\d{1,6})\b", lambda m: f"[#{m.group(1)}]({GITHUB}/issues/{m.group(1)})", text)


def shift_headings(html_text: str, by: int) -> str:
    """Demote headings so a rendered file nests under the page's own h2/h3."""
    return re.sub(r"<(/?)h([1-6])\b", lambda m: f"<{m.group(1)}h{min(6, int(m.group(2)) + by)}", html_text)


def build_commit() -> str:
    """The commit this site is built from. Expert reviews link to SKILL.md at this
    commit, so a review stays tied to the exact text the reviewer read."""
    sha = os.environ.get("VERCEL_GIT_COMMIT_SHA", "")
    if not sha:
        try:
            sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, timeout=5).stdout.strip()
        except (OSError, subprocess.SubprocessError):
            sha = ""
    return sha if re.match(r"^[0-9a-f]{7,40}$", sha) else ""


def changelog_refs(changelog: Optional[str]) -> Dict[str, dict]:
    """Issues cited in the CHANGELOG, as {"42": {"version": "0.2.0", "text": <the sentence>}}.
    The skill page uses this to say which version answered an expert review. When
    an issue is cited in several entries, the earliest version wins."""
    refs: Dict[str, dict] = {}
    for m in re.finditer(r"^## (\d+\.\d+\.\d+)[^\n]*\n(.*?)(?=^## |\Z)", changelog or "", flags=re.M | re.S):
        version, entry = m.group(1), m.group(2)
        for sentence in re.split(r"(?<=[.!?])\s+|\n", entry):
            for n in re.findall(r"(?<![\w/&#`\[])#(\d{1,6})\b", sentence):
                refs[n] = {"version": version, "text": " ".join(sentence.split())[:280]}  # newest first, so the oldest overwrites
    return refs


def changelog_dates(changelog: Optional[str]) -> List[str]:
    if not changelog:
        return []
    return re.findall(r"^## \S+\s*-\s*(\d{4}-\d{2}-\d{2})", changelog, flags=re.MULTILINE)


SKIP_NAMES = {"__pycache__", ".DS_Store"}


def read_skill_files(folder: str, sub: str) -> List[dict]:
    """Every file under one of a skill's folders (references/, scripts/, assets/),
    as {rel, name, text, lines}. text is None for files that aren't UTF-8 text."""
    base = os.path.join(folder, sub)
    out: List[dict] = []
    if not os.path.isdir(base):
        return out
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_NAMES)
        for fn in sorted(filenames):
            if fn in SKIP_NAMES or fn.endswith(".pyc"):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, folder).replace(os.sep, "/")
            try:
                with open(path, "r", encoding="utf-8") as fh:
                    text: Optional[str] = fh.read()
            except (OSError, UnicodeDecodeError):
                text = None
            out.append({"rel": rel, "name": fn, "text": text, "lines": text.count("\n") + 1 if text else 0})
    return out


def load_skills(taxonomy: dict) -> List[dict]:
    skills = []
    for folder in v.discover_skills(SKILLS_DIR):
        sk = v.validate_skill(v.parse_skill(folder), taxonomy)
        entry = v.catalog_entry(sk)
        name = entry["name"] or os.path.basename(folder)
        entry["name"] = name
        entry["url"] = f"/skills/{name}/"
        entry["download_url"] = f"{GITHUB}/releases/latest/download/{name}.skill"
        entry["source_url"] = f"{GITHUB}/tree/main/skills/{name}"
        dates = changelog_dates(sk.changelog)
        entry["latest_date"] = dates[0] if dates else ""
        entry["first_date"] = dates[-1] if dates else ""
        entry["_changelog"] = sk.changelog or ""
        entry["_sections"] = sk.sections
        cases = sk.evals.get("evals") if isinstance(sk.evals, dict) else None
        entry["_evals"] = [c for c in cases if isinstance(c, dict)] if isinstance(cases, list) else []
        for sub in ("references", "scripts", "assets"):
            entry["_" + sub] = read_skill_files(folder, sub)
        skills.append(entry)
    skills.sort(key=lambda s: s["name"])
    return skills


def load_workflows() -> List[dict]:
    out = []
    if not os.path.isdir(WORKFLOWS_DIR):
        return out
    for fname in sorted(os.listdir(WORKFLOWS_DIR)):
        if not fname.endswith(".md") or fname in NON_WORKFLOW_FILES:
            continue
        path = os.path.join(WORKFLOWS_DIR, fname)
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
        yaml_text, body = v.split_frontmatter(text)
        fm = {}
        if yaml_text:
            try:
                fm = v.yaml.safe_load(yaml_text) or {}
            except Exception:
                fm = {}
        if not isinstance(fm, dict):
            fm = {}
        md = fm.get("metadata") if isinstance(fm.get("metadata"), dict) else {}
        name = str(fm.get("name") or os.path.splitext(fname)[0])
        out.append({
            "name": name,
            "title": str(fm.get("title") or md.get("title") or name.replace("-", " ").capitalize()),
            "description": str(fm.get("description") or "").strip(),
            "authors": v.split_list(md.get("authors")),
            "org": str(md.get("org", "")),
            "version": str(md.get("version", "")),
            "status": str(md.get("status", "")),
            "stages": v.split_list(md.get("stages")),
            "skills": v.split_list(md.get("skills")),
            "url": f"/workflows/{name}/",
            "source_url": f"{GITHUB}/blob/main/workflows/{fname}",
            "body": body,
            "steps": parse_workflow_steps(body),
        })
    return out


def step_refs(relationship: str, key: str) -> Optional[List[str]]:
    """Step ids named after `key` ("after 4, 5, and 7" -> ["4", "5", "7"]), or None if `key` is absent."""
    m = re.search(rf"\b{key}\b(.*)", relationship, flags=re.IGNORECASE)
    if not m:
        return None
    ids = []
    for tok in re.findall(r"\d+[a-z]?\b|[A-Za-z]+|,", m.group(1)):
        if re.fullmatch(r"\d+[a-z]?", tok):
            ids.append(tok)
        elif tok.lower() not in (",", "and", "or", "with"):
            break
    return ids


def parse_workflow_steps(body: str) -> List[dict]:
    """The "Skills in this workflow" table as steps, each with the steps it runs after.

    Relationship values are start, after N, parallel with N, independent, and
    optional (see workflows/WORKFLOW-TEMPLATE.md). A step whose relationship
    names no earlier step ("after the experiment ends") follows the previous row."""
    m = re.search(r"^## Skills in this workflow\s*\n(.*?)(?=^## |\Z)", body, flags=re.MULTILINE | re.DOTALL)
    if not m:
        return []
    rows = [ln.strip() for ln in m.group(1).splitlines() if ln.strip().startswith("|")]
    if len(rows) < 3:
        return []
    cells = lambda ln: [c.strip() for c in ln.strip().strip("|").split("|")]  # noqa: E731
    head = [c.lower() for c in cells(rows[0])]

    def col(row: List[str], *names: str) -> str:
        for n in names:
            for i, h in enumerate(head):
                if h.startswith(n) and i < len(row):
                    return row[i]
        return ""

    steps: List[dict] = []
    for ln in rows[2:]:
        row = cells(ln)
        sid = col(row, "step")
        if not sid:
            continue
        skill_cell = col(row, "skill")
        names = re.findall(r"`([a-z0-9-]+)`", skill_cell)
        label = ""
        if len(names) != 1:
            label = re.split(r"\s*\(|,", re.sub(r"`", "", skill_cell), maxsplit=1)[0].strip()
            label = re.sub(r"^the\s+", "", label, flags=re.IGNORECASE)
            label = label[:1].upper() + label[1:]
        rel = col(row, "relationship")
        steps.append({
            "id": sid,
            "skill": names[0] if len(names) == 1 else "",
            "alternatives": names if len(names) > 1 else [],
            "label": label,
            "relationship": rel,
            "optional": "optional" in rel.lower(),
            "carries": col(row, "what carries"),
            "decide": col(row, "human decision"),
        })

    known = {st["id"] for st in steps}
    for i, st in enumerate(steps):
        rel = st["relationship"].lower()
        after = step_refs(rel, "after")
        if after is None and rel.startswith(("start", "independent")):
            after = []
        elif not after:
            parallel = step_refs(rel, "parallel with") or []
            twin = next((x for x in steps[:i] if x["id"] in parallel), None)
            after = list(twin["after"]) if twin else ([steps[i - 1]["id"]] if i else [])
        st["after"] = [x for x in after if x in known and x != st["id"]]
    layer: Dict[str, int] = {}
    for st in steps:
        st["layer"] = 1 + max((layer.get(x, 0) for x in st["after"]), default=-1)
        layer[st["id"]] = st["layer"]
    return steps


def taxonomy_public(taxonomy: dict) -> dict:
    keys = ["stages", "types", "statuses", "weird_statuses", "io_types", "orgs", "verbs", "suggested_tags"]
    return {k: taxonomy.get(k, []) for k in keys}


def label_map(items) -> Dict[str, str]:
    out = {}
    for it in items or []:
        if isinstance(it, dict):
            out[str(it.get("id", ""))] = str(it.get("label") or it.get("id", ""))
        else:
            out[str(it)] = str(it)
    return out


def desc_map(items) -> Dict[str, str]:
    out = {}
    for it in items or []:
        if isinstance(it, dict):
            out[str(it.get("id", ""))] = str(it.get("description") or "")
    return out


ORG_NAMES = {"TAF": "The Agency Fund", "IL": "Irrational Labs", "community": "Community"}


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------

NAV = [
    ("Skills", "/skills/"),
    ("Map", "/map/"),
    ("Workflows", "/workflows/"),
    ("Install", "/install/"),
    ("Contribute", "/contribute/"),
    ("About", "/about/"),
]


def logos_html() -> str:
    taf = inline_svg("taf-logo.svg")
    il = inline_svg("il-logo.svg")
    return (
        '<span class="logos">'
        f'<span class="logo-taf">{taf}</span>'
        '<span class="logo-x" aria-hidden="true">×</span>'
        f'<span class="logo-il">{il}</span>'
        '</span>'
    )


def layout(title: str, description: str, body: str, path: str, extra_head: str = "", page_class: str = "", scripts: tuple = ()) -> str:
    def current(href: str) -> str:
        return ' aria-current="page"' if path.startswith(href) else ""

    def nav_item(label: str, href: str) -> str:
        # The Workflows tab counts the skills in the reader's workflow (workflow.js fills it in).
        count = '<span class="nav-count" data-wf-count hidden></span>' if href == "/workflows/" else ""
        return f'<a href="{E(href)}"{current(href)}>{E(label)}{count}</a>'

    nav = "".join(nav_item(label, href) for label, href in NAV)
    home_current = ' aria-current="page"' if path == "/" else ""
    full_title = f"{title} · {SITE_NAME}" if title != SITE_NAME else SITE_NAME
    canonical = f"{SITE_URL}{path}"
    logos = logos_html()
    script_tags = "\n".join(f'<script src="{E(s)}" defer></script>' for s in ("/app.js", "/workflow.js") + tuple(scripts))
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(full_title)}</title>
<meta name="description" content="{E(description)}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#f4f4f2" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0c0c0c" media="(prefers-color-scheme: dark)">
<meta property="og:title" content="{E(full_title)}">
<meta property="og:description" content="{E(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{E(canonical)}">
<meta property="og:site_name" content="{E(SITE_NAME)}">
<meta name="twitter:card" content="summary">
<link rel="canonical" href="{E(canonical)}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="{E(SITE_NAME)}: what's new" href="/feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="/styles.css">
{THEME_SCRIPT}
{ANALYTICS_SCRIPT if ANALYTICS else ""}
{extra_head}
</head>
<body class="{E(page_class)}">
{sprite()}
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-row">
    <a class="home-tab" href="/"{home_current}>Home</a>
    <nav class="site-nav" id="site-nav" aria-label="Main">{nav}</nav>
    <div class="header-actions">
      <a class="icon-btn" href="{GITHUB}" rel="noopener" target="_blank" aria-label="Source on GitHub" title="GitHub">{ICONS['github']}</a>
      <button class="icon-btn theme-toggle" type="button" aria-label="Switch to light mode">{ICONS['sun']}{ICONS['moon']}</button>
      <button class="icon-btn menu-btn" type="button" aria-label="Menu" aria-expanded="false" aria-controls="site-nav">{ICONS['menu']}</button>
    </div>
  </div>
</header>
<main id="main" class="wrap">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        {logos}
        <p>{E(TAGLINE)}</p>
      </div>
      <nav class="footer-links" aria-label="More">
        <a href="/whats-new/">What's new</a>
        <a href="/feed.xml">RSS feed</a>
        <a href="/propose/">Propose a skill</a>
        <a href="/upload/">Upload a skill</a>
        <a href="{GITHUB}/blob/main/docs/citing.md" rel="noopener">How to cite</a>
        <a href="{GITHUB}/blob/main/DISCLOSURE.md" rel="noopener">Disclosure</a>
        <a href="{GITHUB}/blob/main/GOVERNANCE.md" rel="noopener">Governance</a>
        <a href="{GITHUB}" rel="noopener">GitHub</a>
        <a href="/llms.txt">llms.txt</a>
      </nav>
    </div>
    <div class="footer-bottom">
      <span>Skill content is licensed <a href="{GITHUB}/blob/main/LICENSE-CONTENT.md" rel="noopener">CC BY 4.0</a> and code is <a href="{GITHUB}/blob/main/LICENSE" rel="noopener">MIT</a>.</span>
      <span class="footer-orgs"><a href="https://agency.fund" rel="noopener">The Agency Fund</a><a href="https://irrationallabs.com" rel="noopener">Irrational Labs</a></span>
    </div>
  </div>
</footer>
<div class="sr-only" id="wf-live" aria-live="polite"></div>
{script_tags}
</body>
</html>
"""


def write(path: str, content: str) -> None:
    full = os.path.join(DIST, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(content)


def page(path: str, title: str, description: str, body: str, **kw) -> None:
    out = path.rstrip("/") + "/index.html" if path.endswith("/") else path
    write(out, layout(title, description, body, path, **kw))


# ---------------------------------------------------------------------------
# Components
# ---------------------------------------------------------------------------

def pill(text: str, kind: str = "", stage: str = "") -> str:
    attrs = f' data-stage="{E(stage)}"' if stage else ""
    return f'<span class="pill pill-{E(kind or slugify(text))}"{attrs}>{E(text)}</span>'


def copy_block(cmd: str, label: str = "") -> str:
    lab = f'<span class="code-label">{E(label)}</span>' if label else ""
    cls = "code-row labeled" if label else "code-row"
    return (
        f'<div class="{cls}">{lab}<pre><code>{E(cmd)}</code></pre>'
        f'<button class="copy" type="button" data-copy="{E(cmd)}" aria-label="Copy command">'
        f'{ICONS["copy"]}{ICONS["check"]}<span class="copy-label">Copy</span></button></div>'
    )


def install_tabs(key: str, skill: Optional[dict] = None, n_skills: int = 0) -> str:
    """Three-tab install block. One localStorage key so the user's tool choice follows them.

    With a skill, the agents and Desktop tabs install that one skill; without
    one, every tab installs the whole library."""
    if skill:
        flags = f"--skill {skill['name']}"
        downloads = f'<p><a class="btn" href="{E(skill["download_url"])}" rel="noopener">{ICONS["download"]} Download {E(skill["name"])}.skill</a></p>'
        intro_cc = intro_ag = ""
        intro_dt = "<p>Upload the file under <strong>Settings → Capabilities → Skills</strong>. Zip installs do not update themselves; check <a href=\"/whats-new/\">What's new</a> now and then.</p>"
    else:
        flags = "--all"
        everything = f"all {n_skills} skills" if n_skills else "every skill"
        downloads = (
            f'<p><a class="btn-secondary" href="{GITHUB}/releases/latest/download/besci-navigator.skill" rel="noopener">{ICONS["download"]} besci-navigator.skill</a> '
            f'<a class="btn-ghost" href="{GITHUB}/releases/latest" rel="noopener">Every .skill file {ICONS["arrow"]}</a></p>')
        intro_cc = f"<p>Installs {everything} as one plugin. Turn on auto-update and it stays current.</p>"
        intro_ag = f"<p>Codex, Cursor, Copilot, Gemini CLI, OpenCode and others, through the <code>skills</code> CLI. Installs {everything}.</p>"
        intro_dt = ("<p>Claude Desktop and claude.ai take one skill per upload, so start with the navigator and add skills as it sends you to them. "
                    "Upload each file under <strong>Settings → Capabilities → Skills</strong>; zip installs do not update themselves.</p>")
        downloads, intro_dt = intro_dt, downloads
    return f"""<div class="tabs" data-tabs="install">
  <div class="tablist" role="tablist" aria-label="Install options">
    <button class="tab" role="tab" type="button" data-tab="claude-code" id="{key}-t1" aria-controls="{key}-p1" aria-selected="true">Claude Code</button>
    <button class="tab" role="tab" type="button" data-tab="agents" id="{key}-t2" aria-controls="{key}-p2" aria-selected="false" tabindex="-1">Codex, Cursor, Copilot…</button>
    <button class="tab" role="tab" type="button" data-tab="desktop" id="{key}-t3" aria-controls="{key}-p3" aria-selected="false" tabindex="-1">Claude Desktop</button>
  </div>
  <div class="tabpanel" role="tabpanel" id="{key}-p1" aria-labelledby="{key}-t1">
    {intro_cc}
    {copy_block(f"/plugin marketplace add {REPO}")}
    {copy_block(f"/plugin install {PLUGIN}@{PLUGIN}")}
  </div>
  <div class="tabpanel" role="tabpanel" id="{key}-p2" aria-labelledby="{key}-t2" hidden>
    {intro_ag}
    {copy_block(f"npx skills add {REPO} {flags}")}
  </div>
  <div class="tabpanel" role="tabpanel" id="{key}-p3" aria-labelledby="{key}-t3" hidden>
    {downloads}
    {intro_dt}
  </div>
</div>"""


def add_button(name: str, title: str, cls: str = "add-btn", label: str = "Add") -> str:
    """Adds a skill to the reader's workflow. workflow.js keeps its label and state in sync."""
    return (f'<button class="{cls}" type="button" data-add="{E(name)}" data-label-off="{E(label)}" aria-pressed="false" '
            f'aria-label="Add {E(title)} to your workflow">{ICONS["plus"]}<span class="add-label">{E(label)}</span></button>')


def card(s: dict, stage_labels: Dict[str, str]) -> str:
    status = s["status"] or "draft"
    stage = s["stage"] or ""
    search = " ".join([s["name"], s["title"], s["description"], s["what_it_does"], " ".join(s["tags"]),
                       " ".join(s.get("use_when") or []), " ".join(s["authors"])]).lower()
    is_meta = s["type"] == "meta" or stage == "other"
    stage_label = "Meta-skill" if is_meta else (stage_labels.get(stage, stage) or "No stage")
    return f"""<article class="card" data-name="{E(s['name'])}" data-stage="{E(stage)}" data-type="{E(s['type'])}" data-org="{E(s['org'])}" data-status="{E(status)}" data-tags="{E(' '.join(s['tags']))}" data-search="{E(search)}">
  <h3><a href="{E(s['url'])}">{E(s['title'])}</a></h3>
  <p class="card-name">{E(s['name'])}</p>
  <p class="card-desc">{E(s['what_it_does'])}</p>
  <div class="card-foot"><span class="card-stage">{stage_icon(stage)}{E(stage_label)}</span><span class="spacer"></span>{add_button(s['name'], s['title'])}</div>
</article>"""


def filters_html(skills: List[dict], taxonomy: dict) -> str:
    orgs = sorted({s["org"] for s in skills if s["org"]})
    tags = sorted({t for s in skills for t in s["tags"]})

    def opts(items, all_label):
        o = [f'<option value="">{E(all_label)}</option>']
        for it in items:
            val, lab = (it if isinstance(it, tuple) else (it, it))
            o.append(f'<option value="{E(val)}">{E(lab)}</option>')
        return "".join(o)

    org_opts = [(o, ORG_NAMES.get(o, o)) for o in orgs]
    return f"""<form class="toolbar" role="search" aria-label="Filter skills" onsubmit="return false;">
  <label class="search"><span class="sr-only">Search skills</span>{ICONS['search']}
    <input type="search" id="q" name="q" placeholder="Search by name, method, or tag" autocomplete="off" spellcheck="false"><kbd>/</kbd></label>
  <input type="hidden" id="f-stage" name="stage" value="">
  <details class="more-filters">
    <summary>More filters</summary>
    <div class="more-filters-body">
      <label><span class="sr-only">Type</span><select class="select" id="f-type" name="type">{opts([('atomic', 'Atomic'), ('meta', 'Meta')], 'Atomic and meta')}</select></label>
      <label><span class="sr-only">Organization</span><select class="select" id="f-org" name="org">{opts(org_opts, 'All orgs')}</select></label>
      <label><span class="sr-only">Status</span><select class="select" id="f-status" name="status">{opts([('published', 'Published'), ('draft', 'Draft'), ('deprecated', 'Deprecated')], 'All statuses')}</select></label>
      <label><span class="sr-only">Tag</span><select class="select" id="f-tag" name="tag">{opts(tags, 'All tags')}</select></label>
    </div>
  </details>
  <button type="button" id="f-clear" class="btn-ghost">Clear</button>
  <span class="filter-count" id="f-count" aria-live="polite"></span>
</form>"""


def skill_link(name: str, by_name: Dict[str, dict]) -> str:
    """A skill name in mono, linked to its page when the skill exists."""
    if name in by_name:
        return f'<a class="t-skill" href="{E(by_name[name]["url"])}">{E(name)}</a>'
    return f'<span class="t-skill">{E(name)}</span>'


def tool_line(name: str, sub: str, by_name: Dict[str, dict], wf: Optional[int] = None) -> str:
    """One 'Skill(name)' line in the hero demo, the way Claude Code shows a skill loading."""
    wf_attr = f' data-wf="{wf}"' if wf is not None else ""
    return (f'<div class="t-tool" data-step="tool"{wf_attr}><span class="t-b" aria-hidden="true"></span>'
            f'Skill(<b>{skill_link(name, by_name)}</b>)<span class="t-sub">⎿&nbsp; {E(sub)}</span></div>')


def hero_demo(by_name: Dict[str, dict]) -> str:
    """Three scripted, illustrative conversations: a meta-skill, an atomic skill, and a workflow.

    The full transcript is in the HTML; app.js only reveals it step by step,
    so readers without JavaScript or with reduced motion see all of it."""
    sk = lambda n: skill_link(n, by_name)  # noqa: E731
    clip = ICONS["clip"]
    meta_panel = f"""
  <div class="demo-screen" role="tabpanel" id="demo-p-meta" aria-labelledby="demo-t-meta" data-demo-panel="meta">
    <div class="demo-body" tabindex="0" aria-label="Illustrative conversation using besci-navigator">
      <div class="t-user" data-step="type"><span class="t-text">How do I measure agency in my program?</span></div>
      {tool_line("besci-navigator", f"Read the catalog: {len(by_name)} skills", by_name)}
      <div class="t-ai" data-step="say"><p>Your goal is still open, so I'm in <b>guide mode</b>: a few questions first, one at a time. Say “just tell me which skill” to skip ahead.</p>
        <p class="t-ask">What does the program do, for whom, and what would more agency look like?<small>Suggested: name one decision you want participants to make more on their own.</small></p></div>
      <div class="t-user" data-step="type"><span class="t-text">We run a voice advisory line for smallholder farmers in Ethiopia. We want farmers to make their own planting decisions with confidence, not just follow the advice.</span></div>
      <div class="t-ai" data-step="say"><p class="t-ask">Has your team written down what agency means for these farmers, and what data do you collect now?<small>Suggested: no written definition yet; call logs and a yearly household survey.</small></p></div>
      <div class="t-user" data-step="type"><span class="t-text">No definition yet. We have call logs, and a household survey at baseline in March.</span></div>
      <div class="t-ai" data-step="say"><p>That is enough to recommend skills. Switching to <b>route mode</b>: three skills, in this order.</p></div>
      <div class="t-block" data-step="rows">
        <div class="t-cap" data-row>Recommended skills</div>
        <div class="t-hyp" data-row><span class="t-tag">1 · Define</span><span>{sk("define-agency-construct")}: nobody has written down what agency means for these farmers, and measures chosen before that measure “agency” in name only.<small>Have ready: a paragraph on the advisory line and two or three things a confident farmer does differently.</small></span></div>
        <div class="t-hyp" data-row><span class="t-tag">2 · Measure</span><span>{sk("plan-agency-measurement")}: turns the definition into measures in the calls and outside them. Your call logs already count as data.<small>Have ready: the definition from step 1, and how much room the March survey has.</small></span></div>
        <div class="t-hyp" data-row><span class="t-tag">3 · Measure</span><span>{sk("draft-survey-items")}: writes the baseline questions so farmers with little schooling can answer them when an enumerator reads them aloud.<small>Have ready: the measurement plan from step 2.</small></span></div>
      </div>
      <div class="t-ai" data-step="say"><p><b>Next action:</b> start {sk("define-agency-construct")}. I can pass it what you have told me so far.</p></div>
    </div>
  </div>"""

    skill_panel = f"""
  <div class="demo-screen" role="tabpanel" id="demo-p-skill" aria-labelledby="demo-t-skill" data-demo-panel="skill" hidden>
    <div class="demo-body" tabindex="0" aria-label="Illustrative conversation using plan-agency-measurement">
      <div class="t-user" data-step="type"><span class="t-text">I'm working on a WhatsApp AI mentor that coaches secondary-school students on business skills. How should I measure student agency? We define it as students forming, testing, and revising their own business ideas, and knowing when the mentor's help is worth taking. More in the attached file.</span><span class="t-file">{clip}agency-definition.md</span></div>
      {tool_line("plan-agency-measurement", "Loaded skill", by_name)}
      <div class="t-ai" data-step="say"><p>Your definition focuses on three constructs: <b>entrepreneurial self-efficacy</b>, <b>revising after feedback</b>, and <b>calibrated reliance on the mentor</b>. One question before I plan anything:</p>
        <p class="t-ask">What decision will this plan support?<small>Suggested: choosing between the mentor's direct mode and a questions-first mode.</small></p></div>
      <div class="t-user" data-step="type"><span class="t-text">The mode decision. Students consented to chat analysis, and we can run a 20-minute survey in weeks 1 and 12.</span></div>
      <div class="t-ai" data-step="say"><p>Here is the plan on the 2x2 agency framework. <i>(have)</i> marks data you already collect.</p></div>
      <div class="t-block" data-step="rows">
        <div class="t-cap" data-row>Measures on the 2x2 agency framework</div>
        <table class="t-grid">
          <thead><tr data-row><th></th><th>End goal<small>a viable business idea</small></th><th>Digital tool<small>the AI mentor</small></th></tr></thead>
          <tbody>
            <tr data-row><th>Thoughts and feelings</th><td><span class="t-m"><span class="t-on">on</span>one-item confidence check after each revision <i>#1</i></span><span class="t-m"><span class="t-off">off</span>self-efficacy scale in the week 1 and 12 survey <i>#2</i></span></td><td class="t-dim">not in focus</td></tr>
            <tr data-row><th>Choices and actions</th><td><span class="t-m"><span class="t-on">on</span>LLM-coded idea revisions, experimental <i>#3</i></span><span class="t-m"><span class="t-off">off</span>panel pitch rubric (have) <i>#4</i></span></td><td><span class="t-m"><span class="t-on">on</span>delegation versus pushback in chats <i>#5</i></span><span class="t-m"><span class="t-off">off</span>teacher observation checklist <i>#6</i></span></td></tr>
          </tbody>
        </table>
      </div>
      <div class="t-ai" data-step="say"><p><b>Item #1</b>, drafted example, not from the literature: “How sure are you that you can make your idea work? Not sure / A little sure / Very sure.” Benchmark it against #2 before trusting it.</p></div>
      <div class="t-block" data-step="rows">
        <div class="t-cap" data-row>Next steps</div>
        <ol class="t-list">
          <li data-row><b>Research:</b> a validated entrepreneurial self-efficacy scale for secondary-school students, with a paste-ready search query</li>
          <li data-row><b>Adapt</b> #2 with {sk("translate-survey-instrument")}; build #1, #3, #5 and #6 from the drafted examples</li>
          <li data-row><b>Test:</b> cognitive interviews with 8 students ({sk("draft-cognitive-interview-script")}); model codes against two human coders on 150 chat segments ({sk("audit-llm-qualitative-coding")})</li>
          <li data-row><b>Interpret:</b> drop #1 as a proxy if it does not track #2</li>
          <li data-row><b>Later:</b> {sk("design-evidential-experiment")} for the direct versus questions-first comparison</li>
        </ol>
      </div>
      <div class="t-ai" data-step="say"><p class="t-ask">Want me to search for published entrepreneurial self-efficacy scales for #2 now? I will quote only items I can open.<small>Suggested: yes, limited to scales tested with secondary-school students.</small></p></div>
    </div>
  </div>"""

    rail_steps = [
        ("define-key-behavior", "Behavior"),
        ("decompose-comb-barriers", "COM-B"),
        ("draft-tdf-interview-guide", "Interviews"),
        ("synthesize-interview-findings", "Synthesis"),
        ("select-intervention-levers", "Lever"),
    ]
    rail = "".join(
        f'<li data-stage="{E(by_name.get(n, {}).get("stage", ""))}" title="{E(n)}"><span class="wf-dot">{i + 1}</span><span class="wf-lab">{E(lab)}</span></li>'
        for i, (n, lab) in enumerate(rail_steps))
    wf_panel = f"""
  <div class="demo-screen" role="tabpanel" id="demo-p-workflow" aria-labelledby="demo-t-workflow" data-demo-panel="workflow" hidden>
    <ol class="wf-rail" aria-label="Workflow steps">{rail}</ol>
    <div class="demo-body" tabindex="0" aria-label="Illustrative conversation running the diagnose-to-pilot workflow">
      <div class="t-user" data-step="type"><span class="t-text">Rural women in India learn about kangaroo mother care in a hospital health education session, but few report practicing it at home. Why? I want to study this qualitatively with a small sample, then design the most promising intervention.</span></div>
      {tool_line("besci-navigator", "Matched workflow: diagnose-to-pilot", by_name)}
      <div class="t-ai" data-step="say"><p>This fits <a href="/workflows/diagnose-to-pilot/">From a vague goal to a piloted intervention</a>. I will run its first five skills, from the behavior to a chosen lever, and stop wherever you need to decide.</p></div>
      {tool_line("define-key-behavior", "Step 1 of 5", by_name, 0)}
      <div class="t-ai" data-step="say"><p><b>Target behavior:</b> after discharge, mothers of low-birthweight babies hold the baby skin-to-skin at home every day, for the hours the nurses advised, through the first four weeks. Observable on the ASHA's home visits and a daily tick-sheet.</p></div>
      {tool_line("decompose-comb-barriers", "Step 2 of 5", by_name, 1)}
      <div class="t-block" data-step="rows">
        <div class="t-cap" data-row>Barrier hypotheses, by COM-B</div>
        <div class="t-hyp" data-row><span class="t-tag">O, social</span><span>The mother-in-law thinks a bare baby will catch cold<small>Ask: “What did your mother-in-law say the first time you held the baby this way?”</small></span></div>
        <div class="t-hyp" data-row><span class="t-tag">O, physical</span><span>Housework leaves no long stretch to sit with the baby<small>Ask: “Walk me through yesterday. When could you have held the baby?”</small></span></div>
        <div class="t-hyp" data-row><span class="t-tag">M, reflective</span><span>KMC feels like a hospital treatment that ended at discharge<small>Ask: “Why do you think the nurses asked you to do this?”</small></span></div>
      </div>
      <p class="t-note t-decide" data-step="note">You decide: which hypotheses go to a field round?</p>
      <div class="t-user" data-step="type"><span class="t-text">All three. We can interview about 12 mothers and a few mothers-in-law.</span></div>
      {tool_line("draft-tdf-interview-guide", "Step 3 of 5", by_name, 2)}
      <div class="t-ai" data-step="say"><p>Interview guide ready: questions mapped to the TDF domains behind each hypothesis, a short module for mothers-in-law, and probes to read aloud in Hindi. Interview each mother on her own; what she says about the family changes when her mother-in-law is in the room.</p></div>
      <p class="t-gap" data-step="note">Four weeks of interviews later</p>
      <div class="t-user" data-step="type"><span class="t-text">Notes from 12 mothers and 5 mothers-in-law in six villages.</span><span class="t-file">{clip}interview-notes.docx</span></div>
      {tool_line("synthesize-interview-findings", "Step 4 of 5", by_name, 3)}
      <div class="t-block" data-step="rows">
        <div class="t-cap" data-row>Barrier diagnosis</div>
        <div class="t-res is-yes" data-row><span>Mother-in-law's worry about cold</span><b>supported</b><small>9 of 12</small></div>
        <div class="t-res is-yes" data-row><span>No long stretch of time</span><b>supported</b><small>7 of 12</small></div>
        <div class="t-res is-no" data-row><span>“Only for the hospital”</span><b>not supported</b><small>2 of 12</small></div>
      </div>
      {tool_line("select-intervention-levers", "Step 5 of 5", by_name, 4)}
      <div class="t-ai" data-step="say"><p><b>Barrier:</b> the mother-in-law's worry about cold, which also keeps her from taking a turn. <b>Function:</b> Enablement, the strongest on APEASE. <b>Technique:</b> practical social support: on the first home visit, the ASHA shows the mother-in-law how to hold the baby skin-to-skin too, so the hours are shared. Kept for the next pilot: Modelling, a short video of local grandmothers doing it.</p>
        <p>Next, {sk("draft-lever-content")} writes the ASHA's home-visit script and {sk("design-pilot-feasibility-study")} plans a pilot in ten villages.</p></div>
    </div>
  </div>"""

    tabs = [("meta", "Use a meta-skill", "Meta-skill"), ("skill", "Use an atomic skill", "Atomic skill"), ("workflow", "Run a workflow", "Workflow")]
    # Short labels replace the long ones on narrow screens, where three long tabs overflow.
    tab_html = "\n      ".join(
        f'<button class="demo-tab" type="button" role="tab" id="demo-t-{k}" aria-controls="demo-p-{k}" '
        + ('aria-selected="true"' if i == 0 else 'aria-selected="false" tabindex="-1"')
        + f' data-demo-tab="{k}"><span class="demo-tab-long">{E(long)}</span><span class="demo-tab-short">{E(short)}</span></button>'
        for i, (k, long, short) in enumerate(tabs))
    return f"""<div class="demo reveal" style="--i:2" data-demo>
  <div class="demo-bar">
    <div class="demo-tabs" role="tablist" aria-label="Example">
      {tab_html}
    </div>
  </div>{meta_panel}{skill_panel}{wf_panel}
  <div class="demo-foot">
    <span>Example Use Cases</span>
    <span class="demo-foot-actions">
      <a href="/skills/besci-navigator/" data-demo-for="meta">Open this skill {ICONS['arrow']}</a>
      <a href="/skills/plan-agency-measurement/" data-demo-for="skill" hidden>Open this skill {ICONS['arrow']}</a>
      <a href="/workflows/diagnose-to-pilot/" data-demo-for="workflow" hidden>Open this workflow {ICONS['arrow']}</a>
      <button class="demo-replay" type="button" hidden>{ICONS['replay']} Replay</button>
    </span>
  </div>
</div>"""


def stage_flow(skills: List[dict], taxonomy: dict, by_name: Dict[str, dict]) -> str:
    """The seven stages as a flow chart. Each node links to the catalog filtered by its stage."""
    stages = [x for x in taxonomy.get("stages", []) if isinstance(x, dict) and x.get("id") != "other"]
    by_stage: Dict[str, List[dict]] = {}
    for s in skills:
        by_stage.setdefault(s["stage"], []).append(s)
    steps, panels = [], []
    for i, st in enumerate(stages):
        sid, label, desc = str(st.get("id")), str(st.get("label")), str(st.get("description") or "")
        members = by_stage.get(sid, [])
        n = len(members)
        n_txt = f"{n} skill{'s' if n != 1 else ''}"
        href = f"/skills/?stage={quote(sid)}"
        link = '<span class="flow-link" aria-hidden="true"></span>' if i < len(stages) - 1 else ""
        steps.append(
            f'<li class="flow-step" data-stage="{E(sid)}" style="--i:{i}">'
            f'<a class="flow-node" href="{E(href)}" data-idx="{i}">'
            f'<span class="flow-ring">{stage_icon(sid)}</span>'
            f'<span class="flow-text"><span class="flow-l">{E(label)}</span>'
            f'<span class="flow-n">{n_txt}</span><span class="flow-d">{E(desc)}</span></span></a>{link}</li>')
        featured = [by_name[x] for x in FEATURED.get(sid, []) if x in by_name and by_name[x]["stage"] == sid]
        featured += [s for s in members if s not in featured]
        items = "".join(
            f'<li><a href="{E(s["url"])}"><b>{E(s["title"])}</b><code>{E(s["name"])}</code></a></li>'
            for s in featured[:4])
        panels.append(
            f'<div class="flow-panel" id="flow-p-{E(sid)}" data-stage="{E(sid)}"{" hidden" if i else ""}>'
            f'<div class="flow-panel-main"><h3>{E(label)}</h3>'
            f'<p class="flow-panel-d">{E(desc)}</p>'
            f'<a class="flow-panel-more" href="{E(href)}">All {n} {E(label)} skills {ICONS["arrow"]}</a></div>'
            f'<ul class="flow-panel-skills" aria-label="Example {E(label)} skills">{items}</ul></div>')
    return (f'<div class="flow" data-flow><ol class="flow-track">{"".join(steps)}</ol>'
            f'<div class="flow-panels">{"".join(panels)}</div></div>')


def lower_first(text: str) -> str:
    """Lowercase an artifact label for use mid-sentence, leaving acronyms like COM-B alone."""
    return text[0].lower() + text[1:] if len(text) > 1 and text[1].islower() else text


def handoff(a: dict, b: dict, io_labels: Dict[str, str]) -> str:
    """The artifact label(s) that a passes to b, or "" if they do not connect."""
    shared = [t for t in a["produces"] if t in b["consumes"]]
    return ", ".join(io_labels.get(t, t) for t in shared)


def map_teaser(by_name: Dict[str, dict], taxonomy: dict) -> str:
    """A static five-skill chain, drawn like the map, that leads to the full map."""
    io_labels = label_map(taxonomy.get("io_types"))
    chain = [by_name[n] for n in TEASER_CHAIN if n in by_name]
    parts = []
    for i, s in enumerate(chain):
        if i:
            parts.append('<li class="teaser-link" aria-hidden="true"></li>')
        nxt = handoff(s, chain[i + 1], io_labels) if i < len(chain) - 1 else ""
        passes = f'<span class="teaser-pass">Passes on its {E(lower_first(nxt))}</span>' if nxt else ""
        parts.append(
            f'<li><a class="teaser-node" href="/map/?skill={quote(s["name"])}" data-stage="{E(s["stage"])}">'
            f'{stage_icon(s["stage"])}<b>{E(s["title"])}</b>{passes}</a></li>')
    return f'<ol class="teaser-chain">{"".join(parts)}</ol>'


def workflow_graph(w: dict, by_name: Dict[str, dict], compact: bool = False) -> str:
    """A workflow's steps as a small flow chart: one column per layer, parallel steps
    stacked, each step drawn like a stage on the home page.

    app.js draws the lines from data-after and animates them once on first view.
    The compact form (home tiles) sits inside a link, so its steps are not links."""
    steps = w.get("steps") or [
        {"id": str(i + 1), "skill": n, "alternatives": [], "label": "", "optional": False,
         "carries": "", "decide": "", "after": [str(i)] if i else [], "layer": i}
        for i, n in enumerate(w["skills"])]
    if not steps:
        return ""
    # Draw only the direct links: "after 4, 5, and 7" needs no line from 4 when
    # 4 already leads to 5. The dashed ring says a step in between is optional.
    after = {st["id"]: st["after"] for st in steps}

    def leads_to(a: str, b: str) -> bool:
        return any(x == a or leads_to(a, x) for x in after.get(b, []))
    links = {st["id"]: [a for a in st["after"] if not any(o != a and leads_to(a, o) for o in st["after"])] for st in steps}
    per_layer: Dict[int, List[dict]] = {}
    for st in steps:
        per_layer.setdefault(st["layer"], []).append(st)
    rows = max(len(v) for v in per_layer.values())
    # Row of each step. Steps sharing a layer are ordered by where their
    # predecessors sit, so lines cross less. A step alone in its layer stays level
    # with its one predecessor; one that joins branches spans the rows, centered.
    row_of: Dict[str, Optional[int]] = {}
    mid = (rows - 1) / 2
    for layer in sorted(per_layer):
        mates = per_layer[layer]
        if len(mates) > 1:
            def pull(st: dict) -> float:
                rs = [mid if row_of.get(a) is None else row_of[a] for a in links[st["id"]]]
                return sum(rs) / len(rs) if rs else mid
            for i, st in enumerate(sorted(mates, key=pull)):
                row_of[st["id"]] = i
            continue
        st = mates[0]
        if len(links[st["id"]]) == 1 and row_of.get(links[st["id"]][0]) is not None:
            row_of[st["id"]] = row_of[links[st["id"]][0]]
        else:
            row_of[st["id"]] = None if rows > 1 else 0
    nodes = []
    for st in steps:
        s = by_name.get(st["skill"])
        alts = [by_name[a] for a in st["alternatives"] if a in by_name]
        title = s["title"] if s else (st["label"] or st["skill"])
        stage = s["stage"] if s else (alts[0]["stage"] if alts and len({a["stage"] for a in alts}) == 1 else "")
        r = row_of[st["id"]]
        place = f'--c:{st["layer"] + 1};--r:{1 if r is None else r + 1};--span:{rows if r is None else 1}'
        ring = f'<span class="wfg-ring">{stage_icon(stage)}</span>'
        attrs = (f'data-step="{E(st["id"])}" data-after="{E(" ".join(links[st["id"]]))}" data-stage="{E(stage)}" '
                 f'style="{place}"' + (' data-span' if r is None else "") + (' data-optional' if st["optional"] else ""))
        if compact:
            nodes.append(f'<span class="wfg-node" {attrs} title="{E(title)}">{ring}</span>')
            continue
        info = (f' data-title="{E(title)}" data-carries="{E(st["carries"])}" data-decide="{E(st["decide"])}"'
                + (f' data-alts="{E(", ".join(a["title"] for a in alts))}"' if alts else ""))
        inner = f'{ring}<span class="wfg-t">{E(title)}</span>'
        target = (f'<a class="wfg-hit" href="{E(s["url"])}">{inner}</a>' if s
                  else f'<span class="wfg-hit" tabindex="0">{inner}</span>')
        nodes.append(f'<li class="wfg-node" {attrs}{info}>{target}</li>')
    style = f'style="--cols:{len(per_layer)};--rows:{rows}"'
    if compact:
        return f'<span class="wfg wfg-compact" data-wfg aria-hidden="true" {style}>{"".join(nodes)}</span>'
    hint = "Point at a step to see what it passes on and where your team decides. Dashed steps are optional."
    return (f'<div class="wfg" data-wfg {style}><ol class="wfg-grid" aria-label="Steps in {E(w["title"])}">{"".join(nodes)}</ol>'
            f'<div class="wfg-cap" data-hint="{E(hint)}" aria-live="polite"><p class="wfg-hint">{E(hint)}</p></div></div>')


def workflow_lead(w: dict) -> str:
    """The first clause of a workflow's description, for compact listings."""
    d = w["description"]
    lead = d.split(":", 1)[0] if ":" in d[:240] else d
    if len(lead) > 200:
        lead = lead[:200].rsplit(" ", 1)[0] + "…"
    return lead.rstrip(".") + "."


def install_skills_cmd(names: List[str]) -> str:
    return f"npx skills add {REPO} " + " ".join(f"--skill {n}" for n in names)




# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def build_index(skills: List[dict], taxonomy: dict, workflows: List[dict]) -> None:
    by_name = {s["name"]: s for s in skills}
    n_skills = len(skills)
    meta = [s for s in skills if s["type"] == "meta"]
    meta_links = ", ".join(skill_link(s["name"], by_name) for s in meta)

    tiles = []
    for w in workflows[:4]:
        tiles.append(
            f'<li><a class="wf-tile" href="{E(w["url"])}"><b>{E(w["title"])}</b>'
            f'<span class="wf-tile-lead">{E(workflow_lead(w))}</span>'
            f'{workflow_graph(w, by_name, compact=True)}</a></li>')

    body = f"""
<section class="hero">
  <div class="hero-bg" aria-hidden="true"></div>
  <div class="hero-grid">
    <div class="hero-copy">
      <div class="hero-logos reveal" style="--i:0">{logos_html()}</div>
      <h1 class="reveal" style="--i:1">Behavioral science skills for your AI assistant</h1>
      <p class="lede reveal" style="--i:2">{E(TAGLINE)}</p>
      <p class="hero-actions reveal" style="--i:3"><a class="btn" href="/install/">Install {ICONS['arrow']}</a> <a class="btn-secondary" href="/skills/">Browse skills</a></p>
    </div>
    {hero_demo(by_name)}
  </div>
</section>

<section class="section" aria-labelledby="stages-h">
  <div class="section-head">
    <h2 id="stages-h">Where are you in the project?</h2>
    <p>Skills are grouped by the stage of a project where you'd use them. Pick one to see what's in it.</p>
  </div>
  {stage_flow(skills, taxonomy, by_name)}
  <p class="flow-foot">Three meta-skills look after the library itself: {meta_links}.</p>
</section>

<section class="section" aria-labelledby="teaser-h">
  <div class="section-head">
    <h2 id="teaser-h">See which skills feed into each other</h2>
    <p>Some skills produce something another skill takes in. A barrier diagnosis, for example, is what lever selection starts from. The map draws these links for all {n_skills} skills.</p>
  </div>
  {map_teaser(by_name, taxonomy)}
  <p class="section-actions"><a class="btn-secondary" href="/map/">{ICONS['map']} Open the skill map</a></p>
</section>

<section class="section" aria-labelledby="wf-h">
  <div class="section-head">
    <h2 id="wf-h">Connect multiple skills to create a workflow</h2>
    <p>A workflow runs several skills in order for a bigger job and marks where your team has to decide.</p>
  </div>
  <ul class="wf-grid">{''.join(tiles)}</ul>
  <p class="section-actions"><a class="btn-secondary" href="/workflows/">All workflows</a> <a class="btn-ghost" href="/workflows/build/">Build your own {ICONS['arrow']}</a></p>
</section>

<section class="section install-band" aria-labelledby="install-h">
  <div>
    <h2 id="install-h">Install in Claude Code</h2>
    <p>Two commands install every skill and keep them up to date.</p>
    <p><a href="/install/">Using Codex, Cursor, or Claude Desktop? See every install option.</a></p>
  </div>
  <div>
    {copy_block(f"/plugin marketplace add {REPO}")}
    {copy_block(f"/plugin install {PLUGIN}@{PLUGIN}")}
  </div>
</section>
"""
    page("/", SITE_NAME, f"{TAGLINE} From The Agency Fund and Irrational Labs.", body, page_class="page-index")


def build_catalog(skills: List[dict], taxonomy: dict) -> None:
    stage_labels = label_map(taxonomy.get("stages"))
    stage_descs = desc_map(taxonomy.get("stages"))
    stages = [x for x in taxonomy.get("stages", []) if isinstance(x, dict) and x.get("id") != "other"]
    counts: Dict[str, int] = {}
    for s in skills:
        counts[s["stage"]] = counts.get(s["stage"], 0) + 1

    chips = [f'<button class="stage-chip chip-all" type="button" data-stage="" aria-pressed="true">All stages <span>{len(skills)}</span></button>']
    for st in stages:
        sid = str(st.get("id"))
        chips.append(
            f'<button class="stage-chip" type="button" data-stage="{E(sid)}" data-label="{E(str(st.get("label")))}" '
            f'data-desc="{E(stage_descs.get(sid, ""))}" aria-pressed="false">{stage_icon(sid)}{E(str(st.get("label")))} <span>{counts.get(sid, 0)}</span></button>')
    stage_default = "Pick a stage to narrow the list."

    # Cards grouped by stage, meta-skills first, then the stages in flow order. The
    # group headings hide when a filter or search is on and the grid goes flat.
    groups = [("other", "Meta-skills", "Skills that help you use the library itself.")]
    groups += [(str(st.get("id")), str(st.get("label")), stage_descs.get(str(st.get("id")), "")) for st in stages]
    def group_of(s: dict) -> str:
        return "other" if s["type"] == "meta" or s["stage"] in ("", "other") else s["stage"]

    blocks = []
    for sid, label, desc in groups:
        members = [s for s in skills if group_of(s) == sid]
        if not members:
            continue
        cards = "\n".join(card(s, stage_labels) for s in members)
        blocks.append(
            f'<section class="group" data-stage="{E(sid)}" aria-labelledby="g-{E(sid)}">'
            f'<div class="group-head"><h2 id="g-{E(sid)}">{stage_icon(sid)}<span class="group-l">{E(label)}</span> <span class="group-n">{len(members)}</span></h2><p>{E(desc)}</p></div>\n'
            f'{cards}</section>')
    body = f"""
<section id="catalog" aria-labelledby="catalog-h">
<div class="page-head page-head-row">
  <div>
    <h1 id="catalog-h">Skills</h1>
    <p class="lede">Each skill handles one method. Filter by stage, or search for the method you need.</p>
  </div>
  <a class="btn-secondary" href="/map/">{ICONS['map']} Open the map</a>
</div>
<div class="stage-chips" role="group" aria-label="Filter by stage">{''.join(chips)}</div>
<p class="stage-desc" id="stage-desc" data-default="{E(stage_default)}">{E(stage_default)}</p>
{filters_html(skills, taxonomy)}
<div class="grid" id="grid">
{chr(10).join(blocks)}
</div>
<p id="no-results" class="no-results" hidden>No skills match. <button type="button" class="link-btn" id="f-clear-2">Clear filters</button> or <a href="/propose/">propose the one you need</a>.</p>
</section>
"""
    page("/skills/", "Skills", "Search and filter every skill in the Behavioral Science Skills Library.", body, page_class="page-catalog")


def build_map() -> None:
    body = f"""
<div class="page-head map-head">
  <h1>Skill map</h1>
  <p class="lede">An arrow from one skill to another means the first one produces something the second one uses, as the skills' authors declared it. Follow the arrows to find skills that can run in sequence. They aren't the only order that works.</p>
  <div class="map-tools">
    <label class="search map-search"><span class="sr-only">Find a skill on the map</span>{ICONS['search']}
      <input type="search" id="map-q" placeholder="Find a skill" autocomplete="off" spellcheck="false"></label>
    <p class="map-hint">Click a skill to hold its connections in place.</p>
  </div>
</div>
<div class="map-wrap">
  <div class="map" id="map" aria-label="Skill map"><p class="map-loading">Loading the map…</p></div>
  <aside class="map-panel" id="map-panel" aria-label="Selected skill" hidden></aside>
</div>
<p class="map-narrow muted">The map is wide. Scroll sideways, or use the list on the <a href="/skills/">Skills page</a>.</p>
"""
    page("/map/", "Skill map", "How the skills in the Behavioral Science Skills Library connect: which skill's output another skill takes in.", body,
         page_class="page-map", scripts=("/map.js",))


# ---------------------------------------------------------------------------
# Skill page tabs: one per part of the skill folder
# ---------------------------------------------------------------------------

# What each tab is for, shown at the top of the tab. Keys double as ?tab= values.
TAB_INTROS = {
    "skill": "The instructions your AI follows when this skill runs. Installing the skill gives it this file and everything in the other tabs.",
    "test-cases": "Realistic requests used to check this skill, each paired with what a good answer must contain. Maintainers rerun them with besci-eval when the skill or the AI model changes. They also show the kind of request the skill is built for.",
    "references": "Longer material the skill opens only when a step calls for it, which keeps the main instructions short.",
    "scripts": "Code the skill runs during its steps, so results such as calculations come from code rather than from the AI working them out.",
    "assets": "Files the skill uses as starting points, such as templates. They ship with the skill but aren't instructions.",
    "version-history": "What changed in each version, newest first. An entry that answers an issue or review links to it.",
    "reviews": "Expert reviews come from behavioral scientists at The Agency Fund and Irrational Labs and are kept as issues on GitHub; each shows whether a later version of the skill answered it. Ratings and comments come from anyone who has used the skill.",
}

# Purpose lines for reference files whose opening paragraph describes the case, not the file.
KNOWN_FILES = {
    "worked-example.md": "A full run of the skill on a realistic case, showing the output it should produce.",
    "evidence-notes.md": "The studies behind the method: what each found, how well it is verified, and how far it transfers.",
}
REFERENCE_ORDER = {"worked-example.md": 0, "evidence-notes.md": 2}  # everything else sorts between


def panel_id(key: str) -> str:
    return "skill-md" if key == "skill" else key


def text_html(text: str) -> str:
    """Plain text (a test request, an expected answer) as escaped paragraphs."""
    paras = [p.strip() for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    return "".join("<p>" + E(p).replace("\n", "<br>") + "</p>" for p in paras)


def split_doc(text: str):
    """A markdown file as (frontmatter, title, body without the title, first paragraph)."""
    fm = ""
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            fm, text = text[4:end].strip("\n"), text[end + 4:].lstrip("\n")
    m = re.match(r"#\s+(.+)\n", text)
    title = m.group(1).strip() if m else ""
    body = text[m.end():] if m else text
    first = next((p.strip() for p in re.split(r"\n\s*\n", body)
                  if p.strip() and not p.lstrip().startswith(("#", "|", "-", "*", "```", ">"))), "")
    return fm, title, body, first


def first_sentence(text: str, limit: int = 180) -> str:
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    t = " ".join(t.replace("`", "").replace("**", "").split())
    m = re.match(r"(.+?[.!?])(\s|$)", t)
    s = m.group(1) if m else t
    return s if len(s) <= limit else s[:limit].rsplit(" ", 1)[0] + "…"


def script_purpose(name: str, text: str) -> str:
    """The first paragraph of a script's module docstring, without the leading 'name.py:'."""
    m = re.search(r'("""|\'\'\')\s*(.*?)\s*(?:\n\s*\n|\1)', text, re.S)
    if not m:
        return ""
    s = " ".join(m.group(2).split())
    s = re.sub(r"^" + re.escape(name) + r"\s*[:—-]\s*", "", s)
    return s[:1].upper() + s[1:]


def tab_intro(key: str, title: str, s: dict, source: str = "") -> str:
    src = ""
    if source:
        kind = "tree" if source.endswith("/") else "blob"
        url = f"{GITHUB}/{kind}/main/skills/{s['name']}/{source.rstrip('/')}"
        src = f'<p class="tab-source"><code>{E(source)}</code><a href="{E(url)}" rel="noopener">View on GitHub</a></p>'
    return f'<div class="tab-intro"><h2 class="tab-title">{E(title)}</h2><p>{E(TAB_INTROS[key])}</p>{src}</div>'


def file_head(s: dict, f: dict, title: str, purpose: str = "", download: bool = False) -> str:
    gh = f"{GITHUB}/blob/main/skills/{s['name']}/{f['rel']}"
    size = f"{f['lines']} lines" if f["text"] is not None else "not a text file"
    raw = (f'<a href="https://raw.githubusercontent.com/{REPO}/main/skills/{E(s["name"])}/{E(f["rel"])}" rel="noopener" download>Download</a>'
           if download else "")
    purpose_html = f'<p class="file-purpose">{E(purpose)}</p>' if purpose else ""
    return (f'<header class="file-head"><h3>{E(title)}</h3>'
            f'<p class="file-meta"><code>{E(f["rel"])}</code><span>{size}</span><a href="{E(gh)}" rel="noopener">View on GitHub</a>{raw}</p>'
            f'{purpose_html}</header>')


def render_evals(s: dict):
    """The Test cases tab: each case's request and what a good answer includes. Returns (html, toc)."""
    parts, toc = [], []
    for i, c in enumerate(s["_evals"], 1):
        cid = str(c.get("id", i))
        aid = f"test-case-{slugify(cid) or i}"
        extra = ""
        files = [str(x) for x in (c.get("files") or [])]
        if files:
            extra += ('<p class="case-label">Files given with the request</p><ul class="case-list">'
                      + "".join(f"<li><code>{E(x)}</code></li>" for x in files) + "</ul>")
        checks = [(a.get("text") or a.get("description") or json.dumps(a)) if isinstance(a, dict) else str(a)
                  for a in (c.get("assertions") or [])]
        if checks:
            extra += ('<p class="case-label">Checks on the answer</p><ul class="case-list">'
                      + "".join(f"<li>{E(x)}</li>" for x in checks) + "</ul>")
        parts.append(
            f'<article class="case" id="{E(aid)}"><h3>Test case {E(cid)}</h3>'
            f'<p class="case-label">The request</p><blockquote class="case-prompt">{text_html(str(c.get("prompt", "")))}</blockquote>'
            f'<p class="case-label">What a good answer includes</p><div class="case-expected">{text_html(str(c.get("expected_output", "")))}</div>'
            f'{extra}</article>')
        toc.append((aid, f"Test case {cid}"))
    if not parts:
        return '<p class="muted">This skill has no test cases yet.</p>', []
    return "".join(parts), toc


def render_references(s: dict, local: set):
    """The References tab: an index, then each file rendered in full. Returns (html, toc)."""
    files = sorted(s["_references"], key=lambda f: (REFERENCE_ORDER.get(f["name"], 1), f["rel"]))
    parts, toc, index = [], [], []
    for f in files:
        aid = file_anchor(f["rel"])
        title, purpose, summary, body_html = f["name"], "", "", ""
        if f["text"] is not None and f["name"].endswith(".md"):
            fm, h1, body, first = split_doc(f["text"])
            title = h1 or f["name"]
            purpose = KNOWN_FILES.get(f["name"], "")
            summary = purpose or first_sentence(first)
            if fm:
                body_html += f'<pre><code>{E("---" + chr(10) + fm + chr(10) + "---")}</code></pre>'
            body_html += shift_headings(md_to_html(body, s["name"], local, "references"), 2)
        elif f["text"] is not None:
            body_html = f'<pre class="code-file"><code>{E(f["text"])}</code></pre>'
        parts.append(f'<section class="file-doc" id="{E(aid)}">{file_head(s, f, title, purpose)}<div class="file-body">{body_html}</div></section>')
        toc.append((aid, title))
        sub = f"<span>{E(summary)}</span>" if summary else ""
        index.append(f'<li><a href="#{E(aid)}"><b>{E(title)}</b><code>{E(f["rel"])}</code></a>{sub}</li>')
    index_html = f'<ul class="file-index">{"".join(index)}</ul>' if len(files) > 1 else ""
    return index_html + "".join(parts), toc


def render_scripts(s: dict):
    """The Scripts tab: each script's purpose and full source. Returns (html, toc)."""
    parts, toc = [], []
    for f in s["_scripts"]:
        aid = file_anchor(f["rel"])
        purpose = script_purpose(f["name"], f["text"]) if f["text"] else ""
        code = f'<pre class="code-file"><code>{E(f["text"])}</code></pre>' if f["text"] is not None else ""
        parts.append(f'<section class="file-doc" id="{E(aid)}">{file_head(s, f, f["name"], purpose, download=True)}{code}</section>')
        toc.append((aid, f["name"]))
    return "".join(parts), toc


def render_assets(s: dict) -> str:
    items = []
    for f in s["_assets"]:
        gh = f"{GITHUB}/blob/main/skills/{s['name']}/{f['rel']}"
        size = f"{f['lines']} lines" if f["text"] is not None else ""
        items.append(f'<li><a href="{E(gh)}" rel="noopener"><code>{E(f["rel"])}</code></a><span>{size}</span></li>')
    return f'<ul class="file-list">{"".join(items)}</ul>'


def render_changelog(s: dict, local: set):
    """The Version history tab. #N becomes an issue link; each version gets an id. Returns (html, toc)."""
    md = re.sub(r"^# .*\n", "", s["_changelog"], count=1).strip()
    if not md:
        return "<p class='muted'>No changelog.</p>", []
    out = shift_headings(md_to_html(link_issue_refs(md), s["name"], local), 1)
    toc = []

    def tag(m: "re.Match") -> str:
        ver = m.group(1)
        vid = "v-" + slugify(ver)
        toc.append((vid, ver))
        return f'<h3 id="{vid}">{ver}{m.group(2)}</h3>'
    out = re.sub(r"<h3>(\d+\.\d+\.\d+)([^<]*)</h3>", tag, out)
    return out, toc


def toc_list(key: str, items, first: bool) -> str:
    hidden = "" if first else " hidden"
    lis = "".join(f'<li><a href="#{E(i)}">{E(label)}</a></li>' for i, label in items)
    return f'<ol data-tab-for="{E(key)}"{hidden}>{lis}</ol>'


def build_skill_pages(skills: List[dict], taxonomy: dict) -> None:
    stage_labels = label_map(taxonomy.get("stages"))
    weird_labels = label_map(taxonomy.get("weird_statuses"))
    io_labels = label_map(taxonomy.get("io_types"))
    producers: Dict[str, List[dict]] = {}
    consumers: Dict[str, List[dict]] = {}
    for s in skills:
        for t in s["produces"]:
            producers.setdefault(t, []).append(s)
        for t in s["consumes"]:
            consumers.setdefault(t, []).append(s)

    commit = build_commit()
    for s in skills:
        name = s["name"]
        status = s["status"] or "draft"
        stage = s["stage"] or ""
        year = (s["latest_date"] or s["first_date"] or str(dt.date.today()))[:4]
        authors = ", ".join(s["authors"]) or "Unknown author"
        cite = (f"{authors} ({year}). {s['title']} (version {s['version']}) [AI skill]. "
                f"Behavioral Science Skills Library, The Agency Fund and Irrational Labs. {SITE_URL}{s['url']}")

        def chips(types: List[str], related: Dict[str, List[dict]], verb: str) -> str:
            if not types:
                return '<p class="io-none">Nothing declared.</p>'
            parts = []
            for t in types:
                rel = [r for r in related.get(t, []) if r["name"] != name]
                links = ", ".join(f'<a href="{E(r["url"])}">{E(r["name"])}</a>' for r in rel)
                lab = io_labels.get(t, "")
                sub = (f'<small>{E(lab)}</small>' if lab else "") + (f'<small>{verb} {links}</small>' if links else "")
                parts.append(f'<span class="io-chip">{E(t)}{sub}</span>')
            return "".join(parts)

        chain = f"""<div class="chain" data-stage="{E(stage)}" aria-label="How this skill chains with others">
  <div class="chain-col"><h3>Takes in</h3>{chips(s['consumes'], producers, 'From')}</div>
  <div class="chain-mid"><span class="chain-arrow" aria-hidden="true">→</span><div class="chain-self">{E(name)}</div><span class="chain-arrow" aria-hidden="true">→</span></div>
  <div class="chain-col"><h3>Produces</h3>{chips(s['produces'], consumers, 'Used by')}</div>
  <p class="chain-foot"><a href="/map/?skill={quote(name)}">{ICONS['map']} See it on the map</a></p>
</div>"""

        # Files shown on this page; links to them stay on the page.
        local = {f["rel"] for sub in ("_references", "_scripts", "_assets") for f in s[sub]}
        if s["_evals"]:
            local.add("evals/evals.json")

        sections_html = []
        for heading, text in s["_sections"].items():
            sid = slugify(heading)
            sections_html.append(f'<section class="skill-section" id="{E(sid)}"><h2>{E(heading)}</h2>\n{md_to_html(text, name, local)}</section>')
        skill_toc = [("install", "Install")] + [(slugify(h), h) for h in s["_sections"].keys()] + [("cite", "Cite this skill")]

        evals_html, evals_toc = render_evals(s)
        refs_html, refs_toc = render_references(s, local)
        scripts_html, scripts_toc = render_scripts(s)
        changelog_html, changelog_toc = render_changelog(s, local)

        # (key, tab label, count, panel html, toc entries)
        tabs = [("test-cases", "Test cases", str(len(s["_evals"])),
                 tab_intro("test-cases", "Test cases", s, "evals/evals.json") + evals_html, evals_toc)]
        if s["_references"]:
            tabs.append(("references", "References", str(len(s["_references"])),
                         tab_intro("references", "References", s, "references/") + refs_html, refs_toc))
        if s["_scripts"]:
            tabs.append(("scripts", "Scripts", str(len(s["_scripts"])),
                         tab_intro("scripts", "Scripts", s, "scripts/") + scripts_html, scripts_toc))
        if s["_assets"]:
            tabs.append(("assets", "Assets", str(len(s["_assets"])),
                         tab_intro("assets", "Assets", s, "assets/") + render_assets(s), [("assets", "Files")]))
        tabs.append(("version-history", "Version history", "",
                     tab_intro("version-history", "Version history", s, "CHANGELOG.md") + changelog_html, changelog_toc))

        # Reviews: feedback.js fills the list from /api/reviews; the GitHub link works without it.
        gh_reviews = f"{GITHUB}/issues?q=" + quote(f'is:issue label:expert-review in:title "{name}"')
        reviews_html = f"""{tab_intro("reviews", "Reviews", s)}
<section class="reviews-block" id="expert-reviews" aria-labelledby="expert-reviews-h">
  <h3 id="expert-reviews-h">Expert reviews</h3>
  <div class="review-list" data-expert-reviews><p class="muted">Expert reviews of this skill are kept as <a href="{E(gh_reviews)}" rel="noopener">issues on GitHub</a>.</p></div>
  <p class="reviews-foot"><a href="{E(gh_reviews)}" rel="noopener">See all expert reviews of this skill on GitHub</a></p>
</section>
<section class="reviews-block" id="ratings" aria-labelledby="ratings-h">
  <h3 id="ratings-h">Ratings and comments</h3>
  <div class="ratings" data-ratings><p class="muted">Ratings show here once the site can reach its database.</p></div>
</section>"""
        tabs.append(("reviews", "Reviews", "", reviews_html, [("expert-reviews", "Expert reviews"), ("ratings", "Ratings and comments")]))

        # What feedback.js needs: the skill, the build commit, and which version answered which issue.
        page_data = json.dumps({
            "name": name, "title": s["title"], "version": s["version"], "stage": stage, "repo": REPO,
            "commit": commit, "google_client_id": GOOGLE_CLIENT_ID, "changelog_refs": changelog_refs(s["_changelog"]),
        }, ensure_ascii=False).replace("</", "<\\/")

        warnings_html = ""
        if s["warnings"] or s["errors"]:
            items = "".join(f"<li>[{E(f['code'])}] {E(f['message'])}</li>" for f in s["errors"] + s["warnings"])
            warnings_html = f'<details class="validator-notes"><summary>Validator notes ({len(s["errors"])} error(s), {len(s["warnings"])} warning(s))</summary><ul>{items}</ul></details>'

        tags = " ".join(f'<a class="tag" href="/skills/?tag={quote(t)}">{E(t)}</a>' for t in s["tags"]) or '<span class="muted">none</span>'
        org = ORG_NAMES.get(s["org"], s["org"])

        banner = ""
        if status == "draft":
            banner = '<div class="banner banner-draft"><span>Draft. A maintainer hasn\'t reviewed this skill yet, so check its output carefully.</span></div>'
        elif status == "deprecated":
            banner = '<div class="banner banner-deprecated"><span>Deprecated. This skill is retired; its version history says what replaced it.</span></div>'

        skill_panel = f"""{tab_intro("skill", "Skill", s, "SKILL.md")}
  <aside class="callout" aria-labelledby="fires-h">
    <h2 id="fires-h" class="callout-title">When this skill runs</h2>
    <p>{E(s['description'])}</p>
  </aside>

  {chain}

  <section class="skill-section" id="install" aria-labelledby="install-h">
    <h2 id="install-h">Install</h2>
    {install_tabs("skill", s)}
  </section>

  {''.join(sections_html)}

  <section class="skill-section cite" id="cite"><h2>Cite this skill</h2>
    {copy_block(cite)}
    <p class="muted">Skills are fixed, versioned artifacts. Record the skill name and version in your project documentation the way you would register analysis code. See <a href="{GITHUB}/blob/main/docs/citing.md" rel="noopener">how to cite skills and workflows</a>, which follows Busara's <a href="https://busara.global/our-works/the-sifa-tool-for-a-statement-of-intellectual-fellowship-and-accountability/" rel="noopener">SIFA framework</a> for stating how humans and AI contributed.</p>
  </section>

  <p class="disclosure-line">Using this skill inside a commercial AI product sends what you type to that product's provider. Do not paste sensitive personal or proprietary data without understanding the product's terms. <a href="{GITHUB}/blob/main/DISCLOSURE.md" rel="noopener">Read the disclosure</a>.</p>"""
        tabs.insert(0, ("skill", "Skill", "", skill_panel, skill_toc))

        tab_buttons, panels, tocs = [], [], []
        for i, (key, label, count, panel_html, toc_items) in enumerate(tabs):
            on = i == 0
            cnt = f'<span class="ptab-count">{E(count)}</span>' if count else ""
            if key == "reviews":
                cnt = '<span class="ptab-count" data-review-count></span>'  # filled in by feedback.js
            selected = ' aria-selected="true"' if on else ' aria-selected="false" tabindex="-1"'
            tab_buttons.append(f'<button class="ptab" role="tab" type="button" id="t-{key}" data-tab="{key}" aria-controls="{panel_id(key)}"{selected}>{E(label)}{cnt}</button>')
            default = " data-default" if on else ""
            panels.append(f'<section class="ptab-panel" role="tabpanel" id="{panel_id(key)}" aria-labelledby="t-{key}"{default}>\n{panel_html}\n</section>')
            tocs.append(toc_list(key, toc_items, on))

        body = f"""
<article class="skill-page" data-stage="{E(stage)}">
<p class="breadcrumb"><a href="/skills/">skills</a><span aria-hidden="true">/</span><span>{E(name)}</span></p>
<header class="skill-head">
  <h1>{E(s['title'])}</h1>
  <p class="skill-name-row"><code>{E(name)}</code></p>
  <div class="badges">{pill(stage_labels.get(stage, stage) or 'no stage', 'stage', stage)}{pill('v' + s['version'], 'version')}{pill(s['type'] or 'atomic', 'meta' if s['type'] == 'meta' else 'type')}{pill(status, status)}{pill(org, 'org') if org else ''}</div>
  {banner}
  <p class="skill-what">{E(s['what_it_does'])}</p>
  <div class="skill-actions">
    <button class="btn" type="button" data-panel-open="review" aria-controls="fb-panel">{ICONS['pencil']} Review this skill</button>
    <button class="btn-secondary" type="button" data-panel-open="rate" aria-controls="fb-panel">{ICONS['star']} Rate this skill</button>
    <a class="rating-summary" href="#ratings" data-rating-summary hidden></a>
  </div>
  <p class="skill-actions-note">Expert reviews are for staff at The Agency Fund and Irrational Labs; anyone can rate. <a href="#expert-reviews" data-review-summary hidden></a></p>
</header>
<script type="application/json" id="skill-data">{page_data}</script>

<div class="skill-tabs" data-tabs="skill" data-tabs-url="tab">
<div class="ptabs-bar"><div class="ptabs" role="tablist" aria-label="Parts of this skill">{''.join(tab_buttons)}</div></div>

<div class="skill-layout">
<div class="skill-main">
{''.join(panels)}
</div>

<aside class="skill-side" aria-label="Skill details">
  <div class="side-actions">{add_button(name, s['title'], "add-btn add-btn-lg", "Add to workflow")}</div>
  <nav class="side-box toc" aria-label="On this page"><h2>On this page</h2>{''.join(tocs)}</nav>
  <div class="side-box">
    <h2>Details</h2>
    <dl class="meta">
      <dt>Authors</dt><dd>{E(authors)}</dd>
      <dt>Org</dt><dd>{E(org) or '<span class="muted">Not stated</span>'}</dd>
      <dt>Version</dt><dd>{E(s['version'])}</dd>
      <dt>Status</dt><dd>{E(status)}</dd>
      <dt>Stage</dt><dd><a href="/skills/?stage={E(stage)}">{E(stage_labels.get(stage, stage))}</a></dd>
      <dt>WEIRD</dt><dd>{E(weird_labels.get(s['weird'], s['weird'])) or '<span class="muted">not stated</span>'}</dd>
      <dt>Tests</dt><dd><a href="#test-cases">{s['eval_count']} test cases</a></dd>
      <dt>License</dt><dd>{E(s['license'])}</dd>
      <dt>Source</dt><dd><a href="{E(s['source_url'])}" rel="noopener">skills/{E(name)}</a></dd>
      <dt>Changed</dt><dd>{E(s['latest_date']) or '<span class="muted">Not stated</span>'}</dd>
    </dl>
    <h2 class="side-sub">Tags</h2>
    <div>{tags}</div>
    {warnings_html}
  </div>
</aside>
</div>
</div>
</article>
"""
        page(s["url"], s["title"], s["what_it_does"] or s["description"][:200], body, page_class="page-skill", scripts=("/feedback.js",))


def build_workflows(workflows: List[dict], skills: List[dict], taxonomy: dict) -> None:
    by_name = {s["name"]: s for s in skills}
    stage_labels = label_map(taxonomy.get("stages"))
    items = []
    for w in workflows:
        items.append(
            f'<li class="wf-item"><h2><a href="{E(w["url"])}">{E(w["title"])}</a></h2>'
            f'<p>{E(workflow_lead(w))}</p>{workflow_graph(w, by_name)}</li>')
    items.append(
        '<li class="wf-item wf-build"><h2><a href="/workflows/build/">Build your own</a></h2>'
        '<p>Pick skills from the list or the map, put them in order, and get the install commands and a prompt to run them.</p>'
        f'<p><a class="btn" href="/workflows/build/">Build a workflow {ICONS["arrow"]}</a></p></li>')
    body = f"""
<div class="page-head">
  <h1>Workflows</h1>
  <p class="lede">A workflow is a set of skills for a bigger job. It says which run first, which can run side by side, and where a person has to decide.</p>
</div>
<ul class="wf-list">{''.join(items)}</ul>
<p class="muted">Want to write one for the library? Start from <a href="{GITHUB}/blob/main/workflows/WORKFLOW-TEMPLATE.md" rel="noopener">the workflow template</a>.</p>
"""
    page("/workflows/", "Workflows", "Sets of behavioral-science skills for bigger jobs, with the order and the decision points stated.", body)

    for w in workflows:
        names = [n for n in w["skills"] if n in by_name]
        stages = ", ".join(stage_labels.get(x, x) for x in w["stages"])
        meta = ", ".join(x for x in [", ".join(w["authors"]), ORG_NAMES.get(w["org"], w["org"])] if x)
        wbody = f"""
<article class="skill-page">
<p class="breadcrumb"><a href="/workflows/">workflows</a><span aria-hidden="true">/</span><span>{E(w['name'])}</span></p>
<header class="skill-head">
<h1>{E(w['title'])}</h1>
<p class="skill-name-row"><code>{E(w['name'])}</code></p>
<div class="badges">{pill('v' + w['version'], 'version') if w['version'] else ''}{pill(w['status'] or 'draft', w['status'] or 'draft')}{pill(stages, 'org') if stages else ''}</div>
<p class="skill-what">{E(w['description'])}</p>
<p class="muted">{E(meta)}. <a href="{E(w['source_url'])}" rel="noopener">Source</a></p>
</header>
<section class="wf-overview" aria-labelledby="wf-skills-h">
  <h2 id="wf-skills-h">How the skills connect</h2>
  {workflow_graph(w, by_name)}
  <div class="wf-actions">
    <button class="btn" type="button" data-load-workflow="{E(','.join(names))}">{ICONS['plus']} Open in builder</button>
  </div>
  <h3>Install these {len(names)} skills</h3>
  <p class="muted">In Claude Code, the plugin already includes them. With other agents:</p>
  {copy_block(install_skills_cmd(names))}
</section>
<div class="skill-section prose">{md_to_html(w['body'])}</div>
</article>
"""
        page(w["url"], w["title"], w["description"] or w["title"], wbody)


def build_workflow_builder() -> None:
    body = f"""
<div class="page-head">
  <p class="breadcrumb"><a href="/workflows/">workflows</a><span aria-hidden="true">/</span><span>build</span></p>
  <h1>Build a workflow</h1>
  <p class="lede">Put your skills in order. Between steps you'll see what each skill passes on, or a note where nothing does.</p>
</div>
<div class="builder" id="builder" data-repo="{E(REPO)}" data-plugin="{E(PLUGIN)}" data-github="{E(GITHUB)}">
  <p class="builder-loading muted">Loading…</p>
</div>
<noscript><p class="note">The workflow builder needs JavaScript. You can still browse the <a href="/workflows/">workflows</a> and <a href="/skills/">skills</a>.</p></noscript>
"""
    page("/workflows/build/", "Build a workflow", "Put behavioral-science skills in order, see what each passes to the next, and get the commands to install and run them.", body,
         page_class="page-builder")



def build_install() -> None:
    body = f"""
<div class="page-head">
  <h1>Install</h1>
  <p class="lede">Every option installs the same skills. Only Claude Code updates them for you. With the others, you re-run the command or re-upload the file when a skill changes.</p>
</div>

<div class="steps">
<section class="step" id="claude-code">
  <h2>Claude Code <span class="pill pill-meta">recommended</span></h2>
  <p>Installs the whole library as one plugin. Turn on auto-update for the marketplace and it stays current; otherwise run <code>/plugin update</code> now and then.</p>
  {copy_block(f"/plugin marketplace add {REPO}")}
  {copy_block(f"/plugin install {PLUGIN}@{PLUGIN}")}
  <p>Then describe what you're working on. The navigator answers behavioral-science questions, and a skill runs when you name its method. Type <code>/besci-navigator</code> to call the navigator directly.</p>
</section>

<section class="step" id="agents">
  <h2>Codex, Cursor, Copilot, Gemini CLI, OpenCode and more</h2>
  <p>The <code>skills</code> CLI reads this repository's plugin manifest and installs into whichever agents it finds.</p>
  {copy_block(f"npx skills add {REPO} --all", "Everything")}
  {copy_block(f"npx skills add {REPO} --skill besci-navigator --skill besci-eval", "Just the two meta-skills")}
  <p>Update with <code>npx skills update</code>. For agents with their own plugin marketplaces, re-run the install command to update until we have verified each one's update path.</p>
</section>

<section class="step" id="desktop">
  <h2>Claude Desktop and claude.ai <span class="pill">no terminal</span></h2>
  <ol>
    <li>Open the skill's page in the catalog and click <strong>Download &lt;name&gt;.skill</strong>. Start with <a href="/skills/besci-navigator/">besci-navigator</a> and <a href="/skills/besci-eval/">besci-eval</a>.</li>
    <li>In Claude, open <strong>Settings → Capabilities → Skills → Upload skill</strong> and choose the file.</li>
    <li>Enable it, then ask Claude to do the thing the skill does.</li>
  </ol>
  <p><strong>Zip installs do not update themselves.</strong> Each skill carries its version number; compare it with the catalog page before relying on an old copy, and watch <a href="/whats-new/">What's new</a> or the <a href="/feed.xml">RSS feed</a> for releases. Re-upload to update; Claude replaces the old copy.</p>
  <p><strong>Org admins on Claude for Work:</strong> an admin can upload skills once for the whole organization and re-upload on release, which is as close to auto-update as Desktop gets.</p>
</section>
</div>

<p>To see what changed recently, check <a href="/whats-new/">What's new</a>. To install only some skills, pick them on the <a href="/skills/">Skills page</a> and <a href="/workflows/build/">build a workflow</a>; it gives you the install command for just those.</p>

<div class="note">
  <strong>Before you use any skill.</strong> Using a skill inside a commercial AI product sends what you type to that product's provider. Do not paste sensitive personal or proprietary data without understanding the product's terms. Skills can also be read as an educational resource: learn the method and apply it in your own non-AI workflow. <a href="{GITHUB}/blob/main/DISCLOSURE.md" rel="noopener">Read the full disclosure</a>.
</div>
"""
    page("/install/", "Install", "How to install behavioral-science skills in Claude Code, other coding agents, Claude Desktop, and claude.ai.", body)


def build_contribute() -> None:
    body = f"""
<div class="page-head">
  <h1>Turn a method into a skill</h1>
  <p class="lede">A skill covers one method, narrow enough to describe in a sentence without the word "and". <a href="{GITHUB}/blob/main/docs/skill-spec.md" rel="noopener">The full spec</a> lists everything else a skill has to include.</p>
</div>

<div class="steps">
<section class="step">
  <h2>Claim or propose</h2>
  <p>Check the <a href="/skills/">catalog</a> for something that already covers it. Then <a href="/propose/">propose the skill</a>, which opens a pre-filled GitHub issue so a maintainer can confirm it is atomic before you write it.</p>
</section>

<section class="step">
  <h2>Draft it with besci-skill-creator</h2>
  <p>Install <a href="/skills/besci-skill-creator/"><code>besci-skill-creator</code></a> and say "I want to create a skill for ...". It interviews you against the spec, starting with the atomicity test and the trigger rule, drafts the whole folder (<code>SKILL.md</code>, three test cases, a changelog), runs the validator, does one self-test pass, and packages a <code>.skill</code> file where the environment allows. You can also copy <a href="{GITHUB}/tree/main/template/skill-template" rel="noopener">the template</a> and write by hand.</p>
</section>

<section class="step">
  <h2>Validate</h2>
  <p>The same validator runs in the creator skill, in CI, and on upload, so what passes locally passes everywhere:</p>
  {copy_block("uv run scripts/besci_validate.py skills/<your-skill-name>")}
  <p>Exit 0 means the structure is right. A maintainer still reviews the content.</p>
</section>

<section class="step">
  <h2>Submit it</h2>
  <ol>
    <li><strong>Hand it to a maintainer.</strong> Share the <code>.skill</code> file on Slack or Drive. The maintainer submits it on your behalf; you stay credited in the <code>authors</code> field and on the commit.</li>
    <li><strong>Upload it, no git.</strong> Use the <a href="/upload/">upload form</a> (TAF and IL staff have a contributor key), or open <a href="{GITHUB}/tree/main/inbox" rel="noopener"><code>inbox/</code></a> on GitHub, choose <em>Add file → Upload files</em>, drop the <code>.skill</code> file, and pick <em>Create a new branch and start a pull request</em>. An action unpacks it into <code>skills/</code>, runs the validator, and posts a plain-language checklist on the pull request.</li>
    <li><strong>Clone and open a pull request.</strong> Put the folder under <code>skills/</code>, run the validator, push a branch, open a PR.</li>
  </ol>
</section>

<section class="step">
  <h2>Review</h2>
  <p>Every pull request needs green CI and one approving review from a maintainer, who checks the content against the spec: is it atomic, does the trigger rule name what it should not handle, is the evidence real and the WEIRD note honest, does the output template match what the skill promises, are the failure modes and the escalation point concrete, do the test cases read like real requests. On merge the skill is marked <code>published</code> and appears here. See <a href="{GITHUB}/blob/main/CONTRIBUTING.md" rel="noopener">CONTRIBUTING.md</a> for the reviewer checklist.</p>
  <p>You can also review and rate skills that are already in the library, right here on the site, and you don't need a GitHub account for it. Open any skill from the <a href="/skills/">catalog</a> and go to its Reviews tab. If you work at TAF or IL, sign in with your work Google account and click <em>Review this skill</em>: pick a verdict, mark the parts of the skill your review concerns, and say what should change. The site files it as a GitHub issue for the maintainers, and the skill page later shows which version answered it. Anyone with a Google account can rate a skill from one to five stars and leave a comment, under their name or anonymously.</p>
</section>
</div>

<div class="two-col">
  <div class="panel"><h3>Propose a skill</h3><p>A short form that opens a pre-filled GitHub issue. A maintainer confirms the idea is atomic before you write it.</p><p><a class="btn-secondary" href="/propose/">Propose {ICONS['arrow']}</a></p></div>
  <div class="panel"><h3>Upload a skill</h3><p>Already have a <code>.skill</code> file? Upload it with your contributor key and we open the pull request for you.</p><p><a class="btn-secondary" href="/upload/">Upload {ICONS['arrow']}</a></p></div>
</div>

<div class="note">
  <strong>Before you contribute.</strong> Your published skill content will be processed by third-party AI systems when others use it. You set your own terms for what goes in; you can revise or deprecate your skill at any time through version control. Skill content is licensed CC BY 4.0, code MIT. <a href="{GITHUB}/blob/main/DISCLOSURE.md" rel="noopener">Read the disclosure</a>.
</div>
"""
    page("/contribute/", "Contribute", "How to propose, draft, validate, and submit a behavioral-science skill.", body)


def build_propose(taxonomy: dict) -> None:
    stage_opts = "".join(
        f'<option value="{E(str(x.get("id")))}">{E(str(x.get("label")))}: {E(str(x.get("description", "")))}</option>'
        for x in taxonomy.get("stages", []) if isinstance(x, dict)
    )
    body = f"""
<div class="page-head">
  <h1>Propose a skill</h1>
  <p class="lede">Fill this in and it opens a pre-filled GitHub issue (you need a GitHub account to submit it). A maintainer confirms the idea is atomic before you write the skill, so nobody drafts something that would be sent back.</p>
</div>
<form id="propose-form" class="form" data-repo="{E(REPO)}">
  <label>Title <span class="muted">(human-readable, e.g. "COM-B barrier decomposer")</span>
    <input type="text" name="title" required maxlength="120"></label>
  <label>What it does <span class="muted">(one sentence, no "and")</span>
    <input type="text" name="what" required maxlength="300"></label>
  <label>Stage
    <select name="stage" required><option value="">Choose a stage</option>{stage_opts}</select></label>
  <label>Why it is atomic <span class="muted">(what it takes in, what it produces, what it deliberately does not do)</span>
    <textarea name="atomicity" rows="4" required></textarea></label>
  <label>Evidence base <span class="muted">(the framework, paper, or practice it draws on; a citation or link if you have one)</span>
    <textarea name="evidence" rows="4" required></textarea></label>
  <label>Your name and organization
    <input type="text" name="contact" required maxlength="120"></label>
  <p><button class="btn" type="submit">Open the pre-filled GitHub issue {ICONS['arrow']}</button></p>
  <p class="muted">Opens in a new tab. If GitHub drops some fields, paste them into the issue by hand.</p>
</form>
"""
    page("/propose/", "Propose a skill", "Propose an atomic behavioral-science skill via a pre-filled GitHub issue.", body)


def build_upload() -> None:
    body = f"""
<div class="page-head">
  <h1>Upload a skill</h1>
  <p class="lede">Upload the <code>.skill</code> file that <code>besci-skill-creator</code> gave you. We validate it, unpack it into <code>skills/</code>, and open a pull request for a maintainer to review. You get a link to the pull request and the validator's report.</p>
</div>
<form id="upload-form" class="form" enctype="multipart/form-data" method="post" action="/api/submit">
  <label>Contributor key
    <input type="password" name="contributor_key" required autocomplete="off">
    <span class="muted">Given to TAF and IL staff during Phase 1. Ask a maintainer if you need one.</span></label>
  <label>Your name <input type="text" name="author_name" required maxlength="120"></label>
  <label>Your GitHub handle <span class="muted">(optional, to be credited on the commit)</span>
    <input type="text" name="author_github" maxlength="60" pattern="[A-Za-z0-9-]*"></label>
  <label>Organization
    <select name="org" required><option value="TAF">The Agency Fund</option><option value="IL">Irrational Labs</option><option value="community">Community</option></select></label>
  <label>Skill file <span class="muted">(.skill or .zip, under 10 MB, one skill folder inside)</span>
    <input type="file" name="file" accept=".skill,.zip" required></label>
  <label class="check"><input type="checkbox" name="disclosure_ack" value="yes" required>
    <span>I have read the <a href="{GITHUB}/blob/main/DISCLOSURE.md" rel="noopener" target="_blank">disclosure</a> and understand my skill content will be processed by third-party AI systems when others use it.</span></label>
  <p><button class="btn" type="submit" id="upload-submit">Validate and open a pull request</button> <span id="upload-spinner" class="spinner" hidden aria-hidden="true"></span></p>
</form>
<div id="upload-result" aria-live="polite"></div>
<p class="muted">Prefer not to use the form? Open <a href="{GITHUB}/tree/main/inbox" rel="noopener"><code>inbox/</code></a> on GitHub and use <em>Add file → Upload files</em>; the same validator runs on the pull request.</p>
"""
    page("/upload/", "Upload a skill", "Upload a .skill file; it is validated and turned into a pull request.", body)


def build_whats_new(skills: List[dict]) -> None:
    dated = sorted(skills, key=lambda s: (s["latest_date"] or "", s["name"]), reverse=True)
    items = []
    for s in dated:
        change_md = re.sub(r"^\s*#{1,6} .*\n", "", s["latest_change"] or "", count=1).strip()
        latest = md_to_html(change_md) if change_md else "<p class='muted'>No changelog entry.</p>"
        items.append(
            f'<li class="news-item"><span class="news-date">{E(s["latest_date"]) or "undated"}</span>'
            f'<h3><a href="{E(s["url"])}">{E(s["title"])}</a> <code>{E(s["name"])}</code> <span class="muted" style="font-size:.8rem">v{E(s["version"])}</span></h3>'
            f'<div class="news-body">{latest}</div></li>')
    body = f"""
<div class="page-head">
  <h1>What's new</h1>
  <p class="lede">Recent skill changes, newest first. Each change bumps the skill's version, so a project can cite the exact version it used. The <a href="/feed.xml">RSS feed</a> announces new releases.</p>
</div>
<ul class="news">{''.join(items) or '<li class="muted">Nothing yet.</li>'}</ul>
"""
    page("/whats-new/", "What's new", "Latest changes to skills in the Behavioral Science Skills Library.", body)


def build_about(skills: List[dict]) -> None:
    by_name = {s["name"]: s for s in skills}

    def meta_panel(n: str, fallback: str) -> str:
        s = by_name.get(n)
        if s:
            return f'<div class="panel"><h3><a href="{E(s["url"])}">{E(s["title"])}</a></h3><p><code>{E(n)}</code></p><p>{E(s["what_it_does"])}</p></div>'
        return f'<div class="panel"><h3>{E(n)}</h3><p>{E(fallback)}</p></div>'

    def sl(n: str) -> str:
        """A skill name in code, linked to its page when the skill exists."""
        return f'<a href="{E(by_name[n]["url"])}"><code>{E(n)}</code></a>' if n in by_name else f"<code>{E(n)}</code>"

    def principle(title: str, body: str, practice: str) -> str:
        """One principle card, closed by default: the memorandum's heading, opening to its paragraph as written and where the library carries it out."""
        return (f'<details class="panel principle"><summary><h3>{title}</h3>'
                f'<span class="principle-more" aria-hidden="true"><span class="more">Read more</span><span class="less">Show less</span></span></summary>'
                f'<div class="principle-body"><p>{body}</p><p class="principle-practice"><b>In the library:</b> {practice}</p></div></details>')

    # Word for word from the TAF and IL memorandum of understanding, section 2. Edit the
    # memorandum first if the wording needs to change.
    principles = "\n    ".join([
        principle(
            "Contributors can set their own terms.",
            "We provide a general guideline to help skill authors contribute to the library. However, contributors have full control over what they’d like to put in the skills, whether it involves publicly available information or knowledge that is traditionally more gated. Contributions are also version-controlled, so that a contributor can revise or deprecate their own skill.",
            "authors are credited in the skill's metadata and changelog, including when a maintainer submits it for them. Deprecated skills stay in the history, so projects that cited them can still find them."),
        principle(
            "Use of the library should follow open science guidelines.",
            "Because each skill is a fixed, versioned artifact, teams can document which skills and which workflows (i.e., combinations of skills) they used in a project, much like registering analysis code on OSF. This also aligns with Busara’s <a href=\"https://busara.global/our-works/the-sifa-tool-for-a-statement-of-intellectual-fellowship-and-accountability/\" rel=\"noopener\">SIFA</a> framework for documenting how humans and AI contribute to the production of knowledge. We encourage both skill authors and users to follow these principles when creating, adapting, or applying skills in their work.",
            f"see <a href=\"{GITHUB}/blob/main/docs/citing.md\" rel=\"noopener\">how to cite a skill</a>, and use {sl('draft-sifa-declaration')} to write the SIFA statement for your project."),
        principle(
            "Skills do not replace experts.",
            "Most behavioral scientists work at universities, tech companies, international organizations, or some NGOs. Most of the organizations running programs at scale in low- and middle-income countries have never had access to one. Along with broader support on hiring behavioral scientists for NGOs, we also want to build interim support for NGO practitioners who currently play a role adjacent to a behavioral scientist. A skill library is especially an amplifier for this group: it gives a practitioner a good starting point and helps them learn by doing. We also intend to build a skill module that informs users when the question has outgrown the tool, and they should bring in a specialist. For the experts themselves, skills are a distribution channel for their methods and a way to make their frameworks applied repeatedly. For both groups, we want to be explicit that the library is meant to provide practical value where that value is useful, not to replace human behavioral scientists. The skills are deliberately designed around atomic problems with relatively clear and technical solutions, while real-world research projects involve complex judgments that cannot be fully captured by any AI skills or AI models.",
            f"every skill ends with “When to bring in a specialist”, and the {sl('besci-navigator')} checks those points before it recommends anything."),
        principle(
            "Users and contributors need to be informed about what may be shared with AI providers.",
            "Although the skills themselves are open-source artifacts, using them inside a commercial AI product may require users to provide a third-party model provider with data that it otherwise could not access from users. Therefore, we should clearly disclose this distinction to both users and contributors, encourage users not to provide sensitive personal or proprietary information without understanding the terms of the AI product they are using, and make clear to contributors that their published skill content may be processed by third-party AI systems when others use it. For users who are uncomfortable transferring their work or expertise into an AI system through skills, the library should also be usable as an educational resource where users can use the skills to learn and practice a method, then apply the underlying procedure in their own non-AI workflows.",
            f"the <a href=\"{GITHUB}/blob/main/DISCLOSURE.md\" rel=\"noopener\">disclosure</a> spells this out, and every skill can be read on this site without installing anything."),
    ])

    # Who it is for: the four personas, each with an avatar (site/src/assets/personas/).
    # app.js brings the avatars in once and replays each one's gesture on hover or tap.
    personas = [
        ("learner", "Learners", "People in the public who want to learn about behavioral science."),
        ("practitioner", "Practitioners", "Program designers, product managers, designers, and others who practice behavioral science in their work without formal training in it."),
        ("researcher", "Industry researchers", "UX researchers, M&amp;E researchers, and others who use behavioral science in their research without having formally studied it."),
        ("expert", "Experts", "Behavioral scientists and academic scholars whose job is to study and practice behavioral science."),
    ]
    persona_cards = "\n    ".join(
        f'<div class="persona persona-{key}" style="--i:{i}">{inline_svg(f"personas/{key}.svg")}<h3>{name}</h3><p>{who}</p></div>'
        for i, (key, name, who) in enumerate(personas))

    # How it's run: the broad stages from the memorandum's roadmap. The current stage is
    # the last one whose start date has passed when the site is built.
    stages = [
        (dt.date(2026, 9, 1), "Fall 2026", "Build and test in-house", "The Agency Fund and Irrational Labs write the first skills and try the review process on their own work."),
        (dt.date(2026, 12, 1), "December 2026", "Launch the first version", "The first library of skills goes public, with tutorials and webinars to help people start."),
        (dt.date(2027, 1, 1), "2027", "Co-build with experts", "Invited experts and applied organizations add their own skills and workflows, and rate the ones already here."),
        (None, "Later", "Open to everyone", "Anyone can propose a skill, and a wider coalition of behavioral science groups helps curate the library."),
    ]
    today = dt.date.today()
    now = max((i for i, s in enumerate(stages) if s[0] and s[0] <= today), default=0)
    rm_items = []
    for i, (_, when, title, text) in enumerate(stages):
        state = "is-done" if i < now else "is-now" if i == now else "is-next"
        current = ' aria-current="step"' if i == now else ""
        here = ' <span class="rm-here">Now</span>' if i == now else ""
        rm_items.append(f'<li class="rm-step {state}" style="--i:{i}"{current}><span class="rm-track" aria-hidden="true"><span class="rm-seg"></span><span class="rm-dot"></span></span>'
                        f'<p class="rm-when">{when}{here}</p><h3>{title}</h3><p>{text}</p></li>')
    roadmap = "\n    ".join(rm_items)

    body = f"""
<div class="page-head">
  <h1>About</h1>
  <p class="lede">The Behavioral Science Skills Library is a free, open-source set of AI skills for people who want to practice behavioral science with the help of AI in their daily work. The initial skills and workflows were co-developed by <a href="https://agency.fund" rel="noopener">The Agency Fund</a> and <a href="https://irrationallabs.com" rel="noopener">Irrational Labs</a>. We aim to build this library toward a broader community-driven resource with inputs and contributions from both scholars and practictioners. </p>
</div>

<section class="section about-first">
  <h2>Why we built this</h2>
  <div class="prose">
    <p>Imagine a researcher or a practitioner at an NGO running a large program in a low- or middle-income country. The next phase starts in six weeks. They want to draw on behavioral science in their intervention design, but don't have months to read across disciplines, chase down papers behind paywalls, or consult an expert every time a new question comes up. So they do what most practitioners do: define the problem, look for something useful, try it, and adjust as they go. </p>
    
    <p>The process might look "quick and dirty" from an eye of an academic scholar, but that's just the reality of working in the real world: you have to tinker through rapid trials and errors. Given the circumstances, our big question is: how do we help these people, knowing what we know and what the field knows about behavioral science as a discipline?</p>

    <p>Part of the problem is that the knowledge is scattered. Similar ideas appear under different names across psychology, economics, education, public health, and other fields, each with its own preferred theories and frameworks. Walter Mischel wrote about this <a href="https://www.psychologicalscience.org/observer/the-toothbrush-problem" target="_blank" rel="noopener noreferrer">"toothbrush problem"</a> many years ago: scholars (and psychologists especially) tend to treat other people's theories like toothbrushes, something they'd rather not use. The result is a lot of parallel work and reinventing the wheel. You remember reading about a useful method somewhere, but can't quite recall where or how it worked. Or you develop your own approach without realizing that someone else has already solved a similar problem.</p>

    <p>We don't think everyone needs to agree on one grand theory of human behavior. But at the level of practical tasks, there is a lot we can share: defining a target behavior, identifying barriers, choosing an intervention technique, designing a measure, or planning a test.</p>
    
    <p>Today's AI is incredibly useful for applying these methods. But as you probably notice in your own work, AI can very easily go astray without proper guidance. Hence, we're turning these common methods into small, structured, and reusable skills that an AI assistant can work through with its users. Each skill is documented with its sources, reviewed by someone familiar with the method, and designed to be applied to a real problem.</p>

    <p>We're also taking an open-source approach because we don't think this library should belong to any one team or organization. We hope researchers, practitioners, and others in the behavioral science community will contribute methods, review one another's work, and improve the skills over time. If we can agree on and share even some of the basic ways we work, we can spend less time reinventing methods and more time learning from and building on each other's work.</p>
  </div>
</section>

<section class="section">
  <h2>Who it is for</h2>
  <div class="prose">
    <p>In the social sector, having a behavioral scientist or an academic scholar in the room is a luxury. Most organizations have never had one. Even in the tech sector, many teams do not have a designated user experience researcher (UXR) playing the role of a behavioral scientist. We built the library for the people who carry that line of work in their teams. With an AI assistant and skills written down by experts and other practitioners, they can do more of it themselves, get more capable at it, and know when to bring in a specialist for tasks beyond the scope of the AI skills.</p>
    <p>The skills won't cover every problem, and we wish to be open about this. Each one handles a narrow task with a fairly clear answer, while real projects are full of judgment calls that no skill or AI model can make for you. Hence, every skill ends with a section called “When to bring in a specialist”, which names the situations that need one, the kind of expert to bring in, and what to hand them. When you reach that point, we at The Agency Fund and Irrational Labs, or other organizations like <a href="https://findmybesci.com" rel="noopener">Find My BeSci</a> can also help match your organizations with behavioral scientists.</p>
  </div>
  <p class="prose">The library is built for four kinds of people, and all of them can benefit from using it.</p>
  <div class="personas">
    {persona_cards}
  </div>
</section>

<section class="section">
  <h2>What's in a skill</h2>
  <div class="prose">
    <p>A skill is a folder of instructions, scripts, and resources that an AI assistant loads when a task calls for it. That's Anthropic's definition. They introduced the format for Claude (see <a href="https://support.claude.com/en/articles/12512176-what-are-skills" rel="noopener">What are skills?</a> and <a href="https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills" rel="noopener">Equipping agents for the real world with Agent Skills</a>), and it is now an <a href="https://agentskills.io" rel="noopener">open standard</a> that many other AI tools read. Until your request matches a skill, the assistant sees only its name and a short description. When it matches, the assistant loads the full instructions and follows them.</p>
    <p>Our bar for a useful skill is higher than a good prompt. It covers one method, narrow enough to state in a sentence without “and”. It asks about your situation before it produces anything. It names the framework or evidence it is built on, and how far that evidence has been tested outside <a href="https://pubmed.ncbi.nlm.nih.gov/20550733/" target="_blank" rel="noopener noreferrer">"Western, Educated, Industrialized, Rich, and Democratic (WEIRD)"</a> samples. It says when not to use it, how it tends to go wrong, and when to bring in a specialist. Its output follows a fixed template, so you know what you'll get. And it carries a version number and a changelog, so a project can cite exactly what it used.</p>
    <p>Take the saying-is-believing technique, where students write advice to future students and come to believe the message themselves. How to run it well is published, but spread across several papers. {sl("draft-belonging-story")} puts that procedure in one place, so the assistant helps you adapt it to your students instead of improvising from its own memory of the internet. A manual or a checklist does the same job. The difference is that a skill runs, inside the assistant you already use, on your own context.</p>
  </div>
  <div class="two-col">
    <div class="panel">
      <pre class="tree">skills/decompose-comb-barriers/
├── <b>SKILL.md</b>          <span class="c">trigger rule, stage, version, WEIRD status,</span>
│                     <span class="c">then eight fixed sections, from "What it</span>
│                     <span class="c">does" to "When to bring in a specialist"</span>
├── <b>evals/evals.json</b>  <span class="c">realistic prompts + expected output shape</span>
├── <b>CHANGELOG.md</b>      <span class="c">one entry per version</span>
└── <b>references/</b>       <span class="c">optional detail, loaded on demand</span></pre>
      <p>The full contract is in <a href="{GITHUB}/blob/main/docs/skill-spec.md" rel="noopener">the skill spec</a>. A validator enforces it in CI, on upload, and inside the creator skill.</p>
    </div>
    <div class="panel">
      <h3>The rule for scope</h3>
      <p>One thing a behavioral scientist does, narrow enough to say in one sentence without “and”. If your sentence needs an “and”, you have two skills, and the second usually takes the first one's output.</p>
      <div class="compare">
        <div class="yes"><h3>Atomic</h3><ul><li>Decompose a defined behavior into COM-B barrier hypotheses</li><li>Draft a saying-is-believing exercise for a target population</li><li>Design a measure of user agency using Social Cognitive Theory</li></ul></div>
        <div class="no"><h3>Too broad</h3><ul><li>Design a behavior change program</li><li>Apply behavioral science to a chatbot</li><li>Analyze this program and tell me what's wrong</li></ul></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <h2>Meta-skills for using the library</h2>
  <p class="prose">If you don't know which skill you need, start with the navigator. If you want to examine how good a particular skill is, use the evaluator. IF you want to create a new skill, use the skill creator.</p>
  <div class="two-col">
    {meta_panel("besci-navigator", "Recommends which skills to run, in what order.")}
    {meta_panel("besci-eval", "Checks a skill's structure, triggering, and output quality.")}
    {meta_panel("besci-skill-creator", "Interviews an author and drafts the whole skill folder.")}
  </div>
</section>

<section class="section">
  <h2>Principles</h2>
  <p class="prose">We expect a fair question from users who have concerns about AI as a medium for knowledge dissemination: <em>are you extracting expert judgment into a machine so that organizations can stop paying for experts?</em> We wish to make sure that we address this concern and implement suitable guidelines when building the first version of the library.</p>
  <div class="principles">
    {principles}
  </div>
</section>

<section class="section">
  <h2>How it's run</h2>
  <div class="prose">
    <p>The Agency Fund and Irrational Labs co-own the library, and neither can relicense, rename, or shut it down without the other. The code is MIT-licensed and the skill content is CC BY 4.0, so you can use, adapt, and share a skill as long as you credit its authors. A maintainer reviews every skill before it is published, and the maintainers re-check published skills every quarter. Once a skill is live, anyone can rate it from its page, and staff at both organizations can file an expert review.</p>
    <p>The library opens up in stages, from the two founding teams to anyone who wants to contribute.</p>
  </div>
  <ol class="roadmap">
    {roadmap}
  </ol>
  <p class="prose">Roles and rules are in <a href="{GITHUB}/blob/main/GOVERNANCE.md" rel="noopener">GOVERNANCE.md</a> and <a href="{GITHUB}/blob/main/MAINTAINERS.md" rel="noopener">MAINTAINERS.md</a>.</p>
  <p class="hero-actions"><a class="btn-secondary" href="{GITHUB}" rel="noopener">{ICONS['github']} Source on GitHub</a> <a class="btn-secondary" href="/contribute/">Contribute a skill</a></p>
</section>
"""
    page("/about/", "About", "Why the Behavioral Science Skills Library exists, who it is for, what a skill is, and the principles behind it.", body, page_class="page-about")


def build_404() -> None:
    body = """
<div class="page-head">
  <h1>Page not found</h1>
  <p class="lede">That page does not exist. Try the <a href="/skills/">catalog</a> or the <a href="/">home page</a>.</p>
</div>
"""
    write("404.html", layout("Not found", "Page not found.", body, "/404.html"))


# ---------------------------------------------------------------------------
# Data files
# ---------------------------------------------------------------------------

def rfc822(date_str: str) -> str:
    try:
        d = dt.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        d = dt.datetime(1970, 1, 1)
    return d.strftime("%a, %d %b %Y 00:00:00 +0000")


def build_data(skills: List[dict], workflows: List[dict], taxonomy: dict) -> None:
    public_skills = []
    for s in skills:
        p = {k: val for k, val in s.items() if not k.startswith("_")}
        public_skills.append(p)
    public_workflows = [{k: val for k, val in w.items() if k != "body"} for w in workflows]
    catalog = {
        "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "repo": REPO,
        "site_url": SITE_URL,
        "taxonomy": taxonomy_public(taxonomy),
        "skills": public_skills,
        "workflows": public_workflows,
    }
    write("data/catalog.json", json.dumps(catalog, indent=2, ensure_ascii=False))

    # A small file for the map, the workflow tray, and the builder: catalog.json is too heavy to load on every page.
    lite = {
        "stages": [{"id": str(x.get("id")), "label": str(x.get("label")), "description": str(x.get("description") or "")}
                   for x in taxonomy.get("stages", []) if isinstance(x, dict)],
        "io_types": [{"id": str(x.get("id")), "label": str(x.get("label") or x.get("id")), "user_suppliable": bool(x.get("user_suppliable"))}
                     for x in taxonomy.get("io_types", []) if isinstance(x, dict)],
        "skills": [{k: s[k] for k in ("name", "title", "stage", "type", "what_it_does", "url", "download_url", "consumes", "produces", "version")}
                   for s in skills],
        "workflows": [{"name": w["name"], "title": w["title"], "url": w["url"], "skills": w["skills"]} for w in workflows],
    }
    write("data/skills.json", json.dumps(lite, ensure_ascii=False, separators=(",", ":")))

    lines = [
        f"# {SITE_NAME}",
        "",
        f"{TAGLINE} By The Agency Fund and Irrational Labs.",
        f"Repository: {GITHUB}",
        f"Catalog JSON: {SITE_URL}/data/catalog.json",
        "",
        "## Skills",
        "",
    ]
    for s in skills:
        lines.append(f"- {s['name']} [{s['stage']}, {s['type']}, {s['status']}]: {s['what_it_does']} ({SITE_URL}{s['url']})")
    if workflows:
        lines += ["", "## Workflows", ""]
        for w in workflows:
            lines.append(f"- {w['name']}: {w['description']} ({SITE_URL}{w['url']})")
    write("llms.txt", "\n".join(lines) + "\n")

    dated = sorted(skills, key=lambda s: (s["latest_date"] or "", s["name"]), reverse=True)
    items = []
    for s in dated:
        desc = f"{s['what_it_does']}\n\n{s['latest_change']}".strip()
        items.append(
            "<item>"
            f"<title>{E(s['title'])} v{E(s['version'])}</title>"
            f"<link>{E(SITE_URL + s['url'])}</link>"
            f"<guid isPermaLink=\"false\">{E(s['name'])}@{E(s['version'])}</guid>"
            f"<pubDate>{rfc822(s['latest_date'])}</pubDate>"
            f"<description>{E(desc)}</description>"
            "</item>"
        )
    feed = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0"><channel>'
        f"<title>{E(SITE_NAME)}: what's new</title>"
        f"<link>{E(SITE_URL)}/whats-new/</link>"
        "<description>New and updated skills in the Behavioral Science Skills Library.</description>"
        f"<lastBuildDate>{rfc822(dated[0]['latest_date']) if dated and dated[0]['latest_date'] else rfc822('1970-01-01')}</lastBuildDate>"
        + "".join(items) + "</channel></rss>\n"
    )
    write("feed.xml", feed)

    urls = ["/", "/skills/", "/map/", "/workflows/", "/workflows/build/", "/install/", "/contribute/", "/propose/", "/upload/", "/whats-new/", "/about/"]
    urls += [s["url"] for s in skills] + [w["url"] for w in workflows]
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        + "".join(f"<url><loc>{E(SITE_URL + u)}</loc></url>" for u in urls)
        + "</urlset>\n"
    )
    write("sitemap.xml", sitemap)
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    taxonomy = v.load_taxonomy(os.path.join(ROOT, "taxonomy.yaml"))
    skills = load_skills(taxonomy)
    workflows = load_workflows()

    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST, exist_ok=True)
    if os.path.isdir(SRC):
        shutil.copytree(SRC, DIST, dirs_exist_ok=True)
    else:
        sys.stderr.write(f"warning: {SRC} not found; building without stylesheet or scripts\n")

    build_index(skills, taxonomy, workflows)
    build_catalog(skills, taxonomy)
    build_map()
    build_skill_pages(skills, taxonomy)
    build_workflows(workflows, skills, taxonomy)
    build_workflow_builder()
    build_install()
    build_contribute()
    build_propose(taxonomy)
    build_upload()
    build_whats_new(skills)
    build_about(skills)
    build_404()
    build_data(skills, workflows, taxonomy)

    n_err = sum(len(s["errors"]) for s in skills)
    print(f"Built {len(skills)} skill page(s) and {len(workflows)} workflow page(s) into {os.path.relpath(DIST, ROOT)}/")
    if n_err:
        print(f"note: {n_err} validator error(s) across skills; pages were still built. Run besci_validate.py for details.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
