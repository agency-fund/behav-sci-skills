---
name: plan-scale-up-strategy
description: >-
  Use when a tested intervention must move from a pilot into a system that
  will deliver it routinely and someone asks "how do we scale this?", "how do
  we hand this to the ministry?", or "who owns this after the project ends?".
  Also use when a scalability assessment returned "scale" or "scale after
  these tests" and the next document is the strategy, or when a partner has
  agreed in principle and nobody has written down the sequence, owners, or
  financing. Produces a scale-up strategy after the WHO/ExpandNet guide
  (2010): the innovation package, the user organization, the resource team,
  the environment, the strategic choices (vertical or horizontal scaling,
  pace, financing, monitoring), and an action plan with owners and dates. Do
  not use before the effect has been judged likely to survive scale; run
  assess-scalability first. Not for recording changes to the intervention
  itself (specify-intervention-adaptations), and not for the fidelity
  indicators the roll-out will track (design-fidelity-monitoring).
license: CC-BY-4.0
metadata:
  title: Plan how a tested program reaches routine delivery
  type: atomic
  stage: implement
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "scaling, implementation-science, implementation"
  consumes: "scalability-assessment"
  produces: ""
---

## What it does

Turns a tested intervention plus its scalability assessment into a strategy for moving it into a system that will deliver it routinely.

The WHO/ExpandNet guide treats scaling up as deliberate work with named parts: an innovation, a user organization that will own it, a resource team that supports the move, an environment that helps or hinders, and the strategic choices that connect them. This skill walks those parts, makes each choice explicit with its reason, and ends in an action plan in which every line has an owner and a date. It assumes the effect has already been judged likely to survive scale; it does not make that judgment, and it does not change the intervention.

## When to use it

### Use it when
- Someone asks "how do we scale this?", "how do we get the ministry to take this over?", or "what happens to this when our grant ends?"
- `assess-scalability` returned "scale" or "scale after these tests" and the next document is the plan
- A government, district, or large delivery partner has agreed in principle and the sequence, owners, financing, and monitoring are not written down anywhere
- A donor asks for a sustainability or exit plan for a program that currently runs on project staff
- The team is about to expand to more sites "the same way as the pilot" without deciding who will run it routinely

### Do not use it when
- Nobody has judged whether the effect will survive scale; run `assess-scalability` first, because a strategy for an effect that will not survive is a plan to spend money
- The question is which parts of the intervention can change for the new sites and which cannot; `specify-intervention-adaptations`, whose core-component list is this skill's input
- The question is what indicators the roll-out will track to catch drift; `design-fidelity-monitoring`
- The causal chain the scale-up must preserve is not written down; `draft-theory-of-change` first
- A past roll-out failed and the team wants to know why before planning again; `review-prior-intervention`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The scalability assessment from `assess-scalability`: the verdict and the "what must be true" list. If none exists, stop and send the user there.
2. **Required.** The innovation package: what exactly is being scaled, its core components and adaptable parts (from `specify-intervention-adaptations` or the intervention description), and the materials, training, and supervision it needs.
3. **Required.** The user organization: who will deliver routinely, whether it has asked for this, what it would have to do differently, and who inside it champions the program. The resource team: who holds the know-how, what it will provide, and for how long.
4. **Required.** The environment: the policy that governs this area, the budget cycle and who sets it, known supporters and opponents, elections or reorganizations in the next two years, and programs competing for the same staff.
5. Optional. The theory of change; any fidelity plan; financing options already explored; whether others have begun copying the program uninvited.

If 1, 2, 3, or 4 is missing, ask and stop; for 1, say that the assessment comes first. If 5 is missing, proceed and mark the monitoring and financing sections "to be developed".

## What it draws on

- World Health Organization & ExpandNet (2010). *Nine steps for developing a scaling-up strategy*. WHO. https://www.who.int/publications/i/item/9789241500319
- Milat, A. J., et al. (2020). Intervention Scalability Assessment Tool: A decision support tool for health policy makers and implementers. *Health Research Policy and Systems*, 18. https://doi.org/10.1186/s12961-019-0494-2
- Management Systems International. *Scaling Up Management* framework. Unverified, author to confirm: the dossier located no page for it.

The WHO/ExpandNet guide (dated 20 September 2010; 41 pages) states its aim as facilitating systematic planning for scaling up. Its elements, as the dossier records them, are the innovation (what is being scaled), the user organization (who adopts it and delivers it routinely), the environment (the policy, budget, and political conditions around them), the resource team (who supports the move), and the strategic choices that connect them. The guide organizes planning into nine steps; the dossier does not itemize those steps, so this skill walks the five elements and describes the planning actions generically rather than quoting step names, and the author should check the wording of each section against the guide. Milat et al.'s Intervention Scalability Assessment Tool is the assessment that precedes the strategy, which is why this skill consumes a scalability assessment and refuses to run without one. Nothing is quoted from the MSI framework. The judgment calls this skill adds, none of them published criteria: the distinction between scaling the program and scaling the organization that piloted it; vertical scaling (institutionalization into policy, budgets, job descriptions, and information systems) and horizontal scaling (expansion to more sites or populations) as a choice made explicitly, with a pace tied to the assessment's open tests; the resource team's exit date as a mandatory field; and an action plan in which every line has a named role as owner.

**WEIRD skew:** The guide was written for health systems in low- and middle-income countries, so its vocabulary (user organization, resource team) assumes a public system adopting a program a project piloted. Users in other sectors (education, agriculture, financial inclusion) or scaling through private or market channels should check whether "user organization" maps onto a single institution at all. **Non-WEIRD evidence:** none in the sense of a trial result in the sources this skill draws on; the guide's LMIC health-system origin is a design origin, not a measured outcome.

**Replication status:** Practice guidance, not trial evidence: the dossier records no study testing whether programs scaled with the ExpandNet guide fare better than programs scaled without it, and the dossier's practitioner pointer (BWA's SINTS Scale Up Toolkit) has no URL recorded.

## How to do it

1. **Carry over the assessment.** Write the verdict and the "what must be true" list at the top. Each open test becomes a condition in the action plan with a due date; the plan does not proceed past that date without the result.
2. **Define the innovation package.** Name what is being scaled in one paragraph: the core components and the mechanism each carries (from `specify-intervention-adaptations` or the intervention description), the adaptable parts, the materials, the training, the supervision, and what delivering staff do each week. If a component exists only because the pilot had research staff, say whether it stays and who does it.
3. **Name the user organization.** Who delivers routinely; whether it has asked for this, and in writing; what changes for its staff; who inside it champions the program and who loses from it; what it must be able to do that it cannot do today, and what builds that capacity.
4. **Name the resource team.** Who holds the know-how, what it will provide (training, supervision, data systems, troubleshooting), and the date after which the user organization runs the program without it. A strategy with no exit date is a plan for the pilot organization to keep running the program.
5. **Assess the environment.** The policy that governs the area, the budget cycle and when a line can enter it, supporters and opponents and what each wants, elections or reorganizations ahead, programs competing for the same staff, and any legal or regulatory change needed. If one is needed, see the specialist section before going further.
6. **Make the strategic choices**, each written as a sentence with its reason: vertical scaling, horizontal scaling, or both and in what order; the pace and sequence of sites, gated on the open tests from step 1; how adopters learn about the program; costs per phase and who pays, including after the donor leaves; what is monitored, handing indicator design to `design-fidelity-monitoring`; whether to add or vary components (diversification), where the default is "not until the core package is routine"; and what to do if others copy the program uninvited (spontaneous scaling): support, redirect, or ignore.
7. **Write the action plan**: a table of actions, each with an owner (a role in a named organization), a date, a cost, and the condition from step 1 it depends on. Lines owned by "the team" or "partners" are not owned; rewrite them or drop them.
8. **Write the next steps and the review date** at which the strategy is revisited against monitoring data.
9. **Stop here.** Changes to the intervention go to `specify-intervention-adaptations`; indicators go to `design-fidelity-monitoring`. See `references/evidence-notes.md` for the sources and `references/worked-example.md` for a complete run on an antenatal iron-folate adherence package in Malawi.

## Output template

```markdown
# Scale-up strategy: <program name>

**Scalability assessment carried over:** <verdict>; open conditions: <each "what must be true" item still untested, with its due date>
**Type of scaling:** <vertical / horizontal / both, in this order>, because <reason>

## The innovation package
<what is being scaled, in one paragraph: core components and the mechanism each carries; adaptable parts; materials, training, supervision; what delivering staff do each week; which pilot components are dropped, why, and who now does their job>

## The user organization
- **Who delivers routinely:** <organization, unit, cadre>
- **Has it asked for this:** <yes, by whom, in writing / no>
- **What changes for its staff:** <...>
- **Champions and opponents inside it:** <...>
- **Capacity it must build:** <what, built how, by when>

## The resource team
- **Who:** <...>
- **Provides:** <training, supervision, data, troubleshooting>
- **Exit date:** <the date after which the user organization runs it alone>

## The environment
| Factor | Helps or hinders | What to do about it | Owner |
|---|---|---|---|
| Policy | <...> | <...> | <...> |
| Budget cycle | <...> | <...> | <...> |
| Supporters and opponents | <...> | <...> | <...> |
| Elections, reorganizations, competing programs | <...> | <...> | <...> |
| Legal or regulatory change needed | <none / what> | <...> | <...> |

## Strategic choices
- **Pace and sequence:** <sites or populations in order, with the open condition each wave waits for>
- **Dissemination:** <how adopters learn about the program>
- **Costs and financing:** <cost per phase; who pays; what replaces donor funds and when>
- **Monitoring:** <what is tracked; indicators to design-fidelity-monitoring>
- **Diversification:** <none until routine / what, when>
- **Spontaneous scaling:** <support, redirect, or ignore uninvited copies, and how>

## Action plan
| Action | Owner (role, organization) | Date | Cost | Depends on |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <condition or none> |

## Next steps and review date
<the first three actions, and the date the strategy is revisited against monitoring data>

## What to check before relying on this
- <the assumption about the user organization most likely to be wrong>
- <the open condition from the assessment that could stop the plan>
```

## Where it goes wrong

- **Scaling before assessing.** A strategy written for an effect nobody has judged likely to survive scale is a well-organized way to spend money. If no assessment exists, this skill stops and says so.
- **Scaling the NGO instead of the program.** A plan in which the pilot organization opens more sites with more donor money has no user organization and no exit date. The question the strategy answers is who runs it when the project ends.
- **More sites mistaken for institutionalization.** Horizontal expansion to 40 districts with no budget line, no job description, and no place in the information system is a larger pilot, not a scaled program.
- **A user organization that has not asked.** A strategy that assumes a ministry will adopt because the evidence is good is a wish. If the user organization has not requested the program, the first action is securing that request, not training.
- **Ownerless actions.** "The team will" and "partners will" are not owners. Every line in the action plan names a role in an organization, or it is not in the plan.
- **Changing the intervention inside the strategy.** "We'll shorten the counseling to fit the health worker's day" is an adaptation; it goes through `specify-intervention-adaptations` against the core components, not into a planning table.

## When to bring in a specialist

Tell the user to consult a health-systems or public-policy specialist with scale-up experience, the partner government's own planning and legal staff, and where relevant a public-finance specialist, when:
- The scale-up requires a change in policy, regulation, or law (a cadre allowed to dispense, a guideline rewritten, a procurement rule), because the strategy then depends on a process the team does not control and whose timeline it cannot set
- The government or delivery partner has not asked for the program; building demand for adoption is political work, and a strategy that assumes adoption will mislead the donor
- Financing after the project depends on a line in a national or subnational budget; when that line can enter, and what it displaces, is a public-finance question
- Others are already copying the program uninvited and the copies drop core components; whether to support or distance from them has reputational and safety consequences

Bring them: the scalability assessment, the innovation package with its core components, the environment table, and the draft action plan with its unowned lines marked.
