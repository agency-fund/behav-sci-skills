---
name: audit-researcher-bias
description: >-
  Use when a research team hasn't written down its own beliefs about why its
  audience behaves as it does, or has written them down and wants them
  checked before they shape a diagnosis. It flags beliefs that can't be
  tested as worded, that assume a wealthy Western audience as the norm, or
  that name no evidence that would change the team's mind. Run it at the
  start of a project, right before decompose-comb-barriers, and again before
  major design work. It points out bias; people must correct it. Do not use
  when the question is what published research says about the population
  (assess-evidence-base) or how a past attempt went (review-prior-intervention).
  Not a debiasing plan or training program: it surfaces assumptions, it does
  not fix thinking.
license: CC-BY-4.0
metadata:
  title: Check your team's assumptions about the audience
  type: atomic
  stage: diagnose
  version: "0.1.0"
  status: draft
  authors: "Joe Speed"
  org: IL
  weird: untested-outside-weird
  tags: "confirmation-bias, debiasing, researcher-calibration"
  consumes: "researcher-assumptions, intervention-post-mortem"
  produces: "bias-audit-report"
---

## What it does

Flags the problems in a research team's stated beliefs about why its audience behaves as it does, before those beliefs quietly become barrier hypotheses.

Three problems in particular: beliefs that cannot be tested as worded, beliefs that assume a wealthy Western audience as the implicit norm, and beliefs with no named observation that would change the team's mind. It also flags where experience with one population is being transferred to another. Every flag comes with a rewrite or a follow-up question. The skill surfaces; it does not correct, and a completed audit is not evidence the flagged assumption was fixed.

## When to use it

### Use it when
- A project is starting and the research team has not yet written down what it already believes about why the target population behaves as it does, before looking at any data
- Right before `decompose-comb-barriers` runs, so its barrier hypotheses can be checked against what the researchers believed going in rather than silently reproducing it
- Periodically during a long project, at each major diagnosis or design phase; priors drift and harden over time, so this is meant to be re-run, not done once at kickoff
- Someone on the team says "we already know why they don't do it" and nobody has asked what would prove that wrong

### Do not use it when
- The team expects a fixed intervention, training plan, or debiasing program out the other end; a skill that both surfaces a researcher's biases and prescribes how to fix their thinking is two skills, and this one only does the former
- The question is what the external evidence says about the population; that is `assess-evidence-base`. Running only this audit and treating the population as evidenced leaves the actual evidence gap unaddressed
- The team wants to know whether a past attempt failed on the idea or on delivery; `review-prior-intervention` checks that causal story against the data collected, and its brief can then feed this audit
- The "assumptions" are about the audience's context (channels, decision moment, infrastructure) rather than the team's beliefs about why people behave as they do; `map-audience-context` handles those

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The team's own short, honest answers to three fixed prompts, given before looking at any diagnostic data on the actual target population: (a) What do you already believe is causing the behavior gap? (b) Which population have you personally worked with most, and how similar is it to this one? (c) What observation would change your mind? If the user has not answered these, give them the three prompts in this form and wait. The audit can only work on what is actually stated.
2. Optional. An intervention post-mortem brief from `review-prior-intervention` for this or a related program, so causal stories already found unsupported can be cross-checked against the fresh statement.
3. Optional. Where the project is (kickoff, before diagnosis, before design), which sets the re-audit trigger.
4. Optional. Who wrote the statement and who will read the flags. If the same person does both, the output should say so.

If 1 is missing, ask and stop. If 2 to 4 are missing, assume no post-mortem exists, the project is at kickoff, and the statement has a single author who is also the reader; say the last of these in the report.

## What it draws on

- Klayman, J. (1995). Varieties of confirmation bias. *Psychology of Learning and Motivation*, 32, 385–418.
- Lilienfeld, S. O., Ammirati, R., & Landfield, K. (2009). Giving debiasing away: Can psychological research on correcting cognitive errors promote human welfare? *Perspectives on Psychological Science*, 4(4), 390–398.

Klayman's account of confirmation bias: people do not just fail to seek disconfirming evidence, they often cannot specify what disconfirming evidence would even look like, because the belief was never stated in falsifiable form. The self-audit's fixed prompts are built to force that specification. Asking not just "what do you believe?" but "what would change your mind?" and "what is the most similar population you have actually worked with?" surfaces both the belief and its evidentiary basis (or lack of one) in the same pass. Lilienfeld and colleagues' review of debiasing training is the basis for treating this as a structuring and surfacing exercise rather than a correction exercise. Their finding is that durable debiasing needs deliberate practice against specific, named errors, not a one-off warning; a single audit report does not produce that practice, it gives the team something concrete to practice against.

If an intervention post-mortem brief is available (from `review-prior-intervention`), its "Causal claim check" already tested one causal story against actual data. Cross-check the fresh assumption statement against it: a belief the post-mortem already found unsupported, restated here as if newly being examined, is the same unaudited assumption reappearing under a new label, not independent evidence.

**WEIRD skew:** The debiasing and metacognition literature this skill draws on is itself drawn overwhelmingly from WEIRD research populations and settings (Henrich, J., Heine, S. J., & Norenzayan, A. (2010). The weirdest people in the world? *Behavioral and Brain Sciences*, 33(2-3), 61–83), a pointed irony for a skill about checking researchers' own priors. The technique (forcing falsifiability and a named disconfirming observation) is general-purpose, but treat its effectiveness as unvalidated outside the populations the source studies were run on, as any other skill in this library would be required to.

**Replication status:** Confirmation bias itself is well replicated across many experimental paradigms; Klayman's paper reviews several varieties. Whether a one-off surfacing exercise of this kind changes what a team then does is not established. Lilienfeld and colleagues' review is why this skill expects durable debiasing to need repeated, specific practice rather than one audit, and why the re-audit trigger is mandatory.

## How to do it

1. **Carry the assumption statement over verbatim** at the top of the report, so every flag can be checked against the exact wording.
2. **Test each belief for falsifiability.** Ask what observation could contradict it as currently worded. If almost any observation could be redescribed to fit it, flag it as unfalsifiable and write a rewrite: a version of the same belief that some specific, obtainable observation could actually contradict.
3. **Look for default-to-WEIRD priors.** Name the implicit norm each belief assumes (salaried income, nuclear-household decision-making, individual rather than collective choices, literacy, formal banking) and the specific local fact that would confirm or override that norm for the actual target population.
4. **Check the "what would change your mind?" answer.** Quote it, or write "none given" if the prompt was not answered concretely. Where the answer is vague or requires proof of intent that cannot be observed, flag the downstream risk: a belief nobody specified how to disprove never gets tested.
5. **Assess population-transfer risk.** Record the most similar population the researcher has personally worked with, their stated similarity to the target population, and what is different enough between the two that experience with one may not transfer.
6. **If a post-mortem brief is present, cross-check it.** A causal story its "Causal claim check" already found unsupported by data, restated here as a fresh belief, gets flagged as the same unaudited assumption, not as new input.
7. **Give every flag a next step.** Each flagged assumption needs a concrete rewrite or a concrete follow-up question. A flag with no actionable next step is a criticism, not an audit. If nothing in the statement is flaggable, say so in one line and sanity-check whether the statement was specific enough to audit at all; a "no flags" result should be rare.
8. **Set the re-audit trigger**: before diagnosis begins, before design begins, or after a stated number of weeks or major findings. Note if the statement's author is also the sole reader of the flags.

See `references/worked-example.md` for a complete run on a savings program for Nairobi market vendors.

## Output template

```markdown
# Researcher bias self-audit

**Assumption statement (as given):** <verbatim>

## Unfalsifiable assumptions
- <assumption, quoted or closely paraphrased>. **Why unfalsifiable:** <what observation could never contradict it as currently worded>. **Rewrite as falsifiable:** <a version of the same belief that some specific, obtainable observation could actually contradict>

## Default-to-WEIRD priors
- <assumption>. **Implicit norm assumed:** <e.g. assumes salaried income, nuclear-household decision-making, individual rather than collective financial choices>. **What to check locally:** <the specific local fact that would confirm or override this norm for the actual target population>

## No named disconfirming observation
- <assumption>. **"What would change your mind?" answer given:** <verbatim, or "none given" if the prompt was not answered concretely>. **Risk:** <what happens downstream if this belief is never actually tested because no one specified how it could be wrong>

## Population-transfer risk
- <assumption>. **Most similar population the researcher has personally worked with:** <as stated>. **Stated similarity to target population:** <as stated>. **Gap risk:** <what is different enough between the two that experience with one may not transfer>

## Re-audit trigger
<when this should be re-run for this project, e.g. before diagnosis begins, before design begins, or after a stated number of weeks or major findings>
```

## Where it goes wrong

- **Performative self-awareness.** Answering the prompts with what sounds appropriately humble ("I could be wrong about anything") rather than a specific, checkable belief produces a statement with nothing real to flag. The audit can only work on what is actually stated; vague humility is no more auditable than vague certainty.
- **Treating a completed audit as a resolved bias.** This skill's output is a flag list, not evidence the flagged assumption was corrected. Passing "audited" straight to intervention design as if the flagged priors are now neutralized skips the field-testing the diagnostic skill and the disconfirming observations are meant to prompt.
- **One-time use on a multi-month project.** Priors harden and new ones form as a project proceeds. An audit run once at kickoff and never again will miss the assumptions that calcified during diagnosis itself. The re-audit trigger field exists so this is not left to memory.
- **Auditor and subject as the same unchecked person.** If the person running this skill is also the sole author of the assumption statement, with no one else reviewing the flags, self-serving under-flagging is possible and will not be visible in the report. Where feasible, have a second team member read the flagged report against the original statement.
- **Confusing this with the target-population evidence base.** This skill audits the researcher's priors; it does not survey external evidence on the population. That is `assess-evidence-base`. Running only this one and treating the population as evidenced leaves the actual evidence gap unaddressed.
- **Relabeled post-mortem claim.** A causal story already checked and found unsupported by `review-prior-intervention` can resurface here as a "fresh" assumption if no one cross-checks it. Flag it as the same unaudited belief, not as independent input.

## When to bring in a specialist

Tell the user to consult a local researcher, or an external behavioral scientist not on the team, when:
- The flagged assumptions concern a population nobody on the team is from or close to, so the "what to check locally" items cannot be answered by another round of self-report; a local researcher has to answer them
- The beliefs concern clinical, legal, or stigmatized matters (mental health, violence, sexuality, substance use), where the disconfirming observation the audit calls for cannot be ethically collected by the team itself
- The statement's author is also the sole reader of the flags on a project with real stakes; an external reader should check the flag list against the original statement before it goes into `decompose-comb-barriers`

Bring them: the verbatim statement, the flag list with its rewrites and follow-up questions, and the re-audit trigger.
