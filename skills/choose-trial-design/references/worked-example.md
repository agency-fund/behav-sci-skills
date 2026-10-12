# Worked example: HIV self-test kits through community pharmacies in Lagos

The program, its numbers, the rollout calendar, and the constraints are illustrative. No result is asserted; the example shows the choice, not an outcome.

**User's answers to Before you start.** Intent: a state program distributes HIV self-test kits through 120 community pharmacies in 10 local government areas (LGAs); the change under test is a subsidy (kit price from ₦2,000 to ₦500) plus a peer-referral voucher that lets a buyer give a free kit to a partner; outcome: share of adult customers offered a kit who buy one, from the pharmacy log; decision: whether to scale the bundle to all 20 LGAs. Spillovers: customers of one pharmacy talk; vouchers travel to partners who may use another pharmacy in the same LGA. Rollout: procurement can supply 40 pharmacies per quarter; every pharmacy must be covered within 12 months. Withholding: pharmacies can be delayed, not excluded. Take-up: the program can offer the subsidy at the pharmacy but cannot assign who buys. Components: two; the decision needs to know whether the voucher adds anything beyond the subsidy. Units: 120 pharmacies, 10 LGAs, four quarters; theory of change says price and partner reach are separate mechanisms.

```markdown
# Trial design choice: subsidy and peer-referral voucher for HIV self-test kits, Lagos (illustrative)

**Decision this informs:** scale the bundle to all 20 LGAs, or the subsidy alone, or neither
**Intervention and outcome:** price subsidy and partner voucher at the pharmacy; share of adult customers offered a kit who buy one

## Constraints
| Constraint | Answer | Source |
|---|---|---|
| Spillovers | within a pharmacy via customers talking; across pharmacies within an LGA via vouchers given to partners | program staff |
| Rollout | phased by procurement, 40 pharmacies per quarter, all 120 within 12 months | procurement plan |
| Withholding | can delay any pharmacy; cannot exclude any; all treated by month 12 | state program director |
| Control over take-up | assigns the subsidy and voucher to the pharmacy; cannot assign who buys | program design |
| Components | 2 (subsidy, voucher); decision needs to know which matter: yes | theory of change |
| Units available | 120 pharmacies in 10 LGAs; about 80 adult customers offered a kit per pharmacy per quarter (illustrative); 4 quarters | pharmacy logs |

## Designs ruled in or out
| Design | Verdict | Because |
|---|---|---|
| Individual | out | customers of one pharmacy talk and the subsidy is posted at the counter; no way to treat one customer and not the next |
| Cluster (parallel) | in | the pharmacy is the natural unit; a waitlist treats every pharmacy by month 12 |
| Stepped-wedge | in | matches the 40-per-quarter procurement; costs a time model and loses the clean component separation |
| Factorial | in | two components whose separate value the decision needs; 2×2 at the pharmacy level |
| Encouragement | not needed | the treatment is delivered to the pharmacy and the outcome is measured there; take-up is the outcome, not a compliance problem |

## Chosen design: pharmacy-level 2×2 factorial with a waitlist
- Unit of randomization: pharmacy
- Arms and allocation: control (no change), subsidy only, voucher only, subsidy plus voucher; 30 pharmacies each
- Blocking or stratification: by LGA (12 pharmacies per LGA, 3 per arm), because LGAs differ in testing demand and it contains voucher spillovers within the stratum
- Timing: quarters 1–2 are the test; quarters 3–4 roll out the winning bundle to all 120 pharmacies, meeting the 12-month commitment; procurement is sequenced so 40 pharmacies are supplied per quarter within the assignment
- Randomization procedure: drawn by the evaluation team in a scripted random draw, witnessed by the state program director and one pharmacist association representative; assignment list dated and filed before any supply ships
- Power cost: design effect 1 + (m − 1)ρ at about 80 customers per pharmacy; each main effect uses all 120 pharmacies (60 versus 60); the subsidy × voucher interaction is underpowered and is reported as exploratory
- Analysis implications: cluster-robust analysis at the pharmacy; additivity of the two components assumed and stated; LGA fixed effects
- Ethics of withholding: kits remain available at the full price in every pharmacy; control pharmacies are delayed six months, not excluded; genuine uncertainty about whether the voucher adds value is documented; the state AIDS control agency and the institutional ethics board sign off before the draw

## Runner-up: three-step stepped-wedge at the pharmacy level
Forty pharmacies cross over to the full bundle each quarter in randomized order, with the fourth quarter fully treated. It replaces the factorial if the state will not leave any pharmacy untreated for six months. The cost: the voucher's separate contribution is lost unless steps cross components, and seasonal testing demand (campaign months) must be modeled as a time trend.

## Hand-off
- To estimate-sample-size: unit = pharmacy; m ≈ 80 customers per quarter; binary outcome (purchase among those offered); no local ICC, so a range is needed; take-up 1.0 at the pharmacy level; two quarters of test data; main effects on 60 versus 60 pharmacies
- To plan-evaluation-design: comparison condition = control pharmacies in quarters 1–2; rollout shape = waitlist with all pharmacies treated from quarter 3

## Open questions
- How often vouchers are redeemed at a pharmacy other than the one that issued them; if it is common, LGA-level contamination weakens the voucher main effect and the stratification should be revisited
- Whether procurement can honor a random assignment rather than its usual geographic sequence
```
