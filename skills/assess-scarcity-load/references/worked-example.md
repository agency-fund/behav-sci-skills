# Worked example: commitment-savings enrollment drive, Butuan, Mindanao, Philippines

An illustrative run, not a real assessment. The bank, the take-up figure, and the calendar are invented to show the shape of the output. The target behavior came from `define-key-behavior`; the calendar rows came from the user and from an audience and context brief (`map-audience-context`).

**Input summary (illustrative):** a rural bank runs a June enrollment drive for a commitment savings account (named goal, target amount, lock-in date, opened at the branch with a two-page form). Take-up is about 12%, lowest among farming clients. Clients are small rice farmers (harvest sales in April and October, input loan repaid at harvest) and sari-sari store owners (daily cash). School enrollment fees fall in June; the town fiesta is in August. The bank can move the drive, change the form, or both.

```markdown
# Scarcity load assessment

**Behavior:** Existing clients of the bank's Butuan branch (small rice farmers and sari-sari store owners) open a commitment savings account, with a named goal, a target amount, and a lock-in date, at the branch, during the June enrollment drive.
**The ask as experienced:** Arrives as a branch poster and a text in the first week of June, deadline end of June; requires having: a free morning and fare to town; remembering: the drive dates and the account documents; calculating: an affordable monthly amount; comparing: lock-in dates against school fees, fiesta, and harvest; deciding: a goal, an amount, a date; then a two-page form at the counter.

## Income and expense calendar
| Period | Inflows (source, timing, reliability) | Predictable outflows | Participants call it | Source of this row |
|---|---|---|---|---|
| April | Rice harvest sales (farmers; one lump sum, weather-dependent) | Input loan repayment (farmers) | slack for a few weeks after sale | user; audience brief |
| May | Store income (owners; daily, steady); farmers draw down harvest cash | Land preparation, seed, fertilizer (farmers) | normal (owners), tightening (farmers) | audience brief |
| June | Store income only | School enrollment fees, uniforms, supplies (all) | tight (all; worst for farmers) | user |
| July | Store income only | Household running costs | tight (farmers), normal (owners) | assumed |
| August | Store income rises around fiesta | Fiesta spending (all) | tight (all) | user |
| September | Store income only | Household running costs | tight (farmers), normal (owners) | assumed |
| October | Second rice harvest sales (farmers) | Input loan repayment (farmers) | slack for a few weeks after sale | user; audience brief |
| November to March | Store income (owners); little for farmers until April | Christmas (December); planting inputs (January) | normal (owners), tight (farmers, January to March) | assumed |

## Where the ask lands
June: two months after the April harvest cash, after the loan repayment and planting inputs have been paid, in the month school fees fall due. For farming clients this is near the tightest point of the first half of the year; for store owners it is tight but cushioned by daily cash. The rating differs by subgroup.

## Demands of the ask
| Demand | Count and list | Could the program hold it? |
|---|---|---|
| Things to remember | 2: the drive dates; the documents to bring | reminder text with a document list; or enroll at the harvest-payment visit the client already makes |
| Calculations | 1: an affordable monthly amount against an irregular income | a default amount (a small share of the last harvest payment, or a flat small sum) the client can change |
| Options to compare | 1: lock-in dates against fees, fiesta, harvest | a default lock-in date just before school fees, offered as the suggestion |
| Deadlines | 1: end of June | drop the deadline; keep the account open to join year-round, with a drive timed to harvest |

## Load rating
**High** for farming clients, because the ask lands in a tight month and demands a calculation plus a comparison plus two things to remember. **Medium** for store owners, because the month is tight but the daily cash cushions it, and the demands are the same. Confidence: calendar rows for April, June, August, and October are from the user and the audience brief; the others are assumed. Rubric: judgment aid, not a validated scale.

## Recommendations, in order
1. Move: run the drive in the two to three weeks after the April and October harvest sales, after the input loan is repaid; for store owners, any month outside June and August.
2. Simplify: offer a default amount and a default lock-in date (before next June's fees) that the client can change; shorten the form to what the account needs.
3. Split: open the account at the harvest-payment visit with the defaults; let the client name the goal and adjust the amount later, by text or at the next visit.
4. Remind: only after 1 to 3; one text a week before the harvest-period drive, with the document list.
5. If the program controls a payment: the bank pays out harvest proceeds for some clients; offer the account at that counter, at that moment.

## Is the real constraint money?
Partly. Farming clients have a surplus only in the weeks after each harvest sale; outside those weeks, a simpler form will not create money to save. The recommendations above work for those weeks. If a client's harvest proceeds are fully absorbed by the loan repayment and inputs, the constraint is money, and the question becomes the loan terms, which belong to the bank's leadership, not to this assessment.

## What to check before relying on this
- The assumed rows (May, July, September, November to March); confirm with five to ten clients from each subgroup.
- Whether farmers who repay the loan at the bank's counter actually have cash left at that moment, or whether the repayment takes all of it.
- Whether store owners' income really rises around fiesta or is consumed by it.
```

The exact week of the post-harvest drive, and what the text says, are `choose-delivery-moment`'s and `draft-lever-content`'s calls; this assessment hands them the load map.
