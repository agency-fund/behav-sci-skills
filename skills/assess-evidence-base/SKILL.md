---
name: assess-evidence-base
description: >-
  Use when a program goal is set but nobody has checked what research already
  exists on similar behaviors, audiences, or interventions. Also use when
  someone asks "has this been done before?" or "what does the evidence
  actually say works here?", or when a team is about to define a target
  behavior or generate barrier hypotheses from internal assumptions alone.
  Summarizes what has worked, what has not, how large the effects were, and
  where the evidence is thin or drawn mainly from wealthy Western
  populations. Run it early, before choosing a target behavior. Do not use
  it instead of define-key-behavior; this skill surveys what is known, it
  does not select a behavior, so run both on the same goal. Not for
  reviewing the team's own past attempt (review-prior-intervention) or the
  team's own beliefs about the population (audit-researcher-bias).
license: CC-BY-4.0
metadata:
  title: Check what research already exists
  type: atomic
  stage: define
  version: "0.1.0"
  status: draft
  authors: "Joe Speed"
  org: IL
  weird: weird-only
  tags: "evidence-synthesis, rapid-evidence-assessment, grade"
  consumes: "program-goal"
  produces: "evidence-scan-brief"
---

## What it does

Reviews existing research on the behavior, audience, or setting named in a program goal, so later steps start from evidence rather than intuition.

It reports what is known to work, what is known not to work, and what is untested. The scan is a rapid evidence assessment: time-bounded and structured, meant to produce a usable brief in hours or days rather than exhaustive coverage over months. It always states its own coverage, so a thin scan cannot be mistaken for a null result.

## When to use it

### Use it when
- A program goal has just been stated and no one has checked whether similar interventions have already been tried, anywhere, for this behavior or population
- A team is about to define a target behavior or generate barrier hypotheses based purely on internal assumptions, with no reference to external evidence
- Someone asks "has this been done before?" or "what does the evidence actually say works here?"
- A funder or reviewer asks what the program's design is based on and the team's current answer is a hunch

### Do not use it when
- The team wants to select a target behavior; that is `define-key-behavior`. This skill surveys what is known, it does not choose. Run them on the same input, not one instead of the other
- The "evidence" in question is the team's own prior attempt at this program; `review-prior-intervention` structures that record against the data it collected
- The question is what the team itself believes about the population; `audit-researcher-bias` audits those priors, this skill surveys the literature
- A full systematic review or meta-analysis is required, for a publication or a policy decision; this is a rapid, time-bounded scan and says so

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The program goal as stated, plus whatever is known about the target population, setting, and constraints. This is the same raw input `define-key-behavior` takes; this skill can run in parallel with it.
2. Optional. How much time is available for the scan (a few hours, a day, a week) and which sources the user can reach (open web, specific databases, an organizational library). The "Confidence in this scan" section depends on this being honest.
3. Optional. Any studies, reports, or organizations the team already knows about, so the scan builds on them rather than rediscovering them.
4. Optional. Any specific intervention or approach the team is already considering, so the scan searches for evidence against it as well as for it.

If 1 is missing, ask and stop. If 2 is missing, assume a rapid scan of a few hours using openly available sources and say so under "Confidence in this scan". If 3 and 4 are missing, proceed.

## What it draws on

- Grant, M. J., & Booth, A. (2009). A typology of reviews: an analysis of 14 review types and associated methodologies. *Health Information & Libraries Journal*, 26(2), 91–108.
- Guyatt, G. H., Oxman, A. D., Vist, G. E., et al. (2008). GRADE: an emerging consensus on rating quality of evidence and strength of recommendations. *BMJ*, 336(7650), 924–926.
- Rothstein, H. R., Sutton, A. J., & Borenstein, M. (Eds.). (2005). *Publication Bias in Meta-Analysis: Prevention, Assessment and Adjustments*. John Wiley & Sons, Ch. 1.

A Rapid Evidence Assessment (REA): a time-bounded, structured literature scan rather than a full systematic review. The goal is a usable brief in hours or days, not exhaustive coverage over months. GRADE-style thinking governs how each finding is reported: name the effect (if any), the population and setting it was measured in, and how confident that estimate should be treated. A single small pilot and a multi-site RCT are not equally trustworthy evidence, even if both point the same direction. The publication-bias literature is why the output template has a mandatory section for null and contradicting findings: a scan that only surfaces supporting evidence is not reporting the evidence base, it is building a case for a conclusion already reached.

**WEIRD skew:** This skill's entire purpose is surfacing what is in the indexed, published literature, and that literature is itself overwhelmingly WEIRD (Western, Educated, Industrialized, Rich, Democratic) in its samples (Henrich, J., Heine, S. J., & Norenzayan, A. (2010). The weirdest people in the world? *Behavioral and Brain Sciences*, 33(2-3), 61–83). A "no evidence found" result from this skill means "no published evidence was found", not "this does not work here". The output template forces this distinction into its own field rather than letting it stay implicit.

**Replication status:** Not applicable in the effect sense: a rapid evidence assessment is a review method, not an intervention. Its known limitation is coverage. Two time-bounded scans of the same question can surface different studies, which is why the brief must state how much time and how many sources it covered rather than present itself as complete.

## How to do it

1. **Restate the goal** verbatim or lightly cleaned, so the reader can see what the evidence was scanned for.
2. **Search for evidence on the behavior and population generally**, not only for the intervention the team already has in mind. Searching only for whether a named approach works produces a brief that confirms rather than informs. If every finding points the same direction, check whether the search terms themselves were leading.
3. **Write each finding under "What has already been tried"** with four parts: the intervention or approach, the population and setting it was tried in, the effect reported with size and direction where available, and a confidence qualifier (single pilot, multiple studies, RCT, meta-analysis). Fewer, clearly characterized findings beat a long list of redundant ones that all report the same underlying result.
4. **Fill the "Findings that don't support the goal" section.** Null results, contradicting results, and backfire effects, each with what it implies for this program. If genuinely none were found, write "none found in the time available" explicitly; never omit the section. An empty section on a well-studied behavior is more likely an incomplete search than a one-sided evidence base.
5. **Flag WEIRD skew per finding**, not once for the whole brief: where the finding was actually measured versus the population and setting named in the goal, and what specifically should be validated locally before trusting it.
6. **State the evidence gaps plainly.** What the goal asks that the available literature does not address. A real gap, named, is more useful than a stretched analogy to a loosely related study.
7. **Write "Confidence in this scan":** how much time and how many sources it covered, and what a fuller review would need to check that this one could not.
8. **Check before returning:** Does any finding cite a loosely related behavior or very different population as if it directly answers the goal, without naming the gap? Does anything in the brief read "no evidence found" as "does not work"? Fix both.

See `references/worked-example.md` for a complete run on a savings program for Nairobi market vendors.

## Output template

```markdown
# Evidence scan brief

**Program goal (as given):** <verbatim or lightly cleaned goal statement>

## What has already been tried
- <intervention/approach 1>: <population/setting it was tried in>; <effect reported, with size and direction if available>; <confidence: e.g. single pilot / multiple studies / RCT / meta-analysis>
- <intervention/approach 2>: <...>

## Findings that don't support the goal (mandatory; state "none found in the time available" explicitly if genuinely none, do not omit the section)
- <null result, contradicting result, or backfire effect>: <population/setting>; <what this implies for the current program>

## WEIRD-skew flags (mandatory; per finding above, not once for the whole brief)
- <finding>: <population/setting it was actually measured in, versus the target population/setting named in the program goal>; <what specifically should be validated locally before trusting it as-is>

## Evidence gaps
<what the program goal asks that the available literature simply does not address; a real gap, stated plainly, is more useful than a stretched analogy to a loosely related study>

## Confidence in this scan
<how much time and how many sources this scan covered, and what a fuller review would need to check that this one could not>
```

## Where it goes wrong

- **One-sided search.** Searching only for evidence that the named intervention works, rather than for evidence on the behavior and population generally, produces a brief that confirms rather than informs. If every finding points the same direction, check whether the search terms themselves were leading.
- **Analogy laundering.** Citing a study on a loosely related behavior or a very different population as if it directly answers the program goal, without naming the gap in the WEIRD-skew flags or Evidence gaps section. A study on urban US college students' savings behavior is not silently transferable to rural smallholder farmers; say so if that is the best evidence available.
- **Confidence collapse.** Treating a single small pilot and a replicated RCT as equally strong evidence because both get reported as "a study found". The confidence qualifier in each bullet exists specifically to prevent this.
- **Padding to look thorough.** Listing many superficially similar studies that all report the same underlying finding inflates the appearance of a rich evidence base without adding information. Fewer, more clearly characterized findings beat a long list of redundant ones.
- **Treating "no evidence found" as "doesn't work".** An REA is time-bounded and WEIRD-skewed by construction. Absence of published evidence for this exact population is not evidence of absence. The Evidence gaps section exists to make that distinction explicit rather than letting a thin scan read as a null result.

## When to bring in a specialist

Tell the user to consult a research librarian, an evidence-synthesis specialist, or a behavioral scientist with domain knowledge when:
- The decision the scan informs is high-stakes or hard to reverse (a multi-year program design, a national policy recommendation, a publication), so a time-bounded scan is being asked to carry weight only a systematic review can carry
- The located studies contradict each other and the team has to judge which to weight; that is a GRADE-style methods judgment the scan can flag but not settle
- The relevant evidence is likely to sit in grey literature, program reports, or non-English sources the scan cannot reach, so "no evidence found" may only mean "not indexed where we looked"

Bring them: the brief with its confidence section, the search terms used, and the findings list with its confidence qualifiers.
