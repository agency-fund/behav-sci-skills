# Worked example: a transport reimbursement for reporting an HIV self-test result in Lagos

Setting: an illustrative program ("Test Na Easy", Alimosho, Lagos) that distributes HIV self-test kits through partner pharmacies to adults aged 18 to 35. The diagnosis (from `decompose-comb-barriers`, confirmed by exit interviews) is that kit users do not come back to report a result, so reactive results are not linked to care; the lever brief (from `select-intervention-levers`) selected Incentivization, BCT 10.1 Material incentive (behavior). All numbers are illustrative, not findings.

**Inputs the user gave.** Behavior: an adult who collects a kit returns to the same pharmacy within 7 days and reports the result to the counselor, who records it against the kit serial number; a reactive result gets a referral slip. Verification: the counselor's register, about 3 minutes per return. Barrier confirmed: the return trip costs a fare and an hour, and people see no reason to come back if the result is negative. Supply: counselors are present six days a week (checked). Budget: NGN 1,500 per return (illustrative), 2,000 returns, six-month pilot, end date fixed. Daily income of the target group: about NGN 7,000 (illustrative); round-trip fare about NGN 600. Recipients are community members, not staff.

```markdown
# Incentive scheme specification

**Rewarded behavior:** Adults 18 to 35 who collect a self-test kit from a partner pharmacy in Alimosho return to that pharmacy within 7 days and report the result to the counselor.
**Verification:** Counselor register entry against the kit serial number, at the counter, about 3 minutes per return. "Done" is the return and the report, whatever the result; the result itself is not verified and not rewarded, so there is no reason to misreport.
**Confirmed barrier:** Return trip costs a fare and an hour, with no felt reason to return after a negative result (Opportunity, physical, and Motivation, reflective; exit interviews, illustrative). Incentivization chosen because the hassle is real and one-off; Education was rejected as it does not pay the fare.
**Supply check:** Counselors present six days a week at all partner pharmacies; referral clinics confirmed open. Fixed before the reward.

## The reward
| Element | Specification | Reason |
|---|---|---|
| Size | NGN 1,500 (illustrative): about 2.5 times the round-trip fare; about a fifth of a day's income | Covers the hassle with a margin; small enough to be refusable |
| Form | Cash at the counter, framed as transport reimbursement | Certain and immediate; the reimbursement frame ties the payment to the hassle it offsets |
| Timing | Paid at the counter when the register entry is made; no delay | Immediacy is the mechanism |
| Condition | Return and report within 7 days; monitored by the counselor's register | Verification is cheap and already in the workflow |
| Recipient | The kit user | The person who bears the hassle |

## Monitoring decision
Monitor, because the register already exists and costs about 3 minutes per return. The condition excludes people who move away or lose the kit; they can still report by phone, unrewarded, so linkage is not lost.

## Removal plan
- **End date:** 6 months after launch, fixed in the budget.
- **Taper or stop:** Stop, announced at kit collection from month 5 ("transport support ends on <date>").
- **Expected after removal:** Return rates expected to fall back toward the pre-pilot level; what carries the behavior afterward is the counselor's spoken request to return and a one-line reminder SMS (`design-reminder-schedule`).
- **Measure at:** 3 months after the end: return rate for kits collected that month, from the register.

## Crowding-out check
No existing paid or volunteer motive; recipients are community members. Watch for people collecting kits only to earn the return payment (register duplicate serials and repeat collectors) and for the reimbursement frame drifting into "payment for testing" in the pharmacy's own words.

## Ethics
- **Coercion:** About a fifth of a day's income, refusable; nobody is denied a kit or a referral for not returning.
- **Fairness:** People who return by phone receive nothing; pharmacies outside the pilot offer nothing. Both are stated in the pre-test materials.
- **Review:** `audit-intervention-ethics` before launch; the ethics committee covering the pilot, because the behavior is HIV testing; a clinician reviews the referral path and whether paying for return induces repeat testing.

## Cost
NGN 1,500 per rewarded return plus counselor time; cost per additional verified return to be computed against the no-reward pharmacies by `estimate-cost-effectiveness`.

## What to test
Partner pharmacies randomized to reimbursement versus none, same counselors and kits. Outcome: share of kits with a reported result within 7 days, from the register. Follow-up: the same share 3 months after the reward ends.

## What to check before relying on this
- The verification assumption: that counselors record every return against a serial number and do not record phone reports as returns.
- The sizing assumption: that NGN 600 is the typical fare and NGN 7,000 the typical daily income for this group; both from the field team, not yet confirmed for women.
```

**Where this run stopped.** It did not write the counter script or the SMS (`draft-lever-content`), did not set the reminder cadence (`design-reminder-schedule`), and did not produce the cost-effectiveness estimate (`estimate-cost-effectiveness`). Because payments go to low-income adults and the behavior is HIV testing, the specialist section applies before launch.
