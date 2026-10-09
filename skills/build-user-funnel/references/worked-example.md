# Worked example: MaizeMate, a WhatsApp agronomy assistant

This example continues the MaizeMate running case used across the AI-product skills ported from Joe Speed's prototype. It is illustrative, not a real program. The run below had only the AI product account; no audience and context brief was available.

**AI product account (user-supplied, condensed):** "MaizeMate, our WhatsApp AI agronomy assistant for smallholder maize farmers in western Kenya; the goal is better yields through timely top-dressing. Farmers hear about it from cooperative SMS blasts and local radio; they message it questions and it answers from our agronomy knowledge base."

```markdown
# User funnel map

**Product:** MaizeMate, a WhatsApp AI agronomy assistant
**Development outcome (Level 4):** improved maize yield via top-dressing applied at the correct growth stage
**Instrumentation reality check:** stages 1 to 4 from WhatsApp message logs; stage 5 requires an in-chat micro-survey that does not exist yet; stage 6 requires cooperative harvest records (access unconfirmed).

## Stages
| # | Stage | User action that counts as entry | Confirming metric | Target | Owner |
|---|---|---|---|---|---|
| 1 | Recruitment | Farmer sends any first message | new unique senders per week | 120/week (provisional) | Outreach lead |
| 2 | Onboarding | Farmer completes the 3-question setup (county, crop stage, plot size) | setup completion rate | 70% of new senders | Product lead |
| 3 | Engagement | Farmer asks a substantive agronomy question | at least 1 substantive question per week | 60% of onboarded (provisional) | Product lead |
| 4 | Retention | Farmer returns in a later calendar week | 4-week return rate | 40% (provisional) | Product lead |
| 5 | Proximal outcome | Farmer correctly identifies their plot's top-dressing window | in-chat 2-item check, both correct | 50% of retained (provisional) | Research lead |
| 6 | Development outcome | Season yield on registered plot | cooperative harvest records, kg/acre vs county baseline | +10% (provisional; sponsor threshold unconfirmed) | Research lead |

## Level 1 monitoring underneath the funnel
Weekly golden-set pass rate on the current model and knowledge-base version; guardrail-refusal log reviewed for pesticide-safety and out-of-scope medical queries. Version tags on every conversation.

## Assumptions this funnel makes
- One WhatsApp number is one farmer (shared handsets would inflate stage 1 and corrupt stage 4); check against cooperative rosters.
- Farmers will answer an in-chat quiz (the stage 5 metric) at meaningful rates; unvalidated.
- Cooperatives will share plot-level harvest records; unconfirmed with either cooperative.
```
