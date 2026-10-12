# Evidence notes: estimate-sample-size

Every item below comes from `docs/plan/2026-10-skill-expansion-dossier.md` (entry `estimate-sample-size`, section F). The verification tag is the dossier's. Nothing has been upgraded or added from memory. The dossier records no empirical numbers for this entry; the only formula it gives is the design effect.

## Anchor sources

**Bloom, H. S. (1995). Minimum detectable effects. *Evaluation Review*, 19(5), 547–556. https://doi.org/10.1177/0193841X9501900504** [verified-crossref]
- Defines the minimum detectable effect: the smallest true effect a design detects with a stated power at a stated alpha. The reason this skill reports MDES rather than only N.

**McConnell, B., & Vera-Hernández, M. (2025). Going beyond simple sample size calculations: A practitioner's guide. *Fiscal Studies*, 46(3), 323–348. https://doi.org/10.1111/1475-5890.70005** [verified-crossref]
- Working-paper version: IFS Working Paper W15/17, https://doi.org/10.1920/wp.ifs.2015.1517 [verified-crossref] (Crossref year metadata reads 2026; the report dates the working paper 2015).
- Covers what the textbook formula leaves out: clustering, take-up, attrition, covariates. The dossier notes the authors are LMIC-experienced.

**Vera Hernández, A., & McConnell, B. (2024). *Sample size calculators (Going beyond simple sample size calculations: a practitioner's guide)*. UCL figshare. https://doi.org/10.5522/04/25373830.v1** [verified-fetch: https://api.datacite.org/dois/10.5522%2F04%2F25373830.v1] (DataCite record: UCL, 2024)
- The calculators that accompany the guide. `scripts/power_calc.py` is this skill's own standard-library implementation of the same textbook formulas, not a copy of the UCL calculators.

**Hedges, L. V., & Hedberg, E. C. (2007). Intraclass correlation values for planning group-randomized trials in education. *Educational Evaluation and Policy Analysis*, 29(1), 60–87. https://doi.org/10.3102/0162373707299706** [verified-crossref]
- Reference ICCs from US education data. Cited so the skill can say they do not transfer; no value from it is used as a default.

**Gelman, A., & Carlin, J. (2014). Beyond power calculations. *Perspectives on Psychological Science*, 9(6), 641–651. https://doi.org/10.1177/1745691614551642** [verified-crossref]
- Type S (sign) and Type M (magnitude) errors: when power is low, significant estimates can have the wrong sign and overstate the true effect. The script's `--true-effect` output implements this retrodesign logic in closed form.

## Practitioner sources

- J-PAL, *Power calculations* [verified-fetch: https://www.povertyactionlab.org/resource/power-calculations]. Covers MDE, ICC, clustered designs, attrition, take-up; links a power calculator and Stata/R code; notes effect sizes are usually set too optimistically. The World Bank "Power Dashboard" (Kondylis & Loeser) is linked from this page per the dossier; not fetched, not cited in SKILL.md.
- EGAP, *10 things to know about statistical power* [verified-fetch: https://egap.org/resource/10-things-to-know-about-statistical-power/] (confirmed as a listing on the methods-guides page; the guide itself was not opened by the audit).

## Formula recorded in the dossier

- Design effect 1 + (m − 1)ρ for m units per cluster at ICC ρ (standard formula, per the report). Every other formula in `scripts/power_calc.py` is the standard normal approximation for a two-arm comparison; none is attributed to a specific source in the dossier.

## Non-WEIRD evidence

- None found in the sources this skill draws on, beyond the dossier's note that the IFS calculators come from LMIC-experienced authors. LMIC ICC compilations are scarce.
- Kelcey, Shen & Spybrook (2016), sub-Saharan African education ICCs: [unverified, author to confirm] (dossier unverified item 23). Not cited in SKILL.md as a source; named only so the user knows a compilation may exist.

## Known corrections and cautions

- Cohen (1988): unverified in the dossier and not needed; not cited. Its small-medium-large labels are not planning benchmarks.
- Effect sizes in power calculations are usually set too optimistically (J-PAL); US ICCs may not transfer; report MDES rather than only N; adjust for covariates, take-up, and attrition.
- The dossier entry records no corrections specific to this skill.
- The "fewer than about 30 clusters" escalation threshold in SKILL.md is this skill's rule of thumb, not a figure from any source in the dossier.

## What to check locally

1. The ICC, from the program's own baseline or administrative data at the cluster level; if none exists, the sensitivity table is the output, not a single N.
2. The outcome's SD or baseline rate in this population, and whether it came from data or from a guess.
3. Realistic take-up in the treatment arm and contamination in control, from the program's enrollment history.
4. Attrition between enrollment and outcome measurement in the program's previous rounds.
5. Whether cluster sizes will be roughly equal; the design effect above assumes they are.
