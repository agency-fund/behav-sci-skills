---
name: plan-trials-of-improved-practices
description: >-
  Use when you have one or more candidate practices (a new feeding routine, a
  handwashing step, a way of storing tablets) and want to know whether real
  households will keep doing them before you build counseling or a program
  around them. Also use when a team is about to pick a "recommended practice"
  from a guideline without asking families whether it fits their homes, or
  when positive-deviant practices need to be tried by ordinary households.
  Produces a plan for Trials of Improved Practices (TIPs, the Manoff Group
  method): a practice menu tied to barriers, two household-visit protocols, a
  recording sheet, and the decision rule for keeping a practice. Do not use
  when you need a formal pilot with recruitment, retention, and go/no-go
  thresholds; use design-pilot-feasibility-study instead. Not for finding
  candidate practices in the first place (identify-positive-deviants) or for
  writing the counseling script once practices are chosen (draft-lever-content).
license: CC-BY-4.0
metadata:
  title: Try candidate practices in real homes first
  type: atomic
  stage: diagnose
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "qualitative, barrier-analysis"
  consumes: "intervention-levers, barrier-diagnosis"
  produces: ""
---

## What it does

Plans a round of household trials in which families try one or two candidate practices for about a week, then report what they kept, changed, or dropped.

Trials of Improved Practices (TIPs) is a formative-research method: instead of choosing the "right" practice from a guideline, a counselor visits each household, looks at what the family does now, offers one to three options that fit the gap, lets the family choose, and comes back after the trial period to hear what happened. This skill produces the plan (practice menu, visit protocols, recording sheet, decision rule), not the counseling content. The households' verdicts, tallied across the sample, decide which practices survive.

## When to use it

### Use it when
- A team has candidate practices (from a guideline, from positive deviants, or from its own levers) and asks "will families actually do this?" before building counseling content around them
- Someone says "let's test the recommended practices with a few households first" or "we want mothers to try it before we roll it out"
- A practice is being chosen on expert judgment alone, the program has household access, and nobody has watched a family try it at home
- Positive-deviant practices have been identified and need to be tried by ordinary households to see whether they transfer

### Do not use it when
- No candidate practices exist yet, or the barrier they address is unknown; run `identify-positive-deviants` or `decompose-comb-barriers` first
- The question is whether a program can recruit, retain, and deliver with fidelity, judged against go/no-go thresholds; that is `design-pilot-feasibility-study`
- The practices are already chosen and the task is the counseling card or message; that is `draft-lever-content`
- The team wants to know whether a practice changes an outcome (growth, adherence rates); TIPs reports acceptability, not effect; go to `plan-evaluation-design`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The candidate practices, each stated as who does what, when, how often, with the barrier each is meant to address. Paste the candidate levers from `select-intervention-levers` or the practices from `identify-positive-deviants` if they exist. A practice with no barrier behind it is a wish, not a candidate; send it back.
2. **Required.** The households and the visitors: who in the household does the practice and who decides, where they are, roughly how many can be visited twice within two to three weeks, who will visit (counselors, community health workers, researchers), and in which language.
3. Optional. What households do now, if interviews or observation already exist; otherwise visit 1 collects it.
4. Optional. Constraints: what each practice costs the household, what the program can supply (soap, cups, containers), and anything seasonal that would make the trial week unrepresentative.

If 1 is missing, ask and stop. If 2 is missing, ask once; if the answer is still thin, proceed with a small purposive sample (enough that each practice is tried by several households), two visits about a week apart, and mark that assumption at the top of the plan. If 3 and 4 are missing, note it under "What to check".

## What it draws on

- Manoff Group. *Trials of Improved Practices (TIPs)*. Method page. [unverified, author to confirm] (manoffgroup.com now redirects to jsi.org; no page confirming the method was reachable in this library's audit).
- Dickin, K., Griffiths, M., & Piwoz, E. (1997). *Designing by Dialogue: A Program Planners' Guide to Consultative Research for Improving Young Child Feeding*. AED/SARA Project. [unverified, author to confirm].
- Alive & Thrive. Formative research guides. [unverified, author to confirm] (site returned 403 in the audit).
- CORE Group (2013). *Designing for Behavior Change: For Agriculture, Natural Resource Management, Health and Nutrition*. CORE Group, Food Security and Nutrition Network, USAID. https://coregroup.org/resource-library/designing-for-behavior-change-for-agriculture-natural-resource-management-health-and-nutrition/ (CORE Group is listed among TIPs users.)

TIPs, as described in the sources above, runs in two household visits around a short trial period: visit 1 assesses the current practice and negotiates one to three options the household chooses from; the household tries its choice for about a week; visit 2 records acceptability, modifications, and reasons. The tally across households shows which practices survive contact with real homes and which modifications families make on their own. This skill adds three judgment calls: every practice on the menu must name the barrier it addresses; the recording sheet separates kept, modified, and dropped, each with a verbatim reason; and the decision rule for keeping a practice is written down before fieldwork, so the tally cannot be read to confirm the team's favorite. All three primary sources are unverified in this library's audit, so the method is described generically; see `references/evidence-notes.md`.

**WEIRD skew:** TIPs was developed for young-child feeding programs in low- and middle-income countries, so the usual direction of skew does not apply; the risk runs the other way, carrying a method tuned to feeding into sanitation, adherence, or agriculture without checking that a one-week trial fits the practice's rhythm. **Non-WEIRD evidence:** the labs report behind the dossier lists TIPs use in Indonesia, Zambia, Malawi, Pakistan, Peru, the Dominican Republic, and Rwanda, at report level with no citations retrieved; no WEIRD use was found in the sources this skill draws on.

**Replication status:** practitioner method, single-source; no validation study comparing practices chosen by TIPs with practices chosen another way was found in the dossier, so treat the method as a structured way to ask households, not as evidence that TIPs-chosen practices work.

## How to do it

1. **Carry over the candidate practices with their barriers**, verbatim, at the top of the plan. Drop or send back any practice that has no barrier link.
2. **Write the practice menu.** For each practice: who, what, when, how often; the barrier it addresses; what the household needs to do it (materials, time, money); and a reduced version for households that find the full practice too much. The reduced version is what keeps a household in the trial instead of dropping out.
3. **Draft the visit-1 protocol.** Start with the current practice (what happened yesterday, or observe), name the gap, present only the one to three options that fit that gap, let the household choose one (at most two), agree the specifics (when, with what, who), and ask what they expect to be hard. The household's own choice is the point; a counselor who assigns a practice is running a compliance check, not a trial.
4. **Set the trial period and the follow-up date.** About a week for daily practices; longer for practices done less often, so each household has several chances to do it.
5. **Draft the visit-2 protocol.** Did they try it, how many times, what did they change and why, what did other household members say, will they continue, what would make it easier. Record reasons in the family's words; the modifications and reasons are the finding, not the yes/no.
6. **Build the recording sheet**, one row per household per practice, with the columns in the template. Add a safety column if any practice could be modified into something harmful.
7. **State the decision rule before fieldwork.** Keep a practice if most households that tried it kept it or modified it in a way that preserves the mechanism; rewrite it if the common modification breaks the mechanism; drop it if most dropped it or the stated reason was cost or safety. List in advance which modifications preserve the mechanism and which break it.
8. **Plan the tally and the write-up:** for each practice, how many tried, kept, modified, dropped; the most common modification; the most common reason; the verdict under the rule.
9. **Stop here;** writing the counseling content for the surviving practices is `draft-lever-content`'s job, and testing whether the program can deliver them at scale is `design-pilot-feasibility-study`'s.

See `references/worked-example.md` for a complete run on child-feces disposal in Indonesian CLTS villages.

## Output template

```markdown
# Trials of Improved Practices plan

**Behavior and barrier(s):** <who, what, when; the confirmed barrier(s), carried over verbatim>
**Households:** <who does the practice, who decides, where, how many, who visits, language>
**Trial period:** <length and why; dates of visit 1 and visit 2>

## Practice menu
| # | Practice (who, what, when, how often) | Barrier it addresses | What the household needs | Reduced version |
|---|---|---|---|---|
| 1 | <...> | <...> | <materials, time, money> | <...> |

## Visit 1 protocol
1. <current practice: the question asked or what is observed>
2. <name the gap; present only the options (1 to 3) that fit it>
3. <household chooses one, at most two; agree when, with what, who>
4. <ask what they expect to be hard; record in their words>

## Visit 2 protocol
1. <tried? how many times?>
2. <what changed, and why, in their words>
3. <what other household members said>
4. <will they continue; what would make it easier>

## Recording sheet
| Household | Practice | Tried (times) | Kept / modified / dropped | Modification | Reason (verbatim) | Others' reaction | Continue? |
|---|---|---|---|---|---|---|---|

## Decision rule (fixed before fieldwork)
- Keep: <...>
- Rewrite: <...>
- Drop: <...>
- Modifications that preserve the mechanism: <list>. Modifications that break it: <list>.

## What to check before relying on this
- <the assumption most likely to be wrong: sample, season, who really decides>
```

## Where it goes wrong

- **Counselor assigns, household complies.** If visit 1 ends with "please do this", the trial measures politeness. The protocol must present options and record the household's choice in its own words.
- **Reading "tried once" as "adopted".** A practice tried once and then dropped tells you about the first attempt, not about adoption. The sheet records times tried and the continue intention separately.
- **Treating acceptability as effect.** TIPs shows that a family will do a practice at home, not that the practice improves nutrition, adherence, or sanitation. The write-up must not claim an outcome.
- **A menu with no reduced version.** Households that cannot manage the full practice drop out instead of showing you the version they can manage, which is often the one worth promoting.
- **Writing the rule after the tally.** A decision rule chosen once the counts are in will favor the team's preferred practice. The rule, with the list of mechanism-preserving modifications, goes in the plan before fieldwork.
- **A trial week that misses the practice's rhythm.** A weekly market purchase or a monthly clinic visit cannot be trialed in seven days; set the period from the practice's frequency, not from the method's habit.

## When to bring in a specialist

Tell the user to consult a clinician, a nutritionist, or the program's safeguarding lead when:
- A practice involves medication dosing or timing, feeding of infants under six months, or anything else with clinical risk; a clinician must approve every option on the menu, and every allowed modification, before a household tries it
- A practice adds a food or a cost in a season when households are short, so the trial could displace something the family needs; a nutritionist or program specialist should check the menu and the reduced versions
- Households modify a practice in a way the team cannot judge safe at visit 2; stop the tally for that practice until someone qualified has looked

Bring them: the practice menu with its barrier links, the list of allowed modifications, and the recording sheet.
