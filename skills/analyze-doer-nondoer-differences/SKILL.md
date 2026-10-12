---
name: analyze-doer-nondoer-differences
description: >-
  Use when the Doer/Non-Doer interviews of a Barrier Analysis are done and you
  want to know which determinants separate the people who do the behavior from
  those who do not. Also use when a team has the tally sheet or verbatim
  answers from about 45 Doers and 45 Non-Doers and asks "which barriers
  matter?" or "what do we do with these answers?". Codes the open answers into
  response categories, tabulates the percentage of each group giving each
  response, flags gaps of 15 percentage points or more (Kittle's Practical
  Guide, 2013/2017), writes one Bridge to Activities per flagged determinant
  (CORE Group DBC, 2013), and ranks them into a barrier diagnosis. Do not use
  when the interviews were long, open-ended TDF or COM-B interviews with no
  Doer/Non-Doer split; use synthesize-interview-findings instead. Not for
  writing the questionnaire (draft-barrier-analysis-questionnaire), and not
  for choosing what to do about a flagged determinant (select-intervention-
  levers).
license: CC-BY-4.0
metadata:
  title: Compare Doers and Non-Doers to find the barriers
  type: atomic
  stage: analyze
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "barrier-analysis, qualitative, quantitative, diagnosis"
  consumes: "qualitative-data, interview-guide"
  produces: "barrier-diagnosis"
---

## What it does

Finds the determinants on which Doers answered differently from Non-Doers in a Barrier Analysis.

Barrier Analysis asks the same short questions of people who do one behavior (Doers) and people who do not (Non-Doers), across twelve determinants, the factors that make the behavior more or less likely. This skill takes the answers, codes them into response categories, tabulates the share of each group giving each response, flags the determinants where the groups differ, and writes each flagged determinant as a Bridge to Activities: a one-sentence statement of what the program must change in the priority group's perception, ability, or situation. The output is a barrier diagnosis. The questionnaire comes from `draft-barrier-analysis-questionnaire`; what to do about the barriers is `select-intervention-levers`.

## When to use it

### Use it when
- A Barrier Analysis is complete and the team has a tally sheet, a spreadsheet of coded responses, or a pile of questionnaires with each respondent marked Doer or Non-Doer
- Someone asks "which determinants matter?", "which barriers came out?", or "what do we do with the Doer/Non-Doer answers?"
- A team is about to pick activities from the raw answers ("lots of people mentioned distance, so let's add outreach") without comparing the two groups
- A donor or partner expects Barrier Analysis results in the Designing for Behavior Change format: flagged determinants with Bridges to Activities

### Do not use it when
- The data are transcripts or notes from a few long, open-ended interviews with no Doer/Non-Doer classification; that is `synthesize-interview-findings`
- The questionnaire has not been written or the interviews not done; that is `draft-barrier-analysis-questionnaire`
- A determinant is already flagged and the question is which intervention function or technique addresses it; that is `select-intervention-levers`
- The team wants a formal hypothesis test with a controlled error rate across many outcomes; the 15-point rule is a screening convention, not an inferential test, and `adjust-for-multiple-comparisons` is for pre-specified outcome families in an experiment, not for this

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The data, in one of two forms: a coded tally (for each determinant and response category, how many Doers and how many Non-Doers gave it) or the verbatim answers with each respondent's classification. In both cases, the number of Doers and Non-Doers interviewed, since they are the denominators. Paste the questionnaire from `draft-barrier-analysis-questionnaire` if it exists, so the determinant list and wording are known.
2. **Required.** How the Doer rule held up in the field: whether classification was clean or enumerators had to decide borderline cases, how many respondents were excluded or reclassified, and whether both groups came from the same communities. A comparison between groups recruited in different places is a comparison of places.
3. Optional. Whether the answers have been coded, by whom, and with how many coders. If verbatim only, this skill proposes the categories and the coding needs two people.
4. Optional. The priority group's name as the program uses it ("mothers of children under two in the 24 villages"), for the Bridge wording.

If 1 is missing, ask and stop. If 2 is missing, ask once; if still unanswered, proceed and mark the comparability section "not checked: user to confirm". If 3 is missing, assume the answers are uncoded and include the coding step. If 4 is missing, use the actor from the behavior statement.

## What it draws on

- Kittle, B. (2013; 2nd ed. 2017). *A Practical Guide to Conducting a Barrier Analysis*. Helen Keller International. Lessons 5 and 12. https://coregroup.org/resource-library/a-practical-guide-to-conducting-a-barrier-analysis/
- CORE Group (2013). *Designing for Behavior Change: For Agriculture, Natural Resource Management, Health and Nutrition*. CORE Group, Food Security and Nutrition Network, USAID. https://coregroup.org/resource-library/designing-for-behavior-change-for-agriculture-natural-resource-management-health-and-nutrition/

Kittle's Practical Guide supplies the method this skill reproduces: a sample of 45 Doers and 45 Non-Doers, derived from a case-control calculation (relative risk 3.0, 80% power); coding of the open answers; tabulation of the percentage of each group giving each response; and the rule for flagging a determinant, a Doer/Non-Doer gap of at least 15 percentage points, or p < .05 in the guide's Excel tabulation sheet. The Designing for Behavior Change guide places the result in its planning frame (Priority Group, Influencing Group, Determinants, Bridges to Activities): each flagged determinant becomes a Bridge to Activities, the statement that links what the analysis found to the activities the program will choose. The judgment calls this skill adds: coding is done by two people who reconcile, because categories built by one reader drift toward that reader's hypotheses; the denominator is always the number of respondents in the group, not the number of responses; flagged determinants are ranked by the size of the gap and by how many respondents the response covers, because a 20-point gap on a response three people gave is not a program priority; and the p-value in `scripts/doer_nondoer_tab.py` is a two-sided Fisher exact test, offered as a check on the gap rather than a confirmatory result, since the sources do not record which test the sheet uses.

**WEIRD skew:** the method was built in and for nutrition, health, and sanitation programs in low- and middle-income countries, and its tabulation and Bridge conventions carry no population assumption beyond that. **Non-WEIRD evidence:** the origin is LMIC water, sanitation, and nutrition programming; the labs report cites a Zambia facility-births Barrier Analysis by People in Need; and CORE Group's "Powerful to Change" analysis links Barrier Analysis or Doer/Non-Doer use to the highest behavior change among the programs it reviewed, which is an association between tool use and results, not a validation of the tool. A user anywhere should check that the response categories are built from local words, that both groups came from the same communities, and that the determinants with the largest gaps are ones the program can act on.

**Replication status:** heuristic thresholds with no validation found. The 15-point rule and the p < .05 line are conventions for screening twelve determinants, not tested cutoffs; the 45/45 sample is a design calculation, not an empirical result; and the CORE Group association is not evidence that flagged determinants are causal.

## How to do it

1. **Carry over the behavior, the Doer and Non-Doer rules, and the sample achieved**: Doers, Non-Doers, excluded, reclassified. Check comparability from the respondent-details block (age band, sex, site) and say in the output whether the groups look alike; an imbalance on site is a confound for every row that follows.
2. **Code the open answers, one determinant at a time.** Read every answer for that determinant across both groups, build response categories from the words respondents used (not from the team's hypotheses), and give each category one verbatim anchor. Two coders code independently, compare, and reconcile; record the categories they disagreed on. A respondent who gives two responses is counted once under each; a respondent counts at most once per category. If a coded tally is supplied, check its categories against a sample of verbatim answers before using them.
3. **Tabulate.** For each determinant and response category: Doer count and percent of Doers, Non-Doer count and percent of Non-Doers, and the difference in percentage points (Doer minus Non-Doer). The denominator is the number of respondents in the group. `scripts/doer_nondoer_tab.py` reads a CSV with columns `determinant, response, doer_count, nondoer_count, n_doers, n_nondoers` and prints the percentages, the difference, a two-sided Fisher exact p-value, and the flag; `--help` lists the options and `--self-test` checks the arithmetic.
4. **Flag by the rule**: an absolute difference of 15 points or more, or p < .05. Write next to the table that this is a heuristic from Kittle's guide with no validation, that twelve determinants with several responses each produce many comparisons, and that the p-values describe the gap rather than confirm it. Do not report them as significance tests, and do not send the user to `adjust-for-multiple-comparisons`; the screening question here is which determinants to carry forward, not which effects are real.
5. **Read the direction of each flag.** A response more common among Doers is an enabler the program can reinforce; one more common among Non-Doers is a barrier to remove. Note the coverage: what share of the relevant group gave it.
6. **Write one Bridge to Activities per flagged determinant**, in the Designing for Behavior Change form: "Increase the perception among <priority group> that <...>", "Increase the ability of <priority group> to <...>", "Decrease the perception among <priority group> that <...>", "Increase access to <...> for <priority group>". The Bridge names the determinant and the direction of change; it does not name an activity.
7. **Rank the flagged determinants** by size of gap, then by coverage, then by whether the program can act on them. If more than a handful are flagged, say which the ranking puts first and why; a diagnosis that carries every flag forward has not ranked anything.
8. **List what was not flagged**, including determinants where both groups said the same thing (these are not barriers, whatever the team expected) and responses almost nobody gave.
9. **Stop here.** The barrier diagnosis is the input to `select-intervention-levers`, which chooses the intervention function and technique for each Bridge. Do not propose activities.

See `references/worked-example.md` for a complete run on household latrine use in Lombok, Indonesia, and `references/evidence-notes.md` for the sources.

## Output template

```markdown
# Barrier diagnosis: <short name of the behavior>

**Target behavior:** <who + what + when, carried over verbatim>
**Doer:** <rule as applied> | **Non-Doer:** <rule as applied>
**Sample achieved:** <n> Doers, <n> Non-Doers; <n> excluded; <n> reclassified in the field
**Coding:** <two coders, reconciled / tally supplied by the team and spot-checked>
**Flag rule:** absolute difference of 15 percentage points or more, or Fisher exact p < .05 (Kittle 2013/2017 convention; a heuristic, not a validated cutoff)

## Group comparability
- <site, sex, age band: alike or not, and which rows an imbalance could explain>

## Tabulation
| Determinant | Response category | Doers n (%) | Non-Doers n (%) | Difference (points) | p | Flag |
|---|---|---|---|---|---|---|
| <determinant> | <category> ("<verbatim anchor>") | <n> (<%>) | <n> (<%>) | <+/- points> | <p> | <yes/no> |
<... every category under every determinant; p-values are descriptive, see the flag rule ...>

## Flagged determinants, ranked
1. **<determinant>: <response category>.** Doers <%> vs Non-Doers <%>, <points> points. Direction: <enabler to reinforce / barrier to remove>. Coverage: <share of the relevant group>. Anchor: "<verbatim>".
2. ...

## Bridges to Activities
- <determinant>: "Increase the perception among <priority group> that <...>."
- <determinant>: "Increase the ability of <priority group> to <...>."

## Not flagged
- <determinants where the groups answered alike, and what the team expected of them>
- <responses nobody gave, or only a handful gave>

## What to check before relying on this
- <the comparability problem most likely to explain a flag>
- <the category whose coding the coders disagreed on>
- <whether the top-ranked Bridge is something the program can act on>
```

## Where it goes wrong

- **Percent of responses instead of percent of respondents.** Dividing by the number of answers given, rather than the number of Doers or Non-Doers interviewed, inflates every category and makes the groups incomparable when one group gave longer answers. The denominator is the group size.
- **Categories built from the hypotheses.** If the coder starts from "distance", "cost", and "husband", every answer gets filed under one of them and the analysis confirms what the team believed. Build categories from the respondents' words first; map them to hypotheses afterward.
- **Reading 15 points as proof.** With 45 in each group, a 15-point gap is a few respondents, and twelve determinants with several responses each give chance plenty of chances. The rule screens; it does not confirm. Report the gap, the counts, and the caveat together.
- **Flags on rare responses.** A category given by four Doers and no Non-Doers is a 9-point gap that a Fisher test may still flag; it is not a program priority. Rank by coverage as well as gap.
- **Groups from different places.** Doers recruited at the clinic and Non-Doers in distant villages differ on access whatever the determinant questions say. If the comparability check fails, say so above the table and treat the access and norms rows as unreadable.
- **Bridges that are activities.** "Run radio spots about diarrhea" is an activity. "Increase the perception among caregivers that a child's diarrhea is serious" is a Bridge. Activities belong to `select-intervention-levers` and the design stage.

## When to bring in a specialist

Tell the user to consult an experienced formative-research lead who has run Barrier Analysis when:
- The Doer definition turned out to be contested in the field: enumerators reclassified respondents, borderline cases were common, or the rule was changed partway, because the comparison then rests on two groups nobody can define
- The two groups came from different communities, or the achieved sample is well below 45 per group, because the gaps then reflect place or chance more than determinants, and the lead can say whether the data support any diagnosis
- The behavior is sensitive or stigmatized and Doer status rests on self-report, because the Doers may be the better reporters rather than the better doers

Bring them: the tally with counts and denominators, the codebook with anchors, the questionnaire, and the recruitment record by site.
