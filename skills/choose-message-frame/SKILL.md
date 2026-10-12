---
name: choose-message-frame
description: >-
  Use when a team is deciding whether to word a message or an incentive as
  a gain ("protect your child") or a loss ("put your child at risk"), or is
  about to assume that loss aversion makes the loss frame stronger. Also use
  when someone asks whether a bonus should be paid up front and taken back
  on failure (a loss contract) instead of paid on completion. Classifies the
  behavior as prevention or detection and the vehicle as message or money,
  picks the frame the evidence supports (gain for prevention; no reliable
  loss advantage in the field), writes both variants, and plans the A/B test
  with an honest statement of the small expected difference, drawing on
  Gallagher and Updegraff (2012) and Ferraro and Tracy (2022). Do not use
  when the frame is settled and the team needs the message written; use
  draft-lever-content instead. Not for setting an incentive's amount,
  timing, or conditions (design-incentive-scheme), and not for "most people
  like you do X" messages (write-social-norm-message).
license: CC-BY-4.0
metadata:
  title: Pick gain or loss framing for a message or incentive
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: mixed-evidence
  tags: "framing, incentives, message-design, behavior-change-techniques"
  consumes: "intervention-draft, intervention-levers"
  produces: "intervention-draft"
---

## What it does

Decides whether one message or one incentive contract should be worded as a gain or as a loss, from the type of behavior it targets.

The evidence runs against the common assumption. For messages, gain frames slightly beat loss frames when the behavior prevents a bad outcome, and neither frame wins when the behavior detects one. For money, loss-framed contracts that pay up front and take the money back look strong in the lab and do almost nothing in the field. This skill's main job is to stop a team assuming loss framing works: it sets the honest default, writes both variants so the frame can be tested rather than assumed, and states how small the difference is likely to be.

## When to use it

### Use it when
- A team says "loss aversion means we should tell them what they will lose" before any test has been run
- Someone asks "should the SMS say 'you will protect your baby' or 'you will put your baby at risk'?"
- A program is considering paying a bonus or incentive up front and taking it back if the person does not deliver (a clawback or loss contract)
- A message draft exists in one frame and the team wants to know whether to flip it, or wants to A/B test the frame

### Do not use it when
- The frame is chosen and the team needs the full message, script, or poster written; that is `draft-lever-content`
- The question is how much to pay, when, to whom, or under what conditions; that is `design-incentive-scheme`, which owns the contract itself
- The persuasive content is "most people like you already do this"; that is `write-social-norm-message`, and a norm claim is not a frame choice
- No barrier has been confirmed or no technique chosen; framing is a wording decision on top of a chosen lever, so run `select-intervention-levers` first

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The behavior as who, what, when, and whether doing it prevents a bad outcome (vaccination, bed-net use, saving, handwashing) or finds out whether a bad outcome is already present (an HIV test, a screening, a blood-pressure check). If the user cannot say, ask: "does doing it reduce a risk, or reveal one?"
2. **Required.** The vehicle: a message (SMS, poster, script, letter) or money (a bonus, an incentive, a contract). If money, whether a loss frame would mean withholding or taking back something people already treat as theirs, such as wages, stipends, or benefits; that is an escalation condition, not a design choice.
3. **Required.** The existing draft or incentive specification, from `draft-lever-content` or `design-incentive-scheme` if one exists, or whatever the team has. The two variants are written on top of it.
4. Optional. Whether an A/B test is feasible: roughly how many people, and whether the channel can randomize who gets which variant.
5. Optional. Anything known about how this population reacts to loss or threat language, such as pre-test reactions or local norms about naming bad outcomes aloud.

If 1 or 2 is missing, ask and stop. If 3 is missing, proceed with short illustrative variants marked as placeholders for `draft-lever-content`. If 4 is missing, assume a test is feasible and flag it. If 5 is missing, assume nothing is known and make the local check a required pre-launch step.

## What it draws on

- Gallagher, K. M., & Updegraff, J. A. (2012). Health message framing effects on attitudes, intentions, and behavior: A meta-analytic review. *Annals of Behavioral Medicine*, 43, 101–116. https://doi.org/10.1007/s12160-011-9308-7 (erratum: https://doi.org/10.1007/s12160-012-9446-6)
- Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity: A meta-analysis and a real-effort experiment. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x
- Fryer, R. G., Levitt, S. D., List, J., & Sadoff, S. (2022). Enhancing the efficacy of teacher incentives through framing: A field experiment. *American Economic Journal: Economic Policy*. https://doi.org/10.1257/pol.20190287 (working paper: NBER w18237, 2012, https://doi.org/10.3386/w18237)
- Bulte, E., List, J. A., & van Soest, D. (2020). Toward an understanding of the welfare effects of nudges: Evidence from a field experiment in the workplace. *The Economic Journal*. https://doi.org/10.1093/ej/ueaa054 (NBER w26286 carries the title "...in Uganda", https://doi.org/10.3386/w26286)
- Karlan, D., McConnell, M., Mullainathan, S., & Zinman, J. (2016). Getting to the top of mind: How reminders increase saving. *Management Science*, 62(12), 3393–3411. https://doi.org/10.1287/mnsc.2015.2296
- Hallsworth, M., List, J. A., Metcalfe, R. D., & Vlaev, I. (2017). The behavioralist as tax collector: Using natural field experiments to enhance tax compliance. *Journal of Public Economics*, 148, 14–31. https://doi.org/10.1016/j.jpubeco.2017.02.003
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709

The mechanism usually claimed is loss aversion: a loss of a given size is felt more than a gain of the same size, so stating what people stand to lose should move them more. The message evidence does not bear this out. Across 94 studies and 189 effect sizes, gain-framed messages produced slightly more prevention behavior than loss-framed ones (r = 0.083), neither frame moved attitudes or intentions, and neither frame won for detection behaviors (Gallagher & Updegraff, 2012). The money evidence shrinks on contact with the field: loss-framed contracts pooled at 0.16 SD, but 0.33 SD in the lab against 0.02 SD in the field, with publication bias among the lab studies (Ferraro & Tracy, 2022). The best-known field case, teacher bonuses paid up front, reported 0.20–0.40 SD in the 2012 working paper and 0.124 SD in the 2022 published version, with no effect in the second wave (Fryer et al., 2022). Savings reminders in three countries showed no loss-versus-gain difference (Karlan et al., 2016), and UK tax letters showed no loss-frame advantage (Hallsworth et al., 2017). The judgment calls this skill adds: the prevention-or-detection question is reduced to "reduce a risk, or reveal one"; the field numbers, not the pooled or lab ones, are the planning numbers; and writing both variants is mandatory so the frame is tested, not assumed. See `references/evidence-notes.md`.

**How much to discount.** Lab-to-field shrinkage in loss framing (0.33 to 0.02 SD) and the gap between academic trials and nudge-unit trials (8.7 versus 1.4 percentage points, with about 70% of the gap explained by selective publication plus low power; DellaVigna & Linos, 2022) point the same way. Plan a field program on the field numbers: for a message, a frame difference no larger than r = 0.083 and possibly zero; for a contract, about 0.02 SD.

**WEIRD skew:** The message meta-analysis pools health-communication studies, a literature dominated by high-income-country samples (the dossier records no country breakdown, so treat the pooled estimate as WEIRD-skewed until checked). Check locally whether loss language about a child, a pregnancy, or a diagnosis is acceptable to say aloud at all. **Non-WEIRD evidence:** Uganda (Bulte, List & van Soest, 2020): about 1,000 peri-urban workers; loss-framed contracts raised productivity at a modest welfare cost, effect size unverified; most workers preferred gain contracts, and the gain appeared only among the roughly 20% who chose loss framing. Bolivia, Peru, and the Philippines (Karlan et al., 2016): no frame difference in savings reminders.

**Replication status:** Contested. The direction for prevention messages is small but meta-analytic (r = 0.083, 94 studies, 189 effect sizes); the loss-contract effect shrinks from 0.33 SD in the lab to 0.02 SD in the field and from 0.20–0.40 SD to 0.124 SD on revision; two field trials of framing in reminders and tax letters found nothing.

## How to do it

1. **Classify the behavior** as prevention (doing it reduces a risk) or detection (doing it reveals a risk), and write the reason. This is the only classification the evidence turns on; a detection behavior gets no evidence-based frame preference.
2. **Classify the vehicle** as message or money. If money, check whether the loss frame would withhold or take back wages, stipends, or benefits; if so, stop designing the loss variant and go to "When to bring in a specialist".
3. **Set the default frame.** Prevention message: gain. Detection message: no evidence-based preference; use gain as the default because nothing shows loss doing better and a loss frame has more ways to offend. Money: gain (pay on completion); record the loss contract as low-yield in the field (0.02 SD).
4. **Write both variants** on top of the existing draft: same facts, same single action, same sender, same length; only the frame changes. If the two differ in anything else, the test is no longer a test of the frame.
5. **Plan the A/B test.** Name the unit of randomization, the arms, and the primary outcome, which must be the behavior, because frames did not move attitudes or intentions. Point the team to `estimate-sample-size` for the sample.
6. **State the expected difference** in numbers: no more than r = 0.083 for a prevention message, about 0.02 SD for a contract. Say plainly that a test too small to detect that is a test of whether the message works at all, not of which frame wins, and set the decision rule: if no difference is detected, keep the gain frame.
7. **Require the local check** before launch: both variants shown cold to 5 to 10 members of the population, checking comprehension and whether the loss variant causes offense or distress.
8. **Stop here.** `draft-lever-content` writes the full message in the chosen frame; `design-incentive-scheme` sets the amount, timing, and conditions of any payment.

See `references/worked-example.md` for a complete run on antenatal iron-folate reminders in Malawi.

## Output template

```markdown
# Message frame decision

**Behavior:** <who + what + when, carried over verbatim>
**Behavior type:** <prevention | detection>, because <doing it reduces a risk | reveals one>
**Vehicle:** <message | money>, <channel, or form of payment>
**Source draft:** <from draft-lever-content / design-incentive-scheme / none; if none, the variants below are placeholders>

## Default frame
<gain | loss>, because <the evidence line that applies: prevention message, r = 0.083 for gain; detection message, no preference; contract, 0.02 SD in the field>

## Paired variants
| | Gain frame | Loss frame |
|---|---|---|
| Text | "<...>" | "<...>" |
| Held constant | <facts, the one action, sender, length> | <same> |

## A/B test plan
- **Unit of randomization:** <person, household, clinic, ...>
- **Primary outcome:** <the behavior; not attitude or intention>
- **Expected difference:** <number from the evidence, with the field discount>
- **Sample:** <rough figure, or "run estimate-sample-size">
- **Decision rule:** <what the team does if no difference is detected: keep the gain frame>

## Before launch
- <local pre-test of both variants: n, who, pass criterion, and a check for offense or distress>
- <escalation, if the loss frame touches wages, stipends, benefits, or a stigmatized diagnosis; or "none">

## What to check before relying on this
- <the classification call most likely to be wrong>
- <whether the population tolerates loss language on this topic>
```

## Where it goes wrong

- **Loss aversion as a slogan.** The model, like most teams, reaches for "losses loom larger" and skips the evidence. For prevention messages the meta-analytic result points the other way; write the number (r = 0.083 favoring gain) into the output rather than the slogan.
- **Quoting the lab or working-paper number.** 0.33 SD and 0.20–0.40 SD are the numbers people remember; 0.02 SD and 0.124 SD are the numbers to plan on. Never quote the uncorrected figure alone.
- **Misclassifying detection as prevention.** HIV testing, cancer screening, and blood-pressure checks reveal a risk; the evidence gives no frame advantage there, and a confident "gain frame" recommendation is unearned.
- **Changing more than the frame.** Variants that also differ in length, facts, sender, or the action requested test something else. The "held constant" row exists to catch this.
- **Measuring attitudes or intentions.** Framing had no effect on either; a test on stated intention will show nothing and the team will draw the wrong conclusion about the message.
- **Fear appeals wearing a loss frame.** A loss frame names the benefit foregone; it does not escalate to graphic harm or a child's death. This skill does not write fear appeals, and any loss variant naming a stigmatized or frightening outcome goes to the local check before anyone sees it at scale.

## When to bring in a specialist

Tell the user to consult the relevant specialist when:
- Loss framing would be applied to wages, stipends, or benefits, by paying up front and clawing back or by withholding; a labor-law or ethics reviewer must look at it, and the Uganda finding that most workers prefer gain contracts and that the loss contract carried a welfare cost belongs in that conversation
- The behavior is detection of a stigmatized or frightening condition (HIV, TB, cancer); a loss frame can deter testing or cause distress, so a clinician or counselor and a local researcher should review both variants before the pre-test
- The frame test is meant to be the program's main evaluation; an evaluator or statistician should confirm the sample can detect a difference this small before the team commits to the test

Bring them: the classification with its reason, the paired variants, the test plan with the expected difference, and any pre-test results.
