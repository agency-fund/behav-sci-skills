# Evidence notes: design-incentive-scheme

Every source below is taken from `docs/plan/2026-10-skill-expansion-dossier.md` (compiled 2026-10-12), with the dossier's verification tag carried over. Nothing has been added from memory, and no number appears here that the dossier does not give.

## Anchor sources

### Baird, Ferreira, Özler & Woolcock (2014), *Journal of Development Effectiveness* [verified-crossref]
- https://doi.org/10.1080/19439342.2014.890362 (volume, issue, and pages not given in the dossier).
- Systematic review of cash-transfer programs and schooling: 35 studies (75 reports). Unconditional or unmonitored transfers raised the odds of enrollment by 18 to 25%; explicitly monitored conditional transfers raised them by about 60%; test-score effects small at best.
- What it supports: the monitoring decision (step 5) and the caution that incentives move the rewarded action more than the outcome behind it. The effects are odds ratios, not percentage points.

### Mantzari et al. (2015), *Preventive Medicine* [verified-crossref]
- https://doi.org/10.1016/j.ypmed.2015.03.001 (co-authors, volume, and pages not given in the dossier).
- Systematic review and meta-analysis of personal financial incentives for habitual health behaviors: 34 RCTs. OR 1.53 for outcomes up to 18 months; OR 2.11 three months after the incentive ended; larger under high deprivation (OR 2.17).
- What it supports: the expectation that effects are larger among the deprived (and so the coercion check), and the removal plan. The dossier does not record where the trials ran.

### Gneezy, Meier & Rey-Biel (2011), *Journal of Economic Perspectives* 25(4), 191–210 [verified-crossref]
- https://doi.org/10.1257/jep.25.4.191
- Review of when and why incentives fail to modify behavior: crowding out of intrinsic motivation; effects often dissipate after the incentive is removed.
- What it supports: the crowding-out check (step 7) and the removal plan (step 6). No numbers are quoted from it in the dossier.

### Banerjee, Duflo, Glennerster & Kothari (2010), *BMJ* 340, c2220 [verified-crossref]
- https://doi.org/10.1136/bmj.c2220
- Clustered RCT, rural Rajasthan, India. Full immunization: 39% with reliable camps plus small in-kind incentives (lentils), 18% with reliable camps alone, 6% in control; RR 6.7 versus control. Cost per fully immunized child fell from $55.83 to $27.94 with incentives.
- What it supports: the supply check (the camps came first), in-kind as a form, the small size relative to the hassle, and the cost line. The same numbers appear in the dossier's `estimate-cost-effectiveness` and `audit-process-friction` entries.

### Gibson et al. (2017), *The Lancet Global Health* 5(4), e428–e438 [verified-crossref]
- https://doi.org/10.1016/S2214-109X(17)30072-4
- M-SIMU cluster RCT, Kenya: SMS reminders plus incentives improved childhood immunization coverage and timeliness in a high-coverage setting. Effect size unverified in the dossier.
- What it supports: incentives paired with reminders; direction only. Full citation taken from the dossier's `design-reminder-schedule` entry.

### Banerjee, Chandrasekhar, Dalpath, Duflo, Floretta, Jackson et al. (2025), *Econometrica* 93(4), 1183–1223 [verified-crossref]
- https://doi.org/10.3982/ECTA19739 (NBER w28726, https://doi.org/10.3386/w28726 [verified-crossref]).
- Haryana, India, large-scale immunization experiment. Incentives plus ambassadors plus SMS raised immunizations 44% (J-PAL page, secondary source per the report). SMS reminders alone had no impact (from the `design-reminder-schedule` entry).
- What it supports: an incentive as one part of a bundle; the number is a secondary-source figure and is marked as such in the skill.

## Cross-cutting cautions (dossier section A)

- A4. DellaVigna & Linos (2022), *Econometrica* 90(1), 81–116, https://doi.org/10.3982/ECTA18709 [verified-crossref]. 126 RCTs, 23 million people. Academic journal studies average 8.7 percentage points (+33.4%); nudge-unit trials average 1.4 points (+8.0%). About 70% of the gap is selective publication combined with low power.
- A9. Ferraro & Tracy (2022), *Experimental Economics* 25(5), 1441–1466, https://doi.org/10.1007/s10683-022-09754-x [verified-crossref]. Loss-framed incentive contracts: pooled 0.16 SD; 0.33 SD in the lab versus 0.02 SD in the field, with publication bias among lab studies. Directly relevant here, since loss-framed incentives are an incentive design.
- The dossier's instruction for every technique skill: published lab or academic effects should be discounted when transferred.

## Non-WEIRD evidence

- India: Rajasthan (Banerjee et al. 2010) and Haryana (Banerjee et al. 2025), above.
- Kenya: M-SIMU (Gibson et al. 2017), above; effect size unverified.
- Baird et al.: the countries of the reviewed cash-transfer programs are not listed in the dossier.
- Mantzari et al. and Gneezy et al.: settings not recorded in the dossier.

## Known corrections, gaps, and unverified items

- Lottery evidence: the design report's lottery meta-analyses (certain ES 0.55 versus uncertain 0.17; a 35-RCT network meta-analysis with lottery RR 1.43) have unverified authors. The dossier says do not cite them; the skill does not.
- The US "regret lottery" (Philadelphia) with no pooled effect is stated in the dossier's boundary-conditions line without a citation; the skill carries it as unverified, author to confirm.
- Haryana "+44%" is a secondary-source figure (J-PAL page); the dossier's J-PAL Rajasthan and Haryana pages have no URLs and are not cited.
- Mantzari: the dossier's wording is "OR 1.53 up to 18 months and OR 2.11 three months after the incentive ended"; the skill quotes it as written and does not interpret the ordering.
- Baird: the 18 to 25% and 60% figures are changes in the odds of enrollment, not percentage points; the skill says so.
- The sizing rule (a multiple of the hassle cost and a share of daily income) is the drafter's operationalization of "set the amount relative to the hassle"; the dossier gives no threshold, and the skill names none.
- No verified source in the dossier on incentives for public servants; the escalation for that case rests on the crowding-out review and on fairness reasoning, not on a quoted trial.

## What to check locally

1. Whether the behavior can be verified by someone other than the recipient, and what one verification costs in staff time.
2. Whether supply is reliable: stock, staff, opening hours, before any reward is attached.
3. Daily income and the hassle cost (fare, lost wages, fees) for this subgroup, from the field team, so the amount can be written as a multiple and a share.
4. Whether cash to households is acceptable here or in-kind is preferred, and whether the in-kind good is one the household values.
5. Whether recipients include volunteers, health workers, or officials, and whether paying them is legal.
6. Whether an intrinsic, religious, or prosocial motive already carries the behavior for some people.
7. Who the condition would exclude, and whether the program can accept that.
8. Whether the budget reaches the end date, and what follow-up measure will show decay after removal.
