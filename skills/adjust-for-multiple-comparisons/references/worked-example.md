# Worked example: three families in a Nairobi market-vendor savings trial

Setting: an illustrative individually randomized trial ("Akiba Lock", Gikomba and Toi markets, Nairobi) of a savings-lock reminder for 1,180 female stall vendors (590 per arm), continuing the running case used across this library. The pre-analysis plan, dated 2026-02-10, defines three families and a method for each. The funder decides on scale-up from this report. All numbers are illustrative, not findings.

**Inputs the user gave.** The plan's families and methods, the results for every test with its unadjusted p-value, and the decision each family feeds. The q-values below come from `scripts/bh_adjust.py 0.004 0.012 0.045 0.41`; the Bonferroni values from `scripts/bh_adjust.py 0.02 0.60 0.09`.

```markdown
# Multiple-comparisons report

**Trial:** Akiba Lock; savings-lock reminder vs control; randomized by vendor; 590 per arm
**Plan:** Pre-analysis plan dated 2026-02-10, families as written
**Primary outcome:** Any savings-lock deposit within 30 days; +8.2 percentage points (95% CI 2.1 to 14.3); p = 0.009; one test, not adjusted

## Families
| Family | Tests (m) | Decision it feeds | Method chosen | Reason |
|---|---|---|---|---|
| A. Primary outcome | 1 | Scale-up decision | None (family of one) | The plan names one primary outcome |
| B. Secondary savings outcomes | 4 (plus one index test) | Which outcomes to carry into the next trial | Index (Anderson) plus FDR (Benjamini-Hochberg, 5%) | The outcomes measure one construct; a false lead here costs less than a missed one |
| C. Pre-specified moderators | 3 | Claims in the funder report | FWER (Bonferroni, 5%) | One false subgroup claim in a funder report is costly; the plan named Bonferroni |

## Results by family
### B. Secondary savings outcomes (m = 4; method Benjamini-Hochberg; threshold 0.05)
| Test | Estimate (units, 95% CI) | Unadjusted p | Adjusted q | Conclusion before | Conclusion after |
|---|---|---|---|---|---|
| Deposit count, 90 days | +1.9 deposits (0.6 to 3.2) | 0.004 | 0.016 | Significant | Significant |
| Days to first deposit | -4.1 days (-7.3 to -0.9) | 0.012 | 0.024 | Significant | Significant |
| Balance at day 90 | +KES 640 (15 to 1,265) | 0.045 | 0.06 | Significant | Not significant |
| Withdrawal count, 90 days | -0.3 withdrawals (-1.0 to 0.4) | 0.41 | 0.41 | Not significant | Not significant |

Index: the four outcomes standardized to the control mean and standard deviation, withdrawal count and days to first deposit reversed so higher is better, averaged with inverse-covariance weights. Index effect +0.14 SD (95% CI 0.04 to 0.24), p = 0.006, one test, not adjusted.

### C. Pre-specified moderators (m = 3; method Bonferroni; threshold 0.05)
| Test | Estimate (units, 95% CI) | Unadjusted p | Adjusted p | Conclusion before | Conclusion after |
|---|---|---|---|---|---|
| Sex (women minus men) | +9.0 points (1.4 to 16.6) | 0.02 | 0.06 | Significant | Not significant |
| Market (Toi minus Gikomba) | +1.8 points (-5.0 to 8.6) | 0.60 | 1.0 | Not significant | Not significant |
| Chama member minus non-member | +6.2 points (-1.0 to 13.4) | 0.09 | 0.27 | Not significant | Not significant |

## Conclusions that changed after adjustment
- Balance at day 90: significant unadjusted (p = 0.045) became not significant (q = 0.06). For the next-trial choice this means the balance outcome is a weaker lead than deposit count or days to first deposit, not that balances did not move; the index, which it feeds, held.
- Sex moderator: significant unadjusted (p = 0.02) became not significant (adjusted p = 0.06). The funder report cannot claim the reminder worked better for women; the direction can be reported as a hypothesis for the next plan.

## Requests refused
- None.

## What to check before relying on this
- That the three families match the plan dated 2026-02-10 word for word; this run copied them from the user's summary, not from the registered document.
- That family C's method matches the decision stated: Bonferroni was named in the plan for claims in a funder report; a joint procedure on the raw data would be less conservative and is allowed only if the plan permits it.
- That every index component is oriented so higher is better; two were reversed here.
```

**Where this run stopped.** It did not estimate what the effect was within each subgroup (`analyze-heterogeneous-effects` did that and sent the p-values), did not say why balances moved less than deposits (the trial write-up), and did not rewrite the families for the next trial (`write-pre-analysis-plan`). Had the user asked to move balance at day 90 out of family B so it would stay significant, that request would have gone under "Requests refused" with the date.
