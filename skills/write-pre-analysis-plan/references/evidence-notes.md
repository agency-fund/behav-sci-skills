# Evidence notes: write-pre-analysis-plan

Every item below comes from `docs/plan/2026-10-skill-expansion-dossier.md` (entry `write-pre-analysis-plan`, with the `adjust-for-multiple-comparisons` and `analyze-heterogeneous-effects` entries for the hand-offs). The verification tag is the dossier's. Nothing has been upgraded or added from memory.

## Anchor sources

**Olken, B. A. (2015). Promises and perils of pre-analysis plans. *Journal of Economic Perspectives*, 29(3), 61–80. https://doi.org/10.1257/jep.29.3.61** [verified-crossref]
- The case for and against pre-analysis plans in economics: credibility where the analysis could otherwise be chosen after the data, against rigidity and lost learning. No numbers in the dossier.
- Also the anchor for the existing `plan-evaluation-design`, which handles the measurement side; this skill handles the analysis side.

**Coffman, L. C., & Niederle, M. (2015). Pre-analysis plans have limited upside, especially where replications are feasible. *Journal of Economic Perspectives*, 29(3), 81–98. https://doi.org/10.1257/jep.29.3.81** [verified-crossref]
- The skeptical side of the debate: limited upside, especially where replications are feasible. SKILL.md states this rather than presenting pre-specification as uncontested.

**Banerjee, A., et al. (2020). In praise of moderation: Suggestions for the scope and use of pre-analysis plans for RCTs in economics. NBER Working Paper 26993. https://doi.org/10.3386/w26993** [verified-crossref]
- Argues for moderate plans: pre-specify what matters, keep flexibility, report deviations.
- Correction (dossier correction 9): the plan and report wrote "Duflo et al."; Crossref lists Banerjee as first author. Co-authors were not captured by the audit, so the citation uses "et al.".

**AEA RCT Registry. https://www.socialscienceregistry.org/** [verified-fetch]
- "The American Economic Association's registry for randomized controlled trials." The level of detail this skill targets. The dossier does not list the registry's fields; SKILL.md says "fill the registry fields" without enumerating them.

**Office of Evaluation Sciences (2021). *Analysis plan* template, July 2021. https://oes.gsa.gov/assets/files/AnalysisPlan.pdf** [verified-fetch]
- Sections read by the audit: project description, preregistration details, hypotheses, data and data structure, outcomes, transformations, exclusion, missing data, descriptive statistics, statistical models and hypothesis tests. Quoted: "finalized and date-stamped before we take possession of outcome data."
- The fuller-specification end of the spectrum; SKILL.md uses it where stakes are high. The OES "six-gate evaluation policy" is mentioned in the dossier's labs report without a source and is not used.

**J-PAL. *Pre-analysis plans*. https://www.povertyactionlab.org/resource/pre-analysis-plans** [verified-fetch]
- Quoted: "A PAP should be concise and focused, rather than attempt to be exhaustive." Treats the populated PAP as a separate document.

**EGAP. *10 things to know about pre-analysis plans*. https://egap.org/resource/10-things-to-know-about-pre-analysis-plans/** [verified-fetch, listing only]
- Confirmed as a listing on EGAP's methods-guides page; the guide itself was not opened. Cite as a practitioner guide, not for specific claims.

## Hand-off sources (not cited in SKILL.md; owned by the analyze-stage skills)

- Multiple testing: Anderson (2008), Benjamini and Hochberg (1995), List, Shaikh and Xu (2019), per the `adjust-for-multiple-comparisons` entry. SKILL.md names outcome families and defers the correction's mechanics there.
- Heterogeneity: Bryan, Tipton and Yeager (2021), Wager and Athey (2018), Chernozhukov et al. (2025), per the `analyze-heterogeneous-effects` entry. SKILL.md requires theory-based subgroups and defers execution there.

## Non-WEIRD evidence

- None in the dossier as a study of pre-analysis plans. The practice's origin is in development-economics RCTs (Olken; Banerjee et al.), which SKILL.md records as provenance, not as evidence of effect.
- `weird` is not-applicable, as the dossier proposes: the skill is procedural.

## Known corrections and cautions

- First author of "In praise of moderation" is Banerjee, not Duflo (dossier correction 9).
- Christensen and Miguel (2018), *Journal of Economic Literature*, is unverified in the dossier and not included.
- The dossier flags possible overlap with `plan-evaluation-design` and instructs: keep this skill to the analysis-plan document. SKILL.md carries the design over verbatim and refuses to re-decide it.
- Decision rules in the plan are this skill's addition; none of the sources require them.
- No numbers appear in the dossier for this entry; the worked example's values are illustrative.

## What to check locally

1. Whether the registry is reachable and its timing fits local ethics approval and the launch date.
2. Whether the data structure the plan assumes exists: consistent ids across rounds, cluster identifiers, the baseline variables named as covariates.
3. Who controls the outcome data before registration, and whether any arm-level tabulation has already circulated (a dashboard counts).
4. Which party has the strongest stake in the result here, so that the plan's detail lands where the pressure will be.
5. Whether the smallest effect worth detecting in the design brief is the same number the decision rules use; if the sponsor changed it, the brief is updated first.
