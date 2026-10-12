---
name: draft-implementation-intention-prompt
description: >-
  Use when people say they will do a one-off action (get a vaccine, attend a
  scheduled visit, report a self-test result, register, collect a document)
  and the share who follow through is low. Also use when a team wants to add
  a "when and where will you do it?" question to a message, home visit, or
  form that already reaches people. Writes an if-then plan prompt that asks
  the person to name the date, time, and place they will act, drawing on the
  Gollwitzer and Sheeran (2006) meta-analysis and the Milkman et al. (2011)
  flu-shot trial, and states the small effect to expect. Do not use when the
  behavior is repeated or daily (taking a pill, saving every week,
  exercising); the field trial of plan prompts for repeated behavior found a
  null, so use design-habit-anchor instead. Not for reminders the program
  sends on a schedule (design-reminder-schedule), and not for the final
  message wording with sender and fidelity trace (draft-lever-content).
license: CC-BY-4.0
metadata:
  title: Ask people to plan when and where
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: untested-outside-weird
  tags: "implementation-intentions, behavior-change-techniques, planning-prompts"
  consumes: "intervention-levers"
  produces: "intervention-draft"
---

## What it does

Writes a prompt that asks a person to name the moment they will carry out one action they already intend to do.

The prompt asks for a date, a time, and a place, which turns a vague intention ("I'll get the vaccine") into an if-then plan, called an implementation intention ("if it is Tuesday at 10 and I am passing the clinic, then I go in"), so that the situation, not willpower, triggers the action. It works on the gap between intending and acting. It does not create the intention, and it has a documented null result for repeated behavior.

## When to use it

### Use it when
- People say they will do a one-off action (get a vaccine, attend a scheduled visit, report a self-test result, register, collect a document) and the share who follow through is low
- A team wants to add a "when and where will you do it?" question to a contact that already happens: a message, a home visit, a form, a counseling session
- An appointment or deadline is fixed and the team wants to raise attendance without adding incentives or a new channel
- The lever brief from `select-intervention-levers` names action planning as the technique

### Do not use it when
- The behavior is repeated or daily (taking a pill every day, saving every week, exercising); the one field trial of plan prompts for a repeated behavior found a tight null. Use `design-habit-anchor`
- The program wants to send the person reminders on a schedule; a reminder is sent by the program, a plan is made by the person. Use `design-reminder-schedule`
- People do not yet intend to act (they do not want the thing, do not trust it, or cannot reach it); a plan prompt cannot create motivation. Go back to `select-intervention-levers`
- The team needs the final wording in the local language, with sender and timing notes and a fidelity trace; `draft-lever-content` takes this skill's prompt as its input

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The target behavior (who, what, when) and the lever brief or confirmed barrier. The barrier must be that people intend to act and do not get round to it. State the evidence that intention exists (a survey, interviews, prior take-up of the same action by the same people). If there is none, say so and stop.
2. **Required.** Whether the action is one-off or a fixed appointment, or repeated. If repeated, stop and route to `design-habit-anchor`.
3. **Required.** The action window and the real options: the dates on which the action can be done, the places, the opening hours, what the person must bring. A prompt that asks for a plan the person cannot keep is worse than no prompt.
4. **Required.** The existing contact the prompt will ride on (which message, visit, or form, and who delivers it), because a new channel is a different intervention.
5. Optional. Whether people in this population already plan together (a household that acts as one, a routine clinic day); the voting trial found half the effect where people planned organically.

If 1, 2, or 3 is missing, ask and stop. If 4 is missing, ask once; if still unknown, draft for a text message and flag the channel UNCONFIRMED. If 5 is missing, assume no organic planning and say so in the expected-effect line.

## What it draws on

- Gollwitzer, P. M., & Sheeran, P. (2006). Implementation intentions and goal achievement: A meta-analysis of effects and processes. *Advances in Experimental Social Psychology*, 38, 69–119. https://doi.org/10.1016/S0065-2601(06)38002-1
- Milkman, K. L., Beshears, J., Choi, J. J., Laibson, D., & Madrian, B. C. (2011). Using implementation intentions prompts to enhance influenza vaccination rates. *Proceedings of the National Academy of Sciences*, 108(26), 10415–10420. https://doi.org/10.1073/pnas.1103170108
- Nickerson, D. W., & Rogers, T. (2010). Do you have a voting plan? Implementation intentions, voter turnout, and organic plan making. *Psychological Science*, 21(2), 194–199. https://doi.org/10.1177/0956797609359326
- Carrera, M., et al. (2018). The limits of simple implementation intentions: Evidence from a field experiment on making plans to exercise. *Journal of Health Economics*. https://doi.org/10.1016/j.jhealeco.2018.09.002
- Buttenheim et al. (2022). Planning and commitment prompts to encourage reporting of HIV self-test results: A cluster randomized pragmatic trial in Tshwane District, South Africa. *PLOS Global Public Health*. https://doi.org/10.1371/journal.pgph.0001196
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709
- Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity: A meta-analysis and a real-effort experiment. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x
- Behavioural Insights Team (2014; revised and updated edition, c. 2024). *EAST: Four simple ways to apply behavioural insights*, "Make it timely". London: BIT. https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf

An implementation intention is a plan of the form "if situation X arises, then I do Y". Gollwitzer and Sheeran (2006) pooled 94 independent tests and found d = 0.65 on goal attainment; the mechanism they describe is that the plan hands control of the action to the situational cue, so the person does not have to remember, decide, or summon effort at the moment. Milkman et al. (2011) tested it on flu shots: a prompt that asked for a date and a time added 4.2 percentage points over a 33.1% baseline; a prompt that asked only for a date added 1.5 points, not significant. Specificity is the active ingredient. Nickerson and Rogers (2010) prompted voters to make a voting plan (N = 287,228): turnout rose 4.1 points overall and 9.1 points in single-voter households, where no one else was around to plan with. Carrera et al. (2018) ran plan prompts for gym attendance, a repeated behavior, and found a tight null. The field effects of about 4 points sit far below the meta-analytic d, which fits the general pattern: academic trials average 8.7 percentage points where nudge-unit trials of similar designs average 1.4 (DellaVigna & Linos, 2022), and loss framing shrinks from 0.33 SD in the lab to 0.02 SD in the field (Ferraro & Tracy, 2022). Plan on a few points, not on d = 0.65. The judgment calls this skill adds are the mandatory intention check, the one-off rule, and the requirement that the prompt ask for all three of date, time, and place.

**WEIRD skew:** The meta-analysis, the flu-shot trial, and the voting trial come from WEIRD samples, and the dossier records no non-WEIRD test with a confirmed result. Check locally whether the person can write or say the plan, whether the date and place are theirs to choose (permission, transport, who holds the phone), and whether households plan together, which halves the effect. **Non-WEIRD evidence:** South Africa (Buttenheim et al., 2022): a cluster randomized pragmatic trial of planning and commitment prompts for reporting HIV self-test results in Tshwane District exists, but its result was not retrieved for the dossier, so no number is quoted here (unverified, author to confirm). A savings study summarized by Cenfri, reporting that numeric goals did worse than general commitments, is unverified, author to confirm, and its country is unconfirmed. No LMIC field trial with a confirmed effect was found in the sources this skill draws on.

**Replication status:** replicated for one-off actions (94 tests pooled; two large field trials with effects of about 4 points); a tight null for repeated behavior; mixed overall, and the meta-analytic effect is probably inflated relative to field trials.

## How to do it

1. **Confirm the intention exists** and write its evidence on the first line of the output. A prompt hands an existing intention to a cue; it does not make one.
2. **Confirm the action is one-off or a fixed appointment.** If it is repeated, stop; the field evidence says the prompt will not hold.
3. **Map the real options:** the dates the action can be done, the places, the hours, what the person must bring. The prompt offers these; it does not ask the person to invent them.
4. **Write the prompt with three blanks: date, time, place.** Date alone was not significant; ask for all three. Phrase it as the person's own plan ("I will go on ___ at ___ to ___"), not a slot the program assigns. Add a "how" (transport, who comes along) where getting there is the hard part.
5. **Attach it to an existing contact.** Name the message, visit, or form it rides on and the moment within that contact when the question is asked. Make it timely: close enough to the window that the plan is concrete, early enough that the slot is still open.
6. **Keep the plan with the person.** Say what the person keeps: a card, the message on their phone, a line on the referral slip. A plan spoken and gone loses the cue.
7. **Avoid a numeric goal in the prompt** ("save 500 taka") unless the action itself is a number; one source reports numeric goals doing worse than general commitments (unverified, author to confirm). Ask for when, where, how.
8. **State the small expected effect.** Field trials gave about 4 points; discount further where households plan together or literacy limits writing.
9. **Specify the pre-test:** 5 to 10 people from the population fill in the prompt cold; pass = every blank holds a real date, a time, and a place that exists in the window map.
10. **Stop here.** Final-language wording, sender, and the fidelity trace go to `draft-lever-content`; a program-sent follow-up on the planned date is `design-reminder-schedule`.

See `references/evidence-notes.md` for the annotated sources and `references/worked-example.md` for a complete run on HIV self-test result reporting in Lagos.

## Output template

```markdown
# Implementation intention prompt

**Target behavior:** <who + what + when, carried over verbatim>
**Intention check:** <evidence that people already intend to act, with its source; or "no evidence found: do not run">
**Action type:** <one-off / fixed appointment; the window: dates, hours, places, what to bring>

## The prompt (working copy)
<the literal prompt with blanks, e.g. "I will <action> on <date> at <time> at <place>. I will get there by <how>.">

## Why each element is there
- **Date:** <...>
- **Time:** <why it is asked; date-only was not significant>
- **Place:** <the real options offered>
- **How / with whom:** <if used, why; otherwise "not used">

## Delivery
- **Rides on:** <the existing contact: message, visit, form>
- **Asked by:** <who>
- **When:** <relative to the action window, and why that lead time>
- **What the person keeps:** <card, phone message, slip>

## Boundary checks
- **One-off:** <confirmed how>
- **Organic planning:** <does this population plan together already; effect halved if so>
- **Numeric goal:** <none used / used because the action is itself a number>

## Expected effect
<the published numbers, then the planning range for this program and why it is smaller>

## Required pre-test
<n, procedure, pass criterion>

## What to check before relying on this
- <the assumption most likely to be wrong>
```

## Where it goes wrong

- **Prompting an intention that is not there.** Asking people to plan when they will do something they do not want, trust, or understand produces blank forms or invented plans. The intention check is mandatory; "we assume they want it" fails it.
- **Running on a repeated behavior.** Daily pills, weekly deposits, exercise: the one field trial here found a null, and a prompt that worked for a flu shot does not carry over. Route to `design-habit-anchor`.
- **Date only.** A prompt that asks "when will you come?" and accepts "next week" is the 1.5-point version. Ask for date, time, and place, and make the blanks fit only specific answers.
- **The program's plan, not the person's.** "We have put you down for Tuesday at 10" is an appointment, not an implementation intention. The person names the moment; the program offers the options.
- **Planning on d = 0.65.** The meta-analytic effect is probably inflated relative to field trials; the two large field trials gave about 4 points. A pilot powered on 0.65 will be underpowered.
- **A plan the person cannot keep.** Asking for a date and place when clinic hours, transport, or a spouse's permission make the plan impossible turns the prompt into a record of failure. The window map exists so the blanks can only be filled with real options.

## When to bring in a specialist

Tell the user to consult the relevant specialist when:
- The action carries clinical or safety risk at the planned moment (disclosing an HIV status, leaving home for care where that needs permission, attending somewhere unsafe at certain hours); a clinician or safeguarding lead must review whether asking for a written plan can expose the person, and who will see the plan
- The population includes people whose dates and places are set by someone else (minors, women who need a spouse's permission, workers on shifts); a local qualitative researcher should check whether asking for a plan is realistic or shaming before the pre-test
- The program intends to put the prompt in front of a large population on the strength of evidence untested outside WEIRD samples; a behavioral scientist should design a pilot with a control arm before scale, since the honest planning number is a few points

Bring them: the prompt, the intention evidence, the window map, and a note on who sees the written plan.
