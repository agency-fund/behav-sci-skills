#!/usr/bin/env python3
"""
build_site.py — builds the static catalog site into site/dist/.

Reads:  skills/*/SKILL.md, workflows/*.md, taxonomy.yaml, site/src/
Writes: site/dist/ (gitignored): HTML pages, data/catalog.json, llms.txt,
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
import sys
from typing import Dict, List, Optional
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import besci_validate as v  # noqa: E402

from markdown_it import MarkdownIt  # noqa: E402

ROOT = v.find_repo_root(os.path.dirname(os.path.abspath(__file__))) or os.getcwd()
SITE_URL = os.environ.get("SITE_URL", "https://behav-sci-skills.vercel.app").rstrip("/")
REPO = "agency-fund/behav-sci-skills"
GITHUB = f"https://github.com/{REPO}"
PLUGIN = "behav-sci-skills"
SITE_NAME = "Behavioral Science Skills"
SRC = os.path.join(ROOT, "site", "src")
DIST = os.path.join(ROOT, "site", "dist")
SKILLS_DIR = os.path.join(ROOT, "skills")
WORKFLOWS_DIR = os.path.join(ROOT, "workflows")
NON_WORKFLOW_FILES = {"README.md", "WORKFLOW-TEMPLATE.md"}
START_HERE = ["besci-navigator", "besci-eval"]
FONTS = "https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400;500&family=Montserrat:wght@400;500;600;700;800&display=swap"

MD = MarkdownIt("commonmark", {"html": True, "linkify": False}).enable(["table", "strikethrough"])

E = html.escape

# Inline icons (Lucide-style, stroke = currentColor).
ICONS = {
    "github": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .5C5.65.5.5 5.65.5 12c0 5.08 3.29 9.39 7.86 10.91.58.1.79-.25.79-.56v-2.17c-3.2.7-3.87-1.37-3.87-1.37-.52-1.33-1.28-1.68-1.28-1.68-1.04-.71.08-.7.08-.7 1.15.08 1.76 1.19 1.76 1.19 1.03 1.76 2.69 1.25 3.35.96.1-.75.4-1.25.73-1.54-2.55-.29-5.24-1.28-5.24-5.68 0-1.26.45-2.28 1.19-3.09-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.17 1.18a11 11 0 0 1 5.77 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.23 2.76.11 3.05.74.81 1.19 1.83 1.19 3.09 0 4.41-2.69 5.38-5.26 5.67.41.36.78 1.06.78 2.14v3.17c0 .31.21.67.8.56A11.5 11.5 0 0 0 23.5 12C23.5 5.65 18.35.5 12 .5z"/></svg>',
    "sun": '<svg class="ic-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>',
    "moon": '<svg class="ic-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
    "copy": '<svg class="ic-copy" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg>',
    "check": '<svg class="ic-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5L20 7"/></svg>',
    "grid": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>',
    "map": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="5" cy="6" r="2.5"/><circle cx="19" cy="6" r="2.5"/><circle cx="12" cy="18" r="2.5"/><path d="M7 7.5c2 2 3.5 5 5 8M17 7.5c-2 2-3.5 5-5 8"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "download": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12M6 11l6 6 6-6M4 21h16"/></svg>',
}

THEME_SCRIPT = (
    "<script>(function(){var t=null;try{t=localStorage.getItem('theme')}catch(e){}"
    "document.documentElement.setAttribute('data-theme',t==='light'?'light':'dark');})()</script>"
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


def md_to_html(text: str, skill_name: Optional[str] = None) -> str:
    """Render markdown. Relative links into a skill's own files go to GitHub."""
    if skill_name:
        base = f"{GITHUB}/blob/main/skills/{skill_name}/"
        text = re.sub(
            r"\]\(((?:references|scripts|assets|evals)/[^)\s]+)\)",
            lambda m: f"]({base}{m.group(1)})",
            text,
        )
    out = MD.render(text)
    if skill_name:
        base = f"{GITHUB}/blob/main/skills/{skill_name}/"
        out = re.sub(
            r"<code>((?:references|scripts|assets|evals)/[A-Za-z0-9_./-]+)</code>",
            lambda m: f'<a href="{base}{m.group(1)}" rel="noopener"><code>{m.group(1)}</code></a>',
            out,
        )
    return out


def changelog_dates(changelog: Optional[str]) -> List[str]:
    if not changelog:
        return []
    return re.findall(r"^## \S+\s*-\s*(\d{4}-\d{2}-\d{2})", changelog, flags=re.MULTILINE)


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
            "skills": v.split_list(md.get("skills")),
            "url": f"/workflows/{name}/",
            "source_url": f"{GITHUB}/blob/main/workflows/{fname}",
            "body": body,
        })
    return out


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
    ("Skills", "/"),
    ("Workflows", "/workflows/"),
    ("Install", "/install/"),
    ("Contribute", "/contribute/"),
    ("What's new", "/whats-new/"),
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


def layout(title: str, description: str, body: str, path: str, extra_head: str = "", page_class: str = "") -> str:
    nav = "".join(
        f'<a href="{E(href)}"{" aria-current=\"page\"" if href == path else ""}>{E(label)}</a>'
        for label, href in NAV
    )
    full_title = f"{title} · {SITE_NAME}" if title != SITE_NAME else f"{SITE_NAME}: an open library of atomic AI skills"
    canonical = f"{SITE_URL}{path}"
    logos = logos_html()
    return f"""<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(full_title)}</title>
<meta name="description" content="{E(description)}">
<meta name="color-scheme" content="dark light">
<meta name="theme-color" content="#000000">
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
{extra_head}
</head>
<body class="{E(page_class)}">
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-row">
    <a class="brand" href="/" aria-label="{E(SITE_NAME)} home">
      {logos}
      <span class="brand-sep" aria-hidden="true"></span>
      <span class="brand-name">{E(SITE_NAME)}</span>
    </a>
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
    <div class="footer-grid">
      <div class="footer-brand">
        {logos}
        <p>An open library of small, single-purpose AI skills that put behavioral-science methods into the daily work of social-sector teams. Co-owned by The Agency Fund and Irrational Labs.</p>
      </div>
      <div class="footer-col">
        <h4>Library</h4>
        <a href="/">Skills</a>
        <a href="/?view=map">Skill map</a>
        <a href="/workflows/">Workflows</a>
        <a href="/whats-new/">What's new</a>
        <a href="/feed.xml">RSS feed</a>
      </div>
      <div class="footer-col">
        <h4>Use</h4>
        <a href="/install/">Install</a>
        <a href="/contribute/">Contribute</a>
        <a href="/propose/">Propose a skill</a>
        <a href="/upload/">Upload a skill</a>
        <a href="{GITHUB}/blob/main/docs/citing.md" rel="noopener">How to cite</a>
      </div>
      <div class="footer-col">
        <h4>Project</h4>
        <a href="/about/">About</a>
        <a href="{GITHUB}" rel="noopener">GitHub</a>
        <a href="{GITHUB}/blob/main/DISCLOSURE.md" rel="noopener">Disclosure</a>
        <a href="{GITHUB}/blob/main/GOVERNANCE.md" rel="noopener">Governance</a>
        <a href="/llms.txt">llms.txt</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>Skill content CC BY 4.0 · code MIT · <a href="{GITHUB}/blob/main/LICENSE" rel="noopener">licenses</a></span>
      <span><a href="https://agency.fund" rel="noopener">agency.fund</a> · <a href="https://irrationallabs.com" rel="noopener">irrationallabs.com</a></span>
    </div>
  </div>
</footer>
<script src="/app.js" defer></script>
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


def install_tabs(key: str, skill: Optional[dict] = None, compact: bool = False) -> str:
    """Three-tab install block. One localStorage key so the user's tool choice follows them."""
    names = [skill["name"]] if skill else START_HERE
    flags = " ".join(f"--skill {n}" for n in names)
    if skill:
        downloads = f'<p><a class="btn" href="{E(skill["download_url"])}" rel="noopener">{ICONS["download"]} Download {E(skill["name"])}.skill</a></p>'
    else:
        downloads = "<p>" + " ".join(
            f'<a class="btn-secondary" href="{GITHUB}/releases/latest/download/{n}.skill" rel="noopener">{ICONS["download"]} {n}.skill</a>'
            for n in names) + "</p>"
    intro_cc = "" if compact else "<p>Installs the whole library as one plugin. Turn on auto-update and it stays current.</p>"
    intro_ag = "" if compact else "<p>Codex, Cursor, Copilot, Gemini CLI, OpenCode and others, through the <code>skills</code> CLI.</p>"
    intro_dt = "<p>Upload the file under <strong>Settings → Capabilities → Skills</strong>. Zip installs do not update themselves; check <a href=\"/whats-new/\">What's new</a> now and then.</p>"
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


def card(s: dict, stage_labels: Dict[str, str]) -> str:
    status = s["status"] or "draft"
    stage = s["stage"] or ""
    search = " ".join([s["name"], s["title"], s["description"], s["what_it_does"], " ".join(s["tags"])]).lower()
    kind = "meta" if s["type"] == "meta" else ""
    top_label = "Meta skill" if s["type"] == "meta" else (stage_labels.get(stage, stage) or "Stage?")
    status_pill = "" if status == "published" else pill(status, "status-" + status if False else status)
    org = ORG_NAMES.get(s["org"], s["org"])
    return f"""<article class="card" data-name="{E(s['name'])}" data-stage="{E(stage)}" data-type="{E(s['type'])}" data-org="{E(s['org'])}" data-status="{E(status)}" data-tags="{E(' '.join(s['tags']))}" data-search="{E(search)}">
  <div class="card-top"><span class="dot" aria-hidden="true"></span><span>{E(top_label)}</span><span class="spacer"></span>{status_pill}</div>
  <h3><a href="{E(s['url'])}">{E(s['title'])}</a></h3>
  <p class="card-name">{E(s['name'])}</p>
  <p class="card-desc">{E(s['what_it_does'])}</p>
  <div class="card-foot"><span>{E(org)}</span><span>v{E(s['version'])}</span><span class="spacer"></span><span>{s['eval_count']} test case{'s' if s['eval_count'] != 1 else ''}</span></div>
</article>"""


def filters_html(skills: List[dict], taxonomy: dict) -> str:
    stages = [(str(x.get("id")), str(x.get("label"))) for x in taxonomy.get("stages", []) if isinstance(x, dict)]
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
    <input type="search" id="q" name="q" placeholder="Search skills…" autocomplete="off" spellcheck="false"><kbd>/</kbd></label>
  <label><span class="sr-only">Stage</span><select class="select" id="f-stage" name="stage">{opts(stages, 'All stages')}</select></label>
  <label><span class="sr-only">Type</span><select class="select" id="f-type" name="type">{opts([('atomic', 'Atomic'), ('meta', 'Meta')], 'Atomic and meta')}</select></label>
  <label><span class="sr-only">Organization</span><select class="select" id="f-org" name="org">{opts(org_opts, 'All orgs')}</select></label>
  <label><span class="sr-only">Status</span><select class="select" id="f-status" name="status">{opts([('published', 'Published'), ('draft', 'Draft'), ('deprecated', 'Deprecated')], 'All statuses')}</select></label>
  <label><span class="sr-only">Tag</span><select class="select" id="f-tag" name="tag">{opts(tags, 'All tags')}</select></label>
  <button type="button" id="f-clear" class="btn-ghost">Clear</button>
  <span class="filter-count" id="f-count" aria-live="polite"></span>
</form>"""


def quoted_examples(skills: List[dict], limit: int = 4) -> List[str]:
    """User-voice examples from the navigator's 'Use it when' list, for the hero demo."""
    nav = next((s for s in skills if s["name"] == "besci-navigator"), None)
    out: List[str] = []
    for line in (nav or {}).get("use_when", []) or []:
        m = re.match(r'^\s*["“](.+?)["”]\s*$', str(line))
        if m:
            out.append(m.group(1).strip())
        if len(out) >= limit:
            break
    return out or ["Mothers stop coming to our nutrition sessions after the third visit. Where do I start?"]


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def build_index(skills: List[dict], taxonomy: dict) -> None:
    stage_labels = label_map(taxonomy.get("stages"))
    stage_descs = desc_map(taxonomy.get("stages"))
    by_name = {s["name"]: s for s in skills}
    counts: Dict[str, int] = {}
    for s in skills:
        counts[s["stage"]] = counts.get(s["stage"], 0) + 1

    n_skills = len(skills)
    n_stages = len({s["stage"] for s in skills if s["stage"] and s["stage"] != "other"})
    n_tests = sum(int(s["eval_count"] or 0) for s in skills)
    n_authors = len({a.strip() for s in skills for a in s["authors"] if a.strip()})

    examples = quoted_examples(skills)
    start_cards = []
    for i, n in enumerate(START_HERE):
        s = by_name.get(n)
        if s:
            start_cards.append(
                f'<a class="mini" href="{E(s["url"])}"><span class="mini-ic" aria-hidden="true">{i + 1}</span>'
                f'<span><b>{E(s["title"])}</b><code>{E(n)}</code><span>{E(s["what_it_does"])}</span></span></a>')
        else:
            start_cards.append(f'<span class="mini"><span class="mini-ic">{i + 1}</span><span><b>{E(n)}</b><span>Coming soon.</span></span></span>')

    strip = []
    for i, st in enumerate([x for x in taxonomy.get("stages", []) if isinstance(x, dict) and x.get("id") != "other"]):
        sid = str(st.get("id"))
        strip.append(
            f'<li><button class="stage-btn" type="button" data-stage="{E(sid)}" data-label="{E(str(st.get("label")))}" '
            f'data-desc="{E(stage_descs.get(sid, ""))}" aria-pressed="false">'
            f'<span class="stage-k">{i + 1:02d}</span><span class="stage-l">{E(str(st.get("label")))}</span>'
            f'<span class="stage-n">{counts.get(sid, 0)} skill{"s" if counts.get(sid, 0) != 1 else ""}</span></button></li>')
    n_meta = sum(1 for s in skills if s["type"] == "meta")
    stage_default = f"Seven stages, from defining a behavior to scaling what worked, plus {n_meta} meta-skills that work on the library itself."

    cards = "\n".join(card(s, stage_labels) for s in skills)
    nav_skill = by_name.get("besci-navigator")
    nav_link = f'<a href="{E(nav_skill["url"])}">besci-navigator</a>' if nav_skill else "besci-navigator"

    body = f"""
<section class="hero">
  <div class="hero-grid">
    <div>
      <p class="eyebrow reveal" style="--i:0"><span class="dot" aria-hidden="true" style="--stage: var(--accent)"></span>Open library · The Agency Fund × Irrational Labs</p>
      <h1 class="reveal" style="--i:1">Behavioral science, <span class="accent">one skill</span> at a time.</h1>
      <p class="lede reveal" style="--i:2">Small, single-purpose AI skills that put behavioral-science methods into the daily work of social-sector teams. Each one does one thing a behavioral scientist does, cites its evidence, asks before it answers, and says when to bring in a specialist.</p>
      <p class="hero-actions reveal" style="--i:3"><a class="btn" href="/install/">Install {ICONS['arrow']}</a> <a class="btn-secondary" href="#catalog">Browse {n_skills} skills</a> <a class="btn-ghost" href="/about/">How it works</a></p>
    </div>
    <div class="demo reveal" style="--i:2" aria-label="Example: asking the navigator">
      <div class="demo-bar"><span class="demo-dots" aria-hidden="true"><span></span><span></span><span></span></span><span>claude · besci-navigator</span></div>
      <div class="demo-body">
        <div class="demo-line"><span class="demo-prompt" aria-hidden="true">›</span><span><span id="demo-text" data-examples="{E(json.dumps(examples))}"></span><span class="demo-cursor" aria-hidden="true"></span></span></div>
        <p class="demo-reply"><span class="arrow">↳</span> Describe the problem in plain words. {nav_link} picks the skills and the order, asks at most one question, and says when the library has nothing for a step.</p>
      </div>
    </div>
  </div>
  <div class="stats reveal" style="--i:4" aria-label="Library at a glance">
    <div class="stat"><div class="stat-n" data-count="{n_skills}">{n_skills}</div><div class="stat-l">skills</div></div>
    <div class="stat"><div class="stat-n" data-count="{n_stages}">{n_stages}</div><div class="stat-l">stages covered</div></div>
    <div class="stat"><div class="stat-n" data-count="{n_tests}">{n_tests}</div><div class="stat-l">test cases</div></div>
    <div class="stat"><div class="stat-n" data-count="{n_authors}">{n_authors}</div><div class="stat-l">contributors</div></div>
  </div>
</section>

<section class="section" aria-labelledby="stages-h">
  <div class="section-head">
    <div><p class="eyebrow">By stage</p><h2 id="stages-h">Where are you in the project?</h2><p>Skills are organized by where in a project they are used. Pick a stage to filter the catalog.</p></div>
  </div>
  <ul class="stage-strip">{''.join(strip)}</ul>
  <p class="stage-desc" id="stage-desc" data-default="{E(stage_default)}">{E(stage_default)}</p>
</section>

<section class="section start" aria-labelledby="start-h">
  <div>
    <p class="eyebrow">Start here</p>
    <h2 id="start-h">Install two meta-skills first</h2>
    <p>The navigator tells you which skills to run and in what order. The evaluator checks whether a skill is doing its job on the model you use. Everything else can wait until the navigator sends you there.</p>
    <div class="start-skills">{''.join(start_cards)}</div>
  </div>
  <div>
    {install_tabs("home")}
    <p class="muted" style="font-size:.82rem;margin:.7rem 0 0">Then ask: <em>“Where do I start?”</em> and describe your problem. <a href="/install/">All install options</a>.</p>
  </div>
</section>

<section class="section" id="catalog" aria-labelledby="catalog-h">
  <div class="section-head">
    <div><p class="eyebrow">Catalog</p><h2 id="catalog-h">All skills</h2><p>Every skill is one thing a behavioral scientist does, with its evidence, its output shape, and its escalation point. Switch to the map to see how skills chain: one skill's output is the next one's input.</p></div>
    <div class="view-toggle" role="group" aria-label="View">
      <button type="button" data-view="cards" aria-pressed="true">{ICONS['grid']} Cards</button>
      <button type="button" data-view="map" aria-pressed="false">{ICONS['map']} Map</button>
    </div>
  </div>
  {filters_html(skills, taxonomy)}
  <div class="grid" id="grid">
{cards}
  </div>
  <div class="map" id="map" hidden aria-label="Skill chain map"></div>
  <p id="no-results" class="no-results" hidden>No skills match. <button type="button" class="link-btn" id="f-clear-2">Clear filters</button> or <a href="/propose/">propose the one you need</a>.</p>
</section>
"""
    page("/", SITE_NAME, "An open library of atomic AI skills for behavioral science, by The Agency Fund and Irrational Labs.", body, page_class="page-index")


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
                sub = ""
                if lab or links:
                    sub = f'<small>{E(lab)}' + (f' · {verb} {links}' if links else "") + "</small>"
                parts.append(f'<span class="io-chip">{E(t)}{sub}</span>')
            return "".join(parts)

        chain = f"""<div class="chain" data-stage="{E(stage)}" aria-label="How this skill chains with others">
  <div class="chain-col"><h3>Takes in</h3>{chips(s['consumes'], producers, 'from')}</div>
  <div class="chain-mid"><span class="chain-arrow" aria-hidden="true">→</span><div class="chain-self">{E(name)}</div><span class="chain-arrow" aria-hidden="true">→</span></div>
  <div class="chain-col"><h3>Produces</h3>{chips(s['produces'], consumers, 'used by')}</div>
</div>"""

        sections_html = []
        for heading, text in s["_sections"].items():
            sid = slugify(heading)
            sections_html.append(f'<section class="skill-section" id="{E(sid)}"><h2>{E(heading)}</h2>\n{md_to_html(text, name)}</section>')
        toc = "".join(f'<li><a href="#{E(slugify(h))}">{E(h)}</a></li>' for h in s["_sections"].keys())

        changelog_md = re.sub(r"^# .*\n", "", s["_changelog"], count=1).strip()
        changelog_html = md_to_html(changelog_md) if changelog_md else "<p class='muted'>No changelog.</p>"

        warnings_html = ""
        if s["warnings"] or s["errors"]:
            items = "".join(f"<li>[{E(f['code'])}] {E(f['message'])}</li>" for f in s["errors"] + s["warnings"])
            warnings_html = f'<details class="validator-notes"><summary>Validator notes ({len(s["errors"])} error(s), {len(s["warnings"])} warning(s))</summary><ul>{items}</ul></details>'

        tags = " ".join(f'<a class="tag" href="/?tag={quote(t)}">{E(t)}</a>' for t in s["tags"]) or '<span class="muted">none</span>'
        top_label = "Meta skill" if s["type"] == "meta" else stage_labels.get(stage, stage)
        org = ORG_NAMES.get(s["org"], s["org"])

        banner = ""
        if status == "draft":
            banner = '<div class="banner banner-draft"><span>Draft: this skill has not yet been reviewed by a maintainer. Use with care and send feedback.</span></div>'
        elif status == "deprecated":
            banner = '<div class="banner banner-deprecated"><span>Deprecated: this skill is retired. See its version history for what replaced it.</span></div>'

        body = f"""
<article class="skill-page" data-stage="{E(stage)}">
<p class="breadcrumb"><a href="/">skills</a><span aria-hidden="true">/</span><span>{E(name)}</span></p>
<header class="skill-head">
  <p class="eyebrow"><span class="dot" aria-hidden="true"></span>{E(top_label)} · <span class="keep">v{E(s['version'])}</span></p>
  <h1>{E(s['title'])}</h1>
  <p class="skill-name-row"><code>{E(name)}</code></p>
  <div class="badges">{pill(stage_labels.get(stage, stage) or 'stage?', 'stage', stage)}{pill(s['type'] or 'atomic', 'meta' if s['type'] == 'meta' else 'type')}{pill(status, status)}{pill(org, 'org') if org else ''}</div>
  {banner}
  <p class="skill-what">{E(s['what_it_does'])}</p>
</header>

<div class="skill-layout">
<div class="skill-main">
  <aside class="callout" aria-labelledby="fires-h">
    <h2 id="fires-h" class="callout-title">When this skill fires</h2>
    <p>{E(s['description'])}</p>
  </aside>

  {chain}

  <section class="skill-section" id="install" aria-labelledby="install-h">
    <h2 id="install-h">Install</h2>
    {install_tabs("skill", s)}
  </section>

  {''.join(sections_html)}

  <section class="skill-section" id="version-history"><h2>Version history</h2>{changelog_html}</section>

  <section class="skill-section cite" id="cite"><h2>Cite this skill</h2>
    {copy_block(cite)}
    <p class="muted">Skills are fixed, versioned artifacts. Record the skill name and version in your project documentation the way you would register analysis code. See <a href="{GITHUB}/blob/main/docs/citing.md" rel="noopener">how to cite skills and workflows</a>, which follows Busara's <a href="https://busara.global/our-works/the-sifa-tool-for-a-statement-of-intellectual-fellowship-and-accountability/" rel="noopener">SIFA framework</a> for stating how humans and AI contributed.</p>
  </section>

  <p class="disclosure-line">Using this skill inside a commercial AI product sends what you type to that product's provider. Do not paste sensitive personal or proprietary data without understanding the product's terms. <a href="{GITHUB}/blob/main/DISCLOSURE.md" rel="noopener">Read the disclosure</a>.</p>
</div>

<aside class="skill-side" aria-label="Skill details">
  <nav class="side-box toc" aria-label="On this page"><h2>On this page</h2><ol><li><a href="#install">Install</a></li>{toc}<li><a href="#version-history">Version history</a></li><li><a href="#cite">Cite this skill</a></li></ol></nav>
  <div class="side-box">
    <h2>Details</h2>
    <dl class="meta">
      <dt>Authors</dt><dd>{E(authors)}</dd>
      <dt>Org</dt><dd>{E(org) or '<span class="muted">—</span>'}</dd>
      <dt>Version</dt><dd>{E(s['version'])}</dd>
      <dt>Status</dt><dd>{E(status)}</dd>
      <dt>Stage</dt><dd><a href="/?stage={E(stage)}">{E(stage_labels.get(stage, stage))}</a></dd>
      <dt>WEIRD</dt><dd>{E(weird_labels.get(s['weird'], s['weird'])) or '<span class="muted">not stated</span>'}</dd>
      <dt>Tests</dt><dd>{s['eval_count']} in <a href="{GITHUB}/blob/main/skills/{E(name)}/evals/evals.json" rel="noopener">evals.json</a></dd>
      <dt>License</dt><dd>{E(s['license'])}</dd>
      <dt>Source</dt><dd><a href="{E(s['source_url'])}" rel="noopener">skills/{E(name)}</a></dd>
      <dt>Changed</dt><dd>{E(s['latest_date']) or '<span class="muted">—</span>'}</dd>
    </dl>
    <h2 style="margin-top:.9rem">Tags</h2>
    <div>{tags}</div>
    {warnings_html}
  </div>
</aside>
</div>
</article>
"""
        page(s["url"], s["title"], s["what_it_does"] or s["description"][:200], body, page_class="page-skill")


def build_workflows(workflows: List[dict]) -> None:
    if workflows:
        items = "".join(
            f'<li class="wf-item"><h3><a href="{E(w["url"])}">{E(w["title"])}</a> <code>{E(w["name"])}</code></h3>'
            f'<p>{E(w["description"])}</p><p class="muted">{E(", ".join(w["authors"]))}{" · " if w["authors"] else ""}{E(w["org"])}{" · v" + E(w["version"]) if w["version"] else ""}</p></li>'
            for w in workflows
        )
        listing = f'<ul class="wf-list">{items}</ul>'
    else:
        listing = f"""<div class="empty-state">
  <p><strong>No workflows yet.</strong> The first ones will come from <code>besci-navigator</code> in guide mode and from contributors in Phase 2.</p>
  <p>Want to write one? Copy <a href="{GITHUB}/blob/main/workflows/WORKFLOW-TEMPLATE.md" rel="noopener">the workflow template</a> and open a pull request. Or open the <a href="/?view=map">skill map</a> to see which skills already chain.</p>
</div>"""
    body = f"""
<div class="page-head">
  <p class="eyebrow">Workflows</p>
  <h1>Skills in sequence</h1>
  <p class="lede">A workflow is a recommended set of skills for a larger task, with the relationships between them stated: which runs first, which can run in parallel, which are independent, and where a human decides. A workflow can be as light as "use these three, in any order, but A before B".</p>
</div>
{listing}
<p class="muted">Workflows live in <a href="{GITHUB}/tree/main/workflows" rel="noopener"><code>workflows/</code></a>, never in <code>skills/</code>, because everything in <code>skills/</code> is atomic.</p>
"""
    page("/workflows/", "Workflows", "Recommended sets of behavioral-science skills with their relationships stated.", body)
    for w in workflows:
        wbody = f"""
<article class="skill-page">
<p class="breadcrumb"><a href="/workflows/">workflows</a><span aria-hidden="true">/</span><span>{E(w['name'])}</span></p>
<header class="skill-head">
<p class="eyebrow">Workflow{' · v' + E(w['version']) if w['version'] else ''}</p>
<h1>{E(w['title'])}</h1>
<p class="skill-name-row"><code>{E(w['name'])}</code></p>
<p class="skill-what">{E(w['description'])}</p>
<p class="muted">{E(', '.join(w['authors']))}{' · ' if w['authors'] else ''}{E(ORG_NAMES.get(w['org'], w['org']))} · <a href="{E(w['source_url'])}" rel="noopener">source</a></p>
</header>
<div class="skill-section prose">{md_to_html(w['body'])}</div>
</article>
"""
        page(w["url"], w["title"], w["description"] or w["title"], wbody)


def build_install() -> None:
    body = f"""
<div class="page-head">
  <p class="eyebrow">Install</p>
  <h1>Pick the tool you use</h1>
  <p class="lede">Every path installs the same skills. Claude Code keeps itself updated; the others need a re-run or a re-upload when a skill changes.</p>
</div>

<div class="steps">
<section class="step">
  <h2>Claude Code <span class="pill pill-meta">recommended</span></h2>
  <p>Installs the whole library as one plugin. Turn on auto-update for the marketplace and it stays current; otherwise run <code>/plugin update</code> now and then.</p>
  {copy_block(f"/plugin marketplace add {REPO}")}
  {copy_block(f"/plugin install {PLUGIN}@{PLUGIN}")}
  <p>Then just describe what you are trying to do. The navigator fires on behavioral-science questions; individual skills fire when you name their method. Type <code>/besci-navigator</code> to call it directly.</p>
</section>

<section class="step">
  <h2>Codex, Cursor, Copilot, Gemini CLI, OpenCode and more</h2>
  <p>The <code>skills</code> CLI reads this repository's plugin manifest and installs into whichever agents it finds.</p>
  {copy_block(f"npx skills add {REPO} --all", "Everything")}
  {copy_block(f"npx skills add {REPO} --skill besci-navigator --skill besci-eval", "Just the two meta-skills")}
  <p>Update with <code>npx skills update</code>. For agents with their own plugin marketplaces, re-run the install command to update until we have verified each one's update path.</p>
</section>

<section class="step">
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

<div class="note">
  <strong>Before you use any skill.</strong> Using a skill inside a commercial AI product sends what you type to that product's provider. Do not paste sensitive personal or proprietary data without understanding the product's terms. Skills can also be read as an educational resource: learn the method and apply it in your own non-AI workflow. <a href="{GITHUB}/blob/main/DISCLOSURE.md" rel="noopener">Read the full disclosure</a>.
</div>
"""
    page("/install/", "Install", "How to install behavioral-science skills in Claude Code, other coding agents, Claude Desktop, and claude.ai.", body)


def build_contribute() -> None:
    body = f"""
<div class="page-head">
  <p class="eyebrow">Contribute</p>
  <h1>Turn a method into a skill</h1>
  <p class="lede">A skill is one thing a behavioral scientist does, narrow enough to describe in a sentence without the word "and". It cites its evidence, asks before it answers, shows its output shape, names its failure modes, and says when to bring in a specialist. <a href="{GITHUB}/blob/main/docs/skill-spec.md" rel="noopener">Read the full spec</a>.</p>
</div>

<div class="steps">
<section class="step">
  <h2>Claim or propose</h2>
  <p>Check the <a href="/">catalog</a> for something that already covers it. Then <a href="/propose/">propose the skill</a>, which opens a pre-filled GitHub issue so a maintainer can confirm it is atomic before you write it.</p>
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
  <h2>Submit, three ways</h2>
  <ol>
    <li><strong>Hand it to a maintainer.</strong> Share the <code>.skill</code> file on Slack or Drive. The maintainer submits it on your behalf; you stay credited in the <code>authors</code> field and on the commit.</li>
    <li><strong>Upload it, no git.</strong> Use the <a href="/upload/">upload form</a> (TAF and IL staff have a contributor key), or open <a href="{GITHUB}/tree/main/inbox" rel="noopener"><code>inbox/</code></a> on GitHub, choose <em>Add file → Upload files</em>, drop the <code>.skill</code> file, and pick <em>Create a new branch and start a pull request</em>. An action unpacks it into <code>skills/</code>, runs the validator, and posts a plain-language checklist on the pull request.</li>
    <li><strong>Clone and open a pull request.</strong> Put the folder under <code>skills/</code>, run the validator, push a branch, open a PR.</li>
  </ol>
</section>

<section class="step">
  <h2>Review</h2>
  <p>Every pull request needs green CI and one approving review from a maintainer, who checks the content against the spec: is it atomic, does the trigger rule name what it should not handle, is the evidence real and the WEIRD note honest, does the output template match what the skill promises, are the failure modes and the escalation point concrete, do the test cases read like real requests. On merge the skill is marked <code>published</code> and appears here. See <a href="{GITHUB}/blob/main/CONTRIBUTING.md" rel="noopener">CONTRIBUTING.md</a> for the reviewer checklist.</p>
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
  <p class="eyebrow">Contribute · step 1</p>
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
  <p class="eyebrow">Contribute · submit</p>
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
  <p class="eyebrow">What's new</p>
  <h1>Every change is a version</h1>
  <p class="lede">Each change to a skill bumps its version and adds a changelog entry, so a project can cite exactly what it used. Newest first. Subscribe to the <a href="/feed.xml">RSS feed</a> to hear about releases.</p>
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

    body = f"""
<div class="page-head">
  <p class="eyebrow">About</p>
  <h1>Behavioral science you can install</h1>
  <p class="lede">The Behavioral Science Skills Library is a curated, open-source collection of small, single-purpose AI skills that put behavioral-science methods into the daily work of social-sector teams. It is co-owned by <a href="https://agency.fund" rel="noopener">The Agency Fund</a> and <a href="https://irrationallabs.com" rel="noopener">Irrational Labs</a>.</p>
</div>

<section class="section" style="margin-top:2.5rem">
  <p class="eyebrow">Who it is for</p>
  <h2>Teams without a behavioral scientist in the room</h2>
  <p class="prose">A program designer, product manager, or M&amp;E lead at an NGO who does not have a behavioral scientist on call. Each skill is one thing a behavioral scientist does: decompose a defined behavior into COM-B barriers, draft a cognitive interview script, design a measure of agency. It cites the evidence it draws on, asks before it answers, produces a predictable output, records where it goes wrong, and says when to bring in a specialist.</p>
  <p class="prose"><strong>Skills amplify practitioners; they do not replace experts.</strong> Read the <a href="{GITHUB}/blob/main/DISCLOSURE.md" rel="noopener">disclosure</a> before pasting sensitive data into any AI product.</p>
</section>

<section class="section">
  <p class="eyebrow">What a skill is</p>
  <h2>A folder, a contract, and a test suite</h2>
  <div class="two-col">
    <div class="panel">
      <pre class="tree">skills/decompose-comb-barriers/
├── <b>SKILL.md</b>          <span class="c">trigger rule, stage, version, WEIRD status,</span>
│                     <span class="c">then eight fixed sections, from "What it does"</span>
│                     <span class="c">to "When to bring in a specialist"</span>
├── <b>evals/evals.json</b>  <span class="c">realistic prompts + expected output shape</span>
├── <b>CHANGELOG.md</b>      <span class="c">one entry per version</span>
└── <b>references/</b>       <span class="c">optional detail, loaded on demand</span></pre>
    </div>
    <div class="panel">
      <h3>The rule for scope</h3>
      <p>One thing a behavioral scientist does, narrow enough to say in one sentence without "and". If your sentence needs an "and", you have two skills; the second usually takes the first's output as input.</p>
      <div class="compare">
        <div class="yes"><h3>Atomic</h3><ul><li>Decompose a defined behavior into COM-B barrier hypotheses</li><li>Draft a saying-is-believing exercise for a target population</li><li>Design a measure of user agency using Social Cognitive Theory</li></ul></div>
        <div class="no"><h3>Too broad</h3><ul><li>Design a behavior change program</li><li>Apply behavioral science to a chatbot</li><li>Analyze this program and tell me what's wrong</li></ul></div>
      </div>
      <p>The full contract is in <a href="{GITHUB}/blob/main/docs/skill-spec.md" rel="noopener">the skill spec</a>; a validator enforces it in CI, on upload, and inside the creator skill.</p>
    </div>
  </div>
</section>

<section class="section">
  <p class="eyebrow">Meta-skills</p>
  <h2>Three skills that work on the library itself</h2>
  <div class="two-col">
    {meta_panel("besci-navigator", "Recommends which skills to run, in what order.")}
    {meta_panel("besci-eval", "Checks a skill's structure, triggering, and output quality.")}
    {meta_panel("besci-skill-creator", "Interviews an author and drafts the whole skill folder.")}
  </div>
</section>

<section class="section">
  <p class="eyebrow">Principles</p>
  <h2>From the memorandum of understanding</h2>
  <div class="two-col">
    <div class="panel"><h3>Contributors set their own terms</h3><p>You decide what goes in; you can revise or deprecate your own skill at any time.</p></div>
    <div class="panel"><h3>Use follows open science</h3><p>Skills are versioned so a project can cite exactly what it used, following Busara's SIFA framework. <a href="{GITHUB}/blob/main/docs/citing.md" rel="noopener">How to cite</a>.</p></div>
    <div class="panel"><h3>Skills do not replace experts</h3><p>Every skill names its escalation point. The navigator checks for it.</p></div>
    <div class="panel"><h3>Users are told what is shared</h3><p>Users and contributors are told what is shared with AI providers. <a href="{GITHUB}/blob/main/DISCLOSURE.md" rel="noopener">Disclosure</a>.</p></div>
    <div class="panel"><h3>Skills are Socratic</h3><p>They ask before they answer. "Before you start" is a required section.</p></div>
    <div class="panel"><h3>Evidence is honest</h3><p>Every skill states how far its evidence base has been tested outside WEIRD samples. No citation is ever invented.</p></div>
  </div>
</section>

<section class="section">
  <p class="eyebrow">Governance</p>
  <h2>Co-owned, openly licensed</h2>
  <p class="prose">Co-owned by The Agency Fund and Irrational Labs; see <a href="{GITHUB}/blob/main/GOVERNANCE.md" rel="noopener">GOVERNANCE.md</a> and <a href="{GITHUB}/blob/main/MAINTAINERS.md" rel="noopener">MAINTAINERS.md</a>. Code is MIT; skill content is CC BY 4.0. Phase 1 (October to November 2026) is TAF and IL staff contributing; Phase 2 invites expert organizations; Phase 3 opens to everyone. Decisions already made are recorded as <a href="{GITHUB}/tree/main/docs/adr" rel="noopener">architecture decision records</a>.</p>
  <p class="hero-actions"><a class="btn-secondary" href="{GITHUB}" rel="noopener">{ICONS['github']} Source on GitHub</a> <a class="btn-secondary" href="/contribute/">Contribute a skill</a></p>
</section>
"""
    page("/about/", "About", "Who makes the Behavioral Science Skills Library, what a skill is, and the principles behind it.", body)


def build_404() -> None:
    body = """
<div class="page-head">
  <p class="eyebrow">404</p>
  <h1>Page not found</h1>
  <p class="lede">That page does not exist. Try the <a href="/">catalog</a>.</p>
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

    lines = [
        f"# {SITE_NAME}",
        "",
        "An open library of atomic AI skills for behavioral science, by The Agency Fund and Irrational Labs.",
        f"Repository: {GITHUB}",
        f"Catalog JSON: {SITE_URL}/data/catalog.json",
        "",
        "## Skills",
        "",
    ]
    for s in skills:
        lines.append(f"- {s['name']} [{s['stage']}, {s['type']}, {s['status']}]: {s['what_it_does']} — {SITE_URL}{s['url']}")
    if workflows:
        lines += ["", "## Workflows", ""]
        for w in workflows:
            lines.append(f"- {w['name']}: {w['description']} — {SITE_URL}{w['url']}")
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

    urls = ["/", "/workflows/", "/install/", "/contribute/", "/propose/", "/upload/", "/whats-new/", "/about/"]
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

    build_index(skills, taxonomy)
    build_skill_pages(skills, taxonomy)
    build_workflows(workflows)
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
