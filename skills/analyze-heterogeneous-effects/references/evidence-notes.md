# Evidence notes: analyze-heterogeneous-effects

Every source below is taken from `docs/plan/2026-10-skill-expansion-dossier.md` (compiled 2026-10-12), with the dossier's verification tag carried over. Nothing has been added from memory, and no number appears here that the dossier does not give. The dossier's entry for this skill lists "Numbers to quote: none".

## Anchor sources

### Bryan, Tipton & Yeager (2021), *Nature Human Behaviour* 5(8), 980–989 [verified-crossref]
- https://doi.org/10.1038/s41562-021-01143-3
- Argues that behavioral-science effects should be expected to vary across people and settings, that "haphazard convenience samples" cannot tell for whom, and that trials should use probability samples with moderators measured.
- What it supports: the sample line in the output, the rule that a convenience sample cannot say who benefits in the population, and the push to pre-register moderators. The dossier notes that the fetched text did not explicitly discuss WEIRD samples, so this skill attributes no WEIRD claim to it.

### Wager & Athey (2018), *Journal of the American Statistical Association* 113(523), 1228–1242 [verified-crossref]
- https://doi.org/10.1080/01621459.2017.1319839
- Causal forests: a random-forest estimator of the treatment effect for each unit from its covariates, with confidence intervals that rely on each tree being grown on one subsample and estimated on another.
- What it supports: the flexible model in step 4 and the requirement for sample splitting. The dossier records no application numbers.

### Chernozhukov, Demirer, Duflo & Fernández-Val (2025), *Econometrica* 93, 1121–1164 [verified-crossref]
- https://doi.org/10.3982/ECTA19303 (DOI located in the dossier's audit; a reply to comments exists at 10.3982/ECTA23706). Earlier version: NBER Working Paper 24678 (2018), https://doi.org/10.3386/w24678 [verified-crossref].
- Generic machine-learning inference on heterogeneous effects in randomized experiments: fit any machine-learning proxy of the effect on an auxiliary sample, then on the main sample estimate the best linear predictor, the group average treatment effects by predicted-impact quantile, and the characteristics of the most and least affected. Applications recorded in the dossier: immunization nudges in India (the Haryana experiment) and microcredit.
- What it supports: the three exploratory outputs and the repeated-split medians. The dossier records no effect sizes from the applications, and none are quoted. The dossier records the Haryana immunization experiment separately as Banerjee et al. (2025), *Econometrica* 93(4), 1183–1223, https://doi.org/10.3982/ECTA19739 [verified-crossref]; whether the Chernozhukov application uses that experiment's data is not stated in the dossier (author to confirm), and that paper's Haryana numbers, which the dossier marks as secondary-source, are not used here.

### EGAP, *10 Things to Know About Heterogeneous Treatment Effects* [verified-fetch: https://egap.org/resource/10-things-to-know-about-heterogeneous-treatment-effects/]
- Practitioner methods guide. The dossier confirms it as a listing on EGAP's methods-guides page; the guide itself was not opened, so nothing from its content is quoted.

## Cross-cutting cautions (dossier section A)

- A6. Szaszi, Palinkas, Palfi, Szollosi & Aczel (2018), *Journal of Behavioral Decision Making* 31(3), 355–366, https://doi.org/10.1002/bdm.2035 [verified-crossref] (audit year 2017, online-first): 156 studies, 422 interventions; 74% only tested effectiveness, 24% examined moderators; 7% used a power analysis; none were preregistered. This is the baseline the skill works against: moderators are rarely examined and almost never pre-specified.
- A4. DellaVigna & Linos (2022), *Econometrica* 90(1), 81–116, https://doi.org/10.3982/ECTA18709 [verified-crossref]: 126 RCTs, 23 million people; academic journal studies average 8.7 percentage points, nudge-unit trials 1.4 points; about 70% of the gap is selective publication combined with low power. Relevant because an exploratory subgroup finding is the kind of selected, low-powered result that shrinks on replication.

## Non-WEIRD evidence

- India (Haryana), immunization nudges, and microcredit: the Chernozhukov et al. applications, above; no numbers in the dossier.
- No other non-WEIRD application is recorded in the dossier entry for this skill.

## Known corrections, gaps, and unverified items

- The dossier's caution on Bryan et al.: do not attribute a WEIRD claim to it. The skill does not.
- No numbers are quoted for this skill; the dossier entry lists none.
- "An interaction needs a much larger sample than the main effect" is stated without a multiplier because the dossier gives none.
- The repeated-splits-and-medians step describes the generic machine-learning method; the dossier records the method, not a recommended number of splits, so the skill gives none and the worked example's count is illustrative.
- Software names (grf, GenericML, econml) are standard packages named without citation, as the drafting brief allows.
- The link between the Chernozhukov application and Banerjee et al. (2025) is an inference, marked author to confirm above.

## What to check locally

1. How the sample was drawn, and which population, if any, it can speak for.
2. Which moderators the pre-analysis plan names, with their expected direction, and whether any were powered.
3. The randomization unit and the number of clusters; interaction estimates with few clusters are unreliable.
4. Whether the covariates used as moderators were measured before assignment; anything measured after treatment cannot be a moderator.
5. What decision the result will feed; targeting or exclusion is the escalation case.
6. The outcome's units, so every effect is reported in them before any standardized version.
