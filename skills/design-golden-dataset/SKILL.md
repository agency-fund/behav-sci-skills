---
name: design-golden-dataset
description: >-
  Use when an AI product's answers are judged by trying a few questions and
  deciding they seem fine, and the team needs a repeatable test before
  changing the model, prompt, or knowledge base. Also use when someone says
  "we need a test set for our chatbot", "how do we catch regressions", or
  "set up Level 1 evals", or when refusals and safety behavior have only
  ever been noticed in logs. Specifies a "golden dataset": real questions
  with approved answers, the topics they must cover across knowledge,
  implementation, personalization, and stress-test buckets, who writes the
  answers, and how the AI's replies are scored, including how an LLM judge
  is calibrated against humans. It tests the AI's answers, not its effect on
  users. Do not use when the question is whether users learn, decide, or act
  differently; that is Level 3 (choose-ai-eval-level, plan-evaluation-design).
  Not for writing the knowledge base or guardrail policy, and not for
  experiments on users (design-evidential-experiment).
license: CC-BY-4.0
metadata:
  title: Build a test set to check your AI's answers
  type: atomic
  stage: measure
  version: "0.1.0"
  status: draft
  authors: "Joe Speed"
  org: IL
  weird: likely-generalizes
  tags: "ai-eval, golden-dataset, llm-judge"
  consumes: "ai-product-account"
  produces: "golden-dataset-spec"
---

## What it does

Specifies a golden dataset for one AI product: a fixed set of real user questions with approved answers, so changes to the model, prompt, or knowledge base can be checked against it.

The specification defines the topics to cover, where the questions come from, who writes the answers and to what rules, and how the AI's replies are scored. It is the build plan; the team builds the dataset against it. A golden dataset answers "does the model respond well?", which is Level 1 of The Agency Fund's four-level AI evaluation framework. It says nothing about whether anyone acts differently.

## When to use it

### Use it when
- Response quality is currently assessed by someone typing a few test prompts after each change ("vibe checks", the playbook's own term for the practice this replaces as the only method)
- A model swap, system-prompt rewrite, or knowledge-base update is about to ship with no way to detect regressions against the previous version
- `choose-ai-eval-level` has recommended Level 1 evaluation and the team has no gold-standard test set to run
- Safety behavior (refusals, escalations) has never been tested systematically, only noticed anecdotally in logs
- Someone asks "how do we know the new model didn't get worse?" or "we need a test set for our chatbot"

### Do not use it when
- The question is whether users learn, decide, or act differently; that is Level 3, owned by the funnel's proximal-outcome stage (`build-user-funnel`) and `plan-evaluation-design`, with `choose-ai-eval-level` to say when it has been earned
- The team wants the knowledge base or guardrail policy written; the spec references both as inputs to ideal-response authoring, and writing them is upstream content work
- The product has no AI model in the loop; there is nothing for a golden dataset to test, and `plan-evaluation-design` covers the program's outcomes
- The team wants to test a change on users (message variants, timing); that is `design-evidential-experiment`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The product account: what the product does, for whom, in which languages and registers (including code-switching), what its knowledge base covers, and which failures would be harmful rather than merely wrong.
2. **Required.** What users actually ask: access to logged queries, or at least the team's honest account of the most common and the strangest questions. The coverage plan is derived from real traffic; without it the dataset tests the product everyone hopes exists.
3. **Required.** The guardrail spec, or at minimum the list of things the product must refuse. The stress-test bucket cannot be built without it.
4. Optional. Any existing test set, benchmark result, or logged safety incident, so the spec extends rather than duplicates it.
5. Optional. Who on the team or among partners has the domain expertise to author ideal answers, and whether a native speaker of each covered language is available.

If 1 to 3 are missing, ask and stop. If the team has no logs at all, say so and plan a query-sourcing step rather than inventing queries. If 4 and 5 are missing, assume no prior test set exists and write the authoring rules to require a domain-expert role without naming a person.

## What it draws on

- Wu, Z., On, R., Walsh, J., Korley, E., Madon, T., & Wong, L. (2025). AI Evaluation in the Social Sector: A Living Playbook. Level 1: Model Evaluation. The Agency Fund. https://eval.playbook.org.ai/level1
- The Agency Fund (2025). Model evaluation workshop materials, AI4GD Midpoint Sprint, Nairobi, June 2025. taf-ai-eval-playbook repository, public/model-eval-case-study. https://github.com/agency-fund/taf-ai-eval-playbook

Level 1 of The Agency Fund's AI Evaluation Playbook and its Nairobi model-evaluation workshop define golden datasets as "test questions with the correct answers that help you check whether your AI is working properly." The workshop's structure is adopted directly: a golden dataset of query and ideal-response pairs (the workshop's floor is about 40; more for products with broad domains) spanning four buckets. Knowledge covers canonical factual questions. Implementation covers procedural "how do I actually do this" questions. Personalization covers questions whose right answer depends on the user's stated context and constraints. Stress-test covers queries probing brittleness, hallucination under confident-sounding premises, safety, and ethics, including queries the product must refuse per its guardrails.

The scoring plan follows the playbook's three method families and its warning labels. Reference-based automated metrics (semantic similarity, contextual precision against the golden answer) are cheap and run on every change. Rubric-based LLM-as-judge scoring covers criteria with no single correct phrasing, but the workshop is blunt that LLM judges "typically align with humans only ~50% of the time" out of the box, so the spec must include a human-calibration step (paired human scores on a sample, iterate the judge prompt on discrepancies) before judge scores are trusted. Human annotation remains the reference standard the other two are calibrated against.

Judgment call the source does not fully specify: version binding. A golden run is meaningless if nobody knows which model, system prompt, and knowledge-base version produced it, so this skill makes the spec name the configuration fields every run must record, matching the workshop's own config-worksheet practice.

**WEIRD skew:** Unusually for this library, the source material is non-WEIRD in origin: the workshop this skill operationalizes was built in Nairobi for deployments in low- and middle-income countries. The caveat is technical rather than cultural. Reference-based scoring (semantic-similarity metrics against an ideal answer) is least reliable in exactly the low-resource languages and code-switching registers these products serve, so a golden dataset in a Swahili-English mix needs its automated scores calibrated against human judgment before anyone trusts a pass rate.

**Replication status:** Not applicable in the effect sense: a golden dataset is an evaluation procedure, not an intervention. Fixed test sets with reference answers are standard practice in machine-learning evaluation. The four-bucket structure and the mandatory human-calibration step are the Nairobi workshop's, and the figure that uncalibrated LLM judges agree with humans only about half the time is the workshop's own claim rather than an independent finding.

## How to do it

1. **Pin down the product's domain and traffic**: the languages and registers users actually write in, what the knowledge base covers, and which failures are harmful (safety, medical, restricted advice) rather than merely wrong. The dataset must look like real traffic, not textbook prose.
2. **Set version binding.** Name the fields every run records: model id, system-prompt tag, knowledge-base tag. A pass rate with no version attached can detect that something changed but never what.
3. **Plan coverage across all four buckets**: knowledge, implementation, personalization, stress-test. Set a target count per bucket; the workshop's floor is about 40 queries in total, more for broad domains. All four buckets are mandatory. A dataset with no stress-test bucket tests the product everyone hopes exists, not the one users will poke.
4. **Source the queries.** State per bucket how many come from real logs and how many are expert-written. Stress-test queries come from the guardrail spec (every must-refuse rule becomes at least one golden), a red-team session, and logged incidents.
5. **Write the ideal-response authoring rules**: who writes golden answers (a domain-expert role, not the engineer), what they are written against (the knowledge-base version and the guardrail spec), and the form rules. Prefer must-include facts and must-not-include claims over verbatim text, except for refusal goldens, which quote the guardrail's scripted refusal exactly.
6. **Write the scoring plan**, assigning a method family to each bucket. Use reference-based similarity where a canonical answer exists. Use an LLM-judge rubric (criterion and scale) where quality is graded, with the mandatory human-calibration step and its agreement threshold stated. Keep human review for stress-test results; a must-refuse golden should never pass on an automated score alone.
7. **Check similarity thresholds against the languages covered.** Before setting a pass threshold, compare score distributions on code-switched or low-resource-language queries with human ratings, because reference-based metrics degrade off English.
8. **Set refresh triggers**: every knowledge-base update re-runs the full set before deploy, new observed query patterns become candidate goldens on a stated cadence, and every logged safety incident becomes a stress-test golden.

See `references/worked-example.md` for a complete run on a WhatsApp agronomy assistant for smallholder maize farmers.

## Output template

```markdown
# Golden dataset specification

**Product:** <name + one line>
**Languages/registers covered:** <including code-switching if users mix languages; the dataset must look like real traffic, not textbook prose>
**Version binding:** every run records <model id, system-prompt tag, knowledge-base tag> alongside scores.

## Coverage plan
| Bucket | What it tests | Target count | Query sources |
|---|---|---|---|
| Knowledge | canonical factual questions in domain | <n> | <real logs / expert-written / both> |
| Implementation | procedural guidance users actually need | <n> | <...> |
| Personalization | answers that must change with user context | <n> | <...> |
| Stress-test | brittleness, hallucination bait, safety, must-refuse queries | <n> | <guardrail spec + red-team session + logged incidents> |

## Ideal-response authoring rules
<who writes golden answers (domain-expert role, not the engineer), what they are written against (knowledge-base version, guardrail spec), and the form rules, e.g. must-include facts versus verbatim text; refusal goldens quote the guardrail's scripted refusal>

## Scoring plan
<which metric consumes which bucket: reference-based similarity where a canonical answer exists; LLM-judge rubric (criterion, scale) where quality is graded, with the mandatory human-calibration step and its agreement threshold; human review cadence for stress-test results>

## Refresh triggers
<when the dataset must be extended or re-authored: knowledge-base updates, new observed query patterns, every logged safety incident becomes a stress-test golden>
```

## Where it goes wrong

- **The all-softball dataset.** Queries written by the people who built the knowledge base, phrased the way the knowledge base phrases things. Pass rates soar; real farmers, who ask sideways questions in mixed language, hit failures the set never contained. Sourcing counts from real logs are in the template because of this.
- **No must-refuse goldens.** A dataset that only checks what the product should say, never what it must decline, will happily green-light a model swap that quietly stopped refusing restricted-pesticide advice.
- **Trusting the judge uncalibrated.** LLM-judge scores adopted without the human-agreement check. On a roughly 50 percent baseline alignment, that is a coin flip wearing a rubric. The calibration step is not optional overhead; it is the difference between measurement and theater.
- **Similarity scores on code-switched text taken at face value.** Reference-based metrics are weakest in exactly this library's deployment languages; a threshold tuned on English goldens silently fails Swahili-English ones. Check the distribution before setting the threshold.
- **The unversioned run.** "Pass rate dropped to 79 percent", against which model, prompt, and knowledge base? Without version binding the dataset can detect that something changed but never what, which is most of its job.
- **Out of scope: user outcomes.** A perfect golden pass rate says nothing about whether anyone farms differently. That is the funnel's proximal-outcome stage and Level 3 or 4 evaluation; pointing a golden dataset at that question is answering "does the model respond well?" and calling it impact.

## When to bring in a specialist

Tell the user to involve a domain expert, and where relevant a native-speaker reviewer or an evaluation specialist, when:
- The product operates in a safety-critical domain (health, nutrition, pesticides, finance, legal rights); the stress-test and refusal goldens must be authored and reviewed by someone qualified in that domain, not by the product team
- Users write in a low-resource language or heavy code-switching and no one on the team is a native speaker; both the ideal answers and the calibration ratings need one
- The team wants to act on LLM-judge scores for a decision with consequences (a production model swap, a funder report) and the calibration sample shows agreement below the threshold, or the judge disagrees with humans systematically on one bucket
- The golden pass rate is being asked to stand in for user outcomes; an evaluation specialist should reframe the question at Level 3, starting with `choose-ai-eval-level`

Bring them: the product account, the coverage plan with its sourcing counts, the draft authoring rules, and whatever human-versus-judge agreement data exists.
