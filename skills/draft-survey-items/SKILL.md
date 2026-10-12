---
name: draft-survey-items
description: >-
  Use when a team needs to write survey questions ("write items for our
  baseline", "we need questions that measure X", "turn our measurement plan
  into a questionnaire") for respondents with little schooling or who answer
  orally through an enumerator. Also use when a draft questionnaire leans on
  agree/disagree statements, unlabeled 1-to-10 scales, or reverse-worded
  items and someone asks whether that will work in the field. Produces
  closed-ended items, one idea each, every option labeled in words, an
  enumerator read-aloud version, and a pretest hand-off. Do not use when
  the items exist and the question is whether respondents understand them;
  use draft-cognitive-interview-script. Not for translating items
  (translate-survey-instrument), phone delivery
  (adapt-survey-for-phone-mode), sensitive behaviors that need an indirect
  design (design-list-experiment), choosing an existing validated measure,
  or developing or validating a scale; those last two are separate skills.
license: CC-BY-4.0
metadata:
  title: Write survey questions people can answer
  type: atomic
  stage: measure
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: mixed-evidence
  tags: "measurement, survey-design, quantitative"
  consumes: "measurement-plan"
  produces: "survey-items"
---

## What it does

Writes closed-ended survey items that respondents with little schooling can answer accurately when an enumerator reads them aloud.

Answering a survey item is a cognitive task with four stages: understand the question, retrieve the relevant memory, form a judgment, and map it onto the response options. When the task is too hard, respondents satisfice (give a good-enough answer with the least effort) or acquiesce (agree whatever the content), and the data record the item's difficulty rather than the construct. This skill takes a measurement plan's constructs and writes items that keep each stage easy. It produces draft items for pretesting, not a validated scale.

## When to use it

### Use it when
- A measurement plan names the constructs ("intention to buy fertilizer early", "perceived household support") and someone asks "can you write the questions?" or "we need items for the baseline"
- A draft questionnaire uses agree/disagree batteries, numbered scales with labels only at the ends, or reverse-worded items, and the team asks whether that will work with their respondents
- Enumerators report respondents saying yes to everything, choosing the first option every time, or asking what a question means, and the team wants to rewrite the items rather than retrain
- A team wants the exact words an enumerator should read aloud, including the response options, so every interview asks the same thing

### Do not use it when
- The items exist and the question is whether respondents understand them; run `draft-cognitive-interview-script`, which this skill hands its output to
- The items exist in one language and are needed in another; that is `translate-survey-instrument`
- The survey is moving to phone or IVR delivery; `adapt-survey-for-phone-mode` converts the items
- The behavior is sensitive or stigmatized (sexual behavior, violence, bribes, drug use) and the team wants a better direct question; a better direct question does not remove the social-desirability pressure, and `design-list-experiment` builds the indirect design that does
- The team wants to pick an existing validated measure for a construct, or to build and validate a new scale (item pool, factor structure, reliability); choosing an existing measure and developing or validating a new scale are separate skills, and this one writes draft items only

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The constructs to measure, each with a one-sentence definition and the decision the data will feed. Paste the measurement plan if one exists. A construct without a definition cannot be mapped to an item; "empowerment" is a topic, not a construct.
2. **Required.** The respondents: age, schooling, language, and whether an enumerator reads the items aloud, a phone call delivers them, or respondents read them. Mode decides how many options a scale can carry.
3. **Required.** The length budget (items or minutes for this block) and what comes before and after it in the questionnaire, because earlier items change how later ones are read.
4. Optional. Whether any item must stay comparable to an earlier round or another study; those items are constrained and marked, not rewritten.
5. Optional. Which constructs the team is least sure how to ask about; those get an alternative wording for the pretest.

If 1 or 2 is missing, ask and stop. If 3 is missing, proceed assuming enumerator read-aloud and at most five items per construct (this skill's default, not a finding), and mark the assumption. If 4 and 5 are missing, assume no comparability constraint and give every construct one wording.

## What it draws on

- Krosnick, J. A., & Presser, S. (2010). Question and questionnaire design. In P. V. Marsden & J. D. Wright (Eds.), *Handbook of Survey Research* (2nd ed.). Emerald. (The handbook is confirmed; the chapter's title and authors are as the dossier's report gives them.)
- Tourangeau, R., Rips, L. J., & Rasinski, K. (2000). *The Psychology of Survey Response*. Cambridge University Press. https://doi.org/10.1017/CBO9780511819322
- Laajaj, R., & Macours, K. (2021). Measuring skills in developing countries. *Journal of Human Resources*, 56(4), 1254–1295. https://doi.org/10.3368/jhr.56.4.1018-9805R1
- Harzing, A.-W. (2006). Response styles in cross-national survey research: A 26-country study. *International Journal of Cross Cultural Management*, 6(2), 243–266. https://doi.org/10.1177/1470595806066332
- J-PAL. *Survey design*. https://www.povertyactionlab.org/resource/survey-design
- EGAP. *10 Things to Know About Survey Design*. https://egap.org/resource/10-things-to-know-about-survey-design/ (listed on EGAP's methods guides page; the guide itself was not fetched)
- Gyani, A., Tindall, K., & Gallagher, R. (2022). *Explore Field Guide*, survey section. Behavioural Insights Team. https://www.bi.team/wp-content/uploads/2022/11/BIT-Explore-Field-Guide.pdf

Tourangeau, Rips, and Rasinski give the four-stage model (comprehension, retrieval, judgment, response) that this skill uses to check each item. Krosnick and Presser is the standard treatment of closed-ended question design and the source for preferring construct-specific response options over agree/disagree formats, labeling every scale point, and keeping the task easy enough that respondents do not satisfice. J-PAL's guide adds that each question should be SMART, describes Likert, ranked, numeracy, and frequency scales, and warns about central tendency bias and sensitive questions. Harzing shows that response styles (acquiescence, extreme responding) differ across 26 countries, so a format that works in one place produces different data in another. Laajaj and Macours is the LMIC caution: in Kenya, standard noncognitive skill scales showed weak reliability and validity, with acquiescence among the problems (the exact wording of this finding is unverified, author to confirm). Judgment calls this skill adds: no reverse-keyed items at all for low-literacy or oral administration (the dossier lists the caution without a citation), a default of three to five labeled points when read aloud, and a rule that a sensitive behavior is routed to an indirect design rather than given a better-worded direct item. See `references/evidence-notes.md`.

**WEIRD skew:** The design rules come from US and European survey methodology, developed with literate respondents who often self-administer or answer by telephone. Harzing's cross-national study shows that response style itself varies by country, so the number of scale points, the use of a midpoint, and agree/disagree formats need local checking rather than import. **Non-WEIRD evidence:** Kenya (Laajaj and Macours 2021), where standard noncognitive scales showed weak reliability and validity and acquiescence bias, per the dossier, with the finding's exact wording unverified, author to confirm; Harzing's 26-country sample, whose countries the dossier does not list.

**Replication status:** Mixed. The item-design rules rest on a US and European methodological literature the dossier records as the main evidence base; the one LMIC study in the dossier shows standard scales failing in Kenya, which supports the cautions but has not itself been replicated in the sources here.

## How to do it

1. **Map each construct to its items and write the intended meaning beside each**, as "a correct reading is ...". One item carries one idea; if the sentence needs "and" or "or", split it. The intended meaning is what the pretest scores against.
2. **Pick the item type from the construct**: a bounded behavior count ("in the last 7 days, on how many days..."), a construct-specific rating ("how hard is it for you to..."), an expectation ("of ten farmers like you, how many..."), or a number. Prefer a concrete report over agreement with a statement.
3. **Write construct-specific response options instead of agree/disagree.** "How hard is it to put money aside each week? Not hard, a little hard, very hard" asks about difficulty; "I find it hard to save: agree or disagree" also asks whether the respondent likes agreeing.
4. **Label every point in words and keep the scale short.** Three to five labeled points when read aloud; no numbers without words; no midpoint unless the construct has a real middle. The enumerator reads the full option set every time.
5. **Remove double negatives and reverse-keyed items.** A reverse-worded item is meant to catch careless responding; with low-literacy or oral respondents it mostly creates confusion. Do not put "not" in a question whose answer is yes or no.
6. **Bound every recall window** to a recent period or a local event ("since the last market day"), never "usually" or "in general".
7. **Set the order and note context effects.** Group by topic, put evaluative items after factual ones, and record for each item which earlier item could shape its answer.
8. **Write the enumerator read-aloud version**: full sentences, options read every time, scripted transitions, and no instruction that depends on something the respondent can see.
9. **Run the design check table and cut to the length budget.** An item that fails a rule is rewritten or dropped, not annotated.
10. **Stop here; hand the items with their intended meanings to `draft-cognitive-interview-script`.** The pretest decides whether respondents read the items as intended; nothing in this output is evidence that they do.

See `references/worked-example.md` for a complete run on a Western Kenya fertilizer-timing survey block.

## Output template

```markdown
# Draft survey items: <survey or block name>

**Respondents:** <who, schooling, language>  **Mode:** <enumerator read-aloud / phone / self-completed>
**Length budget:** <n items or minutes>  **Position:** <what comes before and after this block>
**Constructs:** <list from the measurement plan>

## Items by construct
### <Construct 1>: <one-sentence definition>
**Item 1.1:** <question text as asked>
- Options: <every point, labeled in words>
- Type: <bounded count / construct-specific rating / expectation / number>
- Intended meaning: <what a correct reading of this item is>
- Design notes: <recall window; the format avoided and why; comparability constraint if any>

**Item 1.2:** ...

## Order and context
| Position | Item | Why here | Earlier item that could shape the answer |
|---|---|---|---|
| <1> | <1.1> | <...> | <none / item x, because ...> |

## Enumerator read-aloud version
<verbatim script: transitions, each item, options read every time>

## Design check
| Rule | Pass? | Items to fix |
|---|---|---|
| One idea per item | <yes/no> | <...> |
| No agree/disagree format | <yes/no> | <...> |
| Every scale point labeled; three to five points when read aloud | <yes/no> | <...> |
| No reverse-keyed or double-negative items | <yes/no> | <...> |
| Recall window bounded | <yes/no> | <...> |
| Sensitive behaviors routed to an indirect design | <yes/no> | <...> |

## Next step
Items and intended meanings go to draft-cognitive-interview-script; <n> interviews with <who>.

## What to check before relying on this
- <the construct most likely to be read differently by these respondents>
- <the response format most likely to produce a response style here>
```

## Where it goes wrong

- **Agree/disagree batteries creep back.** Given a list of constructs, the model's default is a Likert statement per construct. Every item is a question with construct-specific options; a statement to agree with is a rewrite trigger.
- **Numbers standing in for labels.** "On a scale of 1 to 10" is a task respondents who have not taken surveys before cannot do consistently; every point gets words, and the scale shrinks to what can be held in memory when read aloud.
- **Reverse-keyed items as a quality check.** A reversed item does not detect careless responding in a low-literacy sample; it manufactures it. The design check rejects any item whose scoring runs the other way.
- **Two ideas in one item.** "Do you have the time and money to buy fertilizer at harvest?" cannot be answered by someone with time and no money. Split, or drop one.
- **Rewording a sensitive item instead of routing it.** The skill must not produce a "better" direct question about a stigmatized behavior; it names the item, says why direct wording will not fix it, and points to `design-list-experiment`.
- **Treating the draft as a scale.** The output is draft items; the skill must not report or promise reliability, a factor structure, or a summed score, and must not describe the items as a validated measure.

## When to bring in a specialist

Tell the user to consult a survey methodologist, and for clinical constructs a clinician or psychometrician, when:
- Any construct is a sensitive or stigmatized behavior (sexual behavior, violence, substance use, illegal income); the indirect design in `design-list-experiment` is the first stop, and a methodologist should review whatever direct items remain
- Any construct is clinical (depression, anxiety, disability, cognitive impairment); program-written items are not a substitute for a screener, and a wrong item misclassifies people who then get or miss a referral
- Items must produce scores comparable across rounds, sites, or languages; wording changes made for comprehension can break the comparison, and a psychometrician can say which

Bring them: the construct definitions, the items with intended meanings, the respondent description, and the design check table.
