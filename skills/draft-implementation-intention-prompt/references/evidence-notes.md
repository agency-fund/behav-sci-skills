# Evidence notes: draft-implementation-intention-prompt

Every item below comes from `docs/plan/2026-10-skill-expansion-dossier.md` (entry `draft-implementation-intention-prompt`, section A, section B). The verification tag is the dossier's. Nothing here has been upgraded or added from memory.

## Anchor sources

**Gollwitzer, P. M., & Sheeran, P. (2006). Implementation intentions and goal achievement: A meta-analysis of effects and processes. *Advances in Experimental Social Psychology*, 38, 69–119. https://doi.org/10.1016/S0065-2601(06)38002-1** [verified-crossref]
- d = 0.65 on goal attainment across 94 independent tests. The dossier gives no pooled N and no country breakdown.
- The mechanism: an if-then plan links a situational cue to the action, so the cue, not deliberation, initiates it. The dossier flags the meta-analytic effect as probably inflated relative to field trials.

**Milkman, K. L., Beshears, J., Choi, J. J., Laibson, D., & Madrian, B. C. (2011). Using implementation intentions prompts to enhance influenza vaccination rates. *PNAS*, 108(26), 10415–10420. https://doi.org/10.1073/pnas.1103170108** [verified-crossref]
- Field trial on flu shots. The prompt asking for a date and a time added 4.2 percentage points over a 33.1% baseline; the prompt asking only for a date added 1.5 points, not significant.
- This is the source for the rule that the prompt asks for all three of date, time, and place.

**Nickerson, D. W., & Rogers, T. (2010). Do you have a voting plan? Implementation intentions, voter turnout, and organic plan making. *Psychological Science*, 21(2), 194–199. https://doi.org/10.1177/0956797609359326** [verified-crossref]
- N = 287,228. A plan-making prompt raised turnout 4.1 points overall and 9.1 points in single-voter households.
- The household contrast is the source for the "organic planning" boundary: where people already plan with others, the prompt adds less.

**Carrera, M., et al. (2018). The limits of simple implementation intentions: Evidence from a field experiment on making plans to exercise. *Journal of Health Economics*. https://doi.org/10.1016/j.jhealeco.2018.09.002** [verified-crossref] (report had only a PDF sighting; DOI located in the audit)
- Field experiment on plans to exercise, a repeated behavior; a tight null. The dossier gives no N or effect size. This is the source for the one-off rule and the hand-off to `design-habit-anchor`.

**Buttenheim et al. (2022). Planning and commitment prompts to encourage reporting of HIV self-test results: A cluster randomized pragmatic trial in Tshwane District, South Africa. *PLOS Global Public Health*. https://doi.org/10.1371/journal.pgph.0001196** [verified-crossref]
- The trial exists and is the only LMIC field RCT of the technique in the dossier. Its results were not retrieved in the research session, so no number may be quoted; cite existence only (unverified result, author to confirm).

## Discounting sources (section A)

**DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709** [verified-crossref]
- 126 RCTs, 23 million people. Academic journal studies average 8.7 percentage points (+33.4%); nudge-unit trials average 1.4 points (+8.0%). About 70% of the gap is explained by selective publication combined with low power.

**Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x** [verified-crossref]
- Pooled 0.16 SD; 0.33 SD in the lab versus 0.02 SD in the field, with publication bias among lab studies. The lab-to-field shrinkage example; not implementation-intention evidence.

## Practitioner sources

- Behavioural Insights Team, *EAST*, "Make it timely" [verified-fetch: https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf]. The PDF at this URL is the revised and updated edition (file dated 2024); the preface dates the original to 2014. No individual authors on the cover.

## Non-WEIRD evidence

- South Africa (Buttenheim et al., 2022): trial exists; result not retrieved; no number quoted.
- A savings implementation-intention study summarized by Cenfri reports that numeric goals did worse than general commitments; country unconfirmed. [unverified, author to confirm] (dossier unverified item 13). This is the only basis for the "avoid a numeric goal" step, which is why SKILL.md phrases it as a caution rather than a finding.
- No LMIC field RCT with a confirmed effect was found in the sources this skill draws on. The `weird` value is therefore untested-outside-weird, as the dossier proposes.

## Known corrections and cautions

- The plan's "verify result" for the South Africa trial remains open; cite existence only.
- The meta-analytic d = 0.65 is probably inflated relative to field trials; the two large field trials gave about 4 points. Never give d = 0.65 as a planning number.
- The exercise null applies to repeated behavior; do not generalize the technique to habits.

## What to check locally

1. That intention exists for this action in this population, measured for a specific occasion rather than "someday".
2. Whether the person can write or say a plan, and in what language; the prompt may need to be asked aloud and recorded by the person who delivers it.
3. Whether the date, time, and place are the person's to choose: permission, transport, shift work, who holds the phone.
4. Whether households or groups plan together already, which halved the effect in the voting trial.
5. Whether the action window has real options at the hours people are free; the window map must come from the service, not from the program's assumptions.
6. Who sees the written plan, especially where the action is sensitive.
