---
name: adjust-for-multiple-comparisons
description: >-
  Use when a trial or evaluation tested more than one outcome, arm, or
  subgroup and someone asks "do we need to correct for multiple testing",
  "which of these results are real", or "the reviewer wants Bonferroni".
  Also use when a team is about to report the two significant results out of
  twelve, or to regroup outcomes after seeing them. Groups the tests into the
  families the pre-analysis plan defined, chooses a summary index,
  family-wise error control, or false discovery rate control by the decision
  at stake, computes the correction, and reports adjusted and unadjusted
  results side by side with any conclusion that changed (Anderson; Benjamini
  and Hochberg; List, Shaikh and Xu). Do not use to decide which subgroups
  to test or to estimate subgroup effects; use analyze-heterogeneous-effects
  instead. Not for the Doer/Non-Doer 15-point rule, a heuristic rather than
  a test (analyze-doer-nondoer-differences), or for writing the plan that
  defines the families (write-pre-analysis-plan).
license: CC-BY-4.0
metadata:
  title: Correct for testing many outcomes at once
  type: atomic
  stage: analyze
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: not-applicable
  tags: "multiple-comparisons, quantitative, experimental-design"
  consumes: "analysis-plan, dataset-description"
  produces: ""
---

## What it does

Applies the multiple-testing correction the pre-analysis plan specified to each family of outcomes, arms, or subgroups, then reports adjusted alongside unadjusted results.

A family is the set of tests across which one false positive would count as the same mistake: all secondary outcomes, all arms against control, all pre-specified moderators. The chance of at least one false positive grows with every test added, so a report that shows only the tests that moved is not evidence. This skill does not choose the families; the plan did. When no plan exists it defines them from the decision at stake, says so at the top, and refuses to regroup after the results are seen.

## When to use it

### Use it when
- A trial reports several outcomes, several arms, or several subgroups and someone asks "do we need to correct for multiple comparisons?", "which of these are real?", or "the reviewer wants a Bonferroni correction"
- The pre-analysis plan named families and a correction method and it is time to apply them to the results
- A team is about to report the two significant results out of twelve, or to drop the outcomes that did not move
- Someone proposes combining related survey outcomes into one index so there are fewer tests
- Subgroup interaction p-values arrive from `analyze-heterogeneous-effects` and need adjusting as a family

### Do not use it when
- The question is which subgroups to test or how large the effect was in each; `analyze-heterogeneous-effects` estimates them and sends the p-values here
- The result is a Doer/Non-Doer gap flagged by the 15-percentage-point rule; that rule is a screening heuristic, not an inferential test, and adjusting it misstates what it is (`analyze-doer-nondoer-differences`)
- The families and the method are still being chosen before the data exist; `write-pre-analysis-plan` is where they are set, and this skill reads them from there
- The team wants posterior probabilities or hierarchical shrinkage across outcomes instead of error-rate control; that is a Bayesian analysis, a different procedure from the frequentist one here, so ask for one directly

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The pre-analysis plan's families and the correction method named for each (index, family-wise, or false discovery rate). If no plan exists, or it is silent on families, say so and ask what decision each set of results will feed, so families can be defined from the decision before any number is read.
2. **Required.** The test results: for each test, the family it belongs to, the estimate, and the unadjusted p-value; or the dataset description if the tests are still to be run, in which case the plan's models are run first, as specified.
3. **Required.** The decision each family feeds: a funding, scale-up, or published claim where one false positive is costly, or a next-trial choice where a false lead costs less than a missed one.
4. Optional. The correlation among the outcomes in a family, or the raw data, which lets a joint procedure such as List, Shaikh, and Xu's be less conservative than Bonferroni.

If 1 is missing, ask once; if there is no plan, proceed with families defined from the decision, marked "defined post hoc, before results were read" at the top of the output. If 2 is missing, ask and stop. If 3 is missing, assume one false positive is costly and use family-wise control. If 4 is missing, use Benjamini-Hochberg or Bonferroni from `scripts/bh_adjust.py`.

## What it draws on

- Anderson, M. L. (2008). Multiple inference and gender differences in the effects of early intervention: A reevaluation of the Abecedarian, Perry Preschool, and Early Training Projects. *Journal of the American Statistical Association*, 103(484), 1481–1495. https://doi.org/10.1198/016214508000000841
- Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B*, 57(1), 289–300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x
- List, J. A., Shaikh, A. M., & Xu, Y. (2019). Multiple hypothesis testing in experimental economics. *Experimental Economics*, 22(4), 773–793. https://doi.org/10.1007/s10683-018-09597-5
- EGAP. *10 Things to Know About Multiple Comparisons*. https://egap.org/resource/10-things-to-know-about-multiple-comparisons/ (listing confirmed; the guide itself was not opened for the evidence dossier)

Anderson re-analyzed three early-childhood programs and made two moves this skill copies: group related outcomes into a summary index (each outcome standardized against the control group, oriented so higher is better, averaged with weights that count a redundant outcome less), which replaces many tests with one; and control the family-wise error rate for the tests that remain. The family-wise error rate (FWER) is the probability of at least one false positive across a family; Bonferroni controls it by multiplying each p-value by the number of tests, which is safe but conservative when the tests are correlated. The false discovery rate (FDR) is the expected share of the results called significant that are false; Benjamini and Hochberg's step-up procedure controls it and reports a q-value, the smallest FDR at which that test would count as a discovery. List, Shaikh, and Xu give an FWER procedure for experiments with several treatments, outcomes, and subgroups at once that uses the correlation among the tests to reject more than Bonferroni would. When each fits: FWER when any single false positive is costly, as when one result decides funding or becomes a headline claim; FDR when the results feed exploration, as when choosing which outcomes to carry into the next trial. The judgment calls this skill adds: families come from the plan or from the decision, never from the results; both adjusted and unadjusted numbers are always shown; and any result whose conclusion changes is flagged rather than quietly dropped. The dossier's own note is that FWER versus FDR is a judgment call, so the output states the reason for each choice. See `references/evidence-notes.md`.

**WEIRD skew:** Not applicable: the procedures are statistical and do not depend on the population. Anderson's re-analysis uses three US early-childhood programs; the methods are standard in development RCTs. **Non-WEIRD evidence:** none found in the sources this skill draws on; the evidence dossier records the methods as standard in development RCTs without citing a specific study.

**Replication status:** Not applicable in the effect sense: these are error-control procedures with proofs, not effects. What is contested is the choice between FWER and FDR for a given decision, which is why the output records the reason for each family's choice.

## How to do it

1. **Copy the families from the plan verbatim,** with the method named for each. If the plan is silent, define each family from the decision it feeds, write "defined post hoc, before results were read" at the top, and keep that line in every later version of the report.
2. **For each family choose one of three:** a summary index when the outcomes measure one construct and the question is whether the construct moved; FWER when one false positive is costly; FDR when the family feeds exploration. Write the reason in the family table.
3. **Build any index as Anderson does:** standardize each outcome to the control group's mean and standard deviation, orient so higher is better, average with inverse-covariance weights so a redundant outcome counts less (equal weights if the covariance is not available, and say so). Test the index once.
4. **Compute the corrections.** Run `scripts/bh_adjust.py` with the family's p-values for Benjamini-Hochberg q-values and Bonferroni-adjusted p-values (`--help` lists the options; `--self-test` checks the known cases). For a joint FWER procedure that uses the correlation among tests, use List, Shaikh, and Xu's method (their Stata command is mhtexp) on the raw data.
5. **Report adjusted and unadjusted side by side,** with the family name, m (the number of tests), the method, and the threshold. Never show only the adjusted column: a reader needs to see what changed.
6. **Flag every result whose conclusion changes after adjustment** in its own section, in plain words: "balance at day 90 was significant unadjusted (p = 0.045) and is not after the correction (q = 0.06)". A primary outcome is its own family of one and is not adjusted unless the plan said otherwise.
7. **Refuse to regroup after the fact.** If asked to move an outcome between families, split a family, or drop a test once results are known, record the request under "Requests refused" and keep the original grouping.
8. **Stop here.** Why an effect appeared or vanished is for the trial write-up; what to carry into the next trial goes to `write-pre-analysis-plan`.

See `references/worked-example.md` for a complete run on a Kenyan market-vendor savings trial.

## Output template

```markdown
# Multiple-comparisons report

**Trial:** <name; arms; randomization unit; sample per arm>
**Plan:** <pre-analysis plan dated <date>, families as written / no plan: families defined post hoc, before results were read>
**Primary outcome:** <outcome; estimate (95% CI); p; one test, not adjusted unless the plan said so>

## Families
| Family | Tests (m) | Decision it feeds | Method chosen | Reason |
|---|---|---|---|---|
| <name> | <n> | <funding call / next-trial choice / claim in a report> | <index / FWER (Bonferroni or List-Shaikh-Xu) / FDR (Benjamini-Hochberg)> | <one clause> |

## Results by family
### <Family name> (m = <n>; method <...>; threshold <alpha>)
| Test | Estimate (units, 95% CI) | Unadjusted p | Adjusted p or q | Conclusion before | Conclusion after |
|---|---|---|---|---|---|
| <outcome or subgroup> | <...> | <...> | <...> | <significant / not> | <significant / not> |

<for an index family: the index definition, its components, the weights, and its one test>

## Conclusions that changed after adjustment
- <test>: <unadjusted conclusion> became <adjusted conclusion> (<p> to <adjusted value>); <what this means for the decision it feeds>
<or "None.">

## Requests refused
- <any request to regroup, split, or drop a test after results were seen, with the date>
<or "None.">

## What to check before relying on this
- <that the families match the plan word for word, or that the post hoc line is present>
- <that the method for each family matches the decision stated>
- <for an index: that every component is oriented the same way>
```

## Where it goes wrong

- **Families drawn after the results are in.** Grouping the outcomes that moved into one family and the rest into another is the error the correction exists to prevent, done one level up. Families come from the plan or from the decision, written down before the results are read.
- **Showing only the adjusted column.** A report with adjusted p-values alone hides what changed; one with unadjusted alone hides that twelve tests were run. Both columns, every time.
- **Bonferroni on forty correlated tests.** Bonferroni treats every test as independent; across many correlated outcomes it rejects almost nothing, and the team concludes "no effect" when it should conclude "wrong tool". Use an index, a joint procedure, or FDR, by the decision.
- **Adjusting the primary outcome away.** The primary outcome is one test in its own family. Folding it into the secondary family and then reporting it as "not significant after adjustment" misreads the plan.
- **Correcting a heuristic.** The Doer/Non-Doer 15-point screen is not a hypothesis test; applying Bonferroni to it produces a number that means nothing. Say what the rule is instead.
- **Quietly dropping a result that lost significance.** The flag section exists so that a result which changes conclusion is written down in plain words, not removed from the table.

## When to bring in a specialist

Tell the user to consult a statistician or an econometrician with trial experience when:
- The number of families or outcomes was not pre-specified and the result will decide funding, scale-up, or a published claim; post hoc families need an independent reader
- The tests are many and correlated (several arms crossed with several outcomes) and the plan calls for family-wise control; the joint procedure needs the raw data and someone who has run it
- A primary outcome's conclusion changes after a correction the plan did not name, or the plan and the funder's reporting template disagree about what the primary outcome is
- Outcomes are to be combined into an index and some components are missing for part of the sample

Bring them: the pre-analysis plan, the family table with reasons, the full results table with both columns, and the "Requests refused" list.
