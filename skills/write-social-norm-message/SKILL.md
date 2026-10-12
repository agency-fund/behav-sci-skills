---
name: write-social-norm-message
description: >-
  Use when you want to tell people that most others like them already do the
  behavior (paid the tax, vaccinated, deposited) and need the message written
  so it moves the people who are behind without pulling back those already
  doing well. Also use when a draft already carries a social-proof line ("9
  out of 10 farmers...") and you need to check that the number is true, the
  reference group is close enough, and the message will not backfire. Produces one descriptive or injunctive norm
  message with the approval cue that prevents the boomerang, drawing on
  Schultz et al. (2007), Allcott (2011), and the UK and Guatemala tax-letter
  trials. Do not use when the practice is held in place by a whole community's
  expectations and no message will shift it alone; use plan-collective-pledge
  instead. Not for generic copywriting from a chosen technique
  (draft-lever-content), not for finding out whether a norm problem exists
  (diagnose-social-norm), and not for measuring what people believe others do
  (draft-norms-vignette).
license: CC-BY-4.0
metadata:
  title: Tell people what most of their peers already do
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: mixed-evidence
  tags: "social-norms, message-design, behavior-change-techniques"
  consumes: "social-norm-diagnosis, intervention-levers"
  produces: "intervention-draft"
---

## What it does

Writes one message that tells a person what most comparable people already do, or approve of, so that people behind the norm move toward it without people already ahead of it sliding back.

A descriptive norm is what most people in a group actually do; an injunctive norm is what most of them approve or disapprove of. People use both as a shortcut for what is sensible and expected, so correcting a mistaken belief about others can move behavior with no change in price, access, or information about the behavior itself. The same shortcut runs in reverse: a person who learns they are already better than average tends to drift toward the average. This skill writes the message, inserts the approval cue that blocks that drift, checks that the claim is true, and plans how the backfire will be detected. It does not decide whether a norm problem exists; `diagnose-social-norm` does that first.

## When to use it

### Use it when
- A social norm diagnosis says the behavior is held back by a mistaken belief about what others do (people think few pay, few deposit, few vaccinate, when most do), and the team wants to correct that belief
- Someone asks "can we just tell them most people already do this?" or wants a line like "8 out of 10 parents in your block..." in a letter, SMS, poster, or agent script
- A draft already contains a social-proof claim and the team wants it checked: is the number true, is the reference group close enough, will the people already doing well read it as permission to stop
- Administrative data show the desired behavior is already the majority (taxes paid, children immunized, deposits made) and the team wants to put that fact to work

### Do not use it when
- No one has checked whether a norm problem exists; a norm message aimed at a cost, access, or skill barrier wastes the channel exposure. Run `diagnose-social-norm` first
- The practice is held in place by the whole reference group's expectations and will only change if people see each other abandon it together; that is a coordinated event, `plan-collective-pledge`, not a message
- The technique chosen upstream is not social comparison and the team needs copy for it; `draft-lever-content` is the generic writer
- The question is how to measure what people believe others do or approve of; `draft-norms-vignette` (measure stage) builds that instrument

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The target behavior (who, what, when) and the true share of the closest reference group that already does it, with the data source and its date. No number, no message: this skill will not write "most people" on a guess. If the share is below half, stop and go to the specialist section before writing anything.
2. **Required.** What the target population currently believes others do (the empirical expectation) and whether they think others approve (the normative expectation), from `diagnose-social-norm` or equivalent field evidence. The gap between belief and reality is the only thing the message can correct; if people already know most do it, the message has no work to do.
3. **Required.** The reference group recipients would recognize as "people like me" (same village, clinic, market, or block), the channel, and who the message will appear to come from. The lever brief from `select-intervention-levers` or an audience and context brief usually carries this.
4. Optional. Whether recipients' own current standing is observable (a tax record, a deposit history), so the people already above the norm can be identified for the boomerang measurement.
5. Optional. Whether the behavior is stigmatized, illegal, or sensitive in this setting, which changes what may be said and who may say it.

If 1 is missing, ask and stop. If 2 is missing, ask once; if still missing, proceed and mark the belief gap "assumed, not measured" in the output, with a warning that the message may be wasted. If 3 is missing, ask once, then use the narrowest group the data support and flag the choice. If 4 and 5 are missing, assume standing is not observable and the behavior is not sensitive, and say so in the output.

## What it draws on

- Schultz, P. W., Nolan, J. M., Cialdini, R. B., Goldstein, N. J., & Griskevicius, V. (2007). The constructive, destructive, and reconstructive power of social norms. *Psychological Science*, 18(5), 429–434. https://doi.org/10.1111/j.1467-9280.2007.01917.x
- Allcott, H. (2011). Social norms and energy conservation. *Journal of Public Economics*, 95(9–10), 1082–1095. https://doi.org/10.1016/j.jpubeco.2011.03.003
- Hallsworth, M., List, J. A., Metcalfe, R. D., & Vlaev, I. (2017). The behavioralist as tax collector: Using natural field experiments to enhance tax compliance. *Journal of Public Economics*, 148, 14–31. https://doi.org/10.1016/j.jpubeco.2017.02.003
- Kettle, S., Hernandez, M., Ruda, S., & Sanders, M. (2016). Behavioral interventions in tax compliance: Evidence from Guatemala. World Bank Policy Research Working Paper 7690. https://doi.org/10.1596/1813-9450-7690
- Bicchieri, C. (2016). *Norms in the Wild: How to Diagnose, Measure, and Change Social Norms*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780190622046.001.0001
- Cialdini, R. B., & Jacobson, R. P. (2021). Influences of social norms on climate change-related behaviors. *Current Opinion in Behavioral Sciences*. https://doi.org/10.1016/j.cobeha.2021.01.005 (resolved from an author-year reference; author to confirm it is the intended paper)
- Del Carpio, L. Property-tax norm disclosure in Lima, Peru. Unverified, author to confirm; no citation details located.
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709
- Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity: A meta-analysis and a real-effort experiment. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x

Schultz et al. (2007) is the mechanism paper: told how their energy use compared with their neighbors', US households above the average cut back, but households below the average rose toward it (the boomerang); adding an injunctive cue that signaled approval kept the below-average households where they were. Allcott (2011) ran the same comparison at scale through the Opower program: energy use fell 2.0% on average, 6.3% in the top decile and 0.3% in the bottom decile, so almost all of the effect came from the people furthest from the norm. Hallsworth et al. (2017) found that UK tax letters citing the norm raised payment, and that descriptive wording beat injunctive wording. Kettle et al. (2016), the one verified non-WEIRD trial, sent letters to 43,387 Guatemalan taxpayers; the letter that cited the 64.5% who had already paid brought in about US$760k of extra revenue, 36 times the letter's cost, with effects still visible at 12 months. Bicchieri (2016) supplies the vocabulary (empirical and normative expectations) and the warning that a message only works where the belief it corrects is actually mistaken. See `references/evidence-notes.md` for the annotated list.

Judgment calls this skill adds: the hard stop when fewer than half do the behavior (the sources state the backfire rule; the threshold is this skill's operational line), the mandatory reference-group check, and the requirement to plan the boomerang measurement before anything is sent.

**WEIRD skew:** The mechanism and boomerang evidence (Schultz, Allcott) comes from US households, and the descriptive-beats-injunctive result from UK taxpayers. What varies locally is who counts as "people like me", whether a majority claim is believed, and whether approval from an official sender carries any weight. **Non-WEIRD evidence:** Guatemala (Kettle et al. 2016), 43,387 taxpayers, where a letter citing the 64.5% who had paid raised revenue by about US$760k at 36 times cost, persisting at 12 months; Peru (Del Carpio, Lima property tax, about 20% higher compliance than control) is unverified, author to confirm.

**Replication status:** Replicated in direction, small in magnitude; the boomerang is documented (Schultz) rather than contested, and the descriptive-over-injunctive ordering rests on one UK study. No citable meta-analysis of norm messages is among this skill's sources (two pooled estimates circulate with unverified authors and must not be quoted). Discount for a field program: across 126 nudge-unit RCTs the average effect was 1.4 percentage points against 8.7 in academic journals (DellaVigna & Linos 2022), and loss framing shrank from 0.33 SD in the lab to 0.02 SD in the field (Ferraro & Tracy 2022). Plan for a point or two on a binary outcome, not the Guatemala headline.

## How to do it

1. **Verify the true norm is favorable.** Carry over the share, its source, its date, and the group it describes. If fewer than half of the closest reference group do the behavior, do not write a descriptive message; a true statement that most people do not do it advertises the unwanted behavior. Stop and route to the specialist section.
2. **Pick the closest concrete reference group the data can support.** "Most vendors in Gikomba market" moves more than "most Kenyans", because people conform to people they see as like themselves. If the share is only known at a wider level, say so, and ask whether the same data can be cut narrower before settling.
3. **Decide descriptive, injunctive, or both.** Lead with the descriptive norm when the belief gap is about what others do (the UK trial found this stronger than approval alone). Always add the injunctive cue when some recipients are already above the norm; it is the only documented protection against the boomerang.
4. **State the number plainly** in the recipient's unit and time frame ("7 out of 10 parents in Rajgarh block brought their child for the measles dose last month"). Do not round up, do not use "most" without the number behind it, and do not hedge with a range that hides a minority.
5. **Write the injunctive cue** as a sentence of approval that a person already doing the behavior reads as "keep going" ("Thank you if you are one of them"), not as a comparison that tells them they can relax. In Schultz et al. a single approval cue did this work; in a letter or SMS, one sentence does.
6. **Check that nothing in the message publicizes the unwanted behavior.** "Many have not yet paid" is a descriptive norm for not paying. Remove it, including from the sender's framing and the subject line.
7. **Write the delivery notes:** the sender and why approval from that sender counts here, timing relative to the decision moment, and the number of exposures (the Guatemala effect came from a single letter).
8. **Plan the boomerang measurement before sending.** Pre-specify how recipients above and below the norm will be identified at baseline, the outcome in each group, and the decision rule: if the above-norm group moves down, the cue failed and the message stops. Without a comparison group this cannot be seen; say so.
9. **Stop here.** The local-language redraft and the comprehension pre-test follow the procedure in `draft-lever-content`; the ethics check is `audit-intervention-ethics`; `plan-evaluation-design` turns the measurement plan into a test.

See `references/worked-example.md` for a complete run on fertilizer timing in Western Kenya.

## Output template

```markdown
# Social norm message draft

**Target behavior:** <who + what + when, carried over verbatim>
**True descriptive norm:** <share who already do it, the group it describes, the data source, the date>
**Belief being corrected:** <what recipients believe others do or approve of, from the diagnosis; or "assumed, not measured">
**Norm type:** <descriptive / injunctive / both, with one clause on why>

## Message
<the literal text: one requested action, the number stated plainly, the reference group named, the injunctive cue in place>

## Injunctive cue
<the exact sentence or symbol that signals approval, and why it reads as "keep going" to someone already doing the behavior>

## Reference group check
- Group named in the message: <...>
- Group the number actually describes: <...>
- Match: <same / wider, and why the wider group was used if so>

## Backfire checks
- Majority check: <share is above half: yes or no; if no, this draft must not be sent>
- Unwanted-behavior prevalence: <confirm the message nowhere states or implies how many do not do it>
- Sensitivity: <stigma, legality, or household exposure, and what was changed because of it>

## Delivery notes
- Sender: <who, and why approval from them counts>
- Timing: <relative to the decision moment>
- Exposures: <how many, and the ceiling>

## Boomerang measurement plan
- Baseline split: <how above-norm and below-norm recipients are identified>
- Outcome by group: <what is measured in each, and when>
- Decision rule: <the result that stops the message>

## What to check before relying on this
- <the assumption most likely to be wrong, usually the belief gap or the reference group>
```

## Where it goes wrong

- **Inventing or rounding the norm.** "Most farmers already do this" with no number behind it, or 48% rounded to "about half", is the failure the first required question exists to prevent. If the claim is false it is unethical; if it is unverified, the first person who checks collapses trust in the sender.
- **Publicizing the minority.** "Only 35% have paid, be one of the responsible ones" states a descriptive norm for not paying. The rule is absolute: never publicize a high prevalence of the unwanted behavior, including as motivation.
- **Dropping the cue to fit the SMS.** The injunctive sentence is the first thing cut for length. Without it, people already doing the behavior read the comparison as permission to ease off (Schultz et al. 2007); Allcott's bottom decile moved 0.3% while the top moved 6.3%, which is the pattern the cue protects.
- **A reference group too wide to bite.** National or provincial figures are easy to find and weak to use. If the only number is wide, say so in the check rather than quietly naming a narrower group the number does not describe.
- **Running on a barrier that is not a norm.** If the diagnosis says people cannot afford, reach, or do the behavior, a message that most people do it adds pressure without removing the obstacle, and can shame the people it is aimed at.
- **Planning for the headline effect.** The 36-times-cost result in Guatemala came from one cheap letter on a large base. Budget and sample for a point or two of movement, and read the discount note above before promising more.

## When to bring in a specialist

Tell the user to consult a behavioral scientist, and where noted a local qualitative researcher or safeguarding lead, when:
- The true norm is unfavorable (under half) and the team still wants to use social information; a specialist can judge whether a trend, an injunctive-only message, or a different reference group is defensible, and whether the problem is really a collective one for `plan-collective-pledge`
- The behavior is stigmatized, illegal, or household-sensitive (HIV testing, contraception, informal income), where stating prevalence can expose people, the belief data may be distorted by under-reporting, and the sender's approval may not be welcome; a local qualitative researcher and a safeguarding lead review the message and who delivers it
- The message will go to everyone at once with no comparison group, because the boomerang is invisible without one; an evaluation specialist should see the plan before anything is sent
- The sender is a government or regulator and the number is a legal claim; counsel checks the figure and its date

Bring them: the share with its source and date, the norm diagnosis, the draft with its checks filled in, and the proposed baseline split.
