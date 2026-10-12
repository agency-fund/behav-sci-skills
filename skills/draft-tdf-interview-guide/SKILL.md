---
name: draft-tdf-interview-guide
description: >-
  Use when one behavior is defined (who, what, when), COM-B barrier hypotheses
  exist, and you need the questions to ask people in interviews to find out
  which barriers are real. Also use when a team says "let's do a few
  interviews" or "what should we ask them about why they don't do it" and has
  no structure for the conversation. Produces a semi-structured interview
  guide covering all 14 domains of the Theoretical Domains Framework (TDF),
  each question tied to the hypothesis it tests, with probes, a consent
  placeholder, and a domains-to-hypotheses map. Do not use when you want many
  short structured interviews comparing people who do the behavior with
  people who do not; use draft-barrier-analysis-questionnaire instead. Not for
  testing whether survey items are understood
  (draft-cognitive-interview-script), not for coding transcripts
  (synthesize-interview-findings), and not for generating the hypotheses
  themselves (decompose-comb-barriers, run it first).
license: CC-BY-4.0
metadata:
  title: Write an interview guide that covers every TDF domain
  type: atomic
  stage: diagnose
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: weird-only
  tags: "tdf, com-b, qualitative, diagnosis"
  consumes: "target-behavior-brief, comb-barrier-hypotheses"
  produces: "interview-guide"
---

## What it does

Writes a semi-structured interview guide that asks about one specified behavior across the 14 domains of the Theoretical Domains Framework, with each question tied to the barrier hypothesis it tests.

The Theoretical Domains Framework (TDF) is a set of 14 domains, such as Knowledge, Social influences, and Emotion, that group the constructs behavior-change theories use to explain why a behavior does or does not happen; each domain maps onto one component of the COM-B model (Capability, Opportunity, Motivation). A semi-structured guide fixes the questions loosely enough that the interviewer can follow the respondent. This skill produces the guide plus a map from domains to hypotheses. It does not run the interviews or analyze them.

## When to use it

### Use it when
- A target behavior brief and COM-B barrier hypotheses exist (from `decompose-comb-barriers`) and the next step is "go and ask people", so the hypotheses need to become interview questions
- A team says "let's do a few interviews" or "what should we ask them about why they don't do it" and has no structure for the conversation
- A team has a list of informal explanations and wants interviews that could also surface barriers nobody has thought of, which is what covering all 14 domains is for
- An existing interview guide asks only about knowledge or motivation and the team suspects it is missing environment, social, or habit barriers

### Do not use it when
- The team wants many short structured interviews that compare people who do the behavior with people who do not; that is `draft-barrier-analysis-questionnaire`
- No hypotheses exist yet and the question is still "why aren't they doing it?"; run `decompose-comb-barriers` first and bring its output here
- The questions are meant to test whether draft survey items are understood as intended; that is `draft-cognitive-interview-script`
- The interviews are done and the transcripts need coding; that is `synthesize-interview-findings`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The target behavior as who, what, when (paste the brief from `define-key-behavior`). Check it against AACTT (Presseau et al. 2019): Action, Actor, Context, Target, Time. "Who, what, when" gives Actor, Action, Time; if Context (where, in what situation) or Target (whom or what the action is directed at) is missing, ask once, then proceed with a marked placeholder.
2. **Required.** The COM-B barrier hypotheses from `decompose-comb-barriers`, or at least the team's informal explanations. The guide tests hypotheses; without them every domain gets a generic question and the interviews cannot tell the barriers apart.
3. **Required.** Who the respondents are (the actors themselves, or also the people around them: spouses, supervisors, health workers), who will interview, in what language, and how long each interview can run. Length sets how many questions per domain survive.
4. Optional. Whether the behavior touches health, legal, safety, sexual, or household-authority topics. This sets the consent wording and the escalation.
5. Optional. What the team already knows about local referents: who "people like you" are, which services or resources exist, what the behavior is called locally.

If 1 is missing, ask and stop. If 2 is missing, ask once; if the user offers informal explanations, write them up as provisional hypotheses marked "written by this skill, not from decompose-comb-barriers"; if there is nothing, stop and point to `decompose-comb-barriers`. If 3 is missing, assume one interview of about an hour with the actors themselves in the local language, and mark the assumption. If 4 and 5 are missing, assume the behavior is not sensitive and leave every local referent as a bracketed placeholder.

## What it draws on

- Atkins, L., et al. (2017). A guide to using the Theoretical Domains Framework of behaviour change to investigate implementation problems. *Implementation Science*, 12, 77. https://doi.org/10.1186/s13012-017-0605-9
- Cane, J., O'Connor, D., & Michie, S. (2012). Validation of the theoretical domains framework for use in behaviour change and implementation research. *Implementation Science*, 7, 37. https://doi.org/10.1186/1748-5908-7-37
- Presseau, J., et al. (2019). Action, actor, context, target, time (AACTT): A framework for specifying behaviour. *Implementation Science*, 14, 102. https://doi.org/10.1186/s13012-019-0951-x
- Huijg, J. M., et al. (2014). Discriminant content validity of a theoretical domains framework questionnaire for use in implementation research. *Implementation Science*, 9, 11. https://doi.org/10.1186/1748-5908-9-11
- Gyani, A., Tindall, K., & Gallagher, R. (2022). *Explore Field Guide: A practical tool to map and unpack behaviour*. Behavioural Insights Team. https://www.bi.team/wp-content/uploads/2022/11/BIT-Explore-Field-Guide.pdf

Atkins et al. (2017) set out the procedure this skill follows: specify the behavior first, write one to three questions per domain, code the transcripts deductively against the domains, then judge which domains matter. Cane, O'Connor and Michie (2012) validated the 14-domain structure in a sort study. Huijg et al. (2014) built a questionnaire item bank for the domains and found that items for 11 of the 14 domains showed discriminant content validity; Reinforcement, Goals, and Behavioral regulation did not, so expect those three to blur in interviews as well. The BIT Explore Field Guide supplies a practitioner interview structure and probing rules. The judgment calls this skill adds: every question is labeled with the COM-B hypothesis it tests, so the interview is a test of the output of `decompose-comb-barriers` rather than a tour of the framework; domains with no hypothesis still get one discovery question; and the running order follows the respondent's episode, not the domain list. The probe wording is adapted from TAF's internal COM-B probe sets, which are seed content, not evidence.

**WEIRD skew:** the TDF was developed and validated in UK health services to study why health professionals do or do not follow guidance, and its published question sets assume that setting (a professional role, a workplace, a guideline). **Non-WEIRD evidence:** none found in the sources this skill draws on. A user elsewhere should rewrite Social/professional role and identity as role in family or community when the actor is not a professional, supply local referents for Social influences (whose approval matters here) and for Environmental context and resources (which services, tools, and costs exist), and check every question for translatability before fieldwork.

**Replication status:** single-study for the domain structure (the Cane 2012 sort study), with Huijg 2014 showing 11 of 14 domains discriminable in questionnaire form; AACTT has no reliability data. The TDF is a classification framework, so there is no effect size to replicate.

## How to do it

1. **Carry the target behavior over verbatim** and write it out as AACTT (Action, Actor, Context, Target, Time) at the top. A guide for "adherence" cannot be answered; a guide for "a pregnant woman takes one iron-folate tablet at home each evening until delivery" can.
2. **Map each COM-B hypothesis to the TDF domain that would hold it**, using the table below. Record the domains with no hypothesis; they still get one question, because an interview that only asks about what the team already suspects cannot find anything else.

| TDF domain | COM-B component | Ask about |
|---|---|---|
| Knowledge | Capability, psychological | what the person knows about the behavior, why it is recommended, what the steps are |
| Skills | Capability, psychological or physical | whether they have done it, how it went, what was hard to do |
| Social/professional role and identity | Motivation, reflective | whether doing it fits their role as parent, worker, member of the community |
| Beliefs about capabilities | Motivation, reflective | confidence they could do it, under what conditions |
| Optimism | Motivation, reflective | whether they expect things to go well if they try |
| Beliefs about consequences | Motivation, reflective | what they expect to happen, good or bad, if they do or do not |
| Reinforcement | Motivation, automatic | what has followed past attempts: praise, reward, cost, nothing |
| Intentions | Motivation, reflective | whether they have decided to do it, how firmly |
| Goals | Motivation, reflective | how it ranks against the other things they want to do |
| Memory, attention and decision processes | Capability, psychological | whether they forget, when it comes to mind, how they decide on the day |
| Environmental context and resources | Opportunity, physical | time, money, materials, distance, services, interruptions |
| Social influences | Opportunity, social | who approves, who disapproves, what others around them do |
| Emotion | Motivation, automatic | feelings that come up: fear, shame, worry, relief |
| Behavioral regulation | Capability, psychological | plans, reminders, routines they use or could use |

3. **Write the opening**: the purpose in plain words, a consent placeholder (this skill does not write consent text; the team's approved script goes there), and a reconstruction question ("think about the last time you were due to <behavior>; walk me through that day"). Ask for a concrete episode before any opinion, because recall of a specific day surfaces environment, habit, and emotion that abstract questions miss.
4. **Write one to three questions per domain.** Give two or three to domains carrying a hypothesis and one to the rest. Each question is open-ended, asks one thing, and does not name the barrier it is looking for. Label each with its domain, its COM-B component, and the hypothesis it tests, or "discovery" if none.
5. **Add one or two probes per question** ("can you give me an example?", "what happened next?", "who else was involved?"). Probes get the detail; the question only opens the topic.
6. **Order the questions as a conversation**, grouped by episode and topic, not by domain. The domain is the coding frame for later analysis, not the running order; a guide read domain by domain sounds like a checklist and gets checklist answers. Keep the domain label on each question so coding stays deductive.
7. **Mark every local referent and translation risk**: the people whose opinion matters, services, tools, costs, and any word (such as "goal" or "plan") that may not carry across languages. Put them in brackets for the local team to fill.
8. **Write the closing**: anything we missed, what one change would make it easier, thanks, what happens next. Then count the questions against the interview length and cut, starting with discovery questions in the domains that overlap most (Reinforcement, Goals, Behavioral regulation).
9. **Produce the domains-to-hypotheses map** so a reader can see which hypotheses the guide tests, with which questions, and which domains are discovery-only.
10. **Stop here.** Recommend piloting with two respondents before fieldwork. `synthesize-interview-findings` codes the transcripts against the domains; this skill does not analyze.

See `references/worked-example.md` for a complete run on fertilizer top-dressing timing in Western Kenya, and `references/evidence-notes.md` for the sources.

## Output template

```markdown
# TDF interview guide: <short name of the behavior>

**Target behavior (AACTT):** Action <...>; Actor <...>; Context <...>; Target <...>; Time <...>
**Respondents:** <who> | **Interviewer:** <who> | **Length:** <minutes> | **Language:** <...>
**Hypotheses under test (from decompose-comb-barriers):** H1 <...>; H2 <...>; H3 <...>

## Opening (about <n> minutes)
- Purpose, in plain words: <...>
- [CONSENT: insert the team's approved consent script here; do not start without it]
- Reconstruction: "Think about the last time you <were due to do the behavior>. Walk me through that day, from <start point>."

## Questions, in running order
### <Episode or topic block 1>
1. "<open question>" [<TDF domain>; <COM-B component>; tests <H# or discovery>]
   - Probe: "<...>"
   - Probe: "<...>"
### <Episode or topic block 2>
...

## Closing (about <n> minutes)
- "Is there anything about <behavior> we have not talked about that you think matters?"
- "If one thing changed to make this easier, what would it be?"
- Thanks; what happens next with what they told us.

## Domains-to-hypotheses map
| TDF domain | COM-B component | Hypothesis tested | Question numbers |
|---|---|---|---|
| Knowledge | Capability, psychological | <H# or discovery> | <...> |
| <... one row per domain, all 14 ...> | | | |

## Local adaptation notes
- <bracketed referent to fill, and who fills it>
- <translation risk and the plain-language alternative>

## What to check before relying on this
- Pilot with two respondents; drop any question that gets the same answer whichever hypothesis is true
- <the assumption most likely to be wrong, such as the respondent group or the interview length>
```

## Where it goes wrong

- **Questions that name their own answer.** "Is it because you don't have time?" tests nothing; a respondent agrees with whatever is offered. Every question opens a topic and the probes get the detail. If a question contains the hypothesis it tests, rewrite it.
- **The guide runs domain by domain.** Fourteen headings in framework order turn the interview into a checklist, and respondents answer in checklist mode. Group by episode and topic; keep the domain as a label.
- **Treating the 14 domains as separate.** They overlap by design; Huijg et al. (2014) could not discriminate Reinforcement, Goals, and Behavioral regulation items from the rest. Do not write three strained questions to force a distinction; one question can carry two domain labels, and coding resolves it later.
- **Running on an unspecified behavior.** "Adherence", "uptake", or a behavior with "and" in it produces questions about whichever half the drafter pictured. Insist on AACTT before writing.
- **Importing the UK referents.** Published TDF question sets ask about "your manager", "the guideline", "your professional role". Pasted into a community setting these are meaningless or insulting. Every referent is a bracket for the local team.
- **Writing survey items.** Yes/no and scale questions belong in a questionnaire. If the team wants structured comparison across many short interviews, send them to `draft-barrier-analysis-questionnaire`; do not hybridize.

## When to bring in a specialist

Tell the user to consult an experienced qualitative researcher who knows the setting, plus the relevant ethics review body, when:
- The behavior involves clinical, legal, or safety risk, or a stigmatized topic (sexual health, violence, substance use, household authority), because the questions and the consent process need review before anyone is interviewed
- Respondents include children, or the interviews will run in a language or community no one on the team knows, because the local referents and the probing style then need to be set by someone who does
- The team cannot say what the transcripts will be coded against; a guide with no analysis plan produces transcripts nobody reads

Bring them: the AACTT statement, the hypothesis list, the draft guide with its domain labels, and the respondent and interviewer plan.
