---
name: design-social-recognition
description: >-
  Use when a team wants to make it visible that someone has done a behavior,
  so that being seen to have done it carries weight: "a bracelet for mothers
  whose children are vaccinated on time", "a badge for agents who meet the
  target", "a public thank-you for those who paid". Also use when a program
  is about to hand out certificates or tokens without checking that the
  people whose opinion matters value the signal, that it is tied to verified
  completion, and what happens to those who get none. Specifies the token,
  the completion rule, where it is seen, the reference-group check, the plan
  for non-recipients, and the measurement of uptake and harm, drawing on the
  Sierra Leone vaccination-bracelet trial and the Zambia public-recognition
  trial. Do not use when the reward is money, goods, or airtime; use
  design-incentive-scheme instead. Not for a community pledge event
  (plan-collective-pledge), a message about what most peers do
  (write-social-norm-message), or generic drafting (draft-lever-content).
license: CC-BY-4.0
metadata:
  title: Make doing the behavior visible with a token
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "social-norms, incentives, behavior-change-techniques"
  consumes: "intervention-levers, social-norm-diagnosis"
  produces: "intervention-draft"
---

## What it does

Specifies a token, badge, or ceremony that makes verified completion of one behavior visible to the people whose regard the person cares about.

People act partly to be seen well by a reference group, the people whose opinion of them matters. A visible marker of completion lets a person signal a valued trait (a caring parent, a serious worker) and lets everyone see who has it; the behavior stops being private. In Sierra Leone, bracelets for timely vaccination raised timely complete vaccination by 14.4 points, from about 56% to 71%; in Zambia, public recognition raised hairdressers' sales of condoms, most among those already motivated to serve. The conditions: the signal is valued by the reference group, it is tied to completion that someone verifies, and it is seen where that group looks. The backfire: people without the token are marked too, and where the behavior is private or stigmatized, visibility itself is the harm. This skill specifies the design with those conditions; it does not write the announcement, and it does not decide whether to also pay.

## When to use it

### Use it when
- A lever brief from `select-intervention-levers` selects a social reward or social incentive, a non-financial recognition, for a confirmed barrier
- Someone asks for "a bracelet", "a badge", "a certificate", "a public thank-you", "a wall of honor", or "a ceremony for those who completed"
- A `diagnose-social-norm` or `map-reference-network` output shows the behavior is valued but invisible, so that doing it earns no regard and skipping it costs none
- A program already gives out certificates or tokens and wants to know whether they do anything, or whether they shame the people without one

### Do not use it when
- The reward is money, goods, airtime, or a lottery ticket; that is `design-incentive-scheme`, and mixing a payment into a token muddies the signal
- A whole community must give up a practice together because each household keeps it only while the others do; that is `plan-collective-pledge`
- The lever is telling people what most of their peers already do; that is `write-social-norm-message`
- The behavior is one people would rather keep private, or is stigmatized (HIV testing or treatment, family planning, mental health care, services after abuse); visibility is the harm, so route to `audit-intervention-ethics` and the specialist section below
- It is not yet known whose regard the people doing the behavior actually track; run `map-reference-network` first
- The team needs the words on the certificate or the announcement; that is `draft-lever-content`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The target behavior (who, what, when) and how completion is verified: which register, receipt, or observation, recorded by whom. If completion cannot be verified, say so and stop; a token nobody can check is not a signal.
2. **Required.** Whose regard matters: the reference group, from `map-reference-network` or `diagnose-social-norm`, and whether doing this behavior is admired, neutral, or suspect among them.
3. **Required.** Whether people would want it known that they did, or did not do, this behavior: any stigma, privacy, legal, or safety concern.
4. **Required.** Where the reference group would see the token: market, place of worship, clinic, school gate, village meeting, a messaging group.
5. Optional. Budget per person, who would hand the token out, and how stock would reach them.
6. Optional. The expected share of people who will complete, and whether non-completion is mostly a choice or mostly involuntary (distance, stockouts, cost), so the size and makeup of the non-recipient group is known.

If 1 or 2 is missing, ask and stop. If 3 is missing, ask once; if still unknown, proceed with the stigma screen marked "unverified" and delivery held until it is done. If 4 is missing, assume the place of verification and flag it. If 5 is missing, assume a low-cost wearable token given at verification. If 6 is missing, assume non-completion is partly involuntary and design the mitigations for that case.

## What it draws on

- Karing, A. (2016). Social signaling in childhood immunization: Evidence from a field experiment in Sierra Leone. AEA RCT Registry. https://doi.org/10.1257/rct.1299 (registry record; the journal version is unverified, author to confirm)
- Ashraf, N., Bandiera, O., & Jack, B. K. (2014). No margin, no mission? A field experiment on incentives for public service delivery. *Journal of Public Economics*, 120, 1–17. https://doi.org/10.1016/j.jpubeco.2014.06.014
- Bénabou, R., & Tirole, J. (2006). Incentives and prosocial behavior. *American Economic Review*, 96(5). https://doi.org/10.1257/aer.96.5.1652 (carried in the dossier as a plan-only citation, with no numbers)
- Dolan, P., Hallsworth, M., Halpern, D., King, D., Metcalfe, R., & Vlaev, I. (2012). Influencing behaviour: The mindspace way. *Journal of Economic Psychology*, 33(1), 264–277. https://doi.org/10.1016/j.joep.2011.10.009
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709
- Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity: A meta-analysis and a real-effort experiment. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x

Karing's Sierra Leone trial gave mothers colored bracelets that signaled timely vaccination of their child; timely, complete vaccination rose by 14.4 points, from about 56% to 71% (a search-snippet figure per the dossier). The dossier verified the AEA registry record, dated 2016; a journal version was not located, so the number is quoted with that caveat. Ashraf, Bandiera and Jack gave Zambian hairdressers selling female condoms non-financial public recognition; sales improved, more for agents who were already prosocially motivated; the effect size is unverified in the dossier. Bénabou and Tirole model prosocial behavior as driven partly by the wish to be seen as a good person; the dossier carries the paper as a plan-only citation, so this skill uses it for the mechanism only (this reading is the drafter's, author to confirm). MINDSPACE (Dolan et al.) names Ego and Norms among its nine levers; a visible token works through both, how the person sees themselves and how others see them. The judgment calls this skill adds: the token is handed over only against a verified record; the stigma screen is a gate; a written plan for the people who will visibly lack the token is mandatory; harm to non-recipients is measured alongside uptake; the token must be hard to obtain without completing; and one design carries one lever, so a team that also wants to pay is sent to `design-incentive-scheme`.

How much to discount: both trials are field trials in low-income settings, so the worry is less lab-to-field shrinkage than selection and single-trial variance. The 14.4-point effect is one trial, one token, one behavior, one country. Across applied behavioral science, academic journal trials average 8.7 percentage points where nudge-unit trials of the same kind average 1.4 (DellaVigna & Linos), and loss framing shrinks from 0.33 SD in the lab to 0.02 in the field (Ferraro & Tracy). Plan for well under 14 points, treat the direction as supported and the size as unknown for any new setting, and expect the effect to depend on how much the reference group values the behavior.

**WEIRD skew:** The evidence base is itself non-WEIRD, which is unusual in this library. What to check locally is the meaning of the token: whether a bracelet, sticker, or public list reads as a signal at all, whether the reference group values the behavior it marks, whether the color or form already belongs to a party, a church, or another program, and whether people without one will be shamed or excluded. **Non-WEIRD evidence:** Sierra Leone (Karing 2016, registry): bracelets for timely vaccination, +14.4 points, about 56% to 71%. Zambia (Ashraf, Bandiera & Jack 2014): hairdressers' condom sales rose with public recognition, more for prosocially motivated agents, effect size unverified. Nigeria (Ekiti, World Bank eMBeD): social recognition compared with lottery incentives for health record-keeping, effect size not retrieved.

**Replication status:** Two strong LMIC trials per the plan, in different behaviors and countries, each a single study for its setting; the Sierra Leone paper is verified only as a registry entry and the Zambia effect size is unverified. See `references/evidence-notes.md` for each source with its verification state.

## How to do it

1. **Carry over the behavior and the verification rule verbatim.** Write who records completion, on what, and the rule that the token is handed over only against that record. If nothing can be verified, stop.
2. **Run the stigma and privacy screen.** Would a reasonable person in this group want it known that they did this, and that they did not? If the behavior is private or stigmatized, stop, route to `audit-intervention-ethics`, and point to the specialist section. Write the verdict either way.
3. **Name the reference group and the signal.** From `map-reference-network`: who sees, and what they will read: "a person with this token is read by these people as this kind of person". If the group does not value the behavior, the token is noise; if the group does not see it, it is private, and either way the design should stop here.
4. **Choose the token.** Criteria: visible where the group looks; locally meaningful in form and color; durable for the period; cheap; hard to get without completing (distinct, not sold in the market, handed over only at verification); not already carrying another meaning. Options: wearable, household marker, public list, ceremony, digital badge. Choose one and say why. See `references/worked-example.md` for a complete run.
5. **Tie it to the completion rule.** Any completion or timely completion (Sierra Leone signaled timeliness); what late completers get; whether there are stages. An open path to earn the token later keeps it from becoming a permanent mark.
6. **Design for non-recipients.** Who will visibly lack it, and why: chose not to, or could not (distance, stockouts, cost). What lacking it will be read as. Mitigations: no public naming of non-completers; no token on children or households that marks a family; supply fixed first where non-completion is involuntary. If most non-completion is involuntary, say that the token would mark the poor and recommend against it until supply is fixed.
7. **Write the delivery line:** who hands it over, at the moment of verification, with one spoken line (the words go to `draft-lever-content`), and the stock and replacement plan.
8. **Write the measurement plan.** Uptake is the verified completion rate, never tokens distributed. Signal integrity: tokens seen without a record. Harm: how shaming, exclusion, or conflict among non-recipients will be detected, with a few interview questions at follow-up. A comparison group, pre-registration (filed before launch), and an expected effect below 14.4 points.
9. **Write the evidence statement** for the decision-maker: two LMIC trials, one verified as a registry entry only, the numbers as given above.
10. **Stop here.** `audit-intervention-ethics` reviews the non-recipient plan; `plan-evaluation-design` turns the measurement plan into a test; `draft-lever-content` writes the words.

## Output template

```markdown
# Social recognition design

**Target behavior:** <who, what, when, carried over verbatim>
**Completion is verified by:** <who records what, where; the token is handed over only against this record>
**Reference group (from map-reference-network):** <whose regard matters; what they think of this behavior>

## Stigma and privacy screen (gate)
<would people want it known that they did this, and that they did not? verdict: proceed | stop and route to audit-intervention-ethics>

## The signal
"A <person> with <token> is read by <reference group> as <trait>." <why this group values it; where they will see it>

## Token
- **Form:** <wearable | household marker | public list | ceremony | digital; the specific object, color, material>
- **Why this form:** <visible where the group looks; locally meaningful; durable; cost per unit; not already carrying another meaning>
- **Hard to get without completing:** <how>

## Completion rule
- **Earns the token:** <any completion | timely completion, defined>
- **Late completers:** <...>
- **Stages, if any:** <...>

## Non-recipients
- **Who will visibly lack it, and why:** <chose not to | could not: distance, stockouts, cost; estimated share>
- **What lacking it will be read as:** <...>
- **Mitigations:** <open path to earn it; no public naming; no marking of children or households; supply fixed first>

## Delivery
- **Handed over by, when:** <at verification, by whom>
- **What they say:** <one line; final words drafted by draft-lever-content>
- **Stock and replacement:** <...>

## Measurement plan
- **Uptake:** <verified completion rate, not tokens distributed>
- **Signal integrity:** <tokens seen without a record>
- **Harm:** <how shaming, exclusion, or conflict among non-recipients will be detected>
- **Comparison and pre-registration:** <...>
- **Expected effect:** <below the Sierra Leone 14.4 points; direction supported, size unknown here>

## Evidence statement (mandatory)
<two LMIC trials, one verified as a registry entry only; the numbers as given in What it draws on>

## What to check before relying on this
- <whether the token already means something else locally>
- <the share of non-completion that is involuntary>
```

## Where it goes wrong

- **Token without verification.** Bands handed out at enrollment, or sold in the market, signal nothing; once people see tokens on people who did not complete, the signal is gone for everyone. The token follows the record, never precedes it.
- **A signal nobody reads.** A certificate valued by program staff and invisible to the people whose regard matters is a filing exercise. The signal line must name the reference group and where they see the token.
- **Marking the poor.** Where non-completion is mostly involuntary (distance, stockouts, cost), the token sorts people by circumstance and the people without one are visibly marked. The non-recipient plan is mandatory, and "fix supply first" is a legitimate verdict.
- **Visibility where privacy is the point.** A bracelet for antiretroviral refills, a badge for family-planning uptake: the skill refuses these at the stigma screen rather than designing them well.
- **Counting tokens instead of behavior.** Tokens distributed is a logistics figure. Uptake is verified completion from the register; signal integrity is tokens seen without a record.
- **Paying as well.** Adding airtime or cash to the token turns it into a receipt for a payment; whether the two combine is an open question, not a free bonus. One design, one lever; the payment is `design-incentive-scheme`.

## When to bring in a specialist

Tell the user to consult an ethics or safeguarding lead, and where relevant a clinician or a local community advisor, when:
- The behavior is stigmatized or private (HIV testing or treatment, family planning, mental health care, services after violence); visibility is the harm, and the skill should not build the token however the behavior is reframed
- Most non-completion is involuntary; a program lead and a behavioral scientist should decide whether to fix supply first, because the token would otherwise mark the people the program is meant to serve
- Children would carry the token (a school badge, a mark on a pupil); a child-protection review is needed before any design
- The token's form or color could be read as political, religious, or as a mark authorities might use; community leaders and a local advisor should see the design first

Bring them: the behavior and its verification rule, the stigma screen with its verdict, the reference-group facts, the candidate token, and the non-recipient plan.
