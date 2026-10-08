# Manual validation checklist

Use when the validator script cannot run. Each line mirrors a rule in `scripts/besci_validate.py`; the code in brackets is what the script would report.

## Folder and files
- [ ] Folder name is kebab-case, 1 to 64 characters, no leading, trailing, or double hyphens, and equals `name` in the frontmatter. [E003, E004]
- [ ] For atomic skills, the name starts with a verb from the taxonomy's list (define, decompose, draft, design, measure, map, score, select, adjust, analyze, assess, audit, build, choose, cluster, compare, diagnose, estimate, evaluate, find, generate, identify, plan, prioritize, propose, review, simulate, specify, summarize, synthesize, test, translate, validate, write). [E005]
- [ ] `SKILL.md`, `evals/evals.json`, and `CHANGELOG.md` exist. No `README.md` in the folder. [E001, E029, E030, W033]
- [ ] Only allowed file types; nothing over 2 MB; folder under 10 MB. [E034]
- [ ] Every `references/`, `scripts/`, or `assets/` path mentioned in SKILL.md exists. [E032]
- [ ] SKILL.md is under 500 lines. [W031]

## Frontmatter
- [ ] Only these top-level keys: name, description, license, compatibility, allowed-tools, metadata. [E035]
- [ ] `description` is 1 to 1024 characters, has no `<` or `>`, contains a "use when" clause and a "do not use when" clause. [E006, E007, E008]
- [ ] `license` is CC-BY-4.0 (or MIT for code-only skills). [E009]
- [ ] `metadata` has type, stage, version, status, authors, org, all as plain strings. [E010]
- [ ] type is atomic or meta; stage is one of the seven or other; version is quoted semver; status is draft, published, or deprecated. [E011, E012, E014, E015]
- [ ] Atomic skills have `weird` set to one of: weird-only, mixed-evidence, likely-generalizes, untested-outside-weird, not-applicable. [E018]
- [ ] `consumes` and `produces`, if present, use ids from the taxonomy's io types. [W019]

## Body
- [ ] Exactly these level-2 headings, in this order: What it does; When to use it; Before you start; What it draws on; How to do it; Output template; Where it goes wrong; When to bring in a specialist. [E020, E021]
- [ ] No section is empty. [E022]
- [ ] Only "Before you start" and "When to bring in a specialist" may read "Not applicable: <reason>", and the reason is a real sentence. [E023]
- [ ] First sentence of "What it does" has no "and". [W024]
- [ ] "When to use it" has `### Use it when` with at least three bullets and `### Do not use it when` with at least two. [E025, E026]
- [ ] "What it draws on" has at least one real citation (year, DOI, or URL) plus WEIRD skew and replication status lines. [W027]
- [ ] "Output template" contains a fenced code block. [W028]

## Evals and changelog
- [ ] `evals.json` has `skill_name` equal to the name and at least three cases, each with id, prompt, expected_output. [E029]
- [ ] `CHANGELOG.md` top entry is `## <version> - <date>` matching `metadata.version`. [E030]
