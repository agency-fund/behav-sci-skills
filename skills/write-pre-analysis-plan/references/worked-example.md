# Worked example: tax compliance letters in Guatemala

Illustrative run. The program, numbers, and variables are invented to show the shape of a complete output; none is a finding. Setting: a tax authority and a research partner are about to send one of three letters to taxpayers who declared income but had not paid by the due date. The evaluation design brief came from `plan-evaluation-design`; no outcome data by arm have been seen (confirmed); registration is with the AEA RCT Registry before the letters go out.

**Design brief (carried over):** individual randomization of 24,000 late taxpayers, stratified by taxpayer type (individual, firm) and prior-year payment status; arms: no letter (control), standard reminder letter, reminder plus a descriptive-norm sentence; primary outcome: paid any of the declared amount within 60 days of the letter date (administrative payment records); smallest effect worth detecting: 3 percentage points on the payment rate, set by the authority as the gain that would justify a national mailing.
**Stakes (from the user):** the tax authority wants the norm letter to work and would like to report revenue; the research partner has published on norm messages.

```markdown
# Pre-analysis plan

**Trial:** Late-payment letters, Guatemala (illustrative)
**Registry:** AEA RCT Registry; id to be added on registration
**Date-stamped:** 2026-10-12, before any outcome data by arm were seen
**Design carried over from:** plan-evaluation-design brief dated 2026-10-05

## 1. Hypothesis
Receiving a reminder letter raises the share of late taxpayers who pay any of the declared amount within 60 days, relative to no letter; the norm sentence raises it further relative to the standard letter.

## 2. Design (carried over, not re-decided)
Individual randomization of 24,000 late taxpayers; three arms (control, standard letter, norm letter), equal allocation; stratified by taxpayer type and prior-year payment status; outcome read from payment records 60 days after the mailing date.

## 3. Primary outcome
Paid any amount against the declared liability within 60 days of the letter date: binary, from the authority's payment ledger matched on taxpayer id. No transformation. A taxpayer with no ledger match is coded as not paid, since the ledger is the universe of payments. Smallest effect worth detecting: 3 percentage points, set by the authority (carried over).

## 4. Secondary outcome families
| Family | Outcomes | Index or correction (mechanics in adjust-for-multiple-comparisons) | Why this family |
|---|---|---|---|
| Amount | share of declared liability paid within 60 days; paid in full within 60 days | family-level false discovery rate correction | the authority's revenue question |
| Timing | days from letter to first payment, among payers | reported descriptively, no test | speed matters operationally but is conditional on paying |
| Next period | filed on time in the following period | single outcome, no correction | the persistence question |

## 5. Estimator and inference
Intention-to-treat by assigned arm. Linear probability model of the primary outcome on arm indicators with strata fixed effects and prior-year payment amount as a covariate. Individual randomization, so heteroskedasticity-robust standard errors; no clustering. Attrition: none expected, since the outcome is administrative; any taxpayer deregistered before the mailing is dropped from all arms by the same rule. Exclusions: taxpayers whose letter is returned undelivered stay in the analysis (ITT).

## 6. Pre-specified subgroups
| Subgroup | Variable and cut | Theory-based reason | Status |
|---|---|---|---|
| Prior-year payers vs non-payers | paid in prior year, yes/no (stratum) | for prior payers a letter is a reminder; for non-payers it is information or a norm signal, so the norm sentence should matter more for non-payers | confirmatory |
| Firms vs individuals | taxpayer type (stratum) | firms have accountants who act on reminders regardless of framing, so the norm sentence should matter less | confirmatory |
| Liability size | above vs below the median declared liability | no theory-based prediction | exploratory |

## 7. Decision rules
| Primary result | What the team will do | Who decides | Guardrail results that would override |
|---|---|---|---|
| Norm letter beats standard by 3 points or more | adopt the norm letter nationally for late payers | authority's compliance director | a rise in disputes or complaints logged against letter recipients |
| Standard letter beats control by 3 points but the norm sentence adds under 1 point | adopt the standard letter; do not claim a norm effect | same | same |
| Neither letter reaches 3 points | no national mailing; results reported in full | same | none |

## 8. Where this plan is detailed, where it is flexible
Detailed: the primary outcome, the two confirmatory subgroups (both parties have a stake in the norm result, and prior-payment status is the subgroup most likely to be fished), and the decision rules. Flexible: the exact amount-family index, additional covariates for precision, and any exploratory heterogeneity analysis, all to be labeled exploratory. A populated plan listing every deviation will be posted with the results.

## 9. Registration
AEA RCT Registry fields filled from this document; plan attached and date-stamped; the research partner holds the payment-ledger extract until the registry confirms the entry; the authority's data team sends no arm-level tabulations before day 60.

## Open questions
- Whether the ledger match on taxpayer id is complete for firms with multiple registrations; check at baseline, not endline.
- Whether returned-undelivered letters are logged; if not, the ITT estimate is diluted by an unknown non-delivery rate.
```
