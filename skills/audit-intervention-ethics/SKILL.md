---
name: audit-intervention-ethics
description: >-
  Use when a behavioral intervention has been drafted (a default, a norm
  message, a public pledge, an incentive, a recognition scheme, a reminder)
  and someone asks "is this ok to do?", "is this manipulative?", "will people
  feel shamed?", "do we need to tell them?", or a funder wants an ethics
  check before launch. Also use when a draft relies on shame, fear,
  deception, money offered to people who cannot refuse it, or anything aimed
  at children. Reviews the draft against the OECD (2022) good-practice
  principles and Sunstein's (2015) autonomy, welfare, and dignity tests,
  rates six tests, and returns go, revise, or stop with the required changes.
  Do not use when no draft exists and the team is still choosing the lever;
  select-intervention-levers flags Coercion and Restriction at that step. Not
  for research ethics or IRB review of a study (your organization's ethics
  board), or for rewriting the draft (the skill that produced it, or
  draft-lever-content).
license: CC-BY-4.0
metadata:
  title: Check an intervention is ethical before launch
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: not-applicable
  tags: "ethics, choice-architecture, behavior-change-techniques"
  consumes: "intervention-draft"
  produces: ""
---

## What it does

Reviews one drafted behavioral intervention against published ethical principles for behavioral public policy, returning go, revise, or stop with the reasons.

An intervention can work and still be wrong: it can work only while hidden, make the alternative hard to find, shame or frighten people, or pay people who cannot afford to refuse. This skill asks of a finished draft the questions the OECD's good-practice principles and Sunstein's tests ask: could it be disclosed without losing its effect, can a person decline easily, whose interest it serves and who bears the cost, who is excluded or exposed, whether it relies on shame, fear, or deception, and what the audience is told and what is collected about them. It is a lens on the draft, not a substitute for the organization's ethics board, and it names the questions that belong there.

## When to use it

### Use it when
- A draft intervention exists (from `select-default-option`, `write-social-norm-message`, `plan-collective-pledge`, `design-incentive-scheme`, `design-social-recognition`, `draft-lever-content`, or another technique skill) and the team, a funder, or a partner asks whether it is acceptable to run
- Someone asks "is this manipulative?", "is this shaming people?", "do we have to tell them?", "can they opt out?", or "is it ok to pay poor people for this?"
- The draft relies on shame, fear, scarcity cues, deception, a default people will not notice, money offered to people who cannot refuse it, or anything aimed at children
- A pledge, declaration, public list, or recognition scheme will make visible who did and who did not do the behavior

### Do not use it when
- No draft exists and the team is still choosing the lever; `select-intervention-levers` already flags Coercion and Restriction at that step, and this skill needs a named mechanism to review
- The question is the ethics of a study (consent to be researched, randomization, risks to participants as subjects); that belongs to the organization's ethics board or institutional review board, and this skill says so rather than answering
- The verdict is "revise" and the team wants the rewritten draft; go back to the skill that produced it (`write-social-norm-message`, `select-default-option`, `plan-collective-pledge`, `design-incentive-scheme`, `design-social-recognition`) or to `draft-lever-content`
- The team wants to check its own assumptions about the population; that is `audit-researcher-bias`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The draft, with its mechanism named: what is delivered, to whom, through what mechanism (a default, a descriptive-norm message, a public pledge, a conditional payment, a visible token, a reminder, a loss frame). The ethics of a message and of a default differ: a message can be read and ignored; a default acts on people who never read anything. If the mechanism is not named, ask; if the user cannot name it, send the draft back to the skill that produced it. Do not review a draft whose mechanism is unknown.
2. **Required.** Who delivers it and who it is done to, including the relationship (government to citizen, NGO to beneficiary, employer to worker, lender to borrower, teacher to child, village head to household), and whether any of the audience are children, in crisis, or dependent on the deliverer.
3. **Required.** What the audience will be told and what they will not be told, including whether they will know they are in a program or a trial.
4. Optional. What data the intervention collects or uses (names, phone numbers, health status, payments, who complied) and who sees it.
5. Optional. The outcome the intervention serves and the evidence that it serves the audience's own interest, so welfare is judged in their terms rather than the program's.

If 1 is missing or the mechanism is unnamed, ask and stop. If 2 or 3 is missing, ask once; if still missing, proceed, rate the affected tests "cannot assess", and cap the verdict at "revise". If 4 and 5 are missing, assume no data beyond delivery logs and judge welfare by the behavior's stated benefit, marked as the program's own claim.

## What it draws on

- OECD (2022). *Good practice principles for ethical behavioural science in public policy*. OECD Public Governance Policy Papers. https://doi.org/10.1787/e19a9be9-en
- Sunstein, C. R. (2015). The ethics of nudging. *Yale Journal on Regulation*, 32(2), 413. https://www.yalejreg.com/print/the-ethics-of-nudging/ (SSRN version, 2014: https://doi.org/10.2139/ssrn.2526341)
- OECD (2019). *Tools and Ethics for Applied Behavioural Insights: The BASIC Toolkit*. https://doi.org/10.1787/9ea76a8f-en (ethics section)
- Lades, L. K., & Delaney, L. (2022). Nudge FORGOOD. *Behavioural Public Policy*, 6(1). https://doi.org/10.1017/bpp.2019.53 (online 2020; the dossier gives the acronym and title only, so this skill does not expand FORGOOD into its dimensions)
- Mathur, A., et al. (2019). Dark patterns at scale. *Proceedings of the ACM on Human-Computer Interaction*, 3(CSCW), 81. https://doi.org/10.1145/3359183
- Gray, C. M., et al. (2018). The dark (patterns) side of UX design. *CHI 2018*. https://doi.org/10.1145/3173574.3174108
- Maier, M., et al. (2022). No evidence for nudging after adjusting for publication bias. *Proceedings of the National Academy of Sciences*. https://doi.org/10.1073/pnas.2200300119
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709

Sunstein (2015) supplies the three tests this skill runs by name: autonomy (does the intervention respect the person's ability to choose otherwise), welfare (does it make the person better off by their own lights), and dignity (does it treat the person as an agent rather than an object to be steered), with transparency as the condition that makes the other three checkable. The OECD (2022) principles and the ethics section of the BASIC toolkit (OECD 2019) are the public-policy statements of the same demands, adding consent and data handling; the dossier records their titles and existence, not their text, so the mapping of this skill's six tests onto the OECD's wording is the drafter's and should be checked against the published document (unverified, author to confirm). Mathur et al. (2019) and Gray et al. (2018) catalog interface designs that work against the user (15 types in 7 categories from about 11,000 sites; 5 categories from 118 practitioner examples); the dossier records the counts, not the type names, so this skill uses them as the test "would a reviewer call this a dark pattern" rather than quoting the taxonomy. See `references/evidence-notes.md` for the annotated list.

Judgment calls this skill adds: the fairness and equity test (not among Sunstein's three; it follows the Equity criterion of APEASE used in `select-intervention-levers`), the four flags raised regardless of the ratings, the rule that a "go" cannot sit above a "fail", and the rule that a draft without a named mechanism is not reviewed. The welfare test leans on the cross-cutting cautions: bias-corrected nudge effects average about d = 0.04 (Maier et al. 2022), and nudge-unit trials average 1.4 percentage points against 8.7 in academic journals (DellaVigna & Linos 2022), so "it works" is a weaker welfare argument than the published literature makes it look.

**WEIRD skew:** The sources are normative documents from the OECD, whose members are mostly high-income governments, and a US legal scholar, plus two studies of English-language websites. They state principles rather than effects, so there is no finding to generalize, which is why `weird` is set to not-applicable. What a user elsewhere should check locally: who gives consent (the person, a household head, a village assembly), whether public visibility reads as recognition or as shaming, whether a government, an NGO, or a chief as deliverer carries different legitimacy, and whether people exposed by the intervention can leave. **Non-WEIRD evidence:** none found in the sources this skill draws on; the concern that community-led total sanitation programs have used shaming tactics is an LMIC case the dossier names without a verified paper (unverified, author to confirm).

**Replication status:** Normative; the principles are not an effect and have no replication status. The empirical premise of the welfare test, that the intervention works, should be read with the discounts above.

## How to do it

1. **Write the intervention in one paragraph:** what is delivered, to whom, by whom, through what mechanism, in the audience's terms. If the mechanism cannot be stated, stop (see Before you start); the rest of the audit depends on it.
2. **Run the transparency test.** Write the plain disclosure the audience could be given ("we set the deduction to 5% unless you tell us otherwise") and ask whether the effect would survive it. An intervention that works only while hidden fails.
3. **Run the autonomy test.** How does a person decline, choose otherwise, or opt out; how many steps; would they know they can? For a default, the opt-out route and its cost; for a pledge, whether declining is visible and sanctioned; for an incentive, whether refusing costs more than the money.
4. **Run the welfare test.** Whose interest does it serve, by whose judgment; who bears the cost in time, money, exposure, or risk; does the person end up better off by their own lights? State the effect the program expects and discount it for the cautions above.
5. **Run the fairness and equity test.** Who is excluded (no phone, no literacy, not in the register) and who is more exposed (the poorest, women, renters, minorities); does the intervention widen a gap?
6. **Run the dignity test.** Does it rely on shame, fear, deception, or on steering people as objects? Public visibility of who has not done the behavior is shame unless those people chose the visibility.
7. **Run the consent and data test.** What the audience is told and not told, what is collected, who sees it, whether a person can be identified from anything public, and whether they know they are in a trial.
8. **Raise the four flags regardless of the ratings:** coercion (a penalty for not complying), restriction (an option removed), incentives offered to people who cannot refuse because they are poor, and anything applied to children. Each flag is "none" or a description; a flag is not a rating.
9. **Rate each test pass, concern, or fail** with a one-clause reason, or "cannot assess" where the input is missing.
10. **Give the verdict.** Go: every test passes, or each concern has a named mitigation. Revise: at least one fail that a named change fixes; list the change and the skill that makes it. Stop: a fail no change fixes (deception the effect depends on, coercion of dependents, shaming children). A "go" with a "fail" in the table is an error. Say whether the organization's ethics board must see the draft before launch, and list the research-ethics questions that belong to it.
11. **Stop here.** Do not rewrite the draft; the producing skill does that, and the audit runs again on the revision.

See `references/worked-example.md` for a complete run on a community-led sanitation pledge in Indonesia.

## Output template

```markdown
# Intervention ethics audit

**Intervention in one paragraph:** <what is delivered, to whom, by whom, through what mechanism, in the audience's terms>
**Mechanism:** <default / norm message / pledge / incentive / recognition / reminder / frame / other, named>
**Deliverer and audience:** <relationship> **Children or dependents in the audience:** <no / yes: who>

## Tests
| Test | Rating | Reason |
|---|---|---|
| Transparency | <pass / concern / fail / cannot assess> | <the plain disclosure, and whether the effect survives it> |
| Autonomy | <...> | <how a person declines; steps; whether they would know> |
| Welfare | <...> | <whose interest; who bears the cost; expected effect, discounted> |
| Fairness and equity | <...> | <who is excluded or more exposed> |
| Dignity | <...> | <shame, fear, deception, steering> |
| Consent and data | <...> | <what they are told; what is collected; who sees it; trial awareness> |

## Flags
- **Coercion:** <none / description>
- **Restriction:** <none / description>
- **Incentives to people who cannot refuse:** <none / description>
- **Children:** <none / description>

## Verdict: <GO / REVISE / STOP>
<two to four sentences giving the reasons, pointing at the rows that decided it>

## Required changes before launch
1. <change> (to be made in <skill>)

## Questions for the organization's ethics board
- <research-ethics question, or "none identified">

## Open questions
- <what the audit could not assess, and who can answer it>
```

## Where it goes wrong

- **Auditing the words instead of the mechanism.** A friendly sentence announcing a default gets a transparency pass because the text is clear, while the default acts on everyone who never reads it. The mechanism, not the copy, is the thing under review; name it first.
- **"It works" as the welfare answer.** Effectiveness is not welfare: the question is better off by whose judgment, at whose cost. The effect is also usually smaller than published (Maier et al. 2022; DellaVigna & Linos 2022), so a cost justified by a headline effect may not be justified by the real one.
- **Visibility counted as recognition.** A public list of who vaccinated is recognition for the people on it and exposure for the people who are not. Rate dignity for the non-doers, not the doers.
- **Program enrollment treated as consent to everything.** Joining a program is not consent to a particular mechanism, to data use, or to being in a trial. Each needs its own line in the consent and data row.
- **A "go" from good intentions.** The verdict comes from the table. A "go" above a "fail" row, or a "revise" with no named change, is an audit that did not happen.
- **Acting as the ethics board.** This skill does not approve research with human subjects and must not say it has; it says which questions go to the board and launches nothing.

## When to bring in a specialist

Tell the user to consult the organization's ethics board or an ethicist with behavioral-policy experience, and where noted a safeguarding lead, a data-protection officer, or a local qualitative researcher, when:
- Any test rates "fail" and the team wants to proceed anyway, or the verdict is "stop" and the team disputes it
- The audience includes children, people in crisis, or people dependent on the deliverer (workers, borrowers, tenants, pupils); a safeguarding lead reviews before any launch
- The consent and data row raises identification risk (HIV status, debt, pregnancy, who complied), where a data-protection officer or counsel checks what may be collected and shown
- The intervention is part of a trial, where consent to be researched, randomization, and risk to participants are the board's questions, not this skill's
- A public-visibility mechanism (pledge, list, token) is planned where sanctions against non-doers can be violent or economic; a local qualitative researcher checks what visibility costs here before the pledge is planned further

Bring them: the one-paragraph description with the mechanism named, the test table, the flags, the verdict, and the required changes.
