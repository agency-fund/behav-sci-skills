---
name: identify-positive-deviants
description: >-
  Use when some people in a population already succeed at a behavior or
  outcome under the same constraints as everyone else and you want to find out
  who they are and what they do differently. Also use when a team says
  "positive deviance", "bright spots", "what are the successful ones doing",
  or wants to learn from existing local solutions before designing anything.
  Produces deviant-selection criteria (same constraints, verified outcome), an
  inquiry plan, and a practices table comparing common practice with deviant
  practice and what makes it feasible, as diagnostic input. Do not use when
  you already have a practice and want to test whether households will adopt
  it; use plan-trials-of-improved-practices instead. Not for generating
  barrier hypotheses from a framework (decompose-comb-barriers), not for
  writing the interview guide (draft-tdf-interview-guide), and not for running
  positive deviance as an intervention, whose evidence on outcomes is weak or
  null.
license: CC-BY-4.0
metadata:
  title: Find who already succeeds under the same constraints
  type: atomic
  stage: diagnose
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "qualitative, com-b, diagnosis"
  consumes: "target-behavior-brief"
  produces: ""
---

## What it does

Finds the people who already succeed at one behavior under the same constraints as their neighbors, then documents what they do differently as diagnostic input.

Positive deviance is the observation, from Save the Children's child-nutrition work in Vietnam, that in most communities a few households reach a better outcome with no more resources than the rest, and that their practices are a source of solutions that are already feasible locally. This skill uses it as an inquiry method: who the deviants are, what they do, and what makes it possible. It does not run the "positive deviance/Hearth" program that spreads those practices; as an intervention, the evidence on child growth is weak or null, and the output says so.

## When to use it

### Use it when
- Monitoring or administrative data show that a minority of people, households, or sites reach the outcome while most do not, and the team asks "what are the successful ones doing?"
- A team says "positive deviance", "bright spots", or "learn from the ones who manage" before designing an intervention
- `decompose-comb-barriers` has produced hypotheses and the team wants enablers that already exist locally, not only barriers, as evidence for or against them
- A program is about to import a practice from elsewhere and wants to check first whether a local, feasible version already exists

### Do not use it when
- A candidate practice is already in hand and the question is whether households will try it and keep it; that is `plan-trials-of-improved-practices`
- The question is why most people are not doing the behavior, with no outcome data in which to find deviants; run `decompose-comb-barriers` first
- The team wants an interview guide for a general diagnosis; that is `draft-tdf-interview-guide`
- A confirmed barrier exists and the team wants to choose what to do about it; that is `select-intervention-levers`
- The team wants to run positive deviance as the intervention (spread the practices through group sessions) and expects outcome gains; this skill does not design that, and the evidence does not support the expectation

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The target behavior or the outcome that defines success, as who, what, when, and the source that can verify it (program records, measurements, observation). Self-report alone makes a weak deviant; say so if it is all there is.
2. **Required.** The constraints everyone shares that define "same constraints": income or asset band, land size, distance to services, program inputs received, household size. Without these, the inquiry finds the better-off, not deviants.
3. **Required.** What can be used to screen for candidates: monitoring records, administrative data, or community nomination, and over what period.
4. Optional. Who will do the inquiry (program staff, community members, both) and what field access exists.
5. Optional. Whether success is confidential or stigmatized (a health status, a legal status), or whether naming deviants could shame the rest.

If 1 is missing, ask and stop. If 2 is missing, ask once; if the answer is still thin, propose a constraints screen from the context and mark it "proposed by this skill". If 3 is missing, assume community nomination followed by a verification visit and mark the assumption. If 4 and 5 are missing, assume a staff-led inquiry on a non-sensitive outcome.

## What it draws on

- Pascale, R. T., Sternin, J., & Sternin, M. (2010). *The Power of Positive Deviance*. Harvard Business Press.
- Marsh, D. R., et al. (2004). The power of positive deviance. *BMJ*, 329, 1177. https://doi.org/10.1136/bmj.329.7475.1177
- Bisits Bullen (2011). The positive deviance/hearth approach to reducing child malnutrition: Systematic review. *Tropical Medicine & International Health*. https://doi.org/10.1111/j.1365-3156.2011.02839.x
- Triatmaja et al. (2023). Effectiveness of positive deviance approach to reduce malnutrition among under five children: A systematic review and meta-analysis of interventional studies. *Nutrients*, 15(8), 1961. https://doi.org/10.3390/nu15081961

Pascale, Sternin and Sternin (2010) and Marsh et al. (2004) describe the approach: define the outcome, screen for outliers who succeed under the same constraints, inquire into their practices, verify with the community. The mechanism, as an inquiry, is that a practice a resource-poor household already sustains has passed a feasibility test that an imported practice has not. The two reviews cover positive deviance as an intervention for child malnutrition (the "Hearth" program, in which caregivers of malnourished children practice the deviants' feeding behaviors together). Bisits Bullen (2011) found the included studies were mostly uncontrolled; Triatmaja et al. (2023) pooled interventional studies and found no significant differences in growth z-scores (the dossier does not quote the effect sizes). The judgment calls this skill adds: a candidate must sustain the outcome over more than one period, so one lucky month does not count; a matched set of non-deviants is inquired into with the same protocol, so "different" is checked rather than assumed; every practice is tagged observed or reported; and the output states what it cannot show.

**WEIRD skew:** the approach originated in Vietnam child-nutrition work (Save the Children) and has been used mostly in programs in low- and middle-income countries, so the method itself is not WEIRD-skewed. **Non-WEIRD evidence:** the Vietnam origin and the many LMIC uses recorded in the labs report; the 2011 review and the 2023 meta-analysis cover child-malnutrition programs in LMIC settings, with the null growth result above. A user should check locally that the constraints screen captures the resources that matter here (remittances, a relative in town, a motorbike) and that identifying deviants does not expose or shame anyone.

**Replication status:** as an intervention, weak or null: the 2023 meta-analysis found no significant growth z-score differences, and the 2011 review's studies were mostly uncontrolled. As an inquiry method there is no validation study; it is a practitioner method, and its value lies in the feasibility of what it finds, not in an effect.

## How to do it

1. **Define success operationally**: the outcome, the threshold, the period over which it must hold (at least two measurement periods, to exclude a single good month), and the verification source. Carry the target behavior over verbatim.
2. **Write the shared-constraints screen**: the variables and cutoffs a candidate must fall inside. A candidate outside any cutoff is a resource deviant, not a positive deviant, and is excluded, because a practice that depends on resources others lack is not feasible for them.
3. **Screen for candidates**: apply the threshold to the data, apply the constraints screen, verify the outcome against the source, verify the constraints by a visit or record. List candidates anonymized, with how each was verified.
4. **Plan the inquiry**: for each deviant, an observation visit at the moment the behavior happens plus an interview about what they do, when, with whom, how, and what it costs. Run the same protocol with a matched set of non-deviants under the same constraints. Observe before asking, because people describe what they think they do.
5. **Build the practices table**: for each practice, the common practice, the deviant practice, what makes it feasible (cost, time, materials, skill, social acceptability), whether it was observed or only reported, and the COM-B hypothesis it bears on as a candidate enabler.
6. **Verify with the community**: present the practices, not the names, to a group of community members under the same constraints, and ask whether each is recognized, acceptable, and doable by a household like theirs. Drop practices that depend on hidden resources or that the community rejects.
7. **State what the output cannot show**: that the practices cause the outcome, or that spreading them would move it. Cite the null intervention evidence in the output so nobody downstream promises gains.
8. **Stop here.** The practices are diagnostic input: enablers for `decompose-comb-barriers` to weigh, a candidate practice for `plan-trials-of-improved-practices` to test with households, or evidence for `select-intervention-levers` once a barrier is confirmed.

See `references/worked-example.md` for a complete run on community health agents' condom sales in Lusaka, Zambia, and `references/evidence-notes.md` for the sources.

## Output template

```markdown
# Positive deviance inquiry: <short name of the behavior or outcome>

**Target behavior or outcome:** <who + what + when, carried over verbatim>
**Success defined as:** <outcome, threshold, period> verified by <source>
**Shared-constraints screen:** <variable: cutoff>; <variable: cutoff>; ... (anyone outside is excluded as a resource deviant)

## Deviant-selection criteria
| Criterion | Rule | How verified |
|---|---|---|
| Outcome | <...> | <...> |
| Sustained over | <...> | <...> |
| Same constraints | <...> | <...> |
| Excluded if | <...> | <...> |

## Candidate list
| Unit (anonymized) | Outcome by period | Constraints check | Verified by |
|---|---|---|---|
| <...> | <...> | <...> | <...> |

## Inquiry plan
- Deviants: <n>; observation of <what, when> plus interview on <what they do, when, with whom, how, what it costs, what others say>
- Matched non-deviants: <n>, same protocol, matched on <...>
- Who inquires: <...> | Field dates: <...> | Consent and confidentiality: <...>
- Community verification session: <who attends, how practices are presented without names, what is asked>

## Practices table
| Common practice | Deviant practice | What makes it feasible | Observed or reported | Bears on hypothesis |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> |

## Open questions
- <practices not yet verified, and how to verify them>
- <candidates who may still be resource deviants, and what would show it>

## What this does not show
- Whether these practices cause the outcome, or whether spreading them would change it. As an intervention, positive deviance has weak or null evidence (Triatmaja et al. 2023; Bisits Bullen 2011). Testing a practice with households is plan-trials-of-improved-practices.
```

## Where it goes wrong

- **Resource deviants.** The "deviant" has a relative sending money, a motorbike, a second earner, or a better plot. The constraints screen exists to catch this; if the candidate list has no exclusions, the screen was too loose.
- **One lucky period.** A unit that hit the threshold once is as likely to be noise as a deviant. Require the outcome over more than one period before inquiry, and say which periods.
- **Nominated favorites.** Staff nominate the cooperative, the articulate, or the ones they visit most; communities nominate the respected. Verify nominations against the outcome source before anyone is interviewed.
- **No comparison.** A practice listed from deviant interviews alone may be universal. The matched non-deviants are what make "different" a finding instead of an assumption.
- **Reported as observed.** "I feed the child four times a day" is a report. Mark every practice observed or reported, and do not promote a reported practice to the feasible column without a visit.
- **Sliding into the intervention.** The output lists practices; it does not design the sessions that spread them or promise what spreading them will do. The intervention evidence is null on growth, and the skill must say so rather than let the practices table read as a program.

## When to bring in a specialist

Tell the user to consult a clinician or public-health specialist for the outcome, plus the relevant ethics review body, when:
- Success is a clinical or confidential status (viral suppression, nutritional recovery, mental health), because the threshold needs a clinical definition and identifying deviants can disclose status
- The screen yields only a handful of candidates, or the community verification could expose or shame the households that do not succeed
- The team intends to run positive deviance as the program (Hearth-style sessions) and expects outcome gains; bring an evaluation specialist, because the intervention evidence does not support the expectation

Bring them: the success definition and verification source, the constraints screen, the anonymized candidate list, and the practices table with its observed/reported tags.
