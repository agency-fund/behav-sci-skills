# Worked example: an AI mentor for student entrepreneurs

An illustrative run, built on the hypothetical example in Wu, Goldberg & Xu (2026) and continuing from the definition in `define-agency-construct`'s worked example. The program, the numbers, and the decisions are invented; nothing here is a finding. Items marked "drafted example" were written for this example and come from no published instrument; the one literature entry shows how an item the run could not open is reported.

**Input:** the Pitch Partner definition document (focus: entrepreneurial self-efficacy; revising after feedback; calibrated reliance on the mentor). The team wants to decide whether to switch the mentor from its "direct" mode to one that asks students questions first. Students consented to their chats being analyzed for program improvement. Teachers observe one class session a week; the course ends with a pitch scored by a panel on a rubric; the team can afford a 20-minute in-person survey at week 1 and week 12. No comparison across languages or schools is planned. Asked about items, the team wanted drafted examples now and search queries for published scales later.

```markdown
# Agency measurement plan: Pitch Partner (AI mentor for student entrepreneurs)

**Definition:** A student's capability to form, defend, and revise a business idea of their own, and to judge when the mentor's input helps. Focus: entrepreneurial self-efficacy; revising after feedback; calibrated reliance on the mentor.
**Decision this plan supports:** keep the direct mode or switch to the questions-first mode (product iteration); a funder report may follow.
**Assumed:** the students' consent covers analysis of a de-identified copy of chats by a language model; to confirm with the ethics reviewer.

## Measures on the 2x2 agency framework
| | Agency with respect to the end goal: a viable business idea | Agency with respect to the digital tool: the AI mentor |
|---|---|---|
| **Thoughts and feelings** (internally experienced) | **On-platform:** one-item confidence check right after the student revises the idea, weeks 3, 6, 9 (#1)<br>**Off-platform:** self-efficacy battery in the week 1 and 12 survey (#2) | Not in focus |
| **Choices and actions** (externally expressed) | **On-platform:** LLM coding of chats for setting and revising the idea, every week, experimental (#3)<br>**Off-platform:** panel pitch rubric, week 12 (have) (#4) | **On-platform:** share of turns where the student asks the mentor to choose or write versus pushes back or adapts, every week (#5)<br>**Off-platform:** teacher observation of whether students can explain their idea without the phone, weekly (have, needs a checklist) (#6) |

## Measure details
| # | Instrument | Items | Source | Evidence base | Form | Manifestation |
|---|---|---|---|---|---|---|
| 1 | Single in-chat item, three labeled options | Drafted example, not from the literature: "How sure are you that you can make your idea work? Not sure / A little sure / Very sure" | Bandura, social cognitive theory (self-efficacy) | Single items track multi-item scales only partly and here are asked by the mentor itself, so expect social desirability; benchmark against #2 | End goal | Thoughts and feelings |
| 2 | Entrepreneurial self-efficacy scale, adapted to Class 11 and Hindi | Not accessed; see the research query below | Bandura, social cognitive theory; a published entrepreneurial self-efficacy scale to be found | Most such scales were built with university students or adults in high-income countries; check wording and response format with Class 11 students in Hindi before use | End goal | Thoughts and feelings |
| 3 | Coding instruction with low, medium, and high anchors for setting, testing, and revising the idea | Drafted example anchor, not from the literature: "High: the student changes the idea in response to a critique and says why" | Bandura: intentionality, forethought, self-reactiveness | LLM codes are unvalidated until checked against human coders on these chats, in Hindi-English mixing; a chat shows what students write, not what they do outside it | End goal | Choices and actions |
| 4 | The course's existing pitch rubric | The course's own criteria | The course | Rubric drift between panelists is unknown; a stronger pitch can come from the mentor's wording, so read with #5 and #6 | End goal | Choices and actions |
| 5 | Log coding rules for delegation versus pushback | Drafted example rule, not from the literature: count turns like "just pick one for me" or "write my pitch" as delegation | Lee & See (calibrated reliance); Bastani et al. (answer-seeking) | Copy-paste outside WhatsApp is invisible; asking the mentor to check arithmetic by choice is a proxy, not delegation | Digital tool | Choices and actions |
| 6 | Observation checklist for teachers | Drafted example, not from the literature: "Explains the idea in their own words without looking at the phone: yes / partly / no" | Bastani et al. (unassisted capability) | Teachers see one session a week; observation can change behavior | Digital tool | Choices and actions |

## Next steps
1. **Research further:** a published entrepreneurial self-efficacy scale for secondary-school students: "Validated scales of entrepreneurial self-efficacy for secondary-school students in India or other low- and middle-income countries; for each, items, response format, validation sample, and known limits in Hindi. Cite sources." And whether delegation in chats relates to what students can do unaided: "Studies linking AI chat behavior (answer-seeking, delegation) to unassisted performance among adolescents. Cite sources."
2. **Use, adapt, or build:** adapt #2 once found (translate with translate-survey-instrument; draft the Hindi survey block with draft-survey-items); build #1, #3, #5, and #6 from the drafted examples above; use #4 as it is.
3. **Test and gather evidence:** cognitive interviews with 8 students on #1 and #2 (draft-cognitive-interview-script); correlate #1 with #2 in a pilot class; two trained coders code 150 weekly chat segments stratified by mode, school, and language mix, agree first, then compare the model with their consensus (audit-llm-qualitative-coding); read 50 flagged turns of #5 by hand; two panelists double-score 20 pitches for #4. Before any funder report, bring in a psychometrician for #2.
4. **Interpret the evidence:** drop #1 as a proxy if it does not track #2; do not use #3 for any mode comparison if model-human agreement falls well below human-human agreement or errors cluster in one mode or language mix; if #5 rises in the direct mode while #6 shows students cannot explain their ideas, treat it as erosion whatever #1 says.
5. **Down the road:** design-evidential-experiment for the direct versus questions-first comparison; choose-ai-eval-level before any impact claim.
```
