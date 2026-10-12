# Worked example: Bangladesh mobile money enrollment endline, face-to-face to live calls

An illustrative run. The program, the factory, and every number are invented and marked illustrative; nothing here is a finding.

**Input:** an illustrative "Taka Direct" pilot enrolled garment workers at two factories in Gazipur into mobile money wage accounts by default. The baseline was 45 minutes face to face at the factory, 40 items, with a 5-point satisfaction showcard, a 10-rung "financial security" ladder, and a picture card of account uses. The endline must be by live call because the factories now restrict visits. Frame: 2,400 workers' numbers collected at baseline (illustrative); 61 percent women; 18 percent of women gave a number they described as a husband's or relative's phone (illustrative). Core decisions: whether workers kept the account, whether they use it to save, and whether they feel control over their wages. Enumerators speak Bangla; airtime incentives are affordable; about 150 face-to-face interviews at a community location near the factories are feasible.

```markdown
# Phone-mode instrument: Taka Direct endline

**Mode:** live call  **Face-to-face length:** 45 minutes  **Target call length:** 20 minutes (below the 30-minute ceiling; workers are called after shifts)
**Frame:** baseline numbers for 2,400 workers; respondent's own phone for 82 percent of women and 96 percent of men (illustrative); 18 percent of women gave a husband's or relative's number
**Why phone:** access; factories restrict visits

## 1. Core items kept, items dropped
| Item | Decision it feeds | Keep / drop / later wave | Why |
|---|---|---|---|
| Account still open; last transaction month | kept the account? | keep | primary outcome |
| Balance held back after wage day; deposits in the last month | uses it to save? | keep | primary outcome |
| Who decides how the wage is spent; the financial security ladder | control over wages? | keep | secondary outcome |
| Satisfaction with the account (showcard) | program experience | keep, converted | needed for the implement stage |
| Household asset list (12 items) | wealth covariate | drop | available from baseline |
| Detailed expenditure module (14 items) | consumption | later wave | 15 minutes alone; not needed for the three decisions |
| Anyone taken money from the account or pressured you for the PIN | account control | escalate (section 6) | sensitive on a shared phone |

## 2. Converted items
| Item | Face-to-face format | Phone format | Spoken wording |
|---|---|---|---|
| Satisfaction | showcard, 5 points | unfolding: direction, then intensity | "Overall, are you satisfied or dissatisfied with the account?" then "Is that very or somewhat?" |
| Financial security ladder | 10-rung picture | read-aloud scale, endpoints in words | "Imagine a ladder with ten steps. The bottom step, one, means you could not cover an unexpected cost of 2,000 taka at all; the top step, ten, means you could cover it easily. Which step are you on today?" |
| Account uses | picture card, pick all | short read list, yes/no each | "In the last month, did you use the account to: send money home? pay a bill? keep money aside? buy airtime?" |
| Deposits in the last month | written count | spoken count with an anchor | "Since the last wage day, how many times did you put money into the account, not counting the wage itself?" |

## 3. Consent script and audio instructions
"My name is <name> from <organization>. You took part in a survey at <factory> in <month>. Is this <respondent name>? ... We would like to ask about 20 minutes of questions about the wage account; you can stop at any time and you will receive 50 taka of airtime afterward whether or not you finish (illustrative amount). Is this a good time, and can you speak where others cannot hear you? ... For each question I will read the answer choices; tell me the one closest to your answer."

## 4. Call protocol
- Attempts: 5 per number, spread over after-shift evenings and the Friday off-day, no two on the same day
- Call-back rule: if the respondent asks for another time, that time becomes attempt 1 of a new series
- Replacement rule: a number is retired after 5 failed attempts or a confirmed wrong number; no replacement respondent, since the sample is a panel
- Enumerator language matching: Bangla; two enumerators with Sylheti and Chittagonian for workers who used them at baseline
- Incentive: 50 taka airtime (illustrative), sent within 24 hours of the call ending, including partial interviews
- Log per attempt: date, time, outcome code, who answered (respondent / other adult / child / no answer), language used, reason for call-back

## 5. Who you will reach
Women gave a non-own number more often than men (18 percent against 4 percent, illustrative), so the protocol asks for the respondent by name, never interviews the phone's owner in her place, and schedules a call-back when she is available. The log records who answered on every attempt. The frame will miss workers who changed numbers since baseline; the share is unknown and will be reported as an attrition category.

## 6. Sensitive items
| Item | Keep with privacy check / drop / escalate | Why |
|---|---|---|
| Anyone taken money or pressured you for the PIN | escalate | on a husband's phone the question can expose the respondent; the ethics board and a methodologist decide whether a version can be asked at all |
| Who decides how the wage is spent | keep with privacy check | asked only if the respondent confirmed she can speak privately; otherwise skipped and coded "not asked, privacy" |

## 7. Mode-effect check
150 workers drawn at random from the frame are interviewed face to face at the community location with the same core items and the same spoken wording. Items compared: account open, deposits in the last month, the ladder, satisfaction. Decision rule, pre-specified: if the phone and face-to-face shares differ by more than 10 percentage points on account open or deposits (illustrative threshold), the endline reports the face-to-face estimate as primary and the phone estimate as a sensitivity result.

## 8. Pretest
Eight phone cognitive interviews with baseline workers not in the endline sample; the ladder, the unfolding satisfaction item, and the deposit count are flagged for extra probes; handed to draft-cognitive-interview-script.

## What to check before relying on this
- Women who gave a husband's number: if call-backs fail for them at a higher rate, the endline under-represents the group the default enrollment was meant to protect
- The ladder: a ten-step scale read aloud is the item most likely to shift between modes; the 150-interview comparison is the check
```
