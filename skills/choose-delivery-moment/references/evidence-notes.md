# Evidence notes: choose-delivery-moment

Every source below is taken from `docs/plan/2026-10-skill-expansion-dossier.md` (compiled 2026-10-12), with the dossier's verification tag carried over. Nothing has been added from memory, and no number appears here that the dossier does not give. Where the dossier says a magnitude is unverified, it stays unverified.

## Anchor sources

### Duflo, Kremer & Robinson (2011), *American Economic Review* 101(6), 2350–2390 [verified-crossref]
- https://doi.org/10.1257/aer.101.6.2350 (also NBER w15131, https://doi.org/10.3386/w15131 [verified-crossref]).
- Field RCT, Western Kenya, 1,230 maize farmers. A small, time-limited free-delivery offer for fertilizer made right after harvest raised fertilizer use by 14 percentage points (base 24%) in season 1 and 18 points (base 26%) in season 2. Discounts offered later in the season worked less well.
- What it supports in the skill: the liquidity mechanism (deliver the ask while harvest cash is still present) and the deadline rule (the offer was time-limited). The dossier records "conceptual support from the commitment literature" for the mechanism; the skill does not quote any number for the later-season arms because the dossier gives none.
- The dossier's `audit-process-friction` entry also uses this trial for the "small hassle cost of travel" framing (Datta & Mullainathan on Duflo, Kremer & Robinson).

### Dai, Milkman & Riis (2014), *Management Science* 60(10), 2563–2582 [verified-crossref]
- https://doi.org/10.1287/mnsc.2014.1901
- Archival evidence only: diet-related searches, gym visits, and commitment contracts (stickK) rise after temporal landmarks. No experiment, no meta-analysis, US data.
- What it supports: the salience mechanism, as a hypothesis. The dossier instructs: do not generalize the fresh-start effect to LMIC calendars without saying it is untested there. The skill's landmark table therefore carries an evidence column defaulting to "untested here".

### Karlan, McConnell, Mullainathan & Zinman (2016), *Management Science* 62(12), 3393–3411 [verified-crossref]
- https://doi.org/10.1287/mnsc.2015.2296
- Field experiments in Bolivia, Peru, and the Philippines. Reminders raised savings-goal attainment; messages naming the goal plus the incentive worked best; loss versus gain framing made no difference. Effect size unverified in the dossier.
- What it supports: timing a prompt to the goal it serves (attention at the moment that matters). Cadence belongs to `design-reminder-schedule`, whose dossier entry is the fuller record of this paper.

### Kaur, Mullainathan, Oh & Schilbach (2025), *Quarterly Journal of Economics* 140(1), 635–689 [verified-crossref]
- https://doi.org/10.1093/qje/qjae038 (NBER w28338, https://doi.org/10.3386/w28338 [verified-crossref]; published-version details from the NBER page; audit year 2024, online-first).
- Field experiment with low-income piece-rate manufacturing workers in India. Paying workers earlier raised output by 7% (0.11 SD) and reduced costly, unintentional mistakes; effects concentrated among the most financially constrained (NBER abstract, fetched).
- What it supports: the slack-attention mechanism. This citation is taken from the dossier's `assess-scarcity-load` entry, not from the `choose-delivery-moment` entry; the orchestrator's note allowed it if the dossier includes it, and it does.

### Behavioural Insights Team, *EAST* (2014; revised and updated edition) [verified-fetch: https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf]
- "Make it timely" chapter. Practitioner checklist, no effect sizes. The PDF at this URL is the revised edition, whose preface dates the original to 2014; no individual authors on the cover. The revised edition flags studies that "have not held up to scrutiny".
- What it supports: the practitioner framing only. It is not evidence for any specific moment.

## Cross-cutting cautions (dossier section A)

- A4. DellaVigna & Linos (2022), *Econometrica* 90(1), 81–116, https://doi.org/10.3982/ECTA18709 [verified-crossref]. 126 RCTs, 23 million people. Academic journal studies average 8.7 percentage points (+33.4%); nudge-unit trials average 1.4 points (+8.0%). About 70% of the gap is explained by selective publication combined with low power.
- A9. Ferraro & Tracy (2022), *Experimental Economics* 25(5), 1441–1466, https://doi.org/10.1007/s10683-022-09754-x [verified-crossref]. Loss-framed incentives: pooled 0.16 SD, but 0.33 SD in the lab versus 0.02 SD in the field, with publication bias among lab studies.
- The dossier's instruction for every technique skill: these two patterns point the same way; published lab or academic effects should be discounted when transferred. The Kenyan trial is a field RCT, so the discount is smaller than for a lab effect, but a single trial is still a best case until a local pilot runs.

## Non-WEIRD evidence

- Kenya: Duflo, Kremer & Robinson (above). The only field RCT in this entry on timing an offer to the income calendar.
- India: Kaur et al. (above). Pay timing and attention, not an offer.
- Bolivia, Peru, Philippines: Karlan et al. (above). Reminder timing; effect size unverified.
- Fresh-start effect: no non-WEIRD test found in the sources this skill draws on.

## Known corrections, gaps, and unverified items

- The local landmark list in the skill (new year including local calendars, Ramadan or Eid, school term, harvest, birthdays, payday) is procedure from the planning report, not evidence. The dossier says so explicitly.
- The dossier's "practitioner sources" line mentions a J-PAL Kenya fertilizer evaluation page with no URL; it is not cited in the skill.
- No backfire study was found for delivery timing in the sources this skill draws on. The equity risk the skill names (a deadline or a cash-timed offer excluding people without cash at that moment) is the drafter's reasoning from the mechanism, not a documented harm. The one documented failure is a timing miss: later discounts worked less well.
- Karlan et al. magnitudes: unverified in the dossier; the skill quotes the direction only.
- Kaur et al. is published 2025 in print; the audit records 2024 online-first.

## What to check locally

1. The income calendar: when cash actually arrives for this subgroup (main and secondary harvest, pay cycle, transfer date, remittance pattern), from the field team or administrative data, not from a national almanac.
2. The expense calendar: fees, festivals, lean season, debt repayment dates, and which of them coincide with the landmarks the team is considering.
3. Whether the landmark the team likes is a cash flush or a cash trough for this audience.
4. Whether any landmark has local meaning as a new beginning at all; the fresh-start effect is untested outside the US.
5. Whether present bias is a confirmed barrier (from the diagnosis), before any deadline is attached.
6. The behavior's natural window, confirmed with whoever fixes it (agronomist, clinic, registrar).
7. Who has no cash at the chosen moment (landless laborers, households with fees due) and whether the fallback moment reaches them.
