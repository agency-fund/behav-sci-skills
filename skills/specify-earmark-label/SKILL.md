---
name: specify-earmark-label
description: >-
  Use when money set aside for one thing keeps going to other things or to
  relatives, and the team wants to label it for its purpose without locking
  it: "can we name the account school fees", "should we call the transfer the
  education money", "how do we make this feel set aside". Also use when a
  program is choosing between a transfer with conditions and one that simply
  says what it is for, or is about to add a lock when the diagnosed problem is
  leakage, not temptation. Specifies the target expense, the visible pot, the
  label text, the raiding rule, and the liquidity and kin-pressure checks,
  drawing on mental accounting (Thaler), the Kenya safe-box trial (Dupas and
  Robinson), and Morocco's labeled cash transfer. Do not use when the person
  wants to be bound, with no withdrawal until a date or a stake they lose; use
  design-commitment-device instead. Not for a transfer paid only if a
  condition is verified (design-incentive-scheme), nor for writing the
  messages that carry the label (draft-lever-content).
license: CC-BY-4.0
metadata:
  title: Label money for one purpose without locking it
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "choice-architecture, commitment-devices, behavior-change-techniques"
  consumes: "intervention-levers, barrier-diagnosis"
  produces: "intervention-draft"
---

## What it does

Assigns an explicit purpose label to a sum of money or an account, held in a separate visible place, without enforcing the label.

The mechanism is mental accounting: people sort money into accounts by purpose and treat money in one account as not interchangeable with money in another, so a label makes a sum harder to spend on something else and gives a ready refusal when relatives ask ("that is the school money"). The output specifies the target expense, the pot, the label text, the raiding rule, and two checks (liquidity and kin pressure) that decide whether a label is enough or whether a lock, a condition, or a different lever is needed. It does not write the messages and it does not lock anything.

## When to use it

### Use it when
- Money set aside for one thing keeps going to other things, or to relatives who ask, and someone asks "can we label the account?", "should we name the box?", or "can we call the transfer the education money?"
- A program is about to pay a transfer and is deciding between conditions that someone must verify and simply telling recipients what the money is for at every touchpoint
- A team is about to add a lock, a penalty, or a withdrawal rule to a savings product when the diagnosed problem is leakage, not temptation
- A savings vehicle already exists (a mobile-money wallet, a group pot, a tin at home) and the question is how to make part of it feel set aside for one expense

### Do not use it when
- The person wants to be bound: no withdrawal until a date, a penalty for breaking the rule, a stake they lose. That is `design-commitment-device`, which handles opt-in, take-up, and what happens to people who commit and fail
- The transfer is to be paid only if a condition is met (attendance, a clinic visit) and someone has to verify it; that is `design-incentive-scheme`
- The team needs the words of the message, the sticker, or the agent script that carries the label; that is `draft-lever-content`, which takes this specification as its input
- The diagnosis is that no surplus exists after food and rent. A label reorganizes money; it does not create it. Go back to `select-intervention-levers` with that barrier

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The target expense in the person's own words (school fees, a clinic delivery, a latrine, seed), the amount, the date it falls due, and who it is for. A label on "savings" or "the future" is not a label.
2. **Required.** The confirmed barrier from the barrier diagnosis: the money is spent on other things, it is given to kin who ask, or it is never set aside at all. A label addresses the first two; the third needs a different lever.
3. **Required.** Where the money sits now and which vehicles exist: cash at home, a mobile-money wallet (and whether it offers named sub-wallets), a bank or cooperative account, a savings group, a box. The pot has to be one the person can actually open and see.
4. Optional. Kin and household pressure: who asks for money, how often, whether the person can refuse, and whether a spouse controls cash. This decides whether a label alone will hold.
5. Optional. Whether the money is the person's own saving or a transfer the program pays. A label on a transfer is placed by the program at every touchpoint; a label on own saving is placed by the person.

If 1 or 2 is missing, ask and stop. If 3 is missing, ask once; then proceed with a physical box as the assumed vehicle and flag it. If 4 is missing, assume moderate kin pressure and say so in the kin-pressure check. If 5 is missing, assume own saving.

## What it draws on

- Thaler, R. H. (1999). Mental accounting matters. *Journal of Behavioral Decision Making*, 12(3). https://doi.org/10.1002/(SICI)1099-0771(199909)12:3<183::AID-BDM318>3.0.CO;2-F
- Dupas, P., & Robinson, J. (2013). Why don't the poor save more? Evidence from health savings experiments. *American Economic Review*, 103(4), 1138–1171. https://doi.org/10.1257/aer.103.4.1138
- Benhassine, N., Devoto, F., Duflo, E., Dupas, P., & Pouliquen, V. (2015). Turning a shove into a nudge? A "labeled cash transfer" for education. *American Economic Journal: Economic Policy*, 7(3), 86–125. https://doi.org/10.1257/pol.20130225
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709
- Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity: A meta-analysis and a real-effort experiment. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x

Thaler's mental accounting is the theory: money is sorted into accounts by source and purpose and is not treated as fungible across them. The dossier carries it as a plan-only citation, so this skill uses it for the mechanism and quotes no number from it. Dupas and Robinson, in Kenya, found that a simple safe box raised health savings by 66%; earmarking helped only for emergencies or for people frequently "taxed" by kin, and earmarking for preventive health reduced savings in the working-paper version. That is the documented backfire: a label for a distant, non-urgent purpose ties up liquidity people fear they will need, so they save less rather than lock it away. Benhassine and colleagues, in Morocco's Tayssir program, found that an unconditional transfer merely labeled for education produced large gains in school participation; adding conditionality or paying mothers made almost no difference; parents came to value education more. A "76% dropout reduction" figure circulates for this study and is unverified; this skill does not quote it. The judgment calls this skill adds are: the expense must carry an amount and a date; the raiding rule is written down as soft by default; the liquidity check is mandatory because of the Kenyan backfire; the kin-pressure check decides between a label and a lock; and the lock itself is routed to `design-commitment-device`.

Discount published effects before planning on them. Both anchor trials are field RCTs, so they need less shrinkage than lab effects, but academic journal trials average 8.7 percentage points where nudge-unit trials average 1.4 (DellaVigna and Linos, 126 RCTs, 23 million people; about 70% of the gap is selective publication and low power), and a loss-framing effect of 0.33 SD in the lab was 0.02 SD in the field (Ferraro and Tracy). The Tayssir label rode on a transfer the program itself paid; a label on a person's own saving in a box is a different vehicle, so do not expect the same gains. Hand the numbers to `estimate-expected-effect` for a benchmark.

**WEIRD skew:** The theory comes from US data; the technique's evidence base is from low- and middle-income settings. What varies locally is whether a label is a credible refusal in the household: who may claim money, whether a wife may hold money a husband does not control, and whether a visible pot invites requests rather than deflecting them. **Non-WEIRD evidence:** Kenya (Dupas and Robinson; a safe box raised health savings 66%; earmarking helped for emergencies and for the kin-taxed, reduced savings for preventive health in the working paper); Morocco (Benhassine and colleagues; Tayssir; large school-participation gains from a label alone, almost no added effect from conditions). A user elsewhere should check the kin-pressure and liquidity assumptions with a short round of interviews before launch.

**Replication status:** Replicated in two strong LMIC RCTs in different domains (health saving in Kenya, schooling in Morocco), with a documented backfire condition when the label ties up liquidity; no meta-analysis in the sources this skill draws on.

## How to do it

1. **Carry the confirmed barrier over verbatim** and name the target expense in the person's words, with the amount and the due date. If the expense has no date, give it a trigger ("when the baby comes") so the account has an end.
2. **Choose the pot:** the most separate, visible vehicle the channel allows (a named mobile-money sub-wallet, a separate account, a box with the expense written on it, a group pot). Separate so the sum is not mixed with daily cash; visible so the person and, where it helps refusal, the household can see what it is for.
3. **Write the label text:** the expense, the person it is for, and the amount or date. Then write the raiding rule as soft by default: the person may take the money out, for an emergency, without a penalty. A hard rule is a commitment device and leaves this skill.
4. **Decide lock or label.** If the diagnosis includes temptation or present bias and the person wants to be bound, stop and hand to `design-commitment-device`. If the diagnosis is kin pressure, a label gives a refusal script; pair it with a lockable box only if the person asks for the lock.
5. **Run the liquidity check:** can the person still meet an emergency without raiding the pot? If not, the label will reduce saving, as it did for preventive health in Kenya; soften the label, lower the amount, or add an emergency pot beside it.
6. **Run the kin-pressure check:** who will see the pot, who will ask, and whether "that is the school money" is a credible refusal in this household. Name what the field team confirms with a handful of interviews.
7. **If the money is a program transfer,** put the label on the transfer itself: say who receives it and what it is for at enrollment, at each payment, and in each message, with no condition attached. A condition is `design-incentive-scheme`.
8. **Write the measures and the pre-test:** balance in the pot at the due date, spending on the target expense, and whether anyone went without in an emergency because the money felt locked. Then stop here; `draft-lever-content` writes the words that carry the label.

See `references/worked-example.md` for a complete run on school-fee saving among peri-urban workers in Uganda and `references/evidence-notes.md` for the sources with their verification state.

## Output template

```markdown
# Earmark label specification

**Confirmed barrier:** <leakage to other spending / requests from kin / never set aside; carried over verbatim with the evidence>
**Target expense:** <what, for whom, how much, due when>
**Whose money:** <own saving / program transfer / group pot>

## The pot
- **Vehicle:** <named sub-wallet, separate account, box, group pot; why this one given the channels available>
- **Visibility:** <who sees it, and whether visibility helps or invites requests>
- **Label text:** "<the expense, the person, the amount or date>"
- **Raiding rule:** <soft: withdrawal allowed, emergencies expected, no penalty; or "hard rule wanted: hand to design-commitment-device">

## Lock or label
<the decision and the reason: present bias confirmed and the person wants binding -> design-commitment-device; kin pressure -> label plus refusal script; neither -> label alone>

## Liquidity check
<what buffer exists for emergencies; whether the pot would be the only buffer; what was softened as a result>

## Kin-pressure check
<who asks, how often, who controls cash; whether the label is a credible refusal here; what the field team confirms, with how many interviews>

## Delivery of the label
<where the label appears: at opening, on the box, in each transfer message, on the receipt; who says it>

## What to measure
- <balance in the pot at the due date>
- <spending on the target expense>
- <emergency coping: anyone who went without because the money felt locked>

## Required pre-test
<n members of the audience, shown the pot and label cold: what is this money for, can you take it out, who can ask you for it; pass criterion>

## What to check before relying on this
- <the surplus assumption>
- <the kin-pressure assumption>
```

## Where it goes wrong

- **Label with a lock.** Specifying a pot the person cannot raid "so the label sticks" turns an earmark into a commitment device without the opt-in, the take-up estimate, and the plan for failers that `design-commitment-device` requires. The raiding rule is written down so this cannot happen by omission.
- **Label on no surplus.** If the diagnosis is "nothing left after food", a label reorganizes nothing. Send it back; the barrier is income or expense, not accounting.
- **Vague label.** "Savings", "the future", or "for the family" creates no mental account. A label works when it names one expense with an amount and a date, and the output refuses to leave those placeholders blank.
- **Ignoring the household.** Treating the saver as an individual when a spouse or kin control cash. A label that one household member uses to refuse another can create conflict, which is why the kin-pressure check is mandatory and names who the field team talks to.
- **Preventive-health earmark by default.** Labeling for a distant, non-urgent purpose in a population with no emergency buffer reproduces the Kenyan backfire. The liquidity check must say what the person does in an emergency.
- **Quoting the unverified number.** The "76% dropout reduction" attributed to Tayssir is unverified. Say "large gains in school participation" and nothing more precise.

## When to bring in a specialist

Tell the user to consult the relevant specialist when:
- The label is for preventive or future health spending, or any distant purpose, in a population with no emergency buffer; this is the documented backfire, and a behavioral scientist or financial-inclusion specialist should judge whether a label, an emergency pot, or a different lever is right
- Kin pressure runs along gender lines (a woman labeling money a husband claims); a gender or safeguarding specialist and a local researcher review the label and its visibility before launch
- The money is a government or program transfer; the label changes the program's public meaning and who is seen to deserve it, so policy and legal review comes before the design is final, alongside `audit-intervention-ethics`
- The vehicle is a regulated product (a named account with fees, limits, or interest); a compliance lead checks that the label and the raiding rule are true to the product's terms

Bring them: the confirmed barrier, the pot specification with its label and raiding rule, and the liquidity and kin-pressure checks.
