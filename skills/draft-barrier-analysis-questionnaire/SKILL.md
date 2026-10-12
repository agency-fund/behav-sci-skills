---
name: draft-barrier-analysis-questionnaire
description: >-
  Use when you want to compare people who already do a behavior with people
  who do not, to see which determinants separate them, and need the
  questionnaire. Also use when a team says "Doer/Non-Doer", "Barrier
  Analysis", or wants about 90 short structured interviews rather than a few
  long ones. Produces a Barrier Analysis questionnaire in the format of
  Kittle's Practical Guide (2013/2017): screening questions that classify each
  respondent as a Doer or a Non-Doer, then matched open-ended question pairs
  across twelve determinants (self-efficacy, social norms, positive and
  negative consequences, access, cues for action, susceptibility, severity,
  action efficacy, divine will, policy, culture), with pilot and sampling
  notes. Do not use when you want fewer, longer open-ended interviews across
  the 14 TDF domains; use draft-tdf-interview-guide instead. Not for
  generating barrier hypotheses (decompose-comb-barriers), and not for
  tabulating or comparing the answers once collected
  (analyze-doer-nondoer-differences).
license: CC-BY-4.0
metadata:
  title: Write a Doer/Non-Doer Barrier Analysis questionnaire
  type: atomic
  stage: diagnose
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "barrier-analysis, survey-design, qualitative, diagnosis"
  consumes: "target-behavior-brief"
  produces: "interview-guide"
---

## What it does

Writes a Barrier Analysis questionnaire that classifies each respondent as a Doer or a Non-Doer of one behavior, then asks matched open-ended questions across twelve determinants so the two groups' answers can be compared.

Barrier Analysis is a rapid assessment method from nutrition, health, and water-and-sanitation programming in low- and middle-income countries. Interviewers ask the same short questions of people who do the behavior (Doers) and people who do not (Non-Doers), drawn from the same communities, and the program looks for the determinants on which the two groups answer differently. A determinant is a factor that makes the behavior more or less likely; this skill uses the twelve in Kittle's Practical Guide. The skill writes the instrument. `analyze-doer-nondoer-differences` compares the answers once collected.

## When to use it

### Use it when
- A team says "Barrier Analysis", "Doer/Non-Doer study", or "let's ask the people who do it and the people who don't the same questions"
- One behavior is defined (who, what, when) and the team can tell, from a few questions, whether a given person does it or not
- The team wants structured, comparable answers from many short interviews (the method's convention is 45 Doers and 45 Non-Doers) rather than depth from a few long ones
- A program is planning a behavior-change strategy in nutrition, health, agriculture, or sanitation and its donor or partner expects a Barrier Analysis

### Do not use it when
- The team wants fewer, longer, open-ended interviews that explore every domain of a behavior; that is `draft-tdf-interview-guide`
- The question is still "why aren't they doing it?" with no behavior defined; run `define-key-behavior`, then `decompose-comb-barriers` for hypotheses, and bring the behavior here
- The interviews are done and the question is which determinants differ between Doers and Non-Doers; that is `analyze-doer-nondoer-differences`
- Nobody in the population does the behavior yet, or almost everyone does, so one group cannot be recruited; use `draft-tdf-interview-guide` for a diagnosis that does not need two groups

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The target behavior as who, what, when, with a recall window a respondent can answer about ("in the past seven days", "at the last birth"). Paste the brief from `define-key-behavior` if one exists.
2. **Required.** The Doer rule, the Non-Doer rule, and who is excluded. A Doer meets the full behavior statement, including frequency and time window; a Non-Doer does not; a person to whom the behavior does not apply (no child under two, no latrine within reach) is excluded. Say whether Doer status can be verified from a record or observation, or rests on self-report.
3. **Required.** Who will administer the questionnaire, in what language, and how long each interview can take. Barrier Analysis interviews are short, so the determinant questions must be short.
4. Optional. COM-B hypotheses from `decompose-comb-barriers`, or informal explanations. They sharpen the probes under the determinants they map to; all twelve determinants stay in regardless.
5. Optional. Whether the behavior is sensitive (sexual health, violence, substance use, legal status), which affects whether self-reported Doer status can be trusted and whether ethics review is needed.

If 1 is missing, ask and stop (if the user has a goal rather than a behavior, point to `define-key-behavior`). If 2 is missing, ask once; if the answer is still thin, propose Doer, Non-Doer, and exclusion rules from the behavior statement, marked "proposed by this skill, confirm before fieldwork". If 3 is missing, assume trained local enumerators in the local language and mark the assumption. If 4 and 5 are missing, assume no hypotheses and a non-sensitive behavior.

## What it draws on

- Kittle, B. (2013; 2nd ed. 2017). *A Practical Guide to Conducting a Barrier Analysis*. Helen Keller International. https://coregroup.org/resource-library/a-practical-guide-to-conducting-a-barrier-analysis/
- Davis, T. (2010). *Barrier Analysis Facilitator's Guide*. Food for the Hungry. https://coregroup.org/resource-library/barrier-analysis-facilitators-guide/
- CORE Group (2013). *Designing for Behavior Change: For Agriculture, Natural Resource Management, Health and Nutrition*. CORE Group, Food Security and Nutrition Network, USAID. https://coregroup.org/resource-library/designing-for-behavior-change-for-agriculture-natural-resource-management-health-and-nutrition/

Kittle's Practical Guide is the instrument this skill reproduces: a Doer/Non-Doer questionnaire across twelve determinants (perceived self-efficacy, perceived social norms, perceived positive consequences, perceived negative consequences, perceived access, cues for action, perceived susceptibility, perceived severity, perceived action efficacy, perceived divine will, policy, culture), with a sample of 45 Doers and 45 Non-Doers derived from a case-control calculation (relative risk 3.0, 80% power). The earlier Facilitator's Guide (Davis 2010) is built around eight determinants; this skill follows Kittle's twelve and says so in the output. The Designing for Behavior Change guide places Barrier Analysis inside a planning frame (Priority Group, Influencing Group, Determinants, "Bridges to Activities"). The sources say to always include self-efficacy, social norms, and positive and negative consequences, and to pilot the questionnaire. The judgment calls this skill adds: screening questions are written so they do not reveal which answer makes someone a Doer; each determinant is a matched pair with identical wording except for tense and frame, so the two groups' answers are comparable; and answers are recorded verbatim rather than pre-coded, because the method codes after fieldwork.

**WEIRD skew:** the method was developed in and for programming in low- and middle-income countries; its wording and determinant list reflect nutrition, health, and sanitation work rather than any single national culture. **Non-WEIRD evidence:** the origin is LMIC water, sanitation, and nutrition programming; the labs report cites a Zambia facility-births Barrier Analysis by People in Need, and CORE Group's "Powerful to Change" analysis links Barrier Analysis or Doer/Non-Doer use to the highest behavior change among the programs it reviewed, which is an association, not a validation. A user anywhere should check that "divine will", "policy", and "culture" have a local meaning for this behavior, and that the Doer rule can be verified rather than self-reported when the behavior is socially desirable.

**Replication status:** practitioner method; no psychometric validation of the questionnaire or its determinant list was found. The 45/45 sample rule is a design calculation, not an empirical result, and the CORE Group association is not evidence that the tool itself causes better outcomes.

## How to do it

1. **Carry the behavior over verbatim** and write the Doer, Non-Doer, and exclusion rules as operational sentences. State which determinant list the questionnaire follows (Kittle's twelve) so a reader does not confuse it with the eight of Davis 2010.
2. **Write the screening questions.** Ask about the behavior inside the recall window in a way that does not signal the "right" answer, add the exclusion check, and write the classification rule the interviewer applies. If a record or observation can confirm Doer status, say so and prefer it over self-report.
3. **Write a short respondent-details block**: only what is needed to check that Doers and Non-Doers are comparable (age band, sex, site, the household feature that makes the behavior apply). Nothing that identifies the person.
4. **Write one matched pair per determinant, all twelve.** The Doer version asks about what the person does ("what makes it easier for you to..."), the Non-Doer version about what they would do ("what would make it easier for you to..."); the wording is otherwise identical. Keep each question to one sentence. For social norms ask both who approves or disapproves and what most people like them do; for consequences ask good things and bad things as separate determinants; for susceptibility, severity, and action efficacy name the problem the behavior is meant to prevent.
5. **Add one neutral probe per pair** ("anything else?") and the recording rule: write the respondent's words, do not read out options, do not code during the interview.
6. **Order for flow**: screening, respondent details, self-efficacy first (it is the most concrete), then consequences, access, cues, norms, susceptibility and severity, action efficacy, then divine will, policy, and culture. Deliver one instrument with the Doer and Non-Doer wording side by side so the interviewer asks the version that matches the classification.
7. **Mark local referents and translation risks** in brackets: the problem's local name, the people whose approval matters, the services and places, and any determinant whose wording may not carry across languages.
8. **Write the fieldwork notes**: the 45 Doer and 45 Non-Doer target from the same communities, a pilot with a few of each to check that the screening classifies cleanly and the questions are understood, and the pointer to `analyze-doer-nondoer-differences` for tabulation.
9. **Stop here.** Do not compare answers, pick determinants, or write activities; the analysis skill does the first two and `select-intervention-levers` the third.

See `references/worked-example.md` for a complete run on household latrine use in Lombok, Indonesia, and `references/evidence-notes.md` for the sources.

## Output template

```markdown
# Barrier Analysis questionnaire: <short name of the behavior>

**Target behavior:** <who + what + when, carried over verbatim>
**Doer:** <rule> | **Non-Doer:** <rule> | **Exclude:** <rule>
**Doer status verified by:** <record, observation, or self-report only>
**Determinant list followed:** Kittle (2013; 2nd ed. 2017), twelve determinants
**Administered by:** <who> | **Language:** <...> | **Time per interview:** <minutes>

## A. Screening (classify before continuing)
S1. "<question about the behavior in the recall window>"
S2. "<exclusion check>"
Classification: Doer if <...>; Non-Doer if <...>; end the interview if <...>

## B. Respondent details (for comparability only)
- <age band>, <sex>, <site>, <the feature that makes the behavior apply>

## C. Determinant questions (matched pairs)
### 1. Perceived self-efficacy
- Doer: "<...>" | Non-Doer: "<...>"
- Probe: "Anything else?"
### 2. Perceived positive consequences
- Doer: "<...>" | Non-Doer: "<...>"
<... one block per determinant, all twelve, in the running order from step 6 ...>
### 12. Culture
- Doer: "<...>" | Non-Doer: "<...>"

## D. Closing
- "<anything we have not asked that matters>"; thanks; what happens next

## E. Fieldwork notes
- Sample: 45 Doers and 45 Non-Doers from the same communities (Kittle 2013 case-control calculation, RR 3.0, 80% power)
- Pilot: <n> Doers and <n> Non-Doers; check that screening classifies cleanly and every question is understood
- Record answers verbatim; code after fieldwork; the comparison is done in analyze-doer-nondoer-differences

## Local adaptation and translation risks
- <bracketed referent and who fills it>
- <determinant whose wording may not carry; the plain-language alternative>

## What to check before relying on this
- <whether Doer status can be trusted for this behavior>
- <the assumption most likely to be wrong>
```

## Where it goes wrong

- **Screening that reveals the answer.** "Do you wash your hands with soap after using the latrine?" tells the respondent what a good person says. Ask about specific recent occasions and classify from the detail; when the behavior is socially desirable, verify from a record or observation.
- **Doers and Non-Doers from different places.** Doers recruited near the clinic and Non-Doers from the far villages produce differences that are about distance, not determinants. Recruit both groups from the same communities and use the respondent-details block to check for imbalance.
- **Dropping determinants the team cannot imagine mattering.** Divine will, policy, and culture get cut because they sound irrelevant; they stay until a pilot shows they draw nothing. Self-efficacy, social norms, and positive and negative consequences are never cut.
- **Pre-coding the answers.** Turning the open questions into tick-box items before fieldwork fixes the answer set to what the team already believes. The method records verbatim and codes afterward.
- **Mixing the two determinant lists.** Davis 2010 has eight determinants, Kittle 2013 has twelve. A questionnaire that takes some from each cannot be compared with either; state the list and stick to it.
- **Treating the tool as validated.** No psychometric validation was found, and CORE Group's association between tool use and program results is not one. The questionnaire produces comparable answers; it does not guarantee that the determinants it finds are causal.

## When to bring in a specialist

Tell the user to consult an experienced formative-research lead who has run Barrier Analysis, plus the relevant ethics review body, when:
- The behavior is sensitive or stigmatized (HIV testing, contraception, violence, child discipline, substance use), because self-reported Doer status is unreliable and the questions and consent need review
- The Doer definition is contested inside the team (how many days, which source counts, whether partial counts), because a questionnaire built on a disputed rule classifies people wrongly and every later comparison inherits the error
- The population cannot supply 45 of each group from the same communities, because the sample rule cannot be met and a different design is needed

Bring them: the behavior statement, the Doer, Non-Doer, and exclusion rules, the draft questionnaire, and the recruitment plan.
