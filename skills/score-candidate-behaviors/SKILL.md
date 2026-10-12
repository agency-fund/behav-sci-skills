---
name: score-candidate-behaviors
description: >-
  Use when a team has a long list of behaviors that could move its goal and asks
  "which one should we go after?", "how do we prioritize these?", or "we can't
  work on all of them". Also use when a workshop produced ten candidate behaviors
  and the choice is about to be made by whoever argues loudest, or when the team
  is drawn to the behavior that is easiest to deliver rather than the one that
  matters. Scores each candidate on impact on the goal, likelihood the audience
  will adopt it, and current prevalence (the Impact-Likelihood Matrix, Kneebone,
  Smith and Fielding 2017; BehaviourWorks Method) and returns a shortlist in
  which every score shows whether it rests on data, audience input, or a team
  guess. Do not use to define the one chosen behavior as who does what, when,
  or to score it with APEASE; that is define-key-behavior, run on the winner.
  Not for a digital product's user journey (build-user-funnel) or for why a
  behavior is not happening (decompose-comb-barriers).
license: CC-BY-4.0
metadata:
  title: Rank many candidate behaviors before choosing one
  type: atomic
  stage: define
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: weird-only
  tags: "behavior-definition, behavior-prioritization, impact-likelihood-matrix"
  consumes: "program-goal"
  produces: ""
---

## What it does

Ranks a long list of candidate behaviors on three scores (impact, likelihood of adoption, current prevalence) so a team can shortlist before committing to one.

The Impact-Likelihood Matrix plots each behavior by how much it would move the goal if adopted (impact) against how likely the audience is to take it up (likelihood), with current prevalence (how many already do it) deciding how much headroom is left. The output is a shortlist, not a definition: the winner goes to `define-key-behavior` to be stated as who does what, when and checked with APEASE. The discipline this skill adds is that every score carries its basis, so a team guess cannot pass as a measurement.

## When to use it

### Use it when
- Someone asks "we have twelve possible behaviors; which should we focus on?" or "how do we prioritize these?"
- A workshop or stakeholder session produced a long candidate list and the choice is about to be made by intuition, seniority, or who spoke last
- The team is drawn to a behavior because it is easy to deliver, or because many people already do it, without checking its impact on the goal or the headroom left
- A funder or partner asks why this behavior rather than another, and the team has no written comparison
- Several programs in a portfolio target the same goal through different behaviors and need a common basis for comparison

### Do not use it when
- The list is one or two behaviors and the question is how to state the chosen one precisely; `define-key-behavior` does that, with APEASE
- A behavior is already chosen and the question is why people are not doing it; `decompose-comb-barriers`
- The "behaviors" are steps in a digital product's journey from first contact to outcome; `build-user-funnel`
- Nobody has written down the goal or the chain the behaviors sit in; state the goal plainly or run `draft-theory-of-change` first, because impact is scored against the goal

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The goal in one sentence, with the population it is for. Impact is scored against this goal; without it every impact score is relative to nothing.
2. **Required.** The candidate list, each as who does what (with what, where, when). If the list contains outcomes ("better nutrition"), vague verbs ("engage"), or compound behaviors joined by "and", say which and ask for them to be split or dropped. Four or more candidates; with fewer, `define-key-behavior` handles the comparison itself.
3. **Required.** What the scores can rest on: for impact, any evidence (an evidence scan brief from `assess-evidence-base`, expert views, the team's experience); for likelihood, whether the audience has been asked (survey, interviews, workshop with members of the audience) or the team is guessing; for prevalence, whether any data exist (survey, monitoring, census). This sets the basis label on every score.
4. Optional. Constraints that remove candidates before scoring: illegal, unethical, outside the program's mandate, or already fully covered by another actor.
5. Optional. An audience and context brief from `map-audience-context`, which sharpens the likelihood scores.

If 1 or 2 is missing, ask and stop. If 3 is missing, ask once; if nothing comes back, proceed with every basis labelled "team guess" and say in the first line of the output that the ranking is a hypothesis for the audience to check. If 4 and 5 are missing, assume no constraints and no brief.

## What it draws on

- Kneebone, S., Smith, L., & Fielding, K. (2017). The Impact-Likelihood Matrix: A policy tool for behaviour prioritisation. *Environmental Science & Policy*, 70, 9–20. https://doi.org/10.1016/j.envsci.2016.11.013
- Selinske, M. J., et al. (2020). Identifying and prioritizing human behaviors that benefit biodiversity. *Conservation Science and Practice*. https://doi.org/10.1111/csp2.249
- BehaviourWorks Australia. *The Method*, chapter 5, "Getting ready to Deep Dive: Defining, identifying and prioritising behaviours". https://www.behaviourworksaustralia.org/resources/the-method-book (no authors or year on the page)
- Presseau, J., et al. (2019). Action, actor, context, target, time (AACTT): A framework for specifying behaviour. *Implementation Science*, 14, 102. https://doi.org/10.1186/s13012-019-0951-x
- Gyani, A., Tindall, K., & Gallagher, R. (2022). *Explore Field Guide*. Behavioural Insights Team. https://www.bi.team/wp-content/uploads/2022/11/BIT-Explore-Field-Guide.pdf (TESTS: "Target: identify and prioritise the specific behaviours to change")
- OECD (2019). *Tools and Ethics for Applied Behavioural Insights: The BASIC Toolkit*. https://doi.org/10.1787/9ea76a8f-en

Kneebone, Smith and Fielding built the matrix to rank household water behaviors for Australian policy: each behavior is scored on its impact on the goal, the likelihood the audience adopts it, and its current penetration (the share already doing it), with impact from experts or the literature, likelihood from an audience survey, and penetration from prevalence data. Selinske et al. applied the same logic to behaviors that benefit biodiversity. BehaviourWorks' chapter 5 sets the matrix inside a wider prioritization step and supplies the working definition of a behavior, "WHO does WHAT with WHAT, WHERE and WHEN", with AACTT (action, actor, context, target, time) as a supporting specification tool; BIT's TESTS process and OECD's BASIC toolkit name the same prioritization step without a scoring method. The judgment calls this skill adds, none of them in the sources: every score carries a basis label (data, audience input, team guess); penetration is applied as a headroom adjustment to impact, shown in its own column so a reviewer can see where it changed a rank; and the plot is described in words by quadrant so the result survives a text-only channel.

**WEIRD skew:** The matrix was validated on Australian domestic water behaviors, and BehaviourWorks has since used it for recycling, food waste, and bushfire safety, all in Australia. The scoring logic does not depend on the population, but two things do: likelihood ratings only mean something when they come from the audience, and teams in any setting overrate how likely people are to adopt what the team can deliver. A user elsewhere should check locally that likelihood was rated by members of the audience, not by staff on their behalf; that prevalence data exist rather than being assumed; and that "impact" as experts see it is the impact on the goal the program is accountable for, not on a proxy. **Non-WEIRD evidence:** none found in the sources this skill draws on.

**Replication status:** Single-study: the matrix is peer-reviewed and was validated in one Australian application; no replication in another country or domain appears in the sources this skill draws on. The basis labels are this skill's rule, not a published one.

## How to do it

1. **Carry the goal and population over verbatim** at the top, so every impact score is visibly about that goal.
2. **Clean the list.** Rewrite each candidate as who does what, with what, where, when. Send back outcomes and compound behaviors with a one-line reason; remove candidates that fail the constraints in question 4 and record why. Count received, scored, and removed.
3. **Score impact (1 to 5)** per candidate: if everyone in the population did this, how far would the goal move? Write the basis beside the score: data (a named source), audience input, or team guess. An impact score from an evidence scan brief carries that brief's WEIRD-skew flag.
4. **Score likelihood of adoption (1 to 5)**: how likely the audience is to take the behavior up given its current barriers. Audience input counts only if it came from members of the audience; if the team is guessing, label it so and write the one question that would get the audience's answer.
5. **Record current prevalence** as a percentage or band with its basis, then adjust impact for headroom: a behavior that most people already do has little room to move, however high its impact if adopted universally. Show the adjustment in its own column rather than silently changing the impact score.
6. **Place each candidate in a quadrant** by headroom-adjusted impact and likelihood: high impact, high likelihood (do first); high impact, low likelihood (worth the harder work; the barrier is the next question); low impact, high likelihood (quick wins that do not move the goal); low impact, low likelihood (drop). Describe the plot in words.
7. **Shortlist the top two to four**, with the reason each made it and which of its scores rest on team guesses. A shortlist position that rests on a guess is flagged in the shortlist itself, not only in the table.
8. **Say what would change the ranking**: usually the audience's own likelihood ratings or prevalence data, with the cheapest way to get each.
9. **Stop here.** Hand the top candidate to `define-key-behavior` for who, what, when and the APEASE check. Do not define, diagnose, or design.

See `references/worked-example.md` for a complete run on sanitation behaviors in Indonesian villages and `references/evidence-notes.md` for the sources.

## Output template

```markdown
# Candidate behavior scoring

**Goal:** <one sentence, carried over verbatim>
**Population:** <who the goal is for>
**Candidates received:** <n>; **scored:** <n>; **sent back or removed:** <n, each with its reason>
<if every likelihood basis is "team guess": "This ranking is a hypothesis for the audience to check; no likelihood score came from the audience.">

## Scoring matrix

| # | Behavior (who does what, with what, where, when) | Impact (1–5) | Basis | Likelihood (1–5) | Basis | Current prevalence | Basis | Headroom-adjusted impact |
|---|---|---|---|---|---|---|---|---|
| 1 | <...> | <n> | <data: source / audience input: how / team guess> | <n> | <...> | <% or band, or unknown> | <...> | <n, with the adjustment stated> |

Basis labels: data = a named measured source; audience input = members of the audience were asked; team guess = nobody outside the team rated this.

## Quadrants (the plot, in words)
- **High impact, high likelihood:** <behaviors>; <why>
- **High impact, low likelihood:** <behaviors>; <the barrier that lowers likelihood, to diagnose>
- **Low impact, high likelihood:** <behaviors>; <quick wins; not progress on the goal>
- **Low impact, low likelihood:** <behaviors>; dropped

## Shortlist
1. <behavior>: <why it ranks here>; <which of its scores are team guesses>
2. <...>

## What would change this ranking
- <the audience's likelihood ratings, if not collected: the question to ask and to whom>
- <prevalence data, if unknown: where to get them>

## Open questions
- <anything the scoring could not settle>
```

## Where it goes wrong

- **Team guesses passing as evidence.** A matrix of numbers looks measured. A score without a basis label is not allowed, and a shortlist in which every likelihood score is a team guess must say so in its first line, because that is the version a funder will otherwise read as data.
- **Likelihood rated by the team, not the audience.** The source method sends likelihood to an audience survey for a reason: staff overrate how willing people are to adopt what the program can deliver. If no audience input exists, the skill writes the question that would get it rather than filling the column with confidence.
- **Scoring outcomes or compound behaviors.** "Improve hygiene" has no actor; "build and use a latrine" hides two behaviors with different likelihoods and different barriers. Send both back before scoring; a score on either is a score on nothing.
- **Ignoring prevalence.** A behavior with high impact that 90% already do has 10% headroom. Without the adjustment the matrix ranks the behavior the program would spend its budget confirming.
- **Mistaking the quick-win quadrant for progress.** Low-impact, high-likelihood behaviors are tempting because adoption will show up fast; they do not move the goal, and the output must say so next to them.
- **Letting the matrix decide.** The matrix shortlists; the team chooses; `define-key-behavior` checks the choice with APEASE (acceptability, practicability, effectiveness, affordability, spillover, equity). A rank-one score is not a decision, and the skill must not present it as one.

## When to bring in a specialist

Tell the user to consult a behavioral scientist or a local qualitative researcher when:
- The list includes behaviors with safety, legal, or coercion risk (disclosure to a partner, reporting a neighbor, taking or stopping medication), where "likelihood of adoption" cannot be read off a survey and the candidate may need to be removed on ethical grounds rather than scored
- Impact scores rest on thin or contested evidence and the choice commits a large budget; an evidence specialist should rate impact, with `assess-evidence-base` run first
- The audience is one the team does not know and no audience input is feasible before the decision; a local researcher should run the likelihood ratings rather than the team guessing

Bring them: the cleaned candidate list, the matrix with its basis labels, and the questions under "What would change this ranking".
