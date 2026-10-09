---
name: plan-evaluation-design
description: >-
  Use when a target behavior is defined but nobody has agreed how to measure
  success: the primary outcome, the comparison condition, and the smallest
  effect worth detecting. Also use when someone asks "how will we actually
  know if this worked?" or "what counts as success here?", or when an
  intervention is about to launch with no named primary outcome. Produces a
  pre-registration-style measurement plan fixed before launch, so nobody can
  redefine success after seeing the results. Do not use on a vague program
  goal; run define-key-behavior first, since there is no single behavior to
  measure yet. Not for configuring a rapid product experiment in an
  experimentation tool (design-evidential-experiment), and not for deciding
  which level of AI evaluation a product is ready for (choose-ai-eval-level).
license: CC-BY-4.0
metadata:
  title: Plan how you will measure success
  type: atomic
  stage: test
  version: "0.1.0"
  status: draft
  authors: "Joe Speed"
  org: IL
  weird: likely-generalizes
  tags: "experimental-design, pre-registration, measurement"
  consumes: "target-behavior-brief, comb-barrier-hypotheses, intervention-levers"
  produces: "evaluation-design"
---

## What it does

Produces a pre-registration-style measurement plan for one defined behavior, locked in before launch.

The plan names the primary outcome, what it is compared against, the smallest effect worth detecting, whether the data can actually be collected, and any mediating measures needed to evaluate a specific barrier hypothesis. Fixing these in advance stops anyone from redefining success after seeing which number happened to move.

## When to use it

### Use it when
- A target behavior brief exists and someone is about to design or launch an intervention with no named primary outcome, no comparison condition, and no agreement on what effect size would actually matter
- `decompose-comb-barriers` has produced barrier hypotheses and the team needs to know what mediating measure would let those specific hypotheses be evaluated, not just whether the headline outcome moved
- Someone asks "how will we actually know if this worked?" or "what counts as success here?"
- A funder or partner asks for "the M&E plan" or "the evaluation design" for a behavior the program has already defined

### Do not use it when
- The input is a vague program goal; run `define-key-behavior` first. There is no single behavior yet to measure
- The team wants a launch-ready configuration for a rapid experiment in Evidential (arms, randomization unit, power inputs, delivery mapping); `design-evidential-experiment` does that, and consumes this skill's brief
- The question is which level of AI evaluation an AI product is ready for; `choose-ai-eval-level`
- The team wants to build or pretest the survey instrument itself; instrument skills such as `draft-cognitive-interview-script` come after the outcome is chosen

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The target behavior as who, what, when. Paste the target behavior brief from `define-key-behavior` or state the behavior at that level of specificity. If it is still a goal ("improve savings"), send it back for definition before continuing.
2. **Required.** What the program needs to see to justify continuing or scaling. Has a sponsor, funder, or program lead stated a threshold? If nobody has, say so; the plan will mark the minimum effect provisional rather than invent a rationale.
3. **Required.** What data exists today or could exist: administrative records, transaction logs, survey capacity, and who controls access. "Assumed available" is not an answer.
4. Optional. The COM-B barrier hypotheses from `decompose-comb-barriers`. With them, mediating measures become mandatory.
5. Optional. The intervention lever brief from `select-intervention-levers`, including the planned rollout shape (phased or simultaneous, whether anyone is held back). Without it, the comparison condition is stated as an assumption.

If 1 is missing, ask and stop. If 2 or 3 is missing, ask once; if still unknown, proceed and mark the threshold provisional and the data source unconfirmed under "Open questions". If 4 and 5 are missing, write "Not applicable: no COM-B barrier hypotheses for this run" in the mediating measures section and state the assumed rollout explicitly.

## What it draws on

- Olken, B. A. (2015). Promises and Perils of Pre-analysis Plans. *Journal of Economic Perspectives*, 29(3), 61-80.
- Duflo, E., Glennerster, R., & Kremer, M. (2007). Using Randomization in Development Economics Research: A Toolkit. In T. P. Schultz & J. Strauss (Eds.), *Handbook of Development Economics*, Vol. 4, Ch. 61.

Olken's account of pre-analysis plans: an evaluation's credibility depends on locking in the primary outcome and the effect size that matters before data collection, specifically so neither can be redefined afterward to match whichever measure happened to move (HARKing, hypothesizing after results are known). The output template's mandatory pre-registration statement operationalizes this directly. It exists to be checked against later, not written once and forgotten.

Duflo, Glennerster, and Kremer's toolkit is the basis for treating the program's minimum effect worth detecting as a designed choice tied to what it actually needs to see to be worth continuing, not a statistical-convention default. Note what this section is not: "minimum detectable effect" is also a term of art in power analysis (the smallest effect a study is statistically powered to find, given sample size and baseline variance). That is a different, narrower calculation this skill does not perform. This section is the program-value input such a power calculation would need, not a substitute for one. If no sponsor-stated threshold is available, say so explicitly and mark the number provisional in Open questions. Inventing a plausible-sounding programmatic rationale to fill the gap is exactly the failure this discipline exists to prevent.

The comparison condition depends on knowing the intervention's rollout shape (phased or simultaneous, whether anything is held back) at least as much as the mediating-measures section depends on the barrier hypotheses. If an intervention lever brief is available, use its described rollout to ground the comparison condition; if not, state the assumed rollout explicitly as unconfirmed rather than presenting an invented design as given.

Data-source feasibility is checked explicitly because a plan that assumes a measure exists, because similar programs report it, without confirming it is collectible here at the needed frequency, is not a measurement plan yet. A measure that observes the right construct can still be gamed or degraded in how it is recorded, for instance when an incentive tied to a metric distorts how that metric gets reported. That risk belongs in the feasibility section too, distinct from having picked the wrong construct.

**WEIRD skew:** The statistical methodology (power reasoning, pre-registration against HARKing and p-hacking) is general-purpose and not culturally bound. What is not uniform is the data infrastructure the feasibility section depends on: administrative records, mobile-money transaction logs, or survey infrastructure that would make a chosen primary outcome collectible vary enormously by setting, and the output is only as good as that check is honest.

**Replication status:** Not applicable in the effect sense: pre-registration and the minimum-effect discipline are methodological practices, not interventions. Olken (2015) argues their case and their costs rather than testing them, and the statistical logic in Duflo, Glennerster, and Kremer (2007) is standard. Evidence on how much pre-registration reduces outcome switching comes mainly from clinical trials and economics rather than social-sector program evaluation (unverified, author to confirm).

## How to do it

1. **Carry the target behavior over verbatim** at the top, so every section below is visibly attached to one who, what, when.
2. **Name the primary outcome.** It is the one measure that would make the team say "this worked", and it must observe the target behavior itself, not a proxy adopted for convenience. If a proxy is genuinely necessary, name the substitution and the gap it leaves. Separately, name any way the recording of this measure could be gamed or degraded, such as an incentive tied to the same number.
3. **Set the comparison condition.** State what "no effect" looks like: a control group, a randomized waitlist, or a named historical baseline. If an intervention lever brief names the rollout shape, ground the comparison in it; otherwise state the assumed rollout explicitly as unconfirmed. "Pre/post on the same group only" is not a comparison condition; if it is the fallback, say so and why, because anything else that changed over the period becomes indistinguishable from the intervention's effect.
4. **State the minimum effect worth detecting** as the smallest effect size the program needs to see to justify continuing. Tie it to a sponsor-stated or program-stated threshold. It is not a power calculation and not a default pulled from convention. If no threshold exists, say so here and mark the number provisional in Open questions; do not manufacture a rationale.
5. **Check data-source feasibility.** Say where the primary outcome's data will come from, whether it exists today at the frequency needed, and who would need to grant access.
6. **Write the mediating measures.** If COM-B barrier hypotheses are available, write one row per hypothesis with a measure distinct from the primary outcome that would let that hypothesis be evaluated afterward. If none are available, write "Not applicable: no COM-B barrier hypotheses input for this run" rather than leaving the section out, because an absent section and a checked absence look identical to a downstream reader.
7. **Write the pre-registration statement:** one dated sentence naming the primary outcome and the minimum effect worth detecting, so neither can be quietly redefined after results are seen.
8. **List open questions:** anything the brief had to assume about data access, rollout design, or the decision threshold that needs confirming before the plan is final.

See `references/worked-example.md` for a complete run on the Nairobi market-vendor savings behavior.

## Output template

```markdown
# Evaluation design brief

**Target behavior:** <who + what + when, carried over verbatim>

## Primary outcome metric
<the one measure that would make the team say "this worked"; it must observe the target behavior itself, not a proxy adopted for convenience. If a proxy is genuinely necessary, name the substitution explicitly and say what gap it leaves. Separately, name any risk that the recording of this measure (not the construct itself) could be gamed or degraded, e.g. an incentive tied to the same number distorting how it gets reported.>

## Comparison condition
<what "no effect" looks like: a control group, a randomized waitlist, or a named historical baseline. "Pre/post on the same group only" is not a comparison condition; state plainly if that is the fallback and why. If an intervention lever brief names the rollout shape, ground this in it; if not, state the assumed rollout explicitly as unconfirmed rather than presenting an invented design as settled.>

## Minimum effect worth detecting
<the smallest effect size worth caring about, tied to what the program needs to see to justify continuing; not a statistical power calculation, and not a default pulled from convention. If no sponsor-stated threshold is available, say so explicitly here and mark the number provisional in Open questions, rather than manufacturing a programmatic rationale to fill the gap.>

## Data source feasibility
<where the primary outcome's data will actually come from, whether it exists today at the frequency needed, and who would need to grant access; "assumed available" is not a feasibility check>

## Mediating measures
<mandatory if COM-B barrier hypotheses are available: one row per hypothesis, each with a measure distinct from the primary outcome that would let that specific hypothesis be evaluated afterward. If no barrier diagnosis is available for this target behavior, write "Not applicable: no COM-B barrier hypotheses input for this run" rather than leaving the section out.>

## Pre-registration statement
<one locked-in sentence naming the primary outcome and the minimum effect worth detecting, dated, so neither can be quietly redefined after seeing results>

## Open questions
<anything this brief had to assume about data access, rollout design, or the decision threshold that needs confirming before the plan is final>
```

## Where it goes wrong

- **Proxy substitution.** Swapping the primary outcome for whatever is easiest to measure (app opens instead of an actual deposit) without naming the substitution and the gap it leaves is the most common way an evaluation brief looks rigorous but measures the wrong thing.
- **No named comparison condition.** "We'll check before and after" is not a comparison condition. Anything else that changed over the same period (season, prices, a different program) becomes indistinguishable from the intervention's effect.
- **Default minimum effect.** Powering a study for whatever effect size a statistics template defaults to, rather than the effect size the program needs to see to be worth continuing, produces a technically valid but practically meaningless design.
- **Assumed data feasibility.** Naming a measure because comparable programs report it, without confirming it is collectible for this program, at this frequency, with this population's consent. The feasibility section exists to force that check before it becomes a mid-study surprise.
- **Retroactive outcome redefinition.** Changing which metric counts as "the" primary outcome after seeing which one moved is the exact failure the mandatory, dated pre-registration statement exists to make visible when it happens.
- **Confusing the program threshold with a power calculation.** Presenting the minimum effect worth detecting as if a sample size had been derived from it. This brief supplies the input to that calculation; it does not perform it.

## When to bring in a specialist

Tell the user to consult an evaluation methodologist or statistician, and where relevant a research ethics board, when:
- The team needs an actual power calculation (sample size from baseline variance, intra-cluster correlation, expected attrition); this brief supplies the program-value input to that calculation, not the calculation itself
- The rollout forces a clustered, stepped-wedge, or phased design, or randomization is not possible and a quasi-experimental comparison is being considered; choosing among these is a methodologist's call, not a template's
- The primary outcome is high-stakes (health, safety, eligibility for benefits) or data collection involves vulnerable participants, so the plan needs ethics review before it is locked
- A funder requires formal pre-registration (a trial registry, OSF) or a full pre-analysis plan with specified models; this brief is the input to that document, not a substitute for it

Bring them: this brief with its open questions, any baseline data on the primary outcome, and the rollout plan.
