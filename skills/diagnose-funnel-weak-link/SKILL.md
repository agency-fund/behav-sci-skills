---
name: diagnose-funnel-weak-link
description: >-
  Use when a product's funnel numbers show where users drop out and the team
  is about to redesign that step without first knowing why, or when the team
  can say where users leave but answers why differently depending on who is
  asked. Also use when an engagement experiment is being planned and needs a
  hypothesis worth the sample. Picks the stage furthest below its target and
  sets out two to four competing mechanism hypotheses, each with the
  measurement or experiment that would confirm or rule it out. Needs real
  observed numbers. Do not use without a funnel metric readout; a funnel with
  only targets has no weak link yet, so build and instrument it first with
  build-user-funnel. Not for behaviors outside a product journey (clinic
  attendance, cash savings deposits); that diagnosis belongs to
  decompose-comb-barriers.
license: CC-BY-4.0
metadata:
  title: Find out why users drop out of your product
  type: atomic
  stage: diagnose
  version: "0.1.0"
  status: draft
  authors: "Joe Speed"
  org: IL
  weird: likely-generalizes
  tags: "ai-eval, funnel, com-b"
  consumes: "user-funnel-map, funnel-metric-readout"
  produces: "funnel-weak-link-hypotheses"
---

## What it does

Finds the step in a product's user journey that falls furthest below its target, then sets out competing explanations for why users drop out there.

Each explanation is a mechanism stated so it can be wrong, tagged by where it locates the failure (capability, opportunity, or motivation), and paired with the measurement or experiment that would tell it apart from the others. The output is a differential diagnosis, not a redesign.

## When to use it

### Use it when
- A funnel readout shows a stage far below target and the next team meeting's agenda is a redesign, a new feature, or "more onboarding messages": a fix chosen before any mechanism was named
- The team can say *where* users leave (the numbers say so) but answers *why* differently depending on who is asked
- An engagement experiment is being planned and needs a hypothesis worth the sample; this skill's output is `design-evidential-experiment`'s natural input
- Someone asks "why are users dropping off at this step?" or "what's our weakest link?"

### Do not use it when
- There are no observed numbers. A funnel with only targets has no weak link yet; run the product and collect a funnel metric readout, or build the funnel first with `build-user-funnel`
- The behavior sits outside a product journey (clinic attendance, savings deposits in cash); that diagnosis belongs to `decompose-comb-barriers`, since this skill's stage-transition framing assumes telemetry-visible steps
- The team already has a surviving hypothesis and wants the fix; design the test with `design-evidential-experiment` or the intervention with `select-intervention-levers`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The user funnel map, normally `build-user-funnel`'s output, or at least the stage names, entry actions, and targets. Stage names and targets are what make a drop-off identifiable at all.
2. **Required.** The funnel metric readout: the observed value or transition rate per stage over a stated time window, plus known data-quality caveats (instrumentation gaps, a definition change mid-window). The diagnosis targets the largest target-versus-observed gap, not the stage the team already wants to redesign.
3. Optional. What the team already suspects or wants to fix, so the "pet stage" check can be applied explicitly rather than silently.
4. Optional. Which cheap tests are feasible: log access, the ability to call a handful of users, A/B capability.

If 1 or 2 is missing, ask and stop; there is nothing to diagnose without both. If 3 is missing, assume no prior preference. If 4 is missing, assume log analysis and a handful of user calls are feasible and say so.

## What it draws on

- Wu, Z., On, R., Walsh, J., Korley, E., Madon, T., & Wong, L. (2025). AI Evaluation in the Social Sector: A Living Playbook. Repeatable Motions. The Agency Fund. https://eval.playbook.org.ai/motions
- Michie, S., van Stralen, M. M., & West, R. (2011). The behaviour change wheel: A new method for characterising and designing behaviour change interventions. *Implementation Science*, 6, 42. https://doi.org/10.1186/1748-5908-6-42

Repeatable Motion 03 of The Agency Fund's AI Evaluation Playbook (Wu et al., 2025): use funnel drop-off data to generate "specific, testable hypotheses" about mechanism. The playbook's own examples are "Is the value proposition unclear? Are users overwhelmed? Do they mistrust the AI?", each becoming "a lens for a focused measurement or experiment." The motion sits, in the playbook's words, at the intersection of product management and behavioral science, and its discipline is the one a clinician applies: no treatment before a differential diagnosis, and a differential means more than one candidate mechanism held open at once.

COM-B (Michie et al., 2011) supplies the completeness check on the hypothesis space, a judgment call the playbook itself does not specify. Each candidate mechanism is tagged by whether it locates the failure in **capability** (the user can't: literacy, language, digital skill), **opportunity** (the context won't let them: cost, connectivity, device access, social permission), or **motivation** (they don't want to: unclear value, mistrust, effort not worth it). The tags exist to expose lopsidedness. A hypothesis list that is all motivation is usually a team projecting its own product anxieties, and the template requires at least one opportunity-side (structural, non-psychological) hypothesis for this reason.

Second judgment call: this skill diagnoses the largest unexplained gap, not the stage the team is most excited to fix. If the readout's data-quality caveats can explain the gap (an instrumentation change mid-window), the honest output says so and diagnoses the next-largest real gap instead.

**WEIRD skew:** The diagnostic move (competing mechanism hypotheses with discriminating tests, instead of a redesign reflex) is method, not culture, and the source playbook's cases are low- and middle-income-country deployments. The hypothesis space is where WEIRD defaults creep in: explanations drawn from app-market intuitions (notification fatigue, UX friction) crowd out explanations that dominate in other contexts, such as airtime and data cost, shared handsets, channel trust, and literacy or language mismatch. The output template's requirement that at least one hypothesis be non-psychological exists for this reason.

**Replication status:** Not applicable in the effect sense: differential diagnosis is a method, not an intervention. Using COM-B as a completeness check on funnel hypotheses is this skill's author's judgment call rather than something the playbook specifies, and whether it improves the hypotheses teams generate has not, to the authors' knowledge, been tested.

## How to do it

1. **Find the largest target-versus-observed gap** in the readout. Check the data-quality caveats first: if an instrumentation change or definition change explains a gap, set that gap aside, say so, and diagnose the next-largest real gap. Record every gap set aside and why, including downstream gaps that wait on the upstream break.
2. **Write two to four competing mechanism hypotheses** for that transition, each stated so it can be wrong. One hypothesis is not a differential; five means nothing gets tested.
3. **Tag each hypothesis with its COM-B locus**: capability, opportunity, or motivation.
4. **Check the list for lopsidedness.** At least one hypothesis must locate the failure outside users' heads (cost, access, device, timing) before any motivational story is accepted.
5. **For each hypothesis, name what would discriminate it** from the others (the observation that separates it from H2 and H3) and **the cheapest honest test** (a measurement or experiment with the discriminating signal named).
6. **Check for tautologies.** "Users drop off because they don't engage" restates the metric. Does the mechanism column say something the metric did not already say?
7. **Close with what this diagnosis is not**: no redesign is proposed; fixes come after a hypothesis survives its test, via `design-evidential-experiment` for an experiment or `select-intervention-levers` for intervention design.

See `references/worked-example.md` for a complete run on MaizeMate's six-week pilot readout.

## Output template

```markdown
# Funnel weak-link hypotheses

**Funnel:** <product + funnel name>
**Readout window:** <dates the numbers cover>
**Weakest link:** <stage N to N+1: observed X% vs target Y%>
**Gaps set aside:** <other below-target transitions and why they wait, including any gap plausibly explained by a data-quality caveat rather than by users>

## Competing hypotheses
| # | Mechanism (why users fall out here) | COM-B locus | What would discriminate it | Cheapest honest test |
|---|---|---|---|---|
| H1 | <one mechanism, stated so it can be wrong> | capability / opportunity / motivation | <the observation that separates this from H2/H3> | <measurement or experiment, with the discriminating signal named> |
| H2 | <...> | <...> | <...> | <...> |

<at least one hypothesis must locate the failure outside users' heads (cost, access, device, timing) before any motivational story is accepted>

## What this diagnosis is not
One sentence: no redesign is proposed here; fixes come after a hypothesis survives its test, via the experiment path (design-evidential-experiment) or intervention design (select-intervention-levers) as appropriate.
```

## Where it goes wrong

- **The single-hypothesis diagnosis.** One mechanism, stated confidently, with a test designed to confirm it. The differential is the method; if only one story was ever on the table, this skill ran as decoration for a decision already made.
- **All-motivation hypothesis lists.** Every mechanism about desire and trust, none about cost, access, or capability: the classic WEIRD default, and why the template forces one structural hypothesis. The wrong locus means the winning "fix" gets A/B-tested against a barrier no message can move.
- **Diagnosing the pet stage.** The team wants to rebuild onboarding, so onboarding gets diagnosed while the numbers say the break is elsewhere. The weakest-link line must cite the readout's largest target-versus-observed gap or explicitly justify departing from it.
- **Mechanism-shaped restatements.** "Users drop off because they don't engage" is a tautology wearing a hypothesis costume. The test: does the mechanism column say something the metric did not already say?
- **Ignoring the readout's caveats.** Diagnosing a gap manufactured by an instrumentation change. The gaps-set-aside line exists to force this check before users get theorized about.
- **Out of scope: no numbers, or no journey.** Without a readout there is no weak link to find (build and instrument the funnel first); without a product journey the stage framing itself is wrong, so use `decompose-comb-barriers`.

## When to bring in a specialist

Tell the user to bring in a qualitative or user researcher, a data engineer, or a safeguarding or clinical reviewer when:
- A hypothesis implicates harm or distress (users leaving because the product gave unsafe advice, or because vulnerable users felt exposed or dismissed); the "cheapest honest test" must not be a cold A/B test on those users, and the hypothesis needs ethical review before any test runs
- The readout's data quality is itself in doubt (identity assumptions broken by shared handsets, a definition change mid-window, logging gaps); a data engineer should re-establish the numbers before anyone theorizes about users
- Two or more hypotheses survive their cheapest tests; the next discriminating study needs a qualitative researcher who can talk to the users who left, not another cut of the logs

Bring them: the user funnel map, the readout with its caveats, and the hypothesis table.
