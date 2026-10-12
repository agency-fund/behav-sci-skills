---
name: synthesize-interview-findings
description: >-
  Use when interviews are done and the team needs to know within days which
  barrier hypotheses they support before a design decision. Also use when
  someone says "we have 15 transcripts, what did we learn?" or "code these
  against COM-B or the TDF". Produces a framework matrix (Framework Method,
  Gale et al. 2013, run rapidly after Vindrola-Padros and Johnson 2020): one
  row per respondent, one column per hypothesis with its COM-B or TDF domain,
  each cell a summary with a verbatim anchor; then a supported, not supported,
  or mixed verdict per hypothesis with counts, quotes, and disconfirming
  cases, the confirmed barriers, and what a fuller analysis would add. Do not
  use when the data are Doer/Non-Doer tallies from a Barrier Analysis; use
  analyze-doer-nondoer-differences instead. Not for writing the interview
  guide (draft-tdf-interview-guide), checking codes a language model assigned
  (audit-llm-qualitative-coding), or choosing what to do about a confirmed
  barrier (select-intervention-levers).
license: CC-BY-4.0
metadata:
  title: Turn interview transcripts into a barrier diagnosis
  type: atomic
  stage: analyze
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: not-applicable
  tags: "qualitative, tdf, com-b, diagnosis"
  consumes: "qualitative-data, comb-barrier-hypotheses, interview-guide"
  produces: "barrier-diagnosis"
---

## What it does

Summarizes a set of interviews into a framework matrix coded to COM-B or TDF domains so the team can say which barrier hypotheses the interviews support.

A framework matrix is a table with one row per respondent and one column per hypothesis or domain, each cell holding a short summary of what that person said about that topic with a verbatim anchor. COM-B (Capability, Opportunity, Motivation) and the Theoretical Domains Framework (TDF, 14 domains that map onto COM-B) are the coding frames, carried over from `decompose-comb-barriers` and `draft-tdf-interview-guide`. The skill runs the Framework Method quickly enough to inform a design decision, then states what the speed cost. The output is a barrier diagnosis; what to do about it is `select-intervention-levers`.

## When to use it

### Use it when
- Interviews run from a `draft-tdf-interview-guide` guide (or any guide with hypotheses behind it) are finished and the team asks "what did we learn?", "which barriers came up?", or "do the interviews back our hypotheses?"
- A design decision is days away and the transcripts, recordings, or notes have not been read systematically by anyone
- A team is about to quote the two most vivid interviews as "what people told us" without checking the rest
- Someone asks to "code the transcripts against COM-B" or "against the TDF domains"

### Do not use it when
- The data are Doer/Non-Doer answers from a Barrier Analysis with counts per determinant; that is `analyze-doer-nondoer-differences`
- The interviews have not happened and the question is what to ask; that is `draft-tdf-interview-guide`
- A language model produced the codes or summaries and nobody has checked them against hand coding; run `audit-llm-qualitative-coding` first, then bring the accepted codes here
- The barrier is confirmed and the question is what to do about it; that is `select-intervention-levers`
- The team wants its own assumptions examined before reading the data; `audit-researcher-bias` runs first, and its flagged priors become things to look for among the disconfirming cases

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The interview data: how many interviews, in what form (full transcripts, recordings, interviewer notes), in what language, whether and by whom translated, who interviewed, and who the respondents were. The matrix can be filled from any of these forms; the form sets how deep each cell can go.
2. **Required.** The hypotheses the interviews were meant to test, from `decompose-comb-barriers`, or the domains-to-hypotheses map from the interview guide. Without them the skill can only build a domain-by-domain matrix and will say so.
3. **Required.** The decision this synthesis must inform and when it is due. A decision in ten days with twelve transcripts allows full reading; forty recordings in three days means summarizing from audio, and the output must say which it was.
4. Optional. Respondent attributes worth charting across (site, sex, whether program records show them doing the behavior, interviewer), and whether a local analyst who speaks the language can read alongside.
5. Optional. Whether any coding or summarizing has already been done by a person or by a language model.

If 1 or 2 is missing, ask and stop; if 2 is still missing after one ask, build a domain-only matrix marked "no hypotheses supplied; discovery coding only". If 3 is missing, assume a design decision within two weeks and mark the assumption. If 4 and 5 are missing, assume no attributes beyond respondent id and no prior coding.

## What it draws on

- Gale, N. K., et al. (2013). Using the framework method for the analysis of qualitative data in multi-disciplinary health research. *BMC Medical Research Methodology*, 13, 117. https://doi.org/10.1186/1471-2288-13-117
- Vindrola-Padros, C., & Johnson, G. A. (2020). Rapid techniques in qualitative research: A critical review of the literature. *Qualitative Health Research*, 30(10), 1596–1604. https://doi.org/10.1177/1049732320921835
- Atkins, L., et al. (2017). A guide to using the Theoretical Domains Framework of behaviour change to investigate implementation problems. *Implementation Science*, 12, 77. https://doi.org/10.1186/s13012-017-0605-9
- Braun, V., & Clarke, V. (2019). Reflecting on reflexive thematic analysis. *Qualitative Research in Sport, Exercise and Health*, 11(4), 589–597. https://doi.org/10.1080/2159676X.2019.1628806; and Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), 77–101. https://doi.org/10.1191/1478088706qp063oa
- Hamilton, A. B., & Finley, E. P. (2019). Qualitative methods in implementation research: An introduction. *Psychiatry Research*. https://doi.org/10.1016/j.psychres.2019.112516

The Framework Method (Gale et al. 2013) is the procedure: familiarization with the data, coding against a frame, charting the coded material into a matrix of cases by categories, and interpretation from the matrix. Vindrola-Padros and Johnson (2020) review rapid techniques, among them summarizing straight from recordings or notes into a matrix, and set out the trade-off: speed is bought with depth, so a rapid synthesis says what it skipped. Atkins et al. (2017) describe deductive coding of interview data to TDF domains and judging which domains matter by how often a belief appears, whether beliefs conflict, and how strongly they are held; the dossier records Atkins only as the source for TDF coding, so the three relevance criteria follow this skill's drafting instructions and are to be confirmed against the paper. Braun and Clarke (2006, 2019) are the contrast, not the method: reflexive thematic analysis builds themes inductively, takes longer, and rejects coding-reliability metrics; this skill is deductive and rapid, so its output is not thematic analysis and reports no inter-coder statistic. Hamilton and Finley (2019) introduce qualitative methods in implementation research; whether they cover rapid analysis is unconfirmed in the dossier. The judgment calls this skill adds: every cell carries a verbatim anchor so a reader can check the summary against the words; "not mentioned", "asked and denied", and "not asked" are recorded as three different things; the matrix keeps one discovery column per domain without a hypothesis plus an "other" column; and a verdict is a count with quotes, never a percentage of the population.

**WEIRD skew:** the Framework Method and the rapid techniques are procedures with no population claim, which is why this skill is marked not-applicable; the sources are methods papers from health services research, and the dossier records no sample or setting for them. Setting enters at interpretation: a summary written by someone who does not know the language or the place flattens idiom and misses what was left unsaid, so the reading needs a local analyst. **Non-WEIRD evidence:** none found in the sources this skill draws on; the claim that rapid qualitative methods are used in humanitarian settings is unverified, author to confirm.

**Replication status:** method guidance, not an effect; there is nothing to replicate. The documented cost is the speed-versus-depth trade-off (Vindrola-Padros & Johnson 2020), which the output states every time.

## How to do it

1. **Fix the frame before reading.** Carry over the behavior and the hypotheses H1 to Hn with their COM-B component or TDF domain. Add one discovery column per domain that carries no hypothesis and one "other" column. Write the cell template: summary in the respondent's terms, verbatim anchor with respondent id, and one status from "supports", "contradicts", "mixed", "not mentioned", "asked and denied", "not asked".
2. **Familiarize.** Read each transcript, or listen to each recording, once through before summarizing, noting what stands out and anything that fits no column. Skipping this is where rapid synthesis loses the unexpected.
3. **Summarize each interview into its row.** One to three sentences per cell, in the respondent's words where possible, with one verbatim anchor each. Record the attributes from question 4. Fill every cell; an empty cell is indistinguishable from an unread one.
4. **Code deductively.** Place material under the hypothesis or domain it speaks to; do not invent new domains. Material that fits no column goes to "other", with its anchor, for step 6.
5. **Chart across rows.** For each hypothesis, count respondents who support, contradict, are mixed, did not mention it, or were not asked. Look for beliefs that conflict across respondents, beliefs held strongly, and differences by attribute (site, sex, on-time versus late in program records). The count is of interviews, not of people in the population.
6. **Decide per hypothesis**: supported, not supported, or mixed, with the counts, two or three quotes, and every disconfirming case named. Then list what came up that no hypothesis predicted, from the discovery and "other" columns, and what nobody mentioned despite being asked.
7. **Name the confirmed barrier or barriers** with their COM-B component and the evidence behind each, in the form `select-intervention-levers` consumes. Say which hypotheses remain open and what would settle them.
8. **State the trade-off.** What form the data took, how many interviews were read in full, who read them, whether a second reader checked any rows, and what a fuller analysis would add (full transcription, a second coder, an inductive pass, returning to respondents).
9. **Stop here.** Do not choose levers or write activities; the barrier diagnosis is the input to `select-intervention-levers`.

See `references/worked-example.md` for a complete run on fertilizer top-dressing timing in Western Kenya, and `references/evidence-notes.md` for the sources.

## Output template

```markdown
# Interview synthesis: <short name of the behavior>

**Target behavior:** <who + what + when, carried over verbatim>
**Interviews:** <n>, <respondents>, <language>, <transcripts / recordings / notes>, interviewed by <who>, translated by <who, or not translated>
**Analyst(s):** <who read; whether a local-language reader was involved>
**Decision this informs:** <decision> by <date>
**Frame:** H1 <hypothesis> [<COM-B component / TDF domain>]; H2 <...>; discovery columns: <domains>; other

## Framework matrix
| Respondent | Attributes | H1 <short label> | H2 <short label> | ... | Discovery: <domain> | Other |
|---|---|---|---|---|---|---|
| R01 | <site, sex, ...> | <summary> "<anchor>" (R01) [supports] | <...> [not mentioned] | ... | <...> | <...> |
<... one row per interview, every cell filled with a summary and a status ...>

## Verdict per hypothesis
### H1 <hypothesis>: <supported / not supported / mixed>
- Counts: <n> support, <n> contradict, <n> mixed, <n> not mentioned, <n> not asked (of <N> interviews)
- Evidence: "<quote>" (R0x); "<quote>" (R0y)
- Disconfirming cases: <respondent and what they said, or "none">
- Pattern by attribute: <e.g. supported among late appliers only, or none seen>
### H2 ...

## What came up that no hypothesis predicted
- <topic, how many raised it, anchor>

## Never mentioned, though asked
- <topic the guide covered that drew nothing>

## Confirmed barrier(s)
- <barrier> [<COM-B component>]: <the evidence in one or two sentences>
- Open: <hypothesis still unresolved and what would settle it>

## Speed-versus-depth trade-off
- Data form and depth: <n read in full, n summarized from audio or notes>
- Readers: <one analyst / second reader on n rows>
- What a fuller analysis would add: <...>

## What to check before relying on this
- <the hypothesis the design most depends on and how thin its evidence is>
- <the translation or reading limitation most likely to have hidden something>
```

## Where it goes wrong

- **Counts read as prevalence.** "Nine of twelve farmers said cash was short" is a count of interviews, chosen by who was available. It is not 75% of farmers. Report counts with the N and never a percentage of the population.
- **Summaries in the hypothesis's words.** A cell that says "confirms H1: liquidity constraint" when the farmer said "the money is gone by then, school fees" has coded the frame, not the person. Write the respondent's terms and keep the anchor; the frame goes in the status tag.
- **"Not mentioned" read as "not a barrier".** If the guide never asked about it, silence means nothing. The three absence statuses exist so that absence of evidence is not filed as evidence of absence.
- **Dropping the discovery and other columns.** A matrix with only the hypothesis columns can only confirm or deny what the team already thought. The columns the frame did not predict are where the unexpected barrier appears.
- **Calling it thematic analysis, or reporting a kappa.** This is deductive framework charting done fast. Reflexive thematic analysis (Braun & Clarke 2019) is a different, slower, inductive method that rejects reliability metrics; do not borrow its name or append an inter-coder statistic to a one-reader matrix.
- **Reading translated notes as the words.** An interviewer's English summary of a Chichewa answer has already been interpreted once. Mark which cells rest on translation or notes rather than transcript, and have a local-language reader check the rows the verdict depends on.

## When to bring in a specialist

Tell the user to consult an experienced qualitative researcher who reads the language, and where relevant the organization's safeguarding lead, when:
- The transcripts or recordings are in a language the analyst does not read, because a matrix built from someone else's summaries cannot be checked against the words, and the verdicts then rest on the translator's reading
- Any interview touched harm: violence, abuse, coercion, self-harm, a child at risk, or an illegal act disclosed to the interviewer, because the safeguarding response comes before analysis and the material needs handling rules the matrix does not provide
- The verdict on the hypothesis the design most depends on is mixed, or rests on two or three interviews, and the decision is costly to reverse; the researcher can say whether a few more interviews or a different method would settle it

Bring them: the hypotheses, the interview guide, the matrix with its anchors, the list of disconfirming cases, and the trade-off section.
