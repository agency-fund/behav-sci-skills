---
name: choose-trial-design
description: >-
  Use when a team knows what it wants to test but not how to randomize it:
  "should we randomize people or villages?", "we cannot withhold the program
  from anyone", "the rollout is phased anyway", "which of our components
  matter?". Also use when spillovers, rollout logistics, or the ethics of
  withholding make an individual lottery wrong, or a plan says "RCT" with no
  unit of randomization named. Chooses among individual, cluster,
  stepped-wedge, factorial, and encouragement designs from the program's
  constraints, states each design's power cost and analysis demands (Hemming
  et al. 2015; Hayes and Moulton 2009; Collins 2018), and names a runner-up.
  Do not use for the full measurement plan (outcome, comparison, data
  feasibility); that is plan-evaluation-design, which consumes this choice.
  Not for the sample size (estimate-sample-size), an Evidential setup
  (design-evidential-experiment), an adaptive many-arm test
  (design-adaptive-message-experiment), or a feasibility pilot
  (design-pilot-feasibility-study).
license: CC-BY-4.0
metadata:
  title: Pick how to randomize the test
  type: atomic
  stage: test
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: not-applicable
  tags: "experimental-design, quantitative"
  consumes: "experiment-intent, theory-of-change"
  produces: "evaluation-design"
---

## What it does

Chooses the randomization structure for one test from the program's constraints: individual, cluster, stepped-wedge, factorial, or encouragement.

Each design answers a different constraint. Individual randomization is the most efficient but fails when treated and untreated people affect each other. Cluster randomization assigns whole groups (villages, clinics, schools) and pays for it in power. A stepped-wedge trial gives every cluster the program eventually, in a randomized order, and pays in time and in analysis. A factorial design crosses components to learn which matter. An encouragement design randomizes the offer when the program cannot control who takes it up. This skill lists the constraints, maps each to the designs it rules in or out, picks one, and hands it on; it does not write the measurement plan or size the sample.

## When to use it

### Use it when
- Someone asks "should we randomize individuals or villages?", "how do we run an RCT when everyone has to get it eventually?", or "can we test this when we only control who is invited?"
- An experiment intent or theory of change exists and the plan says "RCT" or "A/B test" with no unit of randomization, timing, or arms named
- The intervention reaches people through a shared channel (one health worker, one classroom, one WhatsApp group), so treated and untreated people would mix
- The program is being rolled out in phases for logistical reasons and the team wants the rollout to double as the test
- The intervention has two or more separable components and the team needs to know which ones matter, not only whether the bundle works

### Do not use it when
- The question is what to measure, against what, and whether the data exist; `plan-evaluation-design` writes that plan and takes this skill's design as an input
- The question is how many people or clusters; `estimate-sample-size` computes that for the design chosen here
- The test runs as a product experiment in Evidential and the tool's fields are the question; `design-evidential-experiment`
- The team wants to find the best of many message variants cheaply with adaptive allocation; `design-adaptive-message-experiment`
- The purpose is to learn whether the program can be delivered at all (recruitment, retention, acceptability) rather than to estimate its effect; `design-pilot-feasibility-study`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The experiment intent: the change being tested, who gets it, the outcome it should move, and the decision the result informs (pilot, scale, policy). The decision sets how precise and how defensible the estimate must be.
2. **Required.** How the intervention travels: can a treated person's neighbor, classmate, fellow patient, or fellow group member be affected through conversation, shared resources, or the same frontline worker? Spillovers rule out individual randomization.
3. **Required.** Rollout and ethics: must every eligible unit receive the program eventually; is there a fixed rollout order or a capacity limit per period; can the program withhold it from some units for the study period, and who decides.
4. **Required.** Control over take-up: can the program assign who receives the treatment, or only who is offered or invited?
5. **Required.** Components: how many separable parts does the intervention have, and does the decision need to know which parts matter?
6. Optional. The number of units at each level (people, clinics, villages, districts), the time available, and the theory of change from `draft-theory-of-change`, which says where the mechanism acts and so where spillovers are likely.

If any of 1 to 5 is missing, ask and stop; each one decides a branch. If 6 is missing, proceed and mark the power implications as unchecked until `estimate-sample-size` runs.

## What it draws on

- Hemming, K., et al. (2015). The stepped wedge cluster randomised trial: Rationale, design, analysis, and reporting. *BMJ*, 350, h391. https://doi.org/10.1136/bmj.h391
- Hayes, R. J., & Moulton, L. H. (2009). *Cluster Randomised Trials*. Chapman & Hall/CRC. https://doi.org/10.1201/9781584888178
- Collins, L. M. (2018). *Optimization of Behavioral, Biobehavioral, and Biomedical Interventions: The Multiphase Optimization Strategy (MOST)*. Springer. https://doi.org/10.1007/978-3-319-72206-1
- EGAP. *10 things to know about cluster randomization*. https://egap.org/resource/10-things-to-know-about-cluster-randomization/
- EGAP. *10 things to know about multisite or block-randomized trials*. https://egap.org/resource/10-things-to-know-about-multisite-or-block-randomized-trials/
- Banerjee, A., Chandrasekhar, A. G., Dalpath, S., Duflo, E., Floretta, J., Jackson, M. O., et al. (2025). Selecting the most effective nudge: Evidence from a large-scale experiment on immunization. *Econometrica*, 93(4), 1183–1223. https://doi.org/10.3982/ECTA19739
- Milkman, K. L., et al. (2021). Megastudies improve the impact of applied behavioural science. *Nature*, 600, 478–483. https://doi.org/10.1038/s41586-021-04128-4

Hayes and Moulton cover cluster randomized trials: when to randomize groups, the loss of power that follows, and the analysis that respects the clustering. Hemming et al. set out the stepped-wedge design: all clusters start untreated and cross over to treatment at randomized times until all are treated; it suits phased rollouts where withholding permanently is unacceptable, but because later periods are more treated than earlier ones, the treatment effect is confounded with time unless time trends are modeled. Collins's MOST framework uses factorial designs to decide which components of a multi-component intervention earn their place; such designs are efficient for main effects because every participant informs every component, and they assume component effects are mostly additive. The EGAP guides cover cluster randomization and blocking (randomizing within strata to improve balance and precision). Two many-arm trials are recorded in the dossier as examples of what large designs make possible: Banerjee et al.'s Haryana immunization experiment with 75 arms, analyzed by aggregating treatment variants with a winner's-curse correction, and Milkman et al.'s 54-intervention megastudy (61,293 people), in which expert forecasts of which arms would win failed. The judgment calls this skill adds, none of them published rules: the constraint-to-design mapping, the requirement to name a runner-up with the condition that would flip the choice, and the rule that the design is chosen before the sample is sized because the sample depends on it.

**WEIRD skew:** The designs are procedural and carry no population content, so `weird` is not-applicable. The constraints that drive the choice are, if anything, more common outside high-income settings: phased rollouts, delivery through shared frontline workers, and small numbers of administrative units. **Non-WEIRD evidence:** the dossier notes that stepped-wedge designs suit the phased rollouts common in LMIC programs (Hemming abstract, per the report), and the Haryana 75-arm experiment (Banerjee et al. 2025) is an Indian field trial; neither is evidence about the designs' validity, which rests on their statistical logic.

**Replication status:** Not applicable in the effect sense; these are design methods. Two known limits stand in for a replication note: stepped-wedge estimates are confounded with secular time trends unless modeled, and factorial designs assume mostly additive component effects, so interactions are poorly powered.

## How to do it

1. **Write the constraints table** from the Before you start answers: spillovers, rollout, withholding, take-up control, components, units available, and the decision. A constraint the user has not stated is marked "unknown", not guessed.
2. **Map each constraint to the designs it rules in or out**, one row per design. Spillovers within a group rule out individual randomization and point to cluster designs. A rollout in which every unit must be treated by a date points to a stepped-wedge, or to a parallel cluster design with a waitlist if the test can finish before the last group is due. No spillovers plus the ability to withhold for the study period points to individual randomization. Several components whose separate value matters point to a factorial, with units set by the spillover answer. Control over the offer only points to an encouragement design, which estimates the effect of the offer on everyone (intention to treat) and, with the assumption that the offer works only through take-up, the effect on those who took up because of it. Many arms whose relative ranking is the question point to `design-adaptive-message-experiment` unless a precise effect per arm is needed.
3. **State the power cost and analysis implications of each surviving design**: individual, none beyond the basics; cluster, the design effect 1 + (m − 1)ρ and the need for enough clusters, with cluster-robust analysis; stepped-wedge, more periods and more measurement, with time modeled; factorial, full-sample main effects under additivity, interactions underpowered; encouragement, a sample that scales with one over the squared take-up difference, and an instrumental-variables analysis.
4. **Choose one design** and write why in terms of the constraints, then **name the runner-up** and the condition that would flip the choice ("if the state will not leave any pharmacy untreated for six months, the stepped-wedge replaces the parallel design").
5. **Specify the structure**: the unit of randomization, the number of arms, the allocation ratio, what to block or stratify on (the strongest unit-level predictor of the outcome), the timing (periods and steps for a stepped-wedge), and how the randomization will be done and witnessed.
6. **Write the ethics note**: how withholding or delaying is justified (genuine uncertainty about the effect, capacity limits, a waitlist that treats everyone by a date) and who signs off.
7. **Write the hand-off**: what `estimate-sample-size` needs (unit, units per cluster, an ICC or the need for one, take-up assumptions, periods) and what `plan-evaluation-design` inherits (the comparison condition and the rollout shape).
8. **Stop here.** Do not size the sample and do not write the measurement plan.

See `references/evidence-notes.md` for the sources and `references/worked-example.md` for a run on HIV self-test kit distribution through pharmacies in Lagos.

## Output template

```markdown
# Trial design choice: <test>

**Decision this informs:** <pilot / scale / policy>
**Intervention and outcome:** <what, for whom, expected to move what>

## Constraints
| Constraint | Answer | Source |
|---|---|---|
| Spillovers | <none / within <group> via <channel> / unknown> | <...> |
| Rollout | <all at once / phased by <capacity> over <time> / unknown> | <...> |
| Withholding | <can withhold from <units> for <period> / must treat all by <date> / cannot withhold> | <...> |
| Control over take-up | <assigns treatment / only the offer> | <...> |
| Components | <n>; decision needs to know which matter: <yes / no> | <...> |
| Units available | <people, clusters at each level, periods> | <...> |

## Designs ruled in or out
| Design | Verdict | Because |
|---|---|---|
| Individual | <in / out> | <constraint> |
| Cluster (parallel) | <in / out> | <...> |
| Stepped-wedge | <in / out> | <...> |
| Factorial | <in / out> | <...> |
| Encouragement | <in / out> | <...> |

## Chosen design: <name>
- Unit of randomization: <...>
- Arms and allocation: <...>
- Blocking or stratification: <variable, why>
- Timing: <periods, steps, dates>
- Randomization procedure: <who draws, how it is witnessed>
- Power cost: <the multiplier or constraint estimate-sample-size must apply>
- Analysis implications: <clustering, time trends, additivity, instrument>
- Ethics of withholding: <justification, who signs off>

## Runner-up: <name>
<what would flip the choice to it>

## Hand-off
- To estimate-sample-size: <unit, m, ICC needed, take-up assumption, periods>
- To plan-evaluation-design: <comparison condition, rollout shape>

## Open questions
- <constraint marked unknown that could change the design>
```

## Where it goes wrong

- **An individual lottery under spillovers.** Randomizing people who share a health worker, a classroom, or a market stall when the treatment travels by word of mouth; contamination pulls the measured effect toward zero and the test "finds nothing".
- **Stepped-wedge as a free lunch.** Choosing it because "everyone gets it" without planning measurement in every period and a time-trend model; the estimate is then confounded with whatever else changed over the rollout.
- **Few clusters.** Six districts, three per arm, is not a trial, however many people live in them; the design effect and the small-sample inference problem both apply. Route to `estimate-sample-size` and expect a verdict of "cannot detect".
- **Factorial for interactions.** A 2×2 design powered for main effects is read as if it could tell whether components work better together; it usually cannot, and the additivity assumption should be stated.
- **Weak encouragement.** An offer that few accept makes the effect on those who took up unestimable in practice; if the take-up difference is small, the design must change, not the claim.
- **A bandit for a scale decision.** Adaptive allocation finds a winning arm cheaply and gives a poor effect estimate; a decision that needs "how much" needs a fixed design.
- **Mistaking a pilot for a test.** A feasibility pilot sized to estimate recruitment and fidelity is not an effect test and should not be labeled one; that is `design-pilot-feasibility-study`.

## When to bring in a specialist

Tell the user to consult an evaluation methodologist or statistician, and where relevant an ethics board and the implementing authority, when:
- Randomization itself is contested ethically or politically (a ministry, community leaders, or a funder objects to withholding or to lotteries); the design question becomes a negotiation about waitlists, phased rollouts, and what counts as genuine uncertainty
- The unit of randomization is a government administrative unit (district, local government area, block); the number of units is small, assignment is politically visible, and the analysis needs small-sample cluster methods
- A stepped-wedge is chosen; the time-trend model and the measurement schedule need a statistician before the first step
- The design is a factorial with more than two components, or an encouragement design with expected take-up below about a third
- Spillovers are themselves the thing to measure (the decision depends on whether effects spread), which needs a design that randomizes the share treated within groups, beyond this skill's scope

Bring them: the constraints table, the chosen design and runner-up, the counts of units at each level, the rollout calendar, and the theory of change.
