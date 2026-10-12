---
name: draft-intervention-description
description: >-
  Use when a team must write down exactly what an intervention was, item by
  item, so another team could rebuild it or a reader could tell what changed:
  for a funder, a new implementer, a scale-up partner, a trial registry, or a
  paper. Also use when the only record is a slide deck or a program name, or
  when "we ran the SMS program" has to become something a stranger could
  replicate. Produces an intervention description on the twelve TIDieR items
  (Hoffmann et al., 2014): each active ingredient named as a behavior change
  technique in plain words with its mechanism, materials and where to get
  them, and how well it was planned kept separate from how well it was
  delivered, using the fidelity plan's data. Do not use when the messages or
  scripts still need writing; that is draft-lever-content. Not for designing
  how delivery is monitored (design-fidelity-monitoring), classifying changes
  made during delivery (specify-intervention-adaptations), or judging whether
  it will scale (assess-scalability).
license: CC-BY-4.0
metadata:
  title: Describe an intervention so others can replicate it
  type: atomic
  stage: implement
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: not-applicable
  tags: "implementation-science, behavior-change-techniques, research-transparency, implementation"
  consumes: "intervention-draft, fidelity-plan"
  produces: "intervention-description"
---

## What it does

Writes down what an intervention actually was, item by item, in enough detail for another team to rebuild it.

It follows the TIDieR checklist (Template for Intervention Description and Replication): twelve items covering the name, the rationale, materials, procedures, provider, mode, location, dose, tailoring, modifications, and how well the intervention was delivered as planned and in fact. Each active ingredient is named as a behavior change technique in plain words with the mechanism it is meant to engage. The description records; it does not evaluate the intervention or recommend changes to it.

## When to use it

### Use it when
- A pilot or program is ending or scaling and the record of what was delivered is a slide deck, a proposal, or the memory of the person who ran it
- A funder, scale-up partner, or new implementing organization asks "what exactly did you do?" and needs to rebuild it without the original team
- A trial registry entry, a pre-analysis plan, or a paper needs its intervention section written to a reporting standard
- Someone says "we ran the SMS program" or "the health workers did counseling" as if that were a description

### Do not use it when
- The messages, scripts, or materials still need writing; `draft-lever-content` produces them, and this skill documents what was then delivered
- The question is how delivery will be checked during rollout; `design-fidelity-monitoring`, whose data fill this skill's "how well: actual" item
- The task is to classify the changes made during delivery as fidelity-consistent or not; `specify-intervention-adaptations` produces the adaptation record this skill carries into item 10
- The question is whether the intervention will survive scale-up; `assess-scalability` consumes this description

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The design documents: the intervention draft from `draft-lever-content` with its fidelity trace, the lever brief from `select-intervention-levers`, delivery notes, training materials, whatever exists in writing. If nothing exists in writing, ask the team for its own written account, and label every item drawn from it "reconstructed from recollection".
2. **Required.** Whether the intervention has been delivered, and if so over what period, and what delivery data exist: the fidelity plan from `design-fidelity-monitoring` and its data, logs, the adaptation record. If it has not been delivered, the description is "as planned" and items 10 and 12 are marked not yet applicable.
3. **Required.** Who the description is for and where it will go: internal record, funder report, hand-off to another implementer, trial registry, or publication. A registry or a publication is an escalation condition.
4. Optional. Where the materials live (drive, repository, appendix) and in which languages, so item 3 can say where to obtain them; and any constraint on what can be shared (partner-confidential materials, details that could identify participants or implementers).

If 1 is missing entirely, ask and stop. If 2 is missing, ask once; if still unclear, write the description as planned and say so at the top. If 3 is missing, assume an internal record that will be handed to another implementer. If 4 is missing, write "location to be added" in item 3, assume everything can be shared, and flag both under Open questions.

## What it draws on

- Hoffmann, T. C., et al. (2014). Better reporting of interventions: Template for intervention description and replication (TIDieR) checklist and guide. *BMJ*, 348, g1687. https://doi.org/10.1136/bmj.g1687
- Michie, S., et al. (2013). The behavior change technique taxonomy (v1) of 93 hierarchically clustered techniques: Building an international consensus for the reporting of behavior change interventions. *Annals of Behavioral Medicine*, 46(1), 81–95. https://doi.org/10.1007/s12160-013-9486-6
- Grant, S., et al. (2018). CONSORT-SPI 2018 Explanation and Elaboration: Guidance for reporting social and psychological intervention trials. *Trials*, 19, 406. https://doi.org/10.1186/s13063-018-2735-z

TIDieR (Hoffmann et al., 2014) is a twelve-item checklist for describing an intervention well enough to be replicated; the dossier confirms the item count. The item labels this skill uses (brief name; why; what: materials; what: procedures; who provided; how; where; when and how much; tailoring; modifications; how well: planned; how well: actual) are from the drafting brief, not from the dossier text, and are unverified, author to confirm against the paper. The Behavior Change Technique Taxonomy v1 (Michie et al., 2013) is 93 techniques in 16 clusters, built as an international consensus for reporting the active ingredients of behavior change interventions; this skill uses it to name ingredients descriptively, carrying a technique label from the lever brief where one exists and otherwise naming the technique in plain words without assigning a taxonomy number from memory. CONSORT-SPI 2018 (Grant et al., 2018) extends trial reporting to social and psychological interventions; a description headed for a registry or a paper is checked against it by a methodologist, not by this skill. The judgment calls this skill adds are the authors' practice rules: item 12 is filled only from fidelity data, never from the protocol; modifications go in item 10 from the adaptation record and are never folded into tailoring; every item carries its source; and the description ends with a rebuild check. See `references/evidence-notes.md`.

**WEIRD skew:** Not applicable in the population sense: TIDieR, the BCTTv1, and CONSORT-SPI are reporting standards and make no claim about how people behave. Their origin is a UK and Australian health-research reporting tradition, so their examples assume a trial write-up; a team describing a program for a district office or a scale-up partner should keep the twelve items and drop the trial framing. What to check locally is whether the description names the context features (clinic hours, agent networks, language, who the messenger was) that a reader elsewhere would otherwise assume away. **Non-WEIRD evidence:** none found in the sources this skill draws on; the dossier records "none (reporting standard)" for this entry.

**Replication status:** Uncontested, per the dossier: these are consensus reporting standards, not effects, so there is nothing to replicate. The dossier gives no numbers for this entry beyond the twelve TIDieR items.

## How to do it

1. **Gather the sources and list them at the top:** the intervention draft and its fidelity trace, the lever brief, delivery notes, training materials, the fidelity plan and its data, the adaptation record. Mark every item below with the source it came from, and write "reconstructed from recollection" where there was none, so a reader can tell documentation from memory.
2. **Fill items 1 through 8 as delivered, not as intended.** Brief name (1). Why (2): the target behavior, the confirmed barrier, and the rationale. Materials (3): each physical or digital material, including training materials, in each language, with where to obtain it. Procedures (4): each activity in order, including enrollment and what happened when someone was absent. Who provided (5): role, background, number, training received, supervision. How (6): face to face, phone, SMS, group, app. Where (7): with the context features that mattered. When and how much (8): contacts, schedule, duration, intensity, period.
3. **Name each active ingredient in item 2 as a behavior change technique in plain words,** with the mechanism it engages and the barrier it addresses. Carry the label verbatim from the lever brief where one exists; where none exists, name the technique descriptively ("feedback on the behavior") and do not assign a taxonomy number from memory. An element that maps to no technique is scaffolding, not an ingredient; say so.
4. **Separate tailoring (9) from modifications (10).** Tailoring is planned variation decided before delivery (language, dose by clinic size, time chosen by the participant). Modifications are changes made during delivery, taken from the adaptation record that `specify-intervention-adaptations` produced, each with what changed, when, who, why, and whether it touched an essential component. A change that appears under tailoring but was decided after launch is a modification.
5. **Write item 11 (how well: planned) from the fidelity plan:** what was monitored, how, by whom, with what thresholds. **Write item 12 (how well: actual) only from the fidelity data:** adherence, dose, and quality as measured, with the sample and period. If no fidelity data exist, item 12 says "not measured" and names what that means for interpreting any outcome.
6. **Run the rebuild check.** For each item, ask whether a reader in another country, with only this document and the materials it points to, could rebuild the intervention. Mark complete, partial, or missing, and say what is still needed. "Available on request" is missing.
7. **Write the Open questions:** every item marked partial or missing and who can close it, every item reconstructed from recollection, and any constraint on sharing.
8. **If the description will be submitted or published,** add the AI-use disclosure with `draft-sifa-declaration` and flag the CONSORT-SPI check for a methodologist.
9. **Stop here.** `assess-scalability` consumes this description; `design-fidelity-monitoring` takes its planned items for the next rollout. What to change next is the team's decision, not this document's.

See `references/worked-example.md` for a complete run on a weekly SMS program for ART adherence in Kisumu.

## Output template

```markdown
# Intervention description (TIDieR)

**Intervention:** <brief name>
**Status:** <as planned / as delivered, <start> to <end>, <where>> · **Written for:** <internal record / funder / hand-off / registry / publication>
**Sources used:** <documents, with "reconstructed from recollection" where there was none>

## 1. Brief name
<the name used in the field, and any other names it went by>

## 2. Why: rationale, active ingredients, mechanism
**Target behavior:** <who + what + when, carried over verbatim> · **Confirmed barrier:** <from the diagnosis, with its source>
| Active ingredient (behavior change technique, plain words) | Mechanism it engages | Barrier it addresses | Source |
|---|---|---|---|
| <label from the lever brief where one exists; no taxonomy number unless the brief gave it> | <what it does to the barrier> | <barrier> | <lever brief / draft / recollection> |

## 3. What: materials
| Material | Language(s) | Where to obtain it |
|---|---|---|
| <each physical or digital material, including training materials> | <languages> | <link, repository, appendix; "available on request" counts as missing> |

## 4. What: procedures
<each activity in order, including enrollment, what happened when someone was absent, and what the provider did between contacts>

## 5. Who provided
<role, background, how many, training received, supervision>

## 6. How
<mode: face to face, phone, SMS, group, app; individual or group>

## 7. Where
<locations, with the context features that mattered: hours, access, who else was present>

## 8. When and how much
<number of contacts, schedule, duration of each, intensity, over what period>

## 9. Tailoring
<planned variation decided before delivery: what varied, for whom, by what rule; or "none">

## 10. Modifications
| What changed | When | Who | Why | Essential component touched | Source |
|---|---|---|---|---|---|
| <from the adaptation record; or "none recorded", stating whether a log existed> | <date> | <role> | <reason> | <yes: which / no> | <record / recollection> |

## 11. How well: planned
<what was monitored, how, by whom, with what thresholds, from the fidelity plan; or "no monitoring planned">

## 12. How well: actual
<adherence, dose, quality as measured, with the sample and period, from the fidelity data; or "not measured", with what that means for interpreting any outcome>

## Rebuild check
| Item | Complete / partial / missing | What a reader elsewhere would still need |
|---|---|---|
| <1 through 12, one row each> | <status> | <what is needed; blank only if complete> |

## Open questions
- <every item marked partial, missing, or reconstructed from recollection, and who can close it>
- <any constraint on sharing materials or details>
```

## Where it goes wrong

- **The protocol as the delivery.** Filling item 12 from the design document, so "how well: actual" reads as complete because the plan said so. Item 12 comes from fidelity data or says "not measured"; there is no third option.
- **Marketing language in place of ingredients.** "An engaging, community-led, culturally sensitive approach" names no technique and no mechanism. Each row of the item 2 table says what was done to which barrier; if that cannot be written, the ingredient is unknown and the rebuild check must say so.
- **Taxonomy numbers from memory.** Assigning a BCTTv1 number the lever brief did not give. A wrong number is worse than a plain-words label, because a reader will trust it. Carry the label; do not invent the code.
- **Modifications hidden as tailoring.** The schedule that changed after week 3, the component dropped when an agent quit, the message rewritten after complaints: these are modifications. Writing them under item 9 as if planned makes the description describe an intervention that was never delivered.
- **"Available on request."** Materials that cannot be obtained from the description cannot be replicated. If the materials cannot be shared, say so and why under Open questions; do not mark item 3 complete.
- **Memory passed off as documentation.** Reconstructing items from recollection without labeling them, so a reader cannot tell what was recorded from what is remembered. The sources line and the per-item source column exist for this.

## When to bring in a specialist

Tell the user to consult the relevant specialist when:
- The description will go into a trial registry, a pre-analysis plan, or a publication; a methodologist or trial statistician checks it against CONSORT-SPI 2018 and the venue's reporting requirements, which go beyond the twelve items
- The intervention includes a clinical component (a medication, a dosage, a referral rule); a clinician checks that items 4 and 8 describe it accurately, because a faithful replication of a wrong dose is a harm
- The materials or the description contain partner-confidential content or details that could identify participants or implementers; counsel or a data-protection officer decides what can be shared before item 3 points anywhere
- The delivery data and the team's account disagree on an essential component; an implementation evaluator reads the fidelity data before item 12 is written, rather than the team splitting the difference

Bring them: the draft description with its sources line and rebuild check, the fidelity plan and its data, the adaptation record, and the materials in their final languages.
