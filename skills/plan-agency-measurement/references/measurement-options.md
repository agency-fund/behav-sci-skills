# Choosing measures (steps 2 to 4)

Use this to fill each focus cell of the 2x2 agency framework with an on-platform and an off-platform measure. The instruments named below are candidates to look up, adapt, and test, not prescriptions; none has been validated for WhatsApp or chat delivery in a low-income setting (see `evidence-notes.md`). Quote items only from a source opened in the current session, or from this file (the few items quoted here were checked against their sources when the skill was drafted), or label them as drafted examples; never reproduce a scale from memory. Full citations are in `evidence-notes.md`.

## On-platform and off-platform data

| | On-platform | Off-platform |
|---|---|---|
| Examples | In-app or in-chat micro-surveys, conversation logs, interaction patterns, task behavior | Phone or in-person surveys, interviews, observation, administrative records, artifacts (pitches, plans, farm records) |
| Strengths | Cheap, in the moment, large samples, behavior rather than recall | Room for multi-item instruments, context, and outcomes beyond the tool |
| Limits | Short; answered mostly by engaged users; asked by the tool itself, so open to halo and social desirability; blind to what happens outside the tool | Costly; smaller samples; recall bias; interviewer effects |
| Rules of thumb | No more than three items per in-app check, woven into the chat flow (AI Evaluation Playbook); prompts triggered by an event, such as after a decision or setback, rather than at app open (van Berkel et al., 2018); conversational delivery in a casual tone reduced satisficing in one experiment (Kim et al., 2019) | Adapt an existing instrument where one fits; time it against the program calendar; link it to a downstream outcome the team trusts |

Keep each in-app prompt short: in experience sampling, longer questionnaires cut compliance and data quality while more frequent prompts did not (Eisele et al., 2022). Benchmark single items: single items in repeated sampling correlated .24 to .61 with multi-item scales and kept most of their predictive validity (Song et al., 2023, in a US clinical sample), so run a multi-item version off-platform at baseline and endline to check that the one-item pulse tracks it.

## Candidates by cell of the 2x2 agency framework

### Agency with respect to the end goal, internally experienced (thoughts and feelings)
- **Domain-specific self-efficacy:** "can do" items (a judgment of capability, not an intention) graded by difficulty for the tasks the tool supports, following Bandura's guide for constructing self-efficacy scales (Bandura, 2006; chapter not accessed, author to confirm). One item in-app; a short battery off-platform. General scales such as the 10-item General Self-Efficacy Scale are better kept as covariates, and that scale's structure differs across countries (Scholz et al., 2002; Villegas Barahona et al., 2018).
- **Goal-setting and the user's own goal:** whether the user has a goal of their own, in their words, captured at intake so later attainment can be judged against it (Kizilcec et al., 2017). Ibrahim & Alkire (2007) offer short items: "Would you like to change anything in your life?", "What would you most like to change?", and "Who do you think will contribute most to any change in your own life?" (quoted from the working paper; author to confirm against the article). Adding the tool as an answer option turns the last into a tool-attribution item.
- **Why the user pursues the goal:** Relative Autonomy Index items (acting to avoid trouble, to please others, or because one values it). In low-literacy settings, a two-type version or short vignettes worked better than the original statements (Vaz, Pratley & Alkire, 2016; Donald et al., 2020).
- **Hope:** the 6-item State Hope Scale measures agency and pathways thinking toward goals and is designed to move with events (Snyder et al., 1996); hope has been measured without self-report, through children's drawings, in Indonesia (Glewwe, Ross & Wydick, 2018).
- **Perceived control over one's life:** the World Values Survey item on freedom of choice and control (1 to 10) is a common benchmark, but it correlates weakly with similar items and behaves differently across countries and genders (Donald et al., 2020). Use it as a benchmark, not the outcome.
- Caution: felt confidence can rise without capability; self-reported learning was over-optimistic in Bastani et al. (2025).

### Agency with respect to the digital tool, internally experienced (thoughts and feelings)
- **Three confidence probes** after a task (Lee et al., 2025): confidence in doing the task without the AI, confidence in the AI doing it, and confidence in evaluating the AI's output. A widening gap between confidence in the AI and confidence in oneself is a warning sign.
- **Felt ability to understand, question, or reject advice:** a one-item check after the tool gives a critique or recommendation.
- **Trust in the tool** (12-item trust-in-automation scale, Jian et al., 2000) or **self-reported dependence on AI** (5-item scale validated with Peruvian medical students, Morales-García et al., 2024; 8-item chatbot dependence scale, Zhang et al., 2025). These were built with students or office workers, not low-literacy users, and self-reported dependence tracks behavior only weakly (Parry et al., 2021, report r = 0.25 between problematic-use scales and logs).
- **Why the user follows the tool:** Relative Autonomy Index-style reason items about the tool ("I follow the app's advice because I would get in trouble otherwise / others expect me to / I agree with it"). These tell endorsed delegation from compliance or drift.
- **AI literacy** as a moderator: the self-efficacy and self-management facets of the Meta AI Literacy Scale (Carolus et al., 2023; 300 German-speaking adults) are closest to agency over the tool.

### Agency with respect to the end goal, externally expressed (choices and actions)
- **Goal progress against the user's own goal,** from logs where visible and from follow-up surveys or records where not.
- **Unassisted outcomes:** performance or decisions when the tool is removed or unavailable. Assisted performance is not capability (Bastani et al., 2025).
- **Rubric-rated work or observation:** a business pitch, a lesson plan, a farm plan, or classroom behavior rated against anchors by trained raters, ideally linked to a downstream outcome such as earnings, yields, or clinic attendance.
- **LLM-coded processes in conversation logs:** setting and revising goals, weighing options, persisting after setbacks (Bandura's four processes make a natural codebook). Experimental; see the LLM protocol in `validation.md`.
- **Decision-making items** ("who decided ...?") where the goal involves household or community decisions. Being the decision-maker signals agency only if the person wants to be involved; add items on whether they were consulted and whether they could decide if they wished (Alkire, 2008; Donald & Hernandez-de-Benito, 2021). Ask about specific situations: in Haryana, India, five concrete situational questions matched coded qualitative interviews as well as 63 candidate questions did (Jayachandran, Biradavolu & Cooper, 2023), and in Bangladesh the standard health-decision question disagreed with concrete scenario questions (Glennerster, Walsh & Diaz-Martin, 2018). These items can put respondents at risk; see the skill's specialist section.

### Agency with respect to the digital tool, externally expressed (choices and actions)
- **Appropriateness of reliance:** where tasks have a right answer, record the user's own answer first, then show the AI's advice, then record the final answer. Relative AI reliance (switching to the AI when it was right) and relative self-reliance (keeping one's own answer when the AI was wrong) both range from 0 to 1 (Schemmer et al., 2023).
- **Share of answer-seeking messages:** in Bastani et al. (2025), 67% of first messages in the unguarded arm were answer-seeking against 37% with the guarded tutor.
- **Asking versus doing:** whether users seek information for their own decision or ask the tool to produce the output (Chatterji et al., 2025, validated this taxonomy against human coders); or augmentation versus automation modes (Handa et al., 2025).
- **Questioning, adapting, or rejecting advice:** turns where the user pushes back, modifies a suggestion, or chooses differently.
- **Disempowerment risk in conversations:** reality, value-judgment, and action distortion, amplified by reliance and dependency (Sharma et al., 2026), for tools that give value-laden advice. Their rubric was checked against one human labeler on 50 conversations, so revalidate locally.
- **Usability observation or interviews** on how users work with the tool, including outside it (copying text into other apps, sharing with family).

## Moments in the user journey

| Moment | Good for | Watch for |
|---|---|---|
| Intake or first session | The user's own goal, in their words; baseline self-efficacy | First-session novelty |
| Right after a decision point, critique, or recommendation | Felt control; agreement or disagreement with the tool; confidence probes | Asking too often; the tool asking about itself |
| After a setback (a failed attempt, bad weather, a missed visit) | Persistence; perceived control under pressure | Small numbers; sensitive moments |
| When the tool is unavailable or removed | Unassisted capability; dependence | Needs planning in the program design |
| End of a program cycle | Multi-item batteries; goal attainment; records | Attrition of the least engaged |

## Reducing reporting bias

A tool that promotes agency invites users to report more of it. From the J-PAL guide (Glennerster, Walsh & Diaz-Martin, 2018) and related work:
- Ask about specific, recent situations, nondirectively, without signaling what the study hopes to find (Brenner & DeLamater, 2016, found directive questions produced over-reporting where nondirective ones did not).
- Frame sensitive questions about someone similar ("for a woman like you in this village ..."), or use vignettes, games, or self-interview technology for low-literacy respondents.
- Collect a short social desirability scale at baseline and test whether effects differ for high scorers, as Dhar, Jain & Jayachandran (2022) did in India.
- Keep enumerators the same across arms, and self-administer where possible; enumerators explained 9% of the variance in noncognitive scores in Kenya (Laajaj & Macours, 2021).
- Do not assume indirect methods are more accurate; a list experiment in Peru found no under-reporting relative to direct questions (Agüero & Frisancho, 2022).

## AI-based measurement tools

- **LangExtract** (Google): open-source library that applies a plain-language extraction prompt with examples to large volumes of text and maps every extraction back to its exact location in the source, which makes human auditing easy. The announcement reports no accuracy figures.
- **GABRIEL** (OpenAI): library for rating attributes of text with GPT models; the working paper reports correlations with human consensus from about 0.55 to 0.8 depending on the construct, and some tasks near chance (Asirvatham et al., 2026, OpenAI-funded, not peer reviewed).
- **ThoughtTrace:** a dataset pairing real conversations with users' private reasons and reactions; transcripts under-specify what users intend, so in-the-moment prompts ("why did you ask that?") add information logs cannot (Jin et al., 2026).

All of these need the validation protocol in `validation.md` and privacy safeguards before use.

## Digital traces: name the error before trusting the signal

Using the total error framework for digital traces (Sen et al., 2021), ask of every log signal:
- Who is not on the platform, and who on it never produces this signal?
- Can the platform's design produce this behavior at all? (A chatbot that never asks for the user's answer first cannot show self-checking.)
- Does one account stand for one person? Shared phones are common.
- Was the signal labeled by a model, and has that labeling been checked?
