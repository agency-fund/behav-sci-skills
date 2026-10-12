---
name: draft-theory-of-change
description: >-
  Use when a program needs its logic written down as a causal chain: "write our
  theory of change", "what's the logic model for this program", "the funder wants
  to see how activities lead to the outcome", or "we have a goal and activities
  but nobody has said which behavior sits in between". Also use when a proposal
  asserts impact without naming the behavior each activity is meant to change, or
  when an evaluation is about to be planned on a chain nobody has made explicit.
  Produces a link-by-link table from activities to target behavior to outcome,
  with the assumption, the evidence, and the strength of evidence behind each
  link (Mayne's theory of change models; TAF Level 0). Do not use to pick the
  one behavior to work on; that is define-key-behavior, which takes this chain
  as input. Not for staging a digital product's user journey (build-user-funnel),
  and not for finding what research exists on the goal (assess-evidence-base).
license: CC-BY-4.0
metadata:
  title: Write the causal chain from activities to outcome
  type: atomic
  stage: define
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "theory-of-change, measurement, evaluation-framework"
  consumes: "program-goal"
  produces: "theory-of-change"
---

## What it does

Writes a program's theory of change as an explicit chain of links from activities to the target behavior to the outcome, with the assumption behind each link rated by its evidence.

A theory of change is the set of claims a program makes about why doing X leads to Y. Most programs carry one implicitly, in proposal prose. This skill turns each claim into a row that can be challenged, evidenced, or tested, with a named behavior in the middle, since a chain in which nobody acts differently is not a behavioral program. In The Agency Fund's four-level evaluation framework this is Level 0: the chain the later levels test. The skill does not choose the behavior, search for evidence, or design the test.

## When to use it

### Use it when
- Someone asks "write our theory of change" or "draft a logic model for this program"
- A proposal narrative or funder report asserts that the activities produce the outcome without naming the behavior in between
- An evaluation or measurement plan is about to be built and the chain it would test has never been written down
- Several activities are running and the team cannot say which assumption each one rests on, or which behavior each is meant to change
- A program is being redesigned and needs to know which links of the old chain had evidence behind them and which were hope

### Do not use it when
- The question is which single behavior to target among the ones the chain depends on; hand the chain to `define-key-behavior`, which states one as who, what, when and scores it
- The program is a digital or AI product and the need is a staged user journey with a metric per stage; that is `build-user-funnel`, which can consume this chain
- Nobody has checked what research exists on the behavior or outcome; run `assess-evidence-base` first or alongside, because this skill cites evidence per link but does not search for it
- The chain exists and the question is how to test it; that is `plan-evaluation-design`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The outcome the program is accountable for: what changes in whose lives, by when if the team has a date. If the user gives a behavior or an activity as the outcome ("more mothers attend antenatal visits"), say so and ask what change in people's lives it serves.
2. **Required.** The activities as delivered: what the program does, by whom, to whom, how often. A list is enough.
3. **Required.** The population: who the activities reach and who the outcome is for, where these differ (activities reach health workers; the outcome is for mothers).
4. Optional. What evidence the team already has for any link: an evidence scan brief from `assess-evidence-base`, monitoring data, a prior evaluation, pilot results. This fills the evidence column.
5. Optional. The behaviors the team already believes the chain runs through, so they are placed explicitly rather than hidden inside an activity-to-outcome arrow.

If 1, 2, or 3 is missing, ask and stop. If 4 is missing, ask once; if nothing comes back, proceed and mark every evidence cell "none supplied". If 5 is missing, derive the behaviors from the activities and flag each as "inferred by this skill, team to confirm".

## What it draws on

- Mayne, J. (2015). Useful theory of change models. *Canadian Journal of Program Evaluation*. https://doi.org/10.3138/cjpe.230
- W.K. Kellogg Foundation (2004). *Logic Model Development Guide*. https://wkkf.issuelab.org/resource/logic-model-development-guide.html
- The Agency Fund. Four-level evaluation framework, Level 0: theory of change. https://eval.playbook.org.ai/ (practice guidance, not a publication).
- Office of Evaluation Sciences (2021). Analysis plan template, July 2021. https://oes.gsa.gov/assets/files/AnalysisPlan.pdf (a practitioner example of a project description feeding testable hypotheses).

Mayne's argument is that a theory of change is useful only when it states the assumptions and risks behind each causal link, not just the boxes. The Kellogg guide supplies the logic model's columns (resources, activities, outputs, outcomes, impact) as practical assistance to nonprofits. TAF's framework places the theory of change at Level 0, so everything later evaluated at Levels 1 to 3 is a test of some link written here. OES, eMBeD, and 3ie work from theories of change in practice; the claim that the method is "common in donor M&E" is unverified, author to confirm. The judgment calls this skill adds, none of them published criteria: the chain must pass through at least one named behavior (who does what, when); every link carries an assumption and an evidence cell; and strength uses four labels (tested here, tested elsewhere, plausible mechanism, assumption) so a chain built on hope reads as one.

**WEIRD skew:** The method is procedural, with no effect size and no study population, so the skew is in who wrote the guidance: Mayne from Canadian government evaluation practice, Kellogg from US nonprofit practice. Both assume only that a reader can name a program's activities and outcomes, which holds anywhere. What a user elsewhere should check locally is the evidence cells, not the method: a link whose evidence comes from a different population is at most "tested elsewhere" and should go through `assess-evidence-transferability` before the rating is raised. **Non-WEIRD evidence:** none found in the sources this skill draws on; eMBeD and 3ie apply the method in low- and middle-income country programs, as practice rather than as a study.

**Replication status:** Framework, no effect to replicate; no validation study of the method exists in the sources this skill draws on. The four strength labels and the named-behavior rule are this skill's additions.

## How to do it

1. **Carry the outcome over verbatim** at the top, then check it is an outcome (a change in people's lives), not a behavior or an output. If it is a behavior, keep it as the target behavior row and ask what outcome it serves; do not promote it.
2. **List the activities as delivered**, one per row, as the left end of the chain. Planned-but-not-running activities get a row marked "planned", because a chain that mixes the two will be tested against activities that never happened.
3. **Name the behavior each activity runs through**: who must do what, when, as a result of it. If an activity reaches the outcome without any person doing anything differently, it is an output, not a link; say so in the row.
4. **Write each link** as from, to, and the assumption in the form "if X then Y because Z". Where the link is behavioral, the "because" is the mechanism, in one clause.
5. **Fill the evidence cell only from what the user supplied.** Write "none supplied" rather than a plausible citation; a theory of change with invented evidence is worse than one with gaps because it stops the team looking. If an evidence scan brief exists, carry its finding and its WEIRD-skew flag into the cell.
6. **Rate the strength** with the four labels. A finding from a different population is at most "tested elsewhere"; the team's belief is "assumption"; a mechanism argument without data is "plausible mechanism"; "tested here" needs data from this population.
7. **List the behaviors the chain depends on** in their own section, each tied to its link number and marked confirmed by the team or inferred by this skill, so `define-key-behavior` has a list to choose from.
8. **Name the weakest links**: the link nearest the outcome with the lowest rating is usually where the program fails. Say which, why, and what evidence would raise its rating.
9. **Stop here.** Do not choose the behavior (`define-key-behavior`), search for evidence (`assess-evidence-base`), or design the test (`plan-evaluation-design`).

See `references/worked-example.md` for a complete run on a rural immunization program in Rajasthan and `references/evidence-notes.md` for the sources.

## Output template

```markdown
# Theory of change

**Outcome (as given):** <who, what change, by when>
**Population:** <who the activities reach; who the outcome is for, if different>
**Activities (as delivered):** <list; mark any that are planned, not running>
**Evidence supplied:** <evidence scan brief / monitoring data / prior evaluation / none>

## Causal chain

| # | Link (from, to) | Assumption (if ..., then ..., because ...) | Evidence | Strength |
|---|---|---|---|---|
| 1 | <activity>, <output or behavior> | <...> | <source as supplied, or "none supplied"> | <tested here / tested elsewhere / plausible mechanism / assumption> |
| 2 | <behavior>, <intermediate outcome> | <...> | <...> | <...> |
| 3 | <intermediate outcome>, <outcome> | <...> | <...> | <...> |

## Behaviors the chain depends on
- <who does what, when> (link <#>); <confirmed by team / inferred by this skill>

## Weakest links
- Link <#>: <why it is the weakest>; <the evidence that would raise its rating>

## What to check before relying on this
- <the assumption most likely to be wrong>
- <any link rated "tested elsewhere" that needs a transferability check>
- <behaviors inferred by this skill that the team has not confirmed>
```

## Where it goes wrong

- **Outputs dressed as outcomes.** "500 mothers trained" or "20,000 messages sent" is an output: something the program did. The chain must continue to what the trained or messaged person does differently, then to what changes because of it. A chain that ends at an output has no outcome row.
- **Chains with no person in them.** An arrow from "SMS campaign" to "lower stunting" skips the behavior that would have to change. Refuse to write a link nobody has to act on; if the team cannot name the behavior, the row says "behavior unknown" and the strength is "assumption".
- **Invented evidence.** The evidence cell is where a model is most tempted to be helpful: a plausible citation, a remembered effect size. Only what the user supplied or an evidence scan brief contains goes in; otherwise "none supplied". Never upgrade a rating on evidence recalled from memory.
- **Rating inflation.** A pilot the team ran but did not measure is not "tested here"; a finding from another country is not "tested here" either, however similar the setting looks. The label asks where the data came from, not how confident the team feels.
- **One chain for several outcomes.** A program claiming three outcomes gets three chains, or a question about which one matters most; a single chain with three endpoints hides which links are shared and which are unique.
- **Treating the table as the evaluation.** The chain says what should be tested. It is not evidence that the program works, and a complete-looking table should not be read as one.

## When to bring in a specialist

Tell the user to consult an evaluation specialist or a behavioral scientist when:
- The chain will justify a funding, scale-up, or policy decision and its critical link is rated "assumption" or "tested elsewhere"; the next step is a test, not a tidier table
- A link passes through clinical, safety, or child-protection behaviors (medication, violence, reporting), where the assumption cannot be checked by asking and the chain itself needs ethical review
- The team disagrees about which behavior the chain runs through; that is a design disagreement a table cannot settle, and `define-key-behavior` run twice will not settle it either

Bring them: the chain table, the evidence supplied for each link, and the weakest-links section.
