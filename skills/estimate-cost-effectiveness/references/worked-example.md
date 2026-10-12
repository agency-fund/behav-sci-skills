# Worked example: cost per additional adherent woman in a Malawi iron-folate reminder program

Setting: an illustrative cluster RCT ("Mayi Wathanzi", Mchinji and Dedza districts, Malawi) of community health worker (CHW) home-visit reminders for daily antenatal iron-folate tablets, 24 health centers (12 per arm), 1,600 women enrolled at treatment centers over 10 months of 2025. The ministry wants the number beside an SMS-only reminder program in another district, per additional adherent woman. All numbers are illustrative, not findings.

**Inputs the user gave.** The effect from the trial's pre-specified model with standard errors clustered by center; an ingredients list with quantities and local prices, including the inputs the program did not pay for; no transfers; research costs listed separately; program perspective; USD 2025 at the average market rate.

```markdown
# Cost-effectiveness estimate

**Program:** Mayi Wathanzi; CHW home visits reminding pregnant women to take daily iron-folate, about 10 visits per woman over the pregnancy; 1,600 women at 12 treatment health centers; 10 months of 2025
**Effect:** Adherence (pill count of 80% or more at 32 weeks): 43% vs 31%, +12 percentage points (95% CI 5 to 19); applies to 1,600 women; source: this trial. Additional adherent women: 0.12 x 1,600 = 192 (80 to 304 at the confidence bounds)
**Perspective:** Program, because the ministry's comparison table is built from implementer costs; the society view is shown in the sensitivity table
**Currency and year:** USD, 2025 prices; Malawi kwacha converted at the 2025 average market rate; **discount rate:** none applied, because all costs fall within one year (10% a year would apply to a multi-year run, following J-PAL)
**Comparator(s):** SMS-only antenatal reminder program, other district; common unit: additional woman adherent at 32 weeks

## Ingredients
| Category | Item | Quantity | Unit price | Cost | Paid / donated / borrowed |
|---|---|---|---|---|---|
| Staff time | CHW visit time, 48 CHWs, 4 h/week, 40 weeks | 7,680 h | $0.75/h | $5,760 | Borrowed (government-stipended; priced at the local wage) |
| Staff time | Supervisors, 4 x 8 h/month x 10 months | 320 h | $2.50/h | $800 | Paid |
| Training | 2-day training, 52 people (venue, per diems, materials) | 1 | $2,600 | $2,600 | Paid |
| Equipment (annualized) | Bicycles, 48 x $90, 3-year life | 48 | $30/year | $1,440 | Paid |
| Materials | Printed adherence cards | 1,600 | $0.20 | $320 | Paid |
| Transport and communication | Phone credit, 48 CHWs x 10 months | 480 | $2 | $960 | Paid |
| Space | Clinic rooms for monthly CHW meetings, 24 centers x 10 | 240 | $5 | $1,200 | Donated |
| Monitoring | Data entry | 1 | $600 | $600 | Paid |
| Participant time (society only) | 1,600 women x 10 visits x 20 min | 5,333 h | $0.50/h | $2,667 | Not in the program total |
| **Delivery total (program perspective)** | | | | **$13,680** | |
| Transfers to participants (separate line) | None | | | $0 | |
| Research costs (excluded from delivery) | Endline survey and pill counts | | | $9,000 | Paid |

## Ratios
- Delivery cost per woman reached: $13,680 / 1,600 = $8.55
- Cost per additional adherent woman: $13,680 / 192 = $71.25
- Cost per percentage point per 1,000 women: $8,550 / 12 = $712.50
- Impact per $100: 192 / 136.8 = 1.40 additional adherent women per $100
- Cost per standard deviation: not needed; the comparator reports the same binary outcome

## Sensitivity
| Scenario | Cost used | Effect used | Cost per additional adherent woman | Impact per $100 |
|---|---|---|---|---|
| Headline | $13,680 | 12 points (192 women) | $71.25 | 1.40 |
| Effect at lower confidence bound | $13,680 | 5 points (80 women) | $171.00 | 0.58 |
| Effect at upper confidence bound | $13,680 | 19 points (304 women) | $45.00 | 2.22 |
| Discounted transferred effect | Not applicable: the effect is from this trial | | | |
| Including transfers | No transfers; same as headline | | $71.25 | 1.40 |
| Excluding donated inputs (clinic space) | $12,480 | 12 points | $65.00 | 1.54 |
| CHW time at $1.50/h | $19,440 | 12 points | $101.25 | 0.99 |
| Society perspective (adds participant time) | $16,347 | 12 points | $85.14 | 1.17 |

## Comparability limits
- Transfers: neither program made transfers, so this line does not separate them.
- Fixed costs: training plus annualized bicycles are $4,040, about 30% of the delivery total; cost per woman would fall if the same CHWs covered more women, and the SMS program's fixed share is not known.
- Prices and wages: CHW time is priced at $0.75/h although the program did not pay it; the SMS program's report does not say whether it priced the nurses who sent the messages. The wage range in the table moves the ratio from $71 to $101.
- Outcome measure: this trial used pill counts; the SMS program reports self-reported adherence, so the two "additional adherent woman" units are not the same measure.

## What to check before relying on this
- The CHW wage of $0.75/h and the 4 hours a week, from the field team's timesheets rather than the plan; this is the largest line and the one most likely to be mispriced.
- Whether the SMS program costed its staff time and its platform fees the same way, before the two numbers are placed in one table.
- The effect is this trial's own; no transfer discount applies. If the ministry reuses this number for a different district, it becomes a transferred effect and should go through estimate-expected-effect first.
```

**Where this run stopped.** It did not say whether $71 per additional adherent woman would hold when the ministry runs the program with its own staff across both districts (`assess-scalability`), and it did not rank the program against the ministry's other candidates with different outcomes; that would need a benefit-cost analysis or the ministry's weights, which is the specialist case.
