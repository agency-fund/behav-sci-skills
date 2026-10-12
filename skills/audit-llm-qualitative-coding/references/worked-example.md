# Worked example: ART adherence interviews in Kisumu, Kenya (LLM coding audit)

Illustrative only. The interviews, agreement figures, and quotes are invented to show one complete run; none of it is a finding.

**Setting (illustrative):** a program at two clinics in Kisumu County that sends SMS reminders to people on antiretroviral therapy (ART) and wants to know why doses are missed. Sixty interviews were held in Dholuo, Kiswahili, or English and translated to English by a local team. A commercial LLM applied a nine-code codebook to the English text. The decision the codes feed is whether to add a disclosure-support session for people who have not told a partner. Two clinic nurses who speak Dholuo hand-coded a stratified subsample blind.

```markdown
# LLM coding audit: Kisumu ART missed-dose interviews, nine-code codebook

**Data:** 60 interview transcripts (English translations of Dholuo, Kiswahili, and English interviews), 412 coded answer units, collected by two program interviewers at Clinic A and Clinic B
**Codebook:** v1.2, 9 codes (forgetting; travel; stigma or fear of being seen; side effects; stock-out; transport cost; disclosure to partner; religion or healing; other) | **Model:** commercial LLM, name and version string in the project log, default settings | **Prompt:** frozen 3 October 2026; stored in the project repository
**Use the codes will be put to:** the decision on adding a disclosure-support session; counts of the stigma and disclosure codes by sex
**Reference coding:** two clinic nurses (Dholuo and Kiswahili speakers, trained on the codebook for one day); blind to model output: yes; independent then reconciled

## Strata and subsample
| Stratum | Why it matters | Units in subsample |
|---|---|---|
| Women, short answers (under 40 words) | the session targets women; short answers give the model least to go on | 6 interviews, 38 units |
| Women, long answers | comparison within women | 6 interviews, 61 units |
| Men, short answers | comparison for the short-answer effect | 6 interviews, 35 units |
| Men, long answers | comparison | 6 interviews, 58 units |
| Original language: Dholuo 14, Kiswahili 7, English 3; Clinic A 12, Clinic B 12 | low-resource language; interviewer effects | (cross-cutting, same 24 interviews) |

## Agreement
| Stratum | n units | Model vs consensus: % agreement | Kappa | Human vs human: % agreement | Kappa |
|---|---|---|---|---|---|
| Overall | 192 | 84 | 0.71 | 88 | 0.79 |
| Women, short | 38 | 63 | 0.39 | 84 | 0.72 |
| Women, long | 61 | 90 | 0.82 | 90 | 0.83 |
| Men, short | 35 | 80 | 0.66 | 86 | 0.75 |
| Men, long | 58 | 91 | 0.84 | 90 | 0.82 |
| Dholuo-origin units | 108 | 79 | 0.63 | 87 | 0.77 |
| Kiswahili- or English-origin units | 84 | 90 | 0.82 | 89 | 0.80 |
Per code (overall): disclosure to partner 74%, kappa 0.52; stigma or fear of being seen 78%, 0.58; forgetting 93%, 0.86; travel 95%, 0.90; side effects 91%, 0.84; stock-out 97%, 0.93; transport cost 94%, 0.88; religion or healing 89%, 0.70; other 71%, 0.41

## Disagreement patterns
- The model misses "stigma or fear of being seen" when it is said by idiom in a short answer. Unit W07-3, consensus: stigma; model: other. Translated text: "I did not want the people at the gate to count me." Twelve of the 21 stigma disagreements are in the women-short stratum; nine are Dholuo-origin.
- The model adds "forgetting" when a respondent says they were away. Unit M11-2, consensus: travel; model: forgetting and travel. "I was in Busia for the funeral, the tablets were here."
- "Disclosure to partner" is split between model and consensus on units where the nurses also disagreed before reconciling (6 of 14 disagreements). These are not clear model errors; both readings are defensible.
- No pattern by clinic or interviewer.

## Stability
- Runs: 2; run-to-run agreement: 93% of units identical; the codes that flipped were "other" and "stigma or fear of being seen", almost all in the women-short stratum

## Decision
**Accept with human review.** The overall agreement is close to the human-to-human baseline, and the long-answer strata match it. The women-short stratum is materially worse (63% against a human baseline of 84%), the gap falls on the two codes the decision depends on, and those codes are also the least stable across runs. The criteria applied: a stratum is "materially worse" when its model agreement sits well below its own human-to-human figure, and the decision's codes must not be the weak ones.
- Conditions: a nurse reviews every unit the model coded "other" or "stigma" in women's interviews under 40 words (about 70 units of 412), and every "disclosure to partner" unit in the full set; a re-audit if the prompt or codebook changes

## Audit note for the SIFA declaration
A commercial LLM (version in the project log) applied codebook v1.2 to 412 answer units from 60 translated interviews under a prompt frozen on 3 October 2026. Two Dholuo-speaking nurses coded a stratified subsample of 24 interviews (192 units) blind and reconciled; the model agreed with their consensus on 84% of units overall (kappa 0.71) against a human-to-human figure of 88% (0.79), but on only 63% (0.39) of short answers from women, where it missed stigma expressed by idiom. Two model runs agreed on 93% of units. The coding was accepted with human review of women's short answers and of every disclosure-to-partner unit; the humans remain accountable for all counts reported.

## What to check before relying on this
- The women-short stratum has 38 units from 6 interviews; the pattern is clear but the figure is not precise.
- Consent forms covered "analysis by the program team"; whether that covers a third-party model should be confirmed with the data-protection officer, and the audit report records that the translated text, without names, was sent.
- The Dholuo-origin gap may be translation as much as the model; a check of the 9 Dholuo stigma units against the audio would separate the two.
```
