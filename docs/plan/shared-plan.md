# Shared plan: v0.1 of the Behavioral Science Skills Library

Agreed on 2026-10-08 between Zezhen (Michael) Wu (TAF) and Claude after the design session recorded in `2026-10-08-grill-session.md`. This is the plan that the initial commit implements. The MOU is the source of the goals; this document is the source of the shape.

## Goal of this stage

MOU Phase 0: the repository exists under TAF's GitHub organization, the skill template and `besci-skill-creator` are created and tested, and the meta-skills `besci-navigator` and `besci-eval` are created and tested. Plus, pulled forward from Phase 1 because it proves the pipeline: a working catalog site, the plugin, the `.skill` zips, and the three contribution paths.

## What a skill is

A folder `skills/<verb-first-name>/` with:

- `SKILL.md`: spec-compliant frontmatter (`name`, `description` as the compressed trigger rule with "use when" and "do not use when", `license`, flat string `metadata`: type, stage, version, status, authors, org, weird, optional tags, consumes, produces) and eight sections in fixed order: What it does; When to use it; Before you start; What it draws on; How to do it; Output template; Where it goes wrong; When to bring in a specialist. The third and eighth accept a justified "Not applicable".
- `evals/evals.json`: at least three realistic test prompts with expected output shape, Anthropic's schema.
- `CHANGELOG.md`: newest first, top entry matches the version.
- Optional `references/`, `scripts/`, `assets/`.

`docs/skill-spec.md` is the prose contract; `scripts/besci_validate.py` enforces it.

## What was built

| Area | Files | State |
|---|---|---|
| Spec and taxonomy | `docs/skill-spec.md`, `taxonomy.yaml`, `docs/taxonomy.md`, `template/skill-template/` | done |
| Validator and tooling | `scripts/besci_validate.py`, `check_sync.py`, `build_site.py`, `snapshot_catalog.py`, `package_skills.py`, `skillzip.py`, `unpack_inbox.py`, `test_submit.py` | done, tested locally |
| Meta-skills | `skills/besci-skill-creator`, `skills/besci-navigator`, `skills/besci-eval` | v0.1.0 drafts, validate clean, not yet reviewed or run against real authors |
| Seed skill | `skills/draft-cognitive-interview-script` | v0.1.0 draft for the author to revise |
| Site | `site/src/`, generated `site/dist/` | builds; pages for catalog, skill, workflows, install, contribute, propose, upload, what's new |
| Submission | `api/submit.py`, `vercel.json`, `inbox/`, `.github/workflows/inbox.yml` | tested without network; needs Vercel and a token |
| CI and release | `.github/workflows/ci.yml`, `snapshot.yml`, `release.yml`, PR and issue templates, CODEOWNERS | written, not yet run on GitHub |
| Plugin | `.claude-plugin/marketplace.json`, `plugin.json` | passes `claude plugin validate` |
| Governance and docs | README, CONTRIBUTING, GOVERNANCE, MAINTAINERS, DISCLOSURE, CODE_OF_CONDUCT, CITATION.cff, LICENSE, LICENSE-CONTENT, `docs/citing.md`, `docs/deployment.md`, `CONTEXT.md`, `AGENTS.md`, `CLAUDE.md`, `docs/adr/` | done |

## How the pieces connect

```
author ──besci-skill-creator──> skills/<name>/ ──validator──> pull request ──review──> main
                                                                    │
     main ──CI──> validate · sync check · build site · package      │
     main ──snapshot.yml──> skills/besci-navigator/references/catalog.md (bot commit)
     main ──Vercel──> site (catalog.json, pages) + /api/submit
     tag  ──release.yml──> GitHub Release with <name>.skill zips
     user ──besci-navigator──> which skill, in what order ──> runs the skill
     author/maintainer ──besci-eval──> structure · triggering · output quality · model comparison
```

## Decisions that constrain future work

See `docs/adr/`: build fresh (0001); flat spec-compliant metadata (0002); one Python validator everywhere (0003); Vercel for site and endpoint (0004); flat `skills/` with taxonomy in metadata (0005).

## What is deliberately not in v0.1

Workflow files (template only); expert ratings; a Workflow Builder page; branding; a custom domain; GitHub login on the upload form (contributor key instead); non-Claude providers in the eval script; automated cross-org review; Joe Speed's sixteen skills (to be ported one at a time).
