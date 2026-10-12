# Worked example: household latrine use in Lombok, Indonesia (Doer/Non-Doer comparison)

Illustrative only. The counts, percentages, p-values, and quotes are invented to show one complete run; none of it is a finding.

**Setting (illustrative):** the district follow-up to the national sanitation program in Lombok Tengah described in `draft-barrier-analysis-questionnaire`. That questionnaire was run by village sanitation volunteers (kader) from neighboring villages. Achieved sample: 46 Doers, 44 Non-Doers, 6 excluded (no latrine), none reclassified. Two kader coded the verbatim answers and reconciled. The table shows twelve response categories across eight determinants; the full run tabulates every category under all twelve determinants. Percentages use 46 and 44 as denominators; p-values and flags come from `scripts/doer_nondoer_tab.py`.

```markdown
# Barrier diagnosis: everyone in the household uses the latrine, every time

**Target behavior:** Every member of a household in the 24 program villages, including children under five, uses the household's latrine (or a shared latrine in the same compound) for every defecation, day and night.
**Doer:** in the past seven days, no household member defecated anywhere other than a latrine, reported by the main caregiver | **Non-Doer:** at least one household member defecated outside a latrine at least once in the past seven days
**Sample achieved:** 46 Doers, 44 Non-Doers; 6 excluded (no latrine in household or compound); 0 reclassified in the field
**Coding:** two kader coded independently and reconciled; they disagreed on 4 of 31 categories, all resolved; Doer status rests on self-report plus a latrine spot-check
**Flag rule:** absolute difference of 15 percentage points or more, or Fisher exact p < .05 (Kittle 2013/2017 convention; a heuristic, not a validated cutoff)

## Group comparability
- Both groups were drawn from all 24 villages (Doers 1 to 3 per village, Non-Doers 1 to 3 per village); respondent sex 40 of 46 women among Doers, 37 of 44 among Non-Doers; household size similar. Non-Doer households have more children under five (mean 1.6 versus 1.1, illustrative), which could explain part of the "children afraid at night" row.

## Tabulation
| Determinant | Response category | Doers n (%) | Non-Doers n (%) | Difference (points) | p | Flag |
|---|---|---|---|---|---|---|
| Perceived self-efficacy | no water near the latrine ("we carry water from the well; at night nobody will") | 8 (17.4) | 27 (61.4) | -44.0 | <.001 | yes |
| Perceived self-efficacy | children afraid to go at night ("the small ones cry, so we take them behind the house") | 10 (21.7) | 21 (47.7) | -26.0 | .014 | yes |
| Perceived positive consequences | fewer illnesses ("the children are not sick so often") | 35 (76.1) | 30 (68.2) | +7.9 | .483 | no |
| Perceived positive consequences | privacy, not being seen ("nobody sees you, especially the women") | 20 (43.5) | 6 (13.6) | +29.8 | .002 | yes |
| Perceived negative consequences | smell and flies ("it smells when it is hot") | 14 (30.4) | 16 (36.4) | -5.9 | .656 | no |
| Perceived access | hard to keep usable: water, cleaning ("cleaning it is work every day") | 9 (19.6) | 25 (56.8) | -37.3 | <.001 | yes |
| Cues for action | nothing reminds us at night ("at night you just go outside") | 11 (23.9) | 20 (45.5) | -21.5 | .046 | yes |
| Perceived social norms | most households like ours use it every time: yes | 38 (82.6) | 17 (38.6) | +44.0 | <.001 | yes |
| Perceived social norms | the village head would disapprove of open defecation | 30 (65.2) | 25 (56.8) | +8.4 | .517 | no |
| Perceived susceptibility | a child here is very likely to get diarrhea | 15 (32.6) | 14 (31.8) | +0.8 | 1.000 | no |
| Perceived divine will | God or fate decides whether a child gets diarrhea | 12 (26.1) | 13 (29.5) | -3.5 | .815 | no |
| Culture | planting season, people are in the fields all day ("in planting we are far from the house") | 6 (13.0) | 15 (34.1) | -21.0 | .025 | yes |
p-values are descriptive: twelve determinants with several categories each give chance plenty of chances. Seven of twelve categories shown are flagged; the ranking below carries five forward.

## Flagged determinants, ranked
1. **Perceived social norms: most households like ours use it every time.** Doers 82.6% vs Non-Doers 38.6%, 44.0 points. Direction: enabler to reinforce. Coverage: 38 of 46 Doers; only 17 of 44 Non-Doers believe it. Anchor: "Here everyone uses it now, it would be shameful not to."
2. **Perceived self-efficacy: no water near the latrine.** 17.4% vs 61.4%, 44.0 points. Direction: barrier to remove. Coverage: 27 of 44 Non-Doers. Anchor: "we carry water from the well; at night nobody will." Overlaps with the access row; the two categories were kept separate because respondents named them under different questions.
3. **Perceived access: hard to keep usable.** 19.6% vs 56.8%, 37.3 points. Direction: barrier to remove. Coverage: 25 of 44 Non-Doers. Anchor: "cleaning it is work every day."
4. **Perceived positive consequences: privacy, not being seen.** 43.5% vs 13.6%, 29.8 points. Direction: enabler to reinforce. Coverage: 20 of 46 Doers. Anchor: "nobody sees you, especially the women."
5. **Perceived self-efficacy: children afraid to go at night.** 21.7% vs 47.7%, 26.0 points. Direction: barrier to remove. Coverage: 21 of 44 Non-Doers; partly explained by Non-Doer households having more small children. Anchor: "the small ones cry, so we take them behind the house."
Also flagged, carried as secondary: cues for action, nothing reminds us at night (21.5 points, p .046); culture, planting season (21.0 points, 15 of 44 Non-Doers).

## Bridges to Activities
- Perceived social norms: "Increase the perception among households in the 24 villages that most households like theirs use the latrine every time, including at night."
- Perceived self-efficacy (water): "Increase the ability of households in the 24 villages to have water at the latrine at night without a trip to the well."
- Perceived access: "Increase the ability of households in the 24 villages to keep the latrine clean and usable with little daily work."
- Perceived positive consequences: "Increase the perception among households, especially women, that using the latrine means not being seen."
- Perceived self-efficacy (children): "Increase the ability of caregivers in the 24 villages to take children under five to the latrine at night."
- Cues for action (secondary): "Increase the presence of a cue at night that prompts household members to use the latrine."
- Culture (secondary): "Decrease the perception among households that defecating in the fields during planting season is acceptable."

## Not flagged
- Perceived susceptibility and perceived divine will: both groups answered alike; the team expected divine will to separate them and it did not.
- Perceived positive consequences, fewer illnesses: common in both groups (76% and 68%); the health message has reached everyone and is not what separates Doers.
- Perceived negative consequences, smell: similar in both groups.
- Policy: no respondent in either group named a village or government rule (0 of 46 and 0 of 44); not shown in the table.

## What to check before relying on this
- Doer status is self-reported for a publicly promoted behavior; some Doers may be Non-Doers who answered well, which would shrink every gap.
- The water and access rows may be one barrier counted twice; confirm with the kader whether respondents meant the same thing before writing two Bridges.
- The "children afraid at night" gap is partly a household-composition difference; check the row among households with at least one child under five only.
- Whether the program can act on water at the latrine; if not, the top-ranked barrier is not the top-ranked Bridge.
```
