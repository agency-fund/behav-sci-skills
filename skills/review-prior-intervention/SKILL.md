---
name: review-prior-intervention
description: >-
  Use when a team has a written record of a program it already tried and
  must decide whether to retry it, change it, or drop the idea. Also use
  when someone says "we tried this before and it didn't work" as if that
  settles whether the idea is bad, or before re-running define-key-behavior
  or assess-evidence-base on a goal the team has a history with. Compares
  what was planned with what happened, judges whether the idea or its
  delivery failed (or whether the data cannot tell), and checks the team's
  explanation against the data it actually collected. A written record is
  required; memory alone is not enough. Do not use to design the next
  attempt; that is intervention design (select-intervention-levers). Not for
  scanning the external literature on what others have tried
  (assess-evidence-base), and not for auditing the team's beliefs about the
  population before any attempt (audit-researcher-bias).
license: CC-BY-4.0
metadata:
  title: "Review a past program: bad idea or bad delivery?"
  type: atomic
  stage: analyze
  version: "0.1.0"
  status: draft
  authors: "Joe Speed"
  org: IL
  weird: mixed-evidence
  tags: "process-evaluation, implementation, pre-mortem"
  consumes: "prior-intervention-record"
  produces: "intervention-post-mortem"
---

## What it does

Turns a team's account of a past intervention into a structured review that separates what was planned from what was actually done.

It judges whether the idea or its delivery failed, or whether the data cannot yet tell, and checks the team's own explanation for the outcome against the data that was actually collected. It is descriptive: it surfaces what happened and what remains ambiguous, so whoever designs the next attempt starts from the record rather than the story.

## When to use it

### Use it when
- A team has a documented account of a prior attempt and is about to decide to retry, adapt, or abandon the underlying idea based on that account alone
- Before `assess-evidence-base` or `define-key-behavior` re-run on the same program goal, so the team's own history is checked rather than silently repeated (retrying an approach that failed for implementation reasons) or silently ignored (abandoning an idea that was never actually tested)
- Someone says "we tried this before and it didn't work" as if that settles whether the idea itself is bad
- A funder or board asks why a previous pilot failed and the team's answer is a story rather than a reading of the data

### Do not use it when
- There is no actual record of what happened; vague recollection with no documented fidelity, dose, reach, or outcome data gives this skill nothing to structure. Ask the team to write down what they remember first, even informally, then come back
- The team wants to design the next attempt; that is intervention design (`select-intervention-levers` for a confirmed barrier, `draft-lever-content` for the content)
- The question is what the external literature says about this kind of intervention; `assess-evidence-base`
- The team wants to check its beliefs about the population before any attempt; `audit-researcher-bias`, which can consume this skill's brief

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The written record of the prior intervention: what was planned (target behavior, mechanism, intended delivery), what the team believes happened, and why they believe it succeeded or failed. If the only source is memory, with no document, notes, logs, or data, stop and ask the team to write down what they remember first, even informally.
2. **Required.** What data was actually collected: delivery logs, attendance, administrative outcomes, surveys, informal observations. For each source, whether it was tracked systematically or noticed anecdotally.
3. Optional. Anything on fidelity, dose, reach, or context that the record does not already contain, such as delivery logs the team has not yet looked at.
4. Optional. The decision this review will inform (retry as is, adapt, abandon) and roughly what a retry would cost, since that sets how much weight a "cannot yet tell" verdict can bear.

If 1 is missing, ask and stop. If 2 is missing, ask once; if the team genuinely has no data, proceed, and say up front that the classification will almost certainly be "cannot yet tell". If 3 and 4 are missing, assume the record is all there is and that a retry is moderately costly.

## What it draws on

- Moore, G. F., Audrey, S., Barker, M., et al. (2015). Process evaluation of complex interventions: Medical Research Council guidance. *BMJ*, 350, h1258.
- Durlak, J. A., & DuPre, E. P. (2008). Implementation matters: A review of research on the influence of implementation on program outcomes. *American Journal of Community Psychology*, 41(3-4), 327-350.

The MRC's process evaluation framework treats fidelity (was it delivered as designed), dose (how much of it actually reached people), reach (what share of the intended population was exposed), and context (what changed in the delivery environment) as the dimensions that separate "did we actually do the thing" from "did the thing work". A program can fail on any of the first three while the underlying idea remains untested. Durlak and DuPre's finding that implementation quality substantially moderates outcomes is why "the idea failed" is never a conclusion this skill lets stand without first checking those four dimensions; a null result with thin fidelity, dose, or reach data supports "cannot yet tell", not "the idea doesn't work". The causal-claim check applies the same falsifiability discipline `audit-researcher-bias` applies to fresh assumption statements, here to a team's story about why a past attempt succeeded or failed.

**WEIRD skew:** The implementation-versus-idea-failure distinction is a general evaluation-methodology point, not a claim about any specific population; it applies to judging any program, anywhere. What is WEIRD-skewed is the MRC framework's own worked examples and evidence base, drawn overwhelmingly from UK health-service interventions. Treat the four-dimension structure (fidelity, dose, reach, context) as portable and the specific thresholds or worked cases in the source literature as needing local judgment.

**Replication status:** Not applicable in the effect sense: the implementation-versus-idea distinction is an evaluation principle, not an intervention. Durlak and DuPre (2008) is a review of a large body of studies finding that implementation quality is consistently associated with program outcomes; the MRC guidance (Moore et al., 2015) is a consensus framework rather than an empirical finding.

## How to do it

1. **Condense the record** at the top, verbatim or lightly cleaned, so a reader can see what the review is a review of.
2. **Write what was planned:** the intervention as originally designed, with its target behavior, mechanism, and intended delivery.
3. **Write what was actually implemented** on the four MRC dimensions: fidelity, dose, reach, context. Every bullet carries a **Basis** marker: confirmed by the record, or inferred and not directly stated. The record stating a scheduling choice's reason ("the hall was only available at 2pm") does not confirm that reason as the cause of a downstream outcome (low attendance) unless the record separately connects them.
4. **Record the outcome as observed,** with a confidence qualifier: a systematically tracked metric and a single informal observation are not equally strong evidence, so say which this is.
5. **Run the causal claim check.** Quote or closely paraphrase the team's stated reason for the outcome; say whether the collected data supports it (yes, no, or partially, naming the specific data point); and name an alternative explanation the data does not rule out.
6. **Classify:** implementation failure, idea failure, or cannot yet tell. Give this equal weight with the planned-versus-implemented section; it is not a formality tacked on at the end. A null result with thin fidelity, dose, or reach data supports "cannot yet tell", and the detail accumulated above must not create pressure toward a firmer conclusion than the data supports. A specific but approximate figure ("roughly 15%") is enough for a firm classification on its own dimension; it is a thin-data case only when the dimension needed to decide is genuinely undocumented, not merely imprecise.
7. **List factors to address before any retry,** descriptively. Name what this review surfaced as unaddressed, for whoever designs the next attempt to work from. Do not redesign.
8. **Stop there.** If the team is about to re-define the behavior or audit its own assumptions, hand this brief to `define-key-behavior` or `audit-researcher-bias` as input; the causal claim check is what the latter cross-checks.

See `references/worked-example.md` for a complete run on a daily SMS medication-reminder program.

## Output template

```markdown
# Intervention post-mortem brief

**Prior intervention (as given):** <verbatim or lightly cleaned account>

## What was planned
<the intervention as originally designed: target behavior, mechanism, intended delivery>

## What was actually implemented
- **Fidelity:** <was it delivered as designed, or did the actual delivery diverge, and how> **Basis:** <confirmed by the record / inferred, not directly stated>
- **Dose:** <how much of it actually reached people: frequency and intensity actually delivered versus what was planned> **Basis:** <confirmed / inferred>
- **Reach:** <what share of the intended population was actually exposed to it> **Basis:** <confirmed / inferred>
- **Context:** <what changed in the delivery environment relative to what was assumed when it was designed; do not present a plausible cause for a downstream outcome as confirmed unless the record itself connects them> **Basis:** <confirmed / inferred>

## Outcome as observed
<what data was actually collected, with a confidence qualifier: a single informal observation and a systematically tracked metric are not equally strong evidence, state which this is>

## Causal claim check
- **Team's stated reason for the outcome:** <verbatim or closely paraphrased>
- **Does the collected data actually support this claim?** <yes / no / partially; name the specific data point that does or does not support it>
- **Alternative explanation the data doesn't rule out:** <...>

## Implementation failure vs. idea failure (mandatory classification)
<state which this looks like, given the fidelity, dose, reach, and context findings above, or state "cannot yet tell" explicitly if that data is too thin to distinguish them. A specific but approximate figure (e.g. "roughly 15%") is enough to support a firm classification on its own dimension; it is a thin-data case only when the dimension needed to decide is genuinely undocumented, not merely imprecise>

## Factors to address before any retry
<descriptive, not a redesign: what this post-mortem surfaced as unaddressed, for whoever designs the next attempt to work from>
```

## Where it goes wrong

- **Implementation/idea conflation.** Concluding "the idea doesn't work" from an outcome that a fidelity, dose, and reach check would show was never actually delivered as designed. This is the central failure the skill exists to prevent, and the worked example is a direct illustration of it.
- **Unchecked causal story.** Accepting the team's stated reason for the outcome without checking it against what data was actually collected. A plausible-sounding story is not evidence, even when the team believes it sincerely.
- **One post-mortem treated as universal.** Applying a single retrospective's conclusions to a future attempt in a materially different context (different population, delivery channel, timeframe) without re-checking whether the same factors apply.
- **Prescribing a redesign.** This skill surfaces what happened and why it is or is not ambiguous; it does not design the next intervention. A post-mortem that jumps to "here's what we should build instead" has drifted into intervention design, a different skill's job.
- **Forced classification on thin data.** Picking "implementation failure" or "idea failure" when fidelity, dose, reach, and context data are too sparse to distinguish them is less honest than stating "cannot yet tell". A firm-sounding wrong classification is worse than an admitted gap.
- **Plausible cause smuggled in as fact.** Writing a plausible explanation for a scheduling or delivery choice's effect ("the 2pm slot conflicted with market hours") into the Context bullet without a Basis marking it as inferred makes an unchecked hypothesis read exactly like an established finding. It is the same problem the causal-claim check exists to catch, relocated one section earlier.

## When to bring in a specialist

Tell the user to consult a process or implementation evaluator, and where relevant an independent evaluator or statistician, when:
- The record is thin on fidelity, dose, or reach and the retry would be expensive or large-scale; a specialist can design the process-evaluation measures the retry needs so that the next null result is interpretable
- The outcome involved harm or a serious adverse event (health, safety, financial loss), where attributing the result to the idea or to delivery has consequences for participants and the review needs an independent reader
- The team's causal story is contested within the organization or with a funder; an independent evaluator reading the same data is more credible than this brief
- The prior attempt was a formal evaluation (an RCT or quasi-experiment) and the question is whether the analysis itself was sound; that is a statistician's review, not a process read

Bring them: the record, every delivery log and outcome dataset, and this brief with its Basis markers.
