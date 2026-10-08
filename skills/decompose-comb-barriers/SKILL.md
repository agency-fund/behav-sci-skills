---
name: decompose-comb-barriers
description: >-
  Use when one behavior is already defined (who does what, when) and the
  question is why people are not doing it. Also use when a team is about to
  jump to an intervention ("let's send a reminder text") without naming the
  barrier it addresses, or when several explanations are being asserted
  informally ("maybe they forgot", "maybe it's too expensive") and need to
  become testable hypotheses. Lists competing Capability, Opportunity, and
  Motivation barrier hypotheses (the COM-B model), each with a diagnostic
  question that would confirm or rule it out. Do not use on a goal or
  outcome statement ("improve maternal health"); run define-key-behavior
  first. Not for choosing what to do about a confirmed barrier
  (select-intervention-levers), and not for drop-off between stages of a
  digital product funnel (diagnose-funnel-weak-link).
license: CC-BY-4.0
metadata:
  title: Find out why people are not doing a behavior
  type: atomic
  stage: diagnose
  version: "0.1.0"
  status: draft
  authors: "Nikhil Ravichandar, Joe Speed"
  org: IL
  weird: mixed-evidence
  tags: "com-b, behavior-change-wheel, diagnosis"
  consumes: "target-behavior-brief, bias-audit-report"
  produces: "comb-barrier-hypotheses"
---

## What it does

Lists competing reasons why one defined behavior is not happening, grouped by the COM-B model, each with a question that would show whether it is the real barrier.

COM-B says a behavior occurs when a person has sufficient Capability (can they do it?), Opportunity (does their situation allow it?), and Motivation (do they want to?) at the moment it needs to happen. This skill produces hypotheses and the questions that discriminate between them. It does not produce a diagnosis; that comes from answering the questions in the field.

## When to use it

### Use it when
- A target behavior brief exists (who, what, when) and the next question is "why isn't this happening already?"
- A team is about to jump straight to intervention ideas ("let's send a reminder text") without having named a barrier the intervention is meant to address
- Several plausible explanations for non-behavior are being asserted informally ("maybe they forgot", "maybe it's too expensive", "maybe they don't think it matters") and need organizing into testable, mutually exclusive hypotheses
- Someone asks "what's stopping them?" or "what are the barriers?" about one specific behavior

### Do not use it when
- The input is a goal or outcome statement ("improve maternal health"); a barrier decomposition has nothing concrete to attach to. Run `define-key-behavior` first
- The barrier is already confirmed by field evidence and the question is what to do about it; that is `select-intervention-levers`
- The behavior is a stage transition in a digital product's funnel with observed drop-off numbers; `diagnose-funnel-weak-link` handles that framing
- The team wants to check its own assumptions about the population before diagnosing; run `audit-researcher-bias` first and feed its report in here

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The target behavior as who, what, when. Paste the target behavior brief from `define-key-behavior` if one exists, or state the behavior at that level of specificity. If the statement contains "and" or lacks an actor or time window, say so and send it back for splitting or definition before continuing.
2. **Required.** What is already known about the context: the setting, the delivery channel, and anything the team has observed or heard from the population so far, even informally. This feeds the "context support" column of the ranking.
3. Optional. A bias audit report from `audit-researcher-bias`. Its flagged assumptions become hypotheses to test, not barriers to assume.
4. Optional. What field access the team has (interviews, observation, administrative data, nothing yet), which sets the "field cost" column.

If 1 is missing, ask and stop. If 2 is missing, ask once; if the answer is still thin, proceed and mark every "context support" cell as "no context available". If 3 and 4 are missing, assume no audit was run and that a short round of interviews is feasible.

## What it draws on

- Michie, S., van Stralen, M. M., & West, R. (2011). The behaviour change wheel: A new method for characterising and designing behaviour change interventions. *Implementation Science*, 6, 42. https://doi.org/10.1186/1748-5908-6-42
- Michie, S., Atkins, L., & West, R. (2014). *The Behaviour Change Wheel: A Guide to Designing Interventions*. Silverback Publishing. Chapter 2 (COM-B and its diagnostic questions).

The COM-B model: behavior (B) occurs when a person has sufficient Capability (psychological: knowledge, skills, ability to self-regulate; physical: strength, stamina, dexterity), Opportunity (physical: time, resources, location; social: norms, sanction, support from others), and Motivation (reflective: beliefs, intentions, evaluations; automatic: habit, emotion, impulse) at the moment the behavior needs to occur. Because the three components are constructed to be jointly exhaustive, a rigorous decomposition should be able to state at least one hypothesis per sub-component even if some are quickly ruled out. The discipline is in naming what would distinguish a real barrier from a plausible-sounding one, not in generating the longest list. One hypothesis per sub-component is a floor, not a ceiling: if two genuinely distinct, non-trivial hypotheses compete for the same sub-component, list both rather than merging or dropping one to fit a one-bullet shape.

Every candidate Capability hypothesis must pass the persistence test before it is placed: would this barrier persist even if the environment fully supported the person (full information, full access, no social cost)? If yes, it is Capability. If no, if the person would be fine once the environment changed, it is Opportunity, not Capability, however much it resembles "doesn't know how" or "doesn't understand". This is the most common mislabel in COM-B application, which is why the output template makes showing the check mandatory.

If a bias audit report is available (from `audit-researcher-bias`), cross-check its flagged assumptions against the hypothesis list: a flagged prior that quietly reappears as a hypothesis needs its own diagnostic question like any other, not a pass on the strength of already having been named. A flagged prior becoming a hypothesis without independent field evidence relocates the bias rather than checking it.

**WEIRD skew:** COM-B is presented as a universal model of behavior (its three components are meant to be exhaustive by construction, not culturally contingent), but the diagnostic question bank and worked examples in the source literature skew toward UK health-behavior contexts. The Opportunity (social) sub-component in particular tends to need the most local adaptation: what counts as socially sanctioned or normal varies more than the framework's examples suggest.

**Replication status:** COM-B is a classification framework rather than an effect, so there is no effect to replicate. It is widely used, and its components are constructed to be jointly exhaustive. The persistence test this skill makes mandatory is a practitioner rule from this skill's authors, not a published criterion; it targets the Capability versus Opportunity mislabeling the authors see most often in practice.

## How to do it

1. **Carry the target behavior over verbatim** at the top of the output, so the hypotheses are visibly attached to one who, what, when.
2. **Write at least one hypothesis per sub-component** (Capability physical and psychological, Opportunity physical and social, Motivation reflective and automatic). Each must be specific enough to produce a question that could rule it out; "lack of motivation" is not a hypothesis yet. Where two genuinely distinct hypotheses compete for one sub-component, list both.
3. **Run the persistence test on every Capability hypothesis** and write the answer on its line: would it persist with full information, access, and no social cost? If the honest answer is no, move the hypothesis to Opportunity. A Capability hypothesis without a persistence-test line is incomplete.
4. **Write a diagnostic question for each hypothesis**, then a "discriminates because" line stating the different answer each hypothesis predicts. If the question would get the same answer whichever hypothesis is true, it is a survey item, not a diagnostic; change the question, not the write-up.
5. **If a bias audit report is present, cross-check it.** Any flagged prior that reappears as a hypothesis gets its own diagnostic question; mark it as a flagged prior so the reader knows it entered on assumption, not evidence.
6. **Score every hypothesis** on two criteria in the ranking table: context support (does existing context make this more or less likely, and why) and field cost (how cheap and fast is its diagnostic question to run). A ranking with no visible scoring is indistinguishable from an unexamined first guess.
7. **Name the top one or two provisional barriers** from that table, in one to three sentences, flagged clearly as provisional until the diagnostic questions are answered in the field.
8. **Stop there.** Do not choose levers or interventions; the confirmed barrier is the input to `select-intervention-levers`, and the confirmation happens in the field, not in this output.

See `references/worked-example.md` for a complete run on the Nairobi market-vendor savings behavior.

## Output template

```markdown
# COM-B barrier hypotheses

**Target behavior:** <who + what + when, carried over verbatim>

## Capability
### Physical
- **Hypothesis:** <specific barrier, e.g. "lacks the physical skill to complete the form unassisted">
  **Persistence test:** <would this persist with full information, access, and social support? state the answer and why>
  **Diagnostic question:** <question whose answer would confirm or rule this out>
  **Discriminates because:** <the different answer this hypothesis predicts versus the other hypotheses in this document>
### Psychological
- **Hypothesis:** <e.g. "can't translate general awareness into a plan that fits their specific, variable schedule">
  **Persistence test:** <...>
  **Diagnostic question:** <...>
  **Discriminates because:** <...>

## Opportunity
### Physical
- **Hypothesis:** <e.g. "the clinic is only open during work hours">
  **Diagnostic question:** <...>
  **Discriminates because:** <...>
### Social
- **Hypothesis:** <e.g. "attending would signal something the person wants to avoid signaling">
  **Diagnostic question:** <...>
  **Discriminates because:** <...>

## Motivation
### Reflective
- **Hypothesis:** <e.g. "doesn't believe the behavior will produce the promised benefit">
  **Diagnostic question:** <...>
  **Discriminates because:** <...>
### Automatic
- **Hypothesis:** <e.g. "a competing habitual behavior crowds out the window to act">
  **Diagnostic question:** <...>
  **Discriminates because:** <...>

## Most likely barrier(s), pending diagnostic answers

| Hypothesis | Context support (does existing context make this more or less likely, and why) | Field cost (how cheap and fast is its diagnostic question to run) |
|---|---|---|
| <hypothesis 1> | <...> | <...> |
| <hypothesis 2> | <...> | <...> |

<1 to 3 sentences naming the top 1 or 2 hypotheses by that table, flagged as provisional until the diagnostic questions are answered in the field; not a restatement of an intuition the table was not used to reach>
```

## Where it goes wrong

- **Motivation as a dumping ground.** It is easy to label every unexplained non-behavior "lack of motivation" because it requires no further evidence. If a hypothesis cannot be stated specifically enough to produce a diagnostic question that could rule it out, it is not a real hypothesis yet.
- **Capability/Opportunity confusion.** "Doesn't know how" (Capability) and "was never told" (Opportunity, if the information was never made available) get mislabeled constantly, including by careful attempts, which is why the persistence-test line is mandatory rather than left as background judgment. A Capability hypothesis whose persistence-test answer is "no, they'd be fine if the environment changed" is a mislabeled Opportunity hypothesis, however the sentence is worded.
- **Non-discriminating questions.** A diagnostic question that would get the same answer regardless of which hypothesis is true is just a survey item. If the "discriminates because" line cannot name a different predicted answer per hypothesis, the question needs to change.
- **Running on a compound or vague behavior.** If the input still contains "and" or lacks a clear who, what, when, the barriers produced will quietly diagnose whichever half of the behavior was easiest to picture, not the behavior as specified.
- **Treating the ranked barriers as confirmed.** This skill produces hypotheses and the questions to test them, not a diagnosis. Passing the "most likely barrier" straight to intervention design without answering the diagnostic questions in the field skips the step the questions exist for.
- **Relocating a flagged prior.** A bias audit flagged "it's a discipline problem"; the decomposition lists "lacks self-regulation" under Capability with no question that could rule it out. The prior has moved, not been tested.

## When to bring in a specialist

Tell the user to consult a behavioral scientist or an experienced qualitative researcher when:
- The behavior involves clinical, safety, or legal risk (medication, violence, child protection, sexual health), because some diagnostic questions cannot be asked directly and the question set itself needs ethical review before fieldwork
- The hypotheses cluster under Opportunity (social) in a context the team does not know well; norms and sanction vary most across settings, and a local researcher should shape the questions and who asks them
- The field round comes back with two hypotheses both supported; the next step is a sharper discriminating study designed by someone who does this for a living, not a judgment call from the table

Bring them: the hypothesis list with its discrimination lines, the ranking table, and whatever field answers already exist.
