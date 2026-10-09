# Worked example: MaizeMate, a WhatsApp agronomy assistant

This example continues the MaizeMate running case used across the AI-product skills ported from Joe Speed's prototype. It is illustrative, not a real program. The run below had only the AI product account; no user funnel map was available.

**AI product account (user-supplied, condensed):** "MaizeMate is our WhatsApp AI assistant answering agronomy questions for smallholder maize farmers in western Kenya; the goal is better yields through timely top-dressing. Piloted with about 1,400 farmers via two cooperatives. We benchmarked answers against an agronomist-written test set last quarter (88% rated acceptable); usage is spiky, many farmers ask one question and never return. Our funder wants to discuss an RCT at the October board meeting."

```markdown
# AI evaluation level recommendation

**Product:** MaizeMate, a WhatsApp AI agronomy assistant for smallholder maize farmers in western Kenya
**Development outcome targeted:** improved maize yields via timely top-dressing fertilizer application
**Decision this recommendation informs:** whether to propose an RCT at the October board meeting or a staged alternative

## Level verdicts
| Level | Question | Verdict | Evidence the verdict rests on |
|---|---|---|---|
| 1: Model | Desired responses? | continue/monitor | 88% acceptable on an agronomist-written test set last quarter; no stress-test bucket reported, so safety behavior is unknown |
| 2: Product | Meaningful interactions? | run now | the account's own description: "many farmers ask one question and never return"; engagement is the weak link |
| 3: User | Thoughts, feelings, actions? | premature | no evidence that usage shifts fertilizer knowledge or intent, and it cannot be read until Level 2 stabilizes |
| 4: Impact | Yield improvement? | premature | fails all three of the playbook's gates: Levels 2 and 3 not strong, not preparing to scale, no confident effect priors |

## What to run now
Level 2: an engagement experiment on the one-question drop-off (for example, proactive check-in variants), designed via design-evidential-experiment.
Level 1, continuing: extend the test set with a stress-test bucket (pesticide misuse, out-of-scope medical questions) before any scale-up.

## Why the premature levels are premature
Level 4: an RCT on yields now would measure the impact of a product most enrolled farmers use once. A null would be uninterpretable (product failure versus idea failure), which is exactly the premature-RCT case the framework warns funders against. Level 3: user-outcome measures are worth building (see below) but cannot carry weight while retention is this weak.

## Evaluability-early steps
Hold out one cooperative's next enrollment cohort from proactive-messaging features; tag model and knowledge-base versions in every logged conversation; randomize enrollment timing across the waitlist now so a future Level 4 comparison group exists by design.

## What would change this recommendation
Level 3 → run now: 4-week retention stabilizing after the engagement experiments. Level 4 → run now: strong Level 3 evidence that usage shifts top-dressing knowledge and intent, plus a scale decision actually on the table.
```
