# Worked example: measuring the M-Pesa savings deposit among Nairobi market vendors

This example continues the running case used across the skills ported from Joe Speed's prototype. The target behavior came from `define-key-behavior`, and the barrier hypotheses from `decompose-comb-barriers`; no intervention lever brief was available, so the comparison condition states its rollout assumption. It is illustrative, not a real program.

**Target behavior (from `define-key-behavior`):** "Female stall vendors in Nairobi's Gikomba and Toi markets deposit that day's net cash surplus into an M-Pesa savings wallet before leaving the market, each trading day."

```markdown
# Evaluation design brief

**Target behavior:** Female stall vendors in Gikomba and Toi markets deposit that day's net cash surplus into an M-Pesa savings wallet before leaving the market, each trading day.

## Primary outcome metric
Share of enrolled vendors' trading days with at least one same-day M-Pesa savings-wallet deposit, measured via transaction logs, not self-reported saving, which the evidence base flags as unreliable for this population. Recording risk: if agents are later paid per deposit, agents could split one deposit into several; the metric counts days with a deposit, not deposit counts, to blunt that.

## Comparison condition
Randomized waitlist: vendors enrolled in month 2 serve as the comparison group for vendors enrolled in month 1, rather than pre/post on one group alone. Market-wide seasonal income shocks would otherwise be indistinguishable from a program effect.

## Minimum effect worth detecting
A 10-percentage-point increase in the share of trading days with a deposit, the threshold the program sponsor has said would justify scaling past the pilot markets.

## Data source feasibility
M-Pesa transaction logs are technically available via the mobile money provider's API with vendor consent, at daily frequency. Confirmed feasible. Household-level savings totals are not independently verifiable and are explicitly out of scope for the primary outcome.

## Mediating measures
- Motivation/reflective hypothesis ("doesn't trust mobile savings versus cash"): a 3-item trust-in-mobile-savings survey scale, administered pre-enrollment and at 8 weeks.
- Opportunity/social hypothesis ("visible saving invites borrowing requests"): self-reported frequency of borrowing requests at the stall, weekly, for the enrolled group only.

## Pre-registration statement
As of 2026-07-30, the primary outcome is locked as share of trading days with an M-Pesa savings deposit, with a minimum effect worth detecting of 10 percentage points; this will not be substituted for a different metric after results are observed.

## Open questions
Whether the mobile money provider's consent process can realistically be completed within the market's normal working hours. Not yet confirmed with the provider.
```
