---
name: translate-survey-instrument
description: >-
  Use when a team has survey items or a questionnaire in one language and
  needs it in another ("translate our survey into Chichewa", "we need the
  Swahili version of this scale", "our enumerators translate on the fly").
  Also use when a translation exists but nobody can say how it was made or
  why items were changed. Produces a target-language instrument through two
  or more independent forward translations, committee reconciliation, a
  documented decision on back-translation, and an item-by-item decision log,
  following the ITC guidelines, Beaton et al., and the TRAPD approach, with
  the pretest handed to draft-cognitive-interview-script. Do not use when
  the items do not exist yet; use draft-survey-items. Not for pretesting
  items with respondents (draft-cognitive-interview-script), for moving an
  instrument to phone delivery (adapt-survey-for-phone-mode), for choosing
  an existing validated measure, or for developing or validating a new
  scale; those last two are separate skills.
license: CC-BY-4.0
metadata:
  title: Translate a survey into another language
  type: atomic
  stage: measure
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "measurement, survey-design"
  consumes: "survey-items"
  produces: "survey-items"
---

## What it does

Produces a target-language version of a survey instrument in which every wording choice is recorded item by item: what changed, why, what was kept non-literal on purpose.

Translation here means moving meaning, not words. Two or more people translate independently, a committee that includes someone from the respondent population reconciles the versions, the team decides whether to back-translate and writes down why, and the reconciled version goes to a cognitive-interview pretest before anyone fields it. The output is a translated instrument plus its decision log. It is not a validated scale, and this skill never claims that it is.

## When to use it

### Use it when
- A team has items in English, French, Hindi, or another source language and the survey will run in a language the respondents actually speak; someone asks "can you translate this?" or "we need the Chichewa version"
- A translation was done by one person (a field coordinator, an enumerator, a consultant) with no record of the choices made, and the team wants to redo it so a reviewer can see why each item reads the way it does
- Enumerators have been translating orally at the point of interview and the team wants one fixed version that everyone reads the same way
- Someone asks "should we back-translate?", "is one translator enough?", or "which dialect should we use?"

### Do not use it when
- The items do not exist yet; write them with `draft-survey-items`, then come back
- The translation exists and the question is whether respondents understand it; that is `draft-cognitive-interview-script`, which this skill hands its output to as the pretest step
- The instrument is moving from face-to-face to phone or IVR delivery; `adapt-survey-for-phone-mode` handles the mode change, before or after translation
- The team wants to pick an existing validated measure for a construct, or to build and validate a new scale (item pools, factor structure, reliability); choosing an existing measure and developing or validating a new scale are separate skills, and translation is neither

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The source instrument, every item verbatim with response options and instructions, and the source language. If it is a published scale, its name and whether the team needs scores comparable to other uses of it.
2. **Required.** The target language, the dialect or region, and the respondents: age, schooling, and whether an enumerator will read the items aloud or respondents will read them. The written standard of a language is often not what respondents speak.
3. **Required.** What each item or scale intends to measure, one phrase each. Translators need the construct, not just the words; without it they translate literally.
4. **Required.** Who is available: how many bilingual people, whether any knows the construct, whether any belongs to the respondent population or works with it daily, and whether a committee meeting can happen.
5. Optional. Whether a funder, ethics board, or scale owner requires back-translation, and the budget for a pretest.

If 1 to 3 are missing, ask and stop. If 4 is missing, ask once; if the answer is still thin, proceed assuming two forward translators, one of whom knows the construct, and mark the staffing plan as an assumption. If 5 is missing, assume no formal requirement and plan the pretest at the default `draft-cognitive-interview-script` uses.

## What it draws on

- International Test Commission (2018). ITC Guidelines for Translating and Adapting Tests (Second Edition). *International Journal of Testing*, 18(2), 101–134. https://doi.org/10.1080/15305058.2017.1398166
- Beaton, D. E., et al. (2000). Guidelines for the process of cross-cultural adaptation of self-report measures. *Spine*, 25(24), 3186–3191. https://doi.org/10.1097/00007632-200012150-00014
- Sousa, V. D., & Rojjanasrirat, W. (2011). Translation, adaptation and validation of instruments or scales for use in cross-cultural health care research: A clear and user-friendly guideline. *Journal of Evaluation in Clinical Practice*, 17(2), 268–274. https://doi.org/10.1111/j.1365-2753.2010.01434.x
- Harkness, J. A. (2003). TRAPD (Translation, Review, Adjudication, Pretest, Documentation). In Harkness, van de Vijver, & Mohler (Eds.), *Cross-Cultural Survey Methods*. Wiley. Unverified, author to confirm: the book exists; the chapter attribution was not confirmed.
- J-PAL. *Survey design*, translation section. https://www.povertyactionlab.org/resource/survey-design
- EGAP. *10 Things to Know About Survey Design*. https://egap.org/resource/10-things-to-know-about-survey-design/ (listed on EGAP's methods guides page; the guide itself was not fetched)

The ITC guidelines set out 18 guidelines in six sections for translating and adapting tests across languages and cultures. Beaton et al. describe a staged adaptation process for self-report measures in which back-translation is a core stage; Sousa and Rojjanasrirat give a step-by-step version of the same process for health care research. TRAPD (Translation, Review, Adjudication, Pretest, Documentation) is the committee approach from cross-cultural survey methodology: several translators work independently, reviewers reconcile, an adjudicator decides, the instrument is pretested, and every decision is documented. J-PAL's guidance is simpler: a fluent speaker translates, then an independent back-translation. The sources disagree about back-translation. The TRAPD school treats it as weak quality assurance, because a translation that back-translates cleanly may simply be literal, and prefers committee review; Beaton keeps it as a stage; J-PAL recommends it. This skill treats back-translation as a decision to make and record, not a default, and adds two judgment calls of its own: the reconciliation committee must include a member of the respondent population or someone who works with them daily, and the decision log must say what was deliberately kept non-literal, since that is what a later reader will otherwise "correct". See `references/evidence-notes.md`.

**WEIRD skew:** The guidelines come from international testing (ITC) and clinical outcome measurement (Beaton; Sousa and Rojjanasrirat), written for moving instruments between languages, so the procedure is not tied to a WEIRD population. What skews is the source instruments: most were developed in English for North American or European respondents, so the construct, the response format, and the recall frame may carry assumptions the target population does not share. A user elsewhere should check the dialect respondents speak, whether items will be read aloud, and whether each construct exists locally. **Non-WEIRD evidence:** a systematic review of Beaton guideline use in Brazil (Revista Mundo da Saúde) is reported in the dossier without citation details (unverified, author to confirm); otherwise none found in the sources this skill draws on.

**Replication status:** Not an effect, so nothing to replicate; the procedure is a professional standard. One element is contested: whether back-translation adds quality assurance. The dossier records the disagreement (TRAPD against, Beaton and J-PAL for) without a study resolving it, which is why this skill makes it an explicit, documented decision.

## How to do it

1. **Carry the source instrument over verbatim**, with the intended meaning beside each item. Translators work from the meaning; the words are evidence of it, not the target.
2. **Set the adaptation scope before anyone translates.** For each item, mark one of: translate literally; adapt (a local equivalent, such as where people actually get medicine rather than "pharmacy"); or flag that the concept may not exist in the target culture. Flags go to the open questions, not to a translator's guess.
3. **Commission two or more independent forward translations.** At least one translator knows the construct; at least one speaks the dialect respondents speak. Independent means they do not see each other's work, so the divergences later are informative.
4. **Reconcile in committee.** The translators, someone who knows the construct, and a member of the respondent population or someone who works with them daily compare the versions item by item, choose or merge, and record the reason. Divergence between translators marks the items whose meaning is unstable; spend the meeting there.
5. **Decide on back-translation and write the decision down.** Do it when a funder, ethics board, or scale owner requires it, or when the committee has no one who reads both languages well. If done, use a translator who has not seen the source, and treat differences as prompts for committee discussion, not as proof of error.
6. **Write the enumerator-facing version**: instructions, transitions, and response options as they will be spoken or read.
7. **Keep the decision log item by item**: source text, final text, what changed from a literal rendering, why, and whether it was kept non-literal on purpose. This is the document a reviewer, a later translator, or the scale owner will ask for.
8. **Plan the pretest.** Hand the reconciled instrument with intended meanings to `draft-cognitive-interview-script`, and flag the items where the translators diverged most for extra probes.
9. **Stop here.** The pretest finds the comprehension problems; fielding, and any claim about validity, comes after it.

See `references/worked-example.md` for a complete run on a Malawi antenatal iron-folate adherence questionnaire.

## Output template

```markdown
# Translated instrument: <instrument name>, <source language> to <target language, dialect>

**Respondents:** <who, region, schooling, read aloud or self-completed>
**Team:** <forward translators: role, knows the construct?, native dialect?; committee members; back-translator if any>
**Published scale:** <yes, name, comparability required / no>

## 1. Scope decisions
| Item | Literal / adapt / flag concept | Reason |
|---|---|---|
| <1> | <...> | <...> |

## 2. Forward translations and reconciliation
| Item | Source text | Translation A | Translation B | Reconciled version | Why this version |
|---|---|---|---|---|---|
| <1> | <...> | <...> | <...> | <...> | <...> |

## 3. Back-translation decision
<done or not done, and why; if done: who, which differences the committee discussed, and how it resolved them>

## 4. Final instrument (enumerator version)
<instructions, each item, response options as they will be spoken>

## 5. Decision log
| Item | Changed from literal? | Why | Kept non-literal on purpose? |
|---|---|---|---|
| <1> | <...> | <...> | <yes: reason / no> |

## 6. Pretest plan
<items flagged for extra probes; number of cognitive interviews; who runs them; handed to draft-cognitive-interview-script>

## Open questions
- <a concept the committee could not place in the target culture>
- <an item still unresolved; a comparability concern for a published scale>
```

## Where it goes wrong

- **Translating words instead of constructs.** Given items without intended meanings, the model produces a literal rendering that preserves idiom and loses meaning. Every item carries its intended meaning into the committee table, and the log says what the item is for.
- **One translator, no record.** A single bilingual colleague's translation is an input to this skill, not a substitute for it; without a second independent version there is nothing to reconcile and no way to see where meaning is unstable.
- **Back-translation as proof.** A back-translation that matches the source shows only that the translation is literal. A deliberately adapted item will back-translate badly and may still be the right version. The committee judges; the back-translation informs.
- **The written standard instead of the spoken dialect.** Formal, written, or prestige forms of a language read well to educated reviewers and sound foreign when read aloud to respondents. The dialect question in "Before you start" exists to prevent this, and the committee member from the population is the check.
- **Silently changing a published scale.** If scoring depends on exact wording, every adaptation goes in the log and comparability is an open question for the scale owner or a psychometrician, not something the committee settles alone.
- **Claiming validity.** A translated and pretested instrument is a translated and pretested instrument. The skill must not describe it as validated or equivalent; that is a separate skill's job.

## When to bring in a specialist

Tell the user to consult a psychometrician or a cross-cultural survey methodologist when:
- The committee cannot find a target-language equivalent for a construct, or the pretest shows respondents paraphrasing an item as something else; the question has become whether the construct exists or means the same thing here, which is a validation question, not a translation question
- The instrument is a clinical screener (PHQ-9 and similar) whose cut-offs will be used for referral or eligibility; cut-offs need local validation before any decision rests on a translated score
- Scores will be compared across languages or countries, or against a published norm; wording changes made for comprehension can break that comparison

Bring them: the decision log with the divergent items marked, the scope decisions, and the pretest tabulation if the pretest has run.
