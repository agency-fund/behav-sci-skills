---
name: design-fidelity-monitoring
description: >-
  Use when an intervention is about to roll out, or already has, and the team
  needs to know whether it is being delivered as designed: which parts to
  watch, what counts as delivered, who checks, how often, and what happens
  when delivery slips. Also use when the only monitoring is the implementer's
  own activity log, or when a funder asks for a fidelity or process-monitoring
  plan. Produces a fidelity monitoring plan: the essential components, one
  observable indicator per component with adherence, dose, and quality kept
  separate, data sources, sampling, action thresholds, and a non-punitive
  feedback loop to implementers, following Carroll et al. (2007) and the MRC
  process-evaluation guidance. Do not use when the program is finished and
  the question is whether it failed in delivery or in idea; that is
  review-prior-intervention. Not for designing feedback as the intervention
  itself (design-feedback-report), and not for documenting what was delivered
  item by item (draft-intervention-description).
license: CC-BY-4.0
metadata:
  title: Monitor whether a program is delivered as designed
  type: atomic
  stage: implement
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "implementation-science, process-evaluation, implementation"
  consumes: "intervention-description"
  produces: "fidelity-plan"
---

## What it does

Designs how a team will check, during rollout, whether an intervention is being delivered the way it was designed.

Implementation fidelity is the degree to which an intervention is delivered as intended. The plan names the components that carry the mechanism, gives each an observable indicator with adherence (was the content delivered), dose (how much reached whom, how often, for how long), and quality (how well) kept separate, sets who collects what and how often, fixes the thresholds that trigger action, and routes the results back to implementers as support rather than judgment. It is a plan. It does not collect the data, and it does not interpret an outcome.

## When to use it

### Use it when
- A rollout is starting or under way and "are they actually doing it?" is answered only by the implementer's own activity log
- A funder or evaluation partner asks for a fidelity, implementation-monitoring, or process-monitoring plan before launch
- A pilot showed an effect and the team wants delivery at scale to stay close to what was piloted
- An evaluation is planned and the team wants a null result to read as "delivered and did not work" rather than "never really delivered"
- Someone asks "how do we know the health workers are saying the right thing?" or "what should supervisors be checking each month?"

### Do not use it when
- The program is finished and the question is whether it failed in delivery or in idea; `review-prior-intervention` reads the record after the fact, where this skill creates the record
- The feedback is the intervention (a report to teachers or farmers meant to change their own behavior); `design-feedback-report` owns that design, including its backfire risks
- The need is to document the intervention item by item so another team can replicate it; `draft-intervention-description`, which this plan's data feed
- The question is whether the intervention is feasible or acceptable at all before a trial; `design-pilot-feasibility-study` sets those progression criteria
- Changes to the intervention are already known and need classifying as fidelity-consistent or not; `specify-intervention-adaptations`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The intervention as planned: the intervention description from `draft-intervention-description`, or the intervention draft from `draft-lever-content` with its fidelity trace, or at minimum a list of the components and who delivers each. If the only account is "the health workers counsel the mothers", ask for what the counseling contains before continuing.
2. **Required.** The delivery system: who the implementers are (NGO staff, government workers, volunteers, a platform), roughly how many, where, and who supervises them. If the implementer is a government partner, whether a written data-sharing or monitoring agreement exists.
3. **Required.** What the monitoring data will be used for: learning and support only, or also staff appraisal, pay, or discipline. The answer changes the design and is an escalation condition.
4. Optional. Existing data streams (registers, a management information system, app logs, call records) and what the team knows about their reliability.
5. Optional. The monitoring budget: monitors available, transport, phones, time per month.

If 1 or 2 is missing, ask and stop. If 3 is missing, ask once; if there is no answer, proceed on the assumption that the data are for learning and support only, state that assumption at the top of the plan, and tell the team it must be confirmed with the implementing organization before launch. If 4 is missing, assume no existing data stream is reliable enough to stand alone. If 5 is missing, design for a small monitoring team and flag where the plan can be cut.

## What it draws on

- Carroll, C., et al. (2007). A conceptual framework for implementation fidelity. *Implementation Science*, 2, 40. https://doi.org/10.1186/1748-5908-2-40
- Dane, A. V., & Schneider, B. H. (1998). Program integrity in primary and early secondary prevention: Are implementation effects out of control? *Clinical Psychology Review*, 18(1), 23–45. https://doi.org/10.1016/S0272-7358(97)00043-3
- Moore, G. F., et al. (2015). Process evaluation of complex interventions: Medical Research Council guidance. *BMJ*, 350, h1258. https://doi.org/10.1136/bmj.h1258
- J-PAL (M. Gibson, updated February 2021). *Implementation monitoring*. https://www.povertyactionlab.org/resource/implementation-monitoring

Carroll et al. (2007) frame implementation fidelity as adherence to the intervention as designed, with adherence covering content, coverage, frequency, and duration, and with moderators that explain why adherence varies: intervention complexity, facilitation strategies (manuals, training, supervision), quality of delivery, and participant responsiveness. Their central move is that the essential components must be identified first, so that fidelity to those, rather than to every detail, is what gets measured. The dossier records the citation only; this reading of the framework is from the drafting brief and is unverified, author to confirm against the paper. Dane and Schneider (1998) is the earlier review asking whether prevention programs measured and reported their implementation at all. The MRC guidance (Moore et al., 2015) places fidelity inside a process evaluation with three strands, implementation, mechanisms of impact, and context; this skill covers the implementation strand only, and a team that needs the other two should read the guidance directly. The J-PAL resource is the practice source: "Implementation requires careful monitoring to ensure that the program maintains fidelity to its design"; it names the threats an evaluation faces that monitoring must catch (attrition, compliance, spillovers, contamination) and defers monitoring-plan detail to a companion resource. The judgment calls this skill adds are the authors' practice rules, not published criteria: separate adherence, dose, and quality indicators per component; at least one data source independent of the implementer's own log; a named action per threshold; and a feedback loop that is task-level and never used for appraisal, on the reasoning that a log that can punish the person who fills it in will be managed rather than filled in. See `references/evidence-notes.md`.

**WEIRD skew:** The framework literature (Carroll et al.; Dane & Schneider; the MRC guidance) comes from UK and North American health and prevention research, and its worked examples assume salaried, supervised providers and records that are filled in at the time of delivery. Check locally: whether registers are completed during the visit or reconstructed later; whether unannounced observation is acceptable to implementers and to the community; whether volunteers or government workers have any supervisor who can act on a threshold; and what a "spot check" signals where monitoring has historically meant audit. **Non-WEIRD evidence:** the J-PAL implementation-monitoring resource is written from LMIC field trials and is the only LMIC-informed source in the dossier entry; no study comparing monitoring designs in an LMIC was found in the sources this skill draws on.

**Replication status:** Not applicable in the effect sense: fidelity monitoring is a method, not an intervention, and the dossier records the method as uncontested. What is contested is the balance between fidelity and adaptation, which the dossier flags as a live tension; that is why this plan logs deviations for classification rather than treating every deviation as a failure. The dossier gives no effect sizes, k, or N for this entry.

## How to do it

1. **Name the essential components.** Take them from the intervention description's planned items or the technique skill's fidelity trace. For each, write the mechanism it carries; a component is essential because dropping it removes the mechanism, not because it is in the manual. Mark everything else adaptable, so monitors are not sent to count what does not matter.
2. **Write one observable indicator per component per dimension.** Adherence: was the content delivered (the script's three messages were said). Dose: coverage (how many of the intended people), frequency, and duration. Quality: how well, by whom, with what skill. Add participant responsiveness where it can be observed. An indicator passes only if two monitors watching the same visit would record the same value.
3. **Match a data source to each indicator.** Administrative logs and registers give dose cheaply but are filled in by the person being monitored. Spot checks (unannounced observation of a delivery) give quality. Back-checks (re-contacting a sample of participants to ask whether the visit happened and what was said) test whether the logs are true. Participant exit surveys give responsiveness. Mystery clients, designed with `design-mystery-client-protocol`, give adherence and quality where the service is delivered at a counter or clinic to strangers. Every essential component gets at least one source independent of the implementer's own record.
4. **Set the sample and the schedule.** For each source: how many units per round, how units are chosen (random from the register, not the implementer's choice), how often, and who collects it. Keep the collector independent of the person collected on; a supervisor's own log is not a check on that supervisor. Size the whole plan to the budget from Before you start and say what gets cut first.
5. **Set a threshold and an action for each indicator.** Write the expected level (from the pilot where one exists, otherwise a stated assumption), the level that triggers action, the action, and who takes it. A threshold without a named actor is a number nobody owns.
6. **Design the feedback loop to implementers.** Who receives which results, in what form, how often. Keep it task-level: the indicator, the gap, one concrete next step. No ranking of people, no link to pay or discipline, and a written commitment to that in the plan. Add an upward channel so implementers can report what is not working before a monitor finds it. If the loop itself needs designing as a report, hand that to `design-feedback-report`; it carries the same self-focus backfire risk.
7. **Set up the adaptation log.** A standing place where any unplanned change is recorded when it happens: date, what changed, who changed it, why, and which essential component it touches. Classification of each entry as fidelity-consistent or not is `specify-intervention-adaptations`' job; this plan only guarantees the entries exist.
8. **List the threats the monitoring must catch** for the evaluation: attrition, non-compliance, spillover, and contamination, each with the indicator that would show it. Without these the outcome analysis cannot tell a weak intervention from a weakly delivered one.
9. **Stop here.** `draft-intervention-description` fills its "how well: actual" item from this plan's data; `specify-intervention-adaptations` classifies the log; `review-prior-intervention` reads the whole record after the fact.

See `references/worked-example.md` for a complete run on antenatal iron-folate counseling in rural Malawi.

## Output template

```markdown
# Fidelity monitoring plan

**Intervention:** <name, carried over from the intervention description or draft>
**Implementers:** <who delivers, roughly how many, supervised by whom>
**Use of the data:** <"learning and support only", stated as a commitment to implementers; or the escalation note if appraisal, pay, or discipline is on the table>

## Essential components
| Component | Mechanism it carries | Essential or adaptable | Why |
|---|---|---|---|
| <component> | <what it does to the barrier> | <essential / adaptable> | <dropping it removes the mechanism / it can vary without loss> |

## Indicators
| Component | Dimension | Indicator (observable) | Data source | Sample and frequency | Collected by |
|---|---|---|---|---|---|
| <component> | <adherence / dose / quality / responsiveness> | <what two monitors would record the same way> | <log / spot check / back-check / exit survey / mystery client> | <n per round, how chosen, how often> | <who, independent of whom> |

## Thresholds and actions
| Indicator | Expected level | Action threshold | Action | Who acts |
|---|---|---|---|---|
| <indicator> | <from the pilot, or a stated assumption> | <the level that triggers action> | <concrete step> | <named role> |

## Feedback loop to implementers
- **Who receives what:** <role: indicators, in what form>
- **Cadence:** <how often, tied to the collection cycle>
- **Task-level rule:** <no ranking of people; no use in appraisal, pay, or discipline; stated in writing to implementers>
- **Upward channel:** <how implementers report problems before a monitor finds them>

## Adaptation log
<where unplanned changes are recorded as they happen: date, what changed, who, why, essential component touched; entries go to specify-intervention-adaptations for classification>

## Threats the monitoring must catch
- **Attrition:** <indicator> · **Non-compliance:** <indicator> · **Spillover:** <indicator> · **Contamination:** <indicator>

## What to check before relying on this
- <the assumption most likely to be wrong: usually that the register is filled in at the time of delivery, or that a supervisor exists who can act>
- <the component the team is least sure is essential>
- <the data-use commitment, if not yet confirmed with the implementing organization>
```

## Where it goes wrong

- **Monitoring the manual, not the mechanism.** A checklist of every step in the protocol, weighted equally, when two steps carry the mechanism and the rest are scaffolding. Monitors then spend their time on what does not matter, and a program can score high on the checklist while never delivering the active ingredient. Step 1 exists to stop this.
- **Logs as truth.** An activity register filled in by the implementer is the cheapest data source and the one most likely to be complete regardless of what happened. A plan whose only source for an essential component is the implementer's own log has no fidelity data on that component; it has a self-report.
- **Dose without quality.** Counting visits, sessions, or messages sent and calling it fidelity. A visit at which the script was not followed is dose without adherence; a script read in a monotone to a mother who left is adherence without quality. The three dimensions are separated in the indicator table because they fail separately.
- **Punitive drift.** The feedback loop starts as support and becomes a league table, a bonus trigger, or a disciplinary file. Once implementers learn the log can hurt them, the log stops describing delivery. The task-level rule and the written commitment are the plan's defense; if the organization will not make that commitment, go to the escalation point.
- **Freezing the intervention.** Treating every deviation as a fidelity failure to be corrected. Some deviations are the adaptation the context needs; the plan's job is to make sure each is logged and classified, not suppressed. The reverse failure, logging nothing and calling every change "local adaptation", is why the log has fields.
- **Monitoring that changes the delivery.** A plan so heavy that implementers spend more time being checked than delivering, or whose spot checks announce themselves so well that the observed visit is the only faithful one. Size the plan to the budget and say what gets cut first.

## When to bring in a specialist

Tell the user to consult the relevant specialist when:
- The implementing organization intends to use the monitoring data for staff appraisal, pay, or discipline; an implementation researcher and the organization's human-resources or labor lead should redesign the loop before launch, because the plan above assumes a non-punitive use it cannot enforce
- The implementer is a government partner and no written data-sharing or monitoring agreement exists; the partner's data-governance office and the team's counsel settle who may observe whom and who owns the records before any spot check is scheduled
- Monitoring involves observing clinical encounters, children, or stigmatized services (HIV, family planning, mental health), or any mystery-client work; an ethics reviewer and, for mystery clients, `design-mystery-client-protocol` with its deception and detection checks
- The plan is meant to double as the evaluation's process evaluation; an implementation researcher working from the MRC guidance (Moore et al., 2015) designs the mechanisms-of-impact and context strands, which this skill does not cover

Bring them: the intervention description or draft with its fidelity trace, the essential-components table, the indicator table, and the data-use answer from Before you start.
