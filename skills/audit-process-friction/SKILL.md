---
name: audit-process-friction
description: >-
  Use when people say they want to do something (enroll, apply, register,
  collect a kit, redeem a voucher) but few finish, and you suspect the process
  itself is the problem: forms, documents, trips, queues, fees, decisions. Also
  use when a team's fix is "explain it more clearly" and you want to check
  whether the problem is hassle rather than information, or when a service
  loses people between intention and completion with no funnel data to read.
  Walks the process as the user would, logs every step with its time, money,
  documents, and decision, tags each step as necessary, removable, or movable,
  and proposes the smallest removals first (a sludge audit, after Sunstein).
  Do not use when you have observed drop-off numbers for the stages of a
  digital product funnel; use diagnose-funnel-weak-link instead. Not for the
  money and attention strain at the moment of the ask (assess-scarcity-load),
  and not for choosing what to do once the friction is confirmed
  (select-intervention-levers).
license: CC-BY-4.0
metadata:
  title: Count the hassle between intention and completion
  type: atomic
  stage: diagnose
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: mixed-evidence
  tags: "sludge, choice-architecture, com-b"
  consumes: "target-behavior-brief"
  produces: "barrier-diagnosis"
---

## What it does

Lists every step a person must get through between deciding to do something to finishing it, then marks which steps the program can remove.

"Sludge" (Sunstein's term) is friction: the paperwork, waiting, trips, fees, and decisions that cost people time, money, or attention, and that quietly screen out the people a program most wants to reach. A sludge audit is an accounting of that friction, step by step, from the user's side. The output is a confirmed barrier diagnosis (in COM-B terms, Opportunity, physical: the situation does not allow the behavior) with the walk-through as evidence, a ranked list of removals, and an expected effect stated cautiously. It is not a redesign of the service.

## When to use it

### Use it when
- People say they want to enroll, apply, or collect something, completion is low, and nobody has walked the process end to end as a user would
- A team's proposed fix is clearer information or more awareness, and you want to check whether the real problem is hassle rather than knowledge
- A service involves forms, documents, trips to an office, queues, fees, or repeat visits, and someone asks "where are we losing people?"
- A barrier hypothesis under Opportunity (physical) from `decompose-comb-barriers` needs confirming with a step count rather than a survey question

### Do not use it when
- The process is a digital product funnel with observed per-stage drop-off numbers; `diagnose-funnel-weak-link` reads those
- The question is whether the ask lands at a moment of financial or mental strain, not how many steps it has; `assess-scarcity-load`
- The behavior itself is not yet defined as who, what, when; run `define-key-behavior` first
- The friction is already confirmed and the question is what to do about it; `select-intervention-levers`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The behavior as who, what, when (paste the target behavior brief if one exists), and the completion point: what counts as "done".
2. **Required.** The process as the program believes it runs, from the moment a person first could act to completion, with every touchpoint (office, agent, pharmacy, phone, app, paper).
3. **Required.** How the walk-through can be done: can someone go through the process as a user (a field officer, a mystery client, a recent user retracing it), or only reconstruct it from staff accounts and documents? This sets how much weight the time and wait figures carry.
4. Optional. Any counts: how many start, how many finish, and anything per step.
5. Optional. Who controls each step (the program, a partner, a government office, a bank), which decides what the program can remove on its own.

If 1 or 2 is missing, ask and stop. If 3 is missing, assume a desk reconstruction and mark every time and wait cell "estimate, not observed". If 4 is missing, write "no data" in the completion-loss column rather than guessing. If 5 is missing, assume the program controls only the steps it runs itself.

## What it draws on

- Sunstein, C. R. (2020). Sludge audits. *Behavioural Public Policy*. https://doi.org/10.1017/bpp.2019.32
- Sunstein, C. R. (2021). *Sludge: What Stops Us from Getting Things Done and What to Do about It*. MIT Press. https://doi.org/10.7551/mitpress/13859.001.0001
- Bettinger, E. P., Long, B. T., Oreopoulos, P., & Sanbonmatsu, L. (2012). The role of application assistance and information in college decisions: Results from the H&R Block FAFSA experiment. *The Quarterly Journal of Economics*, 127(3), 1205–1242. https://doi.org/10.1093/qje/qjs017
- Behavioural Insights Team (2014; revised and updated edition, c. 2024). *EAST: Four simple ways to apply behavioural insights*. London: BIT. https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf ("Make it easy").
- Duflo, E., Kremer, M., & Robinson, J. (2011). Nudging farmers to use fertilizer: Theory and experimental evidence from Kenya. *American Economic Review*, 101(6), 2350–2390. https://doi.org/10.1257/aer.101.6.2350
- Banerjee, A. V., Duflo, E., Glennerster, R., & Kothari, D. (2010). Improving immunisation coverage in rural India: Clustered randomised controlled evaluation of immunisation campaigns with and without incentives. *BMJ*, 340, c2220. https://doi.org/10.1136/bmj.c2220
- Datta, S., & Mullainathan, S. (2014). Behavioral design: A new approach to development policy. *Review of Income and Wealth*, 60(1), 7–35. https://doi.org/10.1111/roiw.12093
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709
- Gyani, A., Tindall, K., & Gallagher, R. (2022). *Explore Field Guide: A practical tool to map and unpack behaviour*. BIT. https://www.bi.team/wp-content/uploads/2022/11/BIT-Explore-Field-Guide.pdf
- Practitioner sources, unverified, author to confirm: Irrational Labs, *3B Framework* (2025), "barriers include every click, field and decision"; ideas42, Daminger, Hayes, Barrows & Wright (2015), *Poverty Interrupted* ("poverty is a tax... in time, money and cognition").

Sunstein's sludge audit asks an institution to count the friction it imposes on people seeking something they are entitled to, and to justify each piece. The strongest single piece of evidence that friction rather than information is the barrier is the FAFSA experiment: the dossier records that help completing the form raised two-year college completion from 28% to 36%, while information alone had no effect. EAST's "Make it easy" states the same principle as a design rule. Two field experiments from low- and middle-income countries show how small the hassle can be: in Western Kenya, a time-limited free-delivery offer made just after harvest raised fertilizer use by 14 points on a base of 24% in one season and 18 points on 26% in the next (Duflo, Kremer & Robinson; Datta & Mullainathan read this as removing a small hassle cost of travel, though the offer combined timing with delivery, so it is not evidence about hassle alone); in rural Rajasthan, reliable monthly immunization camps on their own raised full immunization from 6% to 18% (Banerjee et al.). This skill adds three judgment calls: the three-way tag (necessary, removable, movable); the rule that removals the program controls come before removals that need another institution, and both come before assistance, and assistance before information; and a mandatory discount on any expected effect, after DellaVigna & Linos (academic nudge trials average 8.7 percentage points, nudge-unit trials 1.4). See `references/evidence-notes.md`.

**WEIRD skew:** the sludge framing and the FAFSA experiment are United States evidence, and "Make it easy" comes from United Kingdom government trials; the evidence from elsewhere is about specific hassles removed in specific programs, not about sludge audits as a method. **Non-WEIRD evidence:** Kenya (Duflo, Kremer & Robinson 2011, 1,230 maize farmers: fertilizer use up 14 points on a 24% base, then 18 on 26%) and India (Banerjee et al. 2010, rural Rajasthan: full immunization from 6% to 18% with reliable camps alone). No dedicated LMIC sludge-audit trial was found in the dossier; a Kenya snippet about accounts opened at the place of business (2% still in use after two months) is unverified, author to confirm. A user elsewhere should check which steps are required by local law or a partner's rules before calling them removable.

**Replication status:** mixed. Assisted completion is replicated in the United States and the general principle is widely supported, but the transfer claim rests on single field experiments, and the DellaVigna & Linos gap (about 70% explained by selective publication with low power) says published effects should be discounted before they are used as a forecast.

## How to do it

1. **Fix the start and the end.** The start is the moment the person first could act (receiving the message, hearing of the service), not the office door; the end is the completion point from the brief. An audit that starts at the counter misses the trip to it.
2. **Walk the process as the user would**, in the user's conditions (their phone, their documents, their hours, their language), if access allows. Otherwise reconstruct it from staff, documents, and people who recently finished or gave up, and say which in the output.
3. **Log every step** in the step log: what the person does, where, how long it takes including waiting, what it costs (fees, transport, lost earnings), which documents it needs, what decision it demands (choose an option, calculate an amount, supply a fact they may not know), and who controls it. Count a trip, a queue, and a return visit as steps; they are the ones official flow charts leave out.
4. **Tag each step** necessary (required by law, safety, consent, or the program's core purpose), removable (serves the institution's convenience, duplicates another step, or exists by habit), or movable (could be done by staff instead, pre-filled, batched, or done at a different time or place). Write the reason next to every tag; "necessary" with no reason is the default to challenge.
5. **Estimate completion loss per step where data exist**: counts in and out, or users' reports of where they gave up. Where no data exist, write "no data". Do not invent a drop-off to make the table look complete.
6. **Rank the removals, smallest first.** Steps the program controls and could delete this month come before steps that need another institution; deletions and pre-filling before assistance; assistance before information. The FAFSA result is the reason: information alone did nothing, help did.
7. **State the expected effect cautiously.** Name which removal targets which loss, cite the nearest evidence, apply the DellaVigna & Linos discount, and say what an information-only fix would not do. Never promise a number the counts cannot support.
8. **Write the barrier diagnosis** for `select-intervention-levers`: the confirmed friction, in COM-B terms (Opportunity, physical), with the walk-through evidence and the removable list attached.
9. **Stop here;** choosing the lever and redesigning the process is `select-intervention-levers`' job, and measuring completion after a change belongs to `plan-evaluation-design`.

See `references/worked-example.md` for a complete run on HIV self-test kit collection in Lagos.

## Output template

```markdown
# Process friction audit

**Behavior:** <who, what, when, carried over verbatim>
**Process:** <from the moment the person first could act to the completion point>
**How this was audited:** <walked as a user by whom / observed / reconstructed from staff and documents>

## Step log
| # | Step | Where | Time incl. waiting | Money | Documents | Decision demanded | Who controls | Tag | Why this tag | Completion loss |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | <...> | <...> | <observed or "estimate"> | <...> | <...> | <...> | <...> | necessary / removable / movable | <reason> | <n in, n out, or "no data"> |

**Totals for one person:** <trips>, <hours>, <money>, <documents>, <decisions>

## Removable list, smallest first
1. <step>: <delete / pre-fill / move to staff / batch>; controlled by <who>; targets <which loss>; evidence: <nearest source>
2. <...>

## Steps kept, and why
- <step>: <the law, safety, consent, or purpose reason>

## Expected effect, stated cautiously
<which removal targets which loss; the nearest evidence; the discount applied; what an information-only fix would not do>

## Barrier diagnosis (input to select-intervention-levers)
- Opportunity, physical: <the confirmed friction, with the walk-through evidence>

## What to check before relying on this
- <the step whose time or loss is an estimate, not an observation>
- <who else must agree before a step can go>
```

## Where it goes wrong

- **Auditing the process as staff describe it.** The official flow omits the second trip, the photocopy shop, the ID the person does not have, the queue. Walk it, or reconstruct it from users who gave up, and say which you did.
- **"Necessary" by default.** Every step has a reason someone once gave. A step is necessary only when the reason written next to it is law, safety, consent, or the program's core purpose; anything else is removable or movable until shown otherwise.
- **Inventing the drop-off.** A completion-loss column filled with plausible numbers is worse than one that says "no data", because it will be read as a measurement.
- **Proposing a clearer leaflet.** Information alone did not move FAFSA completion. If the removable list leads with a better message, the ranking rule has not been applied.
- **Removing a step that protected someone.** Consent reading, eligibility checks, and identity verification can look like sludge and be the thing that protects the user or the program. The "steps kept" section must say what each protects.
- **Quoting the published effect as the forecast.** An 8-point gain in a United States experiment is not the expected gain in this program; the expected-effect section applies the discount and names the nearest local evidence.

## When to bring in a specialist

Tell the user to consult a legal or compliance officer, a safeguarding lead, or an evaluator when:
- A removable step is part of a government or regulated process (identity, consent, eligibility verification, financial know-your-customer rules); a legal or compliance person must confirm it can go before it is proposed to the owner
- The process involves health or financial consent, and a step tagged removable is the consent itself; a safeguarding or ethics lead must review the tag
- The team wants a completion-gain number for a proposal or a funder; that is an evaluator's forecast or a measured result from `plan-evaluation-design`, not an extrapolation from this audit

Bring them: the step log with tags and reasons, the removable list, and whatever counts exist.
