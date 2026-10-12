---
name: diagnose-social-norm
description: >-
  Use when a program suspects people keep doing something (open defecation,
  early marriage, skipping a clinic visit) because of what others around them
  do or expect, and wants to know whether that is actually a social norm
  before building anything on it. Also use when someone says "everyone here
  does it" or "the community would not accept it" and the team needs to test
  that claim with respondents. Produces a social norm diagnosis: answers to
  four expectation questions from a sample, a classification as social norm,
  descriptive norm, custom, or moral rule following Bicchieri's framework,
  the reference group respondents point to, and the sanctions. Do not use
  when the norm is already confirmed and the question is exactly whose
  behavior and approval people track; use map-reference-network. Not for
  drafting a norm message or a pledge (write-social-norm-message,
  plan-collective-pledge), and not for building the survey vignette that
  measures expectations (draft-norms-vignette).
license: CC-BY-4.0
metadata:
  title: Find out whether a practice is a social norm
  type: atomic
  stage: diagnose
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "social-norms, qualitative, diagnosis"
  consumes: "target-behavior-brief, qualitative-data"
  produces: "social-norm-diagnosis"
---

## What it does

Determines whether one practice is held in place by what people expect of each other, rather than by habit, personal preference, or moral conviction.

A social norm, in Bicchieri's sense, is a practice people follow because they believe others follow it (an empirical expectation), believe others think they should follow it (a normative expectation), and would stop if those beliefs changed (a conditional preference). This skill asks a sample four questions, classifies the practice, names the reference group respondents point to, and records what happens to people who deviate. It produces a diagnosis, not a message or a pledge; those come later, and only if the diagnosis supports them.

## When to use it

### Use it when
- A team believes "everyone does it here" or "the community would never accept that" and needs to test the claim with respondents rather than assume it
- `decompose-comb-barriers` produced an Opportunity (social) hypothesis ("doing it would signal something people want to avoid") that field work now needs to confirm or rule out
- Someone asks "is this a norm or just a habit?", "would people change if they saw others change?", or "who are they worried about disapproving?"
- A program is about to run a norm-based intervention (publicizing what others do, a public pledge, a community declaration) without evidence that expectations drive the practice

### Do not use it when
- The practice is already diagnosed as a social norm and the question is exactly whose behavior and approval people track; that is `map-reference-network`
- The team wants the survey instrument that measures expectations with controlled variation; that is `draft-norms-vignette` (measure stage)
- The team wants to write the message or plan the pledge; `write-social-norm-message` and `plan-collective-pledge` take a confirmed diagnosis as input, not a hunch
- The barrier has not been narrowed at all and several explanations compete; run `decompose-comb-barriers` first and come here only for its social hypotheses

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The practice as who does what, when, and whether the program wants more or less of it. Paste the target behavior brief from `define-key-behavior` if one exists. A norm diagnosis attaches to one practice; "hygiene" or "gender roles" is too wide to classify.
2. **Required.** What evidence exists or can be collected: interview or focus group transcripts, field notes, or a planned round of interviews, and with whom. State roughly how many respondents and how they were chosen.
3. **Required.** Whether the practice is sensitive, stigmatized, illegal, or harmful (female genital cutting, child marriage, violence, drug use). This changes how the questions can be asked, and whether some can be asked at all.
4. Optional. Who the program assumes the reference group is (the people whose behavior and opinion the actor tracks), and any Opportunity (social) hypothesis from `decompose-comb-barriers`.
5. Optional. Any prevalence figure the program already has (a survey saying 60% do X). It is context, not a diagnosis.

If 1 is missing, ask and stop. If 2 is missing, ask once; if no data exist and no fieldwork is possible, produce only the question set and the classification rules, mark the diagnosis "pending field answers", and say so at the top. If 3 is missing, treat the practice as sensitive until told otherwise and apply the specialist section before any question is asked.

## What it draws on

- Bicchieri, C. (2016). *Norms in the Wild: How to Diagnose, Measure, and Change Social Norms*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780190622046.001.0001
- Bicchieri, C., & Mercier, H. (2014). Norms and beliefs: How change occurs. In *The Complexity of Social Norms*. Springer. https://doi.org/10.1007/978-3-319-05308-0_3
- Cislaghi, B., & Heise, L. (2018). Theory and practice of social norms interventions: Eight common pitfalls. *Globalization and Health*, 14. https://doi.org/10.1186/s12992-018-0398-x (chosen over the same authors' 2018 *Health Promotion International* paper because it lists the diagnostic mistakes this skill guards against)
- UNICEF Innocenti / Penn Social Norms Group (2016). *Why Do People Do What They Do? A Social Norms Manual for Viet Nam, Indonesia and the Philippines*. Unverified, author to confirm: the manual could not be re-fetched in the evidence audit.
- Pickering, A. J., Djebbari, H., Lopez, C., Coulibaly, M., & Alzua, M. L. (2015). Effect of a community-led sanitation intervention on child diarrhoea and child growth in rural Mali: A cluster-randomised controlled trial. *The Lancet Global Health*, 3(11), e701–e711. https://doi.org/10.1016/S2214-109X(15)00144-8
- Cameron, L., Gertler, P., Shah, M., Alzua, M. L., Martinez, S., & Patil, S. (2022). The dirty business of eliminating open defecation: The effect of village sanitation on child height from field experiments in four countries. *Journal of Development Economics*, 159, 102990. https://doi.org/10.1016/j.jdeveco.2022.102990

Bicchieri's framework sorts shared practices by what the person's preference depends on. A custom is followed because it meets the person's own needs, whatever others do. A moral rule is followed because the person holds it right, whatever others do. A descriptive norm is followed because the person expects others to follow it (empirical expectation only). A social norm is followed because the person expects others to follow it and believes others expect them to (empirical plus normative expectation), usually with sanctions for deviating. The distinction matters because the remedies differ: information about what others do can move a descriptive norm; a social norm also needs normative expectations to shift, which is what public pledges and community declarations in community-led total sanitation (CLTS) are meant to do. The CLTS trials are the field evidence that a norm-held practice shifts collectively, with a threshold: child height gained about 0.3 SD only once village coverage passed 50 to 75%. This skill adds two judgment calls: the gap between personal belief and perceived normative expectation is a mandatory line in the output, because it decides whether a later message would correct a misperception or publicize a real majority; and the "if others stopped, would you?" probe must be asked before a practice is called conditional.

**WEIRD skew:** The diagnostic manual was written with UNICEF for trainings in Southeast Asia and Southern Africa (reported; manual unverified), so the method is not WEIRD-derived. What varies locally is who the reference group is, which sanctions are credible, and whether respondents answer expectation questions honestly in front of an outsider; check all three before trusting a classification. **Non-WEIRD evidence:** UNICEF trainings on the manual in Viet Nam, Indonesia, the Philippines, Zimbabwe, and Swaziland (reported; manual unverified); CLTS cluster-randomized trials in India, Indonesia, Mali, and Tanzania, where private sanitation coverage rose 7 to 39 percentage points and child height gained about 0.3 SD once village coverage passed 50 to 75%; in Mali, no change in diarrhea but an effect on stunting (secondary source per the dossier).

**Replication status:** The measurement approach is peer-reviewed, and the CLTS coverage effect is replicated across four countries with mixed health effects. A causal claim that expectations hold the practice in place needs the vignette variation in `draft-norms-vignette`; the four questions here establish the classification, not the causal weight.

## How to do it

1. **Carry the practice over verbatim** at the top, with the direction the program wants. Everything below attaches to that one practice.
2. **Write the four diagnostic questions in the respondents' terms.** Do not ask "why do you do X?"; it returns rationalizations. Ask instead:
   - Personal belief: "Do you yourself think a person like you should do X?"
   - Empirical expectation: "Out of ten people like you in this community, how many do X?"
   - Normative expectation: "Do the people whose opinion matters to you think you should do X? Who are they?"
   - Deviation: "What happens to someone like you who does not do X? And if most people here stopped doing X, would you still do it?" The second half is the conditionality probe; a practice cannot be called interdependent until it has been asked.
3. **Specify who answers.** The actors themselves, plus some of the people they name as mattering. A sample of program staff or community leaders only describes the official norm, not the lived one.
4. **Collect, or code the existing data against the four questions.** For each question, record what respondents said with counts where possible and quotes where not. Mark any question no respondent actually answered as "not asked"; do not infer its answer.
5. **Classify with the decision tree, showing each branch.** Would people keep doing X if others stopped? If yes, it is a custom (serves their own needs) or a moral rule (held as right regardless); say which. If no, does the preference depend on empirical expectations only (descriptive norm) or on normative expectations too, with sanctions (social norm)? Write "cannot tell" when the evidence does not reach a branch.
6. **Name the reference group provisionally:** who respondents pointed to when answering the normative-expectation question, how consistent the answers were, and whether it matches the program's assumed audience. The full map is `map-reference-network`'s job.
7. **Record sanctions:** what respondents say happens to deviants, who applies it, how severe, and who is exempt. A social norm with no credible sanction is weaker than it looks.
8. **Report the belief-expectation gap.** Compare personal beliefs (question 1) with perceived normative expectations (question 3). Many people privately against X who believe others favor it is a misperception, which a design skill can correct; a real majority for X is not, and publicizing it would backfire.
9. **State confidence** and what would raise it: more respondents, respondents outside the program's contacts, or the vignette variation.
10. **Stop here.** Do not draft the message or the pledge. `map-reference-network` maps the group; `write-social-norm-message` and `plan-collective-pledge` take this diagnosis as input only if the call is "social norm" or "descriptive norm".

See `references/worked-example.md` for a complete run on open defecation in an Indonesian village, and `references/evidence-notes.md` for the evidence behind each claim.

## Output template

```markdown
# Social norm diagnosis

**Practice:** <who does what, when, carried over verbatim; the direction the program wants>
**Evidence used:** <number and type of respondents or transcripts; who they are; how chosen; where and when>
**Sensitivity:** <none stated | sensitive: how the questions were adapted, or which were not asked and why>

## Answers to the four diagnostic questions

| Question | What respondents said (counts or quotes) | What it indicates |
|---|---|---|
| 1. Personal belief | <...> | <for, against, split> |
| 2. Empirical expectation | <...> | <believed prevalence> |
| 3. Normative expectation | <...> | <believed approval, and by whom> |
| 4. Deviation and conditionality | <...> | <sanction named; would stop if others stopped: yes, no, split> |

## Classification

**Call:** <social norm | descriptive norm | custom | moral rule | cannot tell>

- Interdependent (would stop if others stopped)? <yes, no, or split, with the evidence>
- Depends on empirical expectations? <yes or no, with the evidence>
- Depends on normative expectations, with sanctions? <yes or no, with the evidence>

**Belief-expectation gap:** <personal beliefs versus perceived expectations; misperception or real majority>

## Reference group (provisional)
<who respondents named; how consistently; whether it matches the program's assumed audience>

## Sanctions
<what, by whom, how severe, who is exempt>

## Confidence and what would raise it
<low, medium, or high, and why; what data would change the call>

## What to check before relying on this
- <the respondent group most likely to have given the official rather than the lived answer>
- <the branch of the tree the evidence reached least>
```

## Where it goes wrong

- **Calling every shared practice a social norm.** If respondents would keep doing X when others stopped, it is a custom or a moral rule, and a norm message or a pledge will not move it. The conditionality probe in question 4 is mandatory for this reason.
- **Asking "why".** "Why do you do X?" returns the reasons people find acceptable to give, not expectations. Use the four questions as written; adapt the wording, not the structure.
- **Confusing personal belief with normative expectation.** "I think women should deliver at the clinic" answers question 1; "my mother-in-law thinks I should deliver at home" answers question 3. Merging them hides the gap that decides the design.
- **Taking the program's audience as the reference group.** Respondents are asked whose opinion matters; the answer is often someone the program never contacts. Write down what they said, not who the program reaches.
- **Reading a prevalence number as a norm.** "70% do X" is a behavior count. It says nothing about expectations and cannot classify the practice.
- **Reading a descriptive norm as a social norm.** No normative expectation and no sanction means publicizing what others do may work, but pledges and sanction-based approaches have nothing to attach to.
- **Diagnosing from staff or leaders alone.** They report the official norm. Without the actors' own answers the classification is not evidence, and the output must say "pending field answers".

## When to bring in a specialist

Tell the user to consult a local qualitative researcher with experience of the practice, and an ethics reviewer, when:
- The practice is harmful or illegal (female genital cutting, child marriage, intimate partner violence), because asking who sanctions deviants, or asking a respondent whether they would stop, can expose them or the interviewer to risk, and the question set needs review before anyone is asked
- The practice is stigmatized (HIV status, mental illness, sexual behavior), because the empirical-expectation question itself can out people in a group setting
- Answers split cleanly between two groups (one conditional, one not), which suggests two populations with different reference groups and needs a sampling design rather than a judgment call

Bring them: the practice statement, the four questions in local wording, the sampling plan, and whatever answers already exist.
