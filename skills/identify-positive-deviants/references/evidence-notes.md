# Evidence notes: identify-positive-deviants

Every item below is taken from `docs/plan/2026-10-skill-expansion-dossier.md` (section C entry for this skill and section F corrections). The verification tags are the dossier's. Nothing was added from memory; where the dossier gives no number, none is quoted.

## Anchor sources

### Pascale, R. T., Sternin, J., & Sternin, M. (2010). *The Power of Positive Deviance*. Harvard Business Press. [verified-fetch: https://openlibrary.org/isbn/9781422110669.json]
- The book-length account of the approach by its originators. The OpenLibrary record gives the subtitle as "how improbable innovators solve the world's toughest problems"; the design report wrote "unlikely innovators". The dossier says to confirm the wording before quoting the subtitle, so the skill cites the title without it.
- Practitioner source, not an evaluation. No numbers.

### Marsh, D. R., et al. (2004). The power of positive deviance. *BMJ*, 329, 1177. https://doi.org/10.1136/bmj.329.7475.1177 [verified-crossref]
- A short peer-reviewed description of the approach and its steps. The dossier records the procedure as: define the outcome, screen for outliers, inquire into practices, verify with the community.
- No effect sizes recorded in the dossier.

### Bisits Bullen (2011). The positive deviance/hearth approach to reducing child malnutrition: Systematic review. *Tropical Medicine & International Health*. https://doi.org/10.1111/j.1365-3156.2011.02839.x [verified-crossref]
- A systematic review of positive deviance/Hearth as an intervention for child malnutrition.
- Result recorded in the dossier: the included studies were mostly uncontrolled.
- Author-name correction from the dossier: the author is "Bisits Bullen", not "Bullen" as the plan wrote. Initials are not given in the dossier, so none are used.
- Population, k, and N: not recorded in the dossier.

### Triatmaja et al. (2023). Effectiveness of positive deviance approach to reduce malnutrition among under five children: A systematic review and meta-analysis of interventional studies. *Nutrients*, 15(8), 1961. https://doi.org/10.3390/nu15081961 [verified-crossref]
- A systematic review and meta-analysis of interventional studies of the positive deviance approach for under-five malnutrition.
- Result recorded in the dossier: no significant growth z-score differences. The dossier does not quote the effect sizes, k, or N, so the skill quotes none.
- Name correction from the dossier: the plan's "2023 Nutrients meta" is Triatmaja et al.

## Numbers quoted in the skill, and where they come from
- None. The dossier records a null result (no significant growth z-score differences) without magnitudes, and "mostly uncontrolled" for the 2011 review. The skill repeats these as stated and adds no figures.

## Non-WEIRD evidence
- Origin: Vietnam child-malnutrition work (Save the Children), per the labs report; no URL recorded.
- Many LMIC uses, per the labs report (no list in the dossier).
- Both reviews cover child-malnutrition programs, which are LMIC programs, so the null intervention result is itself non-WEIRD evidence.
- Consequence for the skill: `weird: likely-generalizes`, as the dossier proposes, with the qualifier "as inquiry": the method's origin and use are LMIC, but what generalizes is the inquiry procedure, not an effect.

## Replication status (as recorded)
- As an intervention: weak. The 2023 meta-analysis found no significant growth z-score differences; the 2011 review's studies were mostly uncontrolled. The dossier instructs the drafter to state this.
- As an inquiry method: no validation study; practitioner method.
- No publication-bias corrections apply, because the pooled result is already null.

## Boundary conditions and cautions from the dossier
- Procedure: define the outcome, screen for outliers, inquire into practices, verify with the community.
- Do not promise nutrition gains.
- Corrections for the drafter: author name "Bisits Bullen"; Triatmaja et al. for the 2023 meta-analysis; subtitle wording of Pascale et al. unconfirmed.

## Practitioner sources
- Save the Children (Vietnam), per the labs report; no URL. Not cited as a document in the skill.

## What the skill adds beyond the sources (judgment calls, not evidence)
- The requirement that the outcome hold over more than one measurement period.
- The explicit shared-constraints screen with named exclusions ("resource deviants").
- A matched set of non-deviants inquired into with the same protocol.
- Tagging every practice observed or reported.
- Presenting practices without names at community verification.
- Linking each practice to the COM-B hypothesis it bears on, so the output feeds `decompose-comb-barriers`.
- A mandatory "What this does not show" section citing the null intervention evidence.

## What to check locally
- Which resources actually separate households here (remittances, a relative in town, a vehicle, a second earner, land quality), so the constraints screen catches them.
- Whether the outcome source is reliable enough to pick outliers (monitoring records can be gamed; measurements drift between enumerators).
- Whether success is confidential or stigmatized, and whether non-deviants could be shamed by the inquiry or the verification session.
- Who nominates, if nomination is used, and what they gain from nominating.
- Whether the practices found are acceptable to the people who would have to adopt them, which the community verification is meant to test.
