---
name: map-audience-context
description: >-
  Use when a program describes its audience only with a broad label, such as
  "smallholder farmers" or "first-time mothers", and says nothing about their
  real setting. Also use before define-key-behavior writes its "who", or when
  someone asks "who exactly are we talking about, and where does this
  decision actually happen for them?" It names a specific group, the moment
  they make the decision, and the channels that already reach them. It also
  flags assumptions carried over from wealthy Western settings, including
  who holds decision authority. Do not use when the decision moment and
  existing channels are already documented at this level of detail; hand
  that straight to define-key-behavior. Not for dividing a population into
  segments or personas, and not for proposing new channels, which is
  intervention design (select-intervention-levers, draft-lever-content).
license: CC-BY-4.0
metadata:
  title: Map your audience and their setting
  type: atomic
  stage: define
  version: "0.1.0"
  status: draft
  authors: "Joe Speed"
  org: IL
  weird: mixed-evidence
  tags: "east, contextual-inquiry, cultural-psychology"
  consumes: "program-goal"
  produces: "audience-context-brief"
---

## What it does

Replaces a broad audience label with a specific, observable group of people at the moment they make the decision the program cares about.

It names the channels that already reach that group today and flags assumptions carried over from wealthy Western settings that nobody has checked locally, including the assumption that the named person is the one who decides. Every claim carries a source label, so a reader can tell direct observation from general knowledge about the country or sector.

## When to use it

### Use it when
- A program goal names its population only the way a funder or stakeholder would ("smallholder farmers", "gig workers", "first-time mothers") with no detail on where, when, or how the target behavior choice actually gets made
- Before `define-key-behavior` writes its "who", or when an existing target behavior brief's "who" still just restates the funder's language
- Someone asks "who exactly are we talking about, and where does this decision actually happen for them?"
- A team is about to assume bank accounts, smartphones, literacy, or individual decision-making for a population nobody on the team has observed

### Do not use it when
- The decision moment and existing channels are already documented at this level of detail; this skill's job is done, hand the documentation straight to `define-key-behavior` instead of re-running it
- The real need is "which of several groups should we target"; that is segmentation into behaviorally distinct personas, a different job, and this skill characterizes one population's context in depth
- The team wants to propose a channel for a future intervention; a channel that does not currently reach the population belongs to `select-intervention-levers` and `draft-lever-content`, not to this map
- The question is what the published literature says about this population; that is `assess-evidence-base`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The program goal as stated, plus whatever is known about the target population and setting. This is the same raw input `define-key-behavior` and `assess-evidence-base` take; this skill can run in parallel with either.
2. **Required.** Where the team's knowledge of this population comes from: direct observation (field visits, which sites), reports from someone who lives it, or general literature about the country or sector. Every section of the output carries a source label, and an unsourced specific claim is indistinguishable from an invented one.
3. Optional. Any assumptions the input already makes about infrastructure (bank access, phones, connectivity, literacy) or about who decides (the individual, a spouse, a household head, a group).
4. Optional. Whether the population plausibly contains groups with different decision moments (men and women, urban and rural, itinerant and fixed), so the operationalization can narrow honestly.

If 1 is missing, ask and stop. If 2 is missing, ask once; if the user does not know, label every claim "general literature about this country or sector" and say so in Open questions. If 3 and 4 are missing, proceed and route the resulting gaps to Open questions.

## What it draws on

- Service, O., Hallsworth, M., Halpern, D., Algate, F., Gallagher, R., Nguyen, S., Ruda, S., & Sanders, M. (2014). *EAST: Four Simple Ways to Apply Behavioural Insights*. The Behavioural Insights Team.
- Beyer, H., & Holtzblatt, K. (1997). *Contextual Design: Defining Customer-Centered Systems*. Morgan Kaufmann Publishers, Ch. 3.
- Datta, S., & Mullainathan, S. (2014). Behavioral design: A new approach to development policy. *Review of Income and Wealth*, 60(1), 7–35.

EAST's "Timely" and "Easy" dimensions only mean something once the actual physical and social moment the behavior choice occurs in is known, not a generic description of the audience's demographics. Contextual inquiry's discipline of describing an environment as actually observed, rather than as reported secondhand by a stakeholder who does not live in it, applies to every section of the output, not just channels. The output template requires a source (directly observed, reported by someone who lives it, or general literature about the country or sector rather than this specific population) for the decision moment and constraints, as it does for channels. Datta and Mullainathan's account of behavioral design in development programs is the basis for the mandatory WEIRD-default check, and that check is not limited to infrastructure. The WEIRD framing's "individualism" component means that who has decision authority is itself a common default: treating the named population as the autonomous decision-maker, when a household or group actually holds that authority, is as much a WEIRD default as assuming a bank account or a smartphone, and the assumption check must consider it explicitly.

When the input only supports a broad, honest operationalization (a whole state or region, not a named district or market), narrow to the most specific subgroup the input actually supports and route the remaining breadth to Open questions. Do not invent a specific place, clinic, or market the input never named just to look more specific. A narrower-than-warranted guess that turns out wrong is worse than an honestly scoped population with the gap named.

**WEIRD skew:** EAST was developed and validated primarily in UK public-sector contexts, and contextual inquiry as a method originated in Western commercial product design. The technique this skill operationalizes (describe the actual decision moment and existing channels rather than working from a funder's abstract label) exists specifically as a check against assuming a WEIRD-default context. Treat the discipline as portable and the source literature's worked examples as needing local replacement, not extension.

**Replication status:** Not applicable in the effect sense: this is a description discipline, not an intervention. EAST summarizes trial evidence from the UK government context into four principles; contextual inquiry is a design practice with no replication literature. What this skill asks a reader to trust is the source labeling on each claim, not an effect.

## How to do it

1. **Restate the goal** verbatim or lightly cleaned.
2. **Operationalize the population.** Write the funder's label verbatim, then the narrowest subgroup the input actually supports: age range, role, site, pattern of activity. If the input only supports something broad, say so here and route the gap to Open questions rather than naming a place the input never mentioned.
3. **Describe the decision moment**: the specific physical and social moment the behavior choice is made, not a general time of day, and who else is present or influential at that moment. Attach a source label: directly observed, reported by someone who lives it, or general literature about the country or sector.
4. **List existing channels and touchpoints**, real and not proposed, each with how you know it reaches this population and its reach or frequency if known. A channel that would be convenient for a future intervention but does not currently reach the population belongs to intervention design, not here.
5. **State environmental constraints at the decision moment**: physical, social, or economic, with a source label.
6. **Run the WEIRD-default assumption check**, mandatory even when the answer is "none found". Cover two kinds of default: infrastructure (banking, literacy, connectivity, formal institutions) and decision authority (the named person treated as autonomous when a spouse, elder, household, or group holds go or no-go power). For each, say whether it is confirmed locally and what to check before relying on it.
7. **Write Open questions**: everything the brief had to infer from limited context, flagged for someone to go and check rather than presented as settled, including any site the brief could not confirm.
8. **Check before returning:** Does any section restate the label with a longer sentence around it? Is any channel one that does not exist yet? Is any specific claim unsourced? Does the brief divide the population into personas rather than describe one group? Fix each.

See `references/worked-example.md` for a complete run on a savings program for Nairobi market vendors.

## Output template

```markdown
# Audience and context brief

**Program goal (as given):** <verbatim or lightly cleaned goal statement>

## Population, as named versus as operationalized
- **As named in the input:** <the funder or stakeholder's label, verbatim>
- **Operationalized:** <the narrowest subgroup the input actually supports, e.g. "women aged 25 to 50 running fixed daily produce stalls in two named markets", not "smallholder farmers" generally. If the input only supports a broad operationalization, say so here and route the specific gap to Open questions rather than naming a place, clinic, or market the input never mentioned.>

## Decision moment
- **Where and when the behavior choice actually gets made:** <the specific physical and social moment, not a general time of day>. **Source:** <directly observed / reported by someone who lives it / general literature about this country or sector, not this specific population>
- **Who else is present or influential at that moment:** <...>

## Existing channels and touchpoints (real, not proposed)
- <channel or touchpoint already reaching this population today, with how you know it reaches them>: <reach or frequency, if known>
- <channel 2>: <...>

(A channel that would be convenient for a future intervention but does not currently reach this population belongs to intervention design later, not to this context map.)

## Environmental constraints at the decision moment
<physical, social, or economic constraints specific to that moment>. **Source:** <...>

## WEIRD-default assumption check (mandatory; state "none found" explicitly if genuinely none)
- <assumption in the input that defaults to Western, formal, literate, or connected infrastructure, OR to the named population being the autonomous decision-maker when a household or group may hold that authority instead>. **Confirmed locally?** <yes / no / unknown>. **What to check before relying on it:** <...>

## Open questions / what still needs field confirmation
<anything this brief had to infer from limited program context, flagged for someone to actually go and check rather than presented as settled>
```

## Where it goes wrong

- **Restating the label.** Repeating "smallholder farmers" or "gig workers" verbatim as the operationalized population is not context; it is the same abstraction with a longer sentence around it.
- **Inventing channels.** Listing a channel that would be convenient for a future intervention (a WhatsApp group that does not exist yet) as if it already reaches this population conflates context mapping with intervention design.
- **Single-anecdote context.** Treating one interview, one field visit, or one team member's assumption as if it characterizes the whole population's decision moment. Flag it as a gap in Open questions rather than presenting it as settled.
- **Unflagged WEIRD defaults.** Assuming banking, literacy, or connectivity infrastructure that has not been confirmed for this specific population, and not naming it in the assumption check, silently imports a different context than the one being mapped.
- **Autonomy default.** Treating the named population as the individual, autonomous decision-maker by default, when a household, spouse, or elder actually holds go or no-go authority, is a WEIRD default just as much as an infrastructure assumption, and the easiest one to miss, since it is not on any checklist of physical requirements.
- **Fabricated specificity.** Narrowing to a named district, clinic, or market the input never mentioned, in order to satisfy the "operationalized" section's specificity bar, is worse than an honestly broad operationalization with the gap named. A wrong specific claim misleads with false confidence; a flagged gap does not.
- **Unsourced claims.** A decision-moment or constraint description with no stated source reads identically whether it came from direct observation or from general knowledge about the country or sector. The Source field exists so a reader can tell which, and weight it accordingly.
- **Confusing this with segmentation.** This skill characterizes one population's context in depth; it does not divide a population into multiple behaviorally distinct personas. If the real need is "which of several groups should we target", that is a different job; do not force this skill to do both.

## When to bring in a specialist

Tell the user to consult a local researcher, an anthropologist or sociologist who knows the setting, or someone from the population itself when:
- Decision authority is unknown and the behavior touches household resources, health, fertility, or gendered norms; a wrong autonomy default here derails every downstream skill, and only someone from or close to the population can answer it
- Every claim in the brief is sourced from general literature and nobody on the team has observed the setting; the brief is then a hypothesis list, and a field visit or local researcher should come before `define-key-behavior`
- The input plausibly covers groups with different decision moments (men and women, urban and rural, fixed and itinerant) and does not support narrowing; a segmentation decision is needed first, and this skill cannot make it

Bring them: the brief with its source labels, the WEIRD-default check, and the Open questions list.
