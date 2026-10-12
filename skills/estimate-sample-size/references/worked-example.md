# Worked example: village-randomized sanitation triggering in Indonesia

The program, its baseline, the ICC range, the attrition and covariate assumptions, and the feasible sample are illustrative. The arithmetic is the script's output for those inputs; it is not a finding about any real sanitation program.

**User's answers to Before you start.** Effect to plan for: 6 percentage points, the smallest effect worth detecting from `estimate-expected-effect` (central expected effect 8 points). Outcome: household uses an improved latrine at 12 months, binary, survey-verified; baseline 35% (illustrative, district health office data). Design from `choose-trial-design`: village-randomized, two arms, equal allocation, 40 households surveyed per village. ICC: no local estimate; 0.05 used as the central assumption with 0.01–0.20 in the sensitivity table. Take-up: triggering is delivered to every assigned village (village-level take-up 1.0, control 0). Attrition: 10% of households not found at endline. Covariates: baseline latrine ownership, R² about 0.10. Feasible: 60 villages (30 per arm). Alpha and power not fixed by a protocol.

```markdown
# Power calculation: CLTS triggering, East Nusa Tenggara district (illustrative)

**Design:** cluster randomized at the village, two arms, 1:1, 40 households per village, from choose-trial-design
**Effect planned for:** 6 percentage points; the smallest effect worth detecting, from estimate-expected-effect (central expected effect 8 points)

## Inputs
| Input | Value | Source |
|---|---|---|
| Alpha (two-sided) | 0.05 | convention |
| Power | 0.80 | convention |
| Outcome type, baseline | binary, p0 = 0.35 | district health office data (illustrative) |
| Cluster size m | 40 households | survey plan |
| ICC | no local estimate; 0.05 central, 0.01–0.20 range | assumption |
| Take-up (treatment, control) | 1.0, 0 | village-level delivery |
| Attrition | 0.10 | program's previous endline (illustrative) |
| Covariate R² | 0.10 | baseline latrine ownership (assumption) |

## Calculation
- Individual-level n per arm: (1.960 × sqrt(2 × 0.38 × 0.62) + 0.842 × sqrt(0.35 × 0.65 + 0.41 × 0.59))² / 0.06² = 1026.2
- Design effect: 1 + (40 − 1) × 0.05 = 2.95
- Take-up: ÷ 1.0²; attrition: ÷ (1 − 0.10); covariates: × (1 − 0.10)
- **Required:** 3,028 households enrolled per arm; 76 villages per arm × 40 (152 villages in total)
- Script: `python scripts/power_calc.py --outcome binary --p0 0.35 --p1 0.41 --icc 0.05 --cluster-size 40 --attrition 0.10 --r2 0.10 --clusters-per-arm 30 --sensitivity --true-effect 0.06`

## Minimum detectable effect for the feasible sample
30 villages per arm (1,200 households enrolled per arm): MDES = 9.6 points (0.20 SD of the baseline outcome), against a planned effect of 6 points

## Sensitivity
| ICC \ effect | 3.0 pp | 4.5 pp | 6.0 pp | 9.0 pp |
|---|---|---|---|---|
| 0.01 | 141 | 63 | 36 | 17 |
| 0.05 | 299 | 134 | 76 | 35 |
| 0.10 | 496 | 222 | 126 | 57 |
| 0.20 | 890 | 399 | 226 | 102 |
(villages per arm; MDES for 30 per arm by ICC: 0.01: 6.5 pp; 0.05: 9.6 pp; 0.10: 12.4 pp; 0.20: 16.7 pp)

## Type S and Type M risk (when the expected effect is below the MDES)
At a true effect of 6 points: power 0.42; P(wrong sign | significant) 0.000; exaggeration ratio 1.52. At the central expected effect of 8 points: power 0.65; exaggeration ratio 1.24. A significant result from this design would overstate a true 6-point effect by about half.

## Verdict
Cannot detect the plausible effect with 60 villages: at ICC 0.05 the design needs 152 villages for 6 points, and 60 villages detect 9.6 points. Options that change it: fund 152 villages at 40 households (the honest cost of a 6-point test); add villages rather than households, since 50 villages per arm at 20 households still only reach an MDES of 8.5 points; collect a fuller baseline to raise R² above 0.10; accept that 60 villages can only confirm an effect of about 10 points or more and say so in the pre-registration; or do not run the effect test and run a feasibility study instead.

## What to check before relying on this
- The ICC: a baseline survey of latrine use in 20 villages would replace the 0.01–0.20 range with an estimate, and the answer moves by a factor of six across that range
- The 35% baseline, which comes from administrative data that may overstate use relative to a verified survey
- Endline attrition of 10%, taken from a previous round in a different district
```
