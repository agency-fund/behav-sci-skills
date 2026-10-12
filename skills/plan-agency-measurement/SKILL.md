---
name: plan-agency-measurement
description: >-
  Use when agency has been defined for a digital or AI tool's users,
  usually by define-agency-construct, and the team must decide how to
  measure it: "what do we ask in-app versus in our phone survey?", "here
  is our agency definition; build the measurement plan", "which published
  scales and items could we use?", "can an LLM score agency in our chat
  logs?". Also use when a team proposes a specific agency measure (an
  in-chat check, a scale, a log signal) and asks whether it will hold up.
  Produces a plan on the 2x2 agency framework: on- and off-platform
  measures per focus cell, candidate instruments with items (found by
  literature search, or drafted examples labeled as such), their source
  and evidence base, and next steps for research, adaptation, testing, and
  interpretation. Do not use when nobody has said what agency means here;
  run define-agency-construct first. Not for drafting a full questionnaire
  (draft-survey-items) or auditing LLM-coded transcripts
  (audit-llm-qualitative-coding).
license: CC-BY-4.0
metadata:
  title: Plan how to measure agency in a digital tool
  type: atomic
  stage: measure
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: mixed-evidence
  tags: "agency, measurement, psychometrics, survey-design, ai-eval, llm-assisted-analysis"
  consumes: "agency-definition, ai-product-account"
  produces: "measurement-plan"
---

## What it does

Plans how to measure a defined agency construct for a digital or AI tool's users.

It takes a definition placed on the 2x2 agency framework (usually from `define-agency-construct`), maps the data the team already has onto the framework, and fills each cell the team chose to focus on with an on-platform and an off-platform measure tied to a moment in the user journey. For each measure it names candidate instruments with items, either found in the literature or drafted as labeled examples, with their source and the evidence behind them. It ends with concrete next steps: what to research, whether to use, adapt, or build each measure, how to test it, and how to read what the tests show. Drafting the full questionnaire, translating it, and auditing LLM coding go to other skills.

## When to use it

### Use it when
- A team has an agency definition (from `define-agency-construct` or its own) and asks "what do we measure, in the app and off it?"
- A team asks "which published scales could we use for this, and what are the items?"
- A team plans to score agency in conversation logs with a language model and wants to know what that score can show and what else to measure beside it
- A team proposes a specific measure (a one-item in-chat check, a scale from another study, a log signal such as "messages without asking the bot") and asks whether it will hold up for a funder claim or a comparison
- A team plans to translate an agency scale built elsewhere and use it with its own users

### Do not use it when
- Nobody has said what agency means for these users; run `define-agency-construct` first
- The team wants the full questionnaire written, with read-aloud and enumerator versions; use `draft-survey-items`, which takes this plan as input
- An LLM has already coded transcripts and the question is whether the codes can be trusted; use `audit-llm-qualitative-coding`
- The team needs the A/B comparison between two versions set up; use `design-evidential-experiment`
- The team needs a primary outcome, comparison condition, and smallest effect for an impact evaluation; use `plan-evaluation-design`, with this plan supplying the agency measures

## Before you start

Ask one question at a time and offer a suggested answer with each, inferred from what the user has already said. Do not ask anything the user's message or documents already answer.

1. **Required.** The agency definition: `define-agency-construct`'s document, or the team's own constructs placed on the 2x2 agency framework. If the team arrives with a measure instead ("GPT will score agency in our logs"), ask which construct the measure is meant to capture.
2. **Required.** The decision or claim the plan will support: iterate the product, compare versions, a funder or board report, or a published claim. This sets how much testing is enough.
3. The data the team collects now, on the platform (logs, in-app questions, interaction patterns) and off it (surveys, observation, records), including any measure already in use or proposed, and what more is feasible on what budget and timeline.
4. Optional. Items: does the team want original items from the literature, found by search, or example items drafted from the construct, not taken from any published instrument?
5. Optional. What users consented to for logs, transcripts, or voice notes.
6. Optional. Whether scores will be compared across groups, languages, sites, or arms.

If the team brings a measure but no construct, ask which construct it is meant to capture; if they cannot name one, or 1 is missing altogether, send them to `define-agency-construct` and stop. If 2 is missing, ask: a product iteration and a funder claim lead to different plans. If 3 is missing, assume on-platform data plus one small off-platform round and mark the assumption. If 4 is missing, give drafted examples, labeled, plus search queries for the originals. If 5 is missing, assume no consent for secondary analysis of conversations, so any LLM coding stays a proposal pending consent and ethics review. If 6 is missing, assume no comparison and note that a later one needs an invariance test first.

## What it draws on

- Wu, Z., Goldberg, B., & Xu, R. (2026, July 1). *Measuring agency in a digital context*. The Agency Fund (Substack), with Google Jigsaw. https://theagencyfund.substack.com/p/measuring-agency-in-a-digital-context
- The Agency Fund. (2026). *ask-agency-measurement* (the Claude skill this one and `define-agency-construct` replace). https://github.com/agency-fund/taf-skills/tree/main/ask-agency-measurement
- Glennerster, R., Walsh, C., & Diaz-Martin, L. (2018). *A practical guide to measuring women's and girls' empowerment in impact evaluations*. J-PAL. https://www.povertyactionlab.org/page/practical-guide-measuring-womens-and-girls-empowerment-impact-evaluations
- Boateng, G. O., Neilands, T. B., Frongillo, E. A., Melgar-Quiñonez, H. R., & Young, S. L. (2018). Best practices for developing and validating scales for health, social, and behavioral research: A primer. *Frontiers in Public Health, 6*, 149. https://doi.org/10.3389/fpubh.2018.00149
- Laajaj, R., & Macours, K. (2021). Measuring skills in developing countries. *Journal of Human Resources, 56*(4), 1254–1295. https://doi.org/10.3368/jhr.56.4.1018-9805R1
- Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning. *PNAS, 122*(26), e2422633122. https://doi.org/10.1073/pnas.2422633122
- Sen, I., Flöck, F., Weller, K., Weiß, B., & Wagner, C. (2021). A total error framework for digital traces of human behavior on online platforms. *Public Opinion Quarterly, 85*(S1), 399–422. https://doi.org/10.1093/poq/nfab018
- Halterman, A., & Keith, K. A. (2026). Codebook LLMs: Evaluating LLMs as measurement tools for political science concepts. *Political Analysis, 34*(2), 188–204. https://doi.org/10.1017/pan.2025.10017
- Ashwin, J., Chhabra, A., & Rao, V. (2026). Using large language models for qualitative analysis can introduce serious bias. *Sociological Methods & Research, 55*(3), 795–839. https://doi.org/10.1177/00491241251338246
- CGD Technical Working Group, with The Agency Fund, IDinsight, and the Center for Global Development. (2026). *AI evaluation playbook*. https://eval.playbook.org.ai/

The blog supplies on- and off-platform data and the define, measure, validate sequence; the earlier skill supplies the coaching style and the measurement questions. The J-PAL guide and Boateng et al. anchor instrument choice, adaptation, and testing. Laajaj & Macours show, in Kenya, how self-reports of noncognitive skills carry systematic error in low-income settings, which is why an instrument from another context needs local testing before use. Bastani et al. show assisted performance rising while unassisted performance fell, which is why expressed measures include unassisted outcomes. Sen et al. give the error framework for log signals; Halterman & Keith, Ashwin et al., and the AI Evaluation Playbook anchor the cautions on LLM-based measures. Candidate instruments and the evidence on each are in `references/measurement-options.md`; testing and interpretation in `references/validation.md`; full citations and verification status in `references/evidence-notes.md`.

**WEIRD skew:** Most published agency, self-efficacy, trust, and AI-dependence scales were built with students or office workers in high-income countries. The women's agency measures (Donald et al., pro-WEAI, Jayachandran et al.) and the measurement-error evidence (Laajaj & Macours) come from low- and middle-income settings. No verified study validates an agency or dependence measure delivered in-chat on WhatsApp or a similar channel in a low-income setting; every instrument needs local cognitive testing, and in-app items need a benchmark against an off-platform measure.

**Replication status:** Mixed. Scale-development and invariance methods are well established and the women's agency indices have multi-country validation, but measuring agency with respect to AI tools rests on single studies and preprints, and how far LLM coding can stand in for human coders is contested.

## How to do it

1. **Check the definition before measuring anything.** Check that each construct is named precisely ("perceived control over the next planting decision", not "agency") and placed on the 2x2 agency framework: its form (agency with respect to the end goal or with respect to the digital tool) and its manifestation (internally experienced as thoughts and feelings, or externally expressed as choices and actions). If the team has not placed a construct, place it yourself and state the placement. If a construct lacks a theory and the choice of instrument depends on one, name the theory. If what the team proposes is unsafe (a sensitive question asked in a shared-phone chat) or cannot support the claim it wants in its timeline (a cross-country comparison next quarter), say so before the plan, then give the plan with the changes and what the team could report instead.
2. **Map the data the team already has onto the framework.** Place each existing source in its cell, on- or off-platform, and mark it "(have)". Usage, retention, and ratings go in no cell; they measure engagement or satisfaction. This shows which focus cells have no data yet.
3. **Choose an on-platform and an off-platform measure for each focus cell, tied to a moment.** Look beyond surveys: conversation logs, interaction patterns, task behavior, unassisted performance, observation, rubric-rated work, interviews, and records can each show what a survey misses. Keep in-app checks to one to three short items, asked at the moment the construct is live (after a decision or setback, not when the app opens), about specific recent situations. Mark any measure that has a language model code conversations as experimental. See `references/measurement-options.md`.
4. **Fill the measure details.** For each measure: the instrument (name, length, response format), items, source (the theory and the paper), evidence base (validated with whom, where, and how; what to check before using it here), form, and manifestation. Items follow the team's choice:
   - **From the literature:** if you have search tools, search, open the source, and quote only what you opened. If the source is paywalled or cannot be found, write "not accessed: paywalled" or "not found" and cite it. Without search tools, write "not accessed: no search tools here" and give paste-ready queries (`references/research-queries.md`).
   - **Drafted examples:** write items from your understanding of the construct and label them "drafted example, not from the literature". The source column names only the theory.
   - Never attribute a drafted item to a published scale, and never reproduce a published scale from memory.
5. **Write the next steps, concretely for this plan.**
   1. **Research further:** the open measurement questions (an instrument validated with these users, how a log signal relates to off-platform behavior), with paste-ready queries.
   2. **Use, adapt, or build:** for each measure, whether to use it as published, adapt it (translate, shorten for chat, add local examples, rework items that may not transfer), or build a new one, and how. Hand item drafting to `draft-survey-items`, translation to `translate-survey-instrument`, phone delivery to `adapt-survey-for-phone-mode`, and sensitive questions to `design-list-experiment`.
   3. **Test and gather evidence:** the cheapest credible checks for the claim the team will make: cognitive interviews (`draft-cognitive-interview-script`), reliability, a check against an outcome the team trusts, an invariance test before any comparison, and a human-coded gold standard before any LLM codes are used (`audit-llm-qualitative-coding`). Name any specialist needed. See `references/validation.md`.
   4. **Interpret the evidence:** what results from those checks would mean keeping, revising, or dropping each measure, and when they would mean the construct itself needs rethinking (back to `define-agency-construct`).
   5. **Down the road:** skills for later decisions, such as `choose-ai-eval-level`, `design-evidential-experiment`, or `plan-evaluation-design`.

See `references/worked-example.md` for a complete run on a hypothetical AI mentor for student entrepreneurs.

## Output template

```markdown
# Agency measurement plan: <tool>

**Definition:** <working definition and focus cells, from define-agency-construct>
**Decision this plan supports:** <iterate / compare versions / funder report / published claim>
**Assumed:** <anything assumed because the team could not say; omit if none>

## Measures on the 2x2 agency framework
| | Agency with respect to the end goal: <goal> | Agency with respect to the digital tool: <tool> |
|---|---|---|
| **Thoughts and feelings** (internally experienced) | **On-platform:** <measure, moment> (#1)<br>**Off-platform:** <measure, moment> (#2) | <... or "not in focus"> |
| **Choices and actions** (externally expressed) | <...> | <...> |

Data the team already collects is marked "(have)".

## Measure details
| # | Instrument | Items | Source | Evidence base | Form | Manifestation |
|---|---|---|---|---|---|---|
| 1 | <name, length, response format> | <items quoted from the source; "not accessed: paywalled / not found / no search tools here"; or "drafted example, not from the literature: ..."> | <theory; authors, year, link> | <validated with whom, where, how; what to check before using it here> | <end goal / digital tool> | <thoughts and feelings / choices and actions> |

## Next steps
1. **Research further:** <open measurement questions>: "<paste-ready query>"
2. **Use, adapt, or build:** <per measure: use as published, adapt, or build new, and how>, with <skills>
3. **Test and gather evidence:** <the cheapest credible checks for this claim; specialist to bring in, if any>, with <skills>
4. **Interpret the evidence:** <what results would mean keep, revise, or drop each measure, or rethink the construct>
5. **Down the road:** <skills for later decisions>
```

## Where it goes wrong

- **Going straight to measurement without a precise construct.** The model picks scales for "agency" before anyone has said what agency means for these users. Check the definition first; send the team to `define-agency-construct` if there is none.
- **Ignoring the forms and manifestations of agency.** Every measure ends up as a self-report about the end goal, so nothing captures what users do, or how they relate to the tool. Place each measure on the 2x2 agency framework.
- **Not thinking about theory when it is needed.** A scale is chosen because it has "agency" in its name, not because it captures the construct the team defined; the theory behind the construct should drive the instrument.
- **Relying only on surveys.** Logs, interaction patterns, task behavior, unassisted performance, observation, rubric-rated work, and records are often already available and show what self-reports miss.
- **Using Western-developed surveys blindly.** A scale built with US college students is translated and fielded as is, with no plan to check what the construct means locally, rework items, or collect measurement evidence that could inform redesigning the items or rethinking the construct.
- Out of scope: defining agency (`define-agency-construct`), writing the full questionnaire (`draft-survey-items`), and designing the experiment that compares versions (`design-evidential-experiment`).

## When to bring in a specialist

Tell the user to bring in a specialist when:
- The plan needs psychometric or survey-design support: choosing and adapting instruments, building new scales, testing reliability, structure, or invariance, or backing a funder-facing or published claim; bring in a psychometrician or survey methodologist.
- The plan relies on more comprehensive LLM-based analysis or labeling of naturalistic data (conversation logs, voice notes, open-ended answers); bring in a researcher experienced in validating LLM-based measurement against human coding.
- Measures ask about decision-making power at home with women, girls, or minors; asking can put people at risk, so bring in an ethics review board and a researcher experienced in women's safety research before fielding anything.
- Conversation logs or voice notes will be analyzed, especially from minors or about health; bring in a data protection lead and the ethics review board on consent, de-identification, and retention.

Bring them: the definition document, this plan, the population description, and what users consented to.
