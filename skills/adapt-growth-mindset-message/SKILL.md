---
name: adapt-growth-mindset-message
description: >-
  Use when a team wants to tell students that ability grows with practice
  and asks for "a growth mindset lesson", "a mindset session for our
  schools", or "the Peru Expande tu Mente program for us", and needs it
  adapted to a local school. Also use when a mindset script is about to be
  copied from a US or World Bank program without deciding which students it
  is for, whether teachers and peers will back it, and how it will be
  measured. Produces a one-session lesson with local examples, the
  saying-is-believing writing task, a delivery and measurement plan, and a
  plain statement of the contested evidence (meta-analytic d = 0.08; Peru
  0.05 to 0.25 SD; Argentina null). Do not use when it is not yet known
  whether students read setbacks as a verdict on fixed ability; run
  identify-wise-intervention-target first. Not for belonging stories
  (draft-belonging-story), values affirmation (draft-values-affirmation),
  or generic drafting from a chosen technique (draft-lever-content).
license: CC-BY-4.0
metadata:
  title: Adapt a growth-mindset lesson to a local school
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: mixed-evidence
  tags: "growth-mindset, wise-interventions, behavior-change-techniques"
  consumes: "intervention-levers, barrier-diagnosis"
  produces: "intervention-draft"
---

## What it does

Adapts a brief "abilities can grow" lesson to one local school context, with a plain statement of which students it should be expected to help.

A growth-mindset lesson tells students that ability develops through practice, strategies, and help from others, so that a poor result reads as information rather than as a verdict. The student then explains the idea in their own words to a younger peer, the "saying-is-believing" task that makes the idea their own. The record is contested: the meta-analytic effect is d = 0.08, a 2023 review found 94% of interventions confounded, one trial at scale in Argentina was null, and the one positive trial in a low- or middle-income country (Peru) reports 0.05 to 0.25 SD depending on estimator. Effects have appeared among lower-achieving students, in one session, where teacher and peer norms let effort pay off, measured on grades. This skill writes the adapted lesson together with those conditions; it does not decide whether ability belief is the barrier.

## When to use it

### Use it when
- `identify-wise-intervention-target` named ability ("can I get better at this?") as the primary question and the affordance check passed or named what must change first
- Someone asks for "a growth mindset lesson", "a mindset session for our students", or "the Peru program adapted for our schools"
- A lever brief from `select-intervention-levers` selects a message about the growth of ability for a confirmed Motivation (reflective) barrier
- A team is about to translate a US or World Bank mindset script word for word, with its examples, into a school it has not checked

### Do not use it when
- It is not yet known whether students read setbacks as a verdict on fixed ability rather than as a belonging or trust problem; run `identify-wise-intervention-target`
- The question students ask is "do people like me belong here?"; that is `draft-belonging-story`
- The threat is to self-integrity, feeling judged in a stigmatized domain; that is `draft-values-affirmation`
- The barrier is teaching quality, absent teachers, no materials, or school fees; a lesson cannot substitute, so route to `select-intervention-levers`
- The team needs other copy (a reminder, a poster, a parent message) for a chosen technique; that is `draft-lever-content`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The target behavior (who, what, when) and the wise-intervention target from `identify-wise-intervention-target`, or at minimum field evidence, in students' words, that they read setbacks as proof of fixed ability. If the evidence points to resources or teaching quality, say so and stop.
2. **Required.** Who will receive the lesson: grade, age, achievement level, and whether the program can reach lower-achieving students specifically or only whole classes.
3. **Required.** The norms facts: what teachers do after a poor result (feedback, a retake, sorting students into the able and the rest), and what peers say about trying hard. The lesson depends on the setting letting effort pay off.
4. **Required.** Delivery: the format (a class period, a computer lab, paper, oral), the language and reading level, and who delivers it (teacher, program staff, self-administered).
5. Optional. Which outcome the program can measure (term grades, test scores, attendance) and whether a test with a comparison group is planned.
6. Optional. Local examples of skill growth (a craft, a sport, farming, a local figure who learned something late) and the school's own vocabulary for effort.

If 1 or 2 is missing, ask and stop. If 3 is missing, ask once; if still unknown, proceed with the norms check marked "unverified" and a teacher briefing written in as a requirement. If 4 is missing, assume one 60 to 90 minute classroom session on paper, delivered by a trained facilitator, and flag it. If 5 is missing, state that grades or scores must be the outcome. If 6 is missing, write placeholder examples marked for local replacement.

## What it draws on

- Yeager, D. S., et al. (2019). A national experiment reveals where a growth mindset improves achievement. *Nature*, 573, 364–369. https://doi.org/10.1038/s41586-019-1466-y
- Sisk, V. F., Burgoyne, A. P., Sun, J., Butler, J. L., & Macnamara, B. N. (2018). To what extent and under which circumstances are growth mind-sets important to academic achievement? Two meta-analyses. *Psychological Science*, 29(4), 549–571. https://doi.org/10.1177/0956797617739704
- Macnamara, B. N., & Burgoyne, A. P. (2023). Do growth mindset interventions impact students' academic achievement? A systematic review and meta-analysis with recommendations for best practices. *Psychological Bulletin*, 149(3–4), 133–173. https://doi.org/10.1037/bul0000352
- Burnette, J. L., et al. (2023). A systematic review and meta-analysis of growth mindset interventions: For whom, how, and why might such interventions work? *Psychological Bulletin*, 149(3–4), 174–205. https://doi.org/10.1037/bul0000368
- Outes-León, I., Sánchez, A., & Vakis, R. (2020). The power of believing you can get smarter: The impact of a growth-mindset intervention on academic achievement in Peru. World Bank Policy Research Working Paper 9141. https://doi.org/10.1596/1813-9450-9141
- Ganimian, A. J. (2020). Growth-mindset interventions at scale: Experimental evidence from Argentina. *Educational Evaluation and Policy Analysis*, 42(3), 417–438. https://doi.org/10.3102/0162373720938041
- Bettinger, E., Ludvigsen, S., Rege, M., Solli, I. F., & Yeager, D. (2018). Increasing perseverance in math: Evidence from a field experiment in Norway. *Journal of Economic Behavior & Organization*, 146, 1–15. https://doi.org/10.1016/j.jebo.2017.11.032
- Walton, G. M., & Wilson, T. D. (2018). Wise interventions: Psychological remedies for social and personal problems. *Psychological Review*, 125(5), 617–655. https://doi.org/10.1037/rev0000115
- Bryan, C. J., Tipton, E., & Yeager, D. S. (2021). Behavioural science is unlikely to change the world without a heterogeneity revolution. *Nature Human Behaviour*, 5(8), 980–989. https://doi.org/10.1038/s41562-021-01143-3
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709
- Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity: A meta-analysis and a real-effort experiment. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x

Walton and Wilson describe a wise intervention as a brief, precise change to the meaning a person makes of a situation, delivered so that it becomes the person's own view. A growth-mindset lesson applies this to one meaning: that a poor result shows fixed low ability. The US national study (Yeager et al.) found gains among lower achievers, about +0.10 GPA (a secondary-source figure per the dossier), and only where peer norms supported taking on challenges, which is why this skill makes the norms check a condition rather than a note. Peru's ¡Expande tu Mente! delivered a 90-minute session to more than 50,000 public-school students at about $0.20 per pupil; it was later scaled to Indonesia as Semua Bisa Pintar! (about 160,000 students) and adapted in South Africa, with no results for either in the sources this skill draws on. The judgment calls this skill adds: the fixed-ability check as the entry condition, lower achievers as the pre-specified group, the norms check as a gate, one session, grades or scores as the outcome, pre-registration (filing the outcome and analysis before delivery) as mandatory because the effects are small, and an evidence statement inside the output so the decision-maker sees the record.

How much to discount: the meta-analytic average is d = 0.08 (k = 43 studies, N = 57,155 students), with about 0.19 for high-risk and 0.34 for low-SES students on limited evidence (Sisk et al.); 94% of interventions in the 2023 review were confounded, and authors with financial incentives reported larger effects (Macnamara & Burgoyne); the companion review found positive effects for those expected to benefit, with large variation (Burnette et al.). Across applied behavioral science, academic journal trials average 8.7 percentage points where nudge-unit trials average 1.4 (DellaVigna & Linos), and loss framing shrinks from 0.33 SD in the lab to 0.02 in the field (Ferraro & Tracy). Plan for a few hundredths of a standard deviation on grades among lower achievers, treat a null as a live outcome, and expect the effect to vary across schools (Bryan, Tipton & Yeager).

**WEIRD skew:** The meta-analyses and the national study are US school samples; Norway (Bettinger et al.) improved perseverance in a WEIRD but non-US setting. Check locally whether "ability grows" is credible where examinations are one-shot and streaming is early, whether teachers will back the message, whether the examples of skill growth are recognizable, and whether a written task suits the reading level. **Non-WEIRD evidence:** Peru (Outes-León, Sánchez & Vakis 2020): more than 50,000 students, math gains reported as 0.14 SD by the World Bank, 0.05 to 0.25 depending on estimator, larger outside Lima, and about 0.2 SD in the World Bank summary; the figures conflict, so this skill quotes the range. Argentina (Ganimian 2020; Salta, 202 schools): null, with small effects ruled out. Indonesia and South Africa: adaptations exist with no results cited.

**Replication status:** Contested. The pooled effect is d = 0.08; the two 2023 reviews disagree on whether the positive subgroup effects survive design corrections; one LMIC trial is modestly positive with conflicting estimates and one is null. See `references/evidence-notes.md` for each source with its verification state.

## How to do it

1. **Confirm the barrier is a fixed-ability belief.** Carry the target behavior and the students' own words over verbatim. If the quotes point to resources, teaching quality, fees, or language of instruction, stop and route to `select-intervention-levers`; otherwise write under "What this lesson does not fix" whatever structural barrier sits beside the belief.
2. **Choose who receives it.** Lower-achieving students are where effects have appeared. If delivery must be whole-class, pre-specify lower achievers (by a named cutoff on the prior term's result) as the primary analysis group, and promise nothing for the rest.
3. **Run the norms check.** Write what teachers do after a poor result and what peers say about trying hard, from the facts given. Verdict: afforded, not afforded, or unverified. If not afforded, name what must change first (a teacher briefing, a retake, feedback in sessions) and write it in as a requirement; a lesson that promises "you can improve" in a setting with no occasion to improve is false, and students find out.
4. **Localize the content without removing the mechanism.** Keep three claims: ability grows with practice; struggle is normal and is information, not a verdict; strategies and help from others are part of effort. Replace the examples (a US athlete, a US classroom) with local ones of skill learned over time. Do not reduce the lesson to "try harder"; effort without strategies or help puts the whole burden on the student.
5. **Write the saying-is-believing task.** The student writes a letter of advice to a younger student who is struggling in the subject, in their own words, using the ideas from the lesson. Where reading is weak, an oral or drawn version with a facilitator counts. Say that letters will be shared with next year's students, and then share them.
6. **Fix delivery.** One session of 60 to 90 minutes (Peru used 90), timed just before the moment the belief becomes live (results returned, a hard unit starting); who delivers and how they are trained; no repeat sessions, since one session is the tested design. See `references/worked-example.md` for a complete run.
7. **Write the measurement plan.** Primary outcome: grades or test scores at a named point; primary subgroup: lower achievers; a comparison group; a pre-registered plan filed before delivery. Beliefs may be measured as a check on delivery, never as the outcome. State the expected effect as a few hundredths of a standard deviation.
8. **Write the evidence statement** for the decision-maker, with the numbers from "What it draws on": contested, small, conditional, one null at scale.
9. **Specify the pre-test:** 5 to 10 students from the target group restate the core idea and the writing task in their own words; 2 to 3 teachers read it and say whether they would back it in class. Pass: all students name "ability grows with practice" and no teacher names a contradiction.
10. **Stop here.** The evaluation design and sample size belong to `plan-evaluation-design` and `estimate-sample-size`; the final-language copy is drafted natively by a local speaker, not translated from this draft.

## Output template

```markdown
# Growth-mindset lesson, adapted

**Target behavior:** <who, what, when, carried over verbatim>
**Barrier evidence carried over:** <the fixed-ability reading, in students' words, with counts>
**Who receives it:** <lower-achieving students, defined by cutoff | whole class, with lower achievers pre-specified>
**What this lesson does not fix:** <the resource, teaching, or structural barrier, routed to select-intervention-levers>

## Norms check
- **Teachers:** <what they do after a poor result; source of the fact>
- **Peers:** <what they say about trying hard; source>
- **Verdict:** <afforded | not afforded: what must change first | unverified: teacher briefing required>

## Core lesson (working copy; final copy drafted natively)
1. <ability grows with practice: the claim, with a local example>
2. <struggle is information, not a verdict: the claim, with a local example>
3. <strategies and help are part of effort: named strategies, named sources of help>

## Saying-is-believing task
<the writing prompt: advice to a younger struggling student; the oral variant if needed; where the letters go>

## Delivery
- **Format and length:** <...>
- **Timing:** <just before which moment>
- **Delivered by:** <who, with what training>
- **Frequency:** once

## Measurement plan
- **Primary outcome:** <grades or scores, when>
- **Primary subgroup:** <lower achievers, how defined>
- **Comparison:** <...>
- **Pre-registration:** <what is filed before delivery>
- **Expected effect:** <a few hundredths of a standard deviation; a null is a live outcome>

## Evidence statement (mandatory)
<the contested record in four sentences, with the numbers as given in What it draws on>

## Required pre-test before launch
<n students, n teachers, pass criterion>

## What to check before relying on this
- <the norms fact most likely to be a hope>
- <the structural barrier the lesson sits beside>
```

## Where it goes wrong

- **A lesson instead of a teacher.** The most serious misuse: a 90-minute session offered where the real barrier is absent teachers, no materials, or fees. The "What this lesson does not fix" line is mandatory so the substitution is visible.
- **Whole-school delivery with an average effect promised.** Effects have appeared among lower achievers in supportive settings; averaged across everyone they are near zero. Pre-specify the subgroup or expect a null.
- **Translating the script, not the lesson.** A word-for-word translation of a US script keeps the US examples and the US classroom assumptions. Localize the examples, keep the three claims.
- **"Try harder."** A message about effort with no strategies or help makes the student responsible for a failure the setting produced; it is not the technique the evidence tested.
- **Measuring beliefs.** A rise in agreement with "ability can grow" is not the outcome. Grades or scores are; a belief measure is a check that the lesson was delivered, nothing more.
- **Quoting the big number.** 0.34 for low-SES students, 0.2 SD in Peru: the largest figures in the record, on limited evidence or one estimator. The output quotes the range and the null.

## When to bring in a specialist

Tell the user to consult an education economist or evaluator, and a psychologist with school-intervention experience, when:
- The program would replace, rather than add to, instructional improvements (teacher recruitment, materials, remedial teaching); the record cannot carry that decision, and the evidence statement must reach whoever is making it
- The lesson is pitched as a fix for structural disadvantage (poverty, discrimination, language of instruction, early streaming); a lesson that tells disadvantaged students the problem is their mindset can do harm, and `audit-intervention-ethics` should review it
- The rollout is regional or national with no pre-registered test; an evaluator should design a test before scaling, since the at-scale record includes a null
- Students in the target group face high-stakes examination failure with known distress or dropout consequences; a school counselor should review the session and what follows a poor result

Bring them: the target and the students' words, the norms check with its facts, the lesson draft, the measurement plan, and the evidence statement.
