---
name: design-commitment-device
description: >-
  Use when people say they want to save, quit, or stick to a plan but keep
  failing because the moment of temptation wins, and you want to offer them a
  way to tie their own hands: a locked savings account, a deposit they forfeit,
  a contract with a penalty they chose. Also use when a team proposes a "lock
  box", "savings commitment", or "quit contract" and needs the stake, the
  verifiable goal, the opt-in rule, and the plan for people who commit and
  fail worked out before launch. Produces a specification for a voluntary
  device built on Bryan, Karlan and Nelson (2010) and the SEED and CARES
  trials in the Philippines. Do not use when the problem is inertia rather
  than temptation (people never get round to enrolling); use
  select-default-option instead. Not for a label on money with no lock
  (specify-earmark-label), not for rewards the program pays
  (design-incentive-scheme), and not for generic drafting of the offer
  script (draft-lever-content).
license: CC-BY-4.0
metadata:
  title: Help people tie their own hands against temptation
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "commitment-devices, present-bias, savings"
  consumes: "intervention-levers, barrier-diagnosis"
  produces: "intervention-draft"
---

## What it does

Specifies a voluntary option that restricts or penalizes a person's future self, with a stake they choose, so that a plan made today survives the moment of temptation.

Present bias is the tendency to weight the present far more than the future, so the self that plans (save for the fees, stop smoking) wants something different from the self that acts (spend tonight, smoke now). A commitment device lets the planning self impose a cost on the acting self: money that cannot be withdrawn until a date, a deposit forfeited on failure, a public promise. It works only for people who know they will be tempted and want the restriction, which is why it is always opt-in and why most people decline it. This skill confirms that temptation is the barrier, chooses soft or hard commitment, sets the goal and the stake, and plans for the people who commit and fail. It does not pick the technique; `select-intervention-levers` does.

## When to use it

### Use it when
- A barrier diagnosis says people intend the behavior, have the means, and fail at the moment of action: "I meant to save it but it was gone by evening", "I always say I'll quit after this pack"
- Someone proposes a lock box, a savings account with a date lock, a deposit contract for quitting, or "a penalty if I don't do it", and needs the terms worked out
- Demand for self-restriction already shows up informally (people hand cash to a neighbor to hold, join a rotating savings group for the discipline) and the team wants to offer a formal version
- A lever brief from `select-intervention-levers` names a commitment or self-restriction technique and the next question is "what exactly do we offer?"

### Do not use it when
- The barrier is inertia (people never enroll, never switch) rather than temptation; a default acts on inertia, and `select-default-option` owns that choice
- The team wants to earmark money for school fees or health without locking it; a label with no lock is `specify-earmark-label`, and it does not cost the person anything on failure
- The stake would be paid by the program (a reward for passing, a bonus for saving) rather than put up by the person; that is `design-incentive-scheme`, a different mechanism with different backfires
- The device is chosen and the team needs the enrollment script, SMS, or form wording; `draft-lever-content` writes that from this skill's specification

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The confirmed barrier, with evidence, from `decompose-comb-barriers` fieldwork or the lever brief: that people state the intention, have the money or ability, and fail at the moment of action. If the evidence says they cannot afford, reach, or do the behavior, say so and stop; a lock on money people do not have is a lock on nothing.
2. **Required.** The target behavior (who, what, when) and whether its completion can be verified by a third party cheaply (a balance on a date, a test result, a logged attendance). Without verification a stake cannot be enforced, so the device must be soft or the goal redefined.
3. **Required.** The population's income pattern and what loss would hurt: seasonal income, debt, a lean period, dependents. This sets the ceiling on the stake and drives the fairness section.
4. Optional. Whether a partner institution (bank, microfinance institution, mobile-money operator, clinic) can hold the stake, enforce the rule, and is trusted by this population to give the money back.
5. Optional. Any existing informal commitment the population already uses, which tells the team what kind of restriction people already accept.

If 1 is missing, ask and stop. If 2 is missing, ask once; if still missing, specify a soft device only and say why. If 3 is missing, ask once; if still missing, cap the stake at a token amount and mark the fairness section "income pattern unknown". If 4 and 5 are missing, assume no partner is confirmed and no informal device exists, and flag both.

## What it draws on

- Bryan, G., Karlan, D., & Nelson, S. (2010). Commitment devices. *Annual Review of Economics*, 2, 671–698. https://doi.org/10.1146/annurev.economics.102308.124324
- Ashraf, N., Karlan, D., & Yin, W. (2006). Tying Odysseus to the mast: Evidence from a commitment savings product in the Philippines. *The Quarterly Journal of Economics*, 121(2), 635–672. https://doi.org/10.1162/qjec.2006.121.2.635
- Giné, X., Karlan, D., & Zinman, J. (2010). Put your money where your butt is: A commitment contract for smoking cessation. *American Economic Journal: Applied Economics*, 2(4), 213–235. https://doi.org/10.1257/app.2.4.213
- Dolan, P., Hallsworth, M., Halpern, D., King, D., Metcalfe, R., & Vlaev, I. (2012). Influencing behaviour: The mindspace way. *Journal of Economic Psychology*, 33(1), 264–277. https://doi.org/10.1016/j.joep.2011.10.009
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709
- Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity: A meta-analysis and a real-effort experiment. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x

Bryan, Karlan, and Nelson (2010) is the narrative review that defines the object: an arrangement entered into voluntarily that restricts future choice or attaches a penalty to it, taken up by people who anticipate their own present bias, and distinguished from an incentive by who puts up the stake. The two canonical trials are both Philippine. SEED (Ashraf, Karlan & Yin 2006), a savings account at Green Bank in Butuan locked until a date or amount the client chose: 1,777 clients surveyed, 710 offered the product, 28.4% took it up, and savings balances rose 81 percentage points versus control at 12 months. CARES (Giné, Karlan & Zinman 2010), a deposit contract for smokers in Mindanao forfeited on a failed urine test: 11% take-up, those offered were 3.3 to 5.8 percentage points more likely to pass the 6-month test, persisting at 12 months, and 66% of committers still failed and lost their money. MINDSPACE (Dolan et al. 2012) lists "Commitments" as one of nine levers, the practitioner statement of the technique. See `references/evidence-notes.md` for the annotated list.

Judgment calls this skill adds: the rule that the device is specified only after the barrier evidence rules out cost, access, and skill; the requirement to write the failure plan and say where forfeited stakes go before launch; and the ceiling on the stake set from the population's income pattern rather than from what maximizes effect.

**WEIRD skew:** Reversed from the usual pattern: the canonical trials are Philippine, so the question is not whether the mechanism travels out of WEIRD samples but whether it travels out of a bank-client or clinic sample with an institution able to hold the stake. What to check locally is trust that the holder returns the money, kin pressure on visible balances, seasonal income, and whether a forfeit reads as a fine from the program. **Non-WEIRD evidence:** Philippines, Butuan (Ashraf, Karlan & Yin 2006), 710 offered, 28.4% take-up, balances +81 percentage points at 12 months; Philippines, Mindanao (Giné, Karlan & Zinman 2010), 11% take-up, +3.3 to 5.8 points passing the 6-month test, 66% of committers failed.

**Replication status:** Mixed: several LMIC successes, no meta-analysis among this skill's sources (the field rests on a narrative review), take-up usually 10 to 30%, and many committers fail. The trial effects are already intent-to-treat effects of a few points on a binary outcome, so there is no lab headline to discount; the general warning still applies: nudge-unit trials average 1.4 percentage points against 8.7 in academic journals (DellaVigna & Linos 2022), and loss framing shrank from 0.33 SD in the lab to 0.02 SD in the field (Ferraro & Tracy 2022). Plan for take-up at the low end and an effect of a few points among those offered.

## How to do it

1. **Confirm that present bias or temptation is the barrier.** Write the evidence in one line: stated intention, means available, failure at the moment of action. If the barrier is cost, access, or skill, stop and send the user back to `select-intervention-levers`; a commitment device cannot create money or ability.
2. **Choose soft or hard commitment.** Hard (money locked or forfeited, access removed) when the goal is verifiable and the person can afford to lose the stake; soft (a public promise, a reminder of the goal, a token deposit) when verification is weak or a loss would cause hardship. Say which and why; the choice is the main design decision.
3. **Set the verifiable goal:** a date or an amount, who verifies it, and how, at what cost. In CARES the verifier was a urine test; in SEED the bank held the balance to the client's own date or amount. No verification, no hard stake.
4. **Set the stake.** The person's own money or access, sized below what would hurt in the lean period from question 3, chosen by the person within a range the program sets. State where forfeited stakes go; a program that keeps them has a reason to want people to fail, so route them elsewhere and say so in the offer.
5. **Make it opt-in and keep it separate.** No automatic enrollment, no bundling with credit or another service people cannot refuse, and an explicit "no" option in the offer. Expect 10 to 30% take-up; the device is for the minority who want it, and that is the design, not a failure.
6. **Plan for the people who commit and fail.** State what they lose, how they learn it, whether a second attempt is offered, and how failures are counted in the evaluation. In CARES two-thirds of committers lost their stake; the plan must assume a majority may.
7. **State the expected take-up and effect** for this population: a share of those offered at the low end of 10 to 30% unless local evidence says otherwise, and a few points of change among those offered. Write this where the funder will read it.
8. **Answer the fairness question:** who is likely to take up (people with slack), who is likely to lose (people with less), and whether the stake could push a poor household into hardship. Route the open items to `audit-intervention-ethics`.
9. **Stop here.** `draft-lever-content` writes the offer script from this specification; `audit-intervention-ethics` reviews the stake and the failure plan; `plan-evaluation-design` sets up the test, with take-up and failure as pre-specified outcomes.

See `references/worked-example.md` for a complete run on school-fee savings among peri-urban workers in Uganda.

## Output template

```markdown
# Commitment device specification

**Target behavior:** <who + what + when, carried over verbatim>
**Barrier confirmation:** <evidence that people intend, can, and fail at the moment of action; source>
**Device type:** <hard / soft, with the reason>

## Goal and verification
- Goal: <date or amount>
- Verified by: <who, how, at what cost per check>

## Stake
- What the person puts up: <money, access, reputation>
- Range the person chooses within: <floor and ceiling, with the ceiling tied to the income pattern>
- Where forfeited stakes go: <not to the program; say where>

## Opt-in rule
- How the offer is made: <...>
- The explicit "no" option: <...>
- Not bundled with: <...>

## Failure plan
- What a failed committer loses: <...>
- How they learn and whether they may try again: <...>
- How failures are counted in the evaluation: <...>

## Expected take-up and effect
- Take-up: <share of those offered, with the reason for the number>
- Effect among those offered: <a few points on the verified outcome; the source for the expectation>

## Fairness
- Who takes up: <...>
- Who loses: <...>
- Could the stake cause hardship: <yes / no, and what was capped because of it>
- Open items for audit-intervention-ethics: <...>

## What to check before relying on this
- <the assumption most likely to be wrong, usually that the barrier is temptation rather than cost>
```

## Where it goes wrong

- **A lock on a liquidity problem.** If people do not have the money, a locked account changes nothing and a forfeit takes money from the poorest. The barrier confirmation line is mandatory for this reason; "they don't save" is not evidence of temptation.
- **An unverifiable goal with a hard stake.** "Spend less on airtime" cannot be checked, so a forfeit on it is either unenforced or enforced on self-report, which invites lying. Redefine the goal to something a third party can see, or make the device soft.
- **The program sets the stake.** A penalty chosen by the program and applied to everyone is a fine, not a commitment, and belongs to `design-incentive-scheme` or to coercion, not here. The person chooses within a range.
- **Auto-enrollment.** A locked account nobody chose is a restriction without a commitment; it removes the mechanism (anticipating one's own temptation) and adds the harm (people locked out of their money). Opt-in is not a formality.
- **Forgetting the failers.** Reporting the SEED balance effect without the CARES failure rate is half the evidence; in a hard device a majority of committers may lose their stake, and a plan that has not said what happens to them is not finished.
- **Selling the take-up effect as a population effect.** 28.4% took up SEED; the effect among those offered is what the trial measured. A device that reaches a tenth of the population and moves them a few points is the realistic promise.

## When to bring in a specialist

Tell the user to consult a financial-inclusion or consumer-protection specialist, and where noted a clinician, when:
- The stake could cause financial harm to poor households: the lean season overlaps the lock period, the population carries debt, or the ceiling cannot be set below what would hurt; the specialist sets the cap and `audit-intervention-ethics` reviews it before any offer
- The behavior is clinical (smoking cessation, medication adherence, alcohol) and the verification is a test; a clinician decides the test, the interval, and what a failed committer is told about relapse
- The institution that would hold the stake is unregulated or not trusted to return the money; a forfeit that is really a loss to an untrustworthy holder is a fraud risk, not a device
- The device would be bundled with credit or offered by a lender, where "commitment" can shade into collateral; a consumer-protection review is needed before the offer is drafted

Bring them: the barrier evidence, the device specification with the stake range and failure plan, what is known about the population's income pattern, and the partner's terms for holding the stake.
