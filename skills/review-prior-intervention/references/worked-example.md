# Worked example: a daily SMS medication-reminder program

This example is from Joe Speed's prototype. It is illustrative, not a real program or dataset. The team's account was the only input; the gateway delivery logs it mentions were checked during the review.

**Prior intervention (as given):** "We ran a 3-month SMS reminder program to improve adherence to a daily medication for enrolled patients. We sent one reminder text per day at 8am. Adherence, measured by pharmacy refill records, barely moved. Our take is that patients just don't care enough about their health to act on a reminder."

```markdown
# Intervention post-mortem brief

**Prior intervention (as given):** A 3-month SMS reminder program sending one daily 8am text to improve medication adherence, measured via pharmacy refill records; adherence barely moved, and the team's take is that patients don't care enough to act on a reminder.

## What was planned
Daily 8am SMS reminder to each enrolled patient, intended to prompt the same-day medication-taking behavior, for 3 months.

## What was actually implemented
- **Fidelity:** Not fully as designed. The SMS gateway's delivery logs (once checked) show roughly 30% of messages failed silently on a subset of carriers, with no fallback or resend. **Basis:** Confirmed by the gateway's own delivery logs.
- **Dose:** For patients on affected carriers, effective dose was closer to 2 reminders a week than the planned 7, a large gap between planned and actual exposure. **Basis:** Confirmed, derived directly from the delivery-log failure rate above.
- **Reach:** All enrolled patients were nominally in scope, but the carrier issue meant reach to a working reminder was uneven and was not segmented or reported at the time. **Basis:** Confirmed that reach was uneven; which specific patients were affected is inferred, not logged.
- **Context:** No change reported in the delivery environment itself (clinic operations, patient population) during the 3 months. **Basis:** Confirmed by the record (absence of a reported change).

## Outcome as observed
Pharmacy refill records (a systematically tracked administrative measure, not a self-report) show adherence essentially flat. Moderate-confidence evidence on the outcome measure itself, but confounded by the fidelity gap above, since the intervention actually delivered was substantially weaker than the one being evaluated.

## Causal claim check
- **Team's stated reason for the outcome:** Patients don't care enough about their health to act on a reminder.
- **Does the collected data actually support this claim?** No direct support. No patient-level data on message receipt, engagement, or attitude was collected; the claim is an inference from the flat outcome alone, not from any data about patient motivation.
- **Alternative explanation the data doesn't rule out:** A substantial share of patients may never have reliably received the reminder at all, given the roughly 30% carrier-level delivery failure. Motivation was never actually tested against a fully delivered intervention.

## Implementation failure vs. idea failure
Cannot yet tell whether the reminder idea fails, but there is a confirmed implementation failure (the carrier delivery gap) substantial enough that the idea has not actually been fairly tested yet. The team's causal claim about patient motivation is not supported by the data collected.

## Factors to address before any retry
Confirm SMS delivery success at the individual-message level (not just enrollment), across all patient carriers, before attributing any future flat result to the reminder concept itself rather than to delivery failure.
```
