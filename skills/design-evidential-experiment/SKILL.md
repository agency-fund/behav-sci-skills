---
name: design-evidential-experiment
description: >-
  Use when a team wants to test one specific change, such as a new message
  or reminder timing, with a randomized experiment in Evidential, the free
  open-source experiment engine built for nonprofits. Also use when someone
  is staring at Evidential's create-experiment form unsure what the fields
  mean (strata, MDE, balance threshold), or is about to ship a change to
  everyone "to see if it helps". Makes every design decision the tool asks
  for: experiment type, arms, randomization unit, eligibility, primary and
  guardrail metrics, detectable effect, sample size, stopping rule, and how
  each arm is delivered, concretely enough to enter into the tool as it
  stands. Do not use for a full-scale impact RCT with enumerator-managed
  arms; that is Level 4, for plan-evaluation-design plus an independent
  evaluator. Do not use to find something to test; run
  diagnose-funnel-weak-link first. Not for deciding which evaluation level
  a product has earned (choose-ai-eval-level).
license: CC-BY-4.0
metadata:
  title: Design an experiment in Evidential
  type: atomic
  stage: test
  version: "0.1.0"
  status: draft
  authors: "Joe Speed"
  org: IL
  weird: likely-generalizes
  tags: "ai-eval, evidential, experimental-design, funnel"
  consumes: "experiment-intent, funnel-weak-link-hypotheses, evaluation-design"
  produces: "experiment-configuration"
---

## What it does

Turns one testable idea into a complete experiment configuration for Evidential, detailed enough to enter into the tool as it stands.

It decides the experiment type, the arms, what is randomized, who is eligible, the primary and guardrail metrics, the effect size to detect, the sample size, when to stop, and how each arm is delivered. Evidential is the free, open-source experiment engine built by IDinsight and The Agency Fund for nonprofits; it automates randomization and analysis but delivers nothing, so the brief has to cover delivery too.

## When to use it

### Use it when
- A change is about to be shipped to everyone at once "to see if it helps" when the population, delivery channel, and data warehouse would support randomizing it
- `diagnose-funnel-weak-link` has produced a surviving hypothesis whose cheapest honest test is an experiment
- `choose-ai-eval-level` has recommended Level 2 or Level 3 evaluation and the team's experimentation stack is Evidential
- A team is staring at Evidential's create-experiment form unsure what half the fields (strata, MDE, balance threshold) should contain; the decisions belong upstream of the form, which is where this skill sits
- Someone asks "how do we set up an A/B test for this?" or "what should the arms and sample size be?"

### Do not use it when
- The question is a full-scale impact RCT with enumerator-managed arms and full counterfactuals; Evidential's documentation says it is not built for that, and it is Level 4 territory for `plan-evaluation-design` plus an independent evaluator
- The team has nothing specific to test yet; an experiment without a mechanism hypothesis produces a significant-or-not answer to a question nobody asked. Run `diagnose-funnel-weak-link` first
- The team is deciding which evaluation level the product has earned; that is `choose-ai-eval-level`
- The question is the cost-effectiveness of the program as a whole; `plan-evaluation-design`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The experiment intent: the change or variant being considered, who it would apply to, what the team expects it to move, and the decision the result will inform.
2. **Required.** Data infrastructure: is there a BigQuery, Postgres, or Redshift warehouse with a clean participants table and a unique, non-identifying id per participant? Which fields exist for eligibility filters and metrics? Without this the brief is a plan for later, not a launch configuration, and the output must say so.
3. **Required.** Delivery capacity: can the program actually deliver each arm's treatment (for example, route a WhatsApp journey by arm)? Evidential returns assignments; it does not deliver treatments.
4. **Required.** Population shape: a known finite roster already in the warehouse, or open enrollment with new participants appearing over time? This decides the experiment type.
5. Optional. Funnel weak-link hypotheses from `diagnose-funnel-weak-link`. If present, the experiment must test a named hypothesis, and the primary metric is the funnel transition that hypothesis predicts will move.
6. Optional. An evaluation design brief from `plan-evaluation-design`. If present, carry its locked primary outcome and minimum effect worth detecting into the metrics section instead of inventing new ones.
7. Optional. The current baseline value of the candidate primary metric and the program's decision threshold (the smallest effect the team would act on).

If 1 to 4 are missing, ask and stop. If 5 and 6 are missing, say the hypothesis and effect size come from the intent alone and flag them as unconfirmed by a diagnosis. If 7 is missing, ask for the baseline once; never fall back silently to the tool's default effect size.

## What it draws on

- IDinsight & The Agency Fund (2025). Evidential: a free, open-source experiment engine built by and for nonprofits. Documentation and API design specification. Apache-2.0 (backend). https://docs.evidential.dev/
- Wu, Z., On, R., Walsh, J., Korley, E., Madon, T., & Wong, L. (2025). AI Evaluation in the Social Sector: A Living Playbook. Repeatable Motions, Motion 04: running experiments with rigor and speed. The Agency Fund. https://eval.playbook.org.ai/motions

Evidential is the experiment engine named by the AI Evaluation Playbook's Motion 04 as the tooling that "help[s] teams automate randomization, track real-time results, and reduce analysis bottlenecks." The design brief mirrors the tool's actual design spec, so every section lands on a real field rather than a vague intention.

- **Experiment type** is Evidential's first fork. `freq_preassigned` samples participants from the warehouse and assigns them up front, with stratified randomization and a pre-launch balance check. `freq_online` assigns arms in real time as new participants appear, with no stratification and no balance check. The adaptive family (`mab_online`, `mab_online_dwh`, `cmab_online`) runs Thompson-sampling bandits that optimize allocation rather than estimate effects precisely. The skill's rule of thumb, taken from the tool's own structure: a known finite population means preassigned; open enrollment means online; "find the best arm cheaply, precise effect size not needed" means bandit.
- **Arms** number 2 to 20, with optional weights summing to 100, the first arm being control. **Eligibility filters** use `includes`, `excludes`, or `between` on flagged participant fields. The **randomization unit** is individual (`primary_key`) or cluster (`cluster_key` plus a desired cluster count, for treatments that spill over within groups). **Strata** apply to preassigned designs only.
- **Metrics** are each a flagged numeric or boolean warehouse field with either a relative `metric_pct_change` or an absolute `metric_target` to detect. Evidential defaults power to 0.8 and alpha to 0.05 and, if the team declines to choose, sets the target effect to baseline × 0.1. This skill treats that last default as a red flag, not a convenience: the detectable effect must come from the program's decision threshold (the evaluation design brief's minimum effect worth detecting, when one exists), echoing the discipline `plan-evaluation-design` enforces.
- **Analysis** is intent-to-treat OLS with strata and pre-treatment outcome values as controls. **Delivery is the client's job**: Evidential has no feature flags. It returns assignments (CSV, REST, or webhook) and the program must map each `arm_name` to an actual treatment path, such as a WhatsApp journey. An experiment with no delivery mapping randomizes nobody into anything.
- **Close-out**: Evidential records a `decision` and an `impact` rating per experiment, doubling as the organization's experiment registry, so the brief must state the decision rule before launch.

Judgment call the sources do not fully specify: guardrail metrics. Evidential permits up to 150 metrics; this skill mandates exactly one primary metric plus a small named set of guardrails (metrics that must not degrade), because a many-primary experiment re-imports the which-number-moved problem that pre-specification exists to kill.

**WEIRD skew:** Evidential was built for social-sector deployments; its early partners run programs in India and across Africa, so the tooling assumptions are already aware of non-WEIRD settings (WhatsApp delivery integration, preassigned designs for populations that are often offline). What it does assume is data infrastructure: a BigQuery, Postgres, or Redshift warehouse with a clean participant table, and client-side capacity to deliver each arm's treatment. Where those are missing, the brief this skill produces is a plan for later, not a launch configuration.

**Replication status:** Not applicable in the effect sense: this skill encodes a tool's design specification and a playbook motion, not an empirical effect. The statistical defaults it carries (power 0.8, alpha 0.05, intent-to-treat OLS with strata controls) are standard experimental practice. The field names and type distinctions are Evidential's and will change as the tool does, so check the brief against the current documentation before entering it.

## How to do it

1. **State the hypothesis under test** verbatim from the weak-link hypothesis or the intent statement. "Variant B is better" is not a hypothesis; name the mechanism the change is supposed to act on.
2. **Write the decision rule before anything else**: what the team will do on a positive, a null, and a negative result. This is what gets entered at close-out as Evidential's `decision`.
3. **Choose the experiment type** with the rule of thumb: known finite population means `freq_preassigned` (warehouse sample, stratified randomization, pre-launch balance check); open enrollment means `freq_online` (real-time assignment, no stratification, no balance check); "find the best arm cheaply, precise effect size not needed" means the bandit family (`mab_online`, `mab_online_dwh`, `cmab_online`). Do not pick a bandit when the team needs a defensible effect estimate for a scale decision.
4. **Set the randomization unit.** Individual (`primary_key`) unless the treatment travels within groups by word of mouth or shared delivery, in which case cluster (`cluster_key` plus the desired cluster count) and say why.
5. **Define the arms** (2 to 20, control first, weights if unequal), the **eligibility filters** (field, relation, value on flagged participant fields), and the **strata** for a preassigned design (or n/a for online).
6. **Choose exactly one primary metric**: a flagged numeric or boolean warehouse field. For a funnel-sourced hypothesis it is the transition the hypothesis predicts will move; if an evaluation design brief exists, it is that brief's locked outcome. Set the detectable effect as `metric_pct_change` or `metric_target` from the program's decision threshold, and say where the threshold came from. Treat the tool's default of baseline × 0.1 as a red flag, never as a convenience.
7. **Name the guardrail metrics**: a small set that must not degrade, each with its direction. Everything else is exploratory and labeled as such.
8. **Work the power inputs**: power (default 0.8), alpha (default 0.05), baseline, required n from the power check against available n and enrollment rate. Set the stopping rule (`end_date`, `target_n`, or manual) and write down the commitment not to peek and stop early on an interim p-value, especially for an online design with no balance check.
9. **Write the delivery integration**: the `arm_name` to delivery-path mapping, who builds it, and how assignment is fetched (CSV, REST assignment endpoint, or webhook). If this section is empty, the experiment does not exist.
10. **Write the analysis plan**: ITT via Evidential's OLS with strata and pre-treatment controls; the balance-check expectation for preassigned, or its absence for online and the small-sample imbalance risk that implies; who reads results and when, and that they record the `decision` and `impact` in the registry.
11. **Add the data and ethics notes**: the participants table and unique id, no personally identifying information in ids, and the consent or notification posture for being experimented on, per the organization's policy.
12. **Check the brief against the Before you start answers.** If the warehouse or delivery capacity is missing, label the output a plan for later and route the infrastructure gap to the data team.

See `references/worked-example.md` for a complete run testing a first-question menu in a WhatsApp agronomy assistant.

## Output template

```markdown
# Experiment configuration brief

**Hypothesis under test:** <mechanism being tested, carried verbatim from the weak-link hypothesis or intent; not "variant B is better">
**Decision rule:** <what the team will do on a positive, null, or negative result, written before launch>

## Design
| Field | Value | Why |
|---|---|---|
| Experiment type | freq_preassigned / freq_online / mab_* | <population + goal rationale> |
| Randomization unit | individual (primary_key) / cluster (cluster_key) | <spillover reasoning> |
| Arms | <name + one-line description each; control first; weights if unequal> | |
| Eligibility filters | <field, relation, value: who is in> | |
| Strata | <fields, preassigned only> or n/a | |
| Start / end | <dates> | |

## Metrics
**Primary:** <one warehouse field; for a funnel-sourced hypothesis, the transition it predicts will move>, detectable effect <pct_change or target>, sourced from <program threshold / evaluation design brief>, not the tool's baseline × 0.1 default.
**Guardrails:** <named metrics that must not degrade, with direction>

## Power & stopping
<power (default 0.8), alpha (default 0.05), required n from the power check vs available n; stopping rule: end_date / target_n / manual, and the commitment not to peek-and-stop early on a p-value>

## Delivery integration
<how each arm becomes a real treatment: the arm_name → delivery-path mapping, who builds it, and how assignment is fetched (CSV / REST assignment endpoint / webhook). If this section is empty the experiment does not exist.>

## Analysis plan
<ITT via Evidential's OLS with strata + pre-treatment controls; balance check expectation for preassigned (or its absence for online, and the small-sample imbalance risk that implies); who reads results and when>

## Data & ethics notes
<participants table + unique id; no PII in ids; consent/notification posture for being experimented on, per org policy>
```

## Where it goes wrong

- **Shipping the tool's default effect size.** Accepting baseline × 0.1 because the field auto-filled. A detectable effect that no decision hangs on produces a study that is powered, significant, and useless: the same failure `plan-evaluation-design` polices, re-imported through a form field.
- **Bandit envy.** Choosing a bandit because "adaptive sounds efficient" when the team needs a defensible effect estimate for a scale decision. Bandits allocate toward winners; they answer "which arm" cheaply, not "how much better, with what confidence".
- **The unmapped arm.** A committed experiment whose treatment arm no system actually delivers. Evidential returns assignments and nothing more; a missing arm-to-journey mapping means both arms silently get control. The delivery section's "if empty, the experiment does not exist" line is load-bearing.
- **Individual randomization under spillover.** Randomizing farmers within cooperatives when the treatment travels by word of mouth; contamination shrinks the measured effect toward null. If the treatment is discussable, the unit is the cluster.
- **Metric sprawl.** Fifteen "primary-ish" metrics, one of which will clear p < 0.05 by luck. One primary, named guardrails, everything else exploratory and labeled, or the registry entry is bait for hypothesizing after the results are known.
- **Peeking at online experiments.** Stopping a `freq_online` experiment the first week the dashboard shows a star. With no balance check and small interim n, that star is noise more often than signal.
- **Out of scope: no warehouse, no delivery capacity, or Level 4 questions.** Without a queryable participant table (or for pure in-person delivery), and for cost-effectiveness-of-the-program questions, this brief can only document aspiration. Route infrastructure gaps to the data team and impact questions to `plan-evaluation-design`.

## When to bring in a specialist

Tell the user to consult a statistician or an independent evaluator when:
- The design randomizes clusters (cooperatives, clinics, villages) and nobody can estimate the intraclass correlation; the required number of clusters can be several times what an individual-level power check suggests
- A bandit is being considered for a decision with real stakes (what to scale, what to fund); bandits allocate toward winners and do not give a defensible effect estimate
- Participants would be experimented on without notification, the treatment touches health, money, or safety, or the organization has no consent policy to point to; an ethics reviewer should see the data and ethics section before launch
- The question has drifted into Level 4 (does the program improve the development outcome, and at what cost?); Evidential is not built for that, and `plan-evaluation-design` plus an external evaluator is the route

Bring them: the hypothesis and decision rule, the design table, the power inputs with the baseline and its source, and the participants table schema.
