# Worked example: antenatal iron-folate counseling in rural Malawi

An NGO supports four rural antenatal clinics in one district of Malawi with a counseling package meant to raise daily iron-folate tablet adherence among pregnant women. The intervention description was drafted with `draft-intervention-description` (planned items only); the nurse script came from `draft-lever-content` with its fidelity trace. All program names, counts, and thresholds are illustrative. Nothing here is a finding.

```markdown
# Fidelity monitoring plan

**Intervention:** Antenatal iron-folate counseling package ("Mankhwala Tsiku ndi Tsiku", illustrative name), four rural clinics
**Implementers:** 8 antenatal nurses (2 per clinic) and 24 Health Surveillance Assistants (HSAs, government community health workers, 6 per clinic), supervised by one clinic in-charge per clinic and the district HSA coordinator
**Use of the data:** Learning and support only. Stated in the memorandum with the District Health Office and at the launch meeting with nurses and HSAs. No individual results go to the in-charge; clinic-level results only.

## Essential components
| Component | Mechanism it carries | Essential or adaptable | Why |
|---|---|---|---|
| Three-message nurse script at each antenatal visit: why daily, take with food at night to limit nausea, what to do after a missed day | Information about health consequences plus instruction on how to perform the behavior (plain-words BCT labels from the lever brief) | Essential | Dropping any message removes the barrier it addresses (nausea was the confirmed barrier) |
| Pictorial tick calendar handed over with the 30-tablet supply | Self-monitoring of the behavior | Essential | Without it the woman has no daily cue or record |
| HSA home visit within 3 weeks of each antenatal visit: pill count, calendar check, restate the night-with-food instruction | Prompt plus feedback on behavior | Essential | Carries the follow-up the pilot showed mattered (illustrative) |
| Group song and greeting that open the clinic counseling session | Rapport | Adaptable | Can vary by clinic without loss |
| Time of the HSA visit (morning or afternoon) | None | Adaptable | Set by the HSA's route |

## Indicators
| Component | Dimension | Indicator (observable) | Data source | Sample and frequency | Collected by |
|---|---|---|---|---|---|
| Nurse script | Adherence | All three messages said in the observed session (yes/no per message) | Spot check: monitor sits in on a session, unannounced | 2 sessions per nurse per month | District monitor (NGO), not the in-charge |
| Nurse script | Quality | Woman restates the night-with-food instruction correctly when the nurse asks | Same spot check | Same sessions | District monitor |
| Tick calendar | Dose (coverage) | Share of women enrolled that month who report receiving a calendar with their tablets | Back-check: phone call or household visit to a random sample drawn from the antenatal register | 10 women per clinic per month, drawn by the monitor, not the nurse | District monitor |
| HSA home visit | Dose (frequency) | Share of enrolled women visited within 3 weeks of the antenatal visit | HSA visit log, verified against the back-check sample ("did an HSA come, and when?") | All log entries; the 10 back-checked women per clinic | HSA coordinator compiles the log; monitor runs the back-check |
| HSA home visit | Adherence | Pill count done and night-with-food instruction restated (yes/no each) | Spot check: monitor accompanies an HSA on a visit, unannounced | 2 visits per HSA per quarter | District monitor |
| Tick calendar | Responsiveness | Calendar ticks present for the days since the last visit (count) | Recorded by the HSA at the visit; verified on accompanied visits | All HSA visits; verified on the accompanied 2 per HSA per quarter | HSA; monitor |

## Thresholds and actions
| Indicator | Expected level | Action threshold | Action | Who acts |
|---|---|---|---|---|
| All three messages said | 90% of observed sessions (pilot level, illustrative) | Below 70% at a clinic in a month | Half-day refresher using the script cards; re-observe next month | Clinic in-charge with the NGO trainer |
| Calendar received | 95% | Below 85% | Stock check at the clinic; confirm calendars are with the tablets, not in a cupboard | NGO logistics officer |
| HSA visit within 3 weeks | 80% | Below 60% at a clinic | Route review with the HSAs; drop or reschedule visits, do not add them to the backlog | HSA coordinator |
| Back-check disagrees with the log | Under 10% of checked women | Above 20% | Data review meeting with the clinic team as a group; no individual follow-up | District monitor with the in-charge |

## Feedback loop to implementers
- **Who receives what:** each clinic team (nurses and HSAs together) gets a one-page sheet with the clinic's four indicators, the gap to the expected level, and one next step; the District Health Office gets the four-clinic summary.
- **Cadence:** monthly, in the week after the back-checks close.
- **Task-level rule:** clinic-level numbers only, no individual names, no ranking across clinics, and no use in appraisal, pay, or discipline; written into the memorandum and said at launch.
- **Upward channel:** the HSA coordinator's monthly phone round asks each HSA "what stopped you this month"; answers go on the sheet's back page.

## Adaptation log
A log page at the back of each HSA visit book and a column on the monitor's spot-check form: date, what changed, who changed it, why, which essential component it touches. Entries are collected monthly and go to `specify-intervention-adaptations` for classification.

## Threats the monitoring must catch
- **Attrition:** women who miss the next antenatal visit, from the register · **Non-compliance:** women who decline the calendar or the home visit, noted by the nurse or HSA · **Spillover:** HSAs who also cover villages served by the two comparison clinics, from the HSA coordinator's route list · **Contamination:** nurses rotated between program and comparison clinics, from the district staffing roster

## What to check before relying on this
- That the antenatal register is filled in during the visit; if it is reconstructed at day's end, the back-check sample is drawn from a list that may already be wrong.
- That the clinic in-charge is present often enough to run a refresher within the month; if not, the action owner must change.
- That the District Health Office signs the data-use clause; until then the feedback loop is a proposal, not a commitment.
- Whether the HSA visit is truly essential or whether the calendar alone carries the follow-up; the pilot data should settle this before the plan is scaled.
```

Mystery clients were not used: the service is delivered to enrolled pregnant women, not to strangers at a counter, so a mystery-client visit would be neither feasible nor ethical here. Had the package included a pharmacy counter, `design-mystery-client-protocol` would supply that source.
