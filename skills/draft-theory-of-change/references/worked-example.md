# Worked example: a mobile immunization camp program in rural Rajasthan

The program, the numbers, and the team's answers are illustrative. They show what a complete run looks like, not findings about any real program.

**User's answers to Before you start.** Outcome: children under two in two blocks of Udaipur district are fully immunized (all scheduled doses) by 24 months; the target in the grant is to raise the share from about 22% to 40% by end-2027 (illustrative baseline from the program's own household listing). Activities as delivered: a mobile camp with a nurse and a cold box visits each of 60 villages on a fixed day each month; a village mobilizer announces the camp two days before; each completed dose earns the caregiver one kilogram of lentils. Population: caregivers (mostly mothers) of children under two; the mobilizer and nurse deliver. Evidence supplied: eight months of camp monitoring data; informal conversations with about a dozen mothers; no evidence scan brief; the team recalls "a trial in Rajasthan with incentives" but did not supply it. Behaviors the team named: caregivers bring the child for each dose.

```markdown
# Theory of change

**Outcome (as given):** Children under two in the two program blocks of Udaipur district are fully immunized by 24 months; from about 22% to 40% by end-2027 (illustrative).
**Population:** Activities reach caregivers of children under two in 60 villages, via the mobilizer and the camp nurse; the outcome is for those children.
**Activities (as delivered):** (a) monthly mobile camp, fixed day per village; (b) mobilizer announcement two days before; (c) one kilogram of lentils per completed dose.
**Evidence supplied:** eight months of camp monitoring data (illustrative); informal conversations with about twelve mothers; no evidence scan brief.

## Causal chain

| # | Link (from, to) | Assumption (if ..., then ..., because ...) | Evidence | Strength |
|---|---|---|---|---|
| 1 | Monthly camp on a fixed day, vaccines available within the village on a predictable date | If the camp runs reliably with stock, then a dose is available without travel, because the main cost of immunization here is a trip to a distant clinic | Monitoring: 92% of scheduled camps held with full stock over eight months (illustrative) | tested here |
| 2 | Announcement plus predictable date, caregivers bring the child to the camp on camp day | If caregivers know the day and trust it will happen, then they attend, because missed visits are driven by not knowing when, not by refusal | Informal conversations with about twelve mothers; not systematic | assumption |
| 3 | Lentils per dose, caregivers return for each later dose until the schedule is complete | If a small immediate reward is attached to each dose, then drop-off between doses falls, because the benefit of later doses is distant while the trip cost is immediate | None supplied; the team recalls a published trial but did not supply it; evidence scan not run | assumption (pending evidence scan) |
| 4 | All doses received by 24 months, child fully immunized | If the cold chain holds and the schedule is completed, then the child is protected, because vaccine efficacy is established outside this program | Cold-chain monitoring: 3 of 24 camp-months reported a cold-box temperature excursion (illustrative); efficacy is biomedical and not assessed here | tested elsewhere (efficacy); tested here (cold chain, with a gap) |

## Behaviors the chain depends on
- Caregivers bring the child to the camp on camp day (link 2); inferred by this skill, team to confirm
- Caregivers return for each later dose until the schedule is complete (link 3); confirmed by team
- The mobilizer announces the camp two days before, every month (link 2); inferred by this skill
- The nurse brings a stocked, cold cold box to every camp (link 1 and 4); inferred by this skill

## Weakest links
- Link 3: it carries the whole gap between first-dose attendance and completion (monitoring shows about 60% of eligible children get a first dose at a camp and about 22% complete; illustrative), and its evidence cell is empty. An evidence scan brief on incentives for immunization completion in India would raise the rating to "tested elsewhere"; completion data from the program's own camps, split by whether the lentils were given, would raise it to "tested here".
- Link 2: the "they don't know when" assumption is a team belief from a dozen conversations; if the real barrier is distance on camp day, opportunity cost, or a spouse's permission, the announcement does nothing. A short diagnostic round (see `decompose-comb-barriers`) would test it.

## What to check before relying on this
- The link 2 assumption that non-attendance is about not knowing the date; it is the cheapest assumption to be wrong about.
- Link 3 is rated "assumption"; run `assess-evidence-base` and then `assess-evidence-transferability` on whatever it finds before treating the incentive as evidenced.
- Three of the four behaviors were inferred by this skill; the team should confirm the mobilizer's and the nurse's behaviors are part of the program's delivery standard, not assumed.
- The cold-chain excursions in link 4 mean "fully immunized" on the register may overstate protection in some camp-months.
```

**What happened next (illustrative).** The team handed the four behaviors to `define-key-behavior`, which selected "caregivers return for each later dose" as the target behavior, and ran `assess-evidence-base` on incentives for immunization completion to fill link 3's evidence cell.
