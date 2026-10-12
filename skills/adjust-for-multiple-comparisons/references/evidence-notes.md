# Evidence notes: adjust-for-multiple-comparisons

Every source below is taken from `docs/plan/2026-10-skill-expansion-dossier.md` (compiled 2026-10-12), with the dossier's verification tag carried over. Nothing has been added from memory, and no number appears here that the dossier does not give. The dossier's entry for this skill lists "Numbers to quote: none"; the only numbers in the skill and its worked example are the arithmetic of the procedures on illustrative inputs.

## Anchor sources

### Anderson (2008), *Journal of the American Statistical Association* 103(484), 1481–1495 [verified-crossref]
- https://doi.org/10.1198/016214508000000841
- Re-evaluation of three US early-childhood programs (Abecedarian, Perry Preschool, Early Training Projects) under multiple inference. Introduces two tools used widely since: summary indices of related outcomes (standardized against the control group, oriented, and weighted by the inverse of the covariance so redundant outcomes count less) and family-wise error control for the tests that remain.
- What it supports: the index option in step 3 and the family-wise option for costly false positives. No effect sizes from the re-analysis are given in the dossier, and none are quoted.

### Benjamini & Hochberg (1995), *Journal of the Royal Statistical Society: Series B* 57(1), 289–300 [verified-crossref]
- https://doi.org/10.1111/j.2517-6161.1995.tb02031.x
- Defines the false discovery rate (the expected share of rejected hypotheses that are false) and gives the step-up procedure that controls it: sort the p-values, compare each to its rank times alpha over m, reject up to the largest that passes.
- What it supports: the FDR option in step 2 and the q-values that `scripts/bh_adjust.py` computes. The dossier also mentions "sharpened q-values" as an FDR variant without a citation; the script implements the original procedure only.

### List, Shaikh & Xu (2019), *Experimental Economics* 22(4), 773–793 [verified-crossref]
- https://doi.org/10.1007/s10683-018-09597-5
- A family-wise error control procedure for experiments with multiple treatments, multiple outcomes, and multiple subgroups tested jointly, which uses the dependence among the tests to be less conservative than Bonferroni.
- What it supports: step 4's joint FWER option when the raw data are available. The dossier records no application numbers. The Stata command name (mhtexp) is standard software named without citation, as the drafting brief allows.

### EGAP, *10 Things to Know About Multiple Comparisons* [verified-fetch: https://egap.org/resource/10-things-to-know-about-multiple-comparisons/]
- Practitioner methods guide. The dossier confirms it as a listing on EGAP's methods-guides page; the guide itself was not opened, so nothing from its content is quoted.

## Cross-cutting cautions (dossier section A)

- A6. Szaszi, Palinkas, Palfi, Szollosi & Aczel (2018), *Journal of Behavioral Decision Making* 31(3), 355–366, https://doi.org/10.1002/bdm.2035 [verified-crossref] (audit year 2017, online-first): 156 studies, 422 interventions; 7% used a power analysis; none were preregistered. Relevant because a family defined in a pre-analysis plan is exactly what these studies lacked.
- A4. DellaVigna & Linos (2022), *Econometrica* 90(1), 81–116, https://doi.org/10.3982/ECTA18709 [verified-crossref]: about 70% of the gap between academic (8.7 points) and nudge-unit (1.4 points) effects is selective publication combined with low power. Reporting the two significant results out of twelve is selective publication inside one study.

## Non-WEIRD evidence

- None found in the sources this skill draws on. The dossier records the procedures as "standard in development RCTs (no specific study cited in the reports)".
- Anderson's data are US early-childhood programs; the procedures themselves do not depend on the population.

## Known corrections, gaps, and unverified items

- The dossier's replication note is "FWER vs FDR is a judgment call"; the skill records the reason for each family's choice rather than fixing a rule.
- "Sharpened q-values" appear in the dossier's boundary-conditions line without a citation; the skill does not implement or cite them.
- The index construction described in step 3 (standardize to control, orient, inverse-covariance weights) is the method as the dossier summarizes Anderson; the exact weighting formula was not re-derived from the paper for this draft (author to confirm against the paper before publication).
- The Doer/Non-Doer 15-point rule is cited from the dossier's `analyze-doer-nondoer-differences` entry, where it is described as a convention with no validation; this skill only says that it is not an inferential test.
- The rule that a primary outcome is its own family of one is the drafter's operationalization of standard pre-analysis-plan practice, not a quoted source.

## What to check locally

1. Whether a pre-analysis plan exists and what it says about families and methods, word for word.
2. Which decision each family feeds, and how costly one false positive would be there.
3. Whether the outcomes within a family are correlated enough that Bonferroni would reject almost nothing, which argues for an index or a joint procedure.
4. Whether every component of a planned index is oriented the same way and present for the whole sample.
5. Whether the funder's reporting template names a different primary outcome from the plan.
6. Whether anyone has already looked at the results before the families were written down.
