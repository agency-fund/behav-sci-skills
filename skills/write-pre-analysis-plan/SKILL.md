---
name: write-pre-analysis-plan
description: >-
  Use when an evaluation design or measurement plan exists and the team
  needs to write down, before any outcome data exist, exactly how the
  results will be analyzed: one primary outcome, the estimator, the
  families of secondary outcomes, the subgroups, and the decision rules.
  Also use when someone says "pre-analysis plan", "PAP", "pre-register
  the analysis", "the AEA registry wants our analysis plan", or asks how
  much to pre-specify. Produces an analysis plan at the AEA RCT
  Registry's level of detail, following Olken (2015), Coffman and
  Niederle (2015), and Banerjee et al. (2020) on how much to fix in
  advance. Do not use when the primary outcome, comparison condition,
  and smallest effect worth detecting have not been chosen; run
  plan-evaluation-design first. Not for configuring the experiment
  itself (design-evidential-experiment), for the mechanics of the
  multiple-testing correction (adjust-for-multiple-comparisons), or for
  running the subgroup analysis (analyze-heterogeneous-effects).
license: CC-BY-4.0
metadata:
  title: Write the analysis plan before the data arrive
  type: atomic
  stage: test
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: not-applicable
  tags: "research-transparency, experimental-design, multiple-comparisons"
  consumes: "evaluation-design, measurement-plan"
  produces: "analysis-plan"
---

## What it does

Writes the analysis side of a pre-registration: one primary outcome, the estimator, the families of secondary outcomes, the subgroups with a reason each, the decision rules, all fixed before any outcome data are seen.

A pre-analysis plan (PAP) is a dated document that says how a trial's data will be analyzed before the outcome data exist, so the analysis cannot be chosen after seeing which number moved. This skill takes a design that already exists and writes the plan at the level of detail the AEA RCT Registry asks for, concentrating detail where it matters (subgroups, parties with a stake in the result) and leaving the rest flexible with a commitment to report deviations.

## When to use it

### Use it when
- A measurement plan or evaluation design brief exists, the trial is about to launch, and nobody has written down how the results will be analyzed
- Someone asks "what goes in a pre-analysis plan?", "how much do we need to pre-specify?", or "the AEA registry wants an analysis plan, what do we upload?"
- A team is proposing subgroups before the data exist ("we should also look at women", "the poorest quintile") and wants to commit now rather than argue later
- The implementer, funder, or a ministry has a stake in the result and the analysis needs to be fixed where that stake is strongest

### Do not use it when
- The primary outcome, comparison condition, or smallest effect worth detecting is still open; run `plan-evaluation-design` first, or `choose-trial-design` if the trial's structure is the question
- The team is configuring a rapid experiment in Evidential; `design-evidential-experiment` carries its own analysis-plan field, and this skill's output feeds it
- The data are in and the question is which correction to apply or how to estimate subgroup effects; `adjust-for-multiple-comparisons` and `analyze-heterogeneous-effects` execute what the plan says
- Outcome data by arm have already been seen; see the specialist section, because a plan written now is not a pre-analysis plan

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The design: the evaluation design brief from `plan-evaluation-design` or the trial design from `choose-trial-design`, with the primary outcome, comparison condition, unit of randomization, strata, smallest effect worth detecting, and timing. If any of these is missing, send it back; this skill does not choose them.
2. **Required.** Whether anyone has seen outcome data by arm: endline, midline, or an interim dashboard. Baseline data are fine. If the answer is yes, stop and go to the specialist section.
3. **Required.** The secondary outcomes the team cares about, and every subgroup anyone has proposed, each with the reason it was proposed.
4. **Required.** Who has a stake in the result (implementer, funder, ministry, the team's own prior) and what each would want it to show. This decides where the plan is detailed.
5. Optional. The registry (AEA RCT Registry, OSF, a trial registry) and its deadline.
6. Optional. A description of the baseline data: the variables available for covariate adjustment and stratification, and the cluster identifiers.

If 1 or 2 is missing, ask and stop. If 3 is missing, write a primary-only plan and say the secondary families are empty. If 4 is missing, assume the implementer has the strongest stake and say so. If 5 or 6 is missing, default to the AEA registry's fields and to intention-to-treat with strata only.

## What it draws on

- Olken, B. A. (2015). Promises and perils of pre-analysis plans. *Journal of Economic Perspectives*, 29(3), 61–80. https://doi.org/10.1257/jep.29.3.61
- Coffman, L. C., & Niederle, M. (2015). Pre-analysis plans have limited upside, especially where replications are feasible. *Journal of Economic Perspectives*, 29(3), 81–98. https://doi.org/10.1257/jep.29.3.81
- Banerjee, A., et al. (2020). In praise of moderation: Suggestions for the scope and use of pre-analysis plans for RCTs in economics. NBER Working Paper 26993. https://doi.org/10.3386/w26993
- AEA RCT Registry. https://www.socialscienceregistry.org/
- Office of Evaluation Sciences (2021). *Analysis plan* template, July 2021. https://oes.gsa.gov/assets/files/AnalysisPlan.pdf
- J-PAL. *Pre-analysis plans*. https://www.povertyactionlab.org/resource/pre-analysis-plans
- EGAP. *10 things to know about pre-analysis plans*. https://egap.org/resource/10-things-to-know-about-pre-analysis-plans/

Olken sets out the promise of pre-analysis plans (an analysis that cannot be chosen after seeing the data, which matters most where someone has a stake in the result) and the perils (rigidity, cost, lost learning from the data). Coffman and Niederle argue the upside is limited, especially where replications are feasible. Banerjee et al. argue for moderation: pre-specify what matters, keep the rest flexible, and report deviations. J-PAL's guidance says a PAP "should be concise and focused, rather than attempt to be exhaustive" and treats the populated PAP, the plan filled in afterward with results and deviations, as a separate document. The OES template, in contrast, pre-specifies a full plan (hypotheses, data structure, outcomes, transformations, exclusions, missing data, models and tests) "finalized and date-stamped before we take possession of outcome data". This skill takes the moderate position as the default and the OES position where stakes are high: detail goes where there are vested interests or subgroups, the rest is flexible and declared so, and a populated PAP follows. One judgment call is this skill's own: the plan carries written decision rules (what the team will do with each result), which none of the sources require but which make the plan usable by a program, not only by a journal.

**WEIRD skew:** Not applicable to the method, which is procedural. The practice comes out of development-economics RCTs (Olken; Banerjee et al.) and a US government evaluation office (OES). What a user elsewhere should check locally: whether the registry is reachable and its timing fits local ethics approval, whether the data structure the plan assumes (cluster identifiers, baseline variables, consistent ids across rounds) actually exists, and who controls the outcome data before registration. **Non-WEIRD evidence:** none found in the sources this skill draws on as a study of pre-analysis plans; the practice's origin in LMIC field trials is a provenance note, not evidence of effect.

**Replication status:** Contested on the level of detail (Coffman and Niederle: limited upside; Banerjee et al.: moderation; OES: full pre-specification, date-stamped); uncontested that whatever is pre-specified must be written before outcome data are seen.

## How to do it

1. **Carry over the design verbatim**: primary outcome, comparison, unit of randomization, strata, smallest effect worth detecting, timing. Do not re-decide any of them; if one is missing, send the user back to `plan-evaluation-design`.
2. **Write the primary hypothesis in one sentence**, with its direction, then the one primary outcome with its exact construction: variable, transformation, measurement window, missing-data rule. One primary outcome, because several primaries re-import the which-number-moved problem.
3. **Group the secondary outcomes into families** by construct (for example savings behavior; health visits; knowledge). Name per family whether an index will be built or a correction applied, and hand the mechanics to `adjust-for-multiple-comparisons`. Everything outside the families is exploratory and labeled so.
4. **Specify the estimator.** Intention-to-treat (ITT: compare people by the arm they were assigned, whether or not they took it up), with covariates named now (baseline outcome, strata), and inference that matches the unit of randomization (cluster-robust standard errors, which allow outcomes within a randomized cluster to be correlated, when clusters were randomized). State the attrition rule and the check for differential attrition between arms.
5. **Pre-specify subgroups**, each with a theory-based reason the effect should differ, the variable and cut defined now, and its status (confirmatory or exploratory). Keep the list short; hand execution to `analyze-heterogeneous-effects`.
6. **Write the decision rules**: for the primary outcome above the threshold, around it, and null or negative, what the team will do, who decides, and which guardrail results would override a positive primary.
7. **Calibrate the detail.** Moderate by default (Banerjee et al.). Add detail where a party has a stake in the result or where a subgroup invites fishing. Say what is left flexible and commit to a populated PAP that lists deviations.
8. **Register it.** Fill the registry fields, date-stamp the plan, attach it, record the registry id, and name who holds the outcome data until registration is confirmed.
9. **Stop here.** The plan goes to the registry; `adjust-for-multiple-comparisons` and `analyze-heterogeneous-effects` execute it when the data arrive.

See `references/worked-example.md` for a complete run on tax-compliance letters in Guatemala, and `references/evidence-notes.md` for the sources with their verification state.

## Output template

```markdown
# Pre-analysis plan

**Trial:** <name>
**Registry:** <AEA RCT Registry / OSF / other; id when available>
**Date-stamped:** <date>, before any outcome data by arm were seen
**Design carried over from:** <plan-evaluation-design brief or choose-trial-design output, dated>

## 1. Hypothesis
<primary hypothesis in one sentence, direction stated>

## 2. Design (carried over, not re-decided)
<unit of randomization; arms; strata; comparison condition; sample; timing of outcome collection>

## 3. Primary outcome
<variable, construction, measurement window, missing-data rule; the smallest effect worth detecting, carried over with its source>

## 4. Secondary outcome families
| Family | Outcomes | Index or correction (mechanics in adjust-for-multiple-comparisons) | Why this family |
|---|---|---|---|

## 5. Estimator and inference
<ITT by assigned arm; covariates named now; cluster-robust or individual standard errors matching the randomization unit; attrition rule and differential-attrition check; exclusion rules>

## 6. Pre-specified subgroups
| Subgroup | Variable and cut | Theory-based reason | Status (confirmatory / exploratory) |
|---|---|---|---|

## 7. Decision rules
| Primary result | What the team will do | Who decides | Guardrail results that would override |
|---|---|---|---|
| Above threshold | | | |
| Around threshold | | | |
| Null or negative | | | |

## 8. Where this plan is detailed, where it is flexible
<the vested interests and subgroup risks that drove extra detail; what is left open and why; commitment to a populated PAP listing deviations>

## 9. Registration
<registry fields filled; date; attachment; who holds the outcome data until registration is confirmed>

## Open questions
- <the assumption most likely to be wrong>
```

## Where it goes wrong

- **Writing it after a peek.** A plan drafted after anyone has seen outcomes by arm, even a dashboard glance, is not a pre-analysis plan. Ask question 2 directly; if the answer is yes, stop and escalate rather than date-stamping a document the data already shaped.
- **Several primary outcomes.** Listing three "primary" outcomes so one is bound to move. One primary; the rest in families.
- **Subgroups without a reason.** A subgroup listed because the variable exists, not because theory says the effect should differ there, is a fishing license. Each subgroup carries its reason or is dropped.
- **Re-deciding the design.** Drifting into choosing the primary outcome or the smallest effect worth detecting. That is `plan-evaluation-design`'s job; this skill carries its answers over.
- **Over-specifying everything.** A plan that fixes every transformation of every outcome is the rigidity Olken and Banerjee et al. warn about; detail goes where the stakes are, and the rest is declared flexible.
- **No decision rule.** A plan that says how the number will be computed but not what anyone will do with it leaves the program's decision to be made after the result, which is where the pressure is.

## When to bring in a specialist

Tell the user to consult a statistician or evaluation methodologist, and where relevant an independent evaluator, when:
- Any outcome data by arm have been seen; the honest options (an exploratory label, a dated populated plan, a plan for only the outcomes not yet seen) need a methodologist's judgment, and the registry entry must say what was seen
- The design is clustered, stepped-wedge, or adaptive, so the estimator and standard errors are not the textbook ITT case
- A party with a stake in the result wants to change the plan before registration; an independent evaluator should hold the plan
- The primary outcome is high-stakes (eligibility for benefits, health) and a wrong decision rule would be acted on

Bring them: the design brief, the draft plan with its decision rules, and the description of the data structure.
