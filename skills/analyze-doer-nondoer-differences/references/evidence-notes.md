# Evidence notes: analyze-doer-nondoer-differences

Every item below is taken from `docs/plan/2026-10-skill-expansion-dossier.md` (section C entries for this skill and for `draft-barrier-analysis-questionnaire`, and section B item B16). The verification tags are the dossier's. Nothing was added from memory; where the dossier gives no number, none is quoted.

## Anchor sources

### Kittle, B. (2013; 2nd ed. 2017). *A Practical Guide to Conducting a Barrier Analysis*. Helen Keller International. Lessons 5 and 12. [verified-fetch: https://coregroup.org/resource-library/a-practical-guide-to-conducting-a-barrier-analysis/]
- The method this skill reproduces. The fetched page shows Helen Keller International, "YEAR PUBLISHED 2013", and "Second Edition (2017)"; the author name is not on the page and comes from the labs report.
- Sample: 45 Doers and 45 Non-Doers, from a case-control calculation (relative risk 3.0, 80% power). A design calculation, not an empirical finding.
- Flag rule (lessons 5 and 12, per the dossier): a determinant is flagged when the Doer/Non-Doer gap is at least 15 percentage points, or p < .05 in the guide's Excel tabulation sheet. The dossier does not record which statistical test the sheet uses; the skill's script computes a two-sided Fisher exact test as its own choice and says so.
- The dossier records no validation of either threshold.

### CORE Group (2013). *Designing for Behavior Change: For Agriculture, Natural Resource Management, Health and Nutrition*. CORE Group, Food Security and Nutrition Network, USAID. [verified-fetch: https://coregroup.org/resource-library/designing-for-behavior-change-for-agriculture-natural-resource-management-health-and-nutrition/]
- The planning frame in which the result is written: Priority Group, Influencing Group, Determinants, "Bridges to Activities". Built on AED's BEHAVE framework per the fetched page, which does not mention TOPS.
- The dossier records the concept of writing Bridges to Activities for flagged determinants but not a wording template. The "increase the perception among <priority group> that ..." form used in the skill follows this skill's drafting instructions; the author should confirm it against the guide.
- Section B16 lists CORE Group DBC among practitioner process frameworks with no peer-reviewed validation: attribute to the organization, do not describe as validated.

## Related, from the questionnaire entry (not cited by this skill)
- Davis, T. (2010). *Barrier Analysis Facilitator's Guide*. Food for the Hungry. [verified-fetch: https://coregroup.org/resource-library/barrier-analysis-facilitators-guide/]. The fetched page says the tool is "built around eight determinants"; Kittle uses twelve. If a tally arrives with eight determinants, the skill says which list it is tabulating.
- Save the Children use of Barrier Analysis: [unverified, author to confirm].
- Practitioner sources named in the dossier for this skill: CORE Group, Food for the Hungry.

## Numbers quoted in the skill, and where they come from
- 45 Doers and 45 Non-Doers; relative risk 3.0; 80% power: Kittle 2013, per the dossier.
- 15 percentage points; p < .05: Kittle, lessons 5 and 12, per the dossier.
- Twelve determinants: the labs report, from Kittle (see the questionnaire skill's notes).
- No effect sizes exist for this method; none are quoted. The percentages and p-values in the worked example are illustrative.

## Non-WEIRD evidence
- The dossier's entry for this skill: "LMIC-native (same as the questionnaire skill)".
- From the questionnaire entry: origin in LMIC water, sanitation, and nutrition programming; a Zambia facility-births Barrier Analysis by People in Need cited in the labs report (no citation details in the dossier); CORE Group's "Powerful to Change" analysis links Barrier Analysis or Doer/Non-Doer use to the highest behavior change among the programs it reviewed, which the dossier marks as an association, not a validation.
- Consequence for the skill: `weird: likely-generalizes`, the dossier's proposed value. The method's conventions carry no population assumption, but generalizing is not the same as validated.

## Replication status (as recorded)
- "Heuristic thresholds; no validation."
- Boundary note: the 15-point rule is a convention; CORE's association between tool use and behavior change is not a validation.
- No publication-bias corrections apply, because no effect is being estimated.

## Corrections and cautions from the dossier
- For this entry: none.
- Carried over from the questionnaire entry: the 2010 Facilitator's Guide uses eight determinants and the 2013 Practical Guide twelve; author names for Kittle and Davis come from the report, not the fetched pages.

## What the skill adds beyond the sources (judgment calls, not evidence)
- Two coders who reconcile, with a codebook anchored in verbatim answers.
- The denominator fixed as the number of respondents in the group.
- A two-sided Fisher exact p-value as the p < .05 check, because the sources do not name the sheet's test.
- Ranking flagged determinants by gap, then coverage, then whether the program can act on them.
- Treating the rule as screening rather than inference, and not routing to `adjust-for-multiple-comparisons`.
- A comparability check on site, sex, and age band before any row is read.
- The Bridge wording pattern (increase or decrease the perception, ability, or access).

## What to check locally
- Whether both groups came from the same communities, and whether the respondent-details block shows an imbalance that could explain a flag.
- Whether the response categories were built from respondents' words or from the team's hypotheses.
- Whether the Doer rule held up in the field (reclassifications, borderline cases) and whether Doer status was verified or self-reported.
- Whether the top-ranked Bridges are things the program can act on in this setting.
- Which determinant list (eight or twelve) the questionnaire followed.
