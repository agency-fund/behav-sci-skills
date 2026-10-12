---
name: design-pilot-feasibility-study
description: >-
  Use when a team is about to run a small first version of an intervention
  "to see if it works" and needs to decide what the pilot must answer: can
  we recruit, do people stay, is it delivered as designed, do people accept
  it, does the outcome data come back usable. Also use when someone says
  "let's pilot it with 50 people first", asks what a feasibility study is,
  or is about to size the main trial from a pilot's effect estimate.
  Produces a pilot design with go, amend, or stop thresholds set before
  fieldwork, a size chosen for estimating rates rather than for
  significance, a qualitative component, and a report skeleton, following
  the CONSORT extension for pilot and feasibility trials (Eldridge et al.
  2016). Do not use when the question is whether the intervention works
  and how success will be measured; use plan-evaluation-design instead.
  Not for household negotiation of practice changes
  (plan-trials-of-improved-practices) or for monitoring delivery during
  rollout (design-fidelity-monitoring).
license: CC-BY-4.0
metadata:
  title: Design a pilot that tests feasibility, not effect
  type: atomic
  stage: test
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: not-applicable
  tags: "experimental-design, process-evaluation, implementation-science"
  consumes: "intervention-draft"
  produces: "evaluation-design"
---

## What it does

Designs a pilot whose job is to test feasibility (recruitment, retention, fidelity, acceptability, data completeness) against thresholds fixed before fieldwork, not to estimate the intervention's effect.

A pilot answers "can this be done as planned, with these people, by this team?" Each feasibility question gets a measurable rate, a threshold that says go, amend, or stop, and a planned change to the main design under each outcome. The pilot is sized to estimate those rates with usable precision. It is too small to say whether the intervention works, and its effect estimate must not be used to size the main trial.

## When to use it

### Use it when
- Someone says "let's pilot it with 50 people first" or "we'll do a small test run" with no statement of what the pilot has to show before the main trial goes ahead
- An intervention draft exists, the main trial is being planned, and the team asks "what should the pilot tell us?" or "what are progression criteria?"
- A pilot has already run and the team is about to take its effect estimate as the main trial's power input, or to read a promising-looking number as proof of concept
- A funder or ethics board asks for a feasibility study, progression criteria, or a go/no-go gate before funding the trial

### Do not use it when
- The question is whether the intervention works and how success will be measured; that is `plan-evaluation-design`, and the trial's structure is `choose-trial-design`
- The team wants households to try a new practice for a week and negotiate what they would keep; that is formative, household-level work in `plan-trials-of-improved-practices`
- The program is already rolling out and the question is whether it is being delivered as designed; `design-fidelity-monitoring`
- The question is how many people the main trial needs; `estimate-sample-size`, with a benchmark from `estimate-expected-effect`, never from the pilot

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The intervention draft: what is delivered, by whom, to whom, how often, through what channel. Paste it from the design skill that produced it.
2. **Required.** The main design the pilot serves: the unit of randomization, who delivers, how the outcome will be collected, and the planned size. If none exists yet, say so; every threshold will be marked provisional against an assumed main design.
3. **Required.** The pilot's resources: how many people or sites, over how long, with what staff, and whether anyone can run short interviews.
4. **Required.** The team's biggest worry: recruitment, dropout, delivery, acceptance, or data. The question whose answer would most change the main design gets the most precision.
5. Optional. Rates from a prior pilot or a similar program (recruitment, retention, data completeness) to anchor thresholds.

If 1 to 3 are missing, ask and stop. If 4 is missing, proceed with the five domains at equal weight and say so. If 5 is missing, derive thresholds from what the main trial needs and mark them provisional.

## What it draws on

- Eldridge, S. M., et al. (2016). CONSORT 2010 statement: Extension to randomised pilot and feasibility trials. *BMJ*, 355, i5239. https://doi.org/10.1136/bmj.i5239
- Bowen, D. J., et al. (2009). How we design feasibility studies. *American Journal of Preventive Medicine*, 36(5), 452–457. https://doi.org/10.1016/j.amepre.2009.02.002
- EGAP. *10 things to know about pilot studies*. https://egap.org/resource/10-things-to-know-about-pilot-studies/

Eldridge et al. extend the CONSORT reporting standard to randomized pilot and feasibility trials: a pilot's objectives are feasibility objectives, its results are reported against them, and the decision about the main trial follows from them. Bowen et al. set out how to design a feasibility study as a study of whether an intervention can be delivered and accepted, distinct from a study of whether it works. The EGAP guide covers the same ground for social-science field experiments. The dossier this skill draws on records one documented misuse: pilots are often wrongly used to estimate effect sizes for the main trial's power calculation. A pilot is small by construction, so its effect estimate is noisy and, when it is used because it looked promising, selected for being high.

The judgment calls this skill adds: the five feasibility domains (recruitment, retention, fidelity, acceptability, data completeness; the dossier names the first four), the three-way go / amend / stop threshold rather than a binary go / no-go, the rule that every threshold is derived from what the main design needs, the rule that the pilot is sized for the precision of a rate rather than for detecting an effect, and the mandatory qualitative component that asks dropouts and deliverers why.

**WEIRD skew:** The anchor sources are trial-methodology guidance from clinical and public-health research; the method is procedural and does not depend on a population. What a user elsewhere should check locally: how recruitment actually happens (gatekeepers, community entry, consent norms), whether the data system the main trial assumes exists at the pilot sites, and whether the pilot season matches the main trial's (planting, school terms, rains), since feasibility rates move with timing. **Non-WEIRD evidence:** none found in the sources this skill draws on; the household-level cousin, Trials of Improved Practices (`plan-trials-of-improved-practices`), is the LMIC-origin method the dossier points to for formative testing with households.

**Replication status:** Method guidance, not an effect; uncontested that a pilot's purpose is feasibility. The one contested practice, sizing the main trial from the pilot's effect estimate, is what this skill tells the model to refuse.

## How to do it

1. **Carry over the intervention draft and the intended main design** at the top, so every threshold is visibly derived from a main design the pilot serves.
2. **List the feasibility questions under five domains**, each as a measurable rate or count: recruitment (what share of those approached enroll, at what rate per week), retention (what share reach the pilot's endline), fidelity (what share of planned sessions, messages, or visits happen as designed), acceptability (what share complete it, what participants and deliverers refuse or change), data completeness (what share of enrolled people have a usable outcome measure).
3. **Set a go / amend / stop threshold for each before fieldwork.** Derive it from the main design: the retention threshold from the attrition the main sample assumes, the recruitment threshold from the enrollment rate the main timeline needs. Write what "amend" means: which part of the design changes if the rate lands there.
4. **Size the pilot for estimating rates, not for significance.** For the rate that matters most (question 4 of Before you start), state the margin the team can act on and choose the number of people or sites that estimates the rate to that margin; the number needed to estimate a rate to a usable margin is usually far below the number needed to detect an effect. Write the sentence "this pilot's effect estimate will not be used to size the main trial" into the design.
5. **Plan the qualitative component.** Short interviews with people who dropped out, refused, or delivered the intervention, each with the one question it must answer (why they left, what they changed, what got in the way), who runs them, and when.
6. **Decide what changes in the main design under each outcome**, as a table: question, result band, design change. A pilot whose results change nothing was not a pilot.
7. **Write the report skeleton** in the spirit of the CONSORT extension: participant flow (approached, eligible, enrolled, retained, with outcome data), each feasibility question with threshold, observed value with its uncertainty, and decision, the qualitative reasons, the changes to the main design, and any effect-direction observation labeled as not a basis for sizing.
8. **Stop here.** The main trial's measurement plan is `plan-evaluation-design`, its size is `estimate-sample-size`, and monitoring delivery during rollout is `design-fidelity-monitoring`.

See `references/worked-example.md` for a complete run on an antenatal iron-folate adherence program in Malawi, and `references/evidence-notes.md` for the sources with their verification state.

## Output template

```markdown
# Pilot feasibility study design

**Intervention piloted:** <carried over verbatim>
**Main design it serves:** <unit of randomization, delivery, outcome collection, planned size; or "assumed, not yet designed">
**What this pilot is not for:** estimating the intervention's effect. Its effect estimate will not be used to size the main trial.

## Feasibility questions and progression criteria
| Domain | Question (as a rate or count) | Go | Amend | Stop | Why this threshold |
|---|---|---|---|---|---|
| Recruitment | <...> | <...> | <...> | <...> | <derived from the main design's ...> |
| Retention | <...> | | | | |
| Fidelity | <...> | | | | |
| Acceptability | <...> | | | | |
| Data completeness | <...> | | | | |

## Pilot size
<the rate that most needs estimating; the margin the team can act on; the number of people or sites that gives it; duration; why this is not a power calculation>

## Qualitative component
<who is interviewed (dropouts, refusers, deliverers), the one question each interview must answer, who runs them, when>

## What changes in the main design
| Question | If go | If amend | If stop |
|---|---|---|---|
| <...> | <no change> | <named design change> | <named stop or redesign> |

## Report skeleton
1. Participant flow: approached, eligible, enrolled, retained, with usable outcome data
2. Each feasibility question: threshold, observed value with its uncertainty, decision
3. Fidelity and acceptability findings, with the qualitative reasons
4. Changes to the main design
5. Any effect-direction observation, labeled "not a basis for sizing the main trial"

## Open questions
- <the assumption most likely to be wrong>
```

## Where it goes wrong

- **Sizing the main trial from the pilot.** A pilot's effect estimate is noisy and, when chosen because it looked good, inflated. The main trial's power input comes from a benchmark (`estimate-expected-effect`), never from the pilot. Refuse to supply the pilot's effect for that purpose.
- **Thresholds written after the data.** Without go / amend / stop bands fixed before fieldwork, whatever happened reads as "promising". The thresholds and their derivation are written into the design, dated.
- **Powering the pilot.** Choosing the pilot size from a power calculation turns it into a small, underpowered trial that answers neither question. Size for the precision of a rate.
- **Counting without asking.** A retention rate of sixty percent with no interviews says nothing about whether the sixty would be forty in the main trial. The qualitative component is mandatory.
- **"Amend" that names nothing.** An amend band with no attached design change is a go band in disguise. Every amend cell names the change.
- **One site standing in for everywhere.** Feasibility at the most cooperative clinic or in the easiest season does not transfer; say which sites and which season the pilot covered and what that leaves unknown.

## When to bring in a specialist

Tell the user to consult a statistician or evaluation methodologist, and an ethics reviewer where relevant, when:
- The team intends to use the pilot's effect estimate as the main trial's power input; bring the pilot design and route the sizing to `estimate-expected-effect` and `estimate-sample-size` with a statistician
- The intervention touches clinical risk, medication, or vulnerable participants, so even the pilot needs ethics review and a stopping rule for harm
- Recruitment or acceptability thresholds are failing in a way that points to coercion, stigma, or community refusal rather than logistics; a local qualitative researcher should read the interviews before any amend decision
- The main design is clustered or stepped-wedge and the pilot has to test the rollout mechanics themselves

Bring them: the progression-criteria table with its derivations, the pilot size reasoning, the main design, and the interview notes.
