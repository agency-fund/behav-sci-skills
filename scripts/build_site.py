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

MD = MarkdownIt("commonmark", {"html": True, "linkify": False}).enable(["table", "strikethrough"])

E = html.escape


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


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
        # Backticked paths into the skill's own files become links too.
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


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------

NAV = [
    ("Catalog", "/"),
    ("Workflows", "/workflows/"),
    ("Install", "/install/"),
    ("Contribute", "/contribute/"),
    ("What's new", "/whats-new/"),
    ("GitHub", GITHUB),
]


def layout(title: str, description: str, body: str, path: str, extra_head: str = "", page_class: str = "") -> str:
    nav = "".join(
        f'<a href="{E(href)}"{" aria-current=\"page\"" if href == path else ""}'
        f'{" rel=\"noopener\" target=\"_blank\"" if href.startswith("http") else ""}>{E(label)}</a>'
        for label, href in NAV
    )
    full_title = f"{title} · {SITE_NAME}" if title != SITE_NAME else SITE_NAME
    canonical = f"{SITE_URL}{path}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(full_title)}</title>
<meta name="description" content="{E(description)}">
<meta property="og:title" content="{E(full_title)}">
<meta property="og:description" content="{E(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{E(canonical)}">
<meta property="og:site_name" content="{E(SITE_NAME)}">
<meta name="twitter:card" content="summary">
<link rel="canonical" href="{E(canonical)}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="{E(SITE_NAME)} — what's new" href="/feed.xml">
<link rel="stylesheet" href="/styles.css">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
{extra_head}
</head>
<body class="{E(page_class)}">
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-row">
    <a class="brand" href="/">{E(SITE_NAME)}</a>
    <nav class="site-nav" aria-label="Main">{nav}</nav>
    <button class="theme-toggle" type="button" aria-label="Toggle dark mode" title="Toggle dark mode">◐</button>
  </div>
</header>
<main id="main" class="wrap">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <p class="footer-orgs">A project of
      <a href="https://agency.fund" rel="noopener"><img src="/assets/taf-logo.svg" alt="The Agency Fund" class="org-logo"></a>
      and
      <a href="https://irrationallabs.com" rel="noopener"><img src="/assets/il-logo.svg" alt="Irrational Labs" class="org-logo"></a>
    </p>
    <p class="footer-links">
      <a href="{GITHUB}" rel="noopener">GitHub</a> ·
      <a href="{GITHUB}/blob/main/DISCLOSURE.md" rel="noopener">Disclosure</a> ·
      <a href="{GITHUB}/blob/main/LICENSE" rel="noopener">License</a> ·
      <a href="/feed.xml">RSS</a> ·
      <a href="/llms.txt">llms.txt</a>
    </p>
    <p class="footer-license">Skill content CC BY 4.0, code MIT.</p>
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

def badge(text: str, kind: str = "") -> str:
    return f'<span class="badge badge-{E(kind or slugify(text))}">{E(text)}</span>'


def copy_block(cmd: str, label: str = "") -> str:
    lab = f'<span class="code-label">{E(label)}</span>' if label else ""
    return (
        f'<div class="code-row">{lab}<pre><code>{E(cmd)}</code></pre>'
        f'<button class="copy" type="button" data-copy="{E(cmd)}" aria-label="Copy command">Copy</button></div>'
    )


def plugin_install_block() -> str:
    return copy_block(f"/plugin marketplace add {REPO}\n/plugin install {PLUGIN}@{PLUGIN}", "Claude Code")


def npx_block(names: List[str]) -> str:
    flags = " ".join(f"--skill {n}" for n in names) if names else "--all"
    return copy_block(f"npx skills add {REPO} {flags}", "Any agent (Codex, Cursor, Copilot, Gemini CLI, ...)")


def card(s: dict, stage_labels: Dict[str, str]) -> str:
    status = s["status"] or "draft"
    search = " ".join([s["name"], s["title"], s["description"], s["what_it_does"], " ".join(s["tags"])]).lower()
    return f"""<article class="card status-{E(status)}" data-name="{E(s['name'])}" data-stage="{E(s['stage'])}" data-type="{E(s['type'])}" data-org="{E(s['org'])}" data-status="{E(status)}" data-tags="{E(' '.join(s['tags']))}" data-search="{E(search)}">
  {('<div class="draft-banner">Draft: not yet reviewed</div>' if status == 'draft' else '')}
  <h3><a href="{E(s['url'])}">{E(s['title'])}</a></h3>
  <p class="card-name"><code>{E(s['name'])}</code></p>
  <p class="card-badges">{badge(stage_labels.get(s['stage'], s['stage']) or 'stage?', 'stage-' + s['stage'])}{badge(s['type'] or 'atomic', 'type')}{badge(status, 'status-' + status)}</p>
  <p class="card-desc">{E(s['what_it_does'])}</p>
  <p class="card-meta">{E(s['org'])}{' · ' if s['org'] else ''}v{E(s['version'])}</p>
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

    return f"""<form class="filters" role="search" aria-label="Filter skills" onsubmit="return false;">
  <label class="filter-search"><span class="sr-only">Search skills</span>
    <input type="search" id="q" name="q" placeholder="Search skills (press / to focus)" autocomplete="off"></label>
  <label><span class="sr-only">Stage</span><select id="f-stage" name="stage">{opts(stages, 'All stages')}</select></label>
  <label><span class="sr-only">Type</span><select id="f-type" name="type">{opts(['atomic', 'meta'], 'Atomic and meta')}</select></label>
  <label><span class="sr-only">Organization</span><select id="f-org" name="org">{opts(orgs, 'All orgs')}</select></label>
  <label><span class="sr-only">Status</span><select id="f-status" name="status">{opts(['published', 'draft', 'deprecated'], 'All statuses')}</select></label>
  <label><span class="sr-only">Tag</span><select id="f-tag" name="tag">{opts(tags, 'All tags')}</select></label>
  <button type="button" id="f-clear" class="btn-secondary">Clear</button>
  <span class="filter-count" id="f-count" aria-live="polite"></span>
</form>"""


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def build_index(skills: List[dict], taxonomy: dict) -> None:
    stage_labels = label_map(taxonomy.get("stages"))
    by_name = {s["name"]: s for s in skills}
    start_rows = []
    for n in START_HERE:
        if n in by_name:
            s = by_name[n]
            start_rows.append(f'<li><a href="{E(s["url"])}"><strong>{E(s["title"])}</strong></a> <code>{E(n)}</code>: {E(s["what_it_does"])}</li>')
        else:
            start_rows.append(f'<li><code>{E(n)}</code>: coming soon.</li>')
    cards = "\n".join(card(s, stage_labels) for s in skills)
    body = f"""
<section class="hero">
  <h1>Behavioral science methods, one skill at a time</h1>
  <p class="lede">An open library of small, single-purpose AI skills that put behavioral-science methods into the daily work of social-sector teams: program designers, product managers, and M&amp;E leads who do not have a behavioral scientist in the room. Each skill does <em>one thing a behavioral scientist does</em>, narrow enough to say in a sentence without the word "and", cites the evidence it draws on, asks before it answers, and says when to bring in a specialist.</p>
  <p class="hero-links"><a class="btn" href="/install/">Install</a> <a class="btn-secondary" href="/contribute/">Contribute a skill</a> <a class="btn-secondary" href="{GITHUB}" rel="noopener">Source on GitHub</a></p>
</section>

<section class="start-here" aria-labelledby="start-here-h">
  <h2 id="start-here-h">Start here</h2>
  <p>Install these two first. The navigator tells you which skills to run and in what order; the evaluator checks whether a skill is doing its job on the model you use.</p>
  <ul class="start-list">{''.join(start_rows)}</ul>
  {plugin_install_block()}
  {npx_block(START_HERE)}
  <p class="muted">Using Claude Desktop or claude.ai? Download the <code>.skill</code> file from each skill's page and upload it under Settings → Capabilities → Skills. <a href="/install/">All install options</a>.</p>
</section>

<section class="catalog" aria-labelledby="catalog-h">
  <h2 id="catalog-h">Catalog <span class="muted">({len(skills)} skill{'s' if len(skills) != 1 else ''})</span></h2>
  {filters_html(skills, taxonomy)}
  <div class="grid" id="grid">
{cards}
  </div>
  <p id="no-results" class="muted" hidden>No skills match. <button type="button" class="link-btn" id="f-clear-2">Clear filters</button></p>
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
        year = (s["latest_date"] or s["first_date"] or str(dt.date.today()))[:4]
        authors = ", ".join(s["authors"]) or "Unknown author"
        cite = (f"{authors} ({year}). {s['title']} (version {s['version']}) [AI skill]. "
                f"Behavioral Science Skills Library, The Agency Fund and Irrational Labs. {SITE_URL}{s['url']}")

        def io_list(types: List[str], related: Dict[str, List[dict]], verb: str) -> str:
            if not types:
                return '<span class="muted">none declared</span>'
            parts = []
            for t in types:
                rel = [r for r in related.get(t, []) if r["name"] != name]
                links = ", ".join(f'<a href="{E(r["url"])}">{E(r["name"])}</a>' for r in rel)
                parts.append(f'<li><code>{E(t)}</code> <span class="muted">{E(io_labels.get(t, ""))}</span>'
                             + (f'<br><span class="muted">{verb}: {links}</span>' if links else "") + "</li>")
            return "<ul class='io-list'>" + "".join(parts) + "</ul>"

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

        body = f"""
<article class="skill-page">
<header class="skill-header">
  <p class="breadcrumb"><a href="/">Catalog</a> › <span>{E(name)}</span></p>
  {('<div class="draft-banner">Draft: this skill has not yet been reviewed by a maintainer. Use with care and send feedback.</div>' if status == 'draft' else '')}
  {('<div class="deprecated-banner">Deprecated: this skill is retired. See its version history for what replaced it.</div>' if status == 'deprecated' else '')}
  <h1>{E(s['title'])}</h1>
  <p class="skill-name"><code>{E(name)}</code> <span class="muted">v{E(s['version'])}</span></p>
  <p class="card-badges">{badge(stage_labels.get(s['stage'], s['stage']), 'stage-' + s['stage'])}{badge(s['type'], 'type')}{badge(status, 'status-' + status)}{badge(s['org'], 'org') if s['org'] else ''}</p>
  <p class="skill-what">{E(s['what_it_does'])}</p>
</header>

<div class="skill-layout">
<div class="skill-main">
  <aside class="callout" aria-labelledby="fires-h">
    <h2 id="fires-h" class="callout-title">When this skill fires</h2>
    <p>{E(s['description'])}</p>
  </aside>

  <section class="install-box" aria-labelledby="install-h">
    <h2 id="install-h">Install</h2>
    <div class="install-option">
      <h3>Claude Code</h3>
      <p class="muted">Installs the whole library as one plugin. Keeps itself current when auto-update is on.</p>
      {copy_block(f"/plugin marketplace add {REPO}")}
      {copy_block(f"/plugin install {PLUGIN}@{PLUGIN}")}
    </div>
    <div class="install-option">
      <h3>Any agent (Codex, Cursor, Copilot, Gemini CLI, ...)</h3>
      {copy_block(f"npx skills add {REPO} --skill {name}")}
    </div>
    <div class="install-option">
      <h3>Claude Desktop and claude.ai</h3>
      <p><a class="btn" href="{E(s['download_url'])}" rel="noopener">Download {E(name)}.skill</a></p>
      <p class="muted">Then open Settings → Capabilities → Skills → Upload skill, choose the file, and enable it. Zip installs do not update themselves: check the version here before relying on an old copy.</p>
    </div>
  </section>

  <nav class="toc" aria-label="On this page"><h2>Contents</h2><ol>{toc}<li><a href="#version-history">Version history</a></li><li><a href="#cite">Cite this skill</a></li></ol></nav>

  {''.join(sections_html)}

  <section class="skill-section" id="version-history"><h2>Version history</h2>{changelog_html}</section>

  <section class="skill-section cite" id="cite"><h2>Cite this skill</h2>
    {copy_block(cite)}
    <p class="muted">Skills are fixed, versioned artifacts. Record the skill name and version in your project documentation the way you would register analysis code. See <a href="{GITHUB}/blob/main/docs/citing.md" rel="noopener">how to cite skills and workflows</a>, which follows Busara's <a href="https://busara.global/our-works/the-sifa-tool-for-a-statement-of-intellectual-fellowship-and-accountability/" rel="noopener">SIFA framework</a> for stating how humans and AI contributed.</p>
  </section>

  <p class="disclosure-line muted">Using this skill inside a commercial AI product sends what you type to that product's provider. Do not paste sensitive personal or proprietary data without understanding the product's terms. <a href="{GITHUB}/blob/main/DISCLOSURE.md" rel="noopener">Read the disclosure</a>.</p>
</div>

<aside class="skill-meta" aria-label="Skill details">
  <dl>
    <dt>Authors</dt><dd>{E(authors)}</dd>
    <dt>Organization</dt><dd>{E(s['org']) or '<span class="muted">—</span>'}</dd>
    <dt>Version</dt><dd>{E(s['version'])}</dd>
    <dt>Status</dt><dd>{E(status)}</dd>
    <dt>Stage</dt><dd><a href="/?stage={E(s['stage'])}">{E(stage_labels.get(s['stage'], s['stage']))}</a></dd>
    <dt>WEIRD evidence</dt><dd>{E(weird_labels.get(s['weird'], s['weird'])) or '<span class="muted">not stated</span>'}</dd>
    <dt>Tags</dt><dd>{tags}</dd>
    <dt>Consumes</dt><dd>{io_list(s['consumes'], producers, 'produced by')}</dd>
    <dt>Produces</dt><dd>{io_list(s['produces'], consumers, 'consumed by')}</dd>
    <dt>Test cases</dt><dd>{s['eval_count']} in <a href="{GITHUB}/blob/main/skills/{E(name)}/evals/evals.json" rel="noopener">evals.json</a></dd>
    <dt>License</dt><dd>{E(s['license'])}</dd>
    <dt>Source</dt><dd><a href="{E(s['source_url'])}" rel="noopener">skills/{E(name)}</a></dd>
    <dt>Last changed</dt><dd>{E(s['latest_date']) or '<span class="muted">—</span>'}</dd>
  </dl>
  {warnings_html}
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
  <p>No workflows yet. The first ones will come from <code>besci-navigator</code> in guide mode and from contributors in Phase 2.</p>
  <p>Want to write one? Copy <a href="{GITHUB}/blob/main/workflows/WORKFLOW-TEMPLATE.md" rel="noopener">the workflow template</a> and open a pull request.</p>
</div>"""
    body = f"""
<h1>Workflows</h1>
<p class="lede">A workflow is a recommended set of skills for a larger task, with the relationships between them stated: which runs first, which can run in parallel, which are independent, and where a human decides. A workflow can be as light as "use these three, in any order, but A before B". Workflows live in <a href="{GITHUB}/tree/main/workflows" rel="noopener"><code>workflows/</code></a>, never in <code>skills/</code>, because everything in <code>skills/</code> is atomic.</p>
{listing}
"""
    page("/workflows/", "Workflows", "Recommended sets of behavioral-science skills with their relationships stated.", body)
    for w in workflows:
        wbody = f"""
<article class="skill-page">
<p class="breadcrumb"><a href="/workflows/">Workflows</a> › <span>{E(w['name'])}</span></p>
<h1>{E(w['title'])}</h1>
<p class="skill-name"><code>{E(w['name'])}</code>{' <span class="muted">v' + E(w['version']) + '</span>' if w['version'] else ''}</p>
<p class="skill-what">{E(w['description'])}</p>
<p class="muted">{E(', '.join(w['authors']))}{' · ' if w['authors'] else ''}{E(w['org'])} · <a href="{E(w['source_url'])}" rel="noopener">source</a></p>
<div class="skill-section">{md_to_html(w['body'])}</div>
</article>
"""
        page(w["url"], w["title"], w["description"] or w["title"], wbody)


def build_install() -> None:
    body = f"""
<h1>Install</h1>
<p class="lede">Pick the path that matches the tool you use. Every path installs the same skills.</p>

<section class="install-option">
  <h2>1. Claude Code (recommended if you can)</h2>
  <p>Installs the whole library as one plugin. Turn on auto-update for the marketplace and it stays current; otherwise run <code>/plugin update</code> now and then.</p>
  {copy_block(f"/plugin marketplace add {REPO}")}
  {copy_block(f"/plugin install {PLUGIN}@{PLUGIN}")}
  <p class="muted">Then just describe what you are trying to do. The navigator fires on behavioral-science questions; individual skills fire when you name their method. Type <code>/besci-navigator</code> to call it directly.</p>
</section>

<section class="install-option">
  <h2>2. Other coding agents: Codex, Cursor, Copilot, Gemini CLI, OpenCode, and more</h2>
  <p>The <code>skills</code> CLI reads this repository's plugin manifest and installs into whichever agents it finds.</p>
  {copy_block(f"npx skills add {REPO} --all")}
  {copy_block(f"npx skills add {REPO} --skill besci-navigator --skill besci-eval")}
  <p class="muted">Update with <code>npx skills update</code>. For agents with their own plugin marketplaces, re-run the install command to update until we have verified each one's update path.</p>
</section>

<section class="install-option">
  <h2>3. Claude Desktop and claude.ai (no terminal)</h2>
  <ol>
    <li>Open the skill's page in the catalog and click <strong>Download &lt;name&gt;.skill</strong>. Start with <a href="/skills/besci-navigator/">besci-navigator</a> and <a href="/skills/besci-eval/">besci-eval</a>.</li>
    <li>In Claude, open <strong>Settings → Capabilities → Skills → Upload skill</strong> and choose the file.</li>
    <li>Enable it, then ask Claude to do the thing the skill does.</li>
  </ol>
  <p class="muted"><strong>Zip installs do not update themselves.</strong> Each skill carries its version number; compare it with the catalog page before relying on an old copy, and watch <a href="/whats-new/">What's new</a> or the <a href="/feed.xml">RSS feed</a> for releases. Re-upload to update; Claude replaces the old copy.</p>
  <p class="muted"><strong>Org admins on Claude for Work:</strong> an admin can upload skills once for the whole organization and re-upload on release, which is as close to auto-update as Desktop gets.</p>
</section>

<section class="install-option">
  <h2>Before you use any skill</h2>
  <p>Using a skill inside a commercial AI product sends what you type to that product's provider. Do not paste sensitive personal or proprietary data without understanding the product's terms. Skills can also be used as an educational resource: read one, learn the method, and apply it in your own non-AI workflow. <a href="{GITHUB}/blob/main/DISCLOSURE.md" rel="noopener">Read the full disclosure</a>.</p>
</section>
"""
    page("/install/", "Install", "How to install behavioral-science skills in Claude Code, other coding agents, Claude Desktop, and claude.ai.", body)


def build_contribute() -> None:
    body = f"""
<h1>Contribute a skill</h1>
<p class="lede">A skill is one thing a behavioral scientist does, narrow enough to describe in a sentence without the word "and". It cites its evidence, asks before it answers, shows its output shape, names its failure modes, and says when to bring in a specialist. <a href="{GITHUB}/blob/main/docs/skill-spec.md" rel="noopener">Read the full spec</a>.</p>

<section>
  <h2>1. Claim or propose</h2>
  <p>Check the <a href="/">catalog</a> for something that already covers it. Then <a href="/propose/">propose the skill</a>, which opens a pre-filled GitHub issue so a maintainer can confirm it is atomic before you write it.</p>
</section>

<section>
  <h2>2. Draft it with besci-skill-creator</h2>
  <p>Install <a href="/skills/besci-skill-creator/"><code>besci-skill-creator</code></a> and say "I want to create a skill for ...". It interviews you against the spec, starting with the atomicity test and the trigger rule, drafts the whole folder (<code>SKILL.md</code>, three test cases, a changelog), runs the validator, does one self-test pass, and packages a <code>.skill</code> file where the environment allows. You can also copy <a href="{GITHUB}/tree/main/template/skill-template" rel="noopener">the template</a> and write by hand.</p>
</section>

<section>
  <h2>3. Validate</h2>
  <p>The same validator runs in the creator skill, in CI, and on upload, so what passes locally passes everywhere:</p>
  {copy_block("uv run scripts/besci_validate.py skills/<your-skill-name>")}
  <p class="muted">Exit 0 means the structure is right. A maintainer still reviews the content.</p>
</section>

<section>
  <h2>4. Submit, three ways</h2>
  <ol class="paths">
    <li><strong>Hand it to a maintainer.</strong> Share the <code>.skill</code> file on Slack or Drive. The maintainer submits it on your behalf; you stay credited in the <code>authors</code> field and on the commit.</li>
    <li><strong>Upload it, no git.</strong> Use the <a href="/upload/">upload form</a> (TAF and IL staff have a contributor key), or open <a href="{GITHUB}/tree/main/inbox" rel="noopener"><code>inbox/</code></a> on GitHub, choose <em>Add file → Upload files</em>, drop the <code>.skill</code> file, and pick <em>Create a new branch and start a pull request</em>. An action unpacks it into <code>skills/</code>, runs the validator, and posts a plain-language checklist on the pull request.</li>
    <li><strong>Clone and open a pull request.</strong> Put the folder under <code>skills/</code>, run the validator, push a branch, open a PR.</li>
  </ol>
</section>

<section>
  <h2>5. Review</h2>
  <p>Every pull request needs green CI and one approving review from a maintainer, who checks the content against the spec: is it atomic, does the trigger rule name what it should not handle, is the evidence real and the WEIRD note honest, does the output template match what the skill promises, are the failure modes and the escalation point concrete, do the test cases read like real requests. On merge the skill is marked <code>published</code> and appears here. See <a href="{GITHUB}/blob/main/CONTRIBUTING.md" rel="noopener">CONTRIBUTING.md</a> for the reviewer checklist.</p>
</section>

<section>
  <h2>Before you contribute</h2>
  <p>Your published skill content will be processed by third-party AI systems when others use it. You set your own terms for what goes in; you can revise or deprecate your skill at any time through version control. Skill content is licensed CC BY 4.0, code MIT. <a href="{GITHUB}/blob/main/DISCLOSURE.md" rel="noopener">Read the disclosure</a>.</p>
</section>
"""
    page("/contribute/", "Contribute", "How to propose, draft, validate, and submit a behavioral-science skill.", body)


def build_propose(taxonomy: dict) -> None:
    stage_opts = "".join(
        f'<option value="{E(str(x.get("id")))}">{E(str(x.get("label")))}: {E(str(x.get("description", "")))}</option>'
        for x in taxonomy.get("stages", []) if isinstance(x, dict)
    )
    body = f"""
<h1>Propose a skill</h1>
<p class="lede">Fill this in and it opens a pre-filled GitHub issue (you need a GitHub account to submit it). A maintainer confirms the idea is atomic before you write the skill, so nobody drafts something that would be sent back.</p>
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
  <p><button class="btn" type="submit">Open the pre-filled GitHub issue</button></p>
  <p class="muted">Opens in a new tab. If GitHub drops some fields, paste them into the issue by hand.</p>
</form>
"""
    page("/propose/", "Propose a skill", "Propose an atomic behavioral-science skill via a pre-filled GitHub issue.", body)


def build_upload() -> None:
    body = f"""
<h1>Upload a skill</h1>
<p class="lede">Upload the <code>.skill</code> file that <code>besci-skill-creator</code> gave you. We validate it, unpack it into <code>skills/</code>, and open a pull request for a maintainer to review. You will get a link to the pull request and the validator's report.</p>
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
    I have read the <a href="{GITHUB}/blob/main/DISCLOSURE.md" rel="noopener" target="_blank">disclosure</a> and understand my skill content will be processed by third-party AI systems when others use it.</label>
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
        latest = md_to_html(s["latest_change"]) if s["latest_change"] else "<p class='muted'>No changelog entry.</p>"
        items.append(f'<li class="news-item"><h3><a href="{E(s["url"])}">{E(s["title"])}</a> <code>{E(s["name"])}</code> <span class="muted">v{E(s["version"])}{" · " + E(s["latest_date"]) if s["latest_date"] else ""}</span></h3>{latest}</li>')
    body = f"""
<h1>What's new</h1>
<p class="lede">Every change to a skill is a version bump with a changelog entry. Newest first. Subscribe to the <a href="/feed.xml">RSS feed</a> to hear about releases.</p>
<ul class="news">{''.join(items) or '<li class="muted">Nothing yet.</li>'}</ul>
"""
    page("/whats-new/", "What's new", "Latest changes to skills in the Behavioral Science Skills Library.", body)


def build_404() -> None:
    body = """
<h1>Page not found</h1>
<p>That page does not exist. Try the <a href="/">catalog</a>.</p>
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

    urls = ["/", "/workflows/", "/install/", "/contribute/", "/propose/", "/upload/", "/whats-new/"]
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
    build_404()
    build_data(skills, workflows, taxonomy)

    n_err = sum(len(s["errors"]) for s in skills)
    print(f"Built {len(skills)} skill page(s) and {len(workflows)} workflow page(s) into {os.path.relpath(DIST, ROOT)}/")
    if n_err:
        print(f"note: {n_err} validator error(s) across skills; pages were still built. Run besci_validate.py for details.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
