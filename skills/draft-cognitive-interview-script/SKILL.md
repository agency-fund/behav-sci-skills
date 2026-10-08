---
name: draft-cognitive-interview-script
description: >-
  Use when a team has draft survey or questionnaire items and wants to check
  whether respondents understand them as intended before fielding them. Also
  use when someone says "pretest our survey", "cognitive testing", "do these
  questions make sense to respondents", or "think-aloud interviews for our
  questionnaire". Produces a full cognitive interview script with probes per
  item and a note-taking sheet. Do not use when the goal is to explore a topic
  or understand lived experience; that is a qualitative interview guide, not
  item pretesting. Not for psychometric validation with numbers (reliability,
  factor structure); run a measurement skill after the items survive this one.
license: CC-BY-4.0
metadata:
  title: Cognitive interview script drafter
  type: atomic
  stage: measure
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: mixed-evidence
  tags: "measurement, qualitative, survey-design, psychometrics"
  consumes: "survey-items"
  produces: "interview-guide"
---

## What it does

Turns a set of draft survey items into a cognitive interview script that tests whether respondents interpret each item the way its author intended.

Cognitive interviewing is the standard pretest for questionnaire items. A small number of respondents (usually 5 to 15 per round) answer the items while thinking aloud and responding to targeted probes, so the team can find comprehension, recall, judgement, and response problems before the survey goes to hundreds of people who cannot be asked what they meant.

## When to use it

### Use it when
- A user has draft survey items (a scale, an intake form, an M&E questionnaire) and asks "will people understand these?" or "can you pretest this?"
- A user asks for "cognitive testing", "cognitive interviews", "think-aloud testing", or "verbal probing" for a questionnaire
- A measure is being adapted to a new language, literacy level, or population and the team wants to check it still means the same thing
- A team is about to translate a validated scale and field it without checking comprehension locally
- Field staff report that respondents "don't get" certain questions and the team wants a structured way to find out why

### Do not use it when
- The user wants to explore experiences, motivations, or barriers in depth; that is a semi-structured qualitative interview guide, and the questions there are open, not item probes
- The user wants to know whether the items measure the construct reliably (Cronbach's alpha, factor analysis, item response theory); that is quantitative validation and comes after cognitive testing
- The user has no items yet and wants help writing them; draft the items first, then come back
- The "items" are behavioral tasks or games rather than questions; usability testing is the closer method

## Before you start

Ask these before writing the script. Do not ask anything the user has already answered.

1. **Required.** Paste the items exactly as respondents will see them, including response options and any instructions. If they exist in more than one language, which language will the interviews be in?
2. **Required.** Who are the respondents? Age range, literacy, language, and anything about the setting (phone, in person, group, time pressure) that changes how the interview can run.
3. **Required.** What does each item intend to measure? One phrase per item is enough. Without the intended meaning there is nothing to compare the respondent's understanding against.
4. Optional. Which items worry you most? Those get the deepest probes.
5. Optional. Interviewer experience: has anyone on the team run a cognitive interview before? This sets how much scaffolding the script carries.
6. Optional. How many interviews, how long each, and will they be recorded?

If 1 to 3 are missing, ask and stop. If 4 to 6 are missing, assume: all items get the standard probe set, interviewers are first-timers, 8 interviews of 45 minutes, audio recorded with consent.

## What it draws on

- Willis, G. B. (2005). *Cognitive Interviewing: A Tool for Improving Questionnaire Design*. SAGE. The reference text for think-aloud and verbal probing methods.
- Beatty, P. C., & Willis, G. B. (2007). Research synthesis: The practice of cognitive interviewing. *Public Opinion Quarterly*, 71(2), 287–311. https://doi.org/10.1093/poq/nfm006
- Tourangeau, R., Rips, L. J., & Rasinski, K. (2000). *The Psychology of Survey Response*. Cambridge University Press. The four-stage model (comprehension, retrieval, judgement, response) that organizes the probes.
- Willis, G. B., & Artino, A. R. (2013). What do our respondents think we're asking? Using cognitive interviewing to improve medical education surveys. *Journal of Graduate Medical Education*, 5(3), 353–356. https://doi.org/10.4300/JGME-D-13-00154.1
- Willis, G. B., & Miller, K. (2011). Cross-cultural cognitive interviewing: Seeking comparability and enhancing understanding. *Field Methods*, 23(4), 331–341. https://doi.org/10.1177/1525822X11416092

**WEIRD skew:** The method was developed in US and UK government survey labs with literate, individually interviewed respondents. Think-aloud in particular assumes respondents are comfortable narrating their own thinking to a stranger, which varies a lot by culture, schooling, and the status gap between interviewer and respondent. Willis and Miller (2011) and later cross-cultural work recommend leaning on concrete verbal probes rather than open think-aloud outside those settings. Users in low-literacy or high-deference contexts should pilot the script itself with two respondents before relying on it.

**Replication status:** Cognitive interviewing is a method, not an effect, so the question is whether it reliably finds item problems. Beatty and Willis (2007) report that it does, but that which problems get found varies by lab, interviewer, and probe style, so results from one small round are indicative rather than definitive.

## How to do it

1. **Map each item to its intended meaning** from the user's answer to question 3. Write it as "Item 4 intends to measure X; a correct understanding is Y." This is the yardstick every probe is scored against.
2. **Choose the mode.** Default to concurrent verbal probing (ask probes right after each item) with a light think-aloud invitation. Switch to retrospective probing (after the whole questionnaire) if the user said the survey is timed, self-administered, or the respondents are unlikely to narrate aloud. Say which you chose and why.
3. **Write the opening**: purpose in plain words ("we are testing the questions, not you"), consent and recording, a one-minute think-aloud practice on a neutral question ("how many windows are in your home?").
4. **For each item, write probes across the four stages**, using `references/probe-bank.md`:
   - Comprehension: "What does the phrase ___ mean to you?" and a paraphrase probe ("Can you say this question in your own words?").
   - Retrieval: "How did you arrive at that answer? What did you think back to?"
   - Judgement: "How sure are you of that answer?" and, for sensitive items, "How comfortable did you feel answering?"
   - Response: "Did any of the answer options fit better than the others? Was there one you wanted that wasn't there?"
   Give the items the user flagged as worrying two extra scripted probes aimed at the specific worry. Give every other item the standard four.
5. **Add conditional probes** the interviewer uses only when they see a cue: a long pause, a request to repeat the question, a changed answer, laughter, or an answer that does not match the options.
6. **Write the close**: "Which question was hardest? Was anything missing?" and thanks.
7. **Produce the note-taking sheet**: one row per item with columns for the four stages, a problem code, and a verbatim quote. The codes are: unclear term, double meaning, recall difficulty, sensitive, options don't fit, instruction missed, translation issue.
8. **Finish with the analysis plan**: how to tabulate problems across interviews, what counts as "fix this item" (a rule of thumb: the same problem in 2 of 8 interviews), and when to run a second round.

Keep the script in the language of the interview. If the user gave items in one language and the interviews are in another, draft the probes in the interview language and keep the original item text alongside.

## Output template

```markdown
# Cognitive interview script: <questionnaire name>

**Respondents:** <who, setting, language>  **Mode:** <concurrent / retrospective probing, think-aloud yes/no>
**Interviews planned:** <n> of <minutes> minutes. **Recording:** <yes with consent / notes only>

## 1. Opening (read aloud)
<purpose, consent, "we are testing the questions, not you", think-aloud practice>

## 2. Items and probes
### Item 1: "<exact item text>"  (response options: <...>)
**Intended meaning:** <one line>
- Comprehension: <probe>
- Paraphrase: <probe>
- Retrieval: <probe>
- Judgement: <probe>
- Response options: <probe>
- Conditional (use if <cue>): <probe>

### Item 2: ...

## 3. Closing
<hardest question, anything missing, thanks>

## 4. Note-taking sheet
| Item | Comprehension | Retrieval | Judgement | Response | Problem code | Quote |
|---|---|---|---|---|---|---|
| 1 | | | | | | |

## 5. After the interviews
- Tabulate problem codes by item across interviews.
- Fix an item when: <rule>.
- Run a second round when: <rule>.

## What to check before relying on this
- <the probe or item most likely to need local adaptation>
```

## Where it goes wrong

- **Leading probes.** The model tends to write probes that contain the intended answer ("Did you understand this as asking about the last 7 days?"). Every probe must be open: "What time period were you thinking about?"
- **Too many probes per item.** More than five or six scripted probes per item makes a 20-item questionnaire a two-hour interview. Standard set of four, extra probes only for flagged items.
- **Think-aloud where it won't work.** In settings with large interviewer–respondent status gaps or low schooling, open think-aloud produces silence. The script must default to concrete probes there, and must say so.
- **Testing the respondent instead of the item.** Scripts that read like a quiz make respondents guess at "right" answers. The opening and the probe wording must keep the item as the object of testing.
- **Treating one round as proof.** Cognitive interviews find problems; they do not certify an item as good. The output must say what a second round or a quantitative check would add.
- **Out of scope:** writing new items from scratch, translating items, and any statistical validation.

## When to bring in a specialist

Tell the user to consult a survey methodologist or a psychometrician when:
- The items are part of a validated scale whose scoring depends on the exact wording, and cognitive testing suggests changing wording; a specialist can judge what changes break comparability.
- The instrument will be used for high-stakes decisions (eligibility, diagnosis, program exit) and the team cannot run a quantitative validation afterward.
- Problems cluster on sensitive items (violence, mental health, income) in a way that suggests the survey mode itself, not the wording, is the issue.
- The interviews are cross-language and the team has no bilingual reviewer to judge whether a problem is translation or comprehension.

Bring them: the items with intended meanings, the tabulated problem codes, and three verbatim quotes per problematic item.
