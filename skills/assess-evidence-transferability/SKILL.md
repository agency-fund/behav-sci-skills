---
name: assess-evidence-transferability
description: >-
  Use when a team has one published finding in hand and asks "will this work
  here?", "does this study apply to our population?", "can we assume the effect
  from that paper?", or "they got 40 points in Afghanistan; what should we
  expect in Bangladesh?". Also use when a proposal quotes a study's effect as
  the expected effect of a program in a different country, population, or
  channel, or when an evidence scan brief flags a finding as WEIRD-skewed and
  someone must decide whether to rely on it. Compares the study's units,
  treatment, outcome, setting, and implementer with the user's and returns a
  transfer verdict, the assumptions to test locally, and a discounted expected
  effect (Szaszi et al. 2025; Henrich et al. 2010; DellaVigna and Linos 2022).
  Do not use to find what evidence exists; that is assess-evidence-base. Not
  for the planning number in a power calculation (estimate-expected-effect),
  and not for a general review of the population's culture or psychology; this
  skill judges one study's fit.
license: CC-BY-4.0
metadata:
  title: Check whether a published finding transfers to your setting
  type: atomic
  stage: define
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "evidence-synthesis, heterogeneity, choice-architecture"
  consumes: "evidence-scan-brief"
  produces: ""
---

## What it does

Judges whether one published finding is likely to hold for the user's population, by comparing the study with the user's case on five dimensions: units, treatment, outcome, setting, implementer.

A published effect was measured on particular people, with a particular version of the intervention, by a particular team, and effects shrink when moved: academic journal studies average several times the effect that the same kinds of interventions produce when government units run them (DellaVigna and Linos). This skill is a lens on one study at a time. It does not search for evidence, and it does not review the culture of the target population; it asks, dimension by dimension, where the user's case differs from the study's, which differences touch the mechanism the effect depends on, and what the effect should be discounted to while those differences are untested.

## When to use it

### Use it when
- Someone asks "will this work here?", "does this paper apply to us?", or "can we use this study's number?"
- A proposal, deck, or theory of change quotes a single study's effect as the program's expected effect in a different country, population, or delivery channel
- `assess-evidence-base` returned a WEIRD-skew flag on a finding and the team must decide whether to rely on it anyway
- The team wants to adopt an intervention from another organization's trial and cannot say which of that trial's conditions it shares
- A funder asks "what is the evidence this transfers?" about one cited study

### Do not use it when
- Nobody has a specific study yet; `assess-evidence-base` finds what exists, then bring one finding here
- The question is what effect size to put in a power calculation; `estimate-expected-effect` turns this skill's discount into a planning number
- The question is how the target population's culture shapes its psychology in general (values, self-construal, norms); that is a separate lens, not a fit check on one study, and this skill does not do cultural theory
- The finding is the team's own prior pilot in the same population; `review-prior-intervention`
- The team needs the chain the finding would sit in; `draft-theory-of-change`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The one finding: citation; population (who, where, how many); the treatment as delivered; the outcome measured; who delivered it; the reported effect with its unit; and, if the paper states one, the mechanism the authors claim. Paste the evidence scan brief entry if the finding came from one. If the user has several findings, ask which one, or run once per finding.
2. **Required.** The user's case on the same dimensions: population; the version of the intervention they would deliver; the outcome they care about; the setting (institutions, infrastructure, literacy, channel); and who would implement.
3. **Required.** The decision the verdict informs: a pilot, a scale-up, a proposal number, a go or no-go. The stakes set how conservative the discount should be.
4. Optional. Any replications or tests of the same intervention in settings nearer the user's, from the evidence scan brief or the team's own knowledge, with citations.
5. Optional. What the team could test cheaply before committing: a survey, a small A/B test, interviews.

If 1, 2, or 3 is missing, ask and stop. If 4 is missing, proceed, state that no near-setting replication was supplied, and treat the finding as single-setting. If 5 is missing, assume a short survey and a round of interviews are feasible.

## What it draws on

- Szaszi, B., et al. (2025). Generalizability of choice architecture interventions. *Nature Reviews Psychology*. https://doi.org/10.1038/s44159-025-00471-9 (first author, year, and title verified; the co-author list is unverified, author to confirm)
- Henrich, J., Heine, S. J., & Norenzayan, A. (2010). The weirdest people in the world? *Behavioral and Brain Sciences*, 33, 61. https://doi.org/10.1017/S0140525X0999152X
- Bryan, C. J., Tipton, E., & Yeager, D. S. (2021). Behavioural science is unlikely to change the world without a heterogeneity revolution. *Nature Human Behaviour*, 5(8), 980–989. https://doi.org/10.1038/s41562-021-01143-3
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709
- Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity: A meta-analysis and a real-effort experiment. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x
- Blumenstock, J., Callen, M., & Ghani, T. (2018). Why do defaults affect behavior? Experimental evidence from Afghanistan. *American Economic Review*, 108(10), 2868–2901. https://doi.org/10.1257/aer.20171676
- Gauri, V., et al. (2018). eMBeDding for impact and scale in developing contexts. *Behavioural Public Policy*, 2(2), 256–262. https://doi.org/10.1017/bpp.2018.11
- Singh, A. (2023). *Before You Wreck Yourself: A Guide to Facing the Hard Truth That We Are All One Level Removed*. Busara and MIT GOV/LAB. https://mitgovlab.org/resources/before-you-wreck-yourself/

Henrich, Heine and Norenzayan showed that most behavioral findings come from Western, Educated, Industrialized, Rich, Democratic (WEIRD) samples that are unusual on many measures, so a study's population is a condition of its result, not a detail. Bryan, Tipton and Yeager argue that effects should be expected to vary across people and settings, and that haphazard convenience samples cannot say how. Szaszi et al. (2025) review what is known about when choice architecture generalizes. DellaVigna and Linos give the size of the problem: across 126 RCTs and 23 million people, academic journal studies averaged 8.7 percentage points (+33.4%) while nudge-unit trials averaged 1.4 points (+8.0%), with about 70% of the gap explained by selective publication combined with low power; Ferraro and Tracy's 0.33 SD in the lab versus 0.02 SD in the field for loss-framed contracts points the same way. Blumenstock, Callen and Ghani are the worked contrast: among 949 employees of one Afghan mobile-money firm, a 5% default contribution against a 0% default raised participation by 40 points, equivalent to a 50% employer match, through present bias and the cognitive cost of deciding rather than endorsement or inattention. A default moved to a setting where that mechanism is absent should not be expected to carry the number. The judgment calls this skill adds, none of them published criteria: a five-dimension fit table (units, treatment, outcome, setting, implementer); the rule that only differences touching the claimed mechanism change the verdict; and a discount that starts from the published-to-field gap and widens for each untested mechanism-relevant difference.

**WEIRD skew:** The lens exists to detect WEIRD skew, and its own sources are mixed: Henrich et al. and Bryan et al. are arguments made from WEIRD-dominated literatures; DellaVigna and Linos cover US government units only; Blumenstock et al. is a field experiment in a low-income country. Attribute the WEIRD argument to Henrich et al., not to Bryan et al., whose text does not discuss WEIRD samples explicitly. A user anywhere should check locally whether the study's claimed mechanism is present in their population before trusting any part of the effect. **Non-WEIRD evidence:** Afghanistan (Blumenstock et al. 2018; 949 employees of one firm; a 5% default raised savings participation by 40 points), and the eMBeD essay's statement that proven nudges are not always effective in developing countries. A claim that about 1% of published psychology papers have African principal investigators or samples appears on a National Academies slide and is unverified, author to confirm.

**Replication status:** Conceptual: the lens is a procedure, not an effect, so there is nothing to replicate. The shrinkage it relies on is replicated across two independent comparisons (DellaVigna and Linos; Ferraro and Tracy). The Afghanistan default result is a single-firm study.

## How to do it

1. **Write the finding in one row**: population, treatment as delivered, outcome, implementer, effect with unit, claimed mechanism. If the mechanism is not stated, write "not stated" and treat every dimension as potentially mechanism-relevant, because there is no way to say which differences are safe.
2. **Write the user's case** on the same five dimensions underneath, from the answers to question 2.
3. **For each dimension, name the difference** and judge whether it touches the mechanism: does the reason the effect occurred depend on this feature? Mark each row "yes", "no", or "unknown", with the reason. (In the Afghanistan study the default worked through present bias and decision cost; a population paid in cash with no payroll deduction has no decision to default, so a setting difference of that kind touches the mechanism.)
4. **Check for near-setting replications**, using only what the user or the evidence scan brief supplied; never from memory. None supplied means the finding is treated as single-setting, which widens the discount.
5. **Discount.** Start from the published effect. State that academic effects average several times the field effect (8.7 against 1.4 points) and that lab effects shrink further in the field (0.33 to 0.02 SD in the loss-framing case). Then, for each "yes" or "unknown" row, widen the discount and say why. Give a range, not a point, label it provisional, and say that the planning number is `estimate-expected-effect`'s job. See `references/evidence-notes.md` for the numbers and their sources.
6. **Give the verdict**: likely transfers, transfers with modifications, unlikely to transfer, or cannot tell. "Cannot tell" is the honest verdict when the mechanism is not stated or two or more rows are "unknown"; it is not a failure of the skill.
7. **List the assumptions to test locally**, each as a testable statement with the cheapest check (a survey item, an interview question, a small A/B arm), and say which assumption would change the verdict most if it failed.
8. **Stop here.** Hand the discount range to `estimate-expected-effect` and the assumptions to the team's fieldwork or `decompose-comb-barriers`. Do not redesign the intervention and do not review the population's culture.

See `references/worked-example.md` for a complete run moving the Afghanistan default-contribution finding to a garment-worker savings program in Bangladesh.

## Output template

```markdown
# Transferability assessment: <short name of the finding>

**Decision this informs:** <pilot / scale-up / proposal number / go or no-go>
**Finding:** <citation as supplied>; effect <size and unit>; claimed mechanism: <... or "not stated">
**Near-setting replications supplied:** <list, or "none supplied; treated as single-setting">

## Fit, dimension by dimension

| Dimension | The study | Your case | Difference | Touches the mechanism? |
|---|---|---|---|---|
| Units (who, how many) | <...> | <...> | <...> | <yes / no / unknown: why> |
| Treatment (what, as delivered) | <...> | <...> | <...> | <...> |
| Outcome (what was measured, when) | <...> | <...> | <...> | <...> |
| Setting (institutions, infrastructure, channel, literacy) | <...> | <...> | <...> | <...> |
| Implementer (who delivered, with what trust and capacity) | <...> | <...> | <...> | <...> |

## Verdict
<likely transfers / transfers with modifications / unlikely to transfer / cannot tell>, because <the differences that touch the mechanism>.

## Discounted expected effect (provisional)
- Published effect: <size, unit>
- Published-to-field discount: <reason, with the source>
- Further discount for untested differences: <one line per "yes" or "unknown" row>
- Range to hand to estimate-expected-effect: <low to high, unit>; provisional, not a planning number

## Assumptions to test locally
1. <testable statement>: <cheapest check>; <would change the verdict if it failed? yes / no>
2. <...>

## What to check before relying on this
- <the "unknown" row that matters most>
- <whether the mechanism is present in your population at all>
```

## Where it goes wrong

- **Confusing similarity with transfer.** Two populations can match on every demographic and differ on the one feature the mechanism needs, or differ on everything visible and share it. Only mechanism-relevant differences change the verdict; the table asks the question row by row so that a demographic match cannot stand in for the answer.
- **Quoting the published number as the expected effect.** Journal effects average several times field effects. A proposal that carries 40 points from Afghanistan into a budget line has skipped this skill; the output must give a discounted range, never repeat the published point estimate as the expectation.
- **Running on several findings at once.** Pooling studies and weighing them is `assess-evidence-base`'s job; this skill runs once per finding, and a request with three papers gets three runs or a question about which one matters.
- **Drifting into cultural theory.** The temptation is to explain what the target population is like. The skill asks whether the study's conditions hold, not what the population values; if the answer needs a cultural account, say so, name it as out of scope, and stop.
- **Replications from memory.** A remembered "there was a similar study in Kenya" is not a replication. Only replications the user or the evidence scan brief supplied, with citations, count; otherwise the finding is single-setting.
- **Treating "cannot tell" as failure.** When the mechanism is unstated or several rows are unknown, "cannot tell" is the right verdict, and the output's value is then the list of what to test. Forcing a verdict to look decisive is the error.

## When to bring in a specialist

Tell the user to consult a behavioral scientist, and a local researcher who knows the population, when:
- The decision is a scale-up or a policy and the verdict is anything other than "likely transfers"; the next step is a local test designed by someone who does this for a living
- The finding concerns clinical, safety, or financial-risk behaviors (medication adherence, HIV testing, defaults that lock up money), where a wrong transfer harms people rather than wasting budget
- The evidence scan brief flags the mechanism itself as contested, so the fit table has nothing stable to compare against
- The team has no field contact with the population and cannot check the mechanism assumptions; a local researcher should run the checks before the discount range is used

Bring them: the fit table, the verdict with its mechanism reasoning, the discount range, and the list of assumptions to test.
