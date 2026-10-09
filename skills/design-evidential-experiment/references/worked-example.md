# Worked example: testing a first-question menu in MaizeMate

This example continues the MaizeMate running case used across the AI-evaluation skills ported from Joe Speed's prototype: a WhatsApp AI agronomy assistant for smallholder maize farmers in western Kenya. It is illustrative, not a real program. The weak-link diagnosis came from `diagnose-funnel-weak-link`.

**Inputs (condensed):** MaizeMate's weak-link diagnosis found that log analysis supported H1: onboarded farmers type nothing, because they do not know what to ask. Intent: test a first-question example menu against the open-ended prompt.

```markdown
# Experiment configuration brief

**Hypothesis under test:** H1: onboarded farmers don't engage because the open "ask me anything" prompt gives no model of a good first question; a localized example-question menu will raise onboarding→engagement.
**Decision rule:** 8 percentage points or more of lift in week-1 engagement: the menu becomes the default for all new farmers. Null: H1 is weakened; escalate H3 (data cost) to a delivery-model review. Negative: keep the open prompt and log the result in the registry.

## Design
| Field | Value | Why |
|---|---|---|
| Experiment type | freq_online | open enrollment: new farmers appear daily; there is no fixed roster to preassign |
| Randomization unit | individual (farmer_wa_id) | the menu is per chat; no within-cooperative spillover expected for a UI prompt |
| Arms | control: open prompt / treatment: 4-item example menu (county-localized) | 50/50 |
| Eligibility filters | onboarding_complete includes true; enrollment_date between 2026-08-17 and 2026-10-12 | new onboarders only; existing users have already seen the open prompt |
| Strata | n/a (online experiments assign without stratification) | |
| Start / end | 2026-08-17 → 2026-10-12 | |

## Metrics
**Primary:** engaged_week1 (boolean: at least one substantive question within 7 days of onboarding), detectable effect +8 percentage points on a 31 percent baseline, from the decision rule above, not the default baseline × 0.1 (which would be a meaninglessly small 3.1 points for this decision).
**Guardrails:** setup_completion_rate (must not fall; a menu shown mid-onboarding could add friction); guardrail_refusal_rate (must not rise; menu items must not bait out-of-scope queries).

## Power & stopping
Power 0.8, alpha 0.05; the power check against the participants table says about 1,100 farmers are needed, roughly 8 weeks of enrollment at current recruitment rates, hence the end date. Stopping: end_date; no early stopping on interim p-values (the online design has no balance check, so mid-stream peeks are doubly untrustworthy at small n).

## Delivery integration
The product lead maps arm_name → WhatsApp flow: assignment is fetched per farmer at onboarding-complete via the per-participant assignment endpoint; "menu" routes to the menu journey, "control" to the current prompt. A webhook on commit notifies the backend to activate the mapping.

## Analysis plan
ITT on engaged_week1 via Evidential's OLS; no strata controls (online); the research lead reads the dashboard at the end date and records decision + impact in the registry. Small-sample caution: check arm sizes for drift weekly, since online assignment carries imbalance risk.

## Data & ethics notes
Participants table: farmers view, unique id farmer_wa_id (hashed; raw phone numbers must not be the id). Message variants fall under the program's existing service-improvement consent; no additional data is collected beyond standard logs.
```
