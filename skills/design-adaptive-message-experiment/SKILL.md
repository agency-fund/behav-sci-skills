---
name: design-adaptive-message-experiment
description: >-
  Use when a team has several candidate messages, reminder timings, or
  nudges and wants to find the best one fast by shifting later waves of
  people toward the arms that are winning, instead of splitting everyone
  evenly for the whole study. Also use when someone says "bandit",
  "adaptive", "Thompson sampling", or "can we drop the losing versions
  partway through?", or has more arms than the sample can test equally.
  Produces an adaptive design: arms, one fast reward metric, batch
  schedule, exploration floor, algorithm, stopping rule, holdout, and an
  inference plan that corrects for adaptive assignment (Offer-Westort,
  Coppock and Green 2021; Kasy and Sautmann 2021). Do not use when the
  team needs one defensible effect estimate from a fixed design for a
  scale or funding decision; use design-evidential-experiment or
  choose-trial-design instead. Not for writing the arms themselves
  (write-social-norm-message, design-reminder-schedule) or for sizing a
  fixed design (estimate-sample-size).
license: CC-BY-4.0
metadata:
  title: Find the best message with an adaptive experiment
  type: atomic
  stage: test
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "experimental-design, quantitative, adaptive-design"
  consumes: "experiment-intent, intervention-draft"
  produces: "evaluation-design"
---

## What it does

Designs a multi-wave experiment that moves later waves of participants toward the better-performing message arms while keeping the final answer statistically honest.

An adaptive (bandit-style) design assigns people in batches. After each batch it updates its estimate of which arms do best on one quickly observed reward (a reply, a click, a visit within days) and sends more of the next batch to those arms. It trades precise estimates of every arm for finding a good arm sooner, with fewer people exposed to weak arms. This skill decides the arms, the reward, the batch schedule, the exploration floor, the algorithm, the stopping rule, the holdout, and the inference correction. It does not write the arms or run the assignment.

## When to use it

### Use it when
- A team has four or more candidate messages, timings, or framings (for example from `write-social-norm-message` or `design-reminder-schedule`) and wants to know which one to roll out, not the precise effect of each
- Someone asks "can we drop the losing versions partway through?", "should we run a bandit?", or "what is Thompson sampling and do we need it?"
- The outcome that matters can be observed within days of sending (a reply, a click, a clinic visit, a deposit), and people keep arriving or messages keep going out in waves, so assignment can change between waves
- The team is about to split a many-arm test evenly and leave every arm underpowered, or to pick a winner by eye from a small first wave

### Do not use it when
- The decision is whether a program works and by how much, for a funder or a scale-up; a fixed-allocation design gives the cleaner estimate. Use `design-evidential-experiment` for a product experiment in Evidential, or `choose-trial-design` for the trial's structure
- The arms do not exist yet; write them with `write-social-norm-message`, `design-reminder-schedule`, or `draft-lever-content`, then come back
- The reward lags by weeks or months (next term's enrollment, harvest yield); there is nothing to update on between waves, so use a fixed design and `estimate-sample-size`
- The question is how many people a fixed design needs; `estimate-sample-size`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The arms: each candidate message or variant pasted in, plus the control (no message, or the current message). Fewer than three arms is a fixed test; say so and point to `design-evidential-experiment`.
2. **Required.** The reward: the one outcome observable per person within days of assignment, where it is recorded, and how many days after sending it is counted. If the only outcome is weeks away, stop and see the specialist section.
3. **Required.** The goal: choose the best arm to roll out afterward (policy choice), or get the most responses during the campaign itself? This decides the algorithm.
4. **Required.** The flow: how many people can be assigned per wave, how many waves, and who implements assignment (Evidential's bandit experiment types, an engineer, a script).
5. Optional. Any arm that could plausibly harm, shame, or mislead, and the organization's consent or notification posture for being experimented on.
6. Optional. An evaluation design brief from `plan-evaluation-design`, for the decision threshold and the outcome that matters beyond the reward.

If 1 to 4 are missing, ask and stop. If 5 is missing, assume no arm is risky but say so under Open questions. If 6 is missing, state the decision threshold as the team's own and mark it provisional.

## What it draws on

- Offer-Westort, M., Coppock, A., & Green, D. P. (2021). Adaptive experimental design: Prospects and applications in political science. *American Journal of Political Science*. https://doi.org/10.1111/ajps.12597
- Kasy, M., & Sautmann, A. (2021). Adaptive treatment assignment in experiments for policy choice. *Econometrica*, 89(1), 113–132. https://doi.org/10.3982/ECTA17527
- EGAP. *10 things to know about adaptive experimental design*. https://egap.org/resource/10-things-to-know-about-adaptive-experimental-design/
- Banerjee, A., Chandrasekhar, A. G., Dalpath, S., Duflo, E., Floretta, J., Jackson, M. O., et al. (2025). Selecting the most effective nudge: Evidence from a large-scale experiment on immunization. *Econometrica*, 93(4), 1183–1223. https://doi.org/10.3982/ECTA19739
- Milkman, K. L., et al. (2021). Megastudies improve the impact of applied behavioural science. *Nature*, 600, 478–483. https://doi.org/10.1038/s41586-021-04128-4

Offer-Westort, Coppock, and Green set out adaptive designs for social science: assign in batches, update after each batch, and choose the algorithm by the goal. Thompson sampling assigns each arm to the next batch in proportion to the current probability that it is the best arm, so it concentrates people on the leader quickly. Exploration sampling, from Kasy and Sautmann, modifies Thompson sampling so that assignment keeps spreading across arms that might still be best rather than piling onto the current leader, because the goal is to choose the best policy at the end rather than to maximize outcomes during the experiment; their application was recruiting farmers into agricultural extension in India. The dossier this skill draws on records a possible published correction to Kasy and Sautmann's optimality result (unverified, author to confirm), so treat exploration sampling as a sound default, not a settled optimum.

Two cautions shape the procedure. First, standard errors computed as if assignment were fixed are biased after adaptive assignment, because which arm a person got depended on earlier outcomes; the inference plan has to say how that is handled. Second, the arm that wins a many-arm comparison carries a winner's curse: its estimate is selected for being high. Banerjee et al. tested 75 arms in Haryana, India, aggregated results by treatment variant, and applied a winner's-curse correction; SMS reminders alone had no impact, while SMS plus information-hub ambassadors was the most cost-effective bundle (+9.1% immunizations per dollar; J-PAL page, secondary source per the dossier). Milkman et al. tested 54 interventions on 61,293 US gym members; 45% raised visits by 9 to 27%, only 8% produced effects that persisted after the program, and expert forecasts failed. The judgment calls this skill adds: a burn-in wave split evenly, an exploration floor in every wave, a holdout kept at fixed allocation, and a confirmatory test after the adaptive phase.

**WEIRD skew:** The method is statistical, not population-bound. The anchor applications are a political-science review (Offer-Westort et al.), one Indian field application (Kasy and Sautmann), one Indian 75-arm trial (Banerjee et al.), and one US megastudy (Milkman et al.). What a user elsewhere should check locally: whether the reward is recorded reliably within days in their system, whether waves arrive at a steady rate, and whether delivery differs by subgroup (shared phones, literacy, network) so that the "best arm" differs by who receives it. **Non-WEIRD evidence:** India: Kasy and Sautmann's exploration-sampling application to recruiting farmers into agricultural extension (the dossier records no effect size); India, Haryana: Banerjee et al. (2025), 75 arms, SMS alone no impact, SMS plus ambassadors most cost-effective at +9.1% immunizations per dollar (secondary source per the dossier).

**Replication status:** Not an effect to replicate. That naive standard errors are biased after adaptive assignment is uncontested; the optimality claim for exploration sampling has a possible published correction (unverified, author to confirm); no message effect size from the many-arm studies is quoted here as a benchmark, since the lesson of those studies is that most arms differ little and short-run winners often do not persist.

## How to do it

1. **Carry over the experiment intent verbatim** and name the single decision the result informs: which arm to roll out, to whom, by when.
2. **Define the arms.** List each with a one-line description, control first. Merge near-duplicates. Name the dimension each arm varies (frame, timing, messenger, sender) so results can be aggregated by dimension, as Banerjee et al. did across 75 arms; with many arms, the dimension-level answer is often the usable one.
3. **Define the one reward metric** observable quickly: what counts as success, within how many days of assignment, read from which system. The reward window is the minimum gap between waves. If the reward lags by weeks, stop and route to the specialist section; the design has nothing to adapt on.
4. **Set the batch schedule and the exploration floor.** Split the first wave evenly as a burn-in. For every later wave set a minimum share per arm so no arm is starved and every arm still has data at the end. State people per wave, number of waves, and who triggers each wave.
5. **Choose the algorithm by the goal.** Policy choice (pick the best arm afterward): exploration sampling. Most responses during this campaign itself (a one-off drive where every person counts): Thompson sampling. Estimates of every arm: fixed allocation, and leave this skill. Write the one-sentence reason.
6. **Pre-specify inference.** Name the estimator and standard errors that account for adaptive assignment, and the winner's-curse correction for the selected arm. If the team has no statistician, the honest default is to estimate the selected arm's effect only in the confirmatory test (step 8) and to report adaptive-phase numbers as descriptive.
7. **Set the stopping rule and the holdout.** Stop at a fixed number of waves or when the probability that the leader is best exceeds a threshold set now. Keep a holdout (a fixed share assigned to control, or a slice assigned evenly) throughout, so the final comparison against control is not itself adaptive.
8. **Decide the confirmatory test.** After the adaptive phase, compare the selected arm against control in one fixed-allocation wave or in the holdout, analyzed the ordinary way. Schedule a persistence check on the outcome that matters, dated.
9. **Write the implementation note:** who runs assignment, where the reward is read, the wave cadence, and the harm or consent review for any flagged arm.
10. **Stop here.** The design goes to `write-pre-analysis-plan` for registration and, if the confirmatory wave needs sizing, to `estimate-sample-size`.

See `references/worked-example.md` for a complete run on HIV self-test kit requests in Lagos, and `references/evidence-notes.md` for the sources with their verification state.

## Output template

```markdown
# Adaptive message experiment design

**Experiment intent:** <carried over verbatim>
**Decision this informs:** <which arm to roll out, to whom, by when>
**Goal:** <policy choice / most responses during this campaign>, which sets the algorithm

## Arms
| Arm | One-line description | Dimension varied | Source |
|---|---|---|---|
| 0 (control) | <current message or none> | | |
| 1 | <...> | <frame / timing / messenger> | <skill or author> |

## Reward metric
<one outcome per person, counted within <N> days of assignment, read from <system>; what counts as success; why this and not the slower outcome that matters more>

## Batch schedule and exploration floor
| Wave | People | Allocation rule |
|---|---|---|
| 1 | <n> | even split (burn-in) |
| 2 onward | <n> | <algorithm> with a floor of <x%> per arm |
<minimum gap between waves = reward window; who triggers each wave>

## Algorithm
<Thompson sampling / exploration sampling, with the one-sentence reason tied to the goal>

## Inference plan
<estimator and standard errors that account for adaptive assignment; winner's-curse correction for the selected arm; who computes it; or the fallback: adaptive-phase numbers descriptive only, effect estimated in the confirmatory test>

## Stopping rule and holdout
<fixed number of waves or a pre-set probability-best threshold; the holdout or fixed control share kept throughout>

## Confirmatory test
<the final fixed-allocation comparison of the selected arm against control, its size, and the dated persistence check on the outcome that matters>

## Implementation
<who runs assignment (tool, engineer, script); where the reward is read; harm or consent review for any flagged arm>

## Open questions
- <the assumption most likely to be wrong>
```

## Where it goes wrong

- **Adapting on a lagging reward.** If the reward arrives weeks after assignment, every wave is assigned on stale information and the design is a fixed test with extra complexity. The reward window must be days.
- **Reading the adaptive-phase estimate as the effect.** Means and standard errors computed as if allocation were fixed are biased after adaptive assignment, and the winner's estimate is inflated by selection. The confirmatory test exists so that the number the team acts on was not produced by the adaptation.
- **Starving the runners-up.** Thompson sampling with no floor can push nearly everyone onto an early leader; an arm that would have won with more data never gets it. The exploration floor and the burn-in wave are not optional.
- **Picking a short-run winner.** The reward is a proxy chosen for speed. Milkman et al. found only 8% of 54 interventions produced effects that persisted; the dated persistence check is part of the design, not an afterthought.
- **Bandit for a scale decision.** Bandits answer "which arm" cheaply, not "how much better, with what confidence". If the result has to justify funding or scale-up, use a fixed design.
- **Shifting people onto an unreviewed arm.** An adaptive design can move most of a wave onto one arm before anyone has checked it. Refuse to include an arm the team has flagged as possibly harmful, shaming, or misleading until it has been reviewed.

## When to bring in a specialist

Tell the user to consult a statistician with adaptive-design experience, and an ethics reviewer where relevant, when:
- The reward lags by weeks; there is nothing to adapt on, and the fix is a fixed design sized with `estimate-sample-size`, not a slower bandit
- Any arm could plausibly harm, shame, or mislead, since adaptation can concentrate exposure on it before the team notices
- The team has no engineer or tool to implement assignment; a bandit run by hand drifts into ad hoc allocation that no inference plan can repair
- The inference plan needs more than "estimate in the confirmatory test": estimators for adaptively collected data are specialist work

Bring them: the arms table with dimensions, the reward definition and window, the batch schedule with its floor, and the decision rule.
