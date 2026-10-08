# Instructions for AI agents working in this repository

This is the Behavioral Science Skills Library: a content repository of AI skills plus the tooling that validates, catalogs, packages, and publishes them. Read these before changing anything.

## Read first

- `CONTEXT.md`: the vocabulary. Use its terms (skill, atomic skill, meta-skill, workflow, trigger rule, escalation point, stage, evidence base, test case) and avoid the terms it lists under "Avoid".
- `docs/skill-spec.md`: the contract every skill meets. `scripts/besci_validate.py` enforces it.
- `docs/adr/`: decisions already made. Do not relitigate them in a change; open an ADR if one needs to change.

## Commands

```
uv sync                                  # once
uv run scripts/besci_validate.py         # every skill; or pass a skill folder
uv run scripts/check_sync.py [--fix]     # bundled copies match their sources
uv run scripts/snapshot_catalog.py       # regenerates the navigator's catalog
uv run scripts/build_site.py             # site/dist/ (gitignored)
uv run scripts/package_skills.py         # dist/*.skill (gitignored)
uv run python scripts/test_submit.py     # upload-endpoint tests, no network
```

CI runs the first five on every pull request. Run them before you finish.

## Rules

1. **One validator.** Change validation rules only in `scripts/besci_validate.py`, then update `docs/skill-spec.md` and `skills/besci-skill-creator/references/checklist.md` to match, then `uv run scripts/check_sync.py --fix`.
2. **Never hand-edit generated files**: `skills/besci-navigator/references/catalog.md`, anything under `site/dist/` or `dist/`, or the bundled copies listed in `scripts/check_sync.py`.
3. **Frontmatter is spec-compliant.** Only `name`, `description`, `license`, `compatibility`, `allowed-tools`, `metadata`. Everything under `metadata` is a plain string; lists are comma-separated. No nested objects.
4. **Skill names are verb-first kebab-case** from the verb list in `taxonomy.yaml`; meta-skills use the `besci-` prefix. American spelling everywhere.
5. **Eight sections, fixed order**, in every `SKILL.md`. "Before you start" and "When to bring in a specialist" may be "Not applicable: <real reason>". At least three evals. Changelog top entry matches `metadata.version`.
6. **Never invent a citation.** Mark anything unverified as "unverified, author to confirm".
7. **Skills do not get a README.** Instructions go in `SKILL.md` or `references/`.
8. **`skills/` holds skills only.** Workflows go in `workflows/<name>.md`.
9. **Evals cost money.** Do not run `skills/besci-eval/scripts/run_evals.py` without the user's go-ahead; use `--dry-run` to show the plan.
10. **Do not commit** `site/dist/`, `dist/`, `.venv/`, `__pycache__/`, or `*-workspace/`.
11. **Keep `SKILL.md` under 500 lines.** Move detail to `references/`.
12. **Taxonomy changes** go in the same pull request as the skill that needs them.

## Where things are

| Path | What |
|---|---|
| `skills/<name>/` | one skill: SKILL.md, evals/, CHANGELOG.md, optional references/ scripts/ assets/ |
| `skills/besci-*` | the three meta-skills; each bundles a copy of the validator or templates |
| `workflows/` | workflow files and template |
| `template/skill-template/` | the starting point for a new skill |
| `taxonomy.yaml` | stages, types, statuses, WEIRD statuses, verbs, io types, suggested tags |
| `scripts/` | validator, sync check, site builder, snapshot, packager, zip safety, inbox unpacker, submit tests |
| `site/src/` | site assets; the builder generates pages from skills |
| `api/submit.py` | the site's upload endpoint (Vercel Python function) |
| `.claude-plugin/` | marketplace and plugin manifests; one plugin, all skills |
| `.github/` | CI, inbox unpack, snapshot commit, release zips, PR and issue templates |
| `docs/` | spec, taxonomy, citing, deployment, ADRs, plan and session records |

## Adding a skill as an agent

Use `besci-skill-creator` if it is installed; otherwise copy `template/skill-template/`, follow the spec, run the validator, and run `scripts/snapshot_catalog.py` so the navigator knows about it. Set `status: draft`. Do not set `published` or `reviewed_by`; a human reviewer does that.
