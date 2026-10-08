# Skill specification

This is the authoring guideline for every skill in the Behavioral Science Skills Library. The validator in `scripts/besci_validate.py` enforces everything marked **required**. `besci-skill-creator` interviews you against this spec; you can also write a skill by hand with `template/skill-template/`.

A skill is a folder:

```
skills/<name>/
├── SKILL.md            required: frontmatter + eight sections
├── evals/evals.json    required: at least three test cases
├── CHANGELOG.md        required: one entry per version
├── references/         optional: material loaded on demand
├── scripts/            optional: code the AI can run
└── assets/             optional: templates used in output
```

No `README.md` inside a skill folder. Keep `SKILL.md` under 500 lines and move detail into `references/`.

## 1. The name

**Required.** Kebab-case, 1 to 64 characters, matches the folder name, and starts with a verb from the `verbs` list in `taxonomy.yaml`. Meta-skills (`besci-*`) are exempt from the verb rule.

The verb-first name is the atomicity rule applied to the folder: if you cannot start the name with one verb, you have more than one skill.

| Good | Not this |
|---|---|
| `decompose-comb-barriers` | `comb-barrier-decomposer` |
| `define-key-behavior` | `behavior-definition` |
| `draft-cognitive-interview-script` | `cognitive-interviews` |

American spelling throughout: behavior, analyze, program.

## 2. Frontmatter

Only the keys allowed by the [Agent Skills spec](https://agentskills.io/specification) may appear at the top level. Everything the catalog needs goes under `metadata` as plain strings. Lists are comma-separated strings, because the spec allows string values only.

```yaml
---
name: decompose-comb-barriers
description: >-
  Use when one behavior is already defined (who does what, when) and you
  need to know why it is not happening. Lists competing capability,
  opportunity, and motivation barriers with a diagnostic question for each.
  Do not use when the goal is still vague ("improve maternal health"); run
  define-key-behavior first. Not for choosing interventions; that comes after.
license: CC-BY-4.0
metadata:
  title: COM-B barrier decomposer
  type: atomic
  stage: diagnose
  version: "0.1.0"
  status: draft
  authors: "Nikhil Ravichandar"
  org: IL
  weird: mixed-evidence
  tags: "com-b, behavior-change-wheel"
  consumes: "target-behavior-brief"
  produces: "comb-barrier-hypotheses"
---
```

| Field | Required | Rule |
|---|---|---|
| `name` | yes | See section 1. |
| `description` | yes | The compressed trigger rule, max 1024 characters, no `<` or `>`. Must contain a "Use when ..." clause and a "Do not use when ..." clause naming the nearest adjacent intent. This is the only text the AI reads before deciding to load the skill, so write it as the user's intents and phrasings, and make it a little pushy: skills under-trigger more often than they over-trigger. |
| `license` | yes | `CC-BY-4.0` for skill content. `MIT` only for a skill that is code with no method content. |
| `metadata.title` | no | Human-readable name for the catalog. Defaults to the name. |
| `metadata.type` | yes | `atomic` or `meta`. |
| `metadata.stage` | yes | One of `define`, `diagnose`, `design`, `measure`, `test`, `analyze`, `implement`, or `other`. The seven are strong recommendations; `other` is accepted with a warning. See the crosswalk in `docs/taxonomy.md`. |
| `metadata.version` | yes | Semver, quoted: `"0.1.0"`. Bump in the same change as the CHANGELOG entry. |
| `metadata.status` | yes | `draft`, `published`, or `deprecated`. Submit as `draft`; a maintainer sets `published` on merge. |
| `metadata.authors` | yes | Names or GitHub handles, comma-separated. |
| `metadata.org` | yes | `TAF`, `IL`, or `community`. |
| `metadata.weird` | atomic only | `weird-only`, `mixed-evidence`, `likely-generalizes`, `untested-outside-weird`, or `not-applicable`. |
| `metadata.tags` | no | Free-form, comma-separated. See `suggested_tags` in `taxonomy.yaml` for consistent spelling. |
| `metadata.consumes` | no | What the skill needs, as ids from `io_types` in `taxonomy.yaml`. Lets the navigator and the site chain skills. Unknown ids are a warning. |
| `metadata.produces` | no | What the skill outputs, as `io_types` ids. |
| `metadata.reviewed_by` | no | Set by the reviewer at merge. |

## 3. The eight sections

**Required**, in this order, each as a level-2 heading with exactly this text. The validator fails on a missing, empty, or reordered section.

### `## What it does`

One sentence, no "and". Then at most a short paragraph. The validator warns if the first sentence contains "and"; the reviewer decides whether the skill needs splitting.

### `## When to use it`

The full trigger rule. The `description` is the compressed version that fires the skill; this section is the complete list, read by humans on the site and by `besci-eval`, which turns every bullet into a trigger test. Two level-3 subheadings, exactly:

```markdown
### Use it when
- (at least three) user intents or phrasings that should invoke this skill
### Do not use it when
- (at least two) adjacent intents that should not, each naming where to go instead
```

### `## Before you start`

The questions the skill asks the user before it produces anything. This is where the Socratic habit lives: a skill should not produce output on a guess it could have checked with one question. List the questions, say which are required, and say what the skill assumes if an answer is missing.

**May be "Not applicable: <reason>"** when the skill genuinely does not need to ask, for instance because it transforms an input the upstream skill already gathered. The reason must be a real sentence. `besci-skill-creator` will push back on it before accepting.

### `## What it draws on`

The evidence base: the framework, paper, or practice this skill operationalizes, with citations (authors, year, title, venue, link). Then two short labelled notes:

- **WEIRD skew:** which populations the evidence comes from and what a user elsewhere should check locally.
- **Replication status:** replicated, mixed, contested, or single-study, in a sentence.

"Common sense" or "general best practice" is not an evidence base. If the skill encodes a practitioner's method rather than a published one, say so and name the practitioner.

### `## How to do it`

The procedure, step by step, in the imperative. Explain why a step matters where it isn't obvious; a model follows a reasoned instruction better than a bare command. Point to `references/` files for detail, one level deep.

### `## Output template`

The exact shape of the response, in a fenced `markdown` block, with placeholders in angle brackets. A user and a reviewer should be able to tell from this block alone whether a run of the skill did its job.

### `## Where it goes wrong`

Known failure modes and out-of-scope cases. What the model tends to do wrong with this method, what inputs break it, what it must refuse to do.

### `## When to bring in a specialist`

The escalation point: the conditions under which the skill tells the user the question has outgrown the tool. Be concrete ("if the behavior involves clinical risk", "if the sample is below 200 and the effect size is unknown"). Say what kind of specialist and what to bring to them.

**May be "Not applicable: <reason>"** for a narrow technical skill with no judgement call the user could get wrong. Same rule: a real reason.

## 4. Test cases: `evals/evals.json`

**Required**, at least three. The format is the one Anthropic's skill-creator uses, so its tooling runs these unchanged.

```json
{
  "skill_name": "decompose-comb-barriers",
  "evals": [
    {
      "id": 1,
      "prompt": "A realistic request a user would actually type, with the context they'd actually give.",
      "expected_output": "The shape of a good answer: which sections appear, what must be present, what must not.",
      "files": [],
      "assertions": []
    }
  ]
}
```

Write prompts the way your users talk, not the way the skill talks. Include one case that should trigger the "Before you start" questions because context is missing, and one that approaches the escalation point.

Trigger tests are not written here. `besci-eval` derives them from `## When to use it`.

## 5. Version history: `CHANGELOG.md`

**Required.** Newest first. The top entry must contain the current `metadata.version`.

```markdown
# Changelog

## 0.1.0 - 2026-10-08
First draft. Interviewed with besci-skill-creator; three evals; not yet reviewed.
```

Patch for wording, minor for new behavior, major when the output template changes shape. Name the reviewer in the entry that marks a skill `published`.

## 6. Files

Allowed types: markdown, text, JSON, YAML, CSV, Python, R, shell, HTML, CSS, JavaScript, PNG, JPG, SVG, GIF. 2 MB per file, 10 MB per skill. Every path `SKILL.md` mentions under `references/`, `scripts/`, or `assets/` must exist.

## 7. Style

- Write for a program designer or M&E lead who has never met a behavioral scientist. Define a term the first time you use it.
- Imperative mood in "How to do it". Explain the why in one clause when a step is not obvious.
- Ask before producing. A skill that gives a confident answer to an underspecified request is a failure mode, not a feature.
- Name the mechanism, not just the tactic. "Send a reminder" is a tactic; "reduce the attention cost at the moment of action" is a mechanism.
- Cite what you draw on. Flag what you are unsure of.

## 8. Running the validator

```bash
uv run scripts/besci_validate.py skills/<name>     # one skill
uv run scripts/besci_validate.py                    # all skills
uv run scripts/besci_validate.py --json             # for tools
```

Exit 0 means the structure is right. Content review by a maintainer is still required before merge.
