# Worked example: MaizeMate's six-week pilot readout

This example continues the MaizeMate running case used across the AI-product skills ported from Joe Speed's prototype. It is illustrative, not a real program. The inputs were the MaizeMate funnel map (see `build-user-funnel`) and a readout for six weeks of pilot.

**Inputs (condensed):** Readout: recruitment 138 per week (target 120), onboarding 74% (target 70%), engagement 31% (target 60%), 4-week retention 22% of the engaged (target 40%). Caveat noted: the onboarding flow was shortened in week 3.

```markdown
# Funnel weak-link hypotheses

**Funnel:** MaizeMate WhatsApp assistant, yield funnel
**Readout window:** 2026-06-22 to 2026-08-02
**Weakest link:** onboarding to engagement: 31% observed vs 60% target (retention is also below target but is downstream of this break)
**Gaps set aside:** retention (22% vs 40%), deferred until the engagement break is understood, since the retained base is currently the 31% who engaged at all. The week-3 onboarding change does not explain the engagement gap: the rate is flat across cohorts before and after.

## Competing hypotheses
| # | Mechanism | COM-B locus | What would discriminate it | Cheapest honest test |
|---|---|---|---|---|
| H1 | Farmers complete setup, then don't know what to ask; the open "ask me anything" prompt gives no model of a good first question | capability | H1 predicts drop-off concentrates on farmers who never send any draft text; H2 predicts sent-but-unanswered attempts | Log analysis: do non-engagers type nothing, or type and abandon? Then A/B a first-question example menu vs the open prompt |
| H2 | Answers to first questions arrive too slowly or read as generic, so the second question never comes | motivation | Response latency and first-answer length and specificity for engagers vs one-question leavers | Compare first-session transcripts; if separated, A/B a personalized first answer (uses the setup's county and crop stage) vs current |
| H3 | Data cost: farmers onboard on free cooperative Wi-Fi at enrollment events, then face airtime costs for substantive chat from home | opportunity | H3 predicts drop-off concentrates among farmers onboarded at events vs self-onboarded; engagement clusters near market-day Wi-Fi | Cross-tab engagement by enrollment source; 10 farmer calls asking about data spend |

## What this diagnosis is not
No redesign is proposed here. H1 or H2 winners go to design-evidential-experiment as experiment intents; an H3 win is a delivery-model problem no message experiment fixes.
```
