# Worked example: daily iron-folate tablets in pregnancy, Dedza district, Malawi

An illustrative run. The program (call it "Mayi Wathanzi", illustrative) supports antenatal care at four rural clinics in Dedza district, Malawi. Its social norm diagnosis (from `diagnose-social-norm`) called not taking the iron-folate tablets a probable social norm with low confidence: women privately favor the tablets, but believe their mothers-in-law and the older women of the village disapprove of "hospital medicine" in pregnancy, and the conditionality branch was reached by only a few respondents. All numbers below are illustrative, not findings.

**Answers to Before you start:** (1) pregnant women enrolled at the four clinics; taking one iron-folate tablet every day from the first antenatal visit; the decision moment is each morning at home, with the month's supply in the house. (2) Reference group: the woman's mother-in-law and the older women of her village. (3) Respondents: pregnant women aged 18 to 40 at antenatal visits, mostly primary schooling, Chichewa, interviewed one to one by a female surveyor reading aloud, in a private room at the clinic. (4) Not harmful or stigmatized; the household authority is not present at the clinic interview. (5) Default: one version per respondent, two-by-two. (6) About 600 respondents over three months; one practice.

```markdown
# Norms vignette: taking iron-folate tablets daily in pregnancy

**Practice and dilemma:** a pregnant woman given a month's supply of iron-folate tablets at her first antenatal visit decides each morning whether to take one
**Reference group named in the cues:** her mother-in-law and the older women of her village
**Respondents and mode:** pregnant women 18 to 40 at antenatal visits; primary schooling; Chichewa; read aloud one to one by a female surveyor in a private room
**Design:** two-by-two between-respondent; versions: 4
**Sensitivity:** none stated; questions asked as written

## Personal normative belief (asked before the scene)
"Do you yourself think a pregnant woman like Chikondi should take the tablets from the clinic every day?" Options: yes, she should; it is up to her; no, she should not

## Base scene (identical in every version)
"Chikondi is four months pregnant with her second child. She lives with her husband and his mother in a village near Dedza. At her first visit to the clinic the nurse gave her a packet of tablets and told her to take one every morning until the baby is born. The packet is on the shelf at home. This morning Chikondi is deciding whether to take a tablet."

## Cue sentences
| Factor | Level A | Level B |
|---|---|---|
| Empirical (what others do) | "Most pregnant women in her village take the tablets every day." | "Most pregnant women in her village do not take the tablets." |
| Normative (what others approve) | "Her mother-in-law and the older women of the village think a pregnant woman should take the tablets from the clinic." | "Her mother-in-law and the older women of the village think a pregnant woman should not take tablets from the clinic." |

## Versions
- V1: base + empirical A + normative A
- V2: base + empirical A + normative B
- V3: base + empirical B + normative A
- V4: base + empirical B + normative B

## Questions after every version
1. "What will Chikondi do this morning?" Options: take the tablet; not take it; cannot say
2. "What would most pregnant women in her village do in her place?" Options: take the tablet every day; take it some days; not take it
3. "If Chikondi takes the tablet every day, what would her mother-in-law and the older women think of her?" Options: they would approve; they would not mind; they would disapprove

## Randomization
Individual respondents; versions generated in advance on the tablet by respondent ID, balanced within surveyor so each surveyor delivers all four versions in near-equal numbers; the version is stored with the record; the surveyor reads the version shown and does not choose it.

## Analysis plan
- Outcome: share answering "take the tablet" to question 1, by version
- Empirical-cue effect: V1 + V2 versus V3 + V4; normative-cue effect: V1 + V3 versus V2 + V4; interaction
- Reading: a shift with the empirical cue only means a descriptive norm; a shift with the normative cue means a social norm held by the mother-in-law and older women; no shift with either means a custom or a moral rule, read with the personal belief question (if most say "she should" and nothing shifts, the diagnosis's low-confidence call is not supported)
- Sample per version: about 150 (illustrative; from a sample-size calculation for a difference in shares between two groups of 300)

## What to check before relying on this
- The empirical cue "most pregnant women do not take the tablets" may be heard as news about side effects rather than as what others do; the pretest should probe what respondents understood it to mean
- Whether respondents answer about Chikondi or about themselves; add the pretest probe "when you answered, were you thinking about Chikondi or about yourself?"
```

Next step: `draft-cognitive-interview-script` to pretest the base scene, the cue sentences, and the three questions with eight respondents in Chichewa before the survey is built; the analysis then feeds back into the `diagnose-social-norm` call.
