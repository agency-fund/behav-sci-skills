---
name: design-mystery-client-protocol
description: >-
  Use when a program wants to know what providers actually do with a client
  (at a clinic, pharmacy, bank agent, mobile money kiosk, or extension
  office) rather than what they say they do, and can send a trained local
  person posing as a client. Also use when someone says "standardized
  patient", "simulated client", "mystery shopper", "secret shopper", or
  "our provider survey says they counsel everyone but we doubt it".
  Produces a mystery client protocol: scripted cases, an essential-action
  checklist, recruitment and training of local standardized clients,
  sampling of providers and visits, an ethics plan for the organization's
  ethics board, detection and debrief, and the adherence analysis, following
  the standardized patient method of Das and colleagues' India study. Do
  not use when the question is what providers know or report about their
  own practice; use draft-survey-items. Not for monitoring the program's
  own delivery over time (design-fidelity-monitoring).
license: CC-BY-4.0
metadata:
  title: Measure what providers do with mystery clients
  type: atomic
  stage: measure
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "measurement, quantitative, process-evaluation"
  consumes: "measurement-plan"
  produces: ""
---

## What it does

Designs an unannounced visit by a trained person posing as a client, so a program can measure what providers actually do rather than what they report.

The standardized patient method, as used in health research, trains local people to present the same case the same way at every visit; immediately afterward, out of sight, each records on a checklist what the provider asked, examined, advised, prescribed, and charged. Because the provider does not know the visit is a measurement, the result is practice as it happens, not practice under observation. The same logic transfers to any counter where a client's request is scripted and the correct response is known: a bank agent, a mobile money kiosk, an agro-dealer, a government office.

## When to use it

### Use it when
- Provider self-reports, exit interviews, or supervisor checklists look too good, and the team wants direct observation without the observer effect of a visible evaluator
- Someone says "standardized patient", "simulated client", "mystery shopper", "secret shopper", or "send someone in posing as a customer"
- An intervention aims to change provider behavior (training, incentives, job aids, a new fee schedule) and the measurement plan names provider practice as the outcome
- The team wants to compare provider types (public, private, informal; agent networks of different firms) on the same scripted case

### Do not use it when
- The question is what providers know, or what they say they do; `draft-survey-items` writes the knowledge test or self-report questionnaire
- The team wants to monitor its own program's delivery continuously as part of implementation; that is `design-fidelity-monitoring`, which may use mystery clients as one indicator among several
- The client's role cannot be faked safely: the case needs a child, a pregnancy, a physical sign, or a procedure the standardized client would have to undergo; use consented direct observation or clinical record review instead
- The team has no access to an ethics review; deception without review is not an option, and the organization's ethics board decides before anything is fielded

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The provider behavior to measure, as who does what for which kind of client, and the setting: facility or outlet type, public or private or informal, and how clients normally present. Paste the measurement plan if one exists.
2. **Required.** Whether an adult without the condition can plausibly present the case with words alone, without undergoing any injection, test, procedure, or medicine. If not, the method is not possible for that case, and the output must say so.
3. **Required.** What ethics review the organization can reach, and whether the providers are public employees whose results could reach their supervisors or a ministry. This decides the consent plan and the reporting rules before any case is written.
4. Optional. The sampling frame (a list of providers), the budget per visit, and whether visits will be repeated after an intervention.
5. Optional. The clinical guideline or service standard the checklist should follow.

If 1 to 3 are missing, ask and stop. If 4 is missing, assume one visit per provider per case, from a list the program must build. If 5 is missing, build the checklist from the national guideline and mark every clinical line "for clinical review".

## What it draws on

- Das, J., Holla, A., Das, V., Mohanan, M., Tabak, D., & Chan, B. (2012). In urban and rural India, a standardized patient study showed low levels of provider training and huge quality gaps. *Health Affairs*, 31(12), 2774–2784. https://doi.org/10.1377/hlthaff.2011.1356
- Kwan, A., et al. (2019). Use of standardised patients for healthcare quality research in low- and middle-income countries. *BMJ Global Health*, 4, e001669. https://doi.org/10.1136/bmjgh-2019-001669 (confirmed to exist in the evidence audit; its content was not summarized there, so no specific recommendation is attributed to it)

Das and colleagues sent standardized patients presenting fixed cases to 305 providers in Delhi and rural Madhya Pradesh, 926 interactions in all, and found low levels of provider training and large quality gaps between what providers knew and what they did. The method's logic is that a scripted case turns every visit into the same test, so differences between providers, provider types, or time points reflect practice rather than case mix. Kwan and colleagues' guide covers the use of the method for quality research in low- and middle-income countries. The judgment calls this skill adds: a no-harm rule for the standardized client (no medicine taken, no procedure undergone, every purchase kept as evidence); a detection record after every visit and a provider end-survey as mandatory data quality steps; facility- or provider-level advance consent with an opt-out as the default rather than a blanket waiver; and an escalation whenever providers are public employees who could be sanctioned on the results.

**WEIRD skew:** The method's main evidence base is India, and the research program behind it is LMIC-native; the plan also names Kenya and China, without citations in the dossier. What a user elsewhere should check: whether a stranger presenting at this provider is plausible (in small communities every client is known), whether a local person of the right age, sex, and language can be recruited and kept unrecognized, and whether posing as a client carries legal risk in this jurisdiction. **Non-WEIRD evidence:** India, Delhi and rural Madhya Pradesh: 305 providers, 926 standardized patient interactions, low provider training and large quality gaps (Das et al. 2012).

**Replication status:** Established method; the dossier records it as such, with the caution that the ethics of deception and the detection rate must be justified for each study. No pooled estimate of how well standardized patient visits agree with clinical records or consented observation appears in the dossier, so none is quoted here.

## How to do it

1. **Fix the cases.** Choose one to three conditions or service requests that the program cares about, that a healthy adult can present with words alone, and that have a clear correct response under a named guideline or service standard. For each, write the opening statement, the answer to every question a provider could plausibly ask (history, duration, prior treatment, family, income, ID), and the refusal rules: no injection, no medicine swallowed, no examination that would reveal the ruse or harm the client; buy what is prescribed and keep it.
2. **Build the essential-action checklist** from the guideline: the history questions, examinations, correct advice, correct treatment, referral, and the harmful actions to record (unnecessary antibiotics, steroids, injections, a wrong product, an undisclosed fee). Mark each line essential or recorded-only, add price charged and consultation time, and send the clinical lines to a clinician for review before training starts. See `references/evidence-notes.md` for the method's evidence and limits.
3. **Recruit and train local standardized clients** who match the case in age, sex, language, dress, and story, and whom the providers do not know. Train until two trainers score the same mock consultation the same way, teach immediate recall to the checklist out of sight, and rehearse the refusal rules until they are automatic.
4. **Write the ethics plan for the organization's ethics board.** State why consented observation would not measure the same thing (the justification for deception); the consent model (facility- or provider-level advance consent with an opt-out, worded "in the coming months a trained person may visit as a client", or a waiver with the reasons); no harm to the client; no harm to providers (results reported in aggregate, no individual results to supervisors unless agreed in writing beforehand); data handling; and what the client does if the provider does something dangerous to real patients. This skill drafts the plan; the ethics board decides.
5. **Sample providers and visits.** State the frame, the number of providers, visits per provider (one per case), timing (ordinary busy hours), spacing so the same client is not seen twice at one site, and the before-and-after schedule if the measurement plan is an evaluation.
6. **Plan detection and debrief.** After each visit the client records whether they believe they were detected and the cues; at the end, a short provider survey asks whether they suspected a standardized client and when; set in advance the rule for visits flagged as detected; debrief every consented provider with aggregate results.
7. **Specify the analysis:** adherence as the share of essential actions completed per visit; the correct-management rate; the harmful-action rate; price and time; comparisons by provider type, case, and time point or arm; the handling of detected visits; and the unit of analysis (the visit, clustered by provider).
8. **Stop here.** The ethics board reviews the plan; the number of providers goes to a sample-size calculation; the program fields nothing until both return.

**The non-health version.** At a bank branch, a mobile money agent, an agro-dealer, or a government counter, the case is a scripted request (open an account, cash in a fixed amount, ask for a named fertilizer, apply for a permit) and the checklist is the service standard: what should be explained, offered, charged, and refused. The same rules apply: the mystery shopper buys nothing they must consume, signs nothing binding without a plan to unwind it, carries the exact cash, and records the visit immediately afterward; consent and reporting follow the same plan, and the firm's or ministry's agreement on reporting rules comes before fielding.

See `references/worked-example.md` for a complete run on informal private providers in rural Rajasthan.

## Output template

```markdown
# Mystery client protocol: <provider behavior>

**Provider behavior measured:** <who does what for which client> **Setting:** <facility or outlet type; public / private / informal>
**Purpose:** <baseline | evaluation outcome | provider-type comparison> **Providers are public employees:** <yes / no; reporting agreement>

## Cases
### Case 1: <name>
- Opening statement: "<what the client says first>"
- Answers to likely questions: <symptom or request details; duration; prior treatment; family; money; ID>
- Refusal and safety rules: <no injection; no medicine taken; purchases kept; exam limits; exit line>
- Correct management per <guideline or standard>: <...>
### Case 2: ...

## Essential-action checklist
| Action | Essential / recorded only | Source |
|---|---|---|
| <history question> | essential | <guideline section> |
| <harmful action to record> | recorded only | <...> |
| Price charged; consultation time | recorded only | |

## Standardized clients
<who; how many; matching to case; training length and consistency standard; recall procedure>

## Ethics plan (for the organization's ethics board)
- Justification for deception: <why consented observation would not measure the same thing>
- Consent: <facility-level / provider-level advance consent with opt-out, wording; or waiver and reasons>
- No harm to the client: <rules>; no harm to providers: <aggregate reporting; written agreement on anything else>
- Dangerous-practice rule: <what the client does if ...>
- Data handling: <...>

## Sampling of providers and visits
<frame; n providers (illustrative); visits per provider; timing; spacing; before and after schedule>

## Detection and debrief
<client detection record; provider end-survey; rule for detected visits; debrief>

## Analysis
<adherence score; correct management; harmful actions; price and time; comparisons; detected visits; unit and clustering>

## What to check before relying on this
- <the case most at risk of detection or harm here>
- <the checklist line most dependent on the clinical review>
```

## Where it goes wrong

- **Cases a healthy adult cannot present.** Anything that needs a child, a pregnancy, a visible sign, or a test result gets the client caught or hurt. Such cases must be refused and the behavior measured by consented observation or record review instead.
- **The client takes the medicine or undergoes the procedure.** No measurement justifies it. The refusal rules are written into the case script and rehearsed, and the output says what the client does when a provider insists.
- **A checklist built from the team's intuition.** "Did the provider seem thorough" is not an item. Every essential line traces to a guideline or service standard and has passed clinical review; otherwise the adherence score measures the team's taste.
- **Reporting individual providers to supervisors.** Results that reach a supervisor turn a measurement into a sanction, and providers who are public employees can lose their jobs on one scripted visit. Aggregate reporting is the default and anything else is agreed in writing before fielding.
- **Skipping the detection check.** A detected visit measures performance under observation, which is exactly what the method exists to avoid. The detection record and the provider end-survey are not optional.
- **Drifting into fidelity monitoring.** One scripted visit per provider at two time points measures provider practice as an outcome. Monthly checks on the program's own staff against its own script are `design-fidelity-monitoring`'s job, with a different sampling logic.

## When to bring in a specialist

Tell the user to consult a clinician, the organization's ethics board, and, where relevant, the government counterpart when:
- Any case could lead a provider to prescribe or perform something harmful (an injection, a controlled drug, a procedure), because the refusal rules and the dangerous-practice rule need clinical judgment the team does not have
- Providers are public employees who could face sanctions on the results; a written reporting agreement with the ministry or district office comes before the first visit
- Posing as a client could expose the standardized clients to legal risk (impersonation rules, purchase of controlled products) or to violence if detected
- The protocol is the primary outcome of an evaluation; the number of providers, visits, and the clustering need a statistician's sign-off

Bring them: the case scripts with refusal rules, the checklist with its guideline sources, the consent and reporting plan, and the sampling plan.
