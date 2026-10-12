# Evidence notes: draft-survey-items

Every source below comes from `docs/plan/2026-10-skill-expansion-dossier.md` (compiled 2026-10-12). Verification tags are carried over as the dossier gives them; nothing has been upgraded or added from memory. Numbers appear only as the dossier writes them.

## The survey-response model and the design rules

### Tourangeau, R., Rips, L. J., & Rasinski, K. (2000). *The Psychology of Survey Response* [verified-crossref]
Cambridge University Press. https://doi.org/10.1017/CBO9780511819322. The research report had this from memory; the DOI was located in the dossier audit.
- The four-stage model: comprehension, retrieval, judgment, response. Each item is a cognitive task; this skill's design check tests each stage.
- Shared with `draft-cognitive-interview-script`, which organizes its probes by the same four stages, so items written here map directly onto that pretest.

### Krosnick, J. A., & Presser, S. (2010). Question and questionnaire design [verified-fetch: https://openlibrary.org/search.json?title=handbook+of+survey+research&author=marsden]
In P. V. Marsden & J. D. Wright (Eds.), *Handbook of Survey Research* (2nd ed.). Emerald. The handbook record (Marsden & Wright, first publish year 2009) is confirmed; the chapter itself was not seen, and its title and authors are from the research report.
- The standard treatment of closed-ended question design. This skill attributes to it the rules it is known for (construct-specific options over agree/disagree formats; label every point; keep the task easy enough to avoid satisficing) and no numbers.

### J-PAL. *Survey design* [verified-fetch: https://www.povertyactionlab.org/resource/survey-design]
- "Each question should be SMART"; Likert, ranked, numeracy, and frequency scales; central tendency bias; sensitive-question techniques.

### EGAP. *10 Things to Know About Survey Design* [verified-fetch: https://egap.org/resource/10-things-to-know-about-survey-design/]
- Confirmed as a listing on EGAP's methods guides page; the guide was not fetched, so no content is attributed to it.

### Gyani, A., Tindall, K., & Gallagher, R. (2022). *Explore Field Guide*, survey section [verified-fetch: https://www.bi.team/wp-content/uploads/2022/11/BIT-Explore-Field-Guide.pdf]
- Behavioural Insights Team. The dossier records "three steps, response rates" for the survey section; no numbers.

## Response styles and the LMIC caution

### Harzing, A.-W. (2006). Response styles in cross-national survey research: A 26-country study [verified-crossref]
*International Journal of Cross Cultural Management*, 6(2), 243–266. https://doi.org/10.1177/1470595806066332.
- Response styles (acquiescence, extreme responding) differ across 26 countries. The dossier does not list the countries or quote effect sizes.
- Implication for this skill: the scale format itself produces country-specific data; agree/disagree formats and midpoints are the most exposed.

### Laajaj, R., & Macours, K. (2021). Measuring skills in developing countries [verified-crossref]
*Journal of Human Resources*, 56(4), 1254–1295. https://doi.org/10.3368/jhr.56.4.1018-9805R1. Print 2021; audit year 2019 (online-first).
- Kenya. The research report attributes to it the finding that standard noncognitive skill scales showed weak reliability and validity, with acquiescence bias among the problems. The paper is verified; the specific finding's wording was from memory in the report: [unverified, author to confirm] before quoting.
- The only LMIC study in the dossier entry; it supports the cautions rather than any particular item format.

## Rules in the dossier without an attached citation
- Reverse-keyed items can themselves cause problems in low-literacy samples. Listed under the entry's boundary conditions with no source; this skill applies it as a rule and does not attribute it to a paper.
- No double-barreled items; balanced options; labeled scale points; sensible option order; choose the number of scale points; pretest with cognitive interviews. Same status.
- Numbers to quote: none verified. The "three to five labeled points" default and the "at most five items per construct" assumption are this skill's practitioner rules, not findings.

## Non-WEIRD evidence
- Kenya (Laajaj & Macours 2021), with the caution above.
- Harzing's 26 countries, unnamed in the dossier.

## Replication status
- Mixed. The design rules rest on a US and European methodological literature the dossier records as the main evidence base; the Kenya study shows standard scales failing, which supports the cautions but is a single study in these sources.

## Known corrections and cautions (from the dossier)
- Dillman *Tailored Design Method* and DeVellis *Scale Development* were unverified in the research report and are not in the dossier; this skill does not cite them.
- Boateng et al. (2018) is not in the dossier and is not cited; the reverse-keyed caution stands on the dossier's boundary-conditions line alone.
- The Laajaj & Macours finding keeps its unverified tag until the wording is checked against the paper.
- Nothing in this entry validates an item set. Reliability, factor structure, and summed scores belong to a separate skill and must not appear in this skill's output.

## What to check locally
- Which response styles this population shows (yes-saying, extreme responding, avoiding the midpoint); a short pretest tabulation by option answers this.
- Whether a midpoint is read as "neither" or as "I do not want to say".
- Which local events or calendar markers bound recall better than "the last 30 days".
- Whether enumerators actually read the options every time; a read-aloud script only works if it is followed.
- Whether any construct is sensitive here even if it is not elsewhere (savings amounts, household authority, who decides); if yes, route it to `design-list-experiment`.
