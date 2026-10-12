# Worked example: antenatal iron-folate reminder SMS, Malawi

A maternal-health NGO working with four rural clinics in Dedza district, Malawi, sends a weekly SMS to pregnant women enrolled in antenatal care, reminding them to take their daily iron-folate tablet. The lever brief from `select-intervention-levers` chose prompts and cues for a confirmed barrier (forgetting on busy days), and `draft-lever-content` produced a gain-framed working draft. The program manager asked whether the message "would hit harder" as a loss. All numbers are illustrative; this is not a real result.

Inputs the user gave: the behavior (pregnant women enrolled at the four clinics take one iron-folate tablet every day from the first antenatal visit to delivery); the vehicle (a weekly SMS in Chichewa from the clinic's number); the existing draft; about 1,200 women enrolled per quarter across the clinics, SMS sent per phone number so randomization by person is feasible; nothing known yet about reactions to loss language.

```markdown
# Message frame decision

**Behavior:** Pregnant women enrolled at the four Dedza clinics take one iron-folate tablet every day from their first antenatal visit until delivery.
**Behavior type:** Prevention, because taking the tablet reduces the risk of anemia; it does not reveal whether anemia is present.
**Vehicle:** Message; weekly SMS in Chichewa from the clinic's number.
**Source draft:** From draft-lever-content (gain-framed working copy; Chichewa final copy pending).

## Default frame
Gain, because for prevention messages the meta-analytic evidence favors gain frames by a small margin (r = 0.083; Gallagher & Updegraff, 2012) and nothing in the evidence favors loss frames for this kind of behavior.

## Paired variants
| | Gain frame | Loss frame |
|---|---|---|
| Text | "Taking your iron tablet every day keeps your blood strong for you and your baby. Take today's tablet after your evening meal." | "Missing your iron tablet leaves your blood weak for you and your baby. Take today's tablet after your evening meal." |
| Held constant | Same fact (iron and blood), one action (take today's tablet), same cue (after the evening meal), same sender, 23 words | Same, 22 words |

## A/B test plan
- **Unit of randomization:** Person (phone number), stratified by clinic.
- **Primary outcome:** Tablets taken, from pill counts at the next antenatal visit; not "do you intend to take it".
- **Expected difference:** At most r = 0.083 in favor of gain, possibly zero. The difference between frames is expected to be far smaller than the difference between sending the SMS and not sending it.
- **Sample:** About 1,200 women per quarter is unlikely to detect a difference this small; run `estimate-sample-size` before committing, and decide whether a frame test is worth running at all.
- **Decision rule:** If no difference is detected, keep the gain frame as final copy.

## Before launch
- Show both variants cold to 8 women at two clinics; pass = all restate the action as "take the tablet after the evening meal"; record any reaction to "weak blood" as alarming, shaming, or inappropriate to say by SMS.
- Escalation: none. No money is involved and the behavior is not detection of a stigmatized condition.

## What to check before relying on this
- Whether women experience the tablet as preventing anemia (prevention) or as treatment for a condition they believe they already have; if the latter, the classification is less clear and the gain default rests on weaker ground.
- Whether "weak blood" carries a local meaning the team has not checked that makes the loss variant unacceptable regardless of the test.
```

What the skill did not do: write the final Chichewa copy (`draft-lever-content`), decide whether the SMS should be weekly or daily (`design-reminder-schedule`), or recommend running the frame test as the program's main evaluation.
