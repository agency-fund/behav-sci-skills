# Worked example: who benefited from a growth-mindset session in Peruvian public schools

Setting: an illustrative cluster RCT ("Creciendo Juntos", three regions of Peru) of a one-session growth-mindset program for grade-8 students in 180 public secondary schools, 90 treatment and 90 control, about 12,000 students, schools randomized. Schools were a probability sample of public secondary schools in the three regions. Primary outcome: end-of-year national math score in points (regional mean about 50, standard deviation about 12). The pre-analysis plan, registered before baseline, names two moderators. All numbers are illustrative, not findings.

**Inputs the user gave.** The plan, the dataset description (covariates: sex, age, baseline math and reading, mother's education, school size, urban or rural, school poverty index), the overall effect, R as the software, and the decision: describe who benefited and choose what to pre-register next. The funder also asked whether to "run it only in rural schools next year"; that is a targeting question and is noted at the end.

```markdown
# Heterogeneous effects report

**Trial:** Creciendo Juntos; treatment vs control; randomized by school; 90 schools (6,050 students) vs 90 schools (5,950 students)
**Primary outcome:** End-of-year national math score, points
**Overall effect:** 1.8 points (95% CI 0.3 to 3.3), pre-specified model, standard errors clustered by school (about 0.15 SD, for cross-outcome comparison only)
**Sample:** Probability sample of public secondary schools in three regions; results speak for public grade-8 students in those regions, not for private schools or other regions
**Decision this informs:** Describe who benefited; choose what to pre-register next. (The "rural schools only" question is a targeting decision; see the specialist note below.)
**Plan status:** Pre-analysis plan dated 2025-02-14 names 2 moderators

## Pre-specified moderators (confirmatory)
| Moderator (verbatim from the plan) | Expected direction | Effect at each level (points, 95% CI) | Interaction (points, 95% CI) | Unadjusted p | Adjusted p (family: pre-specified moderators, m = 2, Bonferroni) |
|---|---|---|---|---|---|
| Baseline math tercile | Larger for bottom tercile | Bottom 3.1 (0.8 to 5.4); middle 1.6 (-0.4 to 3.6); top 0.6 (-1.5 to 2.7) | Bottom minus top 3.0 (0.5 to 5.5) | 0.02 | 0.04 |
| School poverty index above median | Larger in poorer schools | Poorer 2.4 (0.3 to 4.5); less poor 1.1 (-0.9 to 3.1) | 1.3 (-1.6 to 4.2) | 0.38 | 0.76 |

The baseline-tercile interaction holds after adjustment, in the expected direction: the effect is concentrated among students who started in the bottom tercile. The poverty interaction is not detectable at this sample; its interval includes both zero and a difference larger than the overall effect.

## Exploratory machine-learning splits (hypothesis-generating)
- **Method and software:** causal forest, grf in R
- **Sample splitting:** 50% fit, 50% test, split at the school level; 25 repeated splits; medians reported
- **Covariates used:** baseline only: sex, age, baseline math, baseline reading, mother's education, school size, urban or rural, poverty index
- **Best linear predictor:** heterogeneity coefficient 0.6 (95% CI 0.1 to 1.1); reads as real heterogeneity detected, with predictions that overstate the spread
- **Group average effects by predicted-impact quantile:**
  | Group | Effect (points, 95% CI) |
  |---|---|
  | Least affected fifth | 0.2 (-1.8 to 2.2) |
  | Second fifth | 1.0 (-0.9 to 2.9) |
  | Third fifth | 1.6 (-0.3 to 3.5) |
  | Fourth fifth | 2.3 (0.3 to 4.3) |
  | Most affected fifth | 4.1 (1.9 to 6.3) |
  | Most minus least | 3.9 (0.9 to 6.9) |
- **Characteristics of the most and least affected:** baseline math: 38 in the most affected fifth vs 61 in the least (difference -23 points); share girls: 0.58 vs 0.45 (+0.13); mother's education primary or less: 0.47 vs 0.29 (+0.18); rural school: 0.52 vs 0.31 (+0.21). These describe who the model picked out; they are hypotheses, not confirmed moderators.

## Power limits
The trial was powered (80%) to detect a main effect of 1.5 points. Neither moderator was powered; an interaction of that size needs a much larger sample. The poverty result is "not detectable at this sample", not "the same in poor and less poor schools". The exploratory fifths are estimated on half the sample per split and their intervals are wide; the least-affected fifth's interval includes the overall effect.

## What to pre-register next time
- Baseline math tercile, expected larger effect for the bottom tercile, because it held after adjustment here; sample needed: from estimate-sample-size, powered for the interaction, not the main effect
- Sex (girls), expected larger effect, because the most-affected group was more often girls in the exploratory split; sample needed: to be calculated
- Rural school, expected larger effect, because of the exploratory split only; sample needed: to be calculated

## What to check before relying on this
- The sampling assumption: these schools were a probability sample of public secondary schools in three regions, so the results do not speak for private schools or other regions.
- That the sex and rural findings keep their "exploratory" label in the funder summary; only the baseline-tercile result is confirmatory.
- That no enrollment or targeting rule has been drawn from this report: "rural schools only" would be a decision to exclude urban students on an exploratory result, which is the specialist case.
```

**Where this run stopped.** It did not correct the p-values itself beyond handing the two-test family to `adjust-for-multiple-comparisons`, did not calculate the next trial's sample (`estimate-sample-size`), and did not judge whether the effect would survive a government rollout (`assess-scalability`). Because the funder floated running the program only in rural schools, the report told the user to bring the plan, the moderator table, and the exploratory outputs to a statistician before any targeting decision.
