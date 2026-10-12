# Evidence notes: design-list-experiment

Every source below comes from `docs/plan/2026-10-skill-expansion-dossier.md` (compiled 2026-10-12). Verification tags are carried over as the dossier gives them; nothing has been upgraded or added from memory. Numbers appear only as the dossier writes them.

## The method and its estimators

### Blair & Imai (2012). Statistical analysis of list experiments [verified-crossref]
*Political Analysis*, 20(1), 47–77. https://doi.org/10.1093/pan/mpr048.
- The reference paper for the design rules this skill follows: control items chosen so that few respondents answer zero or all (floor and ceiling effects), the sensitive item randomized into one of two otherwise identical lists, and statistical tests for design effects, where adding the sensitive item changes how respondents answer the control items.
- Supplies the estimators the `list` package in R implements. The dossier names the package; it records no accuracy figures for the estimators.
- The design logic: the difference in mean counts between the treatment list and the control list estimates the population share for whom the sensitive statement is true.

### Blair, Coppock & Moor (2020). When to worry about sensitivity bias [verified-crossref]
*American Political Science Review*, 114(4), 1297–1315. https://doi.org/10.1017/S0003055420000374.
- A meta-analysis of 30 years of list experiments compared with direct questions, with a social reference theory of when respondents shade their answers.
- Number the dossier allows: sensitivity bias is usually under 10 percentage points. The dossier also records that list experiments cost variance (from the research report).
- The dossier does not give k, N, or a pooled effect size for this paper; do not quote any.
- This is the reason the skill makes a go-or-no-go section mandatory: a sample that cannot detect a bias of about 10 points produces a noisier number than the direct question it was meant to correct.

### Chuang, Dupas, Huillery & Seban (2021). Sex, lies, and measurement: Consistency tests for indirect response survey methods [verified-crossref]
*Journal of Development Economics*. https://doi.org/10.1016/j.jdeveco.2020.102582.
- Consistency tests of indirect response survey methods, list experiments among them, in Cameroon and Côte d'Ivoire.
- The dossier records the setting and the test design only; it does not record the results or magnitudes. Do not quote a finding from this paper beyond "ran consistency tests in Cameroon and Côte d'Ivoire".
- Correction applied in the dossier audit: the research report's recalled DOI returned 404; the DOI above was located in the audit and is the one to cite.

## Practitioner sources
- EGAP. *10 Things to Know About Survey Experiments*. [verified-fetch: https://egap.org/resource/10-things-to-know-about-survey-experiments/]. Confirmed as a listing on EGAP's methods-guides page; the guide itself was not opened in the audit, so attribute no specific recommendation to it.
- IPA and J-PAL use of list experiments: [unverified, author to confirm]. Not cited in the skill.

## Non-WEIRD evidence
- Cameroon and Côte d'Ivoire (Chuang et al. 2021), consistency tests of indirect methods.
- Vote-buying list experiments across many countries, included in the 30-year meta-analysis (Blair, Coppock & Moor 2020). The dossier does not name the countries.
- No non-WEIRD effect size or bias estimate is recorded in the dossier.

## Replication status (as the dossier states it)
- Low power.
- Does not always beat a direct question.
- Comprehension problems in low-literacy samples.
- Taken together: mixed. The estimators are standard, the method is widely used, and whether it improves on a direct question is an empirical question for each survey, which is why the skill always fields the direct question beside the list.

## Boundary conditions and design rules (from the dossier entry)
- Three to five control items without floor or ceiling problems.
- Randomize the sensitive item into the treatment list.
- Power for a difference in means.
- Analyze with design-effect tests (the `list` R package).

Design choices this skill adds that are not in the dossier (practitioner judgment, to be reviewed):
- Control items drawn from the same general topic area so the sensitive item does not stand out, with at least one negatively correlated pair.
- The sensitive item placed in the middle of the treatment list.
- A practice list with a known correct count and a counting aid (a stone or bean per true statement, out of sight) for oral, low-literacy settings.
- Individual-level assignment generated in advance and balanced within interviewer.
- The claim that a list estimate needs "a multiple" of the direct-question sample is a qualitative statement of the variance cost; no multiplier is quoted because the dossier gives none.

## Known corrections and cautions (from the dossier)
- Chuang et al. (2021) DOI is 10.1016/j.jdeveco.2020.102582; the report's recalled DOI was wrong.
- The dossier assigns no io types to this skill in the plan; `measurement-plan` (consumes) and `survey-items` (produces) are existing taxonomy ids chosen by the drafter.

## What to check locally
- Whether respondents in this mode can hold five statements in mind and report a count; pretest the counting task with `draft-cognitive-interview-script` before fielding.
- Whether each control item is genuinely innocuous and roughly at the expected prevalence here; an item that is itself sensitive or near-universal breaks the floor and ceiling logic.
- Whether the sensitive behavior is safe to estimate in aggregate for this population; a group-level prevalence can be used against a named village or group even when no individual is identified.
- Whether the affordable sample is a multiple of what a direct question would need; if not, the direct question is the better instrument.
- How large under-reporting plausibly is here; the pooled "usually under 10 points" is a prior from mostly WEIRD political surveys, not a local fact.
