# Worked example: antenatal iron-folate adherence in Malawi

Illustrative run. The program, numbers, and thresholds are invented to show the shape of a complete output; none is a finding. Setting: a district health office in central Malawi plans a cluster-randomized trial of a community health worker (CHW) adherence package for pregnant women. Before that, it wants a pilot in two health centers.

**Intervention draft (from the user):** "At the first antenatal visit, the CHW gives each woman a 30-day pill calendar and enrolls her for a weekly voice reminder in Chichewa; the CHW visits once a month to check the calendar and restock."
**Main design (from the user):** cluster RCT across 24 health centers next year, 40 women per center enrolled over 8 weeks, outcome = pill count at the 3-month antenatal visit, sample size assumes 80% retention to that visit.
**Pilot resources:** 2 health centers, 60 women, 12 weeks, 1 study nurse who can run short interviews.
**Biggest worry:** retention to the 3-month visit, then whether the weekly calls go through.

```markdown
# Pilot feasibility study design

**Intervention piloted:** At the first antenatal visit, the CHW gives each woman a 30-day pill calendar and enrolls her for a weekly voice reminder in Chichewa; the CHW visits once a month to check the calendar and restock.
**Main design it serves:** Cluster RCT, 24 health centers, 40 women per center enrolled over 8 weeks, pill count at the 3-month antenatal visit, sample size assuming 80% retention to that visit.
**What this pilot is not for:** estimating the intervention's effect. Its effect estimate will not be used to size the main trial.

## Feasibility questions and progression criteria
| Domain | Question (as a rate or count) | Go | Amend | Stop | Why this threshold |
|---|---|---|---|---|---|
| Recruitment | Share of eligible first-visit women who enroll; women enrolled per center per week | 70% or more, and 5 or more per week | 50 to 69%, or 3 to 4 per week | Below 50%, or under 3 per week | Main design needs 40 per center in 8 weeks, so 5 per week |
| Retention | Share of enrolled women who attend the 3-month visit | 80% or more | 65 to 79% | Below 65% | Main sample size assumes 80% retention |
| Fidelity | Share of scheduled weekly calls that connect; share of monthly CHW visits completed | 75% or more on both | 55 to 74% on either | Below 55% on either | A package delivered at half dose is a different intervention |
| Acceptability | Share of women still using the calendar at the monthly visit; refusals and reasons | 70% or more using | 50 to 69% | Below 50% | Below half, the calendar is not the active ingredient |
| Data completeness | Share of retained women with a countable pill count at 3 months | 90% or more | 75 to 89% | Below 75% | The main outcome is the pill count; a missing count is a missing outcome |

## Pilot size
The rate that most needs estimating is retention. With 60 women the team can tell a retention rate near 80% apart from one near 65% to a margin it can act on (illustrative; confirm the margin with the study statistician); that is an estimation target, not a power calculation. 60 women across 2 centers over 12 weeks: 8 weeks of enrollment, then follow-up to the 3-month visit for the earliest enrollees; later enrollees' 3-month visits fall after the pilot window and are counted when they occur.

## Qualitative component
- Women who miss the 3-month visit (all of them, up to 15): one question, "what stopped you coming?", by phone or at home within 2 weeks of the missed visit; study nurse.
- Women who stop using the calendar (up to 10): "what happened to the calendar?"; at the monthly CHW visit; study nurse.
- Both CHWs and the two center nurses: "what did you skip or change, and why?"; week 12; study nurse.

## What changes in the main design
| Question | If go | If amend | If stop |
|---|---|---|---|
| Recruitment | No change | Extend enrollment to 12 weeks or add centers | Redesign recruitment with the centers before any trial |
| Retention | No change | Raise the sample size for the observed attrition and add a visit reminder | Do not run the trial on the 3-month visit outcome; reconsider outcome timing |
| Fidelity | No change | Fix the failing channel (call provider or CHW schedule) and re-pilot that channel for 4 weeks | Do not run the trial on this package |
| Acceptability | No change | Revise the calendar with the women interviewed | Drop the calendar; reconsider the active ingredient |
| Data completeness | No change | Add a pill-count protocol and nurse training | Change the outcome measure before the trial |

## Report skeleton
1. Participant flow: approached, eligible, enrolled, retained to 3 months, with a countable pill count
2. Each of the five questions: threshold, observed rate with its uncertainty, decision
3. Fidelity and acceptability findings, with the interview reasons
4. Changes to the main design
5. Any observed difference in pill counts, labeled "not a basis for sizing the main trial"

## Open questions
- Whether the two pilot centers are typical: both are on tarmac roads; the main trial includes centers that are not.
- Whether the pilot season (dry season) matches the main trial's enrollment season.
- Ethics: the package involves medication in pregnancy; the district ethics committee reviews the pilot protocol and a stopping rule for any safety concern before enrollment.
```
