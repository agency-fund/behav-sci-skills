---
name: design-and-test-an-sms-program
title: Design, size, and test a reminder or message program
description: >-
  For a team that reaches people by SMS, voice, or WhatsApp and wants
  messages that move a behavior with a due date: specify the audience and
  moment, design the schedule and the messenger, set an honest expected
  effect, size the sample, run an adaptive message test with a
  pre-analysis plan, and learn who it worked for. Ends with a result and a
  heterogeneity read-out. Does not cover the diagnosis of why people miss
  the action; run diagnose-to-pilot first if that is unknown.
license: CC-BY-4.0
metadata:
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  stages: "define, design, test, analyze"
  skills: "map-audience-context, design-reminder-schedule, choose-delivery-moment, select-messenger, choose-message-frame, estimate-expected-effect, estimate-sample-size, design-adaptive-message-experiment, design-evidential-experiment, write-pre-analysis-plan, analyze-heterogeneous-effects"
  tags: "reminders, experimental-design, heterogeneity, framing"
---

## What it is for

Message programs are cheap to run and easy to over-promise. This workflow makes the team decide the moment, cadence, sender, and frame on evidence, plan for a small effect, and test several message variants in a way that converges on the best one without breaking inference.

## When to use it

- When the behavior has a due date or a window (a dose, a visit, a deposit, a filing) and the barrier is attention, not supply or trust
- When a team wants to "text everyone" and has not decided what, when, from whom, or how it will know whether it worked
- Not when the barrier is unknown; run `diagnose-to-pilot` through its step 4 first
- Not when the message is meant to shift a community norm; use `change-a-social-norm`

## Skills in this workflow

| Step | Skill | Version | Relationship | What carries forward | Human decision point |
|---|---|---|---|---|---|
| 1 | `map-audience-context` | 0.1.0 | start | audience and context brief, including channels and the decision moment | Confirm phone access, who holds the phone, and language |
| 2 | `design-reminder-schedule` | 0.1.0 | after 1 | timing, cadence, channel, content requirements | Decide whether reminders alone can work or need a messenger or incentive |
| 3 | `choose-delivery-moment` | 0.1.0 | after 1, parallel with 2 | the calendar moment and deadline rule | Check the moment against the audience's income calendar |
| 4 | `select-messenger` | 0.1.0 | after 2 and 3 | messenger choice with rationale | Run the power test on the leading candidate |
| 5 | `choose-message-frame` | 0.1.0 | after 4, optional | gain and loss variants | Approve a loss variant only after the local check |
| 6 | `estimate-expected-effect` | 0.1.0 | after 2 | effect-size benchmark | Sign off on the discounted planning range, not the published number |
| 7 | `estimate-sample-size` | 0.1.0 | after 6 | power calculation | Decide whether the feasible sample can detect the plausible effect; if not, redesign or stop |
| 8 | `design-adaptive-message-experiment` | 0.1.0 | after 4, 5, and 7 | evaluation design with arms, batches, stopping rule | Set the exploration floor and the holdout |
| 9 | `write-pre-analysis-plan` | 0.1.0 | after 8, before launch | analysis plan | Register it before any outcome data exist |
| 10 | `analyze-heterogeneous-effects` | 0.1.0 | after the experiment ends | who benefited, pre-specified versus exploratory | Decide what to pre-register next time; never target on an exploratory split |

Relationship values: `start`, `after N`, `parallel with N`, `independent`, `optional`.

## How to run it

1. Run `map-audience-context` to fix the subgroup, the decision moment, and the channels that already reach them. Phone sharing and literacy decide whether SMS, voice, or a person is the channel.
2. Run `design-reminder-schedule` and `choose-delivery-moment` together: one sets the cadence and content, the other the calendar moment and any deadline.
3. Run `select-messenger`. If the leading candidate holds power over the audience, change the candidate.
4. Run `choose-message-frame` only if the team is tempted by loss framing; its job is to stop that assumption and write both variants for the test.
5. Run `estimate-expected-effect` on the evidence the team is relying on, then `estimate-sample-size` on the benchmark. If the sample cannot detect the plausible effect, do not run an underpowered test; shrink the arms or extend the window.
6. Run `design-adaptive-message-experiment` to turn the variants into arms with a batch schedule and a stopping rule; if the program uses Evidential with fixed allocation, `design-evidential-experiment` replaces this step.
7. Run `write-pre-analysis-plan` and register it before launch.
8. After the experiment, run `analyze-heterogeneous-effects` to learn who the best arm worked for, keeping pre-specified moderators apart from exploratory splits.

## Worked example

An immunization program in Udaipur district, India, wants more children to return for the third pentavalent dose. Step 1 shows most mothers' numbers belong to a husband's phone and that voice in Mewari is needed. Step 2 sets two voice reminders in the week before the camp, naming the child and the camp date; step 3 places them after market day; step 4's community nomination picks local "information hubs" rather than the ASHA by default, with a random-messenger comparison arm. Step 6 discounts the published reminder effects to a planning range of a few percentage points; step 7 shows the eight-camp sample can detect that only with a two-season window, which the team accepts. Step 8 sets three message arms with a 20% exploration floor; step 9 registers the plan. Step 10 finds the effect concentrated among mothers more than five kilometers from the camp, a hypothesis for the next round rather than a targeting rule.

## Where it goes wrong

- Planning on the meta-analytic number in step 6; field reminder effects are a few points, and the Haryana null for SMS alone is the floor.
- Running step 8 with a reward metric that lags by weeks; adaptive assignment needs a fast signal or it is a fixed-allocation trial with worse inference.
- Writing the pre-analysis plan after the first batch's results are in.
- Turning step 10's exploratory split into an eligibility rule.

## When to bring in a specialist

- Medication reminders: a clinician reviews content in step 2.
- Fewer than about 30 clusters or a rare outcome in step 7: a statistician owns the power calculation.
- Adaptive assignment with no engineer to implement it, or arms that could harm: an experimentalist redesigns step 8 as a fixed-allocation trial.
