# Evidence notes: design-adaptive-message-experiment

Every item below comes from `docs/plan/2026-10-skill-expansion-dossier.md` (entry `design-adaptive-message-experiment`, the `select-messenger` entry for the Haryana numbers, and section A). The verification tag is the dossier's. Nothing has been upgraded or added from memory. "Secondary source per report" means the number came from a summary page (J-PAL) that the dossier's audit did not re-fetch.

## Anchor sources

**Offer-Westort, M., Coppock, A., & Green, D. P. (2021). Adaptive experimental design: Prospects and applications in political science. *American Journal of Political Science*. https://doi.org/10.1111/ajps.12597** [verified-crossref]
- The social-science treatment of adaptive designs: batch assignment, updating between batches, algorithm choice by goal. No numbers quoted in the dossier.
- The dossier does not record the paper's applications or populations; do not attribute a setting to it.

**Kasy, M., & Sautmann, A. (2021). Adaptive treatment assignment in experiments for policy choice. *Econometrica*, 89(1), 113–132. https://doi.org/10.3982/ECTA17527** [verified-crossref]
- Introduces exploration sampling for experiments whose goal is to choose a policy at the end rather than to maximize outcomes during the run.
- Application per the dossier: recruiting farmers into agricultural extension in India; Precision Development lists the paper. No effect size recorded.
- The dossier's report recalls a published correction to the paper's optimality result: [unverified, author to confirm]. The dossier instructs: do not state that a correction exists unless confirmed. SKILL.md says "possible published correction (unverified, author to confirm)" and treats exploration sampling as a default, not a settled optimum.

**EGAP. *10 things to know about adaptive experimental design*. https://egap.org/resource/10-things-to-know-about-adaptive-experimental-design/** [verified-fetch, listing only]
- Confirmed as a listing on EGAP's methods-guides page; the guide itself was not opened by the dossier's audit. Cite as a practitioner guide, not for specific claims.

**Banerjee, A., Chandrasekhar, A. G., Dalpath, S., Duflo, E., Floretta, J., Jackson, M. O., et al. (2025). Selecting the most effective nudge: Evidence from a large-scale experiment on immunization. *Econometrica*, 93(4), 1183–1223. https://doi.org/10.3982/ECTA19739** [verified-crossref]; NBER w28726 https://doi.org/10.3386/w28726 [verified-crossref]
- Haryana, India. 75 arms; treatment-variant aggregation with a winner's-curse correction (dossier, adaptive entry).
- SMS reminders alone had no impact; information-hub ambassadors plus SMS was the most cost-effective option, +9.1% immunizations per dollar (J-PAL page, secondary source per report; `select-messenger` entry).
- Role here: the many-arm context and the winner's-curse correction. The dossier does not describe the trial's allocation as adaptive; do not call it a bandit.

**Milkman, K. L., et al. (2021). Megastudies improve the impact of applied behavioural science. *Nature*, 600, 478–483. https://doi.org/10.1038/s41586-021-04128-4** [verified-crossref] (section A, A10)
- 61,293 people, 54 interventions, US gym. 45% of interventions raised visits by 9 to 27%; only 8% produced effects that persisted after the program; expert forecasts failed.
- Role here: many arms differ little, short-run winners often do not persist, and forecasts do not substitute for testing. The dossier does not describe its allocation as adaptive.

## Discounting sources (section A)

**DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709** [verified-crossref]
- 126 RCTs, 23 million people. Academic journal studies average 8.7 percentage points (+33.4%); nudge-unit trials average 1.4 points (+8.0%); about 70% of the gap from selective publication plus low power.
- Not quoted in SKILL.md; relevant if a team sets its reward-rate expectations from published message studies.

## Practitioner sources

- EGAP guide (above).
- Precision Development (PxD) practice with adaptive assignment, per the dossier's report; no URL or document recorded. Do not cite a PxD result.
- Evidential's adaptive experiment types (the `mab_online`, `mab_online_dwh`, `cmab_online` family) are described in `design-evidential-experiment`, which draws on the Evidential documentation; this skill does not cite them independently.

## Non-WEIRD evidence

- India: Kasy and Sautmann's exploration-sampling application to agricultural extension recruitment; no effect size in the dossier.
- India (Haryana): Banerjee et al. (2025), 75 arms; SMS alone no impact; ambassadors plus SMS most cost-effective, +9.1% immunizations per dollar (secondary source per report).
- The method is statistical and the two field applications recorded are both Indian, which is why `weird` is likely-generalizes, as the dossier proposes.

## Known corrections and cautions

- A published correction to Kasy and Sautmann (2021): dossier unverified item 24. Not stated as fact anywhere in this skill.
- Standard errors after adaptive assignment are biased (dossier replication note). SKILL.md makes the inference plan mandatory and gives a fallback (estimate in a fixed confirmatory wave) for teams without a statistician.
- The dossier names no specific estimator for adaptively collected data; SKILL.md does not name one either and routes that choice to a statistician.
- The exploration floor, burn-in wave, holdout share, and probability-best stopping threshold are this skill's design conventions, not values from any source; the worked example marks its values illustrative.

## What to check locally

1. That the reward is logged automatically within days, for everyone, in a system the team can read between waves.
2. That waves arrive at a steady enough rate that a batch schedule is realistic.
3. Whether delivery differs by subgroup (shared phones, literacy, language, network coverage), so that the best arm for one group is not the best for another.
4. Whether any arm's claim (a norm statement, a deadline) is true in this setting before it is sent.
5. Whether the short-run reward predicts the outcome that matters here; schedule the persistence check rather than assuming it.
