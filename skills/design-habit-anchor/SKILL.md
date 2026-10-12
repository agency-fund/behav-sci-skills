---
name: design-habit-anchor
description: >-
  Use when a program needs people to do something small every day or every
  week, long after the program stops prompting them: taking a daily iron
  tablet, washing hands before cooking, logging each sale, depositing a
  fixed amount on market day. Also use when a team plans to "build a habit
  in 21 days" or assumes a reminder campaign will leave a habit behind when
  it ends. Shrinks the behavior to its minimum repeatable version, ties it
  to one stable cue the person already meets every day, adds a tick sheet,
  and plans a two-to-three-month repetition period with a persistence
  check, drawing on Lally et al. (2010) and Gardner, Lally and Wardle
  (2012). Do not use when the behavior happens once or rarely (a
  vaccination visit, a registration); use draft-implementation-intention-prompt
  instead. Not for scheduling SMS or call reminders
  (design-reminder-schedule), and not for writing the final prompt or
  leaflet wording (draft-lever-content).
license: CC-BY-4.0
metadata:
  title: Anchor a repeated behavior to a daily cue
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: untested-outside-weird
  tags: "habit-formation, behavior-change-techniques, reminders"
  consumes: "intervention-levers"
  produces: "intervention-draft"
---

## What it does

Links one repeated target behavior to a stable cue the person already meets every day, so that after enough repetitions the cue itself triggers the behavior.

A habit is a cue-response link learned by repeating a behavior in the same context; once formed, it runs with little deliberation, which is why it can outlast reminders, incentives, or a program. The one study that timed this found a median of 66 days to self-reported automaticity, with a range of 18 to 254, in 96 volunteers. This skill chooses the cue, shrinks the behavior so it can be repeated, supplies a tick sheet, and plans the months of repetition and the check that follows, while saying plainly that the timeline rests on a small study from a WEIRD setting.

## When to use it

### Use it when
- "We want them to keep taking the tablet without us texting every day"
- "How long do we need to keep the reminders going before it sticks?"
- "Build a savings habit in 21 days" or "a 30-day challenge" is on the table
- The lever brief from `select-intervention-levers` names the BCTTv1 technique "Habit formation" or "Prompts/cues" and the behavior repeats daily or near-daily

### Do not use it when
- The behavior happens once or a few times a year (a vaccination visit, a registration, a one-off deposit); the evidence for one-off actions is for implementation intentions, so use `draft-implementation-intention-prompt`
- The team wants to decide how often to send SMS or call reminders; that is `design-reminder-schedule`. A habit anchor aims to make external prompts unnecessary, so use both only with a plan to fade the reminders
- The anchor is designed and the team needs the leaflet, tick sheet, or prompt wording; that is `draft-lever-content`
- The barrier is supplies, cost, or skill rather than forgetting or inconsistency; a cue does nothing for a tablet that is not in the house, so go back to `select-intervention-levers`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The behavior as who, what, when, and how often it must happen (every day, every market day, every shift). If it is less than a few times a week, say so: the timing evidence is for daily behaviors, and a weekly behavior will take correspondingly longer or may not become automatic at all.
2. **Required.** Three to five things the person already does at a fixed point every day without being told (morning prayer, the first cup of tea, opening the stall, the school bell, the evening meal). These must come from the population, through interviews or the audience and context brief, not from the team's guess.
3. **Required.** Whether the behavior needs anything to be physically present at the cue moment (the tablet, the soap, the phone with the savings menu), and whether it is.
4. Optional. Whether a reminder schedule already runs, and whether the team is able to fade it.
5. Optional. Whether the behavior is a clinical regimen where a missed dose matters (antiretrovirals, TB treatment, insulin); that is an escalation condition.

If 1, 2, or 3 is missing, ask and stop; a cue chosen by the team for the person is the most common way this fails. If 4 is missing, assume no reminders run. If 5 is missing, ask once; if the behavior is any medication, treat it as clinical until told otherwise.

## What it draws on

- Lally, P., van Jaarsveld, C. H. M., Potts, H. W. W., & Wardle, J. (2010). How are habits formed: Modelling habit formation in the real world. *European Journal of Social Psychology*, 40, 998–1009. https://doi.org/10.1002/ejsp.674
- Gardner, B., Lally, P., & Wardle, J. (2012). Making health habitual: The psychology of 'habit-formation' and general practice. *British Journal of General Practice*, 62(605), 664–666. https://doi.org/10.3399/bjgp12X659466
- Wood, W., & Neal, D. T. (2007). A new look at habits and the habit–goal interface. *Psychological Review*, 114(4). https://doi.org/10.1037/0033-295X.114.4.843
- Milkman, K. L., et al. (2021). Megastudies improve the impact of applied behavioural science. *Nature*, 600, 478–483. https://doi.org/10.1038/s41586-021-04128-4
- Blumenstock, J., Callen, M., & Ghani, T. (2018). Why do defaults affect behavior? Experimental evidence from Afghanistan. *American Economic Review*, 108(10), 2868–2901. https://doi.org/10.1257/aer.20171676
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709

Wood & Neal (2007) describe a habit as a learned link between a context cue and a response, formed by repetition and run with little goal deliberation; this is why a formed habit survives when the goal, reminder, or incentive that started it fades, and why the cue must be stable: change the context and the link does not fire. Lally et al. (2010) followed 96 volunteers who each chose one new daily behavior tied to a daily cue and rated its automaticity each day; the median time to the automaticity plateau was 66 days, with a range of 18 to 254 days, some missing data, and self-reported automaticity as the only measure. Gardner, Lally & Wardle (2012) turn this into advice for general practice: pick one behavior, tie it to a daily cue, repeat, and track it. The dossier is explicit that "21 days" is not evidence-based and must not be cited as such. The boundary evidence is sobering: in the megastudy of 54 gym interventions (61,293 people, US), only 8% of interventions produced effects that persisted after the program (Milkman et al., 2021), so persistence is the exception this skill has to design for, not an assumption. The judgment calls this skill adds: the two-to-three-month planning window is a rounding of the 66-day median toward the upper half of the range; the tick sheet is the self-monitoring aid implied by Gardner, Lally & Wardle; and the cue-stability checklist is this skill's own operationalization of "stable context". See `references/evidence-notes.md`.

**How much to discount.** The 66-day median comes from volunteers who chose their own behavior and cue in a research study, so it is closer to a best case than a field estimate. The dossier's cross-cutting pattern (lab 0.33 SD against field 0.02 SD for loss contracts; academic trials 8.7 points against nudge-unit trials 1.4 points, DellaVigna & Linos, 2022) says to discount published effects when transferring them to a field program; here that means planning for longer than 66 days, expecting a share of people never to reach automaticity, and treating persistence after support ends as something to measure rather than assume.

**WEIRD skew:** The timing study is a single small sample of 96 volunteers in a WEIRD research setting, with self-reported automaticity; the persistence benchmark is a US gym population. Check locally which daily cues are truly fixed (prayer times, meals, and market days vary by season, religion, and household role) and whether a daily tick sheet is acceptable and usable by people with low literacy. **Non-WEIRD evidence:** Afghanistan (Blumenstock, Callen & Ghani, 2018): 949 employees of one firm; a default savings contribution led to savings attitudes and habits that persisted after the trial. That is evidence that a repeated behavior started by a default can persist in an LMIC, not a test of cue-anchoring. No LMIC habit-formation study was found in the sources this skill draws on.

**Replication status:** Mixed. The habit mechanism is a well-established theoretical account; the timeline rests on one study of 96 people (median 66 days, range 18–254, self-report); persistence after programs end is rare in the one megastudy that measured it (8% of 54 interventions).

## How to do it

1. **Shrink the behavior to its minimum repeatable version**: one tablet, one deposit of a fixed small amount, one handwash with soap. Repetition is the mechanism, and a behavior too large to repeat on a bad day will not be repeated enough.
2. **Choose the cue from the person's own candidates** and run the stability check on each: happens every day, at the same place, already automatic, immediately before the moment the behavior can be done, with whatever the behavior needs already there. Reject anything the program controls (an SMS, a visit), because the aim is a cue that outlasts the program. See `references/evidence-notes.md` for why each criterion matters.
3. **Write the link in the person's words**: "After I <cue>, I will <behavior> at <place>." One cue, one behavior, one place.
4. **Specify the tick sheet**: one mark per day, kept where the cue happens, for the person's own eyes. Say what it is for (seeing the run of repetitions) and what it is not (reporting to the program).
5. **Set the repetition period at two to three months** and write down why: median 66 days, range 18 to 254, in a small self-report study. Tell people a missed day is a missed day, not a reset, so that one miss does not end the attempt.
6. **Plan the fade.** If reminders or incentives run alongside, state the date they stop (the end of the repetition period) so the cue, not the SMS, becomes the trigger. If the team cannot fade them, say that the program is buying compliance, not a habit.
7. **Plan the persistence check**: the behavior measured at the end of the repetition period and again one to three months after all support has stopped, plus one self-report automaticity item ("I do it without having to think about it"), labeled as self-report.
8. **State the limits honestly** in the output: the timeline rests on 96 volunteers in a WEIRD setting, persistence is the exception in the field, and some people will never reach automaticity.
9. **Stop here.** `draft-lever-content` writes the leaflet or prompt; `design-reminder-schedule` plans any fading reminders; `plan-evaluation-design` sets up the persistence check as a measured outcome.

See `references/worked-example.md` for a complete run on market vendors' daily M-Pesa deposits in Kenya.

## Output template

```markdown
# Habit anchor plan

**Behavior:** <who + what + when, carried over verbatim>
**Minimum repeatable version:** <the smallest form that still counts, and why it is small enough to do on a bad day>
**Frequency:** <daily | each market day | each shift>; <note if less than daily>

## Cue
**Chosen cue:** <from the person's own candidates>
| Check | Answer |
|---|---|
| Happens every day | <yes/no, and seasonal or household exceptions> |
| Same place each time | <...> |
| Already automatic for the person | <...> |
| Immediately before the behavior can be done | <...> |
| What the behavior needs is present at that moment | <...> |
| Not controlled by the program | <...> |
**Rejected cues:** <each, with the check it failed>

## Link statement
"After I <cue>, I will <behavior> at <place>."

## Tick sheet
<format, where it lives, one mark per day, for the person's own use; literacy and material notes>

## Repetition period
<two to three months, with the reason: median 66 days, range 18–254, small self-report study; what to tell people about missed days>

## Supports to fade
<reminders or incentives running alongside, and the date each stops; or "none">

## Persistence check
- **At the end of the period:** <behavior measure>
- **After support stops:** <behavior measure at one to three months, plus the self-report automaticity item>

## What to check before relying on this
- <the cue most likely to be unstable here>
- <the limit of the timeline evidence, stated plainly>
```

## Where it goes wrong

- **The 21-day myth, or any settled timeline.** The model will reach for "21 days" or "30 days" because they are everywhere, or write "habits form in about ten weeks" as a fact. The one timed study found a median of 66 days and a range up to 254 in 96 volunteers using self-report; give the number with its sample size, the self-report caveat, and the WEIRD setting, or a team will plan budgets on it.
- **A behavior too big to repeat.** "Save 10% of income each day" or "the full handwashing routine" is not repeatable on a bad day; shrink it until it is, or no habit forms.
- **A cue the program owns.** Anchoring to the daily SMS or the health worker's visit forms a habit of responding to the program. When the program stops, so does the behavior.
- **An unstable cue.** "After lunch" for someone whose lunch moves with the work, or a prayer time that shifts with the season; the stability table exists to catch this before the field does.
- **Nothing present at the cue moment.** The tablet is in a bag at the clinic, the soap is at the other tap; the link fires and the behavior cannot happen, which teaches the opposite link.
- **Measuring only while support runs.** Compliance during the reminder period says nothing about habit; the only evidence of a habit is the behavior after support stops.

## When to bring in a specialist

Tell the user to consult the relevant specialist when:
- The behavior is a clinical regimen where a missed dose matters (antiretrovirals, TB treatment, insulin, anticoagulants); a clinician must set what else protects against misses, because a habit anchor is a support, not a safeguard, and a missed day during the repetition period is expected
- The behavior has safety-critical timing (a medication relative to food or sleep); the cue cannot be chosen on convenience alone
- The candidate cues are religious or household practices the team does not share; a local advisor should confirm that tying a program behavior to prayer or a meal is acceptable and not disrespectful

Bring them: the behavior in its minimum version, the cue table with rejected cues, the fade plan, and the persistence check design.
