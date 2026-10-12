---
name: design-incentive-scheme
description: >-
  Use when the team has decided to pay or reward people for a behavior and
  needs the terms: "how much should we pay", "conditional or unconditional",
  "should we run a lottery", "what happens when the money stops". Also use
  when a reward is about to be set by budget or guesswork, or a conditional
  transfer has no plan to verify the condition. Specifies the size, form,
  timing, condition, removal plan, crowding-out check, ethics, and cost of a
  reward for one verifiable behavior, drawing on the cash-transfer and health-
  incentive reviews (Baird et al.; Mantzari et al.), Rajasthan's immunization
  camps, and the crowding-out literature (Gneezy, Meier and Rey-Biel). Do not
  use when the reward is non-financial and visible (a bracelet, public
  recognition); use design-social-recognition instead. Not for a transfer
  merely labeled for a purpose with no condition (specify-earmark-label), a
  stake the person puts up (design-commitment-device), or writing the voucher
  or message (draft-lever-content).
license: CC-BY-4.0
metadata:
  title: Design a reward for one verifiable behavior
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "incentives, behavior-change-techniques, cost-effectiveness"
  consumes: "intervention-levers, barrier-diagnosis"
  produces: "intervention-draft"
---

## What it does

Specifies the terms of a reward for one verifiable behavior, from its size to what happens when it stops.

The mechanism: a reward raises the immediate, certain payoff of a behavior whose benefits are delayed or uncertain, and offsets the hassle cost (travel, lost wages, fees) that stops people who already intend to act. That is why incentives work best for one-off actions with a clear hassle cost (an immunization, an enrollment, a test) and why their effects decay when they are withdrawn. The output is a scheme specification with its ethics and cost lines, not the message and not the budget.

## When to use it

### Use it when
- `select-intervention-levers` has selected Incentivization and someone asks "how much should we pay?", "cash, lentils, or airtime?", "conditional or unconditional?", "should we run a lottery?", or "what happens when the money runs out?"
- A reward amount is about to be set by what the budget allows or by guesswork, with no reference to what the behavior costs the person
- A conditional cash transfer is proposed and nobody has said who verifies the condition, what it costs to verify, or who is excluded by it
- An incentive has been running and the team wants to end it, taper it, or has noticed the effect fading

### Do not use it when
- The reward is non-financial and visible (a bracelet, a certificate, a name read out at a meeting); that is `design-social-recognition`, whose mechanism is signaling to others, not payoff
- The transfer is simply labeled for a purpose, with no condition and no verification; that is `specify-earmark-label`
- The stake is the person's own money or reputation, forfeited if they fail; that is `design-commitment-device`
- The team needs the words of the voucher, the SMS, or the agent script; that is `draft-lever-content`, which takes this specification as its input
- The barrier is supply (no vaccines, no teacher, no stock); an incentive cannot fix it. Go back to `select-intervention-levers`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The one behavior to reward as who, what, when, and how it will be verified (a register, a card stamp, a receipt, a visit, a photo), with the cost of one verification. If the behavior cannot be verified, or verification costs more than the reward, say so and stop: an incentive for an unverifiable behavior pays for reporting, not doing.
2. **Required.** The confirmed barrier and the lever brief that chose Incentivization over the other functions. If the barrier is access or supply, stop and send it back.
3. **Required.** Who pays, the budget per person and in total, and the planned end date. An incentive without an end date is a subsidy, which is a policy decision rather than a technique.
4. **Required.** The audience's typical daily income and the hassle cost of the behavior: travel time and fare, wages lost, fees. The reward is sized against these, not set in the abstract.
5. Optional. Whether recipients are public servants, program staff, or volunteers, and whether the behavior currently runs on an intrinsic or prosocial motive that money could replace.

If 1, 2, or 3 is missing, ask and stop. If 4 is missing, ask once; then proceed with the amount expressed as a multiple of the hassle cost rather than a currency figure, marked for the field team to fill. If 5 is missing, assume community members, not staff, and say so.

## What it draws on

- Baird, S., Ferreira, F. H. G., Özler, B., & Woolcock, M. (2014). Conditional, unconditional and everything in between: A systematic review of the effects of cash transfer programmes on schooling outcomes. *Journal of Development Effectiveness*. https://doi.org/10.1080/19439342.2014.890362
- Mantzari, E., et al. (2015). Personal financial incentives for changing habitual health-related behaviors: A systematic review and meta-analysis. *Preventive Medicine*. https://doi.org/10.1016/j.ypmed.2015.03.001
- Gneezy, U., Meier, S., & Rey-Biel, P. (2011). When and why incentives (don't) work to modify behavior. *Journal of Economic Perspectives*, 25(4), 191–210. https://doi.org/10.1257/jep.25.4.191
- Banerjee, A. V., Duflo, E., Glennerster, R., & Kothari, D. (2010). Improving immunisation coverage in rural India: Clustered randomised controlled evaluation of immunisation campaigns with and without incentives. *BMJ*, 340, c2220. https://doi.org/10.1136/bmj.c2220
- Gibson, D. G., et al. (2017). Mobile phone-delivered reminders and incentives to improve childhood immunisation coverage and timeliness in Kenya (M-SIMU): A cluster randomised controlled trial. *The Lancet Global Health*, 5(4), e428–e438. https://doi.org/10.1016/S2214-109X(17)30072-4
- Banerjee, A., Chandrasekhar, A. G., Dalpath, S., Duflo, E., Floretta, J., Jackson, M. O., et al. (2025). Selecting the most effective nudge: Evidence from a large-scale experiment on immunization. *Econometrica*, 93(4), 1183–1223. https://doi.org/10.3982/ECTA19739
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709
- Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity: A meta-analysis and a real-effort experiment. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x

Baird and colleagues (35 studies, 75 reports) found that unconditional or unmonitored transfers raised the odds of school enrollment by 18 to 25%, explicitly monitored conditional transfers by about 60%, with effects on test scores small at best: the condition and its monitoring carry weight, and the incentive moves the rewarded action more than the outcome behind it. Mantzari and colleagues (34 RCTs, habitual health behaviors) report OR 1.53 for outcomes up to 18 months and OR 2.11 three months after the incentive ended, larger under high deprivation (OR 2.17). Banerjee, Duflo, Glennerster and Kothari in Rajasthan: full immunization reached 39% with reliable camps plus a small in-kind reward (lentils), against 18% with camps alone and 6% in control (RR 6.7 versus control), and the cost per fully immunized child fell from $55.83 to $27.94. Gneezy, Meier and Rey-Biel review when incentives fail: a payment can crowd out intrinsic motivation, and its effect often dissipates when it stops. M-SIMU in Kenya found SMS plus incentives improved coverage and timeliness in a high-coverage setting (effect size unverified), and the Haryana trial found incentives plus ambassadors plus SMS raised immunizations 44% (secondary source per the dossier). The judgment calls this skill adds: verification is settled before any amount; the amount is written as a multiple of the hassle cost and a share of daily income; certain and immediate is the default form, because the lottery meta-analyses in the planning material have unverified authors and are not cited, and the one US "regret lottery" the dossier records found no pooled effect (no verified citation; unverified, author to confirm); the removal plan is mandatory; and payments to the poor or to public servants escalate.

Discount published effects before planning on them. Academic journal trials average 8.7 percentage points where nudge-unit trials average 1.4 (DellaVigna and Linos, 126 RCTs, 23 million people; about 70% of the gap is selective publication and low power), and a loss-framing effect of 0.33 SD in the lab was 0.02 SD in the field (Ferraro and Tracy). The Rajasthan ratio sits on a 6% base with reliable camps already in place; the schooling figures are changes in odds, not percentage points. Plan on a fraction of these and hand them to `estimate-expected-effect` for a benchmark.

**WEIRD skew:** The verified non-WEIRD evidence is the immunization trials in India and Kenya. The dossier does not list the countries of the cash-transfer programs in the schooling review, where the Mantzari trials ran, or the settings of the studies Gneezy and colleagues review, so treat those numbers as of unstated origin. **Non-WEIRD evidence:** India (Rajasthan: full immunization 39% with camps plus lentils versus 18% and 6%; Haryana: +44% from a bundle, secondary source); Kenya (M-SIMU; effect size unverified); the cash-transfer programs in Baird and colleagues (countries not listed in the dossier). What varies locally is what counts as a fair amount, whether cash to households is acceptable or in-kind is preferred, and whether paying health workers or officials is legal.

**Replication status:** Replicated for one-off health actions and for enrollment, with crowding out of intrinsic motivation and decay after removal documented; the size of the difference between certain rewards and lotteries is unverified in the sources this skill draws on.

## How to do it

1. **Carry the behavior over verbatim** and write the verification method, its cost per check, and who does it. "Done" must be observable by someone other than the person rewarded; if it is not, stop here and send the behavior back to `define-key-behavior` for a verifiable proxy.
2. **Check the supply side:** can everyone who wants to comply actually do so (stock, staff, opening hours)? The Rajasthan reward worked on top of reliable camps, never instead of them; write what was fixed first.
3. **Size the reward** against the hassle cost and daily income: enough to cover the hassle with a margin, written as a multiple of the hassle cost and as a share of daily income. A reward that is a large share of income is an offer the poor cannot refuse; that is an escalation, not a design choice.
4. **Choose the form and timing:** cash, in-kind, or airtime, paid at verification. Certain and immediate is the default, because the verified evidence is for certain rewards and the lottery evidence is unverified; in-kind (the lentils) where cash is sensitive or where it feeds the household rather than the hassle.
5. **Decide whether to monitor the condition.** Monitored conditions raised schooling effects most in the review, but monitoring costs money and excludes those who cannot comply; if monitoring is unaffordable or exclusion unacceptable, a labeled unconditional transfer (`specify-earmark-label`) is the alternative.
6. **Plan the removal:** the end date, taper or stop, what is expected after (decay is the documented pattern), what carries the behavior afterward (habit, a reminder, a norm), and the follow-up measure months after the end.
7. **Run the crowding-out check:** is there an intrinsic, religious, or prosocial motive already carrying the behavior, or are recipients volunteers or staff? If so, prefer `design-social-recognition` or escalate; write what to watch for after removal.
8. **Write the ethics and cost lines:** coercion (share of income, refusability), fairness to non-recipients, legal review for public servants or government transfers, routed to `audit-intervention-ethics`; cost per verified behavior, routed to `estimate-cost-effectiveness`. Then stop here; `draft-lever-content` writes the voucher and the message.

See `references/worked-example.md` for a complete run on HIV self-test result reporting in Lagos and `references/evidence-notes.md` for the sources with their verification state.

## Output template

```markdown
# Incentive scheme specification

**Rewarded behavior:** <who, what, when; carried over verbatim>
**Verification:** <how, by whom, cost per check; what counts as done; what cannot be verified and is therefore not rewarded>
**Confirmed barrier:** <carried over; why Incentivization was chosen over the other functions>
**Supply check:** <can everyone who wants to comply do so; what was fixed first>

## The reward
| Element | Specification | Reason |
|---|---|---|
| Size | <amount; as a multiple of the hassle cost; as a share of daily income> | <...> |
| Form | <cash / in-kind / airtime; certain, not a lottery> | <...> |
| Timing | <paid at verification; delay in days> | <...> |
| Condition | <the exact condition; monitored or not; who checks> | <...> |
| Recipient | <who receives it: the person, the mother, the household head> | <...> |

## Monitoring decision
<monitor the condition or not; cost per person; who the condition excludes and what happens to them>

## Removal plan
- **End date:** <date>
- **Taper or stop:** <which, and why>
- **Expected after removal:** <decay expected; what carries the behavior afterward>
- **Measure at:** <months after the end; the measure>

## Crowding-out check
<existing motive, if any; recipients' status (community member, volunteer, staff); what to watch for>

## Ethics
- **Coercion:** <reward as a share of daily income; whether it is refusable>
- **Fairness:** <non-recipients, neighbors, those excluded by the condition>
- **Review:** <audit-intervention-ethics; legal review if public servants or a government transfer; ethics committee if clinical>

## Cost
<cost per person incentivized; cost per verified behavior; hand to estimate-cost-effectiveness>

## What to test
<incentive vs no incentive on the same supply; the outcome; follow-up after removal>

## What to check before relying on this
- <the verification assumption>
- <the sizing assumption>
```

## Where it goes wrong

- **Rewarding the report.** Paying for a behavior that is self-reported (pills taken, hand washing) rewards saying, not doing. The verification line is filled before any amount; an unverifiable behavior goes back for a verifiable proxy.
- **Pricing the hassle wrong.** Too small and nothing moves; too large relative to income and the offer is coercive, with a larger crash when it ends. The size row carries both multiples so the reviewer can see which failure the amount risks.
- **Lottery because it is cheap.** The lottery evidence the planning material reviewed has unverified authors and is not cited; the one US regret-lottery result the dossier records was null. Certain and immediate is the default, and a lottery needs its own justification and pilot.
- **No removal plan.** An incentive that quietly becomes a permanent budget line, or stops without warning. Effects decay after removal in the evidence, so the plan names the end date, what carries the behavior afterward, and the follow-up measure.
- **Incentive on broken supply.** Paying people to attend a clinic with no vaccines or a school with no teacher. The supply check is written before the reward; Rajasthan's camps were reliable first.
- **Quoting the uncorrected numbers.** Presenting RR 6.7 as what a program will get, when it sat on a 6% base with reliable camps, or reading Baird's 60% as percentage points when it is a change in odds. Numbers are quoted with their base and their unit.

## When to bring in a specialist

Tell the user to consult the relevant specialist when:
- Payments go to poor households, in cash or in food, at any amount that is a meaningful share of daily income; an ethics review through `audit-intervention-ethics` and, where the work is research, an ethics committee, because the reward may not be refusable
- Payments go to public servants, health workers, teachers, or volunteers; legal, human-resources, and fairness review, because paid and unpaid colleagues doing the same work is a documented route to resentment and crowding out
- The rewarded behavior is clinical (medication, testing, delivery, immunization); a clinician reviews the verification method and the harms an incentive can induce, such as over-testing or pill dumping
- The reward would come from a government budget or be attached to an existing transfer program; policy review, since the condition changes who is entitled to the transfer
- The budget cannot carry the scheme to its end date; stop, because an incentive withdrawn early produces the decay without the benefit

Bring them: the scheme table, the sizing arithmetic with daily income and hassle cost, the monitoring decision, the removal plan, and the ethics section.
