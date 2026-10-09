---
name: select-intervention-levers
description: >-
  Use when field research has confirmed the main reason a behavior is not
  happening and the team needs to decide what to do about it. Also use when
  someone asks "given that this is the barrier, what could we actually do?"
  or is about to jump to an intervention idea ("let's send a text") without
  grounding it in the barrier's COM-B component. Uses the Behavior Change
  Wheel, a published framework that links each type of barrier to the
  intervention functions that can address it, to shortlist interventions,
  score them for practicality with APEASE, and break the best one into a
  specific behavior change technique. Do not use when the barrier is still
  an untested hypothesis; confirm it in the field first using the diagnostic
  questions from decompose-comb-barriers. Not for writing the actual message
  or script (draft-lever-content), and not for values-affirmation exercises
  (draft-values-affirmation).
license: CC-BY-4.0
metadata:
  title: Choose interventions for a confirmed barrier
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Joe Speed"
  org: IL
  weird: mixed-evidence
  tags: "behavior-change-wheel, behavior-change-techniques, apease"
  consumes: "barrier-diagnosis, comb-barrier-hypotheses"
  produces: "intervention-levers"
---

## What it does

Shortlists the types of intervention that can address one confirmed barrier, using the Behavior Change Wheel's published linkage table rather than open brainstorming.

It scores each eligible intervention function for feasibility with APEASE, selects one, and breaks it down into a specific behavior change technique, because a function name ("Environmental restructuring") is a category of mechanism, not something a team can implement. The functions that lose on feasibility are kept as the next thing to try if the selected one fails a pilot.

## When to use it

### Use it when
- Field diagnostic questions from `decompose-comb-barriers` have been answered and one hypothesis is confirmed as the actual barrier
- Someone asks "given that this is the barrier, what could we actually do about it?"
- A team is about to jump straight to an intervention idea ("let's send a text") without grounding it in the barrier's COM-B component
- A pilot of one lever has failed and the team wants the next lever to try for the same confirmed barrier

### Do not use it when
- The barrier list is still unconfirmed hypotheses; a lever selected for the wrong barrier is a wasted pilot. Confirm the barrier in the field first, using the diagnostic questions from `decompose-comb-barriers`
- The lever is chosen and the team needs the actual words, script, or signage; that is `draft-lever-content`
- The intended intervention is a values-affirmation exercise; `draft-values-affirmation` owns that protocol end to end
- No barrier has been diagnosed at all and the question is why the behavior is not happening; run `decompose-comb-barriers`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The one confirmed barrier, stated verbatim, with its COM-B sub-component (e.g. Opportunity/social) and the field evidence that confirmed it: which diagnostic question was asked and what the answers were. If the user offers the whole hypothesis list with none confirmed, say so and stop; this skill runs on one confirmed barrier.
2. **Required.** The target behavior and population the barrier belongs to (who, what, when), so the technique can be made concrete.
3. **Required.** What the implementer controls: budget range, channels, staff, partners, and anything that needs a third party's permission. This drives the Affordability and Practicability scoring.
4. Optional. The full COM-B hypothesis set from `decompose-comb-barriers`, so rejected functions can be positioned against the other hypotheses if the pilot fails.
5. Optional. Whether the source table (Michie, van Stralen & West, 2011, Table 2) is at hand to check cell by cell, which sets the confidence markers.

If 1 is missing or the barrier is unconfirmed, ask and stop. If 2 or 3 is missing, ask once; if still missing, proceed and mark every Practicability cell as "assumed, implementer constraints unknown". If 4 and 5 are missing, assume the table is not at hand and mark linkage confidence accordingly.

## What it draws on

- Michie, S., van Stralen, M. M., & West, R. (2011). The behaviour change wheel: A new method for characterising and designing behaviour change interventions. *Implementation Science*, 6, 42 (see Table 2). https://doi.org/10.1186/1748-5908-6-42
- Michie, S., Richardson, M., Johnston, M., et al. (2013). The Behavior Change Technique Taxonomy (v1) of 93 hierarchically clustered techniques. *Annals of Behavioral Medicine*, 46(1), 81–95.
- Michie, S., Atkins, L., & West, R. (2014). *The Behaviour Change Wheel: A Guide to Designing Interventions*. Silverback Publishing, pp. 46–48 (APEASE criteria).

The Behavior Change Wheel names nine intervention functions (Education, Persuasion, Incentivization, Coercion, Training, Restriction, Environmental restructuring, Modeling, Enablement) and publishes a matrix (Michie, van Stralen & West, 2011, Table 2) linking each COM-B sub-component to the functions theoretically capable of changing it. That matrix must be consulted directly for the confirmed barrier's specific sub-component. Reconstructing it from general impression or memory is exactly the kind of plausible-but-wrong shortcut this skill exists to prevent: a barrier's sub-component (e.g. Opportunity/social) determines which functions are even eligible before feasibility is considered at all. APEASE scoring (the same criteria `define-key-behavior` uses) narrows the eligible functions to one selection. The Behavior Change Technique Taxonomy (BCTTv1) exists because a selected function is not yet implementable: it names a category of mechanism, not an action. The output must name a specific BCT, or it has not specified a lever yet.

One judgment call this skill adds to the source: where the published table is not at hand to check cell by cell, each function listed must carry an explicit confidence marker (high, applied with strong recall of the actual table; lower, applied from general impression), rather than presenting every function with the same unearned certainty. Low-confidence entries are to be verified against the source before the brief is treated as final.

**WEIRD skew:** The COM-B-to-function linkage matrix is presented as a mechanistic, theory-driven mapping rather than a cultural claim: which function could plausibly work follows from which COM-B component the barrier sits in, not from a population's cultural background. What is WEIRD-skewed is the Behavior Change Technique Taxonomy's validation base and worked examples, drawn overwhelmingly from UK and US health-behavior interventions. Treat a selected function as portable and a specific BCT's assumed delivery mechanism (a clinic visit, a printed leaflet) as needing local adaptation.

**Replication status:** The linkage matrix and the taxonomy are frameworks, not effects, so there is no effect to replicate. The BCTTv1 was built through an international consensus exercise and is widely used to code interventions; whether a given technique works for a given barrier in a given setting is an empirical question each pilot answers for itself, which is why the output keeps the rejected functions as the next thing to try.

## How to do it

1. **Carry the confirmed barrier over verbatim**, including its COM-B sub-component and the field evidence that confirmed it. If the sub-component was never named, name it now using the persistence test from `decompose-comb-barriers`; eligibility depends on it.
2. **Read the eligible functions off the published matrix** (Michie, van Stralen & West, 2011, Table 2) for that exact sub-component. Do not brainstorm. For each function, state in one clause why its mechanism matches this sub-component per the matrix.
3. **Mark confidence on every linkage.** If the table is at hand, check cell by cell and say so. If not, mark each function high confidence or lower confidence, and tell the user to verify low-confidence entries against the source before treating the brief as final.
4. **Score each eligible function on APEASE** (Affordability, Practicability, Effectiveness, Acceptability, Side-effects/safety, Equity), each cell `+`, `-`, or `0` with a one-clause reason. Score Practicability against what the implementer actually controls: a function that needs infrastructure, authority, or a partner's cooperation the implementer does not have gets a negative, not a hopeful zero.
5. **Select the top function** and state the tie-breaker reasoning by pointing at specific cells.
6. **Break the selected function into one concrete BCTTv1 technique**, by number and name, and describe how it would apply to this barrier and population. "Environmental restructuring" is a category; "12.1 Restructuring the physical environment: install a partition at the kiosk" is a lever.
7. **Keep the rejected functions** with why each scored poorly; they are the next lever to try if the selected one fails a pilot, not discards.
8. **List open questions** that need field or pilot confirmation before the technique is finalized (permissions, partner cooperation, cost).

See `references/worked-example.md` for a complete run on the Nairobi market-vendor savings barrier.

## Output template

```markdown
# Intervention lever brief

**Confirmed barrier:** <the one hypothesis that fieldwork confirmed, carried over verbatim, including which COM-B sub-component it belongs to and the evidence that confirmed it>

## Applicable intervention functions
<per the BCW's COM-B-to-function linkage matrix (Michie, van Stralen & West, 2011, Table 2) for this specific sub-component>
- <function 1>: <why this function's mechanism matches this sub-component, per the matrix>. **Confidence this linkage is correct:** <high: applied directly from the published table / lower: applied from general recall, verify against the source before finalizing>
- <function 2>: <...>. **Confidence:** <...>

## Feasibility scoring (APEASE)
| Function | A | P | E | A | S | E |
|---|---|---|---|---|---|---|
| <function 1> | <+/-/0: reason> | | | | | |
| <function 2> | ... | | | | | |

(Columns: Affordability, Practicability, Effectiveness, Acceptability, Side-effects/safety, Equity.)

## Selected lever
**Function:** <top-scoring function>. <tie-breaker reasoning, pointing at specific table cells>
**Concrete technique (BCTTv1):** <a specific, numbered, named technique, not a restated function>. <how it would concretely apply to this barrier and population>

## Rejected functions
<functions the matrix linked to this sub-component but that scored poorly on feasibility, with why; kept as the next lever to try if the selected one fails a pilot, not discarded>

## Open questions
<what needs field or pilot confirmation before the selected technique is finalized>
```

## Where it goes wrong

- **Free-brainstormed levers.** Generating candidate levers from intuition instead of the published COM-B-to-function matrix defeats the point. The matrix exists because not every function is theoretically capable of changing every kind of barrier, and skipping it risks selecting one that cannot work by construction.
- **Function without technique.** Stopping at a function name ("Environmental restructuring") without naming a specific BCT is not yet a lever; it is a category. Someone still has to decide what changes.
- **Feasibility blind spots.** Selecting a function that requires infrastructure, authority, or a partner's cooperation the implementer does not have, without that showing up as a negative Practicability score, produces a lever that looks selected but cannot be piloted.
- **Running on an unconfirmed hypothesis.** Selecting levers for a barrier that diagnostic questions have not confirmed risks designing for the wrong problem; the confirmed-barrier input exists specifically to prevent this.
- **Function/technique conflation.** Treating "Environmental restructuring" and "install a partition" as interchangeable labels for the same thing loses the distinction the BCTTv1 exists to enforce: one is a category covering many possible techniques, the other is one specific instance.
- **Unearned certainty.** Listing every applicable function with the same confident tone regardless of how well the specific matrix cell is actually recalled misrepresents a guess as a sourced fact. The mandatory confidence marker exists so a reader knows which functions need checking against Table 2 before the brief is final.

## When to bring in a specialist

Tell the user to consult a behavioral scientist, and where relevant the program's legal or safeguarding lead, when:
- The eligible functions include Coercion or Restriction, or the Incentivization candidate involves payments or penalties; these carry ethical, legal, and backfire risks that an APEASE row cannot settle alone
- The confirmed barrier sits outside the program's authority (a policy, a provider's process, a market rule), so every feasible function needs a partner's cooperation; a specialist can judge whether advocacy or partnership is the real lever rather than a behavior change technique
- The barrier was confirmed on thin evidence (one interview round, a single site) and the pilot will be costly; a specialist can say whether another diagnostic round is cheaper than a wrong pilot
- Low-confidence matrix linkages decide the selection and no one on the team can check Table 2

Bring them: the confirmed barrier with its evidence, the applicable-functions list with confidence markers, the APEASE table, and the open questions.
