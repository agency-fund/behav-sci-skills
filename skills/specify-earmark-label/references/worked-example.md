# Worked example: a school-fees label for peri-urban workers in Uganda

Setting: an illustrative program ("Fees Ready", Wakiso district on the edge of Kampala) for casual workers (porters, boda riders, construction laborers) who pay school fees three times a year. The barrier diagnosis came from `decompose-comb-barriers` confirmed by interviews; the lever from `select-intervention-levers` (Environmental restructuring, BCT 12.5 Adding objects to the environment: a named savings pot). All numbers are illustrative, not findings.

**Inputs the user gave.** Target expense: Term 2 fees for one child, UGX 180,000 (illustrative), due 25 May. Confirmed barriers: fee money kept in the main mobile-money wallet is spent on daily costs, and relatives in the village ask for money about twice a month and are hard to refuse (interviews with 14 workers). Vehicles: the mobile-money operator offers a named savings sub-wallet with no withdrawal fee (confirm with the operator); most workers also keep a tin at home. Kin pressure: high; most are men whose wives do not control the wallet. Own money, not a transfer. Present bias was not confirmed as a barrier.

```markdown
# Earmark label specification

**Confirmed barrier:** Fee money held in the main wallet is spent on daily costs and lent to relatives who ask (Opportunity, social, and Motivation, automatic; 14 interviews, Wakiso, illustrative).
**Target expense:** Term 2 school fees for one named child, UGX 180,000, due 25 May.
**Whose money:** Own saving from daily and weekly pay.

## The pot
- **Vehicle:** A named sub-wallet inside the worker's existing mobile-money account, because it separates the sum from daily cash without a new account, and the balance is visible on the phone. The tin at home was rejected: it is visible to visitors and the interviews say that invites requests.
- **Visibility:** Visible to the worker on the phone; not visible to relatives. The label is for the worker's own refusal, not for display.
- **Label text:** "Fees: Brian, Term 2, UGX 180,000 by 25 May"
- **Raiding rule:** Soft. Withdrawal is allowed at any time without a fee; the confirmation screen restates the label and asks "take from Brian's fees?" and then lets the withdrawal through. No penalty, no delay.

## Lock or label
Label alone. Kin pressure is the confirmed barrier, so the label's job is to give the worker a reply ("that is Brian's fees money") and to keep the sum out of the balance relatives hear about. Present bias was not confirmed, so no lock is offered now; if the pilot shows raiding for non-emergencies, an opt-in lock is a separate decision for `design-commitment-device`.

## Liquidity check
Workers hold about three days of cash on average (illustrative). The sub-wallet is not the only buffer, because it stays withdrawable without a fee; the soft raiding rule is what keeps this from reproducing the Kenyan preventive-health backfire. The amount is set to the actual fee, not more, so the pot does not tie up cash beyond the need.

## Kin-pressure check
Requests come from relatives in the village about twice a month, mostly by phone. The field team confirms with 8 workers whether "that is Brian's fees money" is a reply they would give and whether it ends the request; if it does not, the label is kept but the program adds a named-child receipt the worker can forward, to be drafted by `draft-lever-content`.

## Delivery of the label
At opening by the agent at the work site; in the weekly balance SMS ("Brian's fees: UGX 92,000 of 180,000"); on the withdrawal confirmation screen; on the term-start receipt when the fees are paid from the pot.

## What to measure
- Balance in the sub-wallet on 25 May against the UGX 180,000 target
- Whether Term 2 fees were paid on time, from the school's register
- Emergency coping: any worker who reports going without treatment or food because the money felt locked (short follow-up call)

## Required pre-test
8 workers, shown the opening screen and the label cold: what is this money for, can you take it out, who can ask you for it. Pass: all 8 name the fees and say they can withdraw.

## What to check before relying on this
- The surplus assumption: that at least UGX 10,000 a week (illustrative) is available to set aside; from the interviews, not confirmed for the lowest earners.
- The kin-pressure assumption: that a named-child label ends a request rather than inviting a request for "Brian's" money; the 8-person check decides this.
```

**Where this run stopped.** It did not write the agent script or the SMS wording (`draft-lever-content`), did not design an opt-in lock (`design-commitment-device`), and did not add a condition or a matching payment (`design-incentive-scheme`).
