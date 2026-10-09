# Worked example: a golden dataset for MaizeMate

This example continues the MaizeMate running case used across the AI-evaluation skills ported from Joe Speed's prototype: a WhatsApp AI agronomy assistant for smallholder maize farmers in western Kenya. It is illustrative, not a real program.

**AI product account (user-supplied, condensed):** "MaizeMate answers agronomy questions for smallholder maize farmers in western Kenya over WhatsApp, mostly in a Swahili-English mix, some Luhya. The knowledge base covers maize varieties, planting windows, top-dressing, and common pests. It must refuse to advise on restricted pesticides and anything medical. We benchmarked once against an agronomist's test set, but it has no stress-test questions and we've never re-run it."

```markdown
# Golden dataset specification

**Product:** MaizeMate, a WhatsApp AI agronomy assistant
**Languages/registers covered:** Swahili-English code-switched (the majority of logged traffic), plain Swahili, plain English; 10 Luhya queries to size the gap rather than pretend coverage.
**Version binding:** every run records model id, system-prompt tag, knowledge-base tag.

## Coverage plan
| Bucket | What it tests | Target count | Query sources |
|---|---|---|---|
| Knowledge | variety selection, planting windows, fertilizer types | 15 | 10 from pilot logs, 5 agronomist-written |
| Implementation | "how much CAN per acre", top-dressing timing steps | 15 | 12 from logs (the most common real questions), 3 written |
| Personalization | the same question with different county, rainfall, or crop stage from setup data | 10 | written from 5 real user profiles, 2 variants each |
| Stress-test | banned-pesticide requests, confident wrong premises ("my maize has rust so I should double-spray, right?"), medical spillover, prompt-injection attempts | 12 | guardrail spec (6 must-refuse), red-team hour (4), 2 logged incidents |

## Ideal-response authoring rules
Golden answers are written by the partner agronomist against knowledge-base tag kb-2026-08; engineers may not author agronomy content. Answers list must-include facts and must-not-include claims rather than verbatim text, except refusal goldens, which quote the guardrail's scripted refusal exactly, ending after the single refusal sentence.

## Scoring plan
Knowledge and implementation: semantic similarity against the golden answer, with the pass threshold set only after checking score distributions on code-switched queries against human ratings (reference-based metrics degrade off English). Personalization: LLM-judge rubric "uses the farmer's stated county and crop stage correctly" (0 to 3), calibrated on 30 human-scored pairs; the judge is adopted only at 80 percent agreement or better. Stress-test: automated refusal-match plus mandatory human review of every response; no automated pass.

## Refresh triggers
Every knowledge-base update re-runs the full set before deploy; each month's top five new query patterns become candidate goldens; every safety incident in the logs becomes a stress-test golden within a week.
```
