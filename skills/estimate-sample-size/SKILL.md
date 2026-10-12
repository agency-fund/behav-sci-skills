---
name: estimate-sample-size
description: >-
  Use when someone asks "how many people do we need?", "how many villages,
  schools, or clinics?", "is 400 enough?", or "what is the smallest effect
  we could detect with the sample we have?", or when a funder wants a power
  calculation. Also use when a trial will randomize groups rather than
  individuals, or when take-up or attrition will be well below 100 percent,
  since each changes the answer by multiples. Computes the sample or
  clusters per arm from a planned effect, alpha, power, variance,
  intracluster correlation, take-up, attrition, and covariates; reports the
  minimum detectable effect for a fixed sample; runs a sensitivity table;
  flags Type S and Type M risk (Bloom 1995; McConnell and Vera-Hernández
  2025; Gelman and Carlin 2014). Ships a script. Do not use to decide what
  effect to plan for; run estimate-expected-effect first. Not for the
  randomization structure (choose-trial-design), the measurement plan
  (plan-evaluation-design), or an Evidential setup
  (design-evidential-experiment).
license: CC-BY-4.0
metadata:
  title: Work out how big the sample must be
  type: atomic
  stage: test
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: not-applicable
  tags: "experimental-design, quantitative"
  consumes: "effect-size-benchmark, evaluation-design"
  produces: "power-calculation"
---

## What it does

Estimates the sample a test needs to detect its planned effect, or the smallest effect a fixed sample can detect.

Power is the probability that a test finds an effect of a given size when that effect is real. The inputs that move the answer most are not alpha and power but the effect planned for, whether randomization is by group, and how many people actually take up the treatment; this skill makes each visible, shows the arithmetic, and says plainly when the feasible sample cannot detect the plausible effect. It reports the minimum detectable effect (MDES: the smallest true effect the design would detect with the stated power) because the sample is usually fixed by budget before anyone asks.

## When to use it

### Use it when
- Someone asks "how many people do we need?", "how many clinics or villages?", "is our sample big enough?", or "what could we detect with 2,000 households?"
- A funder, ethics board, or pre-registration form asks for a power calculation or a minimum detectable effect
- `choose-trial-design` has set a cluster, stepped-wedge, factorial, or encouragement design and the team needs to know what that design costs in sample
- `estimate-expected-effect` has produced a benchmark and the next question is whether the program can afford to test it
- A proposal states a sample size with no stated effect, variance, or intracluster correlation behind it

### Do not use it when
- Nobody has decided what effect to plan for, or the only number is a published headline; `estimate-expected-effect` discounts it into a benchmark first
- The unit of randomization is still open ("people or villages?"); `choose-trial-design` picks it, and the sample depends on it
- The team needs the primary outcome, comparison condition, and data feasibility written down; `plan-evaluation-design` does that and consumes this calculation
- The test will run in Evidential and the question is what to enter in its power fields; `design-evidential-experiment` takes this calculation's inputs
- The outcome will be measured with a list experiment; `design-list-experiment` carries the extra variance that method costs

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The effect to plan for, with its unit: the number `estimate-expected-effect` said to hand over, or a program-stated minimum, and whether it is the expected effect or the smallest effect worth detecting.
2. **Required.** The outcome type and its baseline: for a binary outcome, the control-group rate; for a continuous one, the mean and standard deviation, with where the SD comes from (baseline survey, administrative data, a study in a similar population).
3. **Required.** The unit of randomization from `choose-trial-design` or the evaluation design. If clusters: the number of units measured per cluster, and any estimate of the intracluster correlation (ICC: the share of outcome variance that sits between clusters rather than within them), with its source.
4. **Required.** The feasible sample: how many people or clusters the program can reach and afford, so the output can say whether that sample can detect the plausible effect.
5. Optional. Expected take-up in the treatment arm and any take-up in control; expected attrition between enrollment and outcome measurement; whether a baseline measure or covariates will be collected, and the share of outcome variance they explain (R²).
6. Optional. Alpha and power, if a funder or protocol has fixed them.

If 1, 2, or 3 is missing, ask and stop. If 4 is missing, ask once; if still unknown, compute the required sample and mark the feasibility verdict as not assessed. If 5 is missing, assume full take-up, no attrition, and no covariates, say so, and show in the sensitivity table what each would do. If 6 is missing, use alpha 0.05 two-sided and power 0.80 and label them conventions. If no ICC exists, run the sensitivity table across a range and say that no local ICC exists.

## What it draws on

- Bloom, H. S. (1995). Minimum detectable effects. *Evaluation Review*, 19(5), 547–556. https://doi.org/10.1177/0193841X9501900504
- McConnell, B., & Vera-Hernández, M. (2025). Going beyond simple sample size calculations: A practitioner's guide. *Fiscal Studies*, 46(3), 323–348. https://doi.org/10.1111/1475-5890.70005. Earlier version: IFS Working Paper W15/17. https://doi.org/10.1920/wp.ifs.2015.1517
- Vera Hernández, A., & McConnell, B. (2024). *Sample size calculators (Going beyond simple sample size calculations: a practitioner's guide)*. UCL figshare. https://doi.org/10.5522/04/25373830.v1
- Hedges, L. V., & Hedberg, E. C. (2007). Intraclass correlation values for planning group-randomized trials in education. *Educational Evaluation and Policy Analysis*, 29(1), 60–87. https://doi.org/10.3102/0162373707299706
- Gelman, A., & Carlin, J. (2014). Beyond power calculations. *Perspectives on Psychological Science*, 9(6), 641–651. https://doi.org/10.1177/1745691614551642
- J-PAL. *Power calculations*. https://www.povertyactionlab.org/resource/power-calculations
- EGAP. *10 things to know about statistical power*. https://egap.org/resource/10-things-to-know-about-statistical-power/

Bloom defines the minimum detectable effect: the smallest true effect a design detects with a stated power at a stated alpha, which is the right thing to report when the sample is fixed by budget. McConnell and Vera-Hernández go beyond the textbook formula: clustering, imperfect take-up, attrition, covariate adjustment, and the calculators that go with the guide. Hedges and Hedberg supply reference ICCs, from US school data. Gelman and Carlin show that when power is low, a statistically significant estimate has a real chance of having the wrong sign (Type S error) and will on average overstate the true effect (Type M error), so a "significant" result from an underpowered pilot is a poor guide to the effect. J-PAL's resource covers MDE, ICC, clustered designs, attrition, and take-up and notes that effect sizes in power calculations are usually set too optimistically; EGAP's guide is a listing. The formulas this skill uses are the standard normal approximations, reproduced in `scripts/power_calc.py`: per arm, n = 2(z_α/2 + z_β)² / d² for a continuous outcome in SD units; the two-proportion equivalent for a binary outcome; the design effect 1 + (m − 1)ρ for m units per cluster at ICC ρ; division by the squared take-up difference and by (1 − attrition); multiplication by (1 − R²). The judgment calls this skill adds: the sensitivity table is mandatory, the feasibility verdict is mandatory, and Type S and Type M risk is reported whenever the expected effect is below the design's MDES. Cohen (1988) is not cited: the dossier marks it unverified and not needed, and its small-medium-large labels are not planning benchmarks.

**WEIRD skew:** The arithmetic has no population content, so `weird` is not-applicable. The inputs do: the ICC values most often quoted (Hedges and Hedberg 2007) come from US education data and do not transfer to clinics, villages, or farmer groups elsewhere; a sub-Saharan African education compilation (Kelcey, Shen & Spybrook 2016) is unverified, author to confirm. Estimate the ICC from local baseline or administrative data wherever possible. **Non-WEIRD evidence:** none found in the sources this skill draws on, beyond the dossier's note that the IFS calculators come from LMIC-experienced authors; LMIC ICC compilations are scarce.

**Replication status:** Uncontested method. The formulas are standard and not in dispute; the J-PAL observation that planned effects are usually too optimistic is a practitioner judgment, not a measured rate.

## How to do it

1. **Fill the inputs table** with every value and its source, labeling alpha and power as conventions unless a protocol fixed them. An input with no source is an assumption and is marked as one.
2. **Put the effect in the script's unit.** Binary: control rate p0 and treatment rate p1 = p0 + the planned change. Continuous: d in SD units, or the raw difference with `--sd`. If the benchmark came in SD and the outcome is binary, convert back through sqrt(p0(1 − p0)) and show it.
3. **Compute the individual-level n per arm** with `python scripts/power_calc.py --outcome ...` and paste the command and output. Do not do the arithmetic by hand; the script prints each multiplier, and `--help` lists every flag.
4. **If randomization is by cluster, apply the design effect** 1 + (m − 1)ρ and report clusters per arm. Say in words that at any ρ above zero the number of clusters drives power and adding people per cluster has diminishing returns, because that is the trade-off the program can act on.
5. **Inflate for take-up and attrition, deflate for covariates**, each as a named multiplier: ÷ (take-up difference)², ÷ (1 − attrition), × (1 − R²). An encouragement design with a 30-point take-up difference needs about 1 / 0.3² ≈ 11 times the sample of full compliance; write that kind of sentence out.
6. **If the sample is fixed, compute the MDES** with `--n-per-arm` or `--clusters-per-arm`, in the outcome's unit and in SD, and state it next to the planned effect.
7. **Run the sensitivity table** with `--sensitivity` over ICC and effect (add take-up if it is uncertain), because the single-number answer hides which assumption it rests on.
8. **If the expected effect is below the MDES, report Type S and Type M risk** with `--true-effect`: the power at that effect, the chance a significant result has the wrong sign, and the factor by which a significant estimate would overstate the truth.
9. **Give the verdict.** Required against feasible: "can detect" or "cannot detect the plausible effect", with the options that change it (more clusters rather than bigger clusters, covariates or a baseline measure, a less noisy proximal outcome, a stronger encouragement, a larger sample, or not running the test). Never make the calculation work by raising the effect.
10. **Stop here.** Hand the calculation to `plan-evaluation-design` or `design-evidential-experiment`; if the design itself should change, send it back to `choose-trial-design`.

See `references/evidence-notes.md` for the sources and `references/worked-example.md` for a run on a village-randomized sanitation test in Indonesia.

## Output template

```markdown
# Power calculation: <test>

**Design:** <individual or cluster randomized; arms; allocation>, from <choose-trial-design or the evaluation design>
**Effect planned for:** <value, unit>; <expected effect or smallest effect worth detecting>, from <estimate-expected-effect or program statement>

## Inputs
| Input | Value | Source |
|---|---|---|
| Alpha (two-sided) | <0.05> | <convention / protocol> |
| Power | <0.80> | <convention / protocol> |
| Outcome type, baseline | <binary p0 = ... / continuous mean, SD> | <...> |
| Cluster size m | <...> | <...> |
| ICC | <... or "no local estimate; range used"> | <...> |
| Take-up (treatment, control) | <...> | <...> |
| Attrition | <...> | <...> |
| Covariate R² | <...> | <...> |

## Calculation
- Individual-level n per arm: <formula with numbers> = <n>
- Design effect: 1 + (m − 1)ρ = <...>
- Take-up: ÷ <...>²; attrition: ÷ (1 − <...>); covariates: × (1 − <...>)
- **Required:** <n enrolled per arm>; <clusters per arm × m, if clustered>
- Script: `python scripts/power_calc.py <arguments>`

## Minimum detectable effect for the feasible sample
<feasible sample>: MDES = <value, unit> (<SD>), against a planned effect of <...>

## Sensitivity
| ICC \ effect | <0.5×> | <0.75×> | <1×> | <1.5×> |
|---|---|---|---|---|
| <...> | <clusters or n per arm> | <...> | <...> | <...> |

## Type S and Type M risk (when the expected effect is below the MDES)
Power at the expected effect <...>; P(wrong sign | significant) <...>; exaggeration ratio <...>

## Verdict
<Can / cannot detect the plausible effect with the feasible sample>, because <...>. Options that change it: <...>

## What to check before relying on this
- <the ICC source, or that none exists>
- <the SD or baseline source>
- <the take-up and attrition assumptions>
```

## Where it goes wrong

- **Finding power by inflating the effect.** Raising the planned effect until the affordable sample "works". The effect comes from `estimate-expected-effect`; if the sample cannot detect it, the verdict says so.
- **Counting people instead of clusters.** Four villages per arm with 1,000 households is not a trial of 8,000 people; the design effect at any realistic ICC collapses it, and with few clusters the normal approximation itself is optimistic.
- **Borrowed ICCs.** US school ICCs pasted into a clinic or village trial elsewhere. Without a local estimate the honest output is a sensitivity table, not a single number.
- **Ignoring take-up.** An encouragement or opt-in design with modest take-up needs a sample several times larger; the squared take-up difference is the multiplier most often left out.
- **Reporting N without MDES.** A sample size with no stated effect behind it cannot be checked; the MDES line is mandatory even when the required sample is affordable.
- **Rare outcomes.** A binary outcome near 0 or 100 percent breaks the normal approximation; the script will return a number, and it should not be trusted.
- **Reading "powered" as "will find it".** Power 0.80 means one test in five misses a real effect of the planned size, and a significant result from an underpowered test overstates it (Type M).

## When to bring in a specialist

Tell the user to consult a statistician or an evaluation methodologist when:
- Fewer than about 30 clusters are feasible in total; small-sample cluster inference needs methods this script does not implement, and the design may need to change
- The outcome is rare (a baseline rate of a few percent or less), a count, or a time-to-event, where the two-proportion and SD formulas do not apply
- The design is a stepped-wedge, a factorial with more than two components, or unequal allocation across arms, or cluster sizes vary widely; the design effect above is the equal-cluster, two-arm case
- Take-up is expected to be low or two-sided (control units get the treatment too), so the effect on compliers needs an instrumental-variables power calculation
- The calculation will be used for an ethics submission or a pre-registration, where the method must be defended

Bring them: the inputs table with sources, the script command and output, the sensitivity table, the feasible sample, and the design from `choose-trial-design`.
