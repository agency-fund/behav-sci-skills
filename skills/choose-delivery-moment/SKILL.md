---
name: choose-delivery-moment
description: >-
  Use when the intervention is chosen and the question is when to deliver it:
  "when should we make the offer", "before or after harvest or payday", "is
  new year or Ramadan a good time to launch". Also use when a team is about to
  schedule an ask by its own calendar (a quarter start, a staff visit) without
  checking when the audience has cash, attention, and a natural window.
  Produces a timing plan: the income and expense calendar, local temporal
  landmarks with their cash position, the chosen moment with its mechanism
  (liquidity, salience, or slack attention), a deadline rule, an equity check,
  and what to test, drawing on harvest-timed offers in Kenya (Duflo, Kremer
  and Robinson), the fresh-start effect, and EAST. Do not use when the
  question is how many messages and how often; use design-reminder-schedule
  instead. Not for writing the message (draft-lever-content), locking money
  until a date (design-commitment-device), or diagnosing when financial stress
  peaks (assess-scarcity-load).
license: CC-BY-4.0
metadata:
  title: Pick the moment to deliver an ask
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: mixed-evidence
  tags: "scarcity, choice-architecture, behavior-change-techniques"
  consumes: "intervention-levers, audience-context-brief"
  produces: ""
---

## What it does

Chooses the moment to deliver one ask: the point in the audience's calendar where cash is present, attention is free, the behavior naturally falls due.

Three mechanisms are in play, and the output names which one the chosen moment rests on. Liquidity: cash from a harvest, a payday, or a transfer is still there before it is spent. Salience: a temporal landmark (a new year, a term start, a harvest) gives a reason to act now rather than later. Slack attention: financial strain consumes attention, so an ask that needs thought should land in a slack period. The output is a timing plan, not the message and not its cadence.

## When to use it

### Use it when
- A lever has been chosen and someone asks "when should we make the offer?", "which month should this run?", or "before or after harvest (or payday, or the transfer)?"
- A team is about to schedule an ask by its own calendar (the quarter start, the next staff visit, when the budget lands) without checking when the audience has cash and attention
- Someone proposes a launch date because it feels meaningful ("start at new year", "right after Ramadan") and the team needs to know whether that moment has cash and evidence behind it
- An offer worked once and failed when repeated later in the season, and the team suspects the moment, not the offer, carried the effect

### Do not use it when
- The question is how many messages to send, how often, and when to stop; that is `design-reminder-schedule`, which takes the moment chosen here as its anchor
- The team wants to lock money or a decision until a date; that is `design-commitment-device`. This skill may recommend a short deadline, never a penalty or a lock
- The question is when financial stress peaks for this population and what it does to their decisions; that is `assess-scarcity-load` (diagnose stage), whose load map this skill consumes
- The team needs the words of the message or script; that is `draft-lever-content`, which takes the timing line from this plan
- No lever has been chosen yet; run `select-intervention-levers` first, because the moment depends on what is being asked and what it costs

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The ask: who does what, from the intervention lever brief or stated directly, and what it costs the person at the moment of action (cash outlay, time away from work, attention). An ask with no cost at the moment of action has little to time.
2. **Required.** The behavior's natural window: when it must happen (planting), when it can only happen (an enrollment period), or whether a clinic schedule or an administrative deadline fixes it. If the window is fixed, this skill only places the ask inside it.
3. **Required.** The audience's income and expense calendar: when cash arrives (harvest sales, payday, remittances, transfer disbursement) and when the large expenses fall (school fees, festivals, lean-season food, debt repayment). An audience and context brief from `map-audience-context` or a load map from `assess-scarcity-load` supplies part of this.
4. Optional. The temporal landmarks the field team considers meaningful locally (which new year, which religious calendar, term dates, harvest festivals) and the channel's own constraints (when an SMS can go, when agents visit).
5. Optional. Whether present bias (preferring a smaller reward now over a larger one later, against one's own plan) is among the confirmed barriers. This decides whether a deadline is attached.

If 1 or 2 is missing, ask and stop. If 3 is missing, ask once; if the answer is still thin, proceed with every calendar row marked "assumed, confirm with field team". If 4 is missing, use only landmarks the user named; do not fill the table from general knowledge of the country. If 5 is missing, attach no deadline and list it as an option to test.

## What it draws on

- Duflo, E., Kremer, M., & Robinson, J. (2011). Nudging farmers to use fertilizer: Theory and experimental evidence from Kenya. *American Economic Review*, 101(6), 2350–2390. https://doi.org/10.1257/aer.101.6.2350
- Dai, H., Milkman, K. L., & Riis, J. (2014). The fresh start effect: Temporal landmarks motivate aspirational behavior. *Management Science*, 60(10), 2563–2582. https://doi.org/10.1287/mnsc.2014.1901
- Karlan, D., McConnell, M., Mullainathan, S., & Zinman, J. (2016). Getting to the top of mind: How reminders increase saving. *Management Science*, 62(12), 3393–3411. https://doi.org/10.1287/mnsc.2015.2296
- Kaur, S., Mullainathan, S., Oh, S., & Schilbach, F. (2025). Do financial concerns make workers less productive? *The Quarterly Journal of Economics*, 140(1), 635–689. https://doi.org/10.1093/qje/qjae038
- Behavioural Insights Team (2014; revised and updated edition). *EAST: Four simple ways to apply behavioural insights*, "Make it timely". https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709
- Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity: A meta-analysis and a real-effort experiment. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x

Duflo, Kremer and Robinson is the anchor. Among 1,230 maize farmers in Western Kenya, a small, time-limited offer of free fertilizer delivery made right after harvest raised fertilizer use by 14 percentage points on a base of 24% in the first season and by 18 points on a base of 26% in the second; discounts offered later in the season worked less well. The dossier records conceptual support from the commitment-device literature for the mechanism: harvest cash that is present now is gone by planting, so an offer that arrives while the cash is there, with a deadline, lets a farmer who intends to buy act before the intention lapses. Dai, Milkman and Riis supply the salience mechanism: diet searches, gym visits, and commitment contracts rise after temporal landmarks; this is archival US data with no experiment and no meta-analysis. Karlan and colleagues found that reminders in Bolivia, Peru, and the Philippines raised savings-goal attainment, most when the message named the goal and the incentive (effect size unverified in the sources this skill draws on). Kaur and colleagues, among piece-rate workers in India, found that paying earlier raised output by 7% (0.11 SD) and reduced costly mistakes, concentrated among the most financially constrained: strain itself consumes attention. EAST's "Timely" is the practitioner summary. The judgment calls this skill adds are the three-way overlap test (cash, attention, window), the rule that every landmark is scored by its cash position, and the rule that a deadline needs a present-bias diagnosis.

Discount published effects before planning on them. Academic journal trials average 8.7 percentage points where nudge-unit trials average 1.4 (DellaVigna and Linos, 126 RCTs, 23 million people; about 70% of the gap is selective publication and low power), and a loss-framing effect of 0.33 SD in the lab was 0.02 SD in the field (Ferraro and Tracy). The Kenyan numbers above come from one field trial, so they need less shrinkage than a lab effect, but a program that plans on 14 to 18 points without a local pilot is planning on the best case. Hand them to `estimate-expected-effect` for a benchmark.

**WEIRD skew:** The fresh-start evidence is entirely US and archival (search data, gym visits, a commitment website), so which calendar landmarks feel like new beginnings where you work is a local question, not a finding. The liquidity evidence is from low- and middle-income settings. **Non-WEIRD evidence:** Kenya (Duflo, Kremer and Robinson; 1,230 maize farmers; +14 and +18 points from a post-harvest, time-limited offer); India (Kaur and colleagues; piece-rate workers; +7% output from earlier pay); Bolivia, Peru, and the Philippines (Karlan and colleagues; reminder timing; effect size unverified). No non-WEIRD test of the fresh-start effect was found in the sources this skill draws on. A user elsewhere should build the calendar from the field team, not from a national almanac, and should treat any landmark frame as untested.

**Replication status:** Mixed. Harvest timing rests on a single RCT with conceptual support from the commitment-device literature; the fresh-start effect is archival only, with no meta-analysis and no field experiment in the sources this skill draws on; reminder timing is replicated across three countries with unverified magnitudes; the pay-timing result is one strong field experiment.

## How to do it

1. **Carry the ask over verbatim** and write what it costs the person at the moment of action: cash, time, attention. The cost decides which mechanism matters; a free two-minute ask is timed for attention, a purchase is timed for cash.
2. **Build the income and expense calendar** as a table of periods with cash in, cash out, and a net position (flush, trough, neutral), citing the source of each row. Use the load map from `assess-scarcity-load` if there is one. Mark anything the field team has not confirmed as assumed.
3. **List the temporal landmarks** the user or field team named, with dates and the cash position of each, because a landmark on a cash trough (a festival, a term start with fees due) supplies the frame without the means. Do not add landmarks from general knowledge.
4. **Locate the behavior's natural window:** when it must happen, when it can only happen, or "any time". If a clinic or an administrative rule fixes it, the window is set and the choice is where inside it to place the ask.
5. **Choose the moment where cash, attention, and the window overlap.** Name the mechanism it rests on (liquidity, salience, slack attention) and the evidence for that mechanism, saying how far it transfers: harvest timing is one strong Kenyan RCT; fresh start is US archival only. List the moments rejected and why.
6. **Decide the deadline rule.** Attach a short deadline only if present bias is a confirmed barrier, because the Kenyan offer was time-limited for that reason and a deadline otherwise only excludes people who needed more time. State how long it runs and what happens after it.
7. **Run the equity check:** who has no cash or no attention at the chosen moment (the landless, the recently paid, the migrant, the household with fees due) and what the fallback moment for them is.
8. **Write what to test:** the chosen moment against the program's default moment, same offer, with the outcome and who runs it. Then stop here; `design-reminder-schedule` sets the cadence around this moment and `draft-lever-content` writes the words.

See `references/worked-example.md` for a complete run on latrine construction in Indonesian CLTS villages and `references/evidence-notes.md` for the sources with their verification state.

## Output template

```markdown
# Delivery moment plan

**The ask:** <who does what, carried over verbatim; what it costs the person at the moment of action: cash, time, attention>
**Confirmed barrier:** <from the lever brief; say whether present bias is among the confirmed barriers>

## Income and expense calendar
| Period | Cash in | Cash out | Net position | Source |
|---|---|---|---|---|
| <month or season> | <harvest sale, payday, transfer> | <school fees, festival, lean-season food, debt> | <flush / trough / neutral> | <field team / audience-context brief / assumed> |

## Temporal landmarks
| Landmark | Date(s) | Cash position | Frame it offers | Evidence |
|---|---|---|---|---|
| <landmark named by the field team> | <date> | <flush / trough> | <"new season", "new term", "after the festival"> | <untested here / fresh-start is US archival only> |

## The behavior's natural window
<when it must or can only happen; whether a clinic, a season, or an administrative deadline fixes it; "any time" if nothing does>

## Chosen moment
- **When:** <date or event, stated relative to the landmark or window, e.g. "within 14 days of the main harvest sale">
- **Mechanism:** <liquidity / salience / slack attention; the one or two this moment rests on>
- **Evidence it rests on:** <which study, and how far it transfers to this setting>
- **Rejected moments:** <each, with the reason: cash trough, outside the window, attention taken>

## Deadline rule
<a deadline only if present bias is confirmed: how long, what happens after; otherwise "no deadline, because ...">

## Equity check
<who has no cash or attention at this moment; the fallback moment for them>

## What to test
<chosen moment vs the program's default moment, same offer; the outcome; who runs it; hand to design-reminder-schedule for cadence>

## What to check before relying on this
- <the calendar row most likely to be wrong>
- <the landmark whose local meaning is unconfirmed>
```

## Where it goes wrong

- **Fresh start as a universal.** Treating "new year" or "after Ramadan" as a proven motivational moment in a setting where the only evidence is US search and gym data. Enter the landmark as a hypothesis in the table with "untested here" in the evidence column; the Kenyan evidence is about cash, not calendars.
- **Landmark on a cash trough.** New year, Eid, Christmas, and term start are often the largest expense moments of the year. A frame with no cash behind it moves nobody who needs cash to act, which is why the landmark table carries a cash-position column.
- **Timing a supply problem.** If the fertilizer is not in stock or the clinic is closed, no moment works. Check the lever brief's barrier before building a calendar; a supply barrier goes back to `select-intervention-levers`.
- **Deadline by reflex.** Attaching a short deadline because the Kenyan offer had one, without a present-bias diagnosis. A deadline excludes everyone who needed more time and cannot buy it back; the deadline rule must cite the barrier that justifies it.
- **Inventing a calendar.** Filling the calendar and landmark tables from general knowledge of a country rather than from the field team. Harvest dates vary by crop and district, pay cycles by employer, and religious dates by year; every row carries its source, and "assumed" rows are flagged for confirmation.
- **Drifting into cadence.** Specifying how many reminders and at what interval. That is `design-reminder-schedule`; this skill delivers one anchor moment and stops.

## When to bring in a specialist

Tell the user to consult the relevant specialist when:
- The behavior's window is clinically fixed (immunization due dates, antenatal visits, a medication course); a clinician sets the window, and this skill only places the ask inside it
- The chosen moment uses a religious landmark or a fasting period as its frame; local faith or community leaders and a local researcher should confirm the frame is welcome and the ask is appropriate in that period
- The ask is a financial product (a loan, input credit, an insurance premium) timed to the moment of greatest liquidity for poor households; the moment that maximizes take-up also maximizes over-commitment, so a consumer-protection or financial-inclusion specialist reviews it, alongside `audit-intervention-ethics`
- The calendar cannot be built with confidence (several crops, migration, irregular casual pay); the field team or a local economist builds it from data before a moment is chosen

Bring them: the calendar table with its sources, the landmark table, the chosen moment with its mechanism, the deadline rule, and the equity check.
