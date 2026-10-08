---
name: build-user-funnel
description: >-
  Use when an AI or digital product aims at a real-world outcome but nobody
  has written down the steps from a user's first contact to that outcome,
  when "engagement" is reported as one aggregate number (total messages,
  daily active users), or when a theory of change exists only as
  grant-proposal prose and metrics or experiments are about to be built on
  it. Works backward from the outcome to set out six stages, from
  recruitment to the development outcome, each with the user action that
  marks entry, a confirming metric, a target, and an owner. Do not use to
  explain why users drop off at a stage; hand the funnel and the observed
  numbers to diagnose-funnel-weak-link. Not for defining one offline target
  behavior for a non-digital program; that is define-key-behavior.
license: CC-BY-4.0
metadata:
  title: Map the user journey from first contact to outcome
  type: atomic
  stage: define
  version: "0.1.0"
  status: draft
  authors: "Joe Speed"
  org: IL
  weird: likely-generalizes
  tags: "ai-eval, funnel, measurement"
  consumes: "ai-product-account, audience-context-brief"
  produces: "user-funnel-map"
---

## What it does

Turns one real-world outcome into a six-stage user funnel, worked backward from the outcome.

The stages are recruitment, onboarding, engagement, retention, proximal outcome, and development outcome. For each stage it defines the user action that counts as reaching it, the metric that confirms it, a target, and an owner, with model-quality monitoring running underneath the whole funnel. The result turns a theory of change into something a team can measure stage by stage and later diagnose.

## When to use it

### Use it when
- A team reports "engagement" as one aggregate number (total messages, daily active users) with no account of where users are in the journey from first contact to outcome
- A product's theory of change exists only as grant-proposal prose and needs to become, in the playbook's words, "a measurable, cost-aware program design tool" before metrics or experiments are built on it
- `choose-ai-eval-level` needs to judge Level 2 evidence and there are no named stages to judge it against
- Metrics pipelines are about to be built (the playbook's Motion 02) and need to know which indicators matter per stage
- Someone asks "what does our funnel look like?" or "which metrics should we track at each step?"

### Do not use it when
- The task is to define one offline target behavior for a non-digital program; that is `define-key-behavior`, and the funnel's proximal-outcome stage may in fact consume its output
- The question is why an existing funnel leaks at a particular stage; hand the built funnel plus observed numbers to `diagnose-funnel-weak-link`
- The team wants a test set for the model's answers; that is `design-golden-dataset`, which sits underneath the funnel as Level 1 monitoring

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The AI product account: what the product does, for whom, how users currently find and use it, and the one development outcome it targets. The funnel is worked backward from that outcome; a second outcome is a second funnel, so if the account names two, ask which one this run is for.
2. **Required.** Where stage metrics would come from today: message logs, session events, surveys, partner records. This feeds the instrumentation reality check; without it the funnel may list metrics nobody can observe.
3. Optional. An audience and context brief from `map-audience-context`. Its decision moment and existing channels ground the recruitment and onboarding stages in channels this population actually uses rather than invented ones.
4. Optional. Any targets or transition rates the team already has in mind, even rough ones.

If 1 is missing, ask and stop. If 2 is missing, ask once; if still unknown, build the funnel and mark every stage's metric "observability unconfirmed" in the reality check. If 3 is missing, use the channels named in the account and flag them as unconfirmed. If 4 is missing, guess the targets and mark every one provisional.

## What it draws on

- Wu, Z., On, R., Walsh, J., Korley, E., Madon, T., & Wong, L. (2025). AI Evaluation in the Social Sector: A Living Playbook. Repeatable Motions. The Agency Fund. https://eval.playbook.org.ai/motions
- On, R., & Madon, T. (2025). AI4GD User Funnel and Metrics Playbook. The Agency Fund, AI for Global Development accelerator. Companion playbook referenced from the AI Evaluation Playbook's Level 2 chapter.

Repeatable Motion 01 of The Agency Fund's AI Evaluation Playbook (Wu et al., 2025): construct a user funnel across evaluation levels by starting from the targeted development outcome (Level 4) and working backward through the proximal user outcome (Level 3) to retention, engagement, onboarding, and recruitment (all Level 2), with model-quality monitoring (Level 1) running underneath every stage. The motion's stated purpose is carried directly into the output: it "transforms a generic theory of change into a measurable, cost-aware program design tool." The per-stage fields (what the program does, what the user must do to count as entering the stage, the confirming metric, target values and transition rates, and a directly responsible individual) follow the companion AI4GD User Funnel and Metrics Playbook (On & Madon, 2025).

Two constraints this skill enforces that the source states but teams skip. First, *entry is a user action, not a program action*: "we sent 10,000 SMS invitations" is program activity; "farmer sends a first message" is a stage entry. Every stage's entry condition must be something the user does. Second, *the proximal outcome is a real outcome, not more engagement*: the stage before the development outcome must name a change in the user's knowledge, decision, or behavior that plausibly mediates the outcome. If it is phrased as more usage, the funnel has no Level 3 rung and cannot support user evaluation later.

Judgment call the sources do not fully specify: target transition rates at first build are usually guesses. This skill requires them anyway, marked `provisional`, because a funnel with no targets cannot identify a weak link (every stage looks fine when nothing is expected of it), and an explicit guess invites correction where a blank invites nothing.

**WEIRD skew:** The funnel structure is accounting, not psychology: it carries no claims about behavior, and the source playbooks were written for low- and middle-income-country deployments. What does not travel automatically is the instrumentation assumption. Stage metrics presume telemetry (message logs, session events) that shared-phone use, intermittent connectivity, and channel switching (a user moving from WhatsApp to calling a hotline) all quietly break. Confirm each stage's confirming metric is observable for this population before trusting funnel numbers.

**Replication status:** Not applicable in the effect sense: a funnel is an accounting structure, not an intervention. The source playbooks are 2025 practitioner documents, and whether funnels built this way lead to better evaluation decisions than other theory-of-change formats has not, to the authors' knowledge, been tested. Treat the structure as a discipline for making metrics explicit, not as a validated model.

## How to do it

1. **Name the one development outcome** (Level 4) and work backward: the proximal user outcome (Level 3), then retention, engagement, onboarding, and recruitment (all Level 2), with model-quality monitoring (Level 1) underneath every stage. If the account names two outcomes, build one funnel and say the second needs its own.
2. **Write the user action that counts as entry for every stage.** "We broadcast on radio" is program activity, not an entry; "farmer sends any first message" is. Every entry cell contains a user's verb.
3. **Write the proximal outcome as a change in knowledge, decision, or behavior** that plausibly mediates the development outcome. If the row reads as more usage ("asks 3+ questions"), it is the engagement stage again and the funnel has no Level 3 rung.
4. **Choose a confirming metric per stage and run the instrumentation reality check**: say where each metric will come from and name every stage whose metric is not currently observable. An unobservable stage is a named gap, not a discovery at the first readout.
5. **Set a target or transition rate for every stage**, marked provisional when guessed. A funnel with no targets cannot flag a weak link.
6. **Name an owner per stage**, a directly responsible individual or role.
7. **Keep all six stages.** If one genuinely does not apply (a pre-enrolled population with no recruitment), write the row with "not applicable" and the reason; a missing row and a checked non-stage must look different downstream.
8. **List the Level 1 monitoring underneath the funnel**: the model-quality indicators tracked continuously (response quality, safety and guardrail hits) and where they are logged.
9. **List the assumptions the funnel makes** about channel, telemetry, and population, each phrased so it can be checked.

See `references/worked-example.md` for a complete run on MaizeMate, a WhatsApp agronomy assistant.

## Output template

```markdown
# User funnel map

**Product:** <name + one line>
**Development outcome (Level 4):** <the outcome the funnel works backward from; one outcome, since a second outcome is a second funnel>
**Instrumentation reality check:** <where these metrics will come from, and any stage whose metric is not currently observable>

## Stages
| # | Stage | User action that counts as entry | Confirming metric | Target (transition from previous stage) | Owner |
|---|---|---|---|---|---|
| 1 | Recruitment | <...> | <...> | <n or %; mark provisional if guessed> | <name/role> |
| 2 | Onboarding | <...> | <...> | <...> | <...> |
| 3 | Engagement | <...> | <...> | <...> | <...> |
| 4 | Retention | <...> | <...> | <...> | <...> |
| 5 | Proximal outcome (Level 3) | <a knowledge, decision, or behavior change, not more usage> | <...> | <...> | <...> |
| 6 | Development outcome (Level 4) | <...> | <...> | <...> | <...> |

## Level 1 monitoring underneath the funnel
<the model-quality indicators tracked continuously across all stages, such as response quality and safety or guardrail hits, and where they are logged>

## Assumptions this funnel makes
<channel, telemetry, and population assumptions that, if wrong, break a stage's metric; each phrased so it can be checked>
```

## Where it goes wrong

- **Program actions as stage entries.** "We broadcast on radio" in the recruitment row. Nothing about the user has happened yet; the funnel then measures the organization's activity and reads healthy while no farmer moves. Every entry cell must contain a user's verb.
- **The engagement-shaped proximal outcome.** Stage 5 written as "farmer asks 3+ questions" is stage 3 again wearing a hat. If the proximal row names usage, the funnel cannot support Level 3 evaluation, which is most of why it is being built.
- **Metrics nobody can observe.** A tidy funnel whose stage 5 and 6 metrics require surveys or records that do not exist. The instrumentation reality-check line is mandatory precisely so an unobservable stage is a named gap, not a discovery during the first readout.
- **Two outcomes, one funnel.** "Yield and financial resilience" at stage 6 forks every upstream target. One funnel per outcome; build the second separately if it is real.
- **Targets omitted as unknowable.** A funnel with blank targets cannot flag a weak link. Guess, mark provisional, and let the first funnel metric readout correct it.
- **Out of scope: non-digital single behaviors.** A vaccination-uptake program with no product journey does not need six stages; it needs `define-key-behavior` and `decompose-comb-barriers`. Forcing funnel structure onto it manufactures stages with no observable metrics.

## When to bring in a specialist

Tell the user to consult a measurement specialist (a psychometrician or survey methodologist, or the program's M&E lead) or the partner responsible for data access when:
- The stage 5 proximal outcome is a change in knowledge, belief, self-efficacy, or intention that needs a validated instrument rather than a two-item in-chat check; `draft-cognitive-interview-script` and a psychometrician come before that metric is trusted
- The stage 6 metric depends on administrative or partner records (harvest records, clinic registers, exam results) that need a data-sharing agreement; until one exists the funnel's top rung is aspiration
- The instrumentation reality check shows that shared devices, channel switching, or intermittent connectivity break the identity assumption behind the metrics ("one number is one user"); a data engineer should assess what the logs can support before targets are set

Bring them: the funnel table, the instrumentation reality check, and the assumptions list.
