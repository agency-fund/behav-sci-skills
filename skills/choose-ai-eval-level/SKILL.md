---
name: choose-ai-eval-level
description: >-
  Use when a team with an AI product for a social cause must decide which
  evaluation to run next, especially when a funder wants proof of impact or
  someone proposes jumping straight to a randomized controlled trial. Also
  use when the candidate evaluations span very different costs (another
  benchmark run, an A/B test, a psychometric survey, a full RCT) or when
  someone asks "are we ready for an RCT?" Recommends which of The Agency
  Fund's four evaluation levels (the AI model, the product, user behavior,
  real-world impact) the product has earned now, which are premature and
  why, and what to set up now so later evaluation stays possible. Do not use
  to design the recommended evaluation itself; hand a Level 2 or 3
  experiment to design-evidential-experiment and an outcome measurement
  plan to plan-evaluation-design. Not for programs with no AI model in the
  loop; start those at plan-evaluation-design.
license: CC-BY-4.0
metadata:
  title: Choose which AI evaluations to run next
  type: atomic
  stage: test
  version: "0.1.0"
  status: draft
  authors: "Joe Speed"
  org: IL
  weird: likely-generalizes
  tags: "ai-eval, evaluation-framework"
  consumes: "ai-product-account, user-funnel-map"
  produces: "ai-eval-level-recommendation"
---

## What it does

Recommends which evaluations an AI product is ready for, based on what it has already shown.

It uses The Agency Fund's four evaluation levels: the AI model, the product, user behavior, and real-world impact. For each level it says whether to run it now or why it is too early, citing the evidence the verdict rests on, and it lists what to set up now so later evaluation stays possible.

## When to use it

### Use it when
- A team is deciding where the next unit of evaluation effort goes and the candidates span very different costs: another benchmark run, an A/B test, a psychometric survey, a full RCT
- A funder or board is requesting impact evidence and the team needs a defensible, framework-grounded account of what evidence the product's stage can support; the playbook's own recommendation is that funders "match evaluation requirements to the product's development stage, avoiding premature requests for impact evaluations"
- An AI product has strong engagement numbers and someone proposes jumping straight to an RCT with no Level 3 evidence that usage shifts what users think, feel, or do
- Someone asks "are we ready for an RCT?", "what should we evaluate next?", or "what evidence can we honestly show the funder?"

### Do not use it when
- The question is how to design the recommended evaluation; hand a Level 2 or 3 experiment to `design-evidential-experiment` and a Level 3 or 4 measurement plan to `plan-evaluation-design`
- The program has no AI model in the loop; the four levels assume a model whose behavior needs evaluating separately from the product around it. Start a non-AI intervention at `plan-evaluation-design`
- The team wants a Level 1 test set built; that is `design-golden-dataset`
- The decision is whether the product should scale; this skill sequences evidence, it does not make the scale decision

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The AI product account: what the product does and for whom, the development outcome it ultimately targets, its current maturity (prototype, piloted, deployed, scaling), and what evaluation evidence already exists at each level. Honest gaps in, useful recommendation out; a flattering account produces a premature one.
2. **Required.** The decision this recommendation informs: what the team will do differently depending on the answer (propose an RCT at a board meeting, choose between two evaluation budgets). Often it is in the account already.
3. Optional. A user funnel map from `build-user-funnel`. With it, Level 2 evidence ("engaging users as intended") becomes checkable against named stages instead of taken on the team's word.
4. Optional. Any external pressure on the choice (a funder's request, a deadline), so the "why premature" section can answer it directly.

If 1 or 2 is missing, ask and stop. If 3 is missing, proceed, and in the Level 2 row say plainly what the verdict rests on; "founder's impression" is a legitimate, flag-raising thing to write. If 4 is missing, assume none.

## What it draws on

- Wu, Z., On, R., Walsh, J., Korley, E., Madon, T., & Wong, L. (2025). AI Evaluation in the Social Sector: A Living Playbook. The Agency Fund. Living document, Apache-2.0. https://eval.playbook.org.ai/
- Chia, H. S., Carter, S., Abrol, F., Madon, T., On, R., Walsh, J., & Wu, Z. (2025). An AI Evaluation Framework for the Development Sector. The Agency Fund, Center for Global Development, and J-PAL. https://www.cgdev.org/blog/ai-evaluation-framework-for-the-development-sector

The Agency Fund's playbook (Wu et al., 2025; announced jointly with CGD and J-PAL in Chia et al., 2025) defines four incremental evaluation levels, each with broadening scope: **Level 1, model evaluation** ("Does the AI model produce the desired responses?"), **Level 2, product evaluation** ("Does the product facilitate meaningful interactions?"), **Level 3, user evaluation** ("Does the product positively support users' thoughts, feelings, and actions?"), and **Level 4, impact evaluation** ("Does the product improve development outcomes?"). The framework's central discipline, which this skill operationalizes, is stage-matching: Level 1 is cheap and continuous from day one; Level 2 requires a deployed product with real users; Level 3 requires Levels 1 and 2 to be working; Level 4 is warranted only when Levels 1 to 3 are strong, the team is preparing to scale, and priors about the treatment effect are confident. The playbook is explicit that a product still in early design, with inconsistent usage or untested mechanism hypotheses, should run Level 3 evaluations instead of an RCT.

Two further playbook commitments are carried into the output. First, *evaluability early*: holdout groups, staged rollouts, version tagging, and embedded randomization belong in the product's architecture before a Level 4 evaluation is justified, so the option is not foreclosed. Second, *the social-sector bar*: in the tech sector evaluation typically stops at Levels 1 and 2; here Levels 1 to 3 are necessary but not sufficient, so "no level recommended" is never a valid output. The recommendation names what to run now at whatever level fits.

Judgment call the source does not fully specify: the playbook gives gates in qualitative terms ("Levels 1 to 3 are strong"). This skill requires each gate judgment to cite the specific evidence in the AI product account (or the user funnel map) it rests on, so a disagreement about readiness is a disagreement about named evidence, not adjectives.

**WEIRD skew:** The framework was built for the development sector: its worked cases are education, health, and agriculture deployments in low- and middle-income countries, so its evidence base is unusually non-WEIRD for this library. The caveats run the other way. The playbook is a 2025 draft and living document, not a validated instrument, and a 2026 practitioner review by IDinsight is reported to have found that implementers treat the levels as an initial lens rather than a procedure (unverified, author to confirm). Expect to exercise judgment at the boundaries, not to read decisions off a chart.

**Replication status:** Not applicable in the effect sense: the four-level framework sequences evaluations, it is not an intervention, so there is no effect to replicate. It is a 2025 living document, and whether independent teams applying it to the same product reach the same level verdicts has not, to the authors' knowledge, been tested. Treat verdicts as structured judgment anchored to named evidence rather than as measurement.

## How to do it

1. **Carry over the product, the development outcome, and the decision** from the account at the top of the output, so every verdict is visibly tied to one decision.
2. **Give every level a verdict**: run now, continue/monitor, premature, or satisfied for this stage. Include levels already satisfied and levels far out of reach; a skipped row reads as an oversight downstream.
3. **Cite the evidence each verdict rests on**, naming the specific item in the account (or the user funnel map) or writing "none supplied". A disagreement about readiness should be a disagreement about named evidence, not adjectives.
4. **Apply the stage-matching gates.** Level 1 is cheap and continuous from day one. Level 2 needs a deployed product with real users. Level 3 needs Levels 1 and 2 working. Level 4 needs Levels 1 to 3 strong, a scale decision on the table, and confident priors about the treatment effect. A product with inconsistent usage or untested mechanism hypotheses gets Level 2 or 3 work, not an RCT.
5. **Write "what to run now"** for each run-now level: the concrete evaluation, the method family the playbook prescribes at that level, and the evidence it will produce. Point Level 2 and 3 experiments at `design-evidential-experiment` and outcome-measurement planning at `plan-evaluation-design`.
6. **Explain why each premature level is premature**, citing which gate fails and the account evidence behind it. This section is what the team hands a funder asking for the skipped level.
7. **List evaluability-early steps** whatever the verdicts: holdout groups, staged rollouts, version tagging, embedded randomization. This section is mandatory even when Level 4 is far off; it exists precisely for those products.
8. **State what would change the recommendation**: the specific evidence that would move each "premature" to "run now".
9. **Never return "no level recommended".** Levels 1 to 3 are necessary but not sufficient in the social sector, so the output always names something to run now at whatever level fits.

See `references/worked-example.md` for a complete run on MaizeMate, a WhatsApp agronomy assistant.

## Output template

```markdown
# AI evaluation level recommendation

**Product:** <name + one-line description, carried from the account>
**Development outcome targeted:** <the Level 4 outcome>
**Decision this recommendation informs:** <what the team will do differently depending on the answer>

## Level verdicts
| Level | Question | Verdict | Evidence the verdict rests on |
|---|---|---|---|
| 1: Model | Does the model produce the desired responses? | <verdict> | <named evidence from the account, or "none supplied"> |
| 2: Product | Does the product facilitate meaningful interactions? | <verdict> | <...> |
| 3: User | Does it positively support users' thoughts, feelings, actions? | <verdict> | <...> |
| 4: Impact | Does it improve the development outcome? | <verdict> | <...> |

## What to run now
<for each "run now" level: the concrete evaluation, the method family the playbook prescribes at that level, and the evidence it will produce. Point Level 2 and 3 experiments at design-evidential-experiment and outcome-measurement planning at plan-evaluation-design.>

## Why the premature levels are premature
<per premature level: which gate fails, citing the account. This section is what the team hands a funder asking for the skipped level.>

## Evaluability-early steps
<holdouts, staged rollout, version tagging, embedded randomization: the steps to take now so higher levels stay possible later. Mandatory even when Level 4 is far off.>

## What would change this recommendation
<the specific evidence that would move each "premature" to "run now">
```

## Where it goes wrong

- **Rubber-stamping the pressure.** The account says the funder wants an RCT, and the recommendation obligingly finds Level 4 "earned". The gate evidence column is the tell: if the Level 4 row cites the funder's interest rather than Level 1 to 3 evidence, the skill has answered the politics, not the framework.
- **Reading Level 2 off the team's adjectives.** "Engagement is strong" is a claim, not evidence. Without a user funnel map or named metrics in the account, the verdict must say what it is resting on, and "founder's impression" is a legitimate, flag-raising thing to write.
- **Treating levels as a ladder to climb once.** The playbook's levels are iterative: Level 1 monitoring continues at every later stage, and a product change resets Level 2 questions. A recommendation that reads "Level 1: done" has misread the framework.
- **Skipping evaluability-early because Level 4 is far off.** That section exists precisely for products far from an RCT; omitting it forecloses the option this framework is designed to keep open.
- **Out of scope: non-AI products.** For a program with no model in the loop, the level distinctions collapse and this skill's output is noise; use `plan-evaluation-design`. Also out of scope: ruling on whether the product should scale. This skill sequences evidence; it does not make the scale decision.

## When to bring in a specialist

Tell the user to involve an independent evaluator or research partner (a university team, an evaluation firm, a J-PAL or IPA-affiliated researcher) when:
- The recommendation lands on Level 4 run now; an impact evaluation of a product the team built should be designed and analyzed by people without a stake in the result, and the account alone cannot establish that the "confident priors" gate is met
- The product operates in a safety-critical domain (health advice, financial decisions, child protection, mental health), where "desired responses" at Level 1 needs a domain expert's definition, not the team's, before any higher level is read
- A funder and the team still disagree about readiness after seeing the level table; the disagreement is then about what counts as evidence, which a neutral methodologist should arbitrate

Bring them: the product account, the level table with its evidence column, and the user funnel map if one exists.
