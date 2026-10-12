---
name: diagnose-to-pilot
title: From a vague goal to a piloted intervention
description: >-
  The core behavioral-design sequence for a program team that has a goal
  ("more mothers complete antenatal care") and no behavioral diagnosis yet:
  define one behavior, generate barrier hypotheses, test them in interviews,
  pick a lever, draft it with the technique skill that owns it, and plan a
  feasibility pilot and the measurement. Ends with a pilot plan and a
  pre-registration-style measurement plan. Does not cover the main trial's
  analysis or scale-up.
license: CC-BY-4.0
metadata:
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  stages: "define, diagnose, design, test"
  skills: "define-key-behavior, score-candidate-behaviors, decompose-comb-barriers, draft-tdf-interview-guide, synthesize-interview-findings, select-intervention-levers, draft-lever-content, audit-intervention-ethics, design-pilot-feasibility-study, plan-evaluation-design"
  tags: "com-b, behavior-change-wheel, tdf, pilot"
---

## What it is for

A team that knows what outcome it wants and is tempted to jump to an intervention ("let's send a text"). The workflow forces the diagnosis before the design, puts one round of real field data between the hypotheses and the lever, and ends in a pilot that tests feasibility before anyone measures effect.

## When to use it

- When a program goal exists but nobody has named the behavior, the barrier, or the lever
- When a team has an intervention idea and cannot say which barrier it addresses
- Not when the practice is held in place by community expectations; use `change-a-social-norm` instead
- Not when the product is a digital funnel with drop-off data; run `build-user-funnel` and `diagnose-funnel-weak-link` and rejoin this workflow at step 5

## Skills in this workflow

| Step | Skill | Version | Relationship | What carries forward | Human decision point |
|---|---|---|---|---|---|
| 1 | `define-key-behavior` | 0.1.0 | start | target behavior brief | Confirm the behavior is one the program can influence and observe |
| 2 | `decompose-comb-barriers` | 0.1.0 | after 1 | COM-B hypotheses with diagnostic questions | Choose which hypotheses the field round will test |
| 3 | `draft-tdf-interview-guide` | 0.1.0 | after 2 | interview guide | Pick respondents; ethical review of questions if the behavior is sensitive |
| 4 | `synthesize-interview-findings` | 0.1.0 | after 3, once interviews are done | confirmed barrier diagnosis | Decide whether one barrier is confirmed or another field round is needed |
| 5 | `select-intervention-levers` | 0.1.0 | after 4 | one function and one technique | Accept the lever, or send the rejected functions back as the next pilot |
| 6 | the technique skill named by step 5 (for example `design-reminder-schedule`, `select-default-option`, `write-social-norm-message`, `design-incentive-scheme`), or `draft-lever-content` when no technique skill fits | 0.1.0 | after 5 | intervention draft | Review the draft's boundary conditions and backfire line |
| 7 | `audit-intervention-ethics` | 0.1.0 | after 6, optional unless step 6 used a default, incentive, pledge, or recognition | go / revise / stop | Act on a revise or stop verdict |
| 8 | `design-pilot-feasibility-study` | 0.1.0 | after 7 | pilot plan with progression criteria | Set the go / amend / stop thresholds before fieldwork |
| 9 | `plan-evaluation-design` | 0.1.0 | after 8, parallel with running the pilot | measurement plan | Lock the plan before any outcome data exist |

Relationship values: `start`, `after N`, `parallel with N`, `independent`, `optional`.

## How to run it

1. Run `define-key-behavior` on the goal. If it returns several candidate behaviors and the team cannot choose, run `score-candidate-behaviors` first and bring the winner back.
2. Run `decompose-comb-barriers` on the behavior brief. Stop and look at the hypothesis list: the team picks the two or three worth a field round, by the ranking table's context-support and field-cost columns.
3. Run `draft-tdf-interview-guide` on those hypotheses. Field the interviews. Nothing in this workflow proceeds on hypotheses alone.
4. Run `synthesize-interview-findings` on the transcripts or notes. If no hypothesis is supported, go back to step 2 with what was learned; if two are supported, a specialist decides whether a sharper study is cheaper than a wrong pilot.
5. Run `select-intervention-levers` on the confirmed barrier. Keep its rejected functions; they are the next pilot if this one fails.
6. Run the technique skill that owns the selected technique. If none does, `draft-lever-content` is the generic writer.
7. Run `audit-intervention-ethics` if the technique moves money, sets a default, makes behavior visible, or convenes a pledge.
8. Run `design-pilot-feasibility-study`. The pilot answers "can we deliver this and will people take it up", not "does it work".
9. Run `plan-evaluation-design` while the pilot runs, so the measurement plan is locked before any outcome data exist. Hand its output to `estimate-sample-size` and `write-pre-analysis-plan` when the team moves to a trial.

## Worked example

A maternal-health program in Malawi wants more women to take iron-folate tablets daily. Step 1 fixes the behavior: enrolled women take one tablet every day from the first antenatal visit until delivery. Step 2 lists hypotheses across COM-B; the team chooses to test nausea (Motivation, automatic), husbands' disapproval of "hospital medicine" (Opportunity, social), and forgetting (Capability, psychological). Step 3 produces a guide; twenty interviews with women and six with health surveillance assistants are run. Step 4's matrix supports forgetting and nausea and does not support husbands' disapproval. Step 5 selects Environmental restructuring with a cue-based technique for forgetting, keeping Education on nausea management as the next pilot. Step 6 runs `design-habit-anchor`, tying the tablet to the morning tea. Step 7 is skipped (no money, no default, no visibility). Step 8 plans a four-clinic pilot with progression criteria on take-up of the anchor and tick-sheet completion. Step 9 locks the measurement plan: pill counts at the next visit as the primary outcome.

## Where it goes wrong

- Running step 5 on the ranked hypotheses from step 2 without the field round in steps 3 and 4; the lever then addresses a guess.
- Treating the pilot in step 8 as the effect test and powering the trial on its numbers; the pilot measures feasibility.
- Skipping step 7 because the intervention "is just a message" when the message carries a norm or a loss frame; the ethics audit is cheap and the backfire is not.
- Reordering so the technique skill runs before `select-intervention-levers`; the technique skills assume a confirmed barrier and a chosen function.

## When to bring in a specialist

- Any behavior with clinical, safety, or child-protection risk: a clinician or safeguarding lead reviews the interview guide (step 3) and the intervention draft (step 6) before fieldwork.
- Two barriers both supported at step 4, or thin evidence for one: a behavioral scientist or qualitative researcher designs the next field round.
- A trial after the pilot: an evaluator or statistician owns `estimate-sample-size` and `write-pre-analysis-plan`. Bring them the measurement plan from step 9 and the pilot report.
