# Worked example: reminders for monthly immunization camps in Udaipur district, Rajasthan

Illustrative. The program, the villages, and every number below are invented to show a complete run of the skill; none is a finding. The target behavior came from `define-key-behavior`, the barrier from `decompose-comb-barriers` confirmed by exit interviews and a household survey, the audience brief from `map-audience-context`, and the lever brief from `select-intervention-levers`.

**Inputs supplied by the user:** 48 villages; a camp on a fixed day each month, 9am to 2pm, at the anganwadi center; the register holds each child's next due dose and the camp date; exit interviews at 12 camps and a 600-mother survey found most missed doses were explained by not knowing which day the camp fell on (illustrative); vaccine stock reliable for two years; no fees or distrust reported; about 60% of households have a phone, usually held by the husband; many mothers cannot read Hindi SMS; the ASHA visits each hamlet weekly; Mewari voice calls are feasible from the program's call center.

```markdown
# Reminder schedule

**Target behavior:** Mothers of enrolled children under two in the 48 program villages bring the child to the monthly camp at the anganwadi center on the month the next dose is due.
**Barrier check:** Forgetting the camp day. In exit interviews at 12 camps and the 600-mother survey, 64% of mothers of children with a missed dose said they did not know the camp was that day or that week (illustrative). Stock has been reliable for two years; no fees; no distrust of the ANM or ASHA reported. Supply, cost, and trust ruled out.
**Due-date structure:** Recurring monthly, fixed day per village, known from the register. Window: the camp day itself, 9am to 2pm; a missed camp means a one-month delay.

## Schedule
| # | Sent when (relative to the window) | Channel | Names | Stops when |
|---|---|---|---|---|
| 1 | 2 days before the camp | Voice call in Mewari to the household phone, asking for the mother | Child's name, the dose due, the camp day and date, the anganwadi center, the hours | Dose recorded at the camp; household opts out; after 3 monthly cycles with no attendance (then ASHA follow-up instead) |
| 2 | Morning of the camp, during the weekly hamlet round moved to camp day | ASHA in person | The same, plus an offer to walk together | Dose recorded; mother declines |
| 3 | 1 day after a missed camp | Voice call | That the dose is still due and the next camp date | Dose recorded; opt-out |

## Frequency and ceiling
- **Per window:** Two before, one after a miss; three contacts per monthly cycle at most.
- **Ceiling:** Three consecutive cycles of calls with no attendance; after that the household moves to ASHA-only follow-up, because the problem is no longer forgetting. The cadence is a design choice; the weekly-versus-daily claim from Kenya is unverified and is not the reason for it.
- **Opt-out:** Say "stop calls" on any call, or tell the ASHA; takes effect the same month.

## Content requirements (input to draft-lever-content)
- **Names:** The child by name, the specific dose, the day and date, the anganwadi center, the hours; where the mother stated a goal at enrollment ("all doses by the first birthday"), that goal.
- **Does not:** Mention more than one child's dose per call; spend wording on loss or gain framing (no difference in the Karlan trials); disclose anything beyond a routine immunization, since the phone is usually the husband's.

## Channel choice
Voice in Mewari, not Hindi SMS, because many mothers cannot read Hindi and the household phone is held by the husband; the call asks for the mother and leaves the date with whoever answers, since a routine vaccine date is not sensitive. The ASHA covers the 40% of households without a phone and is the morning-of contact for everyone.

## Reminders alone, or bundled?
The Haryana test: in Haryana, SMS alone had no impact and SMS plus local ambassadors was the most cost-effective bundle. Here the barrier is forgetting and the ASHA already reaches every hamlet, so the schedule bundles the call with the ASHA as messenger; run `select-messenger` to confirm the ASHA is the right person rather than assumed. Incentives are not added: stock is reliable and no cost barrier was found, but if the decay check shows attendance falling among phone-less households, run `design-incentive-scheme` before adding more calls.

## Decay check
- **Measure:** Attendance among due children in reminded versus not-yet-reminded villages (a staggered start across the 48 villages), call delivery rate, and opt-outs, at cycles 1, 3, and 6.
- **Trigger:** A fall of more than a third from the cycle-1 effect by cycle 6 (illustrative threshold) sends the schedule back for redesign, with the ASHA-only arm as the comparison.

## Expected effect
Thakkar et al. (2016): OR 2.11 across 16 RCTs, 1.68 after bias correction, in medication adherence, mostly high-income countries. Kenya ART (Pop-Eleches et al., 2011): about 13 to 16 points on reaching 90% adherence with weekly SMS. Kenya immunization (Gibson et al., 2017): positive with incentives attached, size unverified. Haryana (Banerjee et al., 2025): SMS alone no impact. Academic trials average 8.7 points against 1.4 in nudge-unit trials (DellaVigna & Linos, 2022). This program has a confirmed forgetting barrier, reliable stock, and a messenger in the loop, which is closer to the bundles that worked than to the Haryana SMS-only arm. Plan for 5 to 10 percentage points of additional on-time attendance (illustrative planning range), with the Haryana null as the floor if the ASHA contact is not delivered.

## What to check before relying on this
- Whether the 64% "did not know the day" answer holds up when a mother is asked on the camp day itself, or whether it is a polite explanation for a cost or distance problem.
- Whether the household phone is answered during the day and the message reaches the mother, not only the husband.
- Whether the ASHA can move her weekly round to camp day in every hamlet; if not, row 2 is not delivered and the plan is reminders alone.
- Whether the register's due-dose data is current; a call about the wrong dose costs more trust than no call.
```
