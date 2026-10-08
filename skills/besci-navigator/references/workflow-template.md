---
# Copy to workflows/<your-workflow-name>.md. A workflow is a recommended set of
# skills for a larger task, with the relationships between them stated:
# ordered, parallel, or independent, and where a human decides.
name: your-workflow-name
title: Human-readable title
description: >-
  One paragraph: the larger task this workflow is for, who runs it, and what
  they have at the end. Say what it does not cover.
license: CC-BY-4.0
metadata:
  version: "0.1.0"
  status: draft
  authors: "Your Name"
  org: TAF
  stages: "define, diagnose, design"
  tags: "com-b, intervention-design"
---

## What it is for

Two or three sentences on the task and the situation it fits.

## When to use it

- When <situation>
- Not when <adjacent situation>; use <other workflow or a single skill> instead

## Skills in this workflow

| Step | Skill | Version | Relationship | What carries forward | Human decision point |
|---|---|---|---|---|---|
| 1 | `define-key-behavior` | 0.1.0 | start | target behavior brief | Confirm the behavior is the one the program can influence |
| 2 | `decompose-comb-barriers` | 0.1.0 | after 1 | barrier hypotheses | Choose which hypotheses to test in the field |
| 3a | `draft-cognitive-interview-script` | 0.1.0 | after 2, parallel with 3b | interview guide | Pick respondents |
| 3b | `map-behavioral-journey` | 0.1.0 | after 2, parallel with 3a | journey map | None |
| 4 | `select-intervention-levers` | 0.1.0 | after 3a and 3b | candidate levers | Field evidence must confirm at least one barrier before this step |

Relationship values: `start`, `after N`, `parallel with N`, `independent`, `optional`.

## How to run it

1. <Step-by-step, including what to hand from one skill to the next and when to stop and look at real data.>
2. <...>

## Worked example

<A short, real-feeling walk-through with one program. Show the hand-offs.>

## Where it goes wrong

- <Running step 4 without field evidence for step 2.>
- <Treating the sequence as fixed when the context calls for reordering.>

## When to bring in a specialist

- <Conditions, specialist type, what to bring.>
