---
name: analyze-heterogeneous-effects
description: >-
  Use when a trial or evaluation has its main result and someone asks "who
  did it work for", "did it work better for women, poorer households, or low
  performers", or "which subgroups benefited". Also use when a team is about
  to report a subgroup difference it never planned to test as if it were a
  finding, or wants to use machine learning to find who responds. Separates
  the moderators the pre-analysis plan named from exploratory splits, runs
  both with sample splitting, reports effects in the outcome's own units, and
  says what to pre-register next time (Bryan, Tipton and Yeager; Wager and
  Athey; Chernozhukov et al.). Do not use to correct the p-values across the
  subgroup tests; use adjust-for-multiple-comparisons instead. Not for
  judging whether a published effect transfers to your setting before you
  test (assess-evidence-transferability) or whether a pilot effect survives
  scale-up (assess-scalability).
license: CC-BY-4.0
metadata:
  title: Find out who benefited most from a program
  type: atomic
  stage: analyze
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: not-applicable
  tags: "heterogeneity, quantitative, experimental-design"
  consumes: "analysis-plan, dataset-description"
  produces: ""
---

## What it does

Estimates who benefited most from an intervention, keeping the moderator tests the pre-analysis plan named apart from exploratory machine-learning splits so that neither is mistaken for the other.

A pre-specified moderator is a baseline characteristic the pre-analysis plan named, before outcome data were seen, as one along which the effect was expected to differ. Everything else is exploration. The confirmatory part tests those moderators as interactions; the exploratory part lets a flexible model search for who responds, with sample splitting so the same data do not both find a pattern and confirm it. The output reports both, in the outcome's units, with the power limits stated and a list of what to pre-register next time. It does not produce a targeting rule.

## When to use it

### Use it when
- A trial or evaluation has an overall effect estimate and the team, a funder, or a reviewer asks "who did it work for?" or "did it work better for some people than others?"
- The pre-analysis plan named moderators (sex, baseline level, distance to the clinic, phone ownership) and they now need to be tested as the plan said
- Someone proposes "let's see if it worked for women" or "the main effect was null, let's check the subgroups" after seeing the results, and the finding needs its exploratory label attached before it travels
- The team wants to use a causal forest or another machine-learning method to find who responds, and needs the version with sample splitting and the three standard outputs
- The next trial is being planned and the question is which moderators to pre-register

### Do not use it when
- The question is whether a published effect from somewhere else applies to your population before you have tested it; that is `assess-evidence-transferability`
- The question is whether an effect found in a pilot will hold when a different population or implementer runs it at scale; `assess-scalability`
- The moderators are still being chosen before the trial; `write-pre-analysis-plan` is where they get named
- The subgroup tests exist and the task is to correct their p-values as a family; `adjust-for-multiple-comparisons`, which this skill hands them to
- The team wants posterior distributions for subgroup effects or hierarchical shrinkage across subgroups; that is a Bayesian analysis, a different procedure from the frequentist one here, so ask for one directly

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The pre-analysis plan, or the analysis section of the evaluation design: the primary outcome, the pre-specified model, and the moderators it names with their expected direction. If no plan exists, say so; everything in the run is then exploratory, and the report says so at the top.
2. **Required.** A dataset description: arms, randomization unit, sample size per arm, baseline covariates available, the outcome's units, and how the sample was drawn (a probability sample of a named population, or whoever could be reached).
3. **Required.** The decision the result will inform: describe who benefited, choose what to pre-register next, or decide who gets the program next time. The third is the escalation case below.
4. Optional. The overall effect estimate if already computed, and the software in use (R, Stata, Python), so the skill can name the package rather than describe the algorithm.

If 1 is missing, ask once; if there is no plan, proceed with every result marked exploratory. If 2 is missing, ask and stop; without the randomization unit and the sampling frame the estimates cannot be interpreted. If 3 is missing, assume description. If 4 is missing, compute the overall effect first and describe the method in general terms.

## What it draws on

- Bryan, C. J., Tipton, E., & Yeager, D. S. (2021). Behavioural science is unlikely to change the world without a heterogeneity revolution. *Nature Human Behaviour*, 5(8), 980–989. https://doi.org/10.1038/s41562-021-01143-3
- Wager, S., & Athey, S. (2018). Estimation and inference of heterogeneous treatment effects using random forests. *Journal of the American Statistical Association*, 113(523), 1228–1242. https://doi.org/10.1080/01621459.2017.1319839
- Chernozhukov, V., Demirer, M., Duflo, E., & Fernández-Val, I. (2025). Fisher–Schultz Lecture: Generic machine learning inference on heterogeneous treatment effects in randomized experiments, with an application to immunization in India. *Econometrica*, 93, 1121–1164. https://doi.org/10.3982/ECTA19303
- EGAP. *10 Things to Know About Heterogeneous Treatment Effects*. https://egap.org/resource/10-things-to-know-about-heterogeneous-treatment-effects/ (listing confirmed; the guide itself was not opened for the evidence dossier)

Bryan, Tipton, and Yeager argue that effects should be expected to vary, that haphazard convenience samples cannot say for whom, and that trials should use probability samples with moderators measured and pre-specified. Wager and Athey's causal forest is a flexible estimator of the effect for each unit from its covariates, with valid confidence intervals under sample splitting (each tree is grown on one subsample and estimates on another). Chernozhukov, Demirer, Duflo, and Fernández-Val give the generic approach this skill's exploratory section follows: fit any machine-learning model of the effect on one random half, then on the other half estimate three things. The best linear predictor (BLP) is a regression of the outcome on the predicted effects that reports a heterogeneity coefficient, near 1 when the predictions track real differences and near 0 when they track noise. Group average treatment effects (GATES) are the average effects within quantiles of predicted impact, from the group predicted to benefit least to the one predicted to benefit most. The characteristics of the most and least affected (CLAN) are the average baseline covariates of those two groups, side by side. The judgment calls this skill adds: it refuses to let an exploratory split change label; it reports in the outcome's units, not only standard deviations; and it treats a null interaction as "not detectable at this sample", not "no difference". See `references/evidence-notes.md` for the dossier's verification state of each source.

**WEIRD skew:** Not applicable in the usual sense, because the procedure is statistical. What is population-bound is the inference: a heterogeneity estimate describes the sample it was computed on, so a convenience sample cannot say who benefits in the population the program serves, which is the heterogeneity argument's own point about sampling. **Non-WEIRD evidence:** Chernozhukov et al. apply the generic machine-learning method to immunization nudges in Haryana, India, and to microcredit; the evidence dossier records no effect sizes from either application, so none are quoted here.

**Replication status:** Not applicable in the effect sense: causal forests and generic machine-learning inference are estimation methods with proofs rather than effects that replicate or fail to. The relevant status is that machine-learning heterogeneity is exploratory unless pre-specified, and subgroup tests have low power, which is why the output labels every exploratory result a hypothesis for the next trial.

## How to do it

1. **Copy the plan's moderators verbatim** into the confirmatory table with their expected direction, and list everything else the team wants to look at under exploratory. Do not move anything across that line later, whatever it shows.
2. **State the overall effect first,** in the outcome's units with its confidence interval, from the pre-specified model with standard errors clustered at the randomization unit. Every subgroup result is read against it.
3. **Test each pre-specified moderator as a treatment-by-moderator interaction** in that same model. Report the interaction and the effect at each level of the moderator, in outcome units. Hand the set of interaction p-values to `adjust-for-multiple-comparisons` as one family, and show adjusted and unadjusted side by side.
4. **For exploration, split the sample at random** into a fitting half and a testing half. Fit a causal forest or any flexible model of the effect on the fitting half using baseline covariates only. On the testing half compute the BLP, the GATES by predicted-impact quantile, and the CLAN. Repeat the split several times and report the median across splits, so one lucky split does not carry the result. In R, grf (causal forest) or GenericML; in Python, econml. See `references/worked-example.md` for a complete run.
5. **Report effects in the outcome's units** (percentage points, score points, shillings) with intervals; add standardized units only as a second line when comparison across outcomes is needed.
6. **State the power limits.** The sample was powered for the main effect; an interaction of the same size needs a much larger sample, so a null interaction is "not detectable here", not "no difference". Say which moderators the plan powered for, if any.
7. **Label every exploratory result a hypothesis** for the next trial, then write what to pre-register: the moderator, the expected direction, and the sample it would take to test it.
8. **Stop here.** Do not turn a subgroup result into a rule for who gets the program; that is the escalation case. Whether the effect survives a different population is `assess-scalability`.

## Output template

```markdown
# Heterogeneous effects report

**Trial:** <name; arms; randomization unit; sample per arm>
**Primary outcome:** <outcome, in its units>
**Overall effect:** <estimate in outcome units (95% CI), pre-specified model>
**Sample:** <probability sample of <population> / convenience sample of <who was reached>>; <who the results can speak for>
**Decision this informs:** <describe / pre-register next / target (escalated)>
**Plan status:** <pre-analysis plan dated <date> names <n> moderators / no plan: everything below is exploratory>

## Pre-specified moderators (confirmatory)
| Moderator (verbatim from the plan) | Expected direction | Effect at each level (units, 95% CI) | Interaction (units, 95% CI) | Unadjusted p | Adjusted p (family: <name>, m = <n>) |
|---|---|---|---|---|---|
| <moderator> | <...> | <level A: ...; level B: ...> | <...> | <...> | <...> |

<one or two sentences: which interactions hold after adjustment, which do not, and the direction>

## Exploratory machine-learning splits (hypothesis-generating)
- **Method and software:** <causal forest / generic ML; package>
- **Sample splitting:** <share fit / share test; number of repeated splits; medians reported>
- **Covariates used:** <baseline only; list>
- **Best linear predictor:** heterogeneity coefficient <estimate (95% CI)>; <reads as: real heterogeneity detected / not distinguishable from noise>
- **Group average effects by predicted-impact quantile:**
  | Group | Effect (units, 95% CI) |
  |---|---|
  | Least affected <fifth> | <...> |
  | <middle groups> | <...> |
  | Most affected <fifth> | <...> |
  | Most minus least | <...> |
- **Characteristics of the most and least affected:** <covariate: mean in most affected, mean in least affected, difference; three to six rows>

## Power limits
<what the sample was powered for; why a null interaction here means "not detectable", not "no difference"; which moderators, if any, the plan powered for>

## What to pre-register next time
- <moderator>, expected <direction>, because <reason from this run>; sample needed <from estimate-sample-size, or "to be calculated">

## What to check before relying on this
- <the sampling assumption: who this sample can speak for>
- <that every exploratory result still carries its label where the report will be read>
- <that no targeting or exclusion rule has been drawn from this report>
```

## Where it goes wrong

- **A subgroup found after the fact reported as a finding.** "It worked for women" from a split the plan never named is a hypothesis. The report keeps the exploratory label attached to it in every sentence, including the summary a funder will read.
- **Fitting and testing on the same data.** A flexible model will always find heterogeneity in the data it was fit on. Without sample splitting the BLP coefficient is meaningless; the skill refuses to report the three outputs from an unsplit sample.
- **Fishing after a null main effect.** "The overall effect was null, so let's check the subgroups" is the classic route to a false positive. Heterogeneity analysis after a null is legitimate only for the pre-specified moderators, with the adjustment, and with the exploration labeled as such.
- **Reading a null interaction as "no difference".** Subgroup tests are underpowered relative to the main effect. The power limits section exists so that "not detectable at this sample" is never shortened to "the same for everyone".
- **Standard deviations as the only unit.** An effect of 0.1 SD among low performers tells a program officer nothing; the same result as score points or percentage points does. Units first, SD second.
- **A convenience sample speaking for a population.** If the sample is whoever could be reached, the CLAN describes who among those reached responded, not who in the district would. The report says which, in the sample line, every time.

## When to bring in a specialist

Tell the user to consult a statistician or econometrician with trial experience when:
- A subgroup result would be used to target the program to some people or exclude others; that decision needs a confirmatory test in a sample powered for it, a fairness review of who is excluded, and often a legal one
- The randomization unit is a cluster and there are few clusters, since interaction estimates with clustered errors become unreliable well before the main effect does
- The pre-analysis plan is missing or names no moderators and the heterogeneity result will feed a funding decision
- The machine-learning outputs disagree across splits, or the BLP heterogeneity coefficient is far from both 0 and 1, and the team wants to act on them anyway

Bring them: the pre-analysis plan, the dataset description, the overall effect, the moderator table with adjusted and unadjusted p-values, and the three machine-learning outputs with the number of splits.
