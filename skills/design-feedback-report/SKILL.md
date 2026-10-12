---
name: design-feedback-report
description: >-
  Use when a program wants to send people a regular report on how they are
  doing: health workers' visit counts, teachers' session or attendance
  records, households' water or energy use, savings-group deposits. Also
  use when a team already sends performance data and wants to know why it
  is not working or why some people got worse after seeing it. Specifies
  the task-level metric, the comparison (own past, peers, or a standard)
  with an injunctive cue, the cadence, and the protections for top and
  bottom performers, drawing on Kluger and DeNisi (1996) and Allcott and
  Rogers (2014). Do not use when the team needs a one-off "most people do
  X" message rather than repeated personal feedback; use
  write-social-norm-message instead. Not for public rewards or certificates
  (design-social-recognition), not for monitoring delivery for the
  program's own management (design-fidelity-monitoring), and not for
  writing the final report wording (draft-lever-content).
license: CC-BY-4.0
metadata:
  title: Design a performance feedback report
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: mixed-evidence
  tags: "feedback, social-norms, message-design, behavior-change-techniques"
  consumes: "intervention-levers, measurement-plan"
  produces: "intervention-draft"
---

## What it does

Specifies what a repeated feedback report tells one person about their own performance on a task: which metric, compared with what, how often.

Feedback works by making a gap visible between what the person did and a standard, so that attention goes to closing it. It fails, often, when it turns attention from the task to the person: praise, blame, or a rank makes people defend themselves rather than fix the work. The meta-analytic average is positive, yet more than a third of feedback interventions made performance worse, and effects decay once the reports stop. This skill designs the report so it stays on the task, keeps arriving, and does not push the best or the worst performers backward.

## When to use it

### Use it when
- "We want to text each community health worker every month with how many home visits they completed"
- "Teachers will get their class's assessment results each term; how should we present them?"
- "Our household water-use report is not moving anyone, and some households used more after getting it"
- The lever brief from `select-intervention-levers` names one of the BCTTv1 feedback techniques (feedback on behavior, or feedback on the outcomes of behavior) and the next question is what the report should contain

### Do not use it when
- The team wants a single message saying what most people do, with no personal data in it; that is `write-social-norm-message`
- The plan is to reward good performers publicly with a certificate, badge, or ceremony; that is `design-social-recognition`, which trades on visibility rather than private information
- The data are collected so the program can check it is being delivered as designed, and are not returned to the person; that is `design-fidelity-monitoring` (implement stage)
- The report's design is settled and the team needs the actual wording; that is `draft-lever-content`
- No barrier has been confirmed; a report that lands on a supply, pay, or trust barrier moves nothing, so run `select-intervention-levers` first

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The behavior the feedback is about, as who, what, when, and the lever brief that chose feedback for a confirmed barrier. Feedback addresses not knowing how one is doing; it does nothing for a barrier of supplies, pay, or skill.
2. **Required.** What data exist at the level of the individual person, how often they are collected, and how trustworthy they are. Paste the measurement plan if one exists. Feedback on a number the person believes is wrong costs trust that does not come back.
3. **Required.** Who will see each person's report: only the person, their supervisor, their peers, the public. If supervisors could use it in appraisal, pay, or discipline, say so now; that changes the design and is an escalation condition.
4. Optional. The current distribution of performance (roughly how many are far below, near, or above any standard), which sets the top and bottom designs.
5. Optional. The channel (SMS, paper, app, meeting) and the recipients' literacy and numeracy.

If 1, 2, or 3 is missing, ask and stop. If 4 is missing, proceed and design both the top-performer and the bottom-performer protections as if each group exists. If 5 is missing, assume a short text or one-page paper report and flag it.

## What it draws on

- Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. *Psychological Bulletin*, 119, 254–284. https://doi.org/10.1037/0033-2909.119.2.254
- Allcott, H., & Rogers, T. (2014). The short-run and long-run effects of behavioral interventions: Experimental evidence from energy conservation. *American Economic Review*, 104(10), 3003–3037. https://doi.org/10.1257/aer.104.10.3003
- Schultz, P. W., Nolan, J. M., Cialdini, R. B., Goldstein, N. J., & Griskevicius, V. (2007). The constructive, destructive, and reconstructive power of social norms. *Psychological Science*, 18(5), 429–434. https://doi.org/10.1111/j.1467-9280.2007.01917.x
- Allcott, H. (2011). Social norms and energy conservation. *Journal of Public Economics*, 95(9–10), 1082–1095. https://doi.org/10.1016/j.jpubeco.2011.03.003
- Muralidharan, K., & Sundararaman, V. (2010). The impact of diagnostic feedback to teachers on student learning: Experimental evidence from India. *The Economic Journal*. https://doi.org/10.1111/j.1468-0297.2010.02373.x (the result is not recorded in the dossier: unverified, author to confirm from the paper before stating it)
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709
- Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity: A meta-analysis and a real-effort experiment. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x

Feedback intervention theory (Kluger & DeNisi, 1996) says feedback works by directing attention to a gap between performance and a standard; across 607 effect sizes the average effect was d = 0.41, yet more than one-third of feedback interventions reduced performance. The reductions sit where feedback moves attention from the task to the self: praise, blame, and ranking of the person rather than the work. The Opower home energy reports (Allcott, 2011; Allcott & Rogers, 2014) are the field anchor for a repeated comparison report: energy use fell 2.0% on average, the top decile of users cut 6.3% and the bottom decile 0.3%, so the response came from those furthest from the comparison; recipients acted after each report and backslid between them ("action and backsliding"), and when reports stopped after two years the effect decayed 10–20% per year. Schultz et al. (2007) documented the boomerang: people already better than the norm drift toward it when shown a peer comparison, unless an injunctive cue (a sign of approval) tells them they are doing well. Muralidharan & Sundararaman (2010) is cited here only as an experiment on diagnostic feedback to teachers in India; the dossier does not record its result. The judgment calls this skill adds: one task-level metric per report; a rule for choosing among own-past, peer, and standard comparisons; cadence tied to the data cycle with a recurring budget rather than a campaign; and separate protections for the top and the bottom of the distribution. See `references/evidence-notes.md`.

**How much to discount.** The d = 0.41 average pools decades of mostly laboratory and organizational studies. The dossier's cross-cutting pattern (lab 0.33 SD against field 0.02 SD for loss contracts, Ferraro & Tracy, 2022; academic trials 8.7 points against nudge-unit trials 1.4 points, DellaVigna & Linos, 2022) says to discount published effects when transferring them to a field program. Plan on something nearer the Opower field benchmark, a 2.0% average change concentrated in the group furthest from the comparison, than on d = 0.41.

**WEIRD skew:** The meta-analysis pools organizational and educational psychology studies from the pre-1996 literature, overwhelmingly from high-income countries; the Opower and Schultz evidence is US households. Check locally how a comparison with peers is read: in a small team or village, "the average worker in your district" may be readable as named individuals, which turns private feedback into public ranking. **Non-WEIRD evidence:** India (Muralidharan & Sundararaman, 2010): an experiment on diagnostic feedback to teachers; the citation is verified but its result is not recorded in the dossier, so it cannot be used as evidence in either direction (unverified, author to confirm). Otherwise none found in the sources this skill draws on.

**Replication status:** Replicated in direction with high heterogeneity: d = 0.41 across 607 effect sizes, with more than one-third of interventions negative; the self-focus backfire and the peer-comparison boomerang are each documented; decay after reports stop is documented in one large field setting.

## How to do it

1. **Carry over the behavior and the lever** verbatim, and state in one line what the person does not currently know about their own performance. If the honest answer is "they know, they lack supplies or pay", stop and send it back to `select-intervention-levers`.
2. **Choose one task-level metric**: observable, counted the same way every period, and something the person can move by their own action within one period. An outcome the person cannot move alone (a child's test score, a village's disease rate) is a second metric at most, labeled as an outcome, never the headline.
3. **Choose the comparison** and write the reason: own past (safest; the default when peers differ for reasons outside their control or no standard exists), peers (strongest pull, boomerang risk; needs a close reference group the person recognizes and an injunctive cue), or a standard (when a defensible one exists and most people are below it). See `references/evidence-notes.md` for what each rests on.
4. **If peers, add the injunctive cue**: an explicit mark of approval for those at or above the norm, so the best performers are not told, in effect, to relax.
5. **Keep attention on the task.** No person-level labels, no ranks, no praise of the person. State the number, the comparison, the gap, and one concrete next action the person can take before the next report.
6. **Set the cadence** to the data cycle, no faster than the data are refreshed, and plan for decay: the report continues as long as the behavior is wanted, budgeted as a recurring cost. Write down what the team expects to happen if it stops.
7. **Design for the top and the bottom.** Top: the injunctive cue, and a switch to own-past comparison once someone is above the norm. Bottom: show the gap to the next step, not to the top, and make the next action small enough to complete before the next report.
8. **Fix who sees it.** The person sees their own report. If a supervisor sees it, write what the supervisor may and may not do with it; if that cannot be guaranteed, go to "When to bring in a specialist".
9. **Pilot before scaling**: a subset with a comparison group, the behavior measured, and the top and bottom groups read separately, so a fall among people who were already doing well is caught before scale.
10. **Stop here.** `draft-lever-content` writes the report's wording; `plan-evaluation-design` sets up the pilot.

See `references/worked-example.md` for a complete run on reading-session feedback to teachers in Bihar.

## Output template

```markdown
# Feedback report specification

**Behavior:** <who + what + when, carried over verbatim>
**What the person does not currently know:** <the information gap the report closes>
**Data source:** <where each person's number comes from, how often, known reliability problems>

## Metric
- **Headline (task-level):** <one metric the person can move by their own action in one period>
- **Secondary (outcome, optional):** <labeled as an outcome; or "none">

## Comparison
- **Type:** <own past | peers | standard>, because <reason>
- **Reference group or standard:** <who or what, and why the person will recognize it>
- **Injunctive cue:** <the approval mark shown to those at or above the norm; or "not needed: own-past comparison">

## Report content (one period)
<the skeleton: the number, the comparison, the gap, one next action; no rank, no label, no praise of the person>

## Cadence and duration
- **Frequency:** <matched to the data cycle>
- **Duration:** <as long as the behavior is wanted; recurring budget line>
- **If it stops:** <what the team expects, from the decay evidence>

## Top performers
<what they see, and how boomerang is prevented>

## Bottom performers
<what they see, and how discouragement is prevented>

## Who sees it
<the person; any supervisor, with what they may and may not do with it>

## Pilot before scaling
<subset, comparison group, outcome, and the separate read of top and bottom groups>

## What to check before relying on this
- <the data-quality assumption most likely to be wrong>
- <whether the comparison reads as private feedback or public ranking here>
```

## Where it goes wrong

- **Feedback about the person.** "You are one of our weaker CHWs", "Great job, star teacher", or a league table that ranks everyone against everyone moves attention to the self; that is where the one-third of negative results live. A rank is a label. State the number, the gap, and the next action.
- **A metric the person cannot move.** Test scores, disease rates, and deposits by other members depend on others; feedback on them teaches helplessness, not the behavior. Headline the task.
- **Campaign thinking.** Three months of reports and then silence. The evidence says the effect decays 10–20% a year after reports stop; a report that cannot be sustained should not be started without saying so.
- **Peer comparison without an injunctive cue.** The best performers see they are above average and drift down. The cue is not decoration; the boomerang is documented.
- **Routing it to supervisors as a management tool.** Feedback that feeds appraisal, pay, or discipline is monitoring, not feedback, and people respond by gaming the number. This skill refuses to design that; see below.
- **Asserting the India teacher result.** The dossier verifies the citation and not the finding; do not write what it found.

## When to bring in a specialist

Tell the user to consult the relevant specialist when:
- Supervisors could use the report punitively, in appraisal, pay, or discipline; an HR, labor, or ethics reviewer and the program's own management should agree the rules of use before any design is piloted
- The metric is a clinical quality measure (doses given, cases referred, protocol steps completed); a clinician must confirm the metric is safe to optimize on its own
- Individual-level data are so thin or unreliable that a wrong number is likely; an M&E lead should fix the measurement before anyone is told how they are doing
- The pilot shows a fall among people who were already doing well; a behavioral scientist should look at the comparison and cue design before scaling

Bring them: the metric and comparison with their reasons, the report skeleton, the data-quality notes, and the pilot results split by top and bottom groups.
