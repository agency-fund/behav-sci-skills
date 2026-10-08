---
name: define-key-behavior
description: >-
  Use when a program goal is vague ("increase savings", "build trust in the
  vaccine", "improve engagement") and no specific behavior has been chosen.
  Also use when someone asks "what should we actually be trying to change?"
  or "which behavior are we targeting?", or when several candidate behaviors
  are floating around and the team must commit to one before diagnosis or
  design. Picks one observable behavior stated as who does what, when, scores
  it against the alternatives with APEASE, and keeps the runners-up. Most
  other skills in this library need this output, so run it first. Do not use
  when a specific, observable behavior with a named actor and time window is
  already on the table; take that straight to decompose-comb-barriers. Not
  for explaining why a behavior is not happening, and not for staging a
  digital product's user journey (build-user-funnel).
license: CC-BY-4.0
metadata:
  title: Turn a vague goal into one clear behavior
  type: atomic
  stage: define
  version: "0.1.0"
  status: draft
  authors: "Nikhil Ravichandar, Joe Speed"
  org: IL
  weird: mixed-evidence
  tags: "behavior-change-wheel, apease, behavior-definition"
  consumes: "program-goal, evidence-scan-brief, audience-context-brief"
  produces: "target-behavior-brief"
---

## What it does

Turns one vague program goal into a single observable, measurable behavior, stated as who does what, when.

It generates the candidate behaviors that could plausibly move the goal, scores each against the APEASE criteria plus impact and spillover, selects the winner, and keeps the others as a ranked shortlist with the reason each was set aside. Diagnosis on the top choice sometimes fails, so the shortlist is a documented next option, not waste.

## When to use it

### Use it when
- A program document, funder brief, or stakeholder states the goal as an outcome, attitude, or aspiration rather than a behavior: "increase financial resilience", "improve engagement", "reduce stigma"
- Someone asks "what should we actually be trying to change here?" or "what behavior are we targeting?"
- Several candidate behaviors are floating around informally and the team needs one to commit to before diagnosis or design starts
- A team is about to run a barrier diagnosis or design an intervention on a goal that still has no named actor, action, or time window

### Do not use it when
- A specific, already-observable behavior with a named actor and timeframe is on the table; hand it directly to `decompose-comb-barriers`
- The question is why a defined behavior is not happening; that is diagnosis, also `decompose-comb-barriers`
- The "behavior" is a step in a digital product's journey from first contact to outcome; `build-user-funnel` stages that instead
- The team wants to know what research already exists on the goal; run `assess-evidence-base` on the same goal, ideally before this skill

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The program goal as stated, verbatim if possible, and who stated it (funder, program team, government partner).
2. **Required.** At least a rough population and setting: who the program reaches, where, through what delivery channel, and any known constraints (budget, timeline, what is already built). Without this the "who" of the output is generic and every downstream skill inherits the vagueness. If the user cannot answer, offer to run `map-audience-context` first.
3. Optional. An evidence scan brief from `assess-evidence-base` for this goal. It changes the Effectiveness and Impact scores.
4. Optional. An audience and context brief from `map-audience-context`. It supplies the "who" and "when" of the selected behavior.
5. Optional. Any behaviors the team is already leaning toward, so they can be scored on the same table as the alternatives rather than quietly assumed.

If 1 or 2 is missing, ask and stop. If 3 to 5 are missing, proceed, score Effectiveness and Impact from the method's general priors, and say under "Open questions" that no evidence or context brief was available.

## What it draws on

- Michie, S., Atkins, L., & West, R. (2014). *The Behaviour Change Wheel: A Guide to Designing Interventions*. Silverback Publishing. Chapter 3 (specifying and selecting target behaviors) and pp. 46–48 (the APEASE criteria).
- Michie, S., van Stralen, M. M., & West, R. (2011). The behaviour change wheel: A new method for characterising and designing behaviour change interventions. *Implementation Science*, 6, 42. https://doi.org/10.1186/1748-5908-6-42

The Behavior Change Wheel's "select target behavior" step: generate a reasonably exhaustive list of candidate behaviors that could plausibly achieve the stated goal, then score each against the APEASE criteria (Affordability, Practicability, Effectiveness and cost-effectiveness, Acceptability, Side-effects and safety, Equity) plus impact (how much changing this behavior would move the goal) and spillover (whether changing it makes other useful behaviors more or less likely). The highest-scoring candidate becomes the target; the rest are kept as a ranked shortlist rather than discarded.

Two judgment calls this skill adds to the source. First, candidate generation must not stop at whatever channels or products the input happens to name: an existing app, course, or delivery channel describes what is already built, not the boundary of what counts as a candidate, so at least one candidate must come from outside that infrastructure or the shortlist is just ranking variants of one idea. Second, when an evidence scan brief is available, its "what has been tried" and "findings that do not support the goal" sections must visibly change the Effectiveness and Impact scores; a candidate the evidence already shows underperforms should not score the same as one with no evidence either way. When an audience and context brief is available, its operationalized population and decision moment are what "who" and "when" say in the selected behavior; writing a generic "who" when a specific one is sitting in the input is a regression, not a simplification.

**WEIRD skew:** The selection procedure itself is context-agnostic: it is a prioritization method, not a claim about what motivates people. The worked examples and APEASE weightings in the source literature are drawn overwhelmingly from UK and US public health programs, so treat the procedure as portable and the illustrative priors (which behaviors are usually "high impact", what counts as acceptable) as needing local validation.

**Replication status:** Not applicable in the effect sense: this is a prioritization procedure, not an intervention, so there is no effect to replicate. The Behavior Change Wheel is widely used in intervention development; whether independent teams reach the same APEASE scores for the same candidates has not, to the authors' knowledge, been tested, so treat the scores as structured judgment that makes the reasoning inspectable rather than as measurement.

## How to do it

1. **Restate the goal** verbatim or lightly cleaned, so a reader can see what the behavior was selected to serve.
2. **Generate candidates.** List every behavior that could plausibly move the goal, at least three. Push for candidates a reasonable person could have picked first, not strawmen that make the preferred option win. At least one must sit outside the infrastructure the input names (see "What it draws on"). If the user is already leaning toward one, put it on the table with the others.
3. **Score every candidate** on the eight columns: Affordability, Practicability, Effectiveness, Acceptability, Side-effects/safety, Equity, Impact, Spillover. Each cell is `+`, `-`, or `0` with a one-clause reason; a column of bare symbols does not count as scored. Use the evidence scan brief, if present, to ground Effectiveness and Impact. The table is mandatory for every candidate including the winner; a rationale paragraph is not a substitute.
4. **Select the target** and write it as who, what, when, then as one sentence with no "and". If an audience and context brief is present, its operationalized population and decision moment are the "who" and "when". If the statement needs "and" to describe the action, it is two behaviors; split before going on.
5. **Explain why this one** in two to four sentences that point at the specific cells that decided it, especially the tie-breaker where candidates were close. Do not restate the table.
6. **Rank the shortlist** with one line per runner-up saying why it ranked below the winner, tied to its row.
7. **List open questions and assumptions** the selection had to guess at from limited context, so someone can go and check.
8. **Check the output before returning it.** Is the selected behavior something a specific person could be observed doing at a specific moment, not an outcome ("reduce anemia")? Does every row conveniently favor the same candidate across all eight columns? If so the scoring was reverse-engineered; rescore honestly or say plainly that the table did not drive the choice.

See `references/worked-example.md` for a complete run on a savings program for Nairobi market vendors.

## Output template

```markdown
# Target behavior brief

**Program goal (as given):** <verbatim or lightly cleaned goal statement>

## Candidate scoring

| Candidate behavior | A | P | E | A | S | E | Impact | Spillover |
|---|---|---|---|---|---|---|---|---|
| <candidate 1> | <+/-/0: reason> | <+/-/0: reason> | <+/-/0: reason> | <+/-/0: reason> | <+/-/0: reason> | <+/-/0: reason> | <+/-/0: reason> | <+/-/0: reason> |
| <candidate 2> | ... | | | | | | | |
| <candidate 3, from outside the named infrastructure> | ... | | | | | | | |

(Columns, in APEASE order: Affordability, Practicability, Effectiveness, Acceptability, Side-effects/safety, Equity.)

## Selected target behavior
- **Who:** <actor, e.g. "first-time mothers in program clinics">
- **What:** <single observable action, e.g. "attend the 6-week postnatal check">
- **When:** <window, e.g. "within 6 to 8 weeks of delivery">
- **One-sentence behavior statement:** <Who does What, by When; no "and">

## Why this one
<2 to 4 sentences pointing at the specific table cells that decided it: the tie-breaker reasoning where candidates were close, not a restatement of the table>

## Candidate shortlist (ranked, not discarded)
1. <candidate behavior>: <why it ranked below the selected one, tied to its row above>
2. <candidate behavior>: <why it ranked below the selected one, tied to its row above>

## Open questions / assumptions to check
<anything the selection had to guess at from limited program context, including whether an evidence scan or context brief was available>
```

## Where it goes wrong

- **Compound behaviors slip through.** "Attend antenatal care and adhere to iron supplementation" is two behaviors wearing a trench coat. If the output statement needs "and" to describe the action, split it before passing it downstream; this skill's job is exactly one behavior per run.
- **Outcome dressed up as behavior.** "Reduce anemia" is a health outcome, not something anyone does. If the selected behavior is not something a specific person could be observed doing at a specific moment, it has not been defined yet.
- **Selecting for measurability over impact.** The easiest behavior to observe (app logins) is sometimes prioritized over the behavior that drives the goal (offline saving). APEASE scoring catches this only if Impact is scored honestly rather than deferred to "whatever we can already measure".
- **No real alternatives generated.** A candidate list padded with strawmen so the preferred behavior wins makes the shortlist useless as a fallback. A scoring table filled in after the choice looks identical to one that drove the choice; if every row favors the same candidate across all eight columns, the scoring was reverse-engineered.
- **Anchoring on named infrastructure.** Restating the input's existing products or channels as the only candidates ("deposit into the savings product" versus "open the app") is not alternative generation, even if it yields three distinct rows.
- **Context collapse.** Run on a goal with no population or setting, the output's "who" is generic and every downstream diagnosis inherits the vagueness. Ask for at least a rough population and setting, or run `map-audience-context` first and feed its brief in.

## When to bring in a specialist

Tell the user to consult a behavioral scientist or the program's M&E lead when:
- The top two candidates are close and the tie-breaker rests on an Effectiveness or Impact judgment the team has no evidence for; a short evidence scan or a specialist's read should decide it, not a coin flip
- Any candidate carries clinical, safety, or legal consequences (medication adherence, reporting violence, financial products with downside risk), so the Side-effects/safety column needs domain expertise the table cannot supply
- Stakeholders disagree about what the goal means, so Impact scores differently for the funder and the implementer; selection is then a governance decision, not a scoring one

Bring them: the scoring table with its reasons, the ranked shortlist, and the open questions.
