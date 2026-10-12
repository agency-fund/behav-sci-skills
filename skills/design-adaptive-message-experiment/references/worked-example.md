# Worked example: HIV self-test kit requests in Lagos

Illustrative run. The program, numbers, and messages are invented to show the shape of a complete output; none is a finding. Setting: an NGO's WhatsApp line lets people who registered at community outreach in Lagos request a free HIV self-test kit for delivery. Registrations run at roughly 600 a week (illustrative). Five message variants came from `write-social-norm-message`, `design-reminder-schedule`, and `draft-lever-content`; the current message is the control.

**Experiment intent (from the user):** "We want to know which follow-up WhatsApp message gets registered people to request a self-test kit, so we can make it the standard message for the whole line before the next outreach season."

```markdown
# Adaptive message experiment design

**Experiment intent:** We want to know which follow-up WhatsApp message gets registered people to request a self-test kit, so we can make it the standard message for the whole line before the next outreach season.
**Decision this informs:** Which one message becomes the standard follow-up on the Lagos line from January; decided by the program lead after the confirmatory wave.
**Goal:** Policy choice (pick the best arm afterward), which sets the algorithm to exploration sampling.

## Arms
| Arm | One-line description | Dimension varied | Source |
|---|---|---|---|
| 0 (control) | Current message: "Your free HIV self-test kit is ready. Reply KIT to request delivery." | none | current practice |
| 1 | Control text plus "Most people who registered this month have already requested theirs." | frame: descriptive norm | write-social-norm-message |
| 2 | Control text plus "Delivery is discreet: plain packaging, no name on the parcel." | frame: privacy | write-social-norm-message |
| 3 | Control text plus "Takes 2 minutes. Reply KIT and we handle the rest." | frame: ease | draft-lever-content |
| 4 | Control text, sent at 7 pm instead of 10 am | timing | design-reminder-schedule |
| 5 | Control text signed by a named outreach nurse | messenger | program team |

## Reward metric
Kit requested (a "KIT" reply logged on the WhatsApp platform) within 5 days of the message. Read nightly from the platform export. Chosen because it is logged automatically within days; the outcome that matters more, a test result reported within 30 days, is too slow to adapt on and is checked in the confirmatory phase.

## Batch schedule and exploration floor
| Wave | People | Allocation rule |
|---|---|---|
| 1 | about 600 (one week of registrations) | even split, 100 per arm (burn-in) |
| 2 to 5 | about 600 each | exploration sampling with a floor of 8% per arm (illustrative) and control fixed at 15% |
Minimum gap between waves: 5 days (the reward window); in practice one wave per Monday. The data officer triggers each wave after the previous wave's rewards are read.

## Algorithm
Exploration sampling, because the team wants to choose one message for the whole line afterward; Thompson sampling would pile later waves onto an early leader and leave the runners-up too thin to compare.

## Inference plan
Adaptive-phase request rates are reported as descriptive only. The effect of the selected arm against control is estimated in the confirmatory wave (below) with an ordinary two-arm comparison. If the partner statistician is available, the adaptive-phase data are additionally analyzed with an estimator built for adaptively collected data, with a winner's-curse correction for the selected arm; otherwise that analysis is not reported.

## Stopping rule and holdout
Stop the adaptive phase after wave 5, or earlier if the estimated probability that the leading arm is best exceeds 0.9 (illustrative) at the end of a wave. Control is held at a fixed 15% of every wave throughout.

## Confirmatory test
Wave 6 (about 600 people): selected arm versus control, 50/50, same 5-day reward. Persistence check: share of each arm reporting a test result within 30 days, read on day 45 after wave 6.

## Implementation
The data officer runs the assignment script each Monday from the platform export; the WhatsApp line sends by arm label. Arm 1 is sent only if the "most people have already requested" claim is true in the previous wave's data; if it is not, arm 1 is dropped, not softened. Participants were told at registration that follow-up messages vary; no further notification is planned (per organization policy; to confirm).

## Open questions
- Whether 7 pm sends (arm 4) reach people on shared phones; check reply rates by registration channel after wave 1.
- Whether the partner statistician can take the adaptive-phase analysis; if not, the confirmatory wave is the only effect estimate.
- The 0.9 stopping threshold and the 8% floor are the team's choices, not from any source; keep them unless the statistician advises otherwise.
```
