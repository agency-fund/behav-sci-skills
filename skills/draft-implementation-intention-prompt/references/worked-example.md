# Worked example: a plan prompt for reporting HIV self-test results in Lagos, Nigeria

Illustrative. The program, the pharmacies, and every number below are invented to show a complete run of the skill; none is a finding. The target behavior came from `define-key-behavior`, the barrier from `decompose-comb-barriers` confirmed by an exit survey, and the lever brief from `select-intervention-levers`.

**Inputs supplied by the user:** 40 community pharmacies distribute HIV self-test kits; each kit carries a referral card asking the user to report the result by a free USSD code within 7 days, any day, any hour, from any phone; an exit survey of 320 buyers found 82% say they will report, USSD logs show about 19% do (illustrative); the lever brief selected action planning; the pharmacist spends about a minute with each buyer; most buyers own a phone; literacy in English or Yoruba is sufficient for a short card.

```markdown
# Implementation intention prompt

**Target behavior:** Buyers of an HIV self-test kit at the 40 partner pharmacies in Lagos report their result through the free USSD code within 7 days of buying the kit.
**Intention check:** 82% of 320 buyers in the exit survey said they will report; 19% of kits sold in the same period have a USSD report (illustrative). The gap is between intending and doing, not a missing intention. Cost and access were ruled out: the code is free and works from any phone at any hour.
**Action type:** One-off. Window: 7 days from purchase, any hour; the test is done wherever the buyer chooses (most say at home, alone or with a partner); reporting takes one USSD session from the buyer's own phone; nothing to bring.

## The prompt (working copy)
Printed on the referral card the buyer keeps, filled in with the pharmacist:

"I will do my test on ______ (day and date) at ______ (time) at ______ (place).
Right after I read the result, I will dial *XXX*XX# from this phone to report it.
If I am not alone, the person with me will be ______."

## Why each element is there
- **Date:** Fixes the occasion within the 7-day window; "this week" is not accepted on the card.
- **Time:** The flu-shot trial's date-only prompt added 1.5 points (not significant) against 4.2 for date plus time; the time blank is what makes the plan a cue.
- **Place:** Testing is private; the place blank lets the buyer pick somewhere they can read the result and dial at once, which is also where the card should be kept.
- **How / with whom:** Used because some buyers test with a partner; naming that person settles whether the result is reported in private or together, and avoids the plan stalling on a conversation.

## Delivery
- **Rides on:** The pharmacist's minute at the counter when the kit is handed over.
- **Asked by:** The pharmacist, who fills the blanks with the buyer and reads the plan back once.
- **When:** At purchase, which is the start of the 7-day window; the plan is concrete because the buyer is holding the kit, and all dates in the window are still open.
- **What the person keeps:** The referral card with the filled-in plan, inside the kit box.

## Boundary checks
- **One-off:** Confirmed; one kit, one result, one report.
- **Organic planning:** Buyers who test with a partner may already have agreed when; the voting trial found half the effect where people planned together. The exit survey did not ask this; see open questions.
- **Numeric goal:** None used. The action is not a number.

## Expected effect
Gollwitzer and Sheeran (2006): d = 0.65 across 94 tests, probably inflated relative to field trials. Milkman et al. (2011): +4.2 points on a 33.1% base for date plus time. Nickerson and Rogers (2010): +4.1 points overall, +9.1 in single-voter households. The South Africa self-test reporting trial (Buttenheim et al., 2022) exists but its result is not available to this skill, so no number is borrowed from it. Academic trials average 8.7 points against 1.4 in nudge-unit trials (DellaVigna & Linos, 2022). Plan for 2 to 5 percentage points of additional reporting on the 19% base (illustrative planning range), lower if most buyers test with a partner. This is a cheap add-on to an existing contact, not a program on its own.

## Required pre-test
10 buyers across 3 pharmacies fill in the card cold with the pharmacist, in the buyer's preferred language. Pass = all 10 cards hold a day and date inside the 7-day window, a clock time, and a named place; and when asked a day later, at least 8 of 10 can say their plan without looking at the card.

## What to check before relying on this
- Whether the 82% intention figure holds when the question names a day ("will you report this week?") rather than "will you report".
- The share of buyers who test with a partner, which sets the organic-planning discount.
- Whether the pharmacist's minute survives a busy counter; if the card is handed over unfilled, the technique was not delivered.
- Who sees the card: it names a test date and place for an HIV test, so the box, not a wallet, is where it stays.
```
