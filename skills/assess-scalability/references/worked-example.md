# Worked example: an ART adherence SMS program moving from NGO clinics to county delivery in Kisumu, Kenya

The program, the pilot numbers, the costs, and the county's plan are illustrative; none of them is a reported finding. The sources quoted are the ones recorded in the dossier for this skill.

**User's answers to Before you start.** Claim: the Tuko Pamoja program sent weekly SMS adherence reminders to adults on ART at 8 NGO-supported clinics in Kisumu County; a cluster RCT with 1,640 patients found viral suppression at 12 months 9 percentage points higher in the SMS arm (95% CI 3 to 15), pre-registered primary outcome; the NGO's own adherence counselors sent messages from a dashboard, phoned anyone who replied "need help" within 24 hours, and carried caseloads of about 120; cost about USD 4.10 per patient per year. Scale-up: all 71 county ART clinics (about 48,000 patients), run by county staff, messages sent automatically from the national EMR, no dedicated counselor to answer replies, budget USD 1.50 per patient. Decision: a county budget line for the next fiscal year; the county says it can drop it after a year. Subgroup results: effect concentrated in patients enrolled under 12 months; near zero for patients stable on ART more than 3 years. Fidelity data: counselors logged 94% of weekly messages sent and a median reply-to-call time of 6 hours. No earlier scale-up attempt.

```markdown
# Scalability assessment: Tuko Pamoja ART adherence SMS, Kisumu County

**Claim (one line):** +9 percentage points (95% CI 3 to 15) on viral suppression at 12 months, measured on 1,640 adults on ART at 8 NGO-supported clinics in Kisumu County, delivered by NGO adherence counselors (caseload about 120, replies answered within 24 hours), at about USD 4.10 per patient per year
**Scale-up on the table:** from 8 clinics and 1,640 patients to 71 clinics and about 48,000 patients, delivered by county staff, messages sent automatically from the national EMR, no reply handling, at USD 1.50 per patient per year
**Decision this informs:** a county budget line for the next fiscal year; reversible: yes, the county says it can drop it after one year

## Threats to the effect

| Threat | Evidence for the threat (from the pilot) | Evidence against it | Test that would settle it (cost, time) |
|---|---|---|---|
| False positive | One study; the lower bound of the CI is 3 points; the published-to-field pattern (academic 8.7 versus unit 1.4 points, DellaVigna and Linos 2022) says a single estimate is an upper bound | Pre-registered primary outcome; cluster design; no multiple-outcome fishing reported | A second measurement in the first 10 scale clinics with a held-out comparison group (low cost if the EMR holds viral loads; 12 months) |
| Population | The effect sat in patients enrolled under 12 months; stable long-term patients showed near zero; the county caseload is mostly long-term patients (the team estimates two-thirds) | New enrollees are the group the county most wants to retain, so the effect may matter where it exists even if the average shrinks | Compute the share of newly enrolled patients per clinic from the EMR and project the average effect by weighting (no cost; one week) |
| Situation and implementer | The counselor who answered "need help" replies within 24 hours is removed; sending moves from a counselor's dashboard to automated EMR sends; county staff did not select, train, or supervise the pilot messaging; this is the NGO-to-government move the Kenya contract-teacher case warns about (Bold et al. 2018) | Message content and timing can be copied exactly; the EMR already holds phone numbers | A 6-month trial in 10 county clinics, half with a county reply-handler and half with automated sends only, viral load from the EMR (moderate cost; 6 to 9 months) |
| Spillovers | Messaging 48,000 patients at once may raise clinic visits in the same weeks, lengthen queues, and strain pharmacy stock; the pilot's 1,640 patients could not show this | Weekly messages are staggered by enrollment date, which spreads visits | Monitor visit volume and stock-outs in the 10 trial clinics against the other 61 (no extra cost; part of the trial above) |
| Cost at scale | The USD 1.50 budget removes the counselor line, which is the component the pilot's own fidelity data (6-hour median reply time) suggests was active; SMS gateway costs fall per message, supervision costs rise | Automated sending costs almost nothing per patient, so the USD 1.50 version is affordable if it works | Costing of the two trial arms by `estimate-cost-effectiveness` once the trial reports |

## Domain scores (generic set for this library; confirm against the ISAT)

| Domain | Score (1–5) | Evidence behind the score |
|---|---|---|
| Strength of the effect evidence | 3 | One pre-registered cluster RCT, CI 3 to 15, no second study |
| Fit with the scale population | 2 | Effect concentrated in a subgroup that is about one-third of the county caseload |
| Implementer capacity at scale | 2 | County staff have not delivered reply handling; the automated version drops it |
| Delivery system readiness | 4 | The national EMR holds phone numbers and viral loads and can send messages |
| Cost and financing at scale | 3 | A budget line exists at USD 1.50, which funds the automated version only |
| Risk of harm or backfire at scale | 3 | Unanswered "need help" replies could leave patients worse off than no message; no pilot evidence either way |

## Verdict
Scale after these tests, because the USD 1.50 version removes the reply-handling component without evidence that the effect survives its removal, and the scale population is mostly the subgroup in which the pilot found near zero.

## What must be true for the effect to survive
1. Automated sends without reply handling still raise suppression in newly enrolled patients; test: the 10-clinic trial; would change the verdict if it failed: yes
2. The county can staff a reply-handler role in at least the arm that keeps it; test: the trial's staffing log; yes
3. Weighting the pilot's subgroup effects by the county's caseload mix still gives a worthwhile average; test: the EMR share calculation; yes
4. Messaging all patients does not raise stock-outs or queue times in trial clinics; test: the trial's monitoring; no, but it changes the roll-out pace

## What to check before relying on this
- The harm cell is "no pilot evidence either way": whether an unanswered "need help" reply does damage is the first thing the trial must watch.
- The claim line's cost (USD 4.10) includes counselor time; if that figure is wrong, the cost-at-scale row changes.
```

**What happened next (illustrative).** The county agreed to fund the 10-clinic trial before the full budget line; the "what must be true" list went to `plan-scale-up-strategy` as the conditions the strategy must sequence around, and the trial design went to `plan-evaluation-design`.
