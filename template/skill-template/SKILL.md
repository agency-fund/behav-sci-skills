---
# Copy this folder to skills/<your-skill-name>/ and rename it. The folder name
# and the `name` field must match. Delete these comments when done.
# Run: uv run scripts/besci_validate.py skills/<your-skill-name>
name: your-skill-name
description: >-
  Use when <the specific situation or user intent that should fire this
  skill, in the words a user would use>. Also use when <a second trigger>.
  Do not use when <the nearest adjacent intent>; use <other skill> instead.
  Not for <a second thing people might confuse this with>.
license: CC-BY-4.0
metadata:
  title: Human-readable title for the catalog
  type: atomic                 # atomic | meta
  stage: diagnose              # define | diagnose | design | measure | test | analyze | implement | other
  version: "0.1.0"
  status: draft
  authors: "Your Name"
  org: TAF                     # TAF | IL | community
  weird: mixed-evidence        # weird-only | mixed-evidence | likely-generalizes | untested-outside-weird | not-applicable
  tags: "framework-name, method-name"
  consumes: ""                 # optional io_types ids from taxonomy.yaml, comma-separated
  produces: ""                 # optional io_types ids from taxonomy.yaml
---

## What it does

One sentence, no "and". Then one short paragraph at most.

## When to use it

### Use it when
- A user says something like "..."
- A user has <input state> and asks for <operation>
- A team is about to <common mistake this skill prevents>

### Do not use it when
- The user wants <adjacent thing>; point them to <other skill or resource>
- The input is still <too vague / too far upstream>; run <upstream skill> first

## Before you start

Ask these before producing anything. Say which answers you will assume if missing.

1. **Required.** <Question about the target behavior, population, or context.>
2. **Required.** <Question that changes which branch of the method applies.>
3. Optional. <Question that improves the output if known.>

If the user has already given an answer in the conversation, do not ask again.

<!-- Or, if the skill genuinely does not need to ask:
Not applicable: <one real sentence saying why, e.g. "this skill transforms a measurement plan the upstream skill already gathered, and adds no new judgement call">.
-->

## What it draws on

- Author, A., & Author, B. (Year). Title. *Venue*. https://doi.org/...
- Author, C. (Year). Title. *Venue*.

**WEIRD skew:** <Where the evidence comes from and what a user elsewhere should validate locally.>

**Replication status:** <Replicated / mixed / contested / single study, in one sentence.>

## How to do it

1. <First step, imperative, with the reason it matters if not obvious.>
2. <Second step.> See `references/method-notes.md` for the detail.
3. <Produce the output using the template below. Fill every placeholder or say why it is blank.>

## Output template

```markdown
# <Title of the output>

**Context:** <who, what, when, carried over from the user's answers>

## <Section 1>
- <item>

## <Section 2>
- <item>

## What to check before relying on this
- <the assumption most likely to be wrong>
```

## Where it goes wrong

- <A failure mode the model is prone to with this method, and the instruction that prevents it.>
- <An input that breaks the method.>
- <Something the skill must refuse to do.>

## When to bring in a specialist

Tell the user to consult a <kind of specialist> when:
- <concrete condition>
- <concrete condition>

Bring them: <what to prepare so the conversation is efficient>.

<!-- Or:
Not applicable: <one real sentence saying why this narrow technical skill has no judgement call a user could get wrong>.
-->
