---
name: assess-scalability
description: >-
  Use when a pilot or trial showed an effect and someone asks "will this work
  at scale?", "can we take this national?", "should we hand this to the
  government?", or "what breaks when we go from 20 sites to 2,000?". Also use
  when a proposal carries a pilot effect size straight into a scale-up budget,
  or when the implementer, the population, or the cost per person will change
  on the way to scale. Tests the pilot's claim against the named threats to
  scalability (false positive, population, situation and implementer,
  spillovers, cost at scale; Al-Ubaydli, List and Suskind 2020; DellaVigna and
  Linos 2022), scores scalability domains after Milat et al. 2020, and returns
  a verdict with what must be tested before scaling. Do not use to plan how
  the scale-up happens; that is plan-scale-up-strategy. Not for cost per
  outcome at scale (estimate-cost-effectiveness), and not for judging whether
  someone else's published finding fits your setting before any test
  (assess-evidence-transferability).
license: CC-BY-4.0
metadata:
  title: Check whether a pilot effect will survive scale-up
  type: atomic
  stage: implement
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "scaling, implementation-science, heterogeneity"
  consumes: "evaluation-design, intervention-description"
  produces: "scalability-assessment"
---

## What it does

Judges whether an effect measured in a pilot is likely to hold when the program is delivered at scale, by testing the pilot's claim against the named threats to scalability.

A pilot effect is a fact about particular people, a particular implementer, a particular cost, and one draw of the data. Scale changes all four. This skill writes the pilot's claim in one line, asks of each threat what the pilot's own evidence says for and against it, names the test that would settle each, scores the assessment domains, and returns one of three verdicts: scale, scale after these tests, or do not scale yet. It does not plan the scale-up, and it does not compute cost per outcome.

## When to use it

### Use it when
- Someone asks "will this work at scale?", "can we take this national?", or "what breaks when we go from 20 clinics to 2,000?"
- A funding proposal or policy brief carries the pilot's effect size straight into a scale-up budget or an impact projection
- The implementer will change on the way to scale: from an NGO or research team to a ministry, a county, or a contractor
- The population at scale will differ from the pilot's (the pilot recruited volunteers, one region, or one language group)
- A government partner has asked to adopt a program on the strength of one evaluation

### Do not use it when
- The question is how to run the scale-up (who delivers, in what sequence, with what budget); that is `plan-scale-up-strategy`, which consumes this skill's output
- The question is cost per outcome at scale; `estimate-cost-effectiveness` owns that number, and this skill only asks whether cost will change
- No pilot or trial has been run yet and the question is whether a published finding fits your setting; `assess-evidence-transferability`
- The question is who benefited within the pilot; `analyze-heterogeneous-effects`, whose output feeds the population threat here
- A past scale-up failed and the team wants to know why; `review-prior-intervention`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The pilot's claim: the outcome, the effect with its unit and uncertainty, the population it was measured on (who, where, how many), who delivered it, and the cost per person or site as delivered. Paste the evaluation design and the intervention description if they exist.
2. **Required.** The scale-up on the table: how many more people or sites, who would deliver, through which system, and what would change in the delivered version (shorter, cheaper, different staff, different channel).
3. **Required.** The decision this informs and whether it can be reversed: a go or no-go, a staged roll-out, a budget line, a handover to government.
4. Optional. Who benefited within the pilot, from `analyze-heterogeneous-effects` or the pilot's own subgroup results.
5. Optional. Evidence on delivery quality in the pilot: fidelity or monitoring data, and how implementers were selected, trained, supervised, and paid.
6. Optional. Any earlier attempt to scale this or a similar program in the same system, with the record from `review-prior-intervention`.

If 1 or 2 is missing, ask and stop. If 3 is missing, assume a reversible go or no-go and say so. If 4, 5, or 6 is missing, proceed and mark the affected threat "no pilot evidence either way".

## What it draws on

- Milat, A. J., et al. (2020). Intervention Scalability Assessment Tool: A decision support tool for health policy makers and implementers. *Health Research Policy and Systems*, 18. https://doi.org/10.1186/s12961-019-0494-2
- Al-Ubaydli, O., List, J. A., & Suskind, D. (2020). 2017 Klein Lecture: The science of using science: Toward an understanding of the threats to scalability. *International Economic Review*, 61(4), 1387–1409. https://doi.org/10.1111/iere.12476
- Bold, T., et al. (2018). Experimental evidence on scaling up education reforms in Kenya. *Journal of Public Economics*, 168, 1–20. https://doi.org/10.1016/j.jpubeco.2018.08.007
- Banerjee, A., et al. (2017). From proof of concept to scalable policies: Challenges and solutions, with an application. *Journal of Economic Perspectives*, 31(4), 73–102. https://doi.org/10.1257/jep.31.4.73
- List, J. A. (2022). *The Voltage Effect: How to Make Good Ideas Great and Great Ideas Scale*. Crown. https://openlibrary.org/isbn/9780593239483.json (the record confirms title, subtitle, publisher, and year; the author name is not in the record)
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709

Al-Ubaydli, List and Suskind set out the threats to scalability, which the dossier summarizes as population representativeness, implementer quality, spillovers, and cost; List's book carries the same argument for a general audience. DellaVigna and Linos supply the threat that comes before all of these, the false positive: across 126 RCTs and 23 million people, academic journal studies averaged 8.7 percentage points (+33.4%) while the nudge units' own trials averaged 1.4 points (+8.0%), with about 70% of the gap explained by selective publication combined with low power. Bold et al. are the implementer case: the same contract-teacher program in Kenya delivered by an NGO and by the government gave different results. The dossier records the contrast and no effect sizes; the direction (an effect under NGO delivery that did not appear under government delivery) is as this library's drafting brief states it, unverified, author to confirm from the paper. Banerjee et al. use Pratham's Teaching at the Right Level in India as the case of moving from proof of concept to a policy a government can run. Milat et al.'s Intervention Scalability Assessment Tool (ISAT) is a decision-support tool for scoring an intervention's readiness to scale; the dossier records the tool and not its domain list, so the domains this skill scores are a generic set written for this library, marked as such in the output (unverified, author to confirm against the published tool). The judgment calls this skill adds, none of them published criteria: a one-line claim as the unit of assessment; "evidence for, evidence against, test that would settle it" for every threat; and a three-way verdict with a "what must be true" list.

**WEIRD skew:** The threats are general; the false-positive numbers come from US government units only, so a user elsewhere should treat the 8.7-to-1.4 gap as a direction, not a rate. Which threat bites hardest is local: the implementer threat dominates where a government system will deliver with different selection, supervision, and pay than the pilot's; the spillover threat dominates where the program moves prices, queues, or shared resources. **Non-WEIRD evidence:** Kenya (Bold et al. 2018; the contract-teacher program; NGO versus government delivery, no effect sizes recorded in the dossier) and India (Banerjee et al. 2017; Pratham's Teaching at the Right Level, from proof of concept to scaled policy, no effect sizes recorded in the dossier).

**Replication status:** Well supported: the threats are documented in independent LMIC cases (Kenya, India) and in the two-nudge-unit comparison, and the dossier records no contesting evidence. The ISAT is a decision tool, not an effect, so there is nothing to replicate; whether its scores predict successful scale-up is not reported in the sources this skill draws on.

## How to do it

1. **Write the claim in one line**: effect with unit, outcome, population, implementer, cost per unit. Everything below tests this line, so if the user cannot fill a field, write "not reported" and keep it visible.
2. **Test the false-positive threat.** Ask whether the result was pre-registered, how large the sample was, whether the effect is the only estimate or one of many, and whether a second study exists. State the published-to-field gap (8.7 against 1.4 points) as the reason a single pilot estimate is an upper bound, not a forecast.
3. **Test population representativeness.** Compare who was in the pilot (how recruited, where, consenting to what) with who will be reached at scale. Use the heterogeneity results if supplied; if the pilot effect was carried by a subgroup that is a smaller share of the scale population, say so and discount.
4. **Test the situation, above all the implementer.** Write who delivered the pilot and how they were selected, trained, supervised, and paid, then the same for the implementer at scale. Where delivery moves from an NGO or research team to a government system, name this as the threat with the strongest LMIC evidence (Bold et al.) and treat "same program, different implementer" as a different program until tested.
5. **Test spillovers.** Ask what happens when most people in an area are treated rather than a few: shared resources, queues, prices, staff time, or the behavior of untreated neighbors. Say which direction each pushes the effect.
6. **Test cost at scale.** List what drove the pilot's per-unit cost and which lines fall (fixed costs spread), which rise (supervision, logistics, quality), and which disappear (research staff). Do not compute cost per outcome; hand that to `estimate-cost-effectiveness`.
7. **For each threat, write three lines**: evidence for it from the pilot, evidence against it, and the test that would settle it, with a rough cost and time. "No pilot evidence either way" is a legitimate entry, and it counts against scaling now.
8. **Score the domains** in the table, 1 to 5, with the evidence behind each score in the same row. A score with no evidence cell is not a score.
9. **Give the verdict**: scale; scale after these tests; or do not scale yet. Then write the "what must be true" list: each a testable statement, ordered by how much the verdict would change if it failed.
10. **Stop here.** Hand the assessment to `plan-scale-up-strategy`; the tests go to whoever designs them (`plan-evaluation-design` or `design-pilot-feasibility-study`). See `references/evidence-notes.md` for the sources and `references/worked-example.md` for a complete run on an ART adherence SMS program in Kisumu, Kenya.

## Output template

```markdown
# Scalability assessment: <program name>

**Claim (one line):** <effect with unit> on <outcome>, measured on <population: who, where, N>, delivered by <implementer>, at <cost per unit>
**Scale-up on the table:** <from N to N, delivered by whom, through what system, with these changes to the delivered version>
**Decision this informs:** <go or no-go / staged roll-out / budget line / handover>; reversible: <yes / no>

## Threats to the effect

| Threat | Evidence for the threat (from the pilot) | Evidence against it | Test that would settle it (cost, time) |
|---|---|---|---|
| False positive | <pre-registration, sample size, single estimate or one of many, second study> | <...> | <...> |
| Population | <who was in the pilot versus who is reached at scale; subgroup results> | <...> | <...> |
| Situation and implementer | <who delivered; selection, training, supervision, pay; what changes at scale> | <...> | <...> |
| Spillovers | <what changes when most people in an area are treated> | <...> | <...> |
| Cost at scale | <which cost lines fall, rise, or disappear> | <...> | <...> |

## Domain scores (generic set for this library; confirm against the ISAT)

| Domain | Score (1–5) | Evidence behind the score |
|---|---|---|
| Strength of the effect evidence | <...> | <...> |
| Fit with the scale population | <...> | <...> |
| Implementer capacity at scale | <...> | <...> |
| Delivery system readiness | <...> | <...> |
| Cost and financing at scale | <...> | <...> |
| Risk of harm or backfire at scale | <...> | <...> |

## Verdict
<scale / scale after these tests / do not scale yet>, because <the threats that drive it>.

## What must be true for the effect to survive
1. <testable statement>; test: <...>; would change the verdict if it failed: <yes / no>
2. <...>

## What to check before relying on this
- <the "no pilot evidence either way" cells, and which one matters most>
- <the field in the claim line most likely to be wrong>
```

## Where it goes wrong

- **Carrying the pilot number to scale.** The pilot estimate is the upper bound of what scale will show, not the forecast. If the output quotes the pilot effect as the expected effect at scale without the false-positive and implementer discounts, it has not done the job.
- **Treating the implementer as a detail.** "Same program, delivered by the ministry" is a different program until the selection, supervision, and pay of the people delivering it are shown to match. The Kenya contrast exists because this was assumed.
- **Scoring from enthusiasm.** A domain score with an empty evidence cell is a vote, not an assessment. Leave the score blank and write "no evidence" rather than fill it.
- **Confusing scalable with cheap.** A program can be cheap to copy and still lose its effect, because what made it work (a trusted messenger, a small caseload) does not copy. Cost is one threat of five.
- **Running on a program with no evaluation.** If there is no measured effect, there is nothing to assess; send the user to `plan-evaluation-design` rather than scoring a hope.
- **Writing the scale-up plan.** Who delivers, in what order, with what budget is `plan-scale-up-strategy`. This skill stops at the verdict and the list of what must be true.

## When to bring in a specialist

Tell the user to consult an economist or implementation scientist with scale-up experience, together with the government partner's own planning staff, when:
- Delivery moves from an NGO or research team to a government or a large contractor, or the implementer changes in any other way; the test that settles the implementer threat is usually a trial under the new implementer, which needs designing
- The decision is irreversible (a national policy, a law, a procurement, or a handover the organization cannot take back), because the cost of a wrong "scale" verdict is then borne by people who were not in the pilot
- Spillovers could move prices, wages, or queues for untreated people; those effects need a design that treats whole areas, which is a specialist's job
- The population at scale includes groups the pilot excluded (younger, poorer, a different language), and the pilot's subgroup results are too thin to say anything

Bring them: the one-line claim, the threats table with its tests, the domain scores with their evidence, and the pilot's evaluation design and intervention description.
