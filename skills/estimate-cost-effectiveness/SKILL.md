---
name: estimate-cost-effectiveness
description: >-
  Use when a program has an effect estimate and someone asks "what did it
  cost per child immunized", "how does this compare per dollar with the
  other program", "is this worth scaling at this price", or a funder wants
  cost-effectiveness in the report. Also use when a team is about to divide
  its budget by its headline number and call that the cost per outcome.
  Produces a cost per unit of behavior change or outcome from
  ingredients-based costing, a stated perspective, a stated currency year
  and discount rate, the J-PAL impact-per-$100 convention, and a sensitivity
  table, so programs can be compared (Dhaliwal, Duflo, Glennerster and
  Tulloch; J-PAL; Kraft). Do not use when the effect is not yet known and
  the question is what size to expect; use estimate-expected-effect instead.
  Not for whether cost and effect hold at scale (assess-scalability),
  setting the size of a reward (design-incentive-scheme), or comparing
  programs with different outcomes, which needs a benefit-cost analysis.
license: CC-BY-4.0
metadata:
  title: Estimate the cost per unit of behavior change
  type: atomic
  stage: analyze
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "cost-effectiveness, quantitative, scaling"
  consumes: "analysis-plan, evaluation-design"
  produces: ""
---

## What it does

Estimates what one program paid for each unit of behavior change or outcome it produced, in a form that can be set beside another program's number.

Ingredients-based costing means every input is counted at its market value whether or not the program paid for it: a volunteer's hour, a donated hall, and a government nurse's time all go in. The perspective says whose costs count: the program's, the government's, or society's, which adds participants' own time. The result is a cost per unit of effect with the choices behind it stated, and a sensitivity table showing how far the number moves when the cost or the effect moves. It is not a benefit-cost analysis: it puts no money value on the outcome.

## When to use it

### Use it when
- A trial or evaluation has an effect estimate and the team, a funder, or a ministry asks "what did it cost per additional child immunized, per percentage point, per outcome?"
- Two or more programs with the same outcome need to be compared per dollar, or one program needs its number in a funder's comparison table
- A team is about to divide the total budget by the number of people reached, or by the headline effect, and call that the cost per outcome
- The effect comes from a published study elsewhere and the team wants a cost-effectiveness number for its own setting before running a trial
- A scale-up or renewal decision will be argued on cost, and the only costing so far is the accounting budget

### Do not use it when
- The effect is not known yet and the question is what size to plan for; `estimate-expected-effect` produces the discounted effect this skill then consumes
- The question is whether cost and effect will hold when the program grows, changes implementer, or moves region; `assess-scalability`
- The task is to set the size, form, or timing of a reward; `design-incentive-scheme`; this skill costs the scheme once it exists
- The programs being compared have different outcomes (immunization versus school attendance) and the decision needs their value weighed; that is a benefit-cost analysis or a decision-maker's weights, the escalation case below
- The team wants a probability distribution over the cost-effectiveness ratio or the expected value of collecting more information; that is a Bayesian analysis, a different procedure from the deterministic sensitivity ranges here, so ask for one directly

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The effect: the outcome in its units, the estimate with its confidence interval, the number of people it applies to, the period, and where it comes from (this program's trial, or a study elsewhere). If from elsewhere, the discounted effect from `estimate-expected-effect`, not the published figure.
2. **Required.** The cost data available: an ingredients list with quantities and unit prices, or the accounting budget plus a list of inputs the program did not pay for (volunteer time, donated space, government staff, existing infrastructure), and which costs were research rather than delivery.
3. **Required.** The decision and the comparator: which programs will be set beside this one, on which outcome unit, and from whose perspective (program, government, society).
4. Optional. The funder's conventions: currency year, exchange rate or PPP, discount rate, and whether transfers to participants count as costs.

If 1 is missing, ask and stop; a cost per effect needs an effect. If 2 is missing, ask once; if only a budget exists, proceed with the budget and mark every unpriced input as a gap in the sensitivity table. If 3 is missing, assume the program perspective and say so. If 4 is missing, use the trial's final year as the currency year, the average market exchange rate for that year, and a 10% discount rate for costs that fall in more than one year, as the J-PAL guidance does, and state each as an assumption.

## What it draws on

- Dhaliwal, I., Duflo, E., Glennerster, R., & Tulloch, C. (2013). Comparative cost-effectiveness analysis to inform policy in developing countries. In *Education Policy in Developing Countries* (pp. 285–338). University of Chicago Press. https://doi.org/10.7208/chicago/9780226078854.003.0008
- J-PAL (Bhula, Mahoney & Murphy). *Conducting cost-effectiveness analysis (CEA)*. https://www.povertyactionlab.org/resource/conducting-cost-effectiveness-analysis-cea
- Kraft, M. A. (2020). Interpreting effect sizes of education interventions. *Educational Researcher*, 49, 241–253. https://doi.org/10.3102/0013189X20912798
- Banerjee, A. V., Duflo, E., Glennerster, R., & Kothari, D. (2010). Improving immunisation coverage in rural India: Clustered randomised controlled evaluation of immunisation campaigns with and without incentives. *BMJ*, 340, c2220. https://doi.org/10.1136/bmj.c2220
- Kettle, S., Hernandez, M., Ruda, S., & Sanders, M. (2016). Behavioral interventions in tax compliance: Evidence from Guatemala. World Bank Policy Research Working Paper 7690. https://doi.org/10.1596/1813-9450-7690

Dhaliwal, Duflo, Glennerster, and Tulloch set out the comparative approach this skill follows: cost each program by its ingredients, state the perspective, fix a currency year and a discount rate, divide by the effect in a common unit, and present the comparison with its assumptions beside it, because the ratio is only as comparable as the choices behind it. The J-PAL guidance page makes two of those choices concrete: a ten percent discount rate is applied to costs incurred over multiple years, and the monetary value of both cash and in-kind transfers is counted. Kraft argues that an effect size cannot be interpreted without its cost beside it; his benchmarks come from US education trials and are not applied here. Banerjee and colleagues' Rajasthan trial is the worked case: adding a small in-kind incentive to reliable immunization camps cut the cost per fully immunized child from $55.83 to $27.94, because the fixed cost of running a camp was spread over many more children. The judgment calls this skill adds: transfers are shown with and without, since whether they are a cost is contested; research costs are kept apart from delivery costs; the sensitivity table always includes the effect's confidence bounds and, for a transferred effect, the discounted value; and the output states what makes the number not comparable. The J-PAL page has no dedicated sensitivity section, so the sensitivity rows here are the drafter's operationalization of its guidance on key decisions and assumptions. See `references/evidence-notes.md`.

**WEIRD skew:** The method is LMIC-native: the comparative framework and the J-PAL guidance were built for development programs, and the worked numbers come from India and Guatemala. What varies locally is the price of inputs, the wage used for volunteer and participant time, the exchange or PPP treatment, and whether the comparator programs priced their inputs the same way. **Non-WEIRD evidence:** Rajasthan, India (Banerjee et al. 2010): cost per fully immunized child fell from $55.83 to $27.94 when incentives were added to camps; Guatemala (Kettle et al. 2016): tax-compliance letters returned about 36 times the letter cost.

**Replication status:** Not applicable in the effect sense: this is a costing method. What is contested, per the evidence dossier, is how to treat transfers and which discount rate to use, which is why the output shows the ratio with and without transfers and names its rate.

## How to do it

1. **Fix the effect before touching costs.** Write the outcome, its units, the estimate with its interval, the people it applies to, and the period. If the effect is from another study, use the discounted figure from `estimate-expected-effect` and say so; the published number goes in the sensitivity table, not the headline.
2. **State the perspective** and who bears each cost under it. The program perspective counts what the implementer and its partners used; government adds public staff and facilities; society adds participants' time and travel. Say why this perspective fits the decision.
3. **List the ingredients by category:** staff time (hours times a local wage, including volunteers and seconded government staff), materials, transport, equipment (annualized over its useful life), space, training, monitoring, and participants' time if the perspective includes it. Price every input at its market value whether or not the program paid for it, and mark each as paid, donated, or borrowed. Keep transfers to participants (cash, food, vouchers) on their own line, and research costs (surveys, pill counts for the evaluation) outside the delivery total.
4. **Choose the currency year, the exchange or PPP treatment, and the discount rate, and say why.** Default: the trial's final year, the average market exchange rate, and 10% a year on costs that fall in more than one year, the J-PAL convention. Convert everything.
5. **Divide cost by effect in the decision's units.** Compute the delivery cost per person reached, the cost per additional unit of outcome (per additional immunized child, per additional adherent woman), the cost per percentage point per 1,000 people, and the J-PAL convention of impact per $100 spent. Add cost per standard deviation only if the comparison needs it.
6. **Run the sensitivity table.** Rows for the effect at its lower and upper confidence bounds, the discounted effect if the effect was transferred, costs with and without transfers, costs with and without donated inputs, a higher wage for volunteer time, and the society perspective. Show the headline ratio and impact per $100 for each row.
7. **State the comparability limits:** where the comparator programs priced inputs differently, how transfers were treated there, the share of fixed costs (training, equipment, set-up) that would be spread over more people at scale, local prices, and the time horizon.
8. **Stop here.** Whether the cost per outcome holds at scale is `assess-scalability`; a comparison across different outcomes needs a benefit-cost analysis or a decision-maker's weights, the escalation case below.

See `references/worked-example.md` for a complete run on a Malawi antenatal iron-folate adherence program.

## Output template

```markdown
# Cost-effectiveness estimate

**Program:** <name; what was delivered, to whom, over what period>
**Effect:** <outcome in units; estimate (95% CI); people it applies to; source: this trial / discounted transferred effect from estimate-expected-effect>
**Perspective:** <program / government / society>, because <reason tied to the decision>
**Currency and year:** <currency, year; exchange rate or PPP used>; **discount rate:** <rate> (<reason>)
**Comparator(s):** <program(s) and the common outcome unit>

## Ingredients
| Category | Item | Quantity | Unit price | Cost | Paid / donated / borrowed |
|---|---|---|---|---|---|
| Staff time | <...> | <hours> | <wage> | <...> | <...> |
| Materials, transport, equipment (annualized), space, training, monitoring | <one row each> | | | | |
| Participant time (society perspective only) | <...> | | | | |
| **Delivery total** | | | | <...> | |
| Transfers to participants (separate line) | <...> | | | <...> | |
| Research costs (excluded from delivery) | <...> | | | <...> | |

## Ratios
- Delivery cost per person reached: <...>
- Cost per additional <outcome unit>: <delivery total> / <additional units> = <...>
- Cost per percentage point per 1,000 people: <...>
- Impact per $100: <additional units per $100 of delivery cost>
- <Cost per standard deviation, only if the comparison needs it>

## Sensitivity
| Scenario | Cost used | Effect used | Cost per additional <unit> | Impact per $100 |
|---|---|---|---|---|
| Headline | <...> | <point estimate> | <...> | <...> |
| Effect at lower confidence bound | <...> | <...> | <...> | <...> |
| Effect at upper confidence bound | <...> | <...> | <...> | <...> |
| Discounted transferred effect (if the effect is from elsewhere) | <...> | <...> | <...> | <...> |
| Including transfers | <...> | <...> | <...> | <...> |
| Excluding donated inputs | <...> | <...> | <...> | <...> |
| Volunteer time at <higher wage> | <...> | <...> | <...> | <...> |
| Society perspective | <...> | <...> | <...> | <...> |

## Comparability limits
- <transfers: how this program and the comparator treat them>
- <fixed-cost share, and what falls per person at scale>
- <local prices and the wage assumptions>
- <outcome measure differences between this program and the comparator>

## What to check before relying on this
- <the input most likely to be mispriced>
- <whether the comparator programs costed their inputs the same way>
- <whether the effect used is the discounted one, if it was transferred>
```

## Where it goes wrong

- **Budget divided by headline.** Dividing the accounting budget by the number reached, or by the effect, skips every unpriced input and every research cost. The ingredients table exists so that the number counts what was used, not what was paid.
- **Volunteer and government time at zero.** A program run on community health workers and donated clinic space looks cheap until someone else has to pay for them. Price them at the local wage and show the ratio with and without.
- **Published effect used as the effect.** A cost per outcome computed on an effect from a study elsewhere inherits that study's publication bias and lab-to-field shrinkage. Use the discounted figure from `estimate-expected-effect` and keep the published one in the sensitivity table.
- **Transfers hidden or doubled.** A cash transfer is a cost to the program but not a resource consumed, and the comparator may have treated it either way. Show the ratio with and without, on its own line, every time.
- **Comparing across outcomes.** "Program A costs $40 per immunized child and program B $60 per enrolled girl, so A is better" is not a conclusion this skill can reach; it needs a value on each outcome. The skill says so and stops.
- **Pilot costs presented as scale costs.** Training, equipment, and set-up are a large share of a pilot's total and fall per person at scale, while supervision quality may fall too. State the fixed-cost share; leave the scale question to `assess-scalability`.

## When to bring in a specialist

Tell the user to consult a health or development economist with costing experience when:
- The comparison will move budget between programs with different outcomes, which needs a benefit-cost analysis or an explicit statement of the decision-maker's weights, not a cost-effectiveness ratio
- The effect is a health outcome to be expressed in life-years or disability-adjusted life-years, which carries conventions this skill does not implement
- Costs run over several years with uncertain prices or exchange rates, or the funder's conventions conflict with the J-PAL defaults used here
- The result will be published beside other programs' ratios and the comparator costing cannot be checked

Bring them: the ingredients table with its paid, donated, and borrowed marks, the effect with its source and interval, the perspective and conventions chosen, and the sensitivity table.
