---
name: draft-norms-vignette
description: >-
  Use when a team wants survey questions that show whether what others do,
  or what others approve of, drives a practice (latrine use, tablets in
  pregnancy, girls' schooling) instead of asking people why they do it.
  Also use when someone says "write a vignette",
  "scenario questions for our norms survey", "how do we measure empirical
  and normative expectations", or a social norm diagnosis ended "pending the
  vignette round". Produces short scenario versions about a named person
  that vary what others do and what others approve of factorially, the
  questions asked after each version, the randomization, and the analysis
  plan, following Bicchieri's measurement chapter and the experimental
  vignette literature. Do not use when the question is the respondent's own
  sensitive behavior; use design-list-experiment. Not for deciding whether
  the practice is a norm (diagnose-social-norm), not for ordinary attitude
  items (draft-survey-items), and not for pretesting the scenes with
  respondents (draft-cognitive-interview-script).
license: CC-BY-4.0
metadata:
  title: Write scenarios that measure what others do and approve
  type: atomic
  stage: measure
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "social-norms, survey-design, measurement, experimental-design"
  consumes: "social-norm-diagnosis"
  produces: "survey-items"
---

## What it does

Writes short scenarios, in versions that differ only in what other people are said to do or to approve of, so a survey can show whether a practice follows those expectations.

Two terms, used throughout. An empirical expectation is what I believe others like me actually do. A normative expectation is what I believe others think I should do. A norms vignette is a brief story about a named person facing one decision; after hearing it, respondents say what that person will do, what most people like them would do, and what others would think of them. The versions vary the two cues factorially (others do or do not; others approve or disapprove), respondents are randomly assigned to one version, and if the predicted behavior shifts with the cues, the practice is norm-driven. A single story with questions after it is not a vignette experiment; the variation is the instrument.

## When to use it

### Use it when
- `diagnose-social-norm` returned "cannot tell" or "pending field answers" on whether the practice is conditional on expectations, and the team wants a survey instrument that varies the expectations instead of asking about them
- Someone asks to "write a vignette", for "scenario questions for the norms survey", or "how do we measure empirical and normative expectations"
- A team wants to ask about a practice without asking respondents to report their own behavior or judge their neighbors to an interviewer's face, because the topic is awkward in this setting
- A program needs a baseline expectations measure it can repeat after a norms intervention, such as one built with `write-social-norm-message` or `plan-collective-pledge`

### Do not use it when
- The question is how common the respondent's own sensitive behavior is; `design-list-experiment` estimates that without asking anyone to admit it
- The practice, the reference group, and the direction of interest are not yet established; run `diagnose-social-norm` first, since its diagnosis supplies the cues this skill varies
- The team wants ordinary attitude, belief, or knowledge items with no variation; `draft-survey-items`
- The scenes are written and need testing with a handful of respondents before fielding; `draft-cognitive-interview-script`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The practice and its dilemma: who does what, when, and the moment at which the decision is made. Paste the social norm diagnosis if one exists; it supplies the practice, the provisional reference group, and the sanction.
2. **Required.** The reference group the cues will name (neighbors in the hamlet, mothers-in-law, other vendors, the congregation). A cue about "people" in general measures nothing; the cue must name the group whose behavior and approval the diagnosis found people track.
3. **Required.** The respondents and the mode: who answers, their literacy and language, oral or written delivery, individual or group setting. Most LMIC surveys deliver vignettes aloud, and the scene must survive being read by a surveyor.
4. **Required.** Whether the practice is harmful, illegal, or stigmatized (female genital cutting, child marriage, violence, HIV status). This decides whether the scene itself could distress a respondent, and it triggers the specialist route before any wording is drafted.
5. Optional. Which cue the program cares about most, and whether each respondent hears one version (between-respondent) or two (within-respondent).
6. Optional. The survey time available and how many practices need a vignette.

If 1 to 3 are missing, ask and stop. If 4 is missing, treat the practice as sensitive until told otherwise and apply the specialist section before drafting. If 5 and 6 are missing, assume one version per respondent, a full two-by-two design, and one practice.

## What it draws on

- Atzmüller, C., & Steiner, P. M. (2010). Experimental vignette studies in survey research. *Methodology*, 6(3), 128–138. https://doi.org/10.1027/1614-2241/a000014
- Bicchieri, C. (2016). *Norms in the Wild: How to Diagnose, Measure, and Change Social Norms*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780190622046.001.0001. Chapter 2, "Measuring Norms" (chapter DOI 10.1093/acprof:oso/9780190622046.003.0002, seen in the evidence audit's Crossref search but not separately audited)
- Institute for Reproductive Health, Georgetown University (2020). *Social Norms Exploration Tool (SNET)*. https://www.irh.org/social-norms-exploration/ (the pages fetched in the evidence audit do not mention vignettes; SNET is cited here for its participatory norms-exploration approach, not for a sample vignette)
- UNICEF Innocenti / Penn Social Norms Group (2016). *Why Do People Do What They Do? A Social Norms Manual for Viet Nam, Indonesia and the Philippines*. Unverified, author to confirm: the manual could not be re-fetched in the evidence audit.

Atzmüller and Steiner describe the experimental vignette study: short, systematically varied descriptions of a situation, presented to respondents whose judgments are then compared across versions. Because versions are assigned at random, a difference in judgment can be attributed to the factor that was varied, which is what separates a vignette experiment from a story followed by questions. Bicchieri's measurement chapter supplies the reason to vary two factors in particular: a practice is a social norm only if the preference to follow it is conditional on empirical and normative expectations, so showing that requires changing those expectations and watching whether the predicted behavior changes. The judgment calls this skill adds: a fixed, named protagonist who shares the respondent's situation, so answers are about a plausible person and not an abstraction; three fixed questions after every version; a personal normative belief question asked before the scene as an anchor; a two-by-two factorial as the default; and a length limit set by oral delivery.

**WEIRD skew:** The factorial vignette method comes from European and North American survey methodology. The norms application was developed for UNICEF and Penn trainings in Southeast Asia and Southern Africa (reported; manual unverified) and is practiced through SNET, a participatory tool applied in over 15 settings. What to check locally: whether respondents are used to reasoning about a hypothetical third person, whether the scene is plausible in this place, and whether respondents answer about the protagonist or quietly about themselves. **Non-WEIRD evidence:** SNET pilots in 15 or more settings (practitioner; countries not named on the fetched pages); UNICEF trainings in Viet Nam, Indonesia, and the Philippines (labs report; manual unverified). The dossier records no quantitative result from a norms vignette study, so no effect size is quoted.

**Replication status:** The factorial vignette design guidance is peer-reviewed, and the logic that a causal claim about norms needs the factorial variation of empirical and normative cues is established in Bicchieri's framework. Whether vignette answers predict real behavior for a given practice is a single-study question each time; the dossier holds no pooled estimate.

## How to do it

1. **Fix one dilemma in one scene.** Name a protagonist who shares the respondents' sex, age, and situation, place the scene somewhere local and ordinary, and bring the person to one decision moment, with no cue sentence yet. Keep the base scene to what a surveyor can read aloud in about 30 seconds; a longer scene buries the cue.
2. **Write the empirical cue in two versions** that name the reference group from question 2: "Most pregnant women in her village take the tablets every day" and "Most pregnant women in her village do not take the tablets." Use the same quantifier in both ("most", or "seven out of ten"), and change nothing else.
3. **Write the normative cue in two versions,** approval and disapproval by the same reference group: "Her mother-in-law and the older women think a pregnant woman should take the hospital tablets" and "... think she should not."
4. **Combine the cues factorially into four versions,** each the base scene plus one empirical and one normative sentence, identical in every other word. Add a fifth, no-cue version only if the sample allows it; it gives a baseline but costs a cell.
5. **Write the three questions asked after every version,** in the third person, with response options fit for oral delivery (three to five labeled points): what the protagonist will do; what most people in the reference group in her position would do; and what the reference group would think of her if she did the practice. Do not ask why; it returns rationalizations, as `diagnose-social-norm` also warns.
6. **Add the personal normative belief question before the scene:** "Do you yourself think a person like <protagonist> should ...?" It is the respondent's own view, not tied to any cue, and it anchors the reading in step 8.
7. **Randomize version assignment** between respondents, one version each, generated in advance and balanced within surveyor, with the version recorded on the record. Use a within-respondent design (two versions, order randomized) only when the sample is small, and say that carryover between versions is the price.
8. **Write the analysis plan.** The outcome is the share answering that the protagonist does the practice, by version. The empirical-cue effect compares the two "most do" versions with the two "most do not" versions; the normative-cue effect compares "approve" with "disapprove"; report the interaction. Read it: a shift with the empirical cue only means a descriptive norm; a shift with the normative cue means a social norm; no shift with either means a custom or a moral rule, and the personal belief question says which. State the sample per version the comparison needs, from a sample-size calculation. See `references/evidence-notes.md` for the evidence behind the reading.
9. **Stop here.** The versions and questions go to `draft-cognitive-interview-script` for pretesting with a handful of respondents, then into the survey; the analysis feeds the call in `diagnose-social-norm`.

See `references/worked-example.md` for a complete run on iron-folate tablets in pregnancy in Malawi.

## Output template

```markdown
# Norms vignette: <practice>

**Practice and dilemma:** <who does what, when; the decision moment>
**Reference group named in the cues:** <from the diagnosis>
**Respondents and mode:** <who; literacy; language; oral or written; individual or group>
**Design:** <two-by-two between-respondent | within-respondent, two versions>; versions: <4 | 5>
**Sensitivity:** <none stated | sensitive: what was changed or withheld, and the specialist review required>

## Personal normative belief (asked before the scene)
"<Do you yourself think a person like PROTAGONIST should ...?>" Options: <labeled points>

## Base scene (identical in every version)
"<named protagonist; local place; one decision moment; about 30 seconds read aloud>"

## Cue sentences
| Factor | Level A | Level B |
|---|---|---|
| Empirical (what others do) | "<Most REFERENCE GROUP ... do>" | "<Most REFERENCE GROUP ... do not>" |
| Normative (what others approve) | "<REFERENCE GROUP think she should>" | "<REFERENCE GROUP think she should not>" |

## Versions
- V1: base + empirical A + normative A
- V2: base + empirical A + normative B
- V3: base + empirical B + normative A
- V4: base + empirical B + normative B
<optional V0: base scene, no cues>

## Questions after every version
1. "What will PROTAGONIST do?" Options: <...>
2. "What would most REFERENCE GROUP in her position do?" Options: <...>
3. "If she <does the practice>, what would REFERENCE GROUP think of her?" Options: <...>

## Randomization
<unit; how versions are generated, assigned, and recorded; balance across surveyors>

## Analysis plan
- Outcome: share answering "<does the practice>" to question 1, by version
- Empirical-cue effect: V1 + V2 versus V3 + V4; normative-cue effect: V1 + V3 versus V2 + V4; interaction
- Reading: <shift with empirical only = descriptive norm; shift with normative = social norm; neither = custom or moral rule, read with the personal belief question>
- Sample per version: <n, illustrative; from a sample-size calculation>

## What to check before relying on this
- <the cue most likely to be heard as information about facts rather than as an expectation>
- <whether respondents answer about the protagonist or about themselves; the pretest probe that settles it>
```

## Where it goes wrong

- **A story instead of an experiment.** One scene with questions after it, or versions assigned by the surveyor's choice, cannot attribute a shift to the cue. Random assignment to versions is the instrument; without it the output is a set of attitude items.
- **Cues about "people" in general.** "Most people take the tablets" names no one the respondent tracks. The cue must name the reference group the diagnosis found, or the effect of the cue says nothing about the norm.
- **Confounded versions.** Changing the protagonist's age, the place, or the wording of the decision between versions means a difference could be anything. Versions differ in the cue sentences and in nothing else.
- **Asking why.** "Why would she do that?" returns the reasons people find acceptable to give. The three questions ask what she will do, what others would do, and what others would think.
- **Scenes too long or too numeric for oral delivery.** Respondents lose the cue in a two-minute story or in a string of percentages; keep the base scene short, the quantifier simple, and pretest the scene aloud.
- **Respondents answering about themselves.** A protagonist too close to the respondent, or questions that slip into the second person, turn the vignette into a self-report. Keep the third person, give the protagonist a name, and add a pretest probe for whom the respondent was thinking of.
- **Drafting a distressing scene.** For a harmful practice, a scene that depicts it in detail, or that reads as endorsing it, can distress a respondent or signal approval. Such scenes must not be drafted before the specialist route below.

## When to bring in a specialist

Tell the user to consult a local qualitative researcher with experience of the practice, and an ethics reviewer, when:
- The practice is harmful, illegal, or stigmatized (female genital cutting, child marriage, intimate partner violence, HIV disclosure), because the scenario itself can distress a respondent, a version in which the reference group approves can be read as endorsement, and the questions need review before any wording is fixed
- Respondents are minors, or the reference group is the household's authority (a husband, a mother-in-law) and interviews cannot be held in private
- The two-by-two design plus the subgroups the program wants push the sample per version below what a statistician would accept; a survey statistician should set the cells before fielding

Bring them: the base scene, the cue sentences, the three questions and the personal belief question, the sampling plan, and the social norm diagnosis the vignette serves.
