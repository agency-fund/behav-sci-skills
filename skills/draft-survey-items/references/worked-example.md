# Worked example: Western Kenya fertilizer-timing survey block

An illustrative run. The program and the numbers are invented; nothing here is a finding.

**Input (from the measurement plan of an illustrative "Kakamega Early Fertilizer" pilot):** four constructs. (A) Timing of last season's fertilizer purchase relative to the agricultural calendar; feeds the decision whether late purchase is common enough to target. (B) Perceived difficulty of putting money aside for fertilizer at harvest; feeds the choice between a savings lever and a price lever. (C) Empirical expectation of what other farmers in the village do; feeds whether a norm message is plausible. (D) Intention to buy before planting next season; the pre-intervention baseline for the primary outcome. Respondents: smallholder maize farmers in Kakamega County, mostly women, primary schooling, interviewed at home by enumerators reading aloud in Kiswahili or Luhya (translation is a later step; items are drafted in English). Block: at most 8 items, about 5 minutes, after the plot roster and before input-cost questions.

```markdown
# Draft survey items: Kakamega Early Fertilizer baseline, fertilizer-timing block

**Respondents:** smallholder maize farmers, Kakamega County; mostly women; primary schooling; Kiswahili or Luhya  **Mode:** enumerator read-aloud, at home
**Length budget:** 8 items, about 5 minutes  **Position:** after the plot roster; before input-cost questions
**Constructs:** (A) purchase timing last season; (B) difficulty of putting money aside at harvest; (C) expectation of other farmers; (D) intention for next season

## Items by construct
### (A) Purchase timing: when the fertilizer used at planting was bought, relative to the previous harvest and planting
**Item A.1:** Think about the long rains of this year. When did you buy the fertilizer you used at planting?
- Options: before the previous harvest / between the harvest and planting / at planting time / I did not buy fertilizer for the long rains
- Type: bounded behavior report
- Intended meaning: the timing of the purchase for the most recent long-rains season only, not what the farmer usually does
- Design notes: season named rather than "last season"; "usually" avoided; the no-purchase option prevents a forced timing answer

**Item A.2:** (if bought) Did you buy all of it at one time, or in parts?
- Options: all at one time / in parts
- Type: bounded behavior report
- Intended meaning: whether the purchase was split, which changes what "timing" means for the program
- Design notes: asked only after A.1 to keep A.1 single-idea

### (B) Difficulty of putting money aside: how hard the farmer finds it to hold harvest money for fertilizer
**Item B.1:** After the harvest, how hard is it for you to put money aside for the next season's fertilizer?
- Options: not hard / a little hard / very hard
- Type: construct-specific rating
- Intended meaning: the farmer's own assessment of difficulty, whatever the reason
- Design notes: replaces "I find it hard to save for fertilizer (agree/disagree)"; three labeled points; no midpoint, because "a little hard" is the middle

**Item B.2:** What is the biggest reason it is hard?
- Options: the money goes to school fees / the money goes to food / other people ask me for the money / the maize price is low at harvest / another reason
- Type: single-choice reason
- Intended meaning: the main competing use of harvest money, one reason only
- Design notes: asked only if B.1 is "a little hard" or "very hard"; options from the diagnose-stage interviews; "another reason" recorded verbatim

### (C) Expectation of others: how many other farmers the respondent believes buy before planting
**Item C.1:** Think of ten farmers like you in this village. How many of the ten do you think buy their fertilizer before planting time?
- Options: a number from 0 to 10
- Type: expectation
- Intended meaning: the empirical expectation about similar farmers, not approval of early buying
- Design notes: "farmers like you" sets the reference group; a count out of ten replaces a percentage

### (D) Intention: whether the farmer plans to buy before planting next season
**Item D.1:** For the next long rains, do you plan to buy your fertilizer before planting time?
- Options: no / not sure / yes
- Type: bounded intention
- Intended meaning: a plan for the named season, not a general attitude toward early buying
- Design notes: "not sure" kept because the construct has a real middle

**Item D.2:** (if yes) When do you plan to buy it?
- Options: right after this harvest / in the months between harvest and planting / at planting time
- Type: bounded intention
- Intended meaning: the planned timing, in the same categories as A.1 so the two can be compared

## Order and context
| Position | Item | Why here | Earlier item that could shape the answer |
|---|---|---|---|
| 1 | A.1 | factual report first, before any evaluative item | none |
| 2 | A.2 | follows A.1 directly | none |
| 3 | B.1 | difficulty after the behavior report, so it is anchored to practice | A.1: a farmer who reported buying late may rate difficulty higher to explain it; noted for the pretest |
| 4 | B.2 | follows B.1 | none |
| 5 | D.1 | intention after difficulty, before the expectation item | A.1: a late buyer may state an early intention; the pretest judgment probe checks this |
| 6 | D.2 | follows D.1 | none |
| 7 | C.1 | last, so the "ten farmers" frame does not prime the intention items | none |

## Enumerator read-aloud version
"Now I will ask about the fertilizer you used for the long rains this year. There are no right or wrong answers." (A.1) "When did you buy the fertilizer you used at planting? Was it before the previous harvest, between the harvest and planting, at planting time, or did you not buy fertilizer for the long rains?" (A.2, if bought) "Did you buy all of it at one time, or in parts?" (B.1) "After the harvest, how hard is it for you to put money aside for the next season's fertilizer? Not hard, a little hard, or very hard?" (B.2, if a little or very hard) "What is the biggest reason it is hard? The money goes to school fees, the money goes to food, other people ask you for the money, the maize price is low at harvest, or another reason?" (D.1) "For the next long rains, do you plan to buy your fertilizer before planting time? No, not sure, or yes?" (D.2, if yes) "When do you plan to buy it? Right after this harvest, in the months between harvest and planting, or at planting time?" (C.1) "Now think of ten farmers like you in this village. How many of the ten do you think buy their fertilizer before planting time? Give me a number from zero to ten."

## Design check
| Rule | Pass? | Items to fix |
|---|---|---|
| One idea per item | yes | none (A.2 and B.2 split out from their parents) |
| No agree/disagree format | yes | none |
| Every scale point labeled; three to five points when read aloud | yes | none |
| No reverse-keyed or double-negative items | yes | none |
| Recall window bounded | yes | none (season named in A.1 and D.1) |
| Sensitive behaviors routed to an indirect design | yes | none; B.2's "other people ask me for the money" is kept as an option, flagged for the pretest judgment probe |

## Next step
Items and intended meanings go to draft-cognitive-interview-script; eight interviews with farmers in two villages, before translation into Kiswahili and Luhya with translate-survey-instrument.

## What to check before relying on this
- Whether "put money aside" is heard as formal saving only (bank, M-Pesa) or includes keeping cash or grain back; if the former, B.1 under-reports
- Whether the "ten farmers like you" frame works for respondents who have not answered a count-of-others question before; C.1 gets extra probes
```
