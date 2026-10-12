# Worked example: antenatal iron-folate adherence in a rural district of Malawi

An illustrative run. The program is a district health office's antenatal care effort across four rural health centers (illustrative). All counts below are illustrative, not findings.

**Input (from `diagnose-social-norm`):** Practice: "Pregnant women enrolled at the four health centers take one iron-folate tablet every day from their first antenatal visit until delivery." Call: social norm holding the practice down; women stop because husbands and mothers-in-law expect them to avoid "hospital medicine" during pregnancy. Sanction: being blamed if anything goes wrong with the pregnancy. Provisional reference group: husbands, mothers-in-law.

**Program's assumed audience:** pregnant women, reached at the clinic by nurses and at home by Health Surveillance Assistants (HSAs).

```markdown
# Reference network map

**Practice:** Pregnant women enrolled at the four health centers take one iron-folate tablet every day from their first antenatal visit until delivery.
**Diagnosis call:** social norm (holding the practice down), from diagnose-social-norm (September 2026); provisional reference group: husbands, mothers-in-law.
**Program's assumed audience:** pregnant women, via clinic nurses and HSA home visits.

## Design
**Chosen:** egocentric.
**Why:** The four catchments hold about 4,000 households (illustrative), an open population with no natural boundary, so a full-network census cannot be completed. A snowball design would find the most-connected elders but the question is the typical reference group of a pregnant woman, not the settlement's structure. Budget: 28 interviews over two weeks. Egocentric gives the typical set; it cannot show who connects to whom.
**Sample:** 28 pregnant women (7 per center), split between first and later pregnancies, chosen from the antenatal register by every fourth name. Interviewed alone, at home or at the clinic, by a female interviewer.

## Name-generator questions
1. "When you decide whether to take the tablets the clinic gave you each day, whose opinion matters to you?"
2. "Who would notice if you took them, or if you stopped?"
3. "Whose approval would you want before taking medicine during pregnancy?"
4. "Who would you ask if you were unsure about the tablets?"
5. For each person named: "If they told you to take the tablets every day, would you?"
**Name-interpreter questions (per person named):** relationship; lives in the compound or elsewhere; how often seen; took or allowed tablets in her own or her wife's pregnancies; approves of hospital medicine in pregnancy; can stop you taking them, or make it possible.

## Reference group by role

| Role (no names) | Named by (n of N) | Influence: actor would change if they did | Gatekeeping: can permit or block | Does X | Approves X |
|---|---|---|---|---|---|
| Husband | 22 of 28 | Yes (20 of 22: "if he said take them, I would") | Yes: can forbid; controls transport money for visits | n/a | Mixed; 9 of 22 said he is against |
| Mother-in-law | 19 of 28 | Yes (16 of 19) | Yes: lives in the compound, sees the tablets, advises daily | No (her own pregnancies predate the program) | No (15 of 19) |
| Own mother | 11 of 28 | Partly (8 of 11; stronger in first pregnancies) | No: usually lives elsewhere | Mixed | Mixed |
| Older neighbors and co-wives | 9 of 28 | Partly (5 of 9) | No | Mixed | Mixed |
| Traditional birth attendant | 7 of 28 | Partly (4 of 7) | No, but advises on what to avoid | n/a | No (5 of 7) |
| Church women's guild leader | 6 of 28 | Yes (5 of 6) | No | n/a | Yes (5 of 6) |
| HSA | 4 of 28 | No (1 of 4) | No | n/a | Yes |
| Clinic nurse | 3 of 28 | No (1 of 3) | No | n/a | Yes |

## Influential nodes and gatekeepers
- **Influential:** husband; mother-in-law; church women's guild leader (named by few, but every woman who named her said she would follow her).
- **Gatekeepers:** husband (can forbid, controls money); mother-in-law (in the compound, daily contact, sees the tablets).
- **Named often but not influential:** none at the top of the table; HSA and nurse are rarely named and not influential, which is where the program currently spends its contact time.

## Does the reference group match the program's audience?
No. The program talks to pregnant women at the clinic and through HSAs. The people whose approval would change the behavior (husband, mother-in-law) are at home and are not contacted. The guild leader is a route to mothers-in-law that nobody named as a program contact. Own mother matters more in first pregnancies, which the program does not distinguish.

## Community verification
Role table shown to six women at one center. They added "own mother" as more important for first pregnancies and less later (now reflected), and said the TBA matters more in the two centers furthest from the road.

## Who must be in the room
Husbands and mothers-in-law, as the people whose expectations hold the practice down, at whatever point the program addresses the norm; the church women's guild leader as a possible route to mothers-in-law. Which of them delivers any message is `select-messenger`'s decision.

## What to check before relying on this
- Only 7 women per center; the TBA's weight in the two remote centers rests on 3 interviews.
- Husbands were not interviewed; their stated opposition is as reported by wives.
```

Next step: `select-messenger` for who speaks to the mothers-in-law; `plan-collective-pledge` if the program wants a household-level commitment that includes husbands.
