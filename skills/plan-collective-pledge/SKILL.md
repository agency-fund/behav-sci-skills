---
name: plan-collective-pledge
description: >-
  Use when a community needs to give up a practice together because each
  household keeps it only because it expects the others to (open defecation,
  dumping in the river) and the team wants to plan the public event at which
  people commit in front of each other. Also use when someone
  proposes a "declaration day", "pledge ceremony", or "triggering" session and
  needs the first movers, the visibility of each commitment, the coverage
  threshold at which effects appear, and the follow-up planned, not
  improvised. Produces an event plan built on Bicchieri's account of norm
  abandonment and the CLTS sanitation trials in India, Indonesia, Mali, and
  Tanzania. Do not use when a message correcting what people believe others
  do is enough; use write-social-norm-message instead. Not for deciding
  whether a norm exists (diagnose-social-norm), not for mapping who watches
  whom (map-reference-network), not for tokens that reward individual
  completion (design-social-recognition), and not for generic drafting
  (draft-lever-content).
license: CC-BY-4.0
metadata:
  title: Plan a public pledge so a community changes together
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "social-norms, community-led, implementation"
  consumes: "social-norm-diagnosis"
  produces: "intervention-draft"
---

## What it does

Plans a public, coordinated commitment event through which a community abandons a practice together rather than one household at a time.

A social norm holds when each person believes that most others in their reference group do the practice (an empirical expectation), believes that those others think they should (a normative expectation), and prefers to conform only because of those two beliefs. A private change alters neither belief, so the practice persists even when most people privately dislike it. A public, simultaneous commitment changes both at once: each person sees the others commit and hears the group endorse the change. This skill designs that event, the people who go first, the coverage threshold below which nothing happens, and what keeps the new expectation visible afterward. It does not decide whether the practice is a norm; `diagnose-social-norm` does.

## When to use it

### Use it when
- A social norm diagnosis says the practice is held by empirical and normative expectations in a known reference group, and most people would abandon it if they believed the others would
- Someone proposes a "declaration", "pledge ceremony", "triggering" meeting, or "open-defecation-free day" and needs it designed rather than improvised
- A previous norm message or individual counseling moved almost no one, and the field team's explanation is "nobody wants to be first"
- The alternative behavior is within most households' reach (the latrine can be built, the fee can be paid), so a pledge would not demand the impossible

### Do not use it when
- The belief that holds the practice is simply mistaken (people think few vaccinate when most do) and a corrective message would fix it; `write-social-norm-message` is cheaper and carries less exposure risk
- The practice has not been diagnosed as a norm; a custom (people do it because it works for them) or a cost barrier needs `diagnose-social-norm` first, then `select-intervention-levers`
- The team does not know who watches whom and whose approval matters; `map-reference-network` comes first, because the event is built around that network
- The goal is to recognize individual households that already changed with a visible token; that is `design-social-recognition`, which can follow this skill but does not replace it

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The social norm diagnosis from `diagnose-social-norm`: the practice, the reference group, the evidence that empirical and normative expectations hold it in place, and the share who privately favor change. If the diagnosis says custom or preference, say so and stop; a pledge changes expectations, not costs or tastes.
2. **Required.** The reference network from `map-reference-network`: who people watch, whose approval matters, and who the plausible first movers are. If missing, ask once; if still missing, proceed with the whole community treated as one reference group, flagged as an assumption that weakens every later step.
3. **Required.** What the alternative behavior costs in practice (a latrine, a different sales channel, a fee) and whether most households can meet it within the pledge period. A pledge to do what people cannot do produces visible, public failure.
4. **Required.** Whether the practice is a harmful traditional practice, a religious obligation, or one where dissenters face violence or exclusion (child marriage, female genital cutting, caste-linked practices). If yes, go to the specialist section first and produce only the parts marked safe there.
5. Optional. Who would convene (local government, a traditional or religious leader, an NGO), what follow-up channels exist (meetings, signs, radio, household markers), and the planned date.

If 1 is missing, ask and stop. If 2 is missing, ask once, then proceed with the flagged assumption. If 3 is missing, ask once; if still missing, mark the threshold section "coverage unreachable until cost is known". If 4 is unanswered, treat the practice as sensitive until told otherwise. If 5 is missing, assume an NGO convener and no follow-up channel, and say so.

## What it draws on

- Bicchieri, C. (2016). *Norms in the Wild: How to Diagnose, Measure, and Change Social Norms*. Oxford University Press, chapters 4 and 5. https://doi.org/10.1093/acprof:oso/9780190622046.001.0001
- Bicchieri, C., & Mercier, H. (2014). Norms and beliefs: How change occurs. In *The Complexity of Social Norms*. Springer. https://doi.org/10.1007/978-3-319-05308-0_3
- Pickering, A. J., Djebbari, H., Lopez, C., Coulibaly, M., & Alzua, M. L. (2015). Effect of a community-led sanitation intervention on child diarrhoea and child growth in rural Mali: A cluster-randomised controlled trial. *The Lancet Global Health*, 3(11), e701–e711. https://doi.org/10.1016/S2214-109X(15)00144-8
- Cameron, L., Gertler, P., Shah, M., Alzua, M. L., Martinez, S., & Patil, S. (2022). The dirty business of eliminating open defecation: The effect of village sanitation on child height from field experiments in four countries. *Journal of Development Economics*, 159, 102990. https://doi.org/10.1016/j.jdeveco.2022.102990
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709
- Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity: A meta-analysis and a real-effort experiment. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x
- UNICEF Innocenti / Penn Social Norms Group (2016). *Why Do People Do What They Do? A Social Norms Manual*. Unverified, author to confirm; no copy could be fetched.

Bicchieri (2016, chapters 4 and 5) sets out how a norm is abandoned: the change must be public, so that each person's empirical expectation about the others is revised at the same time; it must be coordinated, so that no one is left exposed as the only deviant; and it needs trendsetters, people who care less about disapproval and whom others watch, to go first. Bicchieri and Mercier (2014) make the same argument about beliefs changing before behavior. The sanitation trials are the field test. Community-Led Total Sanitation (CLTS) walks a village through the consequences of open defecation and ends in a collective declaration to stop; Cameron et al. (2022) pool cluster-randomized trials in India, Indonesia, Mali, and Tanzania and find private sanitation coverage rose 7 to 39 percentage points, with child height gaining about 0.3 SD once village coverage passed 50 to 75%. Pickering et al. (2015), the Mali trial, found an effect on stunting but no change in diarrhea. See `references/evidence-notes.md` for the annotated list.

Judgment calls this skill adds: the rule that a pledge event is postponed rather than held when the expected count falls short of the threshold, the requirement that the alternative behavior be affordable before anyone is asked to pledge, and the ethics check on shaming written into the plan rather than left to the facilitator.

**WEIRD skew:** None in the usual direction: the trial evidence is entirely from low- and middle-income settings, and the theory was built on practices such as open defecation. What a user should still check locally is whether the village (or hamlet, clan, or market) is the reference group that matters, whether a public declaration is a recognized form of commitment there, and who can legitimately convene one. **Non-WEIRD evidence:** India, Indonesia, Mali, and Tanzania (Cameron et al. 2022), cluster-randomized CLTS trials, coverage +7 to 39 points, child height about +0.3 SD above 50 to 75% coverage; Mali (Pickering et al. 2015), stunting reduced, diarrhea unchanged (secondary source for that summary, per the dossier).

**Replication status:** Replicated for coverage across four countries, mixed for health outcomes (growth yes, diarrhea no, and only where coverage crossed the threshold). No meta-analysis of pledge events as such is among this skill's sources. Discount for a program with less facilitation than the trials: the academic-versus-unit gap (8.7 against 1.4 percentage points; DellaVigna & Linos 2022) and the lab-to-field shrinkage in loss framing (0.33 to 0.02 SD; Ferraro & Tracy 2022) both say to plan for the bottom of the coverage range, and for no health effect at all unless coverage passes the threshold.

## How to do it

1. **Confirm the diagnosis says norm.** Write the empirical expectation and the normative expectation each in one line, with the evidence, and name the reference group. If the diagnosis says custom or preference, stop and say which skill applies instead.
2. **Identify first movers and trendsetters** from the reference network: people whose change others will notice and whose approval matters, who are least afraid of disapproval, and who can actually comply. Formal leaders are not automatically trendsetters. Check each one's willingness and ability before the event; a first mover who later fails publicly resets the norm.
3. **Design the declaration so each person sees the others commit.** Simultaneous, in one place, witnessed by the reference group, with each commitment visible (a count, a signature, a stand) and the alternative behavior stated concretely. The point of the format is to revise every empirical expectation at once; a pledge signed privately at home does not do that.
4. **Set the threshold logic.** State the share of the reference group that must commit and then comply for the expectation to flip, and the date by which the alternative behavior is feasible for that share. The health effects in the CLTS trials appeared only once coverage passed 50 to 75%. Write down what happens if the expected count falls short: postpone, do not hold a partial pledge.
5. **Plan the follow-up visibility.** State how compliance stays visible to the group after the event (household markers, counts read at meetings, a public tally), because the new expectation decays if no one can see the others keeping their word.
6. **Run the ethics check on shaming and exposure.** No naming of non-compliers, no public humiliation, a way for dissenters to abstain without being singled out, and no sanctions beyond those the community already uses legitimately. A concern raised in practice is that some CLTS facilitation relies on shame or disgust (unverified, author to confirm; no specific study is cited). Route the open questions to `audit-intervention-ethics`.
7. **Specify the measurement:** the pledge count against the threshold, compliance at 3, 6, and 12 months by reference group, and whether the threshold was crossed, which decides whether any health outcome is worth measuring.
8. **Stop here.** `audit-intervention-ethics` reviews the plan; `plan-evaluation-design` sets up the cluster comparison; `design-social-recognition` can add visible tokens for households that comply, after the event.

See `references/worked-example.md` for a complete run on open defecation in a Central Java hamlet.

## Output template

```markdown
# Collective pledge event plan

**Practice to abandon:** <the practice, carried over verbatim>
**Alternative behavior:** <who + what + when, and what it costs a household>
**Reference group:** <from the diagnosis and the network map>
**Norm diagnosis:** empirical expectation: <...>; normative expectation: <...>; evidence: <...>

## First movers and trendsetters
| Person or role | Why others watch them | Willing | Able to comply by the event |
|---|---|---|---|
| <...> | <...> | <yes / no / unknown> | <yes / no / unknown> |

## The declaration
- Format: <where, when, how long, who convenes>
- What each person sees: <how commitments are made visible to the whole group>
- What is said: <the commitment in the community's words, naming the alternative behavior>
- Who may abstain, and how: <...>

## Threshold logic
- Share needed: <the share of the reference group, and why that share>
- Expected count at the event: <...>
- If short: <postpone rule>

## Follow-up visibility
- <channel, frequency, who maintains it>

## Ethics check
- Shaming or exposure risk: <...>
- Dissenters: <...>
- Open items for audit-intervention-ethics: <...>

## Measurement
- <pledge count; compliance at 3, 6, 12 months by reference group; threshold crossing>

## Open questions
- <what needs field confirmation before a date is set>
```

## Where it goes wrong

- **Pledging what people cannot afford.** A declaration to build latrines by households that cannot pay for one produces public failure, and a public failure teaches everyone that the norm held after all. The affordability line in the threshold section is mandatory.
- **Treating a custom as a norm.** If households keep the practice because it works for them, not because of what others expect, the event changes nothing; the diagnosis has to say "norm" with evidence before this skill runs.
- **A private pledge in public clothing.** Individual sign-ups, door-to-door promises, or an SMS pledge revise nobody's expectation about anybody else. If each person cannot see the others commit, the mechanism is absent.
- **Stopping at the event.** A declaration with no follow-up visibility decays; the trials that showed effects had coverage that people could see. The plan is incomplete without the visibility section filled in.
- **Counting a partial pledge as success.** Below the threshold, coverage may rise a little and health will not move; the trials' growth effects appeared only once 50 to 75% of a village had changed. Report the pledge count against the threshold, not alone.
- **Shame as the engine.** A facilitator can produce a fast declaration by humiliating the households that still practice; the skill must refuse to design that, name it in the ethics check, and send it to `audit-intervention-ethics`.

## When to bring in a specialist

Tell the user to consult a specialist in harmful-practice programming, the program's child protection or safeguarding lead, and a local researcher who knows the community, before any planning, when:
- The practice is a harmful traditional practice or carries religious or caste weight (child marriage, female genital cutting, dowry, widow rites); a public pledge event can expose dissenting families and girls, and the specialist decides whether an event is appropriate at all. The skill produces only the diagnosis confirmation and the threshold logic, and withholds the declaration design
- Dissenters would face violence, exclusion, or loss of livelihood; the abstention route needs designing by someone who knows the local sanctions
- The convener holds enforcement power (a government that can fine or evict); the line between a pledge and coercion needs a legal or ethics review
- The team plans to claim a health outcome; an epidemiologist should confirm the threshold and the outcome measure before the event is sold on that promise

Bring them: the norm diagnosis, the reference network map, the draft plan with the ethics check filled in, and what is known about how the community sanctions deviance today.
