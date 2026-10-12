---
name: estimate-expected-effect
description: >-
  Use when a team needs the effect size to plan a test around and the
  numbers in hand come from published studies: "the paper found 12 points,
  what should we expect?", "what effect size goes in the power calculation?",
  "is d = 0.45 realistic for our SMS program?". Also use when a proposal or
  power calculation carries a published or meta-analytic effect unchanged, or
  when a team needs the smallest effect its decision would act on. Discounts
  published estimates for publication bias, lab-to-field shrinkage,
  and the academic-versus-practitioner gap (Maier et al. 2022; Ferraro and
  Tracy 2022; DellaVigna and Linos 2022), keeps the expected effect separate
  from the smallest effect worth detecting, and returns a planning range in
  the outcome's units and in standard deviations. Do not use to judge
  whether one study fits your setting; run assess-evidence-transferability
  first and bring its verdict here. Not for the sample size
  (estimate-sample-size), and not for finding what evidence exists
  (assess-evidence-base).
license: CC-BY-4.0
metadata:
  title: Set a realistic effect size to plan for
  type: atomic
  stage: test
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: mixed-evidence
  tags: "evidence-synthesis, experimental-design, quantitative"
  consumes: "evidence-scan-brief"
  produces: "effect-size-benchmark"
---

## What it does

Turns the published effect sizes a team is relying on into a discounted planning range for one test.

Published effects are usually larger than the effects the same kinds of interventions produce when a program delivers them: the literature is selectively published, lab effects shrink in the field, and academic trials outperform practitioner trials several times over. This skill applies those discounts in a fixed order, shows the arithmetic, and reports two numbers that are often confused: the effect the team should expect, and the smallest effect its decision would act on. It does not compute a sample size, and it does not judge whether one study transfers; it consumes that judgment.

## When to use it

### Use it when
- Someone asks "what effect size should we plan for?", "what goes in the power calculation?", or "is the number from that paper realistic for us?"
- A proposal, theory of change, or power calculation carries a published or meta-analytic effect size unchanged (Mertens et al.'s d = 0.45, or "the trial found 12 points") as the program's expected effect
- `assess-evidence-transferability` has returned a verdict and a provisional discount range, and the team needs a planning number from it
- An evidence scan brief from `assess-evidence-base` lists several effect sizes and the team must pick one number to design around
- A funder or reviewer asks "what is the smallest effect that would justify this program?" and nobody has separated that from the effect the team hopes for

### Do not use it when
- The question is whether one specific study applies to the user's population; `assess-evidence-transferability` judges fit on five dimensions, and this skill consumes its verdict
- The team needs the sample size or the minimum detectable effect for a fixed sample; `estimate-sample-size` turns this skill's benchmark into those
- Nobody has looked for evidence yet; `assess-evidence-base` finds what exists, with effect sizes where reported
- The team needs the full cost-per-outcome comparison that sets a program's threshold; `estimate-cost-effectiveness` does that arithmetic, and this skill only names the cost inputs it needs
- The primary outcome, comparison condition, and locked threshold are the question; `plan-evaluation-design` writes that plan and consumes this benchmark

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** Every published estimate the team is relying on: citation (or the evidence scan brief entry), the effect with its unit (percentage points, percent change, standard deviations, odds ratio), the outcome measured, the sample size if given, and the source type: lab or online study, academic field trial, nudge-unit or practitioner trial, or meta-analysis, saying whether the meta-analysis reports a bias-corrected figure.
2. **Required.** The outcome the test will measure, its unit, and its baseline: the control-group rate for a binary outcome, the mean and standard deviation for a continuous one, with the source of the baseline. The conversion between percentage points and standard deviations depends on it.
3. **Required.** The decision the test informs: a pilot go or no-go, a scale-up, a policy, a funder report. The decision sets the smallest effect worth detecting and how conservative the range should be.
4. Optional. A transferability verdict from `assess-evidence-transferability`, with its discount range.
5. Optional. The cost per person of the intervention, or a threshold the program or sponsor has already stated (from `plan-evaluation-design` if it exists).

If 1 or 2 is missing, ask and stop. If 3 is missing, ask once; if still unknown, assume a pilot and say so. If 4 is missing, treat the evidence as not yet checked for fit and widen the low end of the range. If 5 is missing, mark the smallest effect worth detecting provisional and hand the cost arithmetic to `estimate-cost-effectiveness`.

## What it draws on

- Mertens, S., Herberz, M., Hahnel, U. J. J., & Brosch, T. (2022). The effectiveness of nudging: A meta-analysis of choice architecture interventions across behavioral domains. *Proceedings of the National Academy of Sciences*, 119(1). https://doi.org/10.1073/pnas.2107346118
- Maier, M., Bartoš, F., Stanley, T. D., Shanks, D. R., Harris, A. J. L., & Wagenmakers, E.-J. (2022). No evidence for nudging after adjusting for publication bias. *Proceedings of the National Academy of Sciences*. https://doi.org/10.1073/pnas.2200300119
- Szaszi, B., et al. (2022). No reason to expect large and consistent effects of nudge interventions. *Proceedings of the National Academy of Sciences* (letter). https://doi.org/10.1073/pnas.2200732119
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709
- Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity: A meta-analysis and a real-effort experiment. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x
- Hummel, D., & Maedche, A. (2019). How effective is nudging? A quantitative review on the effect sizes and limits of empirical nudging studies. *Journal of Behavioral and Experimental Economics*, 80, 47–58. https://doi.org/10.1016/j.socec.2019.03.005
- Milkman, K. L., et al. (2021). Megastudies improve the impact of applied behavioural science. *Nature*, 600, 478–483. https://doi.org/10.1038/s41586-021-04128-4
- Bryan, C. J., Tipton, E., & Yeager, D. S. (2021). Behavioural science is unlikely to change the world without a heterogeneity revolution. *Nature Human Behaviour*, 5(8), 980–989. https://doi.org/10.1038/s41562-021-01143-3
- Kraft, M. A. (2020). Interpreting effect sizes of education interventions. *Educational Researcher*, 49, 241–253. https://doi.org/10.3102/0013189X20912798
- Brandon, A., et al. (2017). Do the effects of nudges persist? Theory and evidence from 38 natural field experiments. NBER Working Paper 23277 (revised 2022). https://doi.org/10.3386/w23277
- J-PAL. *Power calculations*. https://www.povertyactionlab.org/resource/power-calculations

Three gaps between published and delivered effects are documented. Publication bias: Mertens et al. pool more than 200 studies (more than 450 effect sizes, N ≈ 2.15 million) into d = 0.45 (95% CI 0.39–0.52) with moderate publication bias; Maier et al.'s bias-corrected re-analysis of the same literature gives about d = 0.04, and Szaszi et al. (2022) put the bias-adjusted range at d ≈ 0.03–0.31 and call the average misleading given heterogeneity. Lab-to-field: Ferraro and Tracy's loss-framed contracts pool to 0.16 SD, but 0.33 SD in the lab against 0.02 SD in the field. Academic-to-practitioner: across 126 RCTs and 23 million people, DellaVigna and Linos find academic journal studies average 8.7 percentage points (+33.4%) while nudge-unit trials average 1.4 points (+8.0%), with about 70% of the gap explained by selective publication combined with low power. Milkman et al.'s megastudy (61,293 people, 54 interventions) adds two cautions: only 8% of interventions produced effects that persisted after the program, and expert forecasts failed. Bryan, Tipton and Yeager argue that effects should be expected to vary across people and settings. Kraft supplies benchmarks for interpreting education effects, from US education RCTs; Hummel and Maedche (100 publications, 317 effect sizes) and Brandon et al. (persistence) are context. J-PAL's power-calculation guidance notes that effect sizes are usually set too optimistically. The judgment calls this skill adds, none of them published rules: the fixed order of discounts; the rule that a planning range never exceeds the best field evidence of the same source type; the two-number rule separating the expected effect from the smallest effect worth detecting; and the refusal to use Cohen's small-medium-large labels, which the dossier marks as not a planning benchmark.

**WEIRD skew:** Every quantitative source is from high-income settings: Mertens, Maier and Szaszi pool a mostly Western literature; DellaVigna and Linos cover two US nudge units; Milkman et al. is a US gym; Kraft's benchmarks are US education RCTs. A user elsewhere should treat the discounts as the floor on how much to shrink a published number, not as a calibrated estimate for their setting, and should look for field trials in a comparable setting before fixing the central value. **Non-WEIRD evidence:** none found in the sources this skill draws on; the per-domain LMIC benchmarks the plan asked for are not in the dossier and are left for the author to add.

**Replication status:** Mixed. The shrinkage itself is replicated across three independent comparisons (Mertens against Maier; lab against field in Ferraro and Tracy; academic against nudge-unit in DellaVigna and Linos), so discounting is not in dispute. The size of the discount is: the Mertens versus Maier average is contested, and critics note the average hides heterogeneity by domain and intervention type.

## How to do it

1. **Tabulate every estimate** with its source type, effect, unit, outcome, sample size, and whether it is already bias-corrected. A single uncorrected headline is the input most runs start with; say so in the table rather than treating it as settled.
2. **Convert each estimate to the test's outcome unit** and show the arithmetic. For a binary outcome the standard deviation is sqrt(p(1 − p)) at the baseline rate p, so a change of x percentage points is x / (100 × sqrt(p(1 − p))) SD; an odds ratio needs the baseline rate to become percentage points. Do not mix percentage points with percent change: 8.7 points was +33.4% in DellaVigna and Linos.
3. **Discount 1, publication bias.** If the figure is an uncorrected meta-analytic or journal average, replace it with the bias-corrected figure where the meta-analysis gives one (for choice architecture, d = 0.45 becomes about 0.04, within a range of 0.03–0.31). Where none exists, keep the published figure as the top of the range only.
4. **Discount 2, lab-to-field.** If the source is a lab or online study, do not carry its size at all; it is evidence of direction. Say why: 0.33 SD in the lab became 0.02 SD in the field for loss framing.
5. **Discount 3, academic-to-practitioner.** If the source is an academic field trial and the user is a program delivering at scale, state the reference gap (8.7 against 1.4 points, a ratio of about six in that sample), use it to set the low end of the range, and do not apply it as a universal constant. If the source is already a nudge-unit or practitioner trial, skip this step; discounting it again is the most common double count.
6. **Adjust for fit.** If an `assess-evidence-transferability` verdict exists, apply its discount range here and name the untested differences it listed. If none exists, say the fit has not been checked and widen the low end.
7. **Note persistence.** If the decision depends on the effect lasting beyond the program, say that only 8% of the 54 megastudy interventions persisted, plan for the during-program effect, and name persistence as unmeasured.
8. **Write the expected-effect range**: low, central, high, each in the outcome's units and in SD, each naming the discount that produced it. A range is the output; a point estimate is a guess dressed up.
9. **State the smallest effect worth detecting separately.** It comes from the decision and the cost, not from the literature: the effect at which the program would act (scale, continue, drop). Carry over a locked threshold from `plan-evaluation-design` if one exists; otherwise give a provisional figure and name the cost inputs `estimate-cost-effectiveness` needs to firm it up.
10. **Name the number to hand on.** Give `estimate-sample-size` the smaller of the central expected effect and the smallest effect worth detecting, and say which it is. If the whole expected range sits below the smallest effect worth detecting, say plainly that the test as conceived is unlikely to find an effect the program would act on, and that the decision is whether to run it at all.
11. **Stop here.** `estimate-sample-size` turns the benchmark into a sample; `plan-evaluation-design` locks the threshold.

See `references/evidence-notes.md` for every number and its verification state, and `references/worked-example.md` for a run on SMS reminders for antenatal iron-folate adherence in Malawi.

## Output template

```markdown
# Effect-size benchmark: <intervention> on <outcome>

**Decision this informs:** <pilot / scale-up / policy / funder report>
**Outcome, unit, baseline:** <outcome>; <percentage points or raw unit>; baseline <rate, or mean and SD> from <source>
**Conversion used:** <e.g. SD of a binary outcome at baseline p = sqrt(p(1 − p)) = ...>

## Published estimates the team is relying on
| Source | Source type | Reported effect (unit) | In the test's unit | Already bias-corrected? |
|---|---|---|---|---|
| <citation> | <lab / academic field / practitioner / meta-analysis> | <...> | <pp and SD> | <yes / no> |

## Discounts, in order
1. Publication bias: <applied or not, and why> → <figure>
2. Lab-to-field: <applied or not, and why> → <figure>
3. Academic-to-practitioner: <applied or not, and why> → <figure>
4. Fit to this setting: <verdict and range from assess-evidence-transferability, or "not checked; low end widened">
5. Persistence: <relevant to the decision or not; what is assumed>

## Expected effect: planning range
| | Percentage points (or raw unit) | SD | Produced by |
|---|---|---|---|
| Low | <...> | <...> | <discount> |
| Central | <...> | <...> | <discount> |
| High | <...> | <...> | <discount> |

## Smallest effect worth detecting
<figure and unit>; set by <decision and cost, or carried from plan-evaluation-design>; <locked / provisional>; cost inputs still needed: <...>

## Number to hand to estimate-sample-size
<figure>, because <it is the smaller of the central expected effect and the smallest effect worth detecting>. <If the expected range sits below the threshold, say so here.>

## What to check before relying on this
- <the untested fit difference that most changes the central value>
- <the baseline rate or SD, if it came from a guess>
- <whether any field trial in a comparable setting exists that would replace the discounted number>
```

## Where it goes wrong

- **Carrying the headline.** Quoting d = 0.45 (Mertens) or a trial's 12 points as the expected effect without the corrected figure next to it. The output must never show an uncorrected number alone.
- **Cohen's labels.** Calling 0.2 "small" and 0.5 "medium" and planning for "medium". Those labels are not benchmarks for field programs; the dossier says not to apply them, and this skill does not cite Cohen.
- **Discounting twice, or not at all.** A nudge-unit figure is already a practitioner field effect; applying the academic-to-practitioner gap to it again shrinks it to nothing. A lab figure left undiscounted does the opposite.
- **Averaging across domains.** Benchmarks are domain-specific: structure interventions such as defaults outperform description interventions in Mertens et al., and food is the most responsive domain. A pooled average applied to a savings SMS program is a category error.
- **Merging the two numbers.** Powering a test for the hoped-for effect when the decision needs a smaller one, or setting the "smallest effect worth detecting" to whatever makes the sample affordable. The threshold comes from the decision and the cost; the expected effect comes from the evidence; they are reported separately.
- **Unit slips.** Percentage points read as percent change, an odds ratio read as a risk ratio, a lab SD read as a field percentage point. Every conversion is shown in the table.
- **Forecasts as evidence.** The team's or an expert's intuition about the effect is not a source; expert forecasts failed in the megastudy.

## When to bring in a specialist

Tell the user to consult a behavioral scientist or an evaluation methodologist when:
- The decision is a scale-up or a policy and no field evidence exists in a comparable setting; the discounts then rest on high-income benchmarks alone, and a local pilot sized by `estimate-sample-size` is the honest next step
- The low end of the range is at or near zero while the test's budget or the program's exposure is large; whether to run the test at all is a judgment call about the decision, not about the arithmetic
- The outcome is clinical or carries financial risk (medication adherence, HIV testing, money locked in savings), so the smallest effect worth detecting has a harm side that cost arithmetic does not capture
- The meta-analytic evidence the team relies on is itself contested (the Mertens versus Maier dispute is the live example) and the choice of corrected figure changes the verdict

Bring them: the source table with conversions, the discount arithmetic, the range, the smallest effect worth detecting with its rationale, and the decision the test informs.
