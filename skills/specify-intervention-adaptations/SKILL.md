---
name: specify-intervention-adaptations
description: >-
  Use when an intervention is being changed, on purpose or by the people
  delivering it, and someone asks "is this still the same program?", "the
  field team dropped the follow-up call, does that matter?", or "we're taking
  this to a new district, what do we need to change?". Also use when a
  scale-up, a cost cut, or a new delivery partner is altering what was
  tested, or when fidelity monitoring shows delivery drifting from the
  design. Logs each modification using the FRAME (Wiltsey Stirman, Baumann
  and Miller 2019) and checks it against the intervention's core components,
  the parts that carry the mechanism; for a planned transfer to a new context
  it follows the ADAPT guidance (Moore et al. 2021). Do not use to write the
  baseline description of the intervention as tested; that is
  draft-intervention-description. Not for the indicators that detect drift
  (design-fidelity-monitoring), and not for judging whether a published
  finding fits your setting before any test
  (assess-evidence-transferability).
license: CC-BY-4.0
metadata:
  title: Track changes to a tested intervention
  type: atomic
  stage: implement
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "implementation-science, implementation, process-evaluation"
  consumes: "intervention-description, intervention-draft"
  produces: "adaptation-record"
---

## What it does

Records each planned or unplanned modification to an intervention in a structured log, checking it against the core components that carry the intervention's mechanism.

Core components are the parts of an intervention that carry its mechanism, so that removing one removes the reason it works; the adaptable periphery is everything else (language, timing, format, messenger, venue), which can change to fit a context without changing why the intervention works. This skill writes down the core components first, then logs every modification with who made it, when, what changed, why, and whether the mechanism survived. The log is the record a scale-up, an evaluation, or a post-mortem reads to know what was actually delivered. It does not write the baseline description, and it does not design the monitoring that catches drift.

## When to use it

### Use it when
- Someone asks "is this still the same program?", "can we cut this part?", or "does it matter that the field team changed that?"
- A scale-up, a cost cut, or a new delivery partner is changing what was tested, and the team wants to know which changes are safe
- A fidelity monitoring round shows delivery differing from the design and nobody has written down how
- The intervention is moving to a new population, setting, language, or delivery system and the team is planning what to change before it goes
- An evaluation is about to report and the team cannot say which version of the intervention the data describes

### Do not use it when
- There is no written description of the intervention as tested; `draft-intervention-description` writes the baseline this skill measures changes against
- The question is what indicators and sampling would detect drift during delivery; `design-fidelity-monitoring`, which feeds its findings back here as unplanned modifications
- The question is whether a published finding from elsewhere fits your setting before any test; `assess-evidence-transferability`
- A past program failed and the team wants to know whether delivery or the idea failed; `review-prior-intervention`, which can read this skill's log
- The team wants to design a new intervention rather than modify a tested one; `select-intervention-levers`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The baseline: the intervention as tested, from `draft-intervention-description` or the intervention draft, with the theory of change or the technique skill that produced it. If no written baseline exists, stop and send the user to `draft-intervention-description`.
2. **Required.** The core components, each with the mechanism it carries. If the team cannot name them, derive them from the theory of change in step 1 and mark them provisional.
3. **Required.** The modifications to record: proposed (planned) or already observed (unplanned), each with who decided or did it, when, and the stated reason, as far as known.
4. Optional. Whether this is a transfer to a new context (population, setting, language, delivery system), which switches on the ADAPT path.
5. Optional. Fidelity monitoring data from `design-fidelity-monitoring`, which supplies unplanned modifications the team may not have noticed.

If 1 is missing, ask and stop. If 2 is missing, derive provisionally and say so. If 3 is missing, ask once; if the user wants the log opened before any change exists, produce the core-component list and an empty log. If 4 and 5 are missing, assume no context transfer and no monitoring data.

## What it draws on

- Wiltsey Stirman, S., Baumann, A. A., & Miller, C. J. (2019). The FRAME: An expanded framework for reporting adaptations and modifications to evidence-based interventions. *Implementation Science*, 14, 58. https://doi.org/10.1186/s13012-019-0898-y
- Moore, G., et al. (2021). Adapting interventions to new contexts: The ADAPT guidance. *BMJ*, 374, n1679. https://doi.org/10.1136/bmj.n1679
- Movsisyan, A., et al. (2019). Adapting evidence-informed complex population health interventions for new contexts: A systematic review of guidance. *Implementation Science*, 14. https://doi.org/10.1186/s13012-019-0956-5

The FRAME is a reporting framework for modifications to evidence-based interventions; the dossier records its fields as what was modified, who modified it, when, why, and whether the modification was fidelity-consistent. The fuller field list this skill uses (whether the change was planned, at what level of delivery it occurred, and the nature of the change) follows the framework as the drafting brief for this library describes it; the dossier does not itemize those further fields, so they are unverified, author to confirm against the paper. The ADAPT guidance (Moore et al.) is for the planned transfer of an intervention to a new context; the dossier records "for planned transfer to a new context follow ADAPT" and does not itemize its steps, so the transfer path in this skill (state the rationale, plan the changes with stakeholders, pilot, then implement and maintain) is described generically, unverified, author to confirm. Movsisyan et al. review the guidance that existed before ADAPT and are the reason this skill treats adaptation as a documented, stepwise activity rather than improvisation. The judgment calls this skill adds, none of them published criteria: core components as a list with one mechanism per component, written before any modification is logged; a fidelity-consistency test phrased as "would the theory of change still predict the outcome?"; and a mandatory flag for any modification that removes a core component without a decision.

**WEIRD skew:** The FRAME and ADAPT are reporting and planning procedures, not claims about human behavior, so they travel; what does not travel is the judgment of which components are core, which depends on the mechanism in the user's population. A core component in the tested setting (a peer messenger, a paper calendar) may be periphery elsewhere, or the reverse, and the local theory of change decides. **Non-WEIRD evidence:** none found in the sources this skill draws on; the ADAPT guidance takes transfer to new contexts as its subject, which is a scope, not a result.

**Replication status:** The sources are frameworks, so there is no effect to replicate; the dossier records the fidelity-versus-adaptation debate as the live question, which is why this skill judges each modification by whether the mechanism survives rather than by how closely delivery resembles the original.

## How to do it

1. **List the core components**, one line each, with the mechanism it carries, taken from the theory of change or the technique skill that produced the intervention. Then write the adaptable periphery in one line. If the team cannot say what mechanism a component carries, it is not yet known to be core; mark it "provisional".
2. **For each modification, fill the FRAME fields**: when it occurred (before delivery, during, at scale-up); planned or unplanned; who decided or did it (the designer, a manager, a frontline worker, the participants); what was modified (content, the context of delivery, training, or the evaluation); at what level (the whole program, a site, a provider, individuals); the nature of the change (added, removed, shortened, substituted, reordered, loosened, tailored); and the goal and reasons given.
3. **Judge fidelity-consistency** for each: does the modified version still contain every core component in a form that carries its mechanism? Ask "would the theory of change still predict the outcome?" and write the answer with its reason. Resemblance to the original is not the test; a shortened session that keeps the mechanism is consistent, and an intact-looking session that lost it is not.
4. **For a transfer to a new context, follow the ADAPT path** generically: state why the intervention needs to change for this context and what the theory of change says must stay; plan the changes with the people who will deliver and receive them; pilot the adapted version before full delivery; then implement and keep recording. Each planned change enters the log in step 2 as a planned modification.
5. **Keep a running log**, versioned by date, so an evaluation can say which version its data describes. Add unplanned modifications from fidelity monitoring as they appear.
6. **Flag silent removals.** Any modification that drops a core component without a recorded decision gets a flag line: what mechanism is gone, who decided, and whether the team knows. Removals made for cost are flagged whether or not they were decided, because a program without a core component is a different program than the one tested.
7. **Write what to check**: which flagged modification matters most, and what monitoring or test would show whether the mechanism survived.
8. **Stop here.** Hand the log to `design-fidelity-monitoring` for the indicators, to `plan-scale-up-strategy` for the innovation package, and to `review-prior-intervention` if an evaluation is being read. See `references/evidence-notes.md` for the sources and `references/worked-example.md` for a complete run on an HIV self-testing program moving from Lagos to Ekiti, Nigeria.

## Output template

```markdown
# Adaptation record: <intervention name>, version <date>

**Baseline:** <the intervention as tested, in one line, with the source document>
**Context transfer:** <none / from where to where, and what differs>

## Core components and the mechanism each carries
| Component | Mechanism | Status |
|---|---|---|
| <component> | <why it works, from the theory of change> | <confirmed / provisional> |

**Adaptable periphery:** <language, timing, format, messenger, venue, as applicable>

## Modification log
| # | When | Planned? | Who decided | What was modified | Level | Nature | Goal and reasons | Fidelity-consistent? |
|---|---|---|---|---|---|---|---|---|
| 1 | <before / during / at scale-up> | <yes / no> | <role> | <content / context / training / evaluation: what> | <program / site / provider / individual> | <added / removed / shortened / substituted / reordered / loosened / tailored> | <...> | <yes / no, because the theory of change would / would not still predict the outcome> |

## Flags: core components removed or weakened
- **Modification #<n>:** removes <component>, which carried <mechanism>; decided by <role or "no recorded decision">; reason <cost / workload / other>. The modified version is a different intervention from the one tested until this is shown otherwise.

## Transfer plan (only when a context transfer is in progress)
- **Rationale:** <why change is needed here; what the theory of change says must stay>
- **Changes planned with stakeholders:** <who was involved; the planned modifications by number>
- **Pilot:** <what, where, how long, what it must show>
- **Implement and maintain:** <who keeps this log, how often>

## What to check before relying on this
- <the flagged modification that matters most, and the test or monitoring that would show whether the mechanism survived>
- <the provisional core component most likely to be mislabeled>
```

## Where it goes wrong

- **A change list with no core components.** A log of what changed, with no statement of what carries the mechanism, cannot say whether any change mattered. The core-component table comes first, or the log is a diary.
- **Drift called adaptation.** A frontline worker who stopped making the follow-up call because the phone credit ran out did not adapt the program; the log records it as unplanned, with the real reason, so the evaluation reads the right version.
- **Everything marked core.** A core-component list that includes the font on the leaflet forbids every change and will be ignored. Core is what carries a mechanism; the test is whether the theory of change names it.
- **Fidelity judged by resemblance.** A session that looks like the original but dropped the part that did the work is not fidelity-consistent, and a shortened session that kept it is. The question is always whether the mechanism survived.
- **Logging only the team's decisions.** Modifications made by frontline staff and by participants are the ones that go unrecorded; use fidelity monitoring data and ask delivery staff directly what they changed.
- **Running without a baseline.** With no written description of the intervention as tested, there is nothing to measure changes against; send the user to `draft-intervention-description` rather than reconstruct the baseline from memory.

## When to bring in a specialist

Tell the user to consult an implementation scientist, and where possible the people who designed and evaluated the original intervention, when:
- A core component is being removed for cost or workload reasons at scale-up, because the scaled program is then a different intervention from the one tested and the evaluation evidence no longer applies to it; the decision to proceed needs someone who can say whether a cheaper form of the mechanism exists
- A modification touches clinical, safety, or legal content (dosing instructions, test-result counseling, referral thresholds), where a "fidelity-consistent" judgment by a program team is not enough
- The transfer is to a population in which the theory of change may not hold at all (a different reference group for a norm message, a different payment system for a default), where the question is transferability rather than adaptation
- Delivery staff and the designers disagree about what is core, which usually means the theory of change is incomplete

Bring them: the core-component table with its mechanisms, the modification log, the flags, and the theory of change or intervention description the components came from.
