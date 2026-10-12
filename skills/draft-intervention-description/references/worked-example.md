# Worked example: weekly SMS for ART adherence at two clinics in Kisumu

An NGO ran a weekly SMS program for adults on antiretroviral therapy (ART) at two public clinics in Kisumu County, Kenya, for 48 weeks, with a fidelity plan from `design-fidelity-monitoring` and an adaptation record from `specify-intervention-adaptations`. The description is for a hand-off to the county health office, which wants to run it at four more clinics. All names, counts, and percentages are illustrative; nothing here is a finding, and no adherence outcome is reported.

```markdown
# Intervention description (TIDieR)

**Intervention:** "Tuko Pamoja" weekly SMS (illustrative name)
**Status:** As delivered, March 2025 to February 2026, two public ART clinics in Kisumu County · **Written for:** hand-off to the county health office
**Sources used:** lever brief (select-intervention-levers); intervention draft with fidelity trace (draft-lever-content); nurse training deck; fidelity plan and its data (gateway logs, monthly back-checks, enrollment spot checks); adaptation record. Nothing reconstructed from recollection.

## 1. Brief name
"Tuko Pamoja" (Swahili, "we are together"); called "the Monday message" by participants and nurses.

## 2. Why: rationale, active ingredients, mechanism
**Target behavior:** Adults on ART at the two clinics take their daily dose at their chosen time, every day. · **Confirmed barrier:** forgetting at the moment of the dose, and feeling alone with the regimen between clinic visits (from the diagnosis; source: lever brief).
| Active ingredient (behavior change technique, plain words) | Mechanism it engages | Barrier it addresses | Source |
|---|---|---|---|
| Weekly prompt by SMS (label carried from the lever brief: "prompts and cues") | A cue at a fixed time each week that re-raises the daily dose to attention | Forgetting | Lever brief |
| Offer of a nurse call on reply ("social support, practical") | A person reachable between visits | Feeling alone with the regimen | Lever brief |
| Greeting line and clinic name in each message | None: delivery scaffolding, so the sender is recognized | n/a | Draft fidelity trace |

## 3. What: materials
| Material | Language(s) | Where to obtain it |
|---|---|---|
| Message bank, 12 messages, one per week rotating four times | Swahili, Dholuo, English | Appendix A of this document; county shared drive, folder "Tuko Pamoja/messages", all three languages |
| Enrollment form with consent, language choice, time-of-day choice | Swahili, English | Appendix B; same folder |
| Nurse callback script | English | Appendix C; same folder |
| Nurse training deck (2 hours) | English | Same folder, "training" |
| SMS gateway configuration (schedule, reply keyword, opt-out keyword) | n/a | Same folder, "gateway", as an export |

## 4. What: procedures
At a routine ART visit the nurse explains the program, takes consent, records the phone number, language, and preferred time on the enrollment form, and enters it in the gateway the same day. The first message is sent the following Monday at the chosen time. Each Monday thereafter the gateway sends the week's message. A participant who replies "1" is called by a clinic nurse; the nurse logs the call. A participant who replies "STOP" is removed the same day. A participant who misses a clinic visit stays enrolled; the message does not mention the missed visit. Participants who change number are re-enrolled at the next visit.

## 5. Who provided
Four ART clinic nurses (two per clinic), each with a two-hour training on enrollment and the callback script; one NGO program officer managed the gateway and reviewed the callback log weekly; the clinic in-charge supervised the nurses.

## 6. How
Individual SMS; individual phone call from a nurse when the participant replied.

## 7. Where
Enrollment at the ART clinics during routine visits (open weekdays 8am to 4pm, both clinics with a private counseling room); messages received wherever the participant was. Both clinics had reliable mobile coverage; one had intermittent power, which did not affect the gateway (hosted off-site).

## 8. When and how much
One enrollment contact of about ten minutes; one message per week at the participant's chosen time for 48 weeks (48 messages); nurse calls as triggered by replies (median one per participant over the period, illustrative).

## 9. Tailoring
Planned before delivery: language (three options) and time of day chosen by the participant at enrollment.

## 10. Modifications
| What changed | When | Who | Why | Essential component touched | Source |
|---|---|---|---|---|---|
| Two Dholuo messages re-translated | Week 6 | Program officer with a Dholuo-speaking nurse | Back-translation showed they implied a diagnosis to anyone reading the phone | Yes: message content; classified fidelity-consistent by specify-intervention-adaptations | Adaptation record |
| Callback window widened from 48 to 72 hours | Week 14 | Clinic in-charge | One nurse on leave; 48 hours no longer achievable | Yes: the support component; classified as a change to watch | Adaptation record |

## 11. How well: planned
Per the fidelity plan: gateway delivery logs for every message (dose); monthly back-check calls to 20 randomly drawn participants per clinic on receipt and recall of the last message (dose, adherence); the nurse callback log checked against the reply log weekly (adherence of the support component, with a 48-hour threshold); two enrollments per nurse per month observed by the program officer (quality). Thresholds: delivery below 85% in a month triggers a gateway check; recall below 70% triggers a message review; callbacks within window below 80% triggers a staffing conversation with the in-charge.

## 12. How well: actual
From the fidelity data, 48 weeks, illustrative: 92% of scheduled messages delivered per the gateway log; across the twelve monthly back-checks, 84% of 480 sampled participants recalled receiving a message in the previous two weeks; 71% of replies were called within 48 hours before week 14 and 88% within 72 hours after; 7 of 8 observed enrollments covered every consent point. No fidelity data on whether the message was read at the chosen time.

## Rebuild check
| Item | Complete / partial / missing | What a reader elsewhere would still need |
|---|---|---|
| 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12 | Complete | |
| 3 | Partial | The Dholuo message bank is on the drive, but the re-translated week-6 versions are not yet marked as current; the gateway export needs a note on which product it is for |

## Open questions
- Item 3: the program officer can mark the current Dholuo versions and annotate the gateway export this month.
- Whether "read at the chosen time" matters for the mechanism; the fidelity plan did not measure it, and the county office should decide whether to add a read-receipt check.
- No constraint on sharing: the materials contain no participant details.
```
