# Evidence notes: estimate-cost-effectiveness

Every source below is taken from `docs/plan/2026-10-skill-expansion-dossier.md` (compiled 2026-10-12), with the dossier's verification tag carried over. Nothing has been added from memory, and no number appears here that the dossier does not give.

## Anchor sources

### Dhaliwal, Duflo, Glennerster & Tulloch (2013), in *Education Policy in Developing Countries* (pp. 285–338), University of Chicago Press [verified-crossref]
- https://doi.org/10.7208/chicago/9780226078854.003.0008
- The comparative cost-effectiveness approach for development programs: ingredients-based costing, a stated perspective, a common currency year and discount rate, cost divided by effect in a common unit, and the comparison presented with its assumptions.
- What it supports: the whole procedure. No effect sizes or cost figures from the chapter are given in the dossier, and none are quoted.

### J-PAL, *Conducting cost-effectiveness analysis (CEA)* (Bhula, Mahoney & Murphy) [verified-fetch: https://www.povertyactionlab.org/resource/conducting-cost-effectiveness-analysis-cea]
- Fetched page. Quotable per the dossier: "A ten percent discount rate is applied for costs incurred over multiple years"; it counts "the monetary value of both cash and in-kind transfers"; it links costing guidelines and a template.
- What it supports: the default discount rate, the transfers line, and the impact-per-$100 convention named in the dossier's boundary conditions. The dossier notes the page has no dedicated sensitivity section and points to a guide on key decisions and assumptions; the sensitivity rows in the skill are the drafter's operationalization.

### Kraft (2020), *Educational Researcher* 49, 241–253 [verified-crossref]
- https://doi.org/10.3102/0013189X20912798
- Cited in the dossier for interpreting magnitude: effect sizes are to be read alongside cost and scalability. The dossier's note from the `estimate-expected-effect` entry: Kraft's benchmarks are US education RCTs.
- What it supports: the instruction that a per-SD effect needs its cost beside it. No benchmark values are quoted, and the skill says the benchmarks are not applied to LMIC programs.

### Banerjee, Duflo, Glennerster & Kothari (2010), *BMJ* 340, c2220 [verified-crossref]
- https://doi.org/10.1136/bmj.c2220 (full citation from the dossier's `audit-process-friction` entry).
- Clustered RCT, rural Rajasthan, India: immunization camps with and without small in-kind incentives. Cost per fully immunized child fell from $55.83 to $27.94 when incentives were added. The dossier's `design-incentive-scheme` entry adds: full immunization 39% with camps plus lentils, 18% with camps alone, 6% in control; RR 6.7 versus control.
- What it supports: the worked LMIC number and the point that spreading a fixed cost over more outcomes lowers the ratio.

### Kettle, Hernandez, Ruda & Sanders (2016), World Bank Policy Research Working Paper 7690 [verified-crossref]
- https://doi.org/10.1596/1813-9450-7690 (full citation from the dossier's `write-social-norm-message` entry; a 2017 book-chapter version exists at https://doi.org/10.1596/978-1-4648-1120-3_ch2 [verified-crossref]).
- Guatemala tax-compliance letters: the dossier's number for this skill is "about 36 times the letter cost".
- What it supports: a second LMIC cost figure; it is a return ratio (revenue against letter cost), closer to a benefit-cost figure than a cost per unit of behavior, and the skill presents it only as an example of a cost line reported beside an effect.

## Other numbers in the dossier entry

- Haryana, India: +9.1% immunizations per dollar for information hubs plus SMS. The dossier marks this "secondary source per report" (a J-PAL page); the experiment is Banerjee et al. (2025), *Econometrica* 93(4), 1183–1223, https://doi.org/10.3982/ECTA19739 [verified-crossref]. Not quoted in the skill because it is a secondary-source figure and the dossier records no primary number.

## Cross-cutting cautions (dossier section A)

- A4. DellaVigna & Linos (2022), *Econometrica* 90(1), 81–116, https://doi.org/10.3982/ECTA18709 [verified-crossref]: academic journal studies average 8.7 percentage points, nudge-unit trials 1.4 points; about 70% of the gap is selective publication combined with low power.
- A9. Ferraro & Tracy (2022), *Experimental Economics* 25(5), 1441–1466, https://doi.org/10.1007/s10683-022-09754-x [verified-crossref]: loss-framed incentive contracts pooled 0.16 SD, 0.33 SD in the lab versus 0.02 SD in the field.
- Why they matter here: a cost per outcome computed on a published effect inherits that shrinkage; this is why the skill takes the discounted effect from `estimate-expected-effect` when the effect is transferred and keeps the published figure in the sensitivity table.

## Non-WEIRD evidence

- India (Rajasthan): Banerjee et al. (2010), above.
- Guatemala: Kettle et al. (2016), above.
- India (Haryana): secondary-source figure, above, not quoted.
- The dossier describes the method itself as LMIC-native (J-PAL comparative CEA).

## Known corrections, gaps, and unverified items

- Replication status in the dossier: "treatment of transfers and discount rates is contested"; the skill shows the ratio with and without transfers and names its rate rather than fixing a rule.
- The dossier gives no reason for the 10% rate; the skill presents it as the J-PAL convention and asks the user to state their own reason.
- The sensitivity rows are the drafter's operationalization; the J-PAL page has no dedicated sensitivity section.
- The categories in the ingredients table (staff time, materials, transport, equipment, space, training, monitoring, participant time) follow the drafting brief and standard ingredients practice; the dossier does not list categories, so the list is not attributed to a source.
- Kraft's benchmark values are not in the dossier and are not quoted.
- The "cost per percentage point per 1,000 people" ratio is a reporting convenience added by the drafter, not a J-PAL convention.

## What to check locally

1. Which inputs the program used without paying for them, and the local wage or rental value of each.
2. Whether the effect is from this program's own trial or from a study elsewhere; if elsewhere, whether `estimate-expected-effect` has discounted it.
3. The comparator programs' costing: perspective, treatment of transfers, currency year, and whether staff time was priced.
4. The funder's conventions for currency year, exchange or PPP, and discount rate.
5. The share of delivery cost that is fixed (training, equipment, set-up) and would fall per person at scale.
6. Whether the outcome measure (pill count, register, self-report) matches the comparator's.
