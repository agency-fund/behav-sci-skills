---
name: define-agency-construct
description: >-
  Use when a team building or evaluating a digital or AI tool (chatbot, AI
  tutor or mentor, WhatsApp assistant) wants to measure, claim, or improve
  its users' agency but has not said precisely what agency means for those
  users: "how do we measure agency for our app?", "is this real
  empowerment or just engagement?", "does our AI make people more capable
  or more dependent?". Also use when a theory of change or board report
  says the tool builds agency, empowerment, self-efficacy, or autonomy and
  the only evidence is usage numbers, even if nobody says "agency". Turns
  the team's own meaning into constructs matched to established theory and
  placed on the 2x2 agency framework: forms (the end goal or the digital
  tool) and manifestations (thoughts and feelings, or choices and actions).
  Do not use when the constructs are named and the question is how to
  measure them; use plan-agency-measurement. Not for a program targeting
  one offline behavior (define-key-behavior) or checking the AI's answers
  (design-golden-dataset).
license: CC-BY-4.0
metadata:
  title: Define what agency means for a tool's users
  type: atomic
  stage: define
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: mixed-evidence
  tags: "agency, social-cognitive-theory, self-determination-theory, measurement, ai-eval"
  consumes: "ai-product-account, theory-of-change"
  produces: "agency-definition"
---

## What it does

Turns what a team means by its users' agency into a precise definition matched to established theory, ready to measure.

Teams that say their tool builds agency usually have something specific in mind ("farmers feel confident deciding what to plant") but have not written it down, or have written it too abstractly to measure ("unlock young people's potential"), or are counting engagement instead. This skill asks what the team means, matches each part to an established construct and the theory it comes from (confidence about a task is self-efficacy, from Bandura's social cognitive theory), and places the constructs on the 2x2 agency framework so the team can see what their definition covers and choose what to focus on. The result is a definition document that `plan-agency-measurement` takes as input.

## When to use it

### Use it when
- A team asks "how do we measure agency for our chatbot / AI tutor / mentor / assistant?" and has not said what agency means for its users
- Someone asks whether an AI tool makes users more capable or more dependent, or whether it is "real empowerment or just engagement"
- A theory of change, grant, or board report claims the tool builds agency, empowerment, self-efficacy, autonomy, or confidence, and the evidence offered is active users, messages, retention, or star ratings
- Agency appears in a theory of change only as an abstract aim ("unlock potential", "empower youth") and the team needs to pin it down
- A team's idea of agency involves decisions made with others (a spouse, parents, the community) and they are unsure how to count them

### Do not use it when
- The constructs are already named and the question is how to measure them, which instruments or items to use, or whether a proposed measure will hold up; use `plan-agency-measurement`
- The question is whether the AI's answers are accurate, safe, or on-policy; use `design-golden-dataset`
- The team needs to decide which evaluation to run next or whether they are "ready for an RCT"; use `choose-ai-eval-level`
- The tool targets one offline behavior rather than agency (for example, attending a clinic visit); use `define-key-behavior`
- The user asks a definitional question ("what does Sen mean by capability?"); answer it directly in a few sentences

## Before you start

Ask one question at a time and offer a suggested answer with each, inferred from what the user has already said ("My guess: farmers making their own planting decisions after a bad season. Is that right?"), so it reads as coaching rather than a form. Do not ask anything the user's message, documents, or theory of change already answer.

1. **Required.** The tool and its users: what the tool does, through which channel, who uses it, where, in what language, and under what constraints (literacy, connectivity, shared phones, who else is in the room).
2. **Required.** The end goal in users' lives that the tool serves, off the platform, and what a better outcome would look like there.
3. **Required.** What the team means by agency here: what would a user with more of it think, feel, choose, or do differently? If they cannot say, offer one example per cell of the 2x2 agency framework for this tool and ask which comes closest.
4. Optional. What it would look like if the tool were wearing agency down.
5. Optional. The metrics the team tracks now, and the theory of change or user funnel if one exists.
6. Optional. Who else shapes users' decisions (spouse, parents, teachers, community, gatekeepers). Ask whenever users are women, girls, or minors or the goal involves household decisions; otherwise propose an answer and check it.

A required answer is missing only when it is neither stated nor reasonably inferable; when you infer it, say so in a line so the team can correct it, alongside the one question you do ask. If 1 or 2 is missing, ask and stop. Question 3 is the center of the skill: do not substitute your own definition for the team's; offer one only as a suggestion to react to. If 4 is missing, propose erosion signs from the tool type and ask the team to confirm them. If 5 is missing, leave usage metrics out of the document rather than guessing what the dashboard holds.

## What it draws on

- Wu, Z., Goldberg, B., & Xu, R. (2026, July 1). *Measuring agency in a digital context*. The Agency Fund (Substack), with Google Jigsaw. https://theagencyfund.substack.com/p/measuring-agency-in-a-digital-context
- The Agency Fund. (2026). *ask-agency-measurement* (the Claude skill this one and `plan-agency-measurement` replace). https://github.com/agency-fund/taf-skills/tree/main/ask-agency-measurement
- Bandura, A. (2001). Social cognitive theory: An agentic perspective. *Annual Review of Psychology, 52*(1), 1–26. https://doi.org/10.1146/annurev.psych.52.1.1
- Alkire, S. (2008). *Concepts and measures of agency* (OPHI Working Paper No. 9). University of Oxford. https://ophi.org.uk/publication/WP-09
- Kabeer, N. (1999). Resources, agency, achievements: Reflections on the measurement of women's empowerment. *Development and Change, 30*(3), 435–464. https://doi.org/10.1111/1467-7660.00125
- Donald, A., Koolwal, G., Annan, J., Falb, K., & Goldstein, M. (2020). Measuring women's agency. *Feminist Economics, 26*(3), 200–226. https://doi.org/10.1080/13545701.2019.1683757
- Ryan, R. M., & Deci, E. L. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. *American Psychologist, 55*(1), 68–78. https://doi.org/10.1037/0003-066X.55.1.68
- Beacock, I., Xu, R., Murray, L., Anson, P., Goldberg, B., Kumar, D., Lee, J., Park, R., & Sinha, A. (2026). *AI usage patterns are shaped by perceived gains in human agency* (arXiv:2607.02313). https://doi.org/10.48550/arXiv.2607.02313
- Bennett, D., Metatla, O., Roudaut, A., & Mekler, E. D. (2023). How does HCI understand human agency and autonomy? *CHI 2023*. https://doi.org/10.1145/3544548.3580651
- Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50_30392
- Cavazzoni, F., Fiorini, A., & Veronese, G. (2022). How do we assess how agentic we are? A literature review of existing instruments to evaluate and measure individuals' agency. *Social Indicators Research, 159*(3), 1125–1153. https://doi.org/10.1007/s11205-021-02791-8

The blog supplies the working definition ("a person's capability to navigate toward the future they want"), the two distinctions behind the 2x2 agency framework, and the three frameworks it names (Bandura, Sen, Jigsaw); the earlier skill supplies the coaching style. Bandura gives the four agentic processes, self-efficacy, and proxy agency, which is why relying on a tool is not automatically lost agency. Alkire's reading of Sen separates ability from autonomy and control from effective power; Kabeer and Donald et al. supply the women's agency decompositions (resources, agency, achievements; goal-setting, sense of agency, acting on goals), and Donald et al. find internal and external indicators correlate only weakly, which is why the framework separates the two manifestations. Self-determination theory distinguishes acting from one's own values from acting under pressure. Beacock et al. is the probable source of Jigsaw's five dimensions (it says "relational" where the blog says "social"; author to confirm). Bennett et al. and Lee & See supply the vocabulary for agency with respect to the digital tool. Cavazzoni et al. found almost every agency study used a different instrument, which is why the definition is built locally rather than borrowed whole. The matching table in `references/frameworks.md` is a judgment call this skill adds. Full citations, verification status, and further sources are in `references/evidence-notes.md`.

**WEIRD skew:** Bandura's theory, self-determination theory, and the human-AI literature come mostly from WEIRD samples, and Jigsaw's ethnography covered the US, Germany, and Singapore. The capability approach and the women's agency work were built in low- and middle-income settings (Donald et al. in Uganda and 20 Sub-Saharan countries; Alkire's indicators). Individualistic framings of autonomy can misread settings where decisions are made jointly; check what counts as agentic with the users themselves.

**Replication status:** Mixed. The frameworks are long-standing and widely used, but there is no agreed definition of agency (Cavazzoni et al.), and agency with respect to AI tools rests on qualitative work and preprints.

## How to do it

1. **Get the context and the team's own meaning** (Before you start). Record their words verbatim; they go into the document.
2. **Set engagement aside, if it came up.** If the team offers usage, retention, or ratings as evidence of agency, say in one line what each measures instead (engagement, satisfaction, a funnel stage) and why it is not agency: heavy use can coexist with no change in what people decide or do. Skip this step if nobody raised it.
3. **Make the meaning concrete.** If it is abstract ("unlock potential"), ask what a user with more agency would think, feel, choose, or do differently, in which situation, by when. Each part should name whose agency, over which decisions or goals, in which part of life off the platform. Stop when each part points at something a person could report or someone could observe. If the users span settings where agency may mean different things (two countries, two languages), say where the definition may need to differ by setting.
4. **Match each part to an established construct and its theory.** "Feel confident deciding what to plant" is agricultural self-efficacy (Bandura's social cognitive theory); "decides for herself" is autonomy or decision-making (Sen's capability approach, Donald et al.); "bounces back after a bad season" is self-reactiveness or hope (Bandura, Snyder). Define each construct in one plain line. Where several theories fit, name the one closest to what the team said, and mention an alternative only when it would change what gets measured. Where nothing fits, keep the team's wording as a local construct and say so; do not force a framework onto a meaning it does not hold, especially where decisions are made jointly. See `references/frameworks.md`.
5. **Place the constructs on the 2x2 agency framework.** Its forms of agency are agency with respect to the end goal (progress on outcomes users value, through, around, or beyond the tool) and agency with respect to the digital tool (understanding, questioning, adapting, and deciding when to rely on it). Its manifestations of agency are internally experienced (thoughts and feelings) and externally expressed (choices and actions). Show the grid with the team's constructs in place and each open cell marked with one example of what could go there for this tool.
6. **Ask what to focus on.** The framework is a thinking aid, not a checklist. The team chooses which cells matter for their goal and their worry, and why. Record in one line what the open cells would catch that this focus will not (for example, felt confidence rising while dependence on the tool grows), and leave the choice with the team. If the team's first message already answers the required questions, do not stop here to ask: draft the full document with a proposed focus and proposed erosion signs, each marked "proposed; confirm", and ask the team to confirm or change them.
7. **Write what erosion would look like** in the chosen cells: observable signs that the tool is wearing agency down, such as asking the tool to decide what the user used to decide, or being unable to act when it is unavailable. Relying on the tool is not erosion by itself; it is agency exercised through a proxy when the user chose it and could act otherwise.
8. **Write the definition document and hand it on.** Tell the user how to take it to `plan-agency-measurement`: paste or attach the document and say which decision the measures will support.

See `references/worked-example.md` for a complete run on a hypothetical AI mentor for student entrepreneurs.

## Output template

```markdown
# Agency definition: <tool>

**Context:** <users, the end goal in their lives, and the tool's role, in one or two sentences>
**In your words:** "<the team's own description of agency>"
**Working definition:** <one or two sentences stating the team's meaning precisely: whose agency, over which decisions or goals, where>
**Not agency:** <only if usage metrics were offered as evidence: each metric and what it measures instead>

## Your definition, matched to theory
| # | What you said | Construct | Theory |
|---|---|---|---|
| 1 | "<their words>" | <construct, defined in one plain line> | <theory or framework: component; or "local construct: no established match"> |

## Where it sits in the 2x2 agency framework
| | With respect to the end goal: <goal> | With respect to the digital tool: <tool> |
|---|---|---|
| **Internally experienced** (thoughts and feelings) | <construct name (#), or "open: e.g., <example>"> | <...> |
| **Externally expressed** (choices and actions) | <...> | <...> |

**Focus:** <the cells the team chose, and why, in their words>
**Not covered by this focus:** <what the open cells would catch that this focus will not>
**Erosion would look like:** <observable signs in the chosen cells that the tool is wearing agency down>

## Next step
To design measures, give this document to plan-agency-measurement and say which decision the measures will support: "<one-line instruction the user can paste>"
```

## Where it goes wrong

- **Not defining agency at all when agency matters to the theory of change.** The model treats "agency" as self-explanatory and moves straight to measures or to the tool's features. If agency is a link in the theory of change, it needs a definition before anything else.
- **Defining agency superficially.** Engagement, retention, satisfaction, or "users chose to use the tool" stand in for agency because they are what the team already has. Usage can rise while nothing changes in what people decide or do.
- **Defining agency too abstractly to measure.** "Empowerment", "unlocking potential", or "voice" with no answer to "what would a user think or do differently?" leaves nothing a survey, log, or observer could pick up.
- Out of scope: choosing measures, instruments, or items (`plan-agency-measurement`), and redesigning the tool to support agency.

## When to bring in a specialist

Tell the user to bring in a specialist when:
- The team needs a domain-specific definition of agency (in farming decisions, learning, health, livelihoods) and is unsure how to define it, or the matching step finds no good theoretical match; bring in a psychologist or economist who has defined or measured agency in that domain.
- Agency here is multifaceted, culturally situated, or contested (decisions made jointly within families, norms that limit who may decide, several theories pulling in different directions), so defining it well takes a good grasp of the theories; bring in a psychologist, economist, or anthropologist with that theoretical background and experience in this setting.

Bring them: the definition document, the team's own words about agency, a description of the users and setting, and the theory of change.
