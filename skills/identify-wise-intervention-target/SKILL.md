---
name: identify-wise-intervention-target
description: >-
  Use when a team is drawn to a brief psychological intervention (a
  growth-mindset message, a belonging story, a values affirmation) and needs
  to know first which question the audience is asking themselves:
  "do people like me belong here?", "can I do this?", "am I a good person?",
  or "are these institutions on my side?". Also use when field data show
  people have the means to act but read the situation in a way that stops
  them ("is this a mindset problem or a real barrier?"). Names the one
  meaning-making question a wise intervention would have to answer, tests
  that the barrier is not structural, checks that the setting can deliver
  what the message promises, and states the replication record honestly. Do
  not use when the barrier is cost, access, time, or information; use
  select-intervention-levers. Not for drafting the exercise
  (draft-values-affirmation, draft-belonging-story,
  adapt-growth-mindset-message), and not for a Self-Determination Theory
  needs assessment, a different framework with its own skill.
license: CC-BY-4.0
metadata:
  title: Find the question a wise intervention must answer
  type: atomic
  stage: diagnose
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: mixed-evidence
  tags: "wise-interventions, belonging, growth-mindset, self-affirmation"
  consumes: "comb-barrier-hypotheses, barrier-diagnosis"
  produces: ""
---

## What it does

Names which meaning-making question a brief psychological intervention would have to answer for this audience before any such intervention is drafted.

A wise intervention, in Walton and Wilson's sense, is a short, precise exercise that changes how people interpret themselves or their situation, so that a self-reinforcing cycle (a setback read as "I do not belong", then withdrawal, then more setbacks) can turn. It can only work when the barrier is a problem of meaning rather than of means, and only when the setting then offers what the new interpretation expects; the technique families it draws on also have uneven replication records. This skill makes those checks and names the question. It does not write the exercise.

## When to use it

### Use it when
- A team proposes a mindset message, a belonging story, or an affirmation and nobody has said which question the audience is asking themselves
- `decompose-comb-barriers` returned a Motivation (reflective) hypothesis ("does not believe the benefit applies to people like them") that field answers support, and the next question is which kind of belief
- Field data show people with the same resources behaving differently depending on how they read a setback ("math is not for people like me", "the clinic staff look down on us")
- Someone asks "is this a mindset problem or a real barrier?" or "which of these psychological interventions fits our situation?"

### Do not use it when
- The barrier is cost, access, time, information, or a process, so that removing it would fix the behavior; that is `select-intervention-levers`
- The question is already named and the team wants the exercise; that is `draft-values-affirmation` (self-integrity), `draft-belonging-story` (belonging), or `adapt-growth-mindset-message` (ability)
- The team wants to assess whether people's needs for autonomy, competence, and relatedness are met (Self-Determination Theory); that is a different framework with its own separate skill, and this skill names a meaning-making question, not a need
- No field data on how the audience reads the situation exist and none can be collected, so this skill would only guess; run `decompose-comb-barriers` and answer its diagnostic questions first

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The behavior as who, what, when, and the barrier diagnosis or COM-B hypotheses, with whatever field evidence exists for the Motivation (reflective) ones.
2. **Required.** How the audience reads the situation, in their words: quotes from interviews, open-ended survey answers, or field notes, especially about setbacks, about "people like me", and about the institution. Without these the skill can list candidate questions only.
3. **Required.** What the setting actually offers after any message: can people improve (feedback, a second attempt, support), can they belong (peers and staff who include them), is the institution in fact on their side? This is the affordance check; it needs facts, not hopes.
4. Optional. The stakes and scale of the decision (a pilot with 200 people, or a regional rollout) and whether a test is planned.
5. Optional. Literacy and delivery constraints (oral or written; group or individual).

If 1 is missing, ask and stop. If 2 is missing, ask once; if no data can be collected, produce the candidate-question table with the structural test and mark the target "not named: no audience interpretations available". If 3 is missing, ask once; if unknown, name the target but mark the affordance "unverified" and say the intervention should not be built until it is checked.

## What it draws on

- Walton, G. M., & Wilson, T. D. (2018). Wise interventions: Psychological remedies for social and personal problems. *Psychological Review*, 125(5), 617–655. https://doi.org/10.1037/rev0000115
- Walton, G. M., et al. (2023). Where and with whom does a brief social-belonging intervention promote progress in college? *Science*, 380(6644), 499–505. https://doi.org/10.1126/science.ade4420 (Crossref lists an erratum, 10.1126/science.ads9718, 2024; author to check what it changes)
- Cohen, G. L., & Sherman, D. K. (2014). The psychology of change: Self-affirmation and social psychological intervention. *Annual Review of Psychology*, 65, 333–371. https://doi.org/10.1146/annurev-psych-010213-115137
- Hall, C. C., Zhao, J., & Shafir, E. (2014). Self-affirmation among the poor: Cognitive and behavioral implications. *Psychological Science*, 25(2), 619–625. https://doi.org/10.1177/0956797613510949
- Hanselman, P., Rozek, C. S., Grigg, J., & Borman, G. D. (2017). New evidence on self-affirmation effects and theorized sources of heterogeneity from large-scale replications. *Journal of Educational Psychology*, 109(3). https://doi.org/10.1037/edu0000141
- Baranov, V., Haushofer, J., & Jang, C. (2020). Can positive psychology improve psychological well-being and economic decision-making? Experimental evidence from Kenya. *Economic Development and Cultural Change*. https://doi.org/10.1086/702860
- Yeager, D. S., et al. (2019). A national experiment reveals where a growth mindset improves achievement. *Nature*, 573, 364–369. https://doi.org/10.1038/s41586-019-1466-y
- Sisk, V. F., Burgoyne, A. P., Sun, J., Butler, J. L., & Macnamara, B. N. (2018). To what extent and under which circumstances are growth mind-sets important to academic achievement? Two meta-analyses. *Psychological Science*, 29(4), 549–571. https://doi.org/10.1177/0956797617739704
- Macnamara, B. N., & Burgoyne, A. P. (2023). Do growth mindset interventions impact students' academic achievement? A systematic review and meta-analysis with recommendations for best practices. *Psychological Bulletin*, 149(3–4), 133–173. https://doi.org/10.1037/bul0000352
- Outes-León, I., Sánchez, A., & Vakis, R. (2020). The power of believing you can get smarter: The impact of a growth-mindset intervention on academic achievement in Peru. World Bank Policy Research Working Paper 9141. https://doi.org/10.1596/1813-9450-9141
- Ganimian, A. J. (2020). Growth-mindset interventions at scale: Experimental evidence from Argentina. *Educational Evaluation and Policy Analysis*, 42(3), 417–438. https://doi.org/10.3102/0162373720938041

Walton and Wilson describe wise interventions as targeting a specific meaning people make of themselves or their situation, so the remedy is precise rather than broad. This skill reduces that to four questions a program audience may be asking: belonging ("do people like me belong here?"), ability ("can I do this, can I get better at it?"), self-integrity ("am I a good person, am I worth something here?"), and trust ("are these institutions on my side?"). Three have a technique family and a skill in this library (belonging stories, growth-mindset messages, values affirmation); trust has none yet. The 2023 belonging study established the condition this skill makes mandatory: the intervention raised full-time first-year completion only where the group was afforded opportunities to belong, and the 2019 mindset study likewise found effects where peer norms supported the message. The judgment calls this skill adds: the structural test (if removing a material barrier would fix the behavior, the target is not here), one primary question only, a mandatory affordance check, and a per-family replication statement in every output.

**WEIRD skew:** Nearly all the evidence is from US students (college belonging, school mindset) and US low-income adults (affirmation). Outside the US the record is thin and mostly null. Check locally whether the four questions make sense in the local idiom, whether "you can improve" is credible in a system with one-shot examinations, and whether an oral format is needed where literacy is low. **Non-WEIRD evidence:** Kenya (Kibera, Nairobi; Baranov, Haushofer & Jang 2020): N = 220 adults, affirmation bundled with gratitude and aspirations exercises; gratitude rose 0.3 SD; no effect on wellbeing, aspirations, cognitive control, or discounting. Peru (Outes-León, Sánchez & Vakis 2020): a 90-minute growth-mindset session for more than 50,000 students at about $0.20 per pupil; math gains reported as 0.14 SD by the World Bank, 0.05 to 0.25 depending on estimator, larger outside Lima, and about 0.2 SD in the World Bank summary; the figures conflict, so quote the range. Argentina (Ganimian 2020; Salta, 202 schools): null, with small effects ruled out.

**Replication status:** Contested, and different per family, so the output must say which family it means. Belonging: replicated with conditions (26,911 students at 22 institutions; effect only where belonging was afforded). Self-affirmation: contested; a large-scale school replication ruled out effects larger than 0.10; a US soup-kitchen study found gains in executive control, fluid intelligence, and willingness to seek benefits, with no effect among the wealthy; Kibera was null on its targeted outcomes; a reported failed replication (Protzko & Aronson 2016) is unverified, author to confirm. Growth mindset: contested; d = 0.08 across k = 43 studies and N = 57,155, about 0.19 for high-risk and 0.34 for low-SES students on limited evidence; a 2023 review found 94% of interventions confounded and larger effects reported by authors with financial incentives. Trust: no evidence in the sources this skill draws on.

## How to do it

1. **Carry over the behavior and the barrier evidence** verbatim at the top, so the target is visibly attached to a field finding about Motivation, not to the program's theory of change.
2. **Tabulate how the audience reads the situation**, in their words, from the interview data: statements about themselves, about "people like me", about the institution, and about what a setback means. Three to six interpretations, each with how many respondents said it.
3. **Run the structural test on each interpretation.** Ask: if the material barrier behind this were removed (cost, access, time, information, a process), would the behavior follow? If yes, mark it structural and route it to `select-intervention-levers`; it is not a wise-intervention target however psychological it sounds. If people in the same material situation differ in the behavior along lines of how they read it, mark it meaning. "Both" is allowed and must say which part is which.
4. **Name the primary question.** Map each meaning interpretation to belonging, ability, self-integrity, or trust. Choose one primary question and write why the others are secondary. Two primaries means two interventions to test separately, not one bundle.
5. **Name the moment it becomes live:** a transition, a first failure, an evaluation, a visible comparison. A wise intervention is timed to just before that moment.
6. **Check affordance.** Write what the message would promise ("you can improve", "people like you belong here", "they are on your side") and, against it, what the setting actually offers. If the setting cannot deliver the promise, the target is not actionable by a wise intervention; say what would have to change first.
7. **State the replication picture for the chosen family only**, from "What it draws on", with the numbers as given there and no promised effect size.
8. **Write the hand-off:** `draft-belonging-story`, `adapt-growth-mindset-message`, or `draft-values-affirmation`; for trust, `select-intervention-levers` with the mechanism stated. Add what a test should pre-register, because the record is fragile.
9. **Stop here.** Do not draft the story, the message, or the exercise.

See `references/worked-example.md` for a complete run in Peruvian public secondary schools, and `references/evidence-notes.md` for every number above with its source and verification state.

## Output template

```markdown
# Wise-intervention target

**Behavior:** <who, what, when, carried over verbatim>
**Barrier evidence carried over:** <the Motivation (reflective) finding and its field support>
**Audience interpretations used:** <n interviews or responses; who; when>

## How the audience reads the situation

| Interpretation (their words) | Said by (n of N) | Candidate question |
|---|---|---|
| <quote or close paraphrase> | <n of N> | <belonging | ability | self-integrity | trust | none> |

## Structural test

| Interpretation | Material barrier in play | If removed, would the behavior follow? | Verdict |
|---|---|---|---|
| <...> | <cost, access, time, information, process, or none> | <yes/no, with the reason> | <structural: to select-intervention-levers | meaning | both: which part is which> |

## The question
**Primary:** <belonging | ability | self-integrity | trust>: "<the question in the audience's words>"
**Why this one, not the others:** <...>
**When it becomes live:** <the transition, failure, evaluation, or comparison, and its timing>

## Affordance check
**What the message would promise:** <...>
**What the setting actually offers:** <facts, with their source>
**Verdict:** <afforded | not afforded: what would have to change first | unverified>

## Replication picture for this family
<the record for this family only, with the numbers as given in What it draws on; no effect size promised>

## Hand-off
<draft-belonging-story | adapt-growth-mindset-message | draft-values-affirmation | trust: select-intervention-levers with the mechanism stated>; <what a test should pre-register: outcome, subgroup, timing>

## What to check before relying on this
- <the interpretation that rests on the fewest respondents>
- <the affordance fact most likely to be a hope rather than a fact>
```

## Where it goes wrong

- **Reading a structural barrier as a belief.** "They do not think they can" when there is no teacher, no money, or no transport. If the structural test says the behavior would follow once the barrier is removed, the target is not here, whatever the quotes sound like.
- **Picking the famous family.** Growth mindset is chosen because the team has heard of it, not because the audience is asking "can I do this?". The question comes from the interpretation table, never from the program's preference.
- **Promising an effect size.** Early and lab studies report large effects; the field record is small (mindset d = 0.08), conditional (belonging), or null (Argentina, Kibera). The output states the record and promises nothing.
- **Skipping affordance.** A belonging message where no one will include them, an ability message where there is no second attempt: the message is then false, and the recipient learns that it was.
- **Naming two questions and recommending a bundle.** The Kibera bundle (affirmation, gratitude, aspirations) moved gratitude only; a bundle hides which component, if any, worked. Name one primary question.
- **Drifting into a needs audit.** Listing autonomy, competence, and relatedness satisfaction is Self-Determination Theory and a different skill. Stop if the output starts to look like a needs scale.
- **Diagnosing without the audience's words.** The four questions are easy to assign from a theory of change. Without quotes, the output is a hypothesis list and must say so in its first line.

## When to bring in a specialist

Tell the user to consult a psychologist with intervention experience, together with a local qualitative researcher, when:
- The audience includes people in clinical distress (depression, trauma, suicidality), because a self-integrity or belonging exercise can bring the threat to mind without resolving it
- The identity threat involves stigma or a protected characteristic (HIV status, caste, ethnicity, disability), because the elicitation questions need local shaping and the affordance check is likely to fail if the institution itself discriminates
- The decision is high-stakes or large-scale (a regional or national rollout, or a program substituting a message for a structural fix) on a family whose record is contested; bring an evaluator to pre-register the test before any scaling

Bring them: the interpretation table with quotes, the structural test, the affordance check with its facts, and the stakes and scale of the decision.
