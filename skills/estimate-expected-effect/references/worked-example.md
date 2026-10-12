# Worked example: SMS reminders for antenatal iron-folate adherence in Malawi

The program, its baseline, the cost, and the decision are illustrative. The two published estimates are the ones the dossier records for Thakkar et al. (2016) and for the Kenya ART weekly-SMS trial (Pop-Eleches et al. 2011; the 13–16 point figure is from a secondary source per the dossier); nothing else about those studies is asserted here.

**User's answers to Before you start.** Estimates: (a) Thakkar et al. (2016), *JAMA Internal Medicine*, meta-analysis of text-message reminders for medication adherence in chronic disease: OR 2.11 (95% CI 1.52–2.93), 16 RCTs, N = 2,742; bias-adjusted OR 1.68; adherence estimated to rise from 50% to 67.8%; source type: meta-analysis, bias-corrected figure available. (b) Kenya ART trial (Pop-Eleches et al. 2011): weekly SMS raised the share reaching 90% adherence by about 13–16 points over 48 weeks; source type: academic field trial. Outcome: share of enrolled pregnant women reaching 80% or more of daily iron-folate doses by pill count at the third antenatal visit; baseline 30% (illustrative, from the program's own pill counts at four clinics). Decision: whether to scale SMS from four clinics to the district's 22 clinics (illustrative). No transferability verdict. Cost about $0.40 per woman per month (illustrative).

```markdown
# Effect-size benchmark: SMS reminders on iron-folate adherence (80%+ of doses by pill count)

**Decision this informs:** scale-up from 4 clinics to 22 in one district
**Outcome, unit, baseline:** adherence at the third antenatal visit; percentage points; baseline 30% from the program's pill counts (illustrative)
**Conversion used:** SD of a binary outcome at p = 0.30 is sqrt(0.30 × 0.70) = 0.458, so 1 SD = 45.8 points; odds ratios applied to baseline odds 0.30 / 0.70 = 0.429

## Published estimates the team is relying on
| Source | Source type | Reported effect (unit) | In the test's unit | Already bias-corrected? |
|---|---|---|---|---|
| Thakkar et al. 2016, 16 RCTs, N = 2,742 | meta-analysis (chronic-disease adherence) | OR 2.11; bias-adjusted OR 1.68 | OR 2.11 at p = 0.30: odds 0.904, p = 0.475, +17.5 pp (0.38 SD); OR 1.68: odds 0.720, p = 0.419, +11.9 pp (0.26 SD) | yes (1.68) |
| Kenya ART weekly SMS (Pop-Eleches et al. 2011; secondary source) | academic field trial | +13 to +16 pp (90% adherence, 48 weeks) | +13 to +16 pp (0.28–0.35 SD) | no |

## Discounts, in order
1. Publication bias: applied to Thakkar; the bias-adjusted OR 1.68 replaces 2.11 → +11.9 pp at this baseline, the top of the range
2. Lab-to-field: not applied; neither source is a lab study
3. Academic-to-practitioner: applied to the Kenya trial, an academic field trial; the reference gap is 8.7 versus 1.4 points (ratio about six, DellaVigna and Linos 2022); 13–16 pp / 6 ≈ 2–3 pp sets the low end; not applied as a constant
4. Fit to this setting: not checked; ART adherence (lifelong, clinic-monitored) differs from a daily supplement in pregnancy with nausea and household disapproval as known barriers, and phone ownership among pregnant women here is unknown; low end widened to 2 pp
5. Persistence: not needed; SMS continues at scale, so the during-program effect is the one the decision uses

## Expected effect: planning range
| | Percentage points | SD | Produced by |
|---|---|---|---|
| Low | 2 | 0.04 | academic-to-practitioner gap on the Kenya trial, widened for unchecked fit |
| Central | 5 | 0.11 | judgment: nearer the low end because both sources are academic and fit is unchecked |
| High | 12 | 0.26 | bias-adjusted meta-analytic OR 1.68 at the 30% baseline |

## Smallest effect worth detecting
5 points; set by the scale-up decision: at $0.40 per woman per month over about six months of enrollment (illustrative), a 5-point gain is roughly $48 per additional adherent woman; whether that is acceptable is `estimate-cost-effectiveness`'s call; provisional; cost inputs still needed: clinic staff time to maintain phone lists, SMS gateway fees at 22 clinics

## Number to hand to estimate-sample-size
5 points (0.11 SD), the smaller of the central expected effect (5) and the smallest effect worth detecting (5); they coincide here. If the true effect sits at the low end (2 points), a test powered for 5 will most likely miss it, and that risk should be stated in the power calculation.

## What to check before relying on this
- Phone ownership and control among pregnant women at the four clinics; if under half own a phone, the reachable population shrinks and the fit discount should widen
- The 30% baseline, which comes from pill counts at four clinics and may not hold at the other 18
- Whether any field trial of SMS reminders for antenatal supplements exists in southern Africa; it would replace the ART-based numbers as the top of the range
```
