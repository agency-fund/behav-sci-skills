# Evidence notes: estimate-expected-effect

Every item below comes from `docs/plan/2026-10-skill-expansion-dossier.md` (entry `estimate-expected-effect`, section A, bench entry E12). The verification tag is the dossier's. Nothing has been upgraded or added from memory; numbers are quoted only as the dossier writes them.

## Anchor sources

**Mertens, S., Herberz, M., Hahnel, U. J. J., & Brosch, T. (2022). The effectiveness of nudging: A meta-analysis of choice architecture interventions across behavioral domains. *PNAS*, 119(1). https://doi.org/10.1073/pnas.2107346118** [verified-crossref] (audit year 2021, online-first)
- d = 0.45 (95% CI 0.39–0.52) per the abstract; some secondary sources say 0.43. More than 200 studies, more than 450 effect sizes, N ≈ 2.15 million.
- "Structure" interventions (defaults, choice-set changes) beat "description" and "assistance" interventions; food is the most responsive domain. Moderate publication bias.
- Correction recorded in the dossier: the plan's "d ≈ 0.43" is a secondary figure; quote 0.45.

**Maier, M., Bartoš, F., Stanley, T. D., Shanks, D. R., Harris, A. J. L., & Wagenmakers, E.-J. (2022). No evidence for nudging after adjusting for publication bias. *PNAS*. https://doi.org/10.1073/pnas.2200300119** [verified-crossref]
- RoBMA bias-corrected average about d = 0.04 for the same literature. Critics and a rejoinder note the average hides heterogeneity.

**Szaszi, B., et al. (2022). No reason to expect large and consistent effects of nudge interventions. *PNAS* (letter). https://doi.org/10.1073/pnas.2200732119** [verified-crossref] (first author, year, title confirmed; co-authors not captured by the audit)
- Bias-adjusted range d ≈ 0.03–0.31; the average is misleading given heterogeneity.

**DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709** [verified-crossref]
- 126 RCTs, 23 million people. Academic journal studies average 8.7 percentage points (+33.4%); nudge-unit trials average 1.4 points (+8.0%). About 70% of the gap is explained by selective publication combined with low power.
- Two US nudge units only. The ratio "about six" used in SKILL.md is this skill's arithmetic (8.7 / 1.4), not a figure the paper reports.

**Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity: A meta-analysis and a real-effort experiment. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x** [verified-crossref] (DOI located in the audit)
- Pooled 0.16 SD; 0.33 SD in the lab versus 0.02 SD in the field; publication bias among lab studies. The dossier's designated lab-to-field shrinkage example; it is about loss framing, not a general constant.

**Hummel, D., & Maedche, A. (2019). How effective is nudging? A quantitative review on the effect sizes and limits of empirical nudging studies. *Journal of Behavioral and Experimental Economics*, 80, 47–58. https://doi.org/10.1016/j.socec.2019.03.005** [verified-crossref]
- 100 publications, 317 effect sizes. Context only; no number from it is used as a benchmark.

**Milkman, K. L., et al. (2021). Megastudies improve the impact of applied behavioural science. *Nature*, 600, 478–483. https://doi.org/10.1038/s41586-021-04128-4** [verified-crossref]
- 61,293 people, 54 interventions, US gym. 45% of interventions raised visits by 9–27%; only 8% produced effects that persisted after the program; expert forecasts failed.

**Bryan, C. J., Tipton, E., & Yeager, D. S. (2021). Behavioural science is unlikely to change the world without a heterogeneity revolution. *Nature Human Behaviour*, 5(8), 980–989. https://doi.org/10.1038/s41562-021-01143-3** [verified-crossref]
- Expect heterogeneous effects; avoid haphazard convenience samples; measure moderators. The fetched text did not discuss WEIRD samples explicitly, so no WEIRD claim is attributed to it.

**Kraft, M. A. (2020). Interpreting effect sizes of education interventions. *Educational Researcher*, 49, 241–253. https://doi.org/10.3102/0013189X20912798** [verified-crossref]
- Benchmarks for interpreting education effects, from US education RCTs. The dossier quotes no thresholds from it, so SKILL.md quotes none; a user in education should read the paper directly.

**Brandon, A., et al. (2017). Do the effects of nudges persist? Theory and evidence from 38 natural field experiments. NBER Working Paper 23277 (revised 2022). https://doi.org/10.3386/w23277** [verified-crossref] (bench entry E12)
- Persistence of nudge effects; evidence mostly US energy and utility data (weird-only). No PNAS version exists; Crossref also lists a 2026 *Review of Economic Studies* version (10.1093/restud/rdag012), noted as a pointer only. No numbers in the dossier.

## Practitioner sources

- J-PAL, *Power calculations* [verified-fetch: https://www.povertyactionlab.org/resource/power-calculations]. Notes that effect sizes in power calculations are usually set too optimistically.

## Non-WEIRD evidence

- None found in the sources this skill draws on. DellaVigna and Linos cover US units only; Milkman et al. is a US gym; Kraft is US education.
- The plan's "LMIC benchmarks from J-PAL evidence per domain" are not in the reports and must be added by the author before the skill can give domain-specific LMIC reference points.

## Known corrections and cautions

- Mertens: 0.45, not 0.43 (dossier correction 12).
- Benchmarks are domain-specific; do not apply Cohen's labels. Cohen (1988) is unverified in the dossier and not needed; it is not cited.
- Never quote d = 0.45 or a journal-trial point estimate alone; the bias-corrected and field figures go beside it.
- The pattern the dossier asks every technique skill to state: lab-to-field shrinkage (0.33 to 0.02 SD) and the academic-versus-unit gap (8.7 versus 1.4 points) point the same way; published lab or academic effects should be discounted when transferred.

## What to check locally

1. Whether any field trial of the same intervention type exists in a comparable setting; if so, it replaces the discounted high-income figure as the top of the range.
2. The baseline rate or SD of the outcome in the program's own data; the pp-to-SD conversion is only as good as that number.
3. Whether the source the team relies on is already a practitioner (nudge-unit) result, in which case the academic-to-practitioner discount must not be applied again.
4. Which domain the intervention belongs to, because the pooled nudge average hides large differences by domain and by structure versus description interventions.
5. Whether the decision depends on persistence after the program ends; if so, the during-program effect is not the number that matters.
