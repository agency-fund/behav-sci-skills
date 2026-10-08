---
name: besci-eval
description: >-
  Use when someone wants to check how good a skill in the Behavioral
  Science Skills Library is: validate its structure, test whether it fires
  on the right requests and stays quiet on the wrong ones, grade its outputs
  against its own template, compare it across models, or re-test it after a
  new model is released. Trigger on "evaluate this skill", "test my skill",
  "does this skill trigger correctly", "run the evals", "regression test",
  "compare models on this skill", "is this skill still good on the new
  model". Do not use for writing or revising a skill's content
  (besci-skill-creator), for choosing which skill to use (besci-navigator),
  or for evaluating an AI product or chatbot (that is The Agency Fund's
  evaluation playbook, a different thing).
license: CC-BY-4.0
metadata:
  title: Behavioral science skill evaluator
  type: meta
  stage: other
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: not-applicable
  tags: "meta, evaluation, regression"
  consumes: "skill-draft"
  produces: "eval-report"
---

## What it does

Runs three checks on one library skill: structure, triggering, output quality.

The result is a report an author or maintainer can act on.

The checks are **structure** (does the folder meet the spec), **triggering** (does the description fire on the right requests and not on adjacent ones), and **output quality** (do the skill's own test cases produce outputs that match its template, ask its questions, cite its evidence, and escalate when they should). The rubric comes from the skill's own sections, so every skill in the library is gradable without anyone writing a rubric by hand. In Claude Code the same checks run through the API across several models.

## When to use it

### Use it when
- "Evaluate my skill before I submit it"
- "Run the evals for decompose-comb-barriers"
- "Does this skill trigger on the right prompts? I think it over-fires."
- "A new Claude model came out; which of our skills got worse?"
- "Compare this skill on Opus and Sonnet"
- "Grade these three outputs against the skill's template"
- A maintainer reviewing a pull request wants an independent read of the evals

### Do not use it when
- The author wants to change the skill's content, add sections, or rewrite the description; use besci-skill-creator, then come back
- The user wants to know which skill to use for their problem; use besci-navigator
- The user wants to evaluate an AI chatbot, product, or program outcome; that is The Agency Fund's four-level evaluation framework at https://eval.playbook.org.ai/, not skill evaluation
- The skill is not a library skill (no eight sections, no evals.json); run the structural check only and say the rest does not apply

## Before you start

Ask these one at a time unless already answered.

1. **Required.** Which skill? A path to the folder, an uploaded `.skill` file, or pasted files. The folder must contain `SKILL.md` and `evals/evals.json`.
2. **Required.** Which checks: structure, triggering, output quality, or all three? Default to all three.
3. **Required.** Environment. Code execution with a filesystem and an API key means the script path (Claude Code, or a sandbox with `ANTHROPIC_API_KEY`). Otherwise the checks run inside this conversation, qualitatively, on the current model only.
4. Optional. Models to compare, if the script path is available. Default is the current flagship; add a second model to compare.
5. Optional. A baseline: compare against the skill's previous version, or against no skill at all? Default: no baseline for a first run; previous version when re-testing after a change.
6. Optional. Which other skills are installed alongside it? Triggering is judged relative to neighbors, so the catalog snapshot is used by default.

If the skill has fewer than three evals, stop and send the author to besci-skill-creator; there is nothing to grade.

## What it draws on

- The library's skill specification (`docs/skill-spec.md` in the repository) and its validator, bundled as `scripts/besci_validate.py`. Structure is whatever the validator says it is.
- Anthropic's skill-creator evaluation approach: run each test prompt with the skill, optionally against a baseline, and grade with explicit assertions; aggregate across runs because single runs vary.
- Standard information-retrieval measures for triggering: precision (of the times it fired, how often it should have) and recall (of the times it should have fired, how often it did), computed over the should-fire and should-not-fire phrasings in the skill's "When to use it" section.
- The grading rubric in `references/rubric.md`, derived from the eight sections every library skill has.
- The partnership's intent that skills be re-testable when models change, so that a skill is a versioned artifact whose behavior is known, not a prompt that silently drifts.

**WEIRD skew:** Not applicable to the evaluator. The rubric checks whether a skill surfaces its own WEIRD status when relevant.

**Replication status:** Not applicable; this is a procedure. Single runs of a language model vary, which is why the script repeats each case and reports spread.

## How to do it

**Check 1: Structure.** With a filesystem, run `python scripts/besci_validate.py <skill-folder>` from this skill's folder and include the report verbatim. Without one, walk `references/checklist.md` and report pass or fail per item. Errors here stop the evaluation; warnings are noted and the evaluation continues.

**Check 2: Triggering.** Take every bullet under "Use it when" (should fire) and "Do not use it when" (should not fire) from `SKILL.md`, plus the prompts in `evals.json` (should fire unless the case says otherwise). For each phrasing, judge as a fresh model would: given only this skill's `description` and the descriptions of the other skills in the catalog snapshot, would you load this skill for this request? Record yes or no with a one-line reason. Compute precision and recall. List every miss and every false alarm with the phrase and the clause in the description that caused it. Suggest the smallest edit to the description that fixes the worst miss, but do not apply it; that is the author's call via besci-skill-creator.

**Check 3: Output quality.** For each case in `evals.json`, act as a fresh user sending that prompt to a model that has only this skill, produce the full response, then grade it with `references/rubric.md`: eight criteria, each scored 0, 1, or 2, with a one-line justification quoting the output. Compare against the case's `expected_output` and say whether the shape matched. Flag any invented citation, any output produced when the skill should have asked first, and any missed escalation as blocking. Where the script path is available, run each case three times per model and report the median and range; where it is not, run once and say so.

**Script path.** `python scripts/run_evals.py <skill-folder> --models claude-opus-5-5 claude-sonnet-5-5 --runs 3` runs checks 2 and 3 through the Claude API, grades with the rubric using a judge model, and writes `<skill>-workspace/eval-<date>/report.md` and `results.json`. Add `--baseline <path-to-old-skill-folder>` to compare versions. The script needs `ANTHROPIC_API_KEY` or an `ant auth login` profile and the `anthropic` package. Estimate cost before running: cases × models × runs × roughly two calls.

**Reporting.** Fill the output template. Lead with the verdict: ready to submit, fix first, or not gradable. Keep the author's next action to one line per finding.

## Output template

```markdown
# Evaluation: <skill-name> v<version>  (<date>, <model(s)>, <n runs per case>)

**Verdict:** <ready to submit / fix first / not gradable>
**Why:** <one sentence>

## 1. Structure
<validator report or checklist result>

## 2. Triggering
Precision <p> (n fired correctly / n fired), recall <r> (n fired / n should fire)
| Phrase | Should fire | Fired | Reason |
|---|---|---|---|
Misses and false alarms: <list, each with the description clause responsible>
Smallest fix: <proposed description edit, not applied>

## 3. Output quality
| Case | Asked first | Template | Evidence | Mechanism | Escalation | Plain language | No invention | Matches expected | Total /16 |
|---|---|---|---|---|---|---|---|---|---|
Blocking findings: <invented citation, output without asking, missed escalation>
Representative excerpt: <the single most telling quote from an output>

## 4. Model comparison  (script path only)
| Model | Trigger P/R | Quality median (range) | Notes |
|---|---|---|---|

## Next actions for the author
1. <one line>
2. <one line>
```

## Where it goes wrong

- **Grading the skill's own vocabulary.** Evals written in the skill's language pass trivially. Note when `evals.json` prompts read like the skill rather than like users, and suggest rewriting them.
- **One run as truth.** Model outputs vary. Without repetition, report findings as indicative and say so.
- **Judging triggering in a vacuum.** A description that fires correctly alone can over-fire next to neighbors. Always judge against the catalog's other descriptions.
- **Rewriting the skill.** The evaluator reports; the author decides. Proposed edits are proposals.
- **Treating "fix first" as failure.** Most first drafts land there. Say what to fix, in order.
- **Confusing skill evaluation with program evaluation.** Nothing here measures whether an intervention worked.
- Out of scope: evaluating workflows, evaluating non-library skills beyond structure, expert ratings (planned for a later phase).

## When to bring in a specialist

Tell the author or maintainer to involve a domain specialist when:
- Output-quality grading finds that two runs give substantively different method advice, since the evaluator can judge shape but not which advice is right.
- The skill's evidence base cannot be verified from the cited sources during grading.
- The skill touches clinical, safety, or child-protection content; the rubric's escalation criterion is necessary but not sufficient there.
- A model comparison shows a quality drop on the new model and the author cannot tell whether the skill or the model is at fault.

Bring them: the report, the two most different outputs for the same case, and the skill's "What it draws on" section.
