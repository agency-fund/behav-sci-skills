# Worked example: household latrine use in Lombok, Indonesia

Illustrative only. The program, numbers, and rules are invented to show one complete run; none of it is a finding.

**Setting (illustrative):** a district follow-up to the national community-based sanitation program (STBM) in Lombok Tengah, West Nusa Tenggara. Latrines were built in 24 triggered villages; monitoring suggests they are used unevenly, especially at night and by small children. The behavior came from `define-key-behavior`. The team supplied the Doer and Non-Doer rules, named village sanitation volunteers (kader) as enumerators, Bahasa Indonesia with Sasak, and about 20 minutes per interview. No hypotheses were supplied.

```markdown
# Barrier Analysis questionnaire: everyone in the household uses the latrine, every time

**Target behavior:** Every member of a household in the 24 program villages, including children under five, uses the household's latrine (or a shared latrine in the same compound) for every defecation, day and night.
**Doer:** in the past seven days, no household member defecated anywhere other than a latrine (reported by the main caregiver, who answers for children) | **Non-Doer:** at least one household member defecated outside a latrine at least once in the past seven days | **Exclude:** no latrine in the household or compound; respondent cannot speak for all household members
**Doer status verified by:** self-report, plus an enumerator spot-check of the latrine for signs of use (illustrative; a weak check that confirms some use, not use by everyone)
**Determinant list followed:** Kittle (2013; 2nd ed. 2017), twelve determinants
**Administered by:** village sanitation volunteers (kader), two days' training | **Language:** Bahasa Indonesia, Sasak where preferred | **Time per interview:** about 20 minutes

## A. Screening (classify before continuing)
S1. "Is there a latrine in your house or in this compound that your household can use?" [if no, thank and end]
S2. "Thinking about the past seven days, where did each person in your household go to defecate? Let's go through them: you, your spouse, each child, anyone else living here." [list each member; note any place other than a latrine]
S3. "Was there any time in the past seven days, at night or in the fields, when someone in the household did not use the latrine?"
Classification: Doer if every member is reported as using a latrine every time in S2 and S3 gives nothing; Non-Doer if S2 or S3 names any member or occasion outside a latrine; end the interview if S1 is no or the respondent cannot answer for every member.

## B. Respondent details (for comparability only)
- Respondent's age band; sex; village; number of household members; number of children under five; latrine type (own or shared)

## C. Determinant questions (matched pairs)
### 1. Perceived self-efficacy
- Doer: "What makes it easier for everyone in your household to use the latrine every time?" | Non-Doer: "What would make it easier for everyone in your household to use the latrine every time?"
- Doer: "What makes it difficult?" | Non-Doer: "What would make it difficult?"
- Probe: "Anything else?"
### 2. Perceived positive consequences
- Doer: "What good things happen because everyone in your household uses the latrine?" | Non-Doer: "What good things would happen if everyone in your household used the latrine?"
### 3. Perceived negative consequences
- Doer: "What bad things happen because everyone uses the latrine?" | Non-Doer: "What bad things would happen if everyone used the latrine?"
### 4. Perceived access
- Doer: "How difficult is it to keep the latrine usable: water, cleaning, repairs?" | Non-Doer: "How difficult would it be to keep the latrine usable: water, cleaning, repairs?"
### 5. Cues for action
- Doer: "What reminds people in your household to use the latrine, especially at night?" | Non-Doer: "What would remind people in your household to use the latrine, especially at night?"
### 6. Perceived social norms
- Both: "Would most people in this village approve or disapprove of a household where someone defecates in the fields or the river?" then "Who in particular would approve, and who would disapprove?" [people whose approval matters]
- Both: "Do most households like yours use their latrine every time?"
### 7. Perceived susceptibility
- Both: "How likely is it that a child in your household will get [diarrhea, local term] in the next month?"
### 8. Perceived severity
- Both: "How serious would it be if a child in your household got [diarrhea, local term]?"
### 9. Perceived action efficacy
- Both: "How likely is it that a child gets [diarrhea] if everyone in the household uses the latrine every time?"
### 10. Perceived divine will
- Both: "Do you think it is God's will, or fate, that decides whether a child gets [diarrhea]?"
### 11. Policy
- Both: "Are there any village rules or government rules that make it easier or harder for your household to use the latrine every time?"
### 12. Culture
- Both: "Are there any customs or beliefs here that make it easier or harder for everyone to use the latrine, for example at night, during planting, or for small children?"

## D. Closing
- "Is there anything about using the latrine that we have not asked and that matters to you?"; thanks; explain that the answers from many households will shape what the program does next.

## E. Fieldwork notes
- Sample: 45 Doers and 45 Non-Doers drawn from the same 24 villages, both groups spread across villages (Kittle 2013 case-control calculation, RR 3.0, 80% power)
- Pilot: 3 Doers and 3 Non-Doers in one village; check that S2 and S3 classify cleanly, that the difficult/easier pairs are understood, and that the interview fits in 20 minutes
- Record answers verbatim; code after fieldwork; the comparison is done in analyze-doer-nondoer-differences

## Local adaptation and translation risks
- [diarrhea, local term]: the kader team supplies the Sasak and local Indonesian words caregivers use for a child's diarrhea.
- [people whose approval matters] in determinant 6: the local team lists them (village head, religious leader, in-laws, neighbors) as prompts for the probe, not as options to read out.
- "Every time" and "at night": check that the Sasak rendering keeps both; the behavior fails most often at night.
- Kader are known in the village and promoted latrine building; a kader interviewing their own neighbors will draw Doer-sounding answers. Prefer kader from a different village.

## What to check before relying on this
- Doer status rests on one caregiver's report for the whole household, for a behavior the program has publicly promoted; expect over-reporting. The spot-check confirms only that the latrine is used by someone.
- The seven-day window assumes memory of each member's behavior; if the pilot shows caregivers cannot answer for adults, narrow the behavior to children under five or ask each adult separately.
- No hypotheses were supplied, so no determinant carries a sharpened probe; if `decompose-comb-barriers` is run later, add its probes under the matching determinants before fieldwork.
```
