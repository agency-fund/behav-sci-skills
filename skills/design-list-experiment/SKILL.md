---
name: design-list-experiment
description: >-
  Use when a program needs to know how common a sensitive behavior is
  (unprotected sex, missed doses, bribes, resold inputs) and expects
  respondents to deny it if asked directly. Also use when someone says "people won't admit that on a survey", "our self-report
  numbers look too good", or asks for an "item count", "unmatched count",
  or "list experiment" question. Produces a list experiment design: a
  control list of innocuous items, a treatment list that adds the sensitive
  item, the randomization, a counting comprehension check, sample size
  inputs, a direct comparison question, and the analysis plan, following
  Blair and Imai's design rules and the pooled evidence that the method buys
  a modest bias correction at a high cost in variance. Do not use when the
  behavior is not sensitive or a well-worded direct question would be
  answered honestly; use draft-survey-items. Not for measuring what people
  think others do or approve of (draft-norms-vignette), and not for
  computing the sample size (estimate-sample-size).
license: CC-BY-4.0
metadata:
  title: Measure a sensitive behavior without asking directly
  type: atomic
  stage: measure
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: mixed-evidence
  tags: "list-experiment, survey-design, measurement, quantitative"
  consumes: "measurement-plan"
  produces: "survey-items"
---

## What it does

Designs an item-count question that estimates how common a sensitive behavior is in a population without asking any respondent to admit it.

The design in one sentence: a control group hears three to five innocuous statements and reports how many apply to them, not which; a treatment group hears the same list plus the sensitive statement; the difference in mean counts between the two groups estimates the share of the population for whom the sensitive statement is true. No individual answer reveals anything, which is the protection. The price is noise: the estimate is a difference of two means of counts, so it needs a far larger sample than a direct question, and it can only ever describe the group, never a person.

## When to use it

### Use it when
- A program needs a prevalence estimate for a behavior people hide (unprotected sex, missed medication doses, bribes, reselling subsidized inputs, selling a vote) and the direct-question numbers look implausibly low or high
- Someone says "nobody will admit that on a survey", "our self-report looks too good", or asks for an "item count", "unmatched count", or "list experiment" question
- A measurement plan names a sensitive outcome and the team wants a second estimate beside the direct question to see how much respondents under-report
- The survey is already anonymous but an interviewer is present, so the worry is social desirability rather than data security

### Do not use it when
- The behavior is not sensitive, or a well-worded direct question would be answered honestly; `draft-survey-items` writes that question
- The question is what respondents think others do or approve of, not what they themselves do; `draft-norms-vignette` measures expectations
- The team needs the sample size number; this skill produces the inputs, `estimate-sample-size` produces the N
- The team needs a measure per person (to target, follow up, or score individuals); a list experiment estimates a group share and cannot classify anyone

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The sensitive behavior as who, what, over what recall window, and why it is sensitive here (illegal, shameful, risky to admit to this interviewer). Paste the measurement plan if one exists.
2. **Required.** The population and the survey mode: literacy and numeracy, language, face-to-face, phone, or self-administered, and whether an interviewer is present. Counting statements in one's head is the hard part of this design, and the mode decides whether it can be done at all.
3. **Required.** Roughly how many respondents the team can afford, and whether the estimate is needed for the whole sample only, for subgroups, or for a comparison between experimental arms. The design spends sample fast; this answer decides whether it is feasible.
4. Optional. Whether a direct question on the same behavior will also be asked, and to whom.
5. Optional. The survey the items must sit in (topic, length, tone), so the control items do not stand out.

If 1 to 3 are missing, ask and stop. If 4 is missing, assume the direct question is asked to everyone after the list. If 5 is missing, assume the items stand alone and say so.

## What it draws on

- Blair, G., & Imai, K. (2012). Statistical analysis of list experiments. *Political Analysis*, 20(1), 47–77. https://doi.org/10.1093/pan/mpr048
- Blair, G., Coppock, A., & Moor, M. (2020). When to worry about sensitivity bias: A social reference theory and evidence from 30 years of list experiments. *American Political Science Review*, 114(4), 1297–1315. https://doi.org/10.1017/S0003055420000374
- Chuang, E., Dupas, P., Huillery, E., & Seban, J. (2021). Sex, lies, and measurement: Consistency tests for indirect response survey methods. *Journal of Development Economics*. https://doi.org/10.1016/j.jdeveco.2020.102582
- EGAP. *10 Things to Know About Survey Experiments*. https://egap.org/resource/10-things-to-know-about-survey-experiments/ (listed on EGAP's methods-guides page; the guide itself was not fetched in the evidence audit)

Blair and Imai set out the design rules this skill follows: control items chosen so that few respondents answer zero or all (floor and ceiling effects, which expose treatment respondents at the extremes and push them to lie), the sensitive item randomized into one list, and tests for design effects, where adding the sensitive item changes how respondents answer the control items. Blair, Coppock, and Moor pooled 30 years of list experiments against direct questions and found that sensitivity bias, the gap between what people report and what the list estimates, is usually under 10 percentage points, while the list design pays for its protection in variance. The judgment calls this skill adds: decide whether the bias is worth the variance before designing anything; treat the counting task as the main failure point in oral, low-literacy surveys and require a practice list; and always field a direct question beside the list so the bias is measured, not assumed.

**WEIRD skew:** Most of the pooled evidence comes from US and comparative-politics surveys of literate respondents (voting, prejudice, vote buying), where counting a read-aloud list is easy. A user elsewhere should check whether respondents can hold five statements in mind and report a count, and whether the control items are innocuous in this setting. **Non-WEIRD evidence:** Chuang, Dupas, Huillery, and Seban ran consistency tests of indirect response methods, list experiments among them, in Cameroon and Côte d'Ivoire; the 30-year meta-analysis includes vote-buying list experiments across many countries. The dossier records the settings and the test design, not the magnitudes, so no non-WEIRD effect size is quoted here.

**Replication status:** Mixed. The estimators are standard and the method is widely used, but the pooled evidence says it is low-powered, does not always beat a direct question, and runs into comprehension problems in low-literacy samples. Treat every list experiment as a design to be validated against its direct question, not as an automatic improvement.

## How to do it

1. **Decide whether the bias is worth the variance.** State a prior on under-reporting (the pooled "usually under 10 points" unless the behavior is illegal or stigmatized here, in which case say why it could be larger) and the affordable sample from question 3. A list estimate needs a multiple of the sample a direct question needs; if the team cannot afford that, stop and say the design would add noise rather than accuracy, and suggest a carefully worded direct question with `draft-survey-items`.
2. **Write the sensitive item** as one plain statement in the respondent's words, with the same tense and recall window the direct question would use, true or false for every respondent, with no justifying clause. "In the past three months I had sex without a condom with someone whose HIV status I did not know" is an item; "I sometimes take risks" is not.
3. **Choose three to five control items** from the same general topic area so the sensitive item does not stand out, each unrelated to the sensitive behavior, with prevalences spread from low to high and at least one pair that is negatively correlated (someone who says yes to one tends to say no to the other), so that few respondents answer zero or all. Write the expected prevalence of each and show the floor and ceiling reasoning. See `references/evidence-notes.md` for why this step carries the design.
4. **Randomize assignment at the individual level,** half control and half treatment, generated in advance (not by the interviewer), balanced within interviewer, with the version recorded on each record. Place the sensitive item in the middle of the treatment list, never first or last.
5. **Write the delivery script and the comprehension check:** the instruction read aloud ("I will read some statements; tell me only how many are true for you, not which ones"), a practice list on a neutral topic with a known correct count, a counting aid for oral settings if literacy is low (the respondent sets aside a stone or bean per true statement, out of the interviewer's sight), and the rule for what the interviewer does if the respondent starts naming items.
6. **Add the direct question** on the same behavior, asked to everyone after the list (or to a separate random group if the team prefers), so that list estimate minus direct estimate is the measured sensitivity bias.
7. **Hand the sample size inputs to `estimate-sample-size`:** the estimand (a difference in mean counts), the expected prevalence, the expected variance of the control count given the items, and any subgroup or arm comparison. Do not compute the N here.
8. **Write the analysis plan:** difference in means with standard errors; the design-effect test; floor and ceiling diagnostics (the share of control respondents answering zero or all); the list-versus-direct comparison; the software (the `list` package in R implements the Blair and Imai estimators); and the decision rule for which estimate to report. Pre-specify it before fielding.
9. **Stop here.** Send the items and the script to `draft-cognitive-interview-script` to pretest the counting task with a handful of respondents, and the inputs to `estimate-sample-size`.

See `references/worked-example.md` for a complete run on a Lagos HIV self-testing program.

## Output template

```markdown
# List experiment design: <sensitive behavior>

**Behavior measured:** <who, what, recall window> **Why sensitive here:** <reason>
**Population and mode:** <who; literacy; language; face-to-face / phone / self-administered; interviewer present?>
**Affordable sample:** <n, illustrative> **Estimate needed for:** <whole sample | subgroups | arm comparison>

## Is the bias worth the variance?
<prior on under-reporting and why; the sample multiple a list estimate needs; go or no-go, with the reason>

## Items
**Sensitive item (treatment list only):** "<statement>"
**Control items (both lists):**
1. "<statement>" (expected prevalence: <low / mid / high>, illustrative)
2. "<statement>" (...)
3. "<statement>" (...)
**Floor and ceiling check:** <why few respondents will answer zero or all; which pair is negatively correlated>
**Treatment list order:** <position of the sensitive item>

## Randomization
<unit; ratio; how assignment is generated and recorded; who must not know the version>

## Delivery script and comprehension check
<instruction read aloud; practice list with its correct count; counting aid, if any; rule when a respondent names items>

## Direct comparison question
"<item>" asked to <whom>, <when relative to the list>

## Sample size inputs (for estimate-sample-size)
- Estimand: difference in mean counts between lists
- Expected prevalence: <p>; expected variance of the control count: <reasoning from the items>; subgroups or arms: <...>
- The list estimate needs a multiple of the direct-question sample; the N is computed there, not here

## Analysis plan
- Difference in means with standard errors; software: <...>
- Design-effect test; floor and ceiling diagnostics; list minus direct = measured sensitivity bias
- Decision rule: <when to report the list estimate, the direct estimate, or both>

## What to check before relying on this
- <the control item most likely to be misread or non-innocuous locally>
- <whether respondents in this mode can count five statements; the pretest that settles it>
```

## Where it goes wrong

- **Running it where a direct question would do.** Sensitivity bias is usually under 10 points and the list design costs variance; a sample that cannot detect a 10-point bias produces a noisier number than the direct question it was meant to correct. The go-or-no-go section is mandatory for this reason.
- **Control items with a floor or a ceiling.** If many control respondents answer zero or all, treatment respondents at those extremes are exposed and shade their answers, and the estimate is biased in the direction the design exists to remove. Items with spread prevalence and a negatively correlated pair are the fix; a longer list is not.
- **A sensitive item that is not a single plain statement.** A justification clause, a double-barreled item, or a different recall window from the direct question makes the list and direct estimates incomparable.
- **Counting failure in oral surveys.** Respondents name items, lose count, or answer for the last item only. The script must carry the "how many, not which" instruction, a practice list, and a counting aid, and the output must say plainly when the mode makes the design infeasible.
- **Reading the list estimate as individual data.** The design cannot say which respondent did the behavior; any attempt to score, target, or follow up individuals from it must be refused.
- **Skipping the direct comparison.** Without it, the team cannot say whether the list experiment corrected anything, and the variance was spent for nothing.

## When to bring in a specialist

Tell the user to consult a survey statistician, and the organization's ethics board, when:
- The behavior is illegal or dangerous to disclose even in aggregate (drug use, same-sex behavior, political activity in a repressive setting): a prevalence estimate for a named village or group can be used against that group, so the question is whether to measure it at all, not how
- The affordable sample is not a multiple of what the direct question would need, or the estimate must hold for subgroups; the design-effect and power questions need someone who runs these calculations routinely
- The list estimate is the primary outcome of an evaluation, where power, pre-registration, and the choice between estimators need a statistician's sign-off

Bring them: the sensitive and control items with expected prevalences, the prior on under-reporting, the affordable sample, the mode, and the draft analysis plan.
