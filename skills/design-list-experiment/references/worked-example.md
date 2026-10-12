# Worked example: condomless sex with a partner of unknown status, Lagos HIV self-testing program

An illustrative run. The program (call it "TestNow Lagos", illustrative) distributes HIV self-test kits through community pharmacies in three local government areas of Lagos State, Nigeria, to adults aged 18 to 30. Its measurement plan names "sex without a condom with a partner of unknown HIV status in the past three months" as a secondary outcome. The direct question at baseline returned 11% (illustrative), which the team believes is far too low. All numbers below are illustrative, not findings.

**Answers to Before you start:** (1) adults 18 to 30 who collected a kit; past three months; sensitive because of stigma and because the interviewer is from the program. (2) Face to face, in English, Yoruba, or Pidgin, by program enumerators; literacy mixed, numeracy adequate for small counts. (3) About 2,400 endline interviews; whole-sample estimate only. (4) Yes, keep the direct question. (5) The items sit in a 25-minute endline survey on health and daily life.

```markdown
# List experiment design: condomless sex with a partner of unknown HIV status

**Behavior measured:** adults 18 to 30 who collected a self-test kit; sex without a condom with a partner whose HIV status they did not know; past three months **Why sensitive here:** stigma; the interviewer is from the program that gave them the kit
**Population and mode:** young adults, mixed literacy, English, Yoruba, or Pidgin; face to face; program enumerator present
**Affordable sample:** 2,400 (illustrative) **Estimate needed for:** whole sample only

## Is the bias worth the variance?
Prior on under-reporting: the pooled evidence says sensitivity bias is usually under 10 points; here the direct estimate (11%) sits far below what the program's counseling notes suggest, so a bias of 10 points or more is plausible (illustrative judgment). With 2,400 respondents split 1,200 and 1,200 and a whole-sample estimate only, the design is worth attempting. Go, on condition that the counting pretest passes and `estimate-sample-size` confirms 2,400 can detect a 10-point difference in means given the control-count variance below.

## Items
**Sensitive item (treatment list only):** "In the past three months, I had sex without a condom with someone whose HIV status I did not know."
**Control items (both lists):**
1. "In the past seven days, I took a danfo bus at least once." (expected prevalence: high, illustrative)
2. "In the past month, I traveled outside Lagos State." (expected prevalence: low, illustrative)
3. "Most mornings, I listen to the radio." (expected prevalence: mid, illustrative)
4. "Yesterday, I spent most of the day at home." (expected prevalence: mid, illustrative; negatively correlated with item 1)
**Floor and ceiling check:** item 1 is true for most respondents, so few answer zero; item 2 is rare, so few answer all four; items 1 and 4 pull against each other, which keeps the control count away from both extremes. Expected control count mostly 1 to 3.
**Treatment list order:** items 1, 3, sensitive item, 4, 2.

## Randomization
Individual respondents; 1:1; versions generated in advance on the tablet by respondent ID, balanced within enumerator; the version is stored with the record; the enumerator sees only the list to read, not a "treatment" label.

## Delivery script and comprehension check
Read aloud: "I am going to read you a short list of statements. Do not tell me which ones are true for you. Only tell me how many of them are true. Think about each one, then give me the number." Practice list (neutral): "I ate rice this week; I have been to Abuja; I own a goat; I have a younger brother." Enumerator confirms the respondent gives a count, not a list. Counting aid: four or five bottle caps; the respondent moves one aside, below the table, for each true statement, then counts them. If the respondent names an item, the enumerator says "Only the number, please", re-reads the full list, and records that the instruction was repeated.

## Direct comparison question
"In the past three months, did you have sex without a condom with someone whose HIV status you did not know?" asked to everyone, after the list and two unrelated items.

## Sample size inputs (for estimate-sample-size)
- Estimand: difference in mean counts between lists
- Expected prevalence: about 0.20 to 0.25 (illustrative); expected variance of the control count: moderate, four items with one negatively correlated pair; subgroups or arms: none
- The list estimate needs a multiple of the direct-question sample; the N is computed there, not here

## Analysis plan
- Difference in means with standard errors; software: the `list` package in R
- Design-effect test; floor and ceiling diagnostics (share of control respondents answering zero or four); list minus direct = measured sensitivity bias
- Decision rule: report both estimates; if the design-effect test fails or more than a small share of control respondents sit at zero or four, report the direct estimate as primary and the list estimate as exploratory

## What to check before relying on this
- Item 3 (radio) may be near-universal in some neighborhoods, which would push the control count toward the ceiling; confirm its prevalence in the pretest
- Whether respondents keep to "how many, not which" with a program enumerator present; the cognitive pretest of eight respondents settles this
```

Next step: `draft-cognitive-interview-script` to pretest the counting task and item wording; `estimate-sample-size` with the inputs above before the endline sample is fixed.
