# Behavioral Science Skills Library

Small, single-purpose AI skills that put behavioral-science methods into the daily work of social-sector teams. A joint project of [The Agency Fund](https://agency.fund) and [Irrational Labs](https://irrationallabs.com).

**Catalog and install guide:** https://behav-sci-skills.vercel.app

## Who this is for

A program designer, product manager, or M&E lead at an NGO who does not have a behavioral scientist in the room. Each skill is one thing a behavioral scientist does: decompose a defined behavior into COM-B barriers, draft a cognitive interview script, design a measure of agency. It cites the evidence it draws on, asks before it answers, produces a predictable output, records where it goes wrong, and says when to bring in a specialist.

Skills amplify practitioners; they do not replace experts. Read `DISCLOSURE.md` before pasting sensitive data into any AI product.

## Start here

Install the two meta-skills first. The **navigator** tells you which skill to use for your problem. The **evaluator** tells you how good a skill is.

**Claude Code** (keeps itself updated):

```
/plugin marketplace add agency-fund/behav-sci-skills
/plugin install behav-sci-skills@behav-sci-skills
```

**Codex, Cursor, Copilot, and other agents:**

```
npx skills add agency-fund/behav-sci-skills --skill besci-navigator --skill besci-eval
```

**Claude Desktop / claude.ai:** download `besci-navigator.skill` and `besci-eval.skill` from the [latest release](https://github.com/agency-fund/behav-sci-skills/releases/latest), then Settings → Capabilities → Skills → Upload skill. Zips do not update themselves; the [What's new](https://behav-sci-skills.vercel.app/whats-new/) page and its RSS feed announce new versions.

Then ask: *"Where do I start? Mothers stop coming to our nutrition sessions after the third visit."*

## What a skill is

A folder with a `SKILL.md`, at least three test cases, and a changelog:

```
skills/decompose-comb-barriers/
├── SKILL.md            frontmatter (trigger rule, stage, version, authors, WEIRD status)
│                       + eight sections: What it does · When to use it · Before you start
│                       · What it draws on · How to do it · Output template
│                       · Where it goes wrong · When to bring in a specialist
├── evals/evals.json    realistic prompts with the expected shape of output
├── CHANGELOG.md        one entry per version
└── references/         optional detail loaded on demand
```

The rule for scope: **one thing a behavioral scientist does, narrow enough to say in one sentence without "and".**

| Atomic | Too broad |
|---|---|
| Decompose a defined behavior into COM-B barrier hypotheses | Design a behavior change program |
| Draft a saying-is-believing exercise for a target population | Apply behavioral science to a chatbot |
| Design a measure of user agency using Social Cognitive Theory | Analyze this program and tell me what's wrong |

The full specification is in `docs/skill-spec.md`. Larger tasks are **workflows**: ordered sets of skills with the relationships between them stated, in `workflows/`.

## The three meta-skills

| Skill | What it does |
|---|---|
| `besci-navigator` | Recommends which skills to run, in what order. Route mode answers a concrete task in one turn; guide mode interviews you and drafts a workflow. |
| `besci-eval` | Checks a skill's structure, whether it fires on the right requests, and whether its outputs match its own template. Re-runs across models when a new one ships. |
| `besci-skill-creator` | Interviews an author about one method, one question at a time, and drafts the whole skill folder, validated and self-tested. |

## Contribute

Phase 1 (Oct–Nov 2026) is TAF and IL staff. Three paths, all ending in a pull request a maintainer reviews:

1. Hand your `.skill` file to a maintainer.
2. Upload it on GitHub's website into `inbox/` with "Create a new branch and start a pull request"; a bot unpacks and checks it.
3. Clone, run the validator, open a pull request.

See `CONTRIBUTING.md`. Propose a skill before writing it at https://behav-sci-skills.vercel.app/propose/.

## Repository map

```
skills/            one folder per skill (atomic and meta)
workflows/         workflow files and the template
template/          copy to start a new skill by hand
taxonomy.yaml      stages, verbs, input/output types, tags
docs/              skill-spec, taxonomy, citing, deployment, adr/, plan/
scripts/           validator, site builder, catalog snapshot, packager (Python)
site/src/          static site assets; built to site/dist/ by scripts/build_site.py
api/               the upload endpoint (Vercel function)
inbox/             drop zone for .skill uploads via the GitHub web UI
.claude-plugin/    Claude Code marketplace and plugin manifests
.github/           CI, inbox unpacker, catalog snapshot, releases, templates
```

Common commands (after `uv sync`):

```
uv run scripts/besci_validate.py            # check every skill
uv run scripts/build_site.py                 # build the site into site/dist/
uv run scripts/snapshot_catalog.py           # refresh the navigator's catalog
uv run scripts/package_skills.py             # build .skill zips into dist/
```

## Principles

From the Memorandum of Understanding between TAF and IL:

- **Contributors set their own terms.** You decide what goes in; you can revise or deprecate your own skill.
- **Use follows open science.** Skills are versioned so a project can cite exactly what it used. See `docs/citing.md` and Busara's SIFA framework.
- **Skills do not replace experts.** Every skill names its escalation point. The navigator checks for it.
- **Users and contributors are told what is shared with AI providers.** See `DISCLOSURE.md`.
- **Skills are Socratic.** They ask before they answer.

## Governance and license

Co-owned by The Agency Fund and Irrational Labs; see `GOVERNANCE.md` and `MAINTAINERS.md`. Code is MIT (`LICENSE`); skill content is CC BY 4.0 (`LICENSE-CONTENT.md`). Vocabulary in `CONTEXT.md`; decisions in `docs/adr/`; roadmap in `docs/plan/next-steps.md`.

Status: v0.1.0, Phase 0 complete, internal build and dogfooding underway.
