---
name: assess-scarcity-load
description: >-
  Use when a program asks people to do something that takes attention, memory,
  or a decision (enroll, choose a plan, fill a form, remember a date, save) and
  you want to know whether the ask lands when they are short of money or mental
  bandwidth. Also use when take-up is lowest among the poorest participants, or
  when a team plans to launch an ask right before harvest, payday, school fees,
  or a festival. Maps the household's income and expense calendar, locates the
  ask against the tight periods, counts the memory and decision demands, rates
  the load, and recommends timing shifts or simplifications (scarcity research
  after Mullainathan and Shafir, with field evidence from Kaur et al. on pay
  timing). Do not use when the question is how many steps, documents, or trips
  the process has; use audit-process-friction instead. Not for picking the
  exact moment to deliver a message (choose-delivery-moment, which takes this
  load map as input), and not for listing every barrier hypothesis
  (decompose-comb-barriers).
license: CC-BY-4.0
metadata:
  title: Rate the load at the moment of the ask
  type: atomic
  stage: diagnose
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: mixed-evidence
  tags: "scarcity, com-b"
  consumes: "target-behavior-brief, audience-context-brief"
  produces: ""
---

## What it does

Estimates how much cognitive or financial strain a person is under at the moment a program makes its ask, then moves or simplifies the ask if the load is high.

Scarcity research says a shortfall of money takes attention: the person is still working on the shortfall while the program asks for a decision, a calculation, or a remembered date. "Bandwidth" here means the attention and working memory left for everything else. An ask that lands in a tight period (before harvest, before payday, in school-fee month) competes with the shortfall for that bandwidth. The output is a load map with a recommendation. It does not write the ask, and it does not pick the exact delivery moment.

## When to use it

### Use it when
- Take-up or follow-through is lowest among the poorest participants and the team suspects the ask is too demanding at the wrong time
- A team is scheduling an enrollment drive, a savings sign-up, or a training and asks "when in the month or the season should we do this?"
- Someone says "they just forget" or "they don't follow through" about a population living on irregular income
- An ask requires a calculation, a comparison between options, or remembering a date or a code, and the team wants to know how heavy that is for this population right now

### Do not use it when
- The friction is in the number of steps, trips, documents, or fees; `audit-process-friction` counts those
- The load map already exists and the question is which day, hour, or landmark to deliver a message on; `choose-delivery-moment`
- No behavior has been defined as who, what, when; run `define-key-behavior` first
- The team wants the full set of competing barrier hypotheses rather than this one; `decompose-comb-barriers`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The behavior as who, what, when (paste the target behavior brief if one exists) and the ask itself: exactly what the program asks the person to do, when it arrives, through which channel, by what deadline, and what it requires them to have in hand, remember, calculate, compare, or decide.
2. **Required.** The population's income and expense rhythm: how they earn (daily wage, piece-rate, harvest sales, remittances, salary), when money arrives, and the large predictable outflows (rent, school fees, festivals, planting inputs, loan repayments). Paste the audience and context brief from `map-audience-context` if one exists.
3. Optional. Any evidence of when take-up is lowest: by week of the month, by season, or for which subgroup.
4. Optional. What the program can change: the timing of the ask, the design of the ask, or the timing of its own payments or transfers, and which is cheapest.

If 1 is missing, ask and stop. If 2 is missing, ask once; if still unknown, proceed with a calendar marked "assumed, to be confirmed with participants" and say the rating is provisional. If 3 and 4 are missing, assume the timing and the design can change and that money cannot, and say so.

## What it draws on

- Mullainathan, S., & Shafir, E. (2013). *Scarcity: Why Having Too Little Means So Much*. Henry Holt / Picador.
- Mani, A., Mullainathan, S., Shafir, E., & Zhao, J. (2013). Poverty impedes cognitive function. *Science*, 341, 976. https://doi.org/10.1126/science.1238041
- Kaur, S., Mullainathan, S., Oh, S., & Schilbach, F. (2025). Do financial concerns make workers less productive? *The Quarterly Journal of Economics*, 140(1), 635–689. https://doi.org/10.1093/qje/qjae038 (also NBER w28338, https://doi.org/10.3386/w28338)
- O'Donnell, M., et al. (2021). Empirical audit and review and an assessment of evidentiary value in research on the psychological consequences of scarcity. *Proceedings of the National Academy of Sciences*. https://doi.org/10.1073/pnas.2103313118
- Haushofer, J., & Fehr, E. (2014). On the psychology of poverty. *Science*. https://doi.org/10.1126/science.1232491
- Bryan, C. J., Tipton, E., & Yeager, D. S. (2021). Behavioural science is unlikely to change the world without a heterogeneity revolution. *Nature Human Behaviour*, 5(8), 980–989. https://doi.org/10.1038/s41562-021-01143-3
- ideas42, Daminger, Hayes, Barrows & Wright (2015). *Poverty Interrupted*. [unverified, author to confirm].

The scarcity account (Mullainathan & Shafir) is that a shortfall of money captures attention, so the bandwidth left for other decisions shrinks, and that this is a feature of the situation, not of the person. Mani et al. tested it with Indian sugarcane farmers before and after harvest; the effect size is unverified in this library's audit, so this skill does not quote one. The field evidence this skill leans on is Kaur et al.: low-income piece-rate manufacturing workers in India who were paid earlier produced 7% more (0.11 SD) and made fewer costly, unintentional mistakes, with the effect concentrated among the most financially constrained. O'Donnell et al. audited 20 scarcity-priming studies and found mixed results, which is why the lab side of this literature is treated as contested. Haushofer & Fehr is the broader review (its content was not fetched in the audit). Bryan, Tipton & Yeager is the reason the rating is given per subgroup: Kaur's effect was concentrated, and a program-wide average would hide it. This skill adds three judgment calls: a three-level load rating from two inputs (financial tightness at the moment of the ask; memory and decision demands), offered as a judgment aid rather than a validated scale; a fixed order of recommendations (move, simplify, split, remind); and the rule that when the calendar shows the household lacks the money at every point, the skill says so and stops instead of designing around it. See `references/evidence-notes.md`.

**WEIRD skew:** the strongest evidence is from India, not from WEIRD samples; the contested lab-priming studies are mostly United States and online samples. The skew therefore runs the unusual way: a user in a high-income setting should check whether a field result from piece-rate workers transfers to salaried populations, and a user in another low-income setting should map the local calendar rather than assume the sugarcane or piece-rate pattern. **Non-WEIRD evidence:** India sugarcane farmers (Mani et al. 2013; pre- versus post-harvest cognitive performance; effect size unverified) and India low-income piece-rate manufacturing workers (Kaur et al. 2025; earlier pay raised output 7%, 0.11 SD, concentrated among the most constrained).

**Replication status:** contested for the original lab priming effects (a published comment on the 2013 *Science* paper, not separately cited in the dossier, and the O'Donnell et al. 2021 audit of 20 studies, which gave mixed results); strong for field pay timing on the strength of Kaur et al. 2025, one large field experiment; the dossier gives no meta-analysis, so no pooled number is quoted.

## How to do it

1. **Write the ask as the person experiences it:** when it arrives, through what channel, by what deadline, and what it requires them to have, remember, calculate, compare, or decide. "Enroll" usually hides four or five sub-asks; list them.
2. **Map the income and expense calendar** for the population over the relevant cycle (month, season, year): inflows by source, timing, and reliability; predictable outflows; and the periods participants themselves call tight. Use the audience and context brief, existing interviews, or the user's knowledge, and record the source of each row, because an assumed row is the first thing to check.
3. **Locate the ask on the calendar.** Does it land in a tight period, just after an inflow, or at a point that differs by household (wage earners versus farmers in the same village)? If it differs, split the rating by subgroup.
4. **Count the demands of the ask:** things to remember, calculations, options to compare, deadlines; and for each, whether the program could hold it instead (pre-fill, a default, a reminder, a staff member who does the arithmetic). These are the demands that compete with bandwidth already taken by the shortfall.
5. **Rate the load.** High when the ask lands in a tight period and demands two or more things to remember, or any calculation or comparison; medium when one of those holds; low when neither. State the rating's confidence (observed calendar or assumed) and say that the rubric is a judgment aid from this skill's author, not a validated scale.
6. **Recommend, in this order:** move the ask to a slack period, usually just after an inflow; simplify it (remove the calculation, set a default, let the program hold the memory); split it (enroll now, decide the details later); and only then add reminders, because a reminder is one more demand on the same bandwidth. If the program controls a payment or transfer, consider timing it to arrive when the constraint binds, as Kaur et al. did with pay.
7. **Say whether the real constraint is money.** If the calendar shows the household lacks the money for the behavior at every point in the cycle, write that the fix is money or eligibility, not timing or design, and escalate rather than recommending a simpler form.
8. **Stop here;** `choose-delivery-moment` picks the moment using this load map, and `draft-lever-content` writes the ask.

See `references/worked-example.md` for a complete run on a commitment-savings enrollment drive in Butuan, Philippines.

## Output template

```markdown
# Scarcity load assessment

**Behavior:** <who, what, when, carried over verbatim>
**The ask as experienced:** <arrives when, via what, deadline; requires having / remembering / calculating / comparing / deciding: list each>

## Income and expense calendar
| Period | Inflows (source, timing, reliability) | Predictable outflows | Participants call it | Source of this row |
|---|---|---|---|---|
| <month or season> | <...> | <...> | tight / normal / slack | <interviews / audience brief / assumed> |

## Where the ask lands
<the period; what else competes for money and attention then; whether this differs by subgroup, and for whom>

## Demands of the ask
| Demand | Count and list | Could the program hold it? |
|---|---|---|
| Things to remember | <n: ...> | <pre-fill / reminder / no> |
| Calculations | <n: ...> | <default / staff / no> |
| Options to compare | <n: ...> | <...> |
| Deadlines | <n: ...> | <...> |

## Load rating
**<low / medium / high>** for <subgroup>, because <financial tightness at the moment> and <memory and decision demands>. Confidence: <observed calendar / assumed>. Rubric: judgment aid, not a validated scale.

## Recommendations, in order
1. Move: <to which period, and why>
2. Simplify: <which demand the program takes over>
3. Split: <what is asked now, what later>
4. Remind: <only if 1 to 3 are done; what and when>
5. If the program controls a payment: <time it to arrive when ...>

## Is the real constraint money?
<yes / no / partly, with the calendar evidence; if yes, what this skill cannot fix and who decides>

## What to check before relying on this
- <the calendar row that is assumed>
- <the subgroup the rating may not fit>
```

## Where it goes wrong

- **Calling it "scarcity" without a calendar.** Scarcity is a claim about a shortfall that varies over time; a high rating with no mapped calendar is a stereotype of poor people as permanently overwhelmed, and it points to the wrong fix.
- **Quoting the lab effects.** The 2013 lab-priming results are contested and the Mani effect size is unverified in the dossier; do not quote one. Lean on the field evidence (Kaur et al.) and on the local calendar.
- **Designing around a money problem.** If the household cannot pay for the behavior at any point in the cycle, a simpler form changes nothing. Say so and escalate.
- **Treating the calendar as uniform.** Farmers and shopkeepers in the same village have different tight periods. A single rating for "the community" hides the subgroup the ask fails for.
- **Over-reminding.** Adding reminders to an ask that is already heavy at a tight moment adds a demand; reminders come last in the order, after moving, simplifying, and splitting.
- **Picking the moment.** This skill produces the load map. The delivery moment is `choose-delivery-moment`'s call, with other inputs (landmarks, channel, habit) this skill does not weigh.

## When to bring in a specialist

Tell the user to consult program leadership, an economist, or a consumer-protection or clinical specialist when:
- The calendar shows the household lacks the money for the behavior at every point in the cycle; the decision is about transfer size, price, credit, or eligibility, and belongs to program leadership and an economist, not to a design fix
- The ask concerns debt, a loan, insurance, or a health decision made during a crisis; a consumer-protection or clinical specialist should review whether simplifying the ask removes a safeguard
- The team wants to move the timing of a cash transfer or wage on the strength of this assessment; an economist or evaluator should design that change, since the field evidence is one experiment in one setting

Bring them: the calendar with its sources, the demands table, the load rating by subgroup, and the "Is the real constraint money?" answer.
