---
name: change-a-social-norm
title: Diagnose and shift a social norm
description: >-
  For a practice that a community keeps because each household expects the
  others to (open defecation, early marriage, skipping a clinic visit):
  establish whether it is a norm at all, find whose behavior and approval
  people track, measure the expectations, then choose between a message
  that corrects a misperception and a public pledge that changes the
  expectations together, with an ethics audit before launch. Does not cover
  the trial design or scale-up.
license: CC-BY-4.0
metadata:
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  stages: "diagnose, measure, design"
  skills: "diagnose-social-norm, map-reference-network, draft-norms-vignette, draft-cognitive-interview-script, write-social-norm-message, plan-collective-pledge, design-social-recognition, audit-intervention-ethics"
  tags: "social-norms, qualitative, survey-design"
---

## What it is for

Teams that say "everyone here does it" or "the community would not accept it" and are about to build a campaign on that claim. The workflow tests the claim, finds the reference group, measures the expectations, and only then picks the remedy, because a norm message works where a belief is mistaken and fails where the majority really does the unwanted thing.

## When to use it

- When a practice persists across households and the team suspects expectations, not individual preference, hold it in place
- When a norm message or a "declaration day" has been proposed and nobody has checked the true norm
- Not when the barrier is cost, access, or forgetting; use `diagnose-to-pilot`
- Not when the question is who should deliver a message about anything else; `select-messenger` alone

## Skills in this workflow

| Step | Skill | Version | Relationship | What carries forward | Human decision point |
|---|---|---|---|---|---|
| 1 | `diagnose-social-norm` | 0.1.0 | start | social norm diagnosis (norm, descriptive norm, custom, or moral rule) | Decide whether the field answers support calling it a norm; if custom or moral rule, leave this workflow |
| 2 | `map-reference-network` | 0.1.0 | after 1 | reference-group table by role and influence | Confirm the reference group with the community; decide who must be in the room |
| 3 | `draft-norms-vignette` | 0.1.0 | after 2 | vignette versions and the expectation survey | Pretest the scenes with `draft-cognitive-interview-script`; approve for a harmful practice only after the specialist route |
| 4a | `write-social-norm-message` | 0.1.0 | after 3, parallel with 4b, if the survey shows a mistaken belief about a favorable majority | norm message with injunctive cue | Verify the majority claim is true before anything is sent |
| 4b | `plan-collective-pledge` | 0.1.0 | after 3, parallel with 4a, if the survey shows a real unfavorable norm | pledge event plan | Postpone the event if the expected count falls short of the threshold |
| 5 | `design-social-recognition` | 0.1.0 | after 4b, optional | token or ceremony plan | Run the stigma screen first |
| 6 | `audit-intervention-ethics` | 0.1.0 | after 4a, 4b, or 5 | go / revise / stop | Act on the verdict; shaming and exposure are the usual revise reasons |

Relationship values: `start`, `after N`, `parallel with N`, `independent`, `optional`.

## How to run it

1. Run `diagnose-social-norm` with a first sample's answers to the four expectation questions. If the practice is a custom or a moral rule, stop: neither a norm message nor a pledge will move it, and the barrier belongs in `decompose-comb-barriers`.
2. Run `map-reference-network`. The reference group is often not the program's audience; the output says who must be reached.
3. Run `draft-norms-vignette` to build the survey that measures empirical and normative expectations with the factorial variation, and field it. The result decides step 4.
4. If most people already do the desired behavior and others underestimate that, run `write-social-norm-message` (4a). If the unwanted practice really is the majority, a message would backfire; run `plan-collective-pledge` (4b). Both may run when the diagnosis differs across subgroups.
5. Run `design-social-recognition` only when the pledge needs a visible, ongoing signal and the stigma screen passes.
6. Run `audit-intervention-ethics` on whatever step 4 or 5 produced. Pledge events and visibility carry the exposure risks the audit exists for.

## Worked example

A sanitation program in East Nusa Tenggara, Indonesia, believes villages keep open defecation because "it is the custom". Step 1's four questions show that most respondents think others defecate in the open and that others would mock a household that built a latrine first: a social norm, not a custom. Step 2 finds the reference group is the hamlet and the religious leader, not the village head the program had been working through. Step 3's vignettes confirm that respondents expect the protagonist to build a latrine when told that most hamlet households have and that the religious leader approves. The survey shows the real majority still defecates in the open, so step 4a is ruled out and step 4b plans a hamlet-level declaration with the religious leader as first mover and a coverage threshold before the event. Step 6 revises the plan to drop the named-household map the team had proposed.

## Where it goes wrong

- Sending a "most people do X" message where the survey shows X is a minority practice; the message publicizes the unwanted norm.
- Running step 4 on the staff's or leaders' account of the norm instead of the actors' answers from steps 1 and 3.
- Treating the program's beneficiaries as the reference group and never reaching the people whose approval the actors actually track.
- Skipping step 6 because the event is "community-led"; public commitment exposes dissenters, and the audit is where that is weighed.

## When to bring in a specialist

- Harmful traditional practices (child marriage, female genital cutting, violence): a safeguarding lead and a local researcher review every instrument and plan from step 1 onward; some questions cannot be asked and some events cannot be held.
- A reference group that spans villages or includes absent decision-makers (migrant husbands, employers): a social-network researcher designs the mapping.
- A pledge plan where the alternative behavior costs money the households do not have: program leadership decides on subsidies before anyone is asked to commit.
