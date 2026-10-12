# Worked example: monthly feedback to teachers running reading sessions, Bihar

A state education program in Bihar, India, supports government primary teachers to run a daily 45-minute reading session grouped by children's current level. Monitors visit each school twice a month and record whether the session ran. The lever brief from `select-intervention-levers` chose feedback on behavior for a confirmed barrier: teachers do not know how their own session count compares with what the program expects, and assume "most schools skipped this month too". The measurement plan supplies each teacher's monthly session count from monitor visits. All numbers are illustrative; this is not a real result.

Inputs the user gave: the behavior (teachers in 240 program schools in two blocks of Gaya district run the reading session every school day); data (monitor records, twice monthly, with a known gap when a monitor misses a visit); who sees it (the teacher; the block officer receives a school-level aggregate, not per-teacher numbers, under a written agreement that it is not used in appraisal); distribution (about a third of teachers run fewer than half the expected sessions, a third near the expectation, a third above); channel (SMS in Hindi to the teacher's phone, plus a paper version shown by the monitor at the next visit).

```markdown
# Feedback report specification

**Behavior:** Teachers in the 240 program schools in two blocks of Gaya district run the 45-minute reading session every school day.
**What the person does not currently know:** How many sessions the monitor recorded for them last month, and how that compares with what the program expects.
**Data source:** Monitor visit records, two visits per school per month, extrapolated to the month; known problem: a missed visit leaves one observation, which the report labels "based on one visit".

## Metric
- **Headline (task-level):** Reading sessions run last month, as recorded by the monitor, against 22 expected school days.
- **Secondary (outcome, optional):** None in the monthly report. Children's reading levels go in the termly summary, labeled as an outcome, because a teacher cannot move them in one month.

## Comparison
- **Type:** Standard (22 school days), with own past as a second line, because the program's expectation is defensible and most teachers are below it. A peer comparison is not used in the first version: teachers in a block know each other, and "the average teacher in your block" would read as named colleagues.
- **Reference group or standard:** The school calendar: 22 teaching days in the month.
- **Injunctive cue:** The words "On track" for any teacher at 18 or more sessions, so teachers above the expectation are not told to relax.

## Report content (one period)
"Reading session, [month]: the monitor recorded [n] sessions out of 22 school days (last month: [m]). [On track. | Next step: run the session on the two days after the monitor's visit, the days most often missed.] Next visit: [date]."

## Cadence and duration
- **Frequency:** Monthly, after the second monitor visit, not sooner, because one visit is not a reliable count.
- **Duration:** Every month the program runs; budgeted as a recurring SMS and monitor cost, not a campaign.
- **If it stops:** From the field evidence on repeated reports, expect the effect to decay by something like 10–20% per year after the last report; do not plan a three-month burst.

## Top performers
Teachers at 18 or more sessions see "On track" and the own-past line; no peer line, so there is nothing to drift down toward.

## Bottom performers
Teachers below 11 sessions see the gap to the next step ("reach 11 next month"), not the gap to 22, and one action: run the session on the days most often missed.

## Who sees it
The teacher, by SMS and on paper at the next visit. The block officer sees a school-level aggregate only; the written agreement says it is not used in appraisal or transfer decisions.

## Pilot before scaling
Two months in 60 of the 240 schools, chosen by lottery; the outcome is the monitor-recorded session count; the result is read separately for teachers above 18 at baseline and those below 11, to catch a fall among the top group and discouragement at the bottom.

## What to check before relying on this
- Whether a two-visit count is believable to teachers; if they dispute the number, the report loses trust before it can work.
- Whether "On track" reads as approval or as sarcasm in the local register; test the phrase with the Hindi draft.
```

What the skill did not do: write the final Hindi SMS (`draft-lever-content`), design the monitoring system itself (`design-fidelity-monitoring`), or design a reward for the top teachers (`design-social-recognition`).
