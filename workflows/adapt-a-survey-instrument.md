---
name: adapt-a-survey-instrument
title: Bring a survey instrument into a new language and mode
description: >-
  For a team that has a questionnaire in one language and setting and needs
  it to work in another: translate it with a documented team process, write
  any missing items for low-literacy or oral administration, pretest with
  cognitive interviews, and convert it for phone delivery if fieldwork
  cannot be face to face. Ends with a pretested instrument and a decision
  log. Does not choose an existing validated measure or validate a scale;
  those are separate skills.
license: CC-BY-4.0
metadata:
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  stages: "measure"
  skills: "translate-survey-instrument, draft-survey-items, draft-cognitive-interview-script, adapt-survey-for-phone-mode, design-list-experiment"
  tags: "survey-design, measurement, qualitative"
---

## What it is for

Instruments travel badly. A translation done by one colleague on the fly, an agree/disagree battery read aloud to respondents who have never taken a survey, a 60-minute face-to-face questionnaire moved to a phone call: each produces numbers that look like data. This workflow makes every change explicit and tested.

## When to use it

- When a baseline or endline instrument exists in another language or was built for self-administration
- When fieldwork is moving to phone or interactive voice response
- Not when the construct has no instrument yet and the team needs to find or build one; those are separate skills
- Not when the question is whether a sensitive behavior can be asked directly; `design-list-experiment` alone

## Skills in this workflow

| Step | Skill | Version | Relationship | What carries forward | Human decision point |
|---|---|---|---|---|---|
| 1 | `translate-survey-instrument` | 0.1.0 | start | target-language items with a decision log | Decide on back-translation and record why; confirm the construct exists locally |
| 2 | `draft-survey-items` | 0.1.0 | after 1, optional | new or rewritten items for constructs the source instrument handles badly orally | Approve the response formats for oral delivery |
| 3 | `draft-cognitive-interview-script` | 0.1.0 | after 1 and 2 | cognitive interview script | Pick respondents who match the field population; decide what to change after the interviews |
| 4 | `adapt-survey-for-phone-mode` | 0.1.0 | after 3, optional | phone-ready instrument and mode-effect plan | Decide on the call length and the privacy gate for sensitive items |
| 5 | `draft-cognitive-interview-script` | 0.1.0 | after 4, optional | pretest of the phone version | Approve the final instrument |

Relationship values: `start`, `after N`, `parallel with N`, `independent`, `optional`.

## How to run it

1. Run `translate-survey-instrument` with the source items and their intended meanings. The committee must include someone from the respondent population. Keep the decision log; a later reader will otherwise "correct" the deliberate adaptations.
2. If the source instrument relies on agree/disagree statements, unlabeled numeric scales, or reverse-keyed items, run `draft-survey-items` for those constructs so the oral version works.
3. Run `draft-cognitive-interview-script` and field it with respondents like the field population. Change items on what the interviews show, and log the changes.
4. If fieldwork is by phone, run `adapt-survey-for-phone-mode`; it cuts length, converts scales, and plans the mode-effect check.
5. Pretest the phone version with a short second cognitive-interview round before launch.

## Worked example

A savings program in Butuan, Philippines, has an English self-efficacy and savings-behavior questionnaire built for literate respondents and needs it in Cebuano for enumerator-read interviews, with the endline by phone. Step 1 produces two forward translations, a committee reconciliation with a program client on the panel, a decision not to back-translate, and a log noting that one idiom was kept non-literal on purpose. Step 2 rewrites the four agree/disagree self-efficacy items as questions with construct-specific options. Step 3's cognitive interviews with twelve clients show that "set aside" was heard as "hide from the household"; the item is rewritten. Step 4 cuts the endline to eighteen minutes, converts the five-point scales to unfolding questions, and adds a privacy gate before the income items because phones are shared. Step 5 pretests the phone version with six clients.

## Where it goes wrong

- Skipping step 3 because the translation "reads well"; cognitive interviews are where the meaning gap shows.
- Calling the output validated or equivalent; it is translated and pretested, and comparability with the source is a separate question for a psychometrician.
- Moving a clinical screener with published cut-offs through this workflow and keeping the cut-offs; local validation is a different skill's job.
- Treating a change between a face-to-face baseline and a phone endline as a program effect before the mode-effect check.

## When to bring in a specialist

- Clinical screeners (PHQ-9 and similar) or any instrument whose scoring depends on exact wording: a psychometrician and, for screeners, a clinician, before step 1 ends.
- A construct that may not exist in the target culture: a cultural psychologist or local researcher decides whether translation is even the right task.
- Sensitive items on shared phones at step 4: a safeguarding lead sets the privacy gate.
