---
name: design-reminder-schedule
description: >-
  Use when people intend to do something with a due date (the next vaccine
  dose, a clinic review, a loan installment, a savings deposit) and miss it
  because it slips their mind, and the team wants to send reminders. Also use
  when a team is about to "text everyone" and has not decided the timing,
  frequency, channel, or what the message names, or whether reminders alone
  can work. Specifies when each reminder goes, how often, through which
  channel, and what it names, drawing on the Thakkar et al. (2016) adherence
  meta-analysis, the Kenya ART and Haryana immunization trials, and Karlan et
  al. (2016) savings reminders. Do not use when the person should make their
  own plan once for a one-off action; use draft-implementation-intention-prompt.
  Not for picking the calendar moment to deliver an offer
  (choose-delivery-moment), who sends it (select-messenger), whether to pay
  (design-incentive-scheme), or the message text itself (draft-lever-content).
license: CC-BY-4.0
metadata:
  title: Plan when and how often to remind
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: mixed-evidence
  tags: "reminders, behavior-change-techniques, sms"
  consumes: "intervention-levers, audience-context-brief"
  produces: "intervention-draft"
---

## What it does

Specifies the schedule for reminding people about one pending action they already intend to take.

The output fixes when each reminder goes relative to the action window, how often, through which channel, and what it names, and decides whether reminders alone can carry the effect or need a messenger or an incentive beside them. A reminder works by returning the action to the top of mind at a moment it can be done; it adds no motivation, supply, or trust, which is why SMS alone had no impact in the Haryana immunization trial.

## When to use it

### Use it when
- People intend to do something with a due date (the next vaccine dose, a clinic review, a loan installment, a deposit toward a savings goal) and miss it because it slipped their mind
- A team is about to send SMS ("let's text everyone") and has not decided the timing, frequency, channel, or what the message names
- Reminders already go out and the effect seems to be fading, or nobody knows whether the cadence is right
- The lever brief from `select-intervention-levers` names prompts or cues as the technique

### Do not use it when
- The person should make their own plan once for a one-off action; a plan is made by the person, a reminder is sent by the program. Use `draft-implementation-intention-prompt`
- The question is which moment in the calendar to deliver an offer at (after harvest, at payday); that is `choose-delivery-moment`. This skill sets the cadence around a known due date
- The question is who should send the message, or whether to pay people; those are `select-messenger` and `design-incentive-scheme`, and this skill says when to bring them in
- The team needs the message text in the local language with a fidelity trace; `draft-lever-content` takes this schedule as its input
- The barrier is supply (stock-outs, closed clinics), cost, or distrust rather than forgetting; a reminder for an action people cannot or will not take is noise. Go back to `select-intervention-levers`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The target behavior (who, what, when) and the confirmed barrier with its evidence. The barrier must be forgetting or attention at the moment of action (people say they meant to; attendance rises when someone prompts them; no supply, cost, or trust problem was found). If the evidence points to supply, cost, or trust, say so and stop.
2. **Required.** The due-date structure: one fixed date per person, a rolling window, or a recurring cycle; and how the program knows each person's date (a register, an app, the person's own report).
3. **Required.** Phone access from the audience and context brief: who owns the phone, whether it is shared, literacy, language, network coverage, and which channels already reach this population.
4. Optional. Whether a messenger or an incentive is already part of the program, and the budget per person, which sets the bundling decision.
5. Optional. Any data from reminders already sent (delivery rates, opt-outs, responses), which seeds the decay check.

If 1, 2, or 3 is missing, ask and stop. If 4 is missing, design for reminders alone and leave the bundling question open. If 5 is missing, plan the decay check from zero.

## What it draws on

- Thakkar, J., et al. (2016). Mobile telephone text messaging for medication adherence in chronic disease: A meta-analysis. *JAMA Internal Medicine*. https://doi.org/10.1001/jamainternmed.2015.7667
- Free, C., et al. (2013). The effectiveness of mobile-health technology-based health behaviour change or disease management interventions for health care consumers: A systematic review. *PLoS Medicine*, 10(1), e1001362. https://doi.org/10.1371/journal.pmed.1001362
- Karlan, D., McConnell, M., Mullainathan, S., & Zinman, J. (2016). Getting to the top of mind: How reminders increase saving. *Management Science*, 62(12), 3393–3411. https://doi.org/10.1287/mnsc.2015.2296
- Pop-Eleches, C., et al. (2011). Mobile phone technologies improve adherence to antiretroviral treatment in a resource-limited setting: A randomized controlled trial of text message reminders. *AIDS*, 25(6), 825–834. https://doi.org/10.1097/QAD.0b013e32834380c1
- Horvath, T., et al. (2012). Mobile phone text messaging for promoting adherence to antiretroviral therapy in patients with HIV infection. *Cochrane Database of Systematic Reviews*, CD009756. https://doi.org/10.1002/14651858.CD009756
- Gibson, D. G., et al. (2017). Mobile phone-delivered reminders and incentives to improve childhood immunisation coverage and timeliness in Kenya (M-SIMU): A cluster randomised controlled trial. *The Lancet Global Health*, 5(4), e428–e438. https://doi.org/10.1016/S2214-109X(17)30072-4
- Banerjee, A., Chandrasekhar, A. G., Dalpath, S., Duflo, E., Floretta, J., Jackson, M. O., et al. (2025). Selecting the most effective nudge: Evidence from a large-scale experiment on immunization. *Econometrica*, 93(4), 1183–1223. https://doi.org/10.3982/ECTA19739
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709
- Behavioural Insights Team (2014; revised and updated edition, c. 2024). *EAST: Four simple ways to apply behavioural insights*, "Make it timely". London: BIT. https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf

A reminder returns a pending action to attention at a moment it can be acted on; the mechanism is limited attention, not motivation or means. Thakkar et al. (2016) pool 16 RCTs (N = 2,742) of text reminders for medication adherence: odds ratio 2.11 (95% CI 1.52–2.93), falling to 1.68 after adjustment for publication bias; adherence was estimated to rise from 50% to 67.8%. Free et al. (2013) review 75 trials, mostly low quality and nearly all in high-income countries. Karlan et al. (2016) ran reminder trials with savers in Bolivia, Peru, and the Philippines: reminders raised savings-goal attainment, messages that named the goal and the incentive worked best, and loss versus gain framing made no difference; the effect size is unverified in the dossier. Pop-Eleches et al. (2011), at a clinic in Kenya, found weekly SMS raised the share of patients reaching 90% ART adherence by about 13 to 16 points over 48 weeks (a secondary-source figure); the Cochrane review (Horvath et al., 2012) rated two Kenyan weekly-SMS RCTs as high-quality evidence. Gibson et al. (2017), Kenya: SMS plus incentives improved immunization coverage and timeliness in a high-coverage setting; effect size unverified. Banerjee et al. (2025), Haryana: SMS reminders alone had no impact, and SMS plus local information-hub ambassadors was the most cost-effective bundle (+9.1% immunizations per dollar; a secondary-source figure). Most of this evidence is already from the field, so the discount is smaller than for lab-based techniques, but the published odds ratio still shrinks by bias correction and academic trials average 8.7 percentage points where nudge-unit trials average 1.4 (DellaVigna & Linos, 2022); plan on the corrected numbers and on the Haryana null as the floor. The judgment calls this skill adds are the barrier check, the "reminders alone?" decision, the stop rule, and the decay check.

**WEIRD skew:** The meta-analytic numbers (Thakkar; Free) come from trials nearly all in high-income countries, with personal phones and high literacy; the clearest single trials are LMIC. Check locally who holds the phone, whether SMS is read or needs voice, whether the program knows each person's due date, network coverage, and whether the barrier is forgetting at all. **Non-WEIRD evidence:** Kenya (Pop-Eleches et al., 2011: weekly SMS raised the share reaching 90% ART adherence by about 13 to 16 points over 48 weeks; Gibson et al., 2017: SMS plus incentives improved immunization coverage and timeliness, effect size unverified); India (Banerjee et al., 2025, Haryana: SMS alone had no impact, SMS plus ambassadors the most cost-effective bundle); Bolivia, Peru, and the Philippines (Karlan et al., 2016: reminders raised savings-goal attainment, effect size unverified).

**Replication status:** replicated for ART adherence (a 16-trial meta-analysis and two high-quality Kenyan RCTs agree); mixed for immunization (Kenya positive with incentives attached, Haryana null for SMS alone); effects decay over time. A claim that weekly messages beat daily ones in Kenya is unverified, author to confirm, and is not used to set cadence here.

## How to do it

1. **Confirm the barrier is forgetting.** Carry the target behavior and barrier over verbatim and write the evidence that people intend to act and could act if prompted. If the evidence shows stock-outs, fees, distance, or distrust, stop: the Haryana trial is what a reminder does against those barriers.
2. **Map the due dates.** State the structure (fixed, rolling, recurring), how the program learns each person's date, and the action window: the first day the action can be done and the last day it still counts.
3. **Time each reminder shortly before the window opens**, with a lead time long enough to arrange the action (transport, money, time off) and short enough to stay in mind. Say the lead time and the reason. A reminder after the window is a reproach, not a cue.
4. **Set the frequency and the ceiling.** One reminder per window for a one-off action, plus at most one follow-up if the action is not recorded. For a recurring action, one per cycle; the Kenyan ART trials used weekly messages. Do not justify a daily cadence with the unverified weekly-versus-daily claim. State the ceiling (how many sends before stopping) and the stop rule: the action is recorded, the person opts out, or the ceiling is reached.
5. **Write the content requirements** for `draft-lever-content`: the message names the specific action, the date, the place, and the person's own goal where one exists (naming the goal is the Karlan finding; the date and place are this skill's addition so the message lands on a doable moment); one action per message; no effort spent on loss versus gain framing, which made no difference.
6. **Choose the channel** from the audience and context brief: SMS where phones are personal and read; voice where literacy or shared phones make SMS unreliable; a visit where neither reaches. Say who holds the phone and what the message could disclose if someone else reads it.
7. **Decide whether reminders alone can work.** Apply the Haryana test: does the person also need information or trust (bring in `select-messenger`), or does the action cost them money or time they will not spend unprompted (bring in `design-incentive-scheme`)? If supply is unreliable, the answer is neither; stop.
8. **Plan the decay check.** Name what is measured (action rate among reminded versus not, delivery rate, opt-outs), at what intervals, and the drop that triggers a change to the schedule.
9. **State the expected effect, discounted.** Quote the corrected numbers and the nulls, then give a planning range for this program and why it is where it is.
10. **Stop here.** The message text is drafted by `draft-lever-content`; the test is designed by `plan-evaluation-design`.

See `references/evidence-notes.md` for the annotated sources and `references/worked-example.md` for a complete run on immunization camp reminders in Rajasthan.

## Output template

```markdown
# Reminder schedule

**Target behavior:** <who + what + when, carried over verbatim>
**Barrier check:** <evidence that forgetting or attention is the barrier; how supply, cost, and trust were ruled out>
**Due-date structure:** <fixed / rolling / recurring; how each person's date is known; the action window>

## Schedule
| # | Sent when (relative to the window) | Channel | Names | Stops when |
|---|---|---|---|---|
| 1 | <e.g. 2 days before the window opens> | <SMS / voice / visit> | <action, date, place, goal> | <action recorded / opt-out / ceiling> |
| 2 | <...> | <...> | <...> | <...> |

## Frequency and ceiling
- **Per window:** <n sends>
- **Ceiling:** <maximum sends before stopping, and why>
- **Opt-out:** <how a person stops the messages>

## Content requirements (input to draft-lever-content)
- **Names:** <the action, the date, the place, the person's goal>
- **Does not:** <more than one action; loss or gain framing work; anything that discloses a condition on a shared phone>

## Channel choice
<why this channel, from phone ownership, sharing, literacy, language, and network>

## Reminders alone, or bundled?
<the Haryana test: what else the person needs; messenger, incentive, or neither, naming the skill to run>

## Decay check
- **Measure:** <what, among whom, at which intervals>
- **Trigger:** <the drop that changes the schedule, and who decides>

## Expected effect
<the published numbers with their corrections and nulls, then the planning range for this program and why>

## What to check before relying on this
- <the assumption most likely to be wrong>
```

## Where it goes wrong

- **Reminding people to do what they cannot do.** Where the clinic is out of stock, the fee is unaffordable, or the sender is distrusted, reminders produce the Haryana result: no impact, plus annoyance. The barrier check is mandatory, not a formality.
- **A message that names nothing.** "Remember your appointment" is the weak version; the messages that worked best in the Karlan trials named the person's goal. The content requirements must list what the message names.
- **Cadence from memory.** Writing "daily is too much, weekly is right" as if it were a finding; the weekly-versus-daily contrast is unverified, author to confirm. State the cadence as a design choice with a ceiling and a decay check, not as evidence.
- **Assuming a personal phone.** Sending SMS about an HIV clinic visit or a loan installment to a phone held by a spouse or shared in a household. The channel section must say who holds the phone and what the message discloses.
- **Quoting the wrong Kenya number.** A "53%" figure for the Kenyan ART trial circulates and could not be found; the dossier's figure is about 13 to 16 points. Refuse to quote 53%.
- **No stop rule.** Reminders that keep arriving after the action is done, or after the person opted out, erode trust in every later message from the program. Every row in the schedule table ends with a stop condition.

## When to bring in a specialist

Tell the user to consult the relevant specialist when:
- The reminder concerns medication dosing (what to take, how much, when); a clinician or pharmacist must sign off the content requirements, and the schedule must not stand in for clinical follow-up
- The barrier evidence points to supply or trust rather than forgetting (stock-outs, fees, a distrusted sender); the program or supply-chain lead must fix that first, because no schedule will, and the skill should say so rather than design around it
- The population shares phones and the message could disclose a condition (HIV, family planning, debt); a privacy or safeguarding review must happen before the first send
- The program plans to scale on a reminder effect that is decaying; a behavioral scientist should design the decay measurement and say whether a messenger or incentive bundle is the real intervention

Bring them: the schedule table, the barrier evidence, the phone-access data, and the content requirements.
