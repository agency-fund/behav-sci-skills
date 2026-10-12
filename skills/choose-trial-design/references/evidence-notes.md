# Evidence notes: choose-trial-design

Every item below comes from `docs/plan/2026-10-skill-expansion-dossier.md` (entry `choose-trial-design`, the `design-adaptive-message-experiment` and `select-messenger` entries for the Haryana trial, and section A for the megastudy). The verification tag is the dossier's. Nothing has been upgraded or added from memory. The dossier records no empirical numbers for this entry.

## Anchor sources

**Hemming, K., et al. (2015). The stepped wedge cluster randomised trial: Rationale, design, analysis, and reporting. *BMJ*, 350, h391. https://doi.org/10.1136/bmj.h391** [verified-crossref]
- The stepped-wedge design: all clusters start in control and cross over to treatment at randomized times. Per the report, the abstract notes it suits phased rollouts, which are common in LMIC programs.
- The dossier's replication note: the design is confounded with time trends, so time must be modeled.

**Hayes, R. J., & Moulton, L. H. (2009). *Cluster Randomised Trials*. Chapman & Hall/CRC. https://doi.org/10.1201/9781584888178** [verified-crossref] (the report had it from memory; the book DOI was located in the audit)
- The standard text on cluster randomized trials: when to randomize groups, the power cost, and the analysis. No specific page or number is quoted in the dossier.

**Collins, L. M. (2018). *Optimization of Behavioral, Biobehavioral, and Biomedical Interventions: The Multiphase Optimization Strategy (MOST)*. Springer. https://doi.org/10.1007/978-3-319-72206-1** [verified-crossref]
- MOST: factorial designs to decide which components of an intervention earn their place. The dossier's replication note: factorial designs assume mostly additive component effects.

**EGAP, *10 things to know about cluster randomization*** [verified-fetch: https://egap.org/resource/10-things-to-know-about-cluster-randomization/] (listing only; the guide itself was not opened by the audit)

**EGAP, *10 things to know about multisite or block-randomized trials*** (https://egap.org/resource/10-things-to-know-about-multisite-or-block-randomized-trials/; named in the dossier entry alongside the cluster guide, which was confirmed as a listing; this URL was not separately tagged)

## Many-arm examples recorded in the dossier

**Banerjee, A., Chandrasekhar, A. G., Dalpath, S., Duflo, E., Floretta, J., Jackson, M. O., et al. (2025). Selecting the most effective nudge: Evidence from a large-scale experiment on immunization. *Econometrica*, 93(4), 1183–1223. https://doi.org/10.3982/ECTA19739** [verified-crossref]; NBER w28726 https://doi.org/10.3386/w28726 [verified-crossref]
- Haryana, India. 75 arms; treatment-variant aggregation with a winner's-curse correction (per the `design-adaptive-message-experiment` entry). Results quoted elsewhere in the dossier (SMS alone had no impact; ambassadors plus SMS the most cost-effective bundle, +9.1% immunizations per dollar) are from a J-PAL page, secondary source per report, and are not used by this skill.

**Milkman, K. L., et al. (2021). Megastudies improve the impact of applied behavioural science. *Nature*, 600, 478–483. https://doi.org/10.1038/s41586-021-04128-4** [verified-crossref]
- 61,293 people, 54 interventions, US gym; 45% of interventions raised visits by 9–27%; only 8% persisted; expert forecasts failed. Used here only as an example of a many-arm design.

## Practitioner sources

- EGAP guides (above).
- J-PAL, *Randomization* resource page: the report marked it verified; the audit did not re-fetch it and records no URL. Not cited in SKILL.md.

## Non-WEIRD evidence

- Stepped-wedge suits phased rollouts common in LMIC programs (Hemming abstract, per the report).
- The Haryana experiment (Banerjee et al. 2025) is an Indian field trial with 75 arms. Neither item is evidence about a design's validity; the designs rest on their statistical logic.

## Known corrections and cautions

- The dossier entry records no corrections specific to this skill.
- Replication status per the dossier: stepped-wedge is confounded with time trends; factorial designs assume mostly additive component effects.
- The design effect 1 + (m − 1)ρ quoted in SKILL.md is the standard formula recorded in the `estimate-sample-size` entry.
- The "take-up below about a third" and "fewer than about 30 clusters" thresholds are this skill's rules of thumb, not figures from any dossier source.

## What to check locally

1. Whether people in the same cluster really share the channel the intervention travels through; the spillover answer sets the unit, and it should come from the theory of change or fieldwork, not assumption.
2. The actual rollout calendar and capacity per period, which determine whether a waitlist or a stepped-wedge is feasible.
3. Who has authority to withhold or delay, and whether they will hold to the assignment once drawn.
4. Expected take-up of an offer in this population, from enrollment history, before choosing an encouragement design.
5. How many units exist at each level; small counts of administrative units rule out designs that look fine on paper.
