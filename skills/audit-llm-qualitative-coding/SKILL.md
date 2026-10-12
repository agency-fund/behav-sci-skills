---
name: audit-llm-qualitative-coding
description: >-
  Use when an AI language model (ChatGPT, Claude, Gemini, or a script) has
  coded, or is about to code, transcripts, open answers, or field notes, and
  the team must decide whether the codes can be used. Also use when someone
  says "the LLM coded our transcripts, is that OK?", "how do we check the AI
  coding?", or a reviewer or funder asks how machine coding was validated.
  Audits the model's codes against a blind, hand-coded, stratified subsample:
  agreement overall and per respondent subgroup, the pattern in the
  disagreements, run-to-run stability, and an accept, accept-with-review, or
  reject decision, written up for the AI-use disclosure (Ashwin, Chhabra & Rao
  2025; Than et al. 2025). Do not use when the question is what the interviews
  say about the barriers; that is synthesize-interview-findings. Not for
  writing the AI-use disclosure (draft-sifa-declaration, which takes this
  audit as input), evaluating an AI product (choose-ai-eval-level), or
  examining the team's own assumptions (audit-researcher-bias).
license: CC-BY-4.0
metadata:
  title: Check whether AI-assigned interview codes can be trusted
  type: atomic
  stage: analyze
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: mixed-evidence
  tags: "llm-assisted-analysis, qualitative, research-transparency"
  consumes: "qualitative-data"
  produces: ""
---

## What it does

Audits the codes a large language model assigned to qualitative data against a blind hand-coded subsample, by respondent subgroup, to decide whether the machine coding can be used.

A large language model (LLM) can apply a codebook to hundreds of transcripts in an hour. The question this skill answers is not "does it agree with us?" but "where does it fail, for whom, and does that matter for the decision?". It produces an audit report: agreement overall and per stratum, the pattern in the disagreements, run-to-run stability, a three-way decision, and an audit note for `draft-sifa-declaration`. The analysis itself happens in `synthesize-interview-findings`.

## When to use it

### Use it when
- A team has used, or plans to use, an LLM to code transcripts, open-ended survey answers, or field notes and asks "can we trust this?", "is it OK to use the AI coding?", or "how do we validate it?"
- A funder, journal, ethics board, or reviewer asks how machine-assigned codes were checked
- The coded data cover respondents who differ in language, dialect, literacy, sex, or site, and nobody has looked at whether the model does equally well for each
- A team is about to report counts or themes from LLM codes in a decision document

### Do not use it when
- The question is what the interviews say about the barriers; that is `synthesize-interview-findings`, which takes the accepted codes
- The team wants the disclosure statement written; that is `draft-sifa-declaration`, which consumes this audit's note
- The subject is an AI product's quality or impact rather than a model used as a research tool; `choose-ai-eval-level`
- The team wants its own priors about the population examined; `audit-researcher-bias`
- No human can code a subsample in the data's language; the audit cannot run, and the skill says so rather than auditing one model against another

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The coding task as run or planned: what was coded (transcripts, answers, notes), how many units, the codebook with each code's definition, the exact prompt, the model and version, and whether the coding has already been done. An audit of an unfixed codebook or prompt proves nothing.
2. **Required.** The respondent traits that could drive differential error, such as sex, language or dialect of the interview, whether the text is an original or a translation, site, literacy or schooling, interviewer, and length of answer; and which subgroup the program is for.
3. **Required.** Who can hand-code a subsample: two people who read the language and know the setting, blind to the model's codes, and the time they have. Without them there is no reference coding.
4. Optional. What the codes will be used for (a design decision, a count in a report, a published claim), which sets how much error the decision can bear.
5. Optional. Whether the transcripts contain identifying details or disclosures of harm, and whether consent covered machine processing. This decides whether the text should go to a third-party model at all.

If 1 is missing, ask and stop. If 2 is missing, ask once, then propose strata from the attributes visible in the data, marked "proposed by this skill". If 3 is missing, produce the audit plan only (strata, subsample, coding instructions) and say the decision waits on the hand coding. If 4 is missing, assume the codes feed a design decision. If 5 is missing, ask it anyway before any text is sent to a model.

## What it draws on

- Ashwin, J., Chhabra, A., & Rao, V. (2025). Using large language models for qualitative analysis can introduce serious bias. *Sociological Methods & Research*. https://doi.org/10.1177/00491241251338246 (earlier version: World Bank Policy Research Working Paper 10597, 2023, https://doi.org/10.1596/1813-9450-10597)
- Than, N., Fan, L., Law, T., Nelson, L. K., & McCall, L. (2025). Updating "The Future of Coding": Qualitative coding with generative large language models. *Sociological Methods & Research*, 54(3), 849–888. https://doi.org/10.1177/00491241251339188
- Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement is not quality: Blind expert verification of human and LLM qualitative coding when human consensus is not ground truth. arXiv preprint, arXiv:2607.28890. https://arxiv.org/abs/2607.28890

Ashwin, Chhabra, and Rao (2025) coded interview transcripts from Rohingya refugees and Bangladeshi host communities with an LLM and found that its coding errors were not random with respect to respondent characteristics: the model was worse for some kinds of respondent than for others, so an overall agreement figure can hide a subgroup for whom the codes are wrong. That finding is why this skill stratifies the audit sample and reports agreement per stratum. Than and colleagues (2025) update the methods literature on qualitative coding for generative models; the dossier records no numbers from it. Liu and colleagues (2026, a preprint) found that human-to-LLM agreement was lower than human-to-human agreement, but that a blind expert could not reliably tell the quality apart, and conclude that "agreement-based evaluation is therefore insufficient for automation decisions". This skill therefore treats the human codes as a reference rather than ground truth, inspects every disagreement rather than only counting them, and makes the decision on the pattern of errors, not on a statistic. The judgment calls this skill adds: the codebook and prompt are frozen before the audit; percent agreement and Cohen's kappa (agreement corrected for what chance alone would produce) are reported as the usual statistics with no pass threshold, because the sources give none; the model is re-run on the same inputs to check stability; and the decision has three outcomes, so "accept with human review of the weak stratum" sits between accept and reject.

**WEIRD skew:** mixed. The study that motivates the subgroup check is from Bangladesh; the other two are methods papers whose data the dossier does not describe; and differential error by language or dialect is plausible on the face of it, though the sources do not themselves test a mechanism. **Non-WEIRD evidence:** Ashwin, Chhabra, and Rao (2025), Bangladesh, Rohingya refugee and host-community transcripts: LLM coding errors were not random with respect to respondent characteristics. A user anywhere should check the model on the local language, dialect, and code-switching, on translated versus original text, and on the subgroup the program serves.

**Replication status:** new method; single-study for the differential-error finding (Ashwin et al. 2025), with Liu et al. (2026) a preprint not yet peer reviewed. Say this in the report; do not present the audit as a validated protocol.

## How to do it

1. **Freeze the target.** Record the codebook version, the exact prompt, the model and version, any settings, and the date. Any change after this point voids the audit; if the prompt must change, the audit runs again.
2. **Define the strata** from the traits in question 2: at minimum the program's target subgroup, the language or dialect of the interview, original versus translated text, and short versus long answers, because short answers are where a model has least to go on. Say in the report why each stratum was chosen.
3. **Draw the subsample**, stratified, with enough units in every stratum to show a pattern. The sources give no sample rule; state the count per stratum and say that a stratum with a handful of units can show gross failure only.
4. **Hand-code the subsample blind.** Two coders who read the language code independently without seeing the model's output, then reconcile to a consensus. Keep the pre-reconciliation codes: human-to-human agreement is the baseline the model is compared against (Liu et al.), and a unit the humans could not agree on is not one the model can be faulted for.
5. **Compute agreement** between the model and the consensus: percent agreement and Cohen's kappa, per code and overall, then per stratum, next to the human-to-human figures. Report them as description; the sources give no threshold that turns a kappa into a pass.
6. **Inspect every disagreement.** Classify each as the model missing a code, adding a code, choosing the wrong code, or the humans being wrong on reflection. Then look for the pattern: short answers, idiom, dialect, code-switching, translated text, sensitive topics, a particular interviewer. Say what the pattern is in plain words and which stratum carries it.
7. **Re-run the model** on the same subsample at least once more and report run-to-run agreement. A model that disagrees with itself cannot be accepted on one run.
8. **Decide**: accept (no stratum materially worse than the rest, errors not concentrated on the codes the decision depends on, stable across runs); accept with human review of the named strata or codes; or reject (errors concentrated in the target subgroup or on the decision's codes, or unstable). Write out the criteria applied, because no published rule applies them for you.
9. **Write the audit note for `draft-sifa-declaration`**: what the model did, what the humans did, the agreement figures, the pattern, and the decision, in four or five sentences. Then stop; the analysis continues in `synthesize-interview-findings` with the accepted codes.

See `references/worked-example.md` for a complete run on ART adherence interviews in Kisumu, Kenya, and `references/evidence-notes.md` for the sources.

## Output template

```markdown
# LLM coding audit: <dataset and coding task>

**Data:** <units coded, form, language(s), original or translated, collected by whom>
**Codebook:** <version, number of codes> | **Model:** <name, version, settings> | **Prompt:** <frozen on date; stored at>
**Use the codes will be put to:** <decision / report / publication>
**Reference coding:** <two coders, roles, language competence; blind to model output: yes>

## Strata and subsample
| Stratum | Why it matters | Units in subsample |
|---|---|---|
| <e.g. women, Dholuo, short answers> | <program's target group; low-resource language> | <n> |

## Agreement
| Stratum | n | Model vs consensus: % agreement | Kappa | Human vs human: % agreement | Kappa |
|---|---|---|---|---|---|
| Overall | <n> | <%> | <k> | <%> | <k> |
| <stratum> | <n> | <%> | <k> | <%> | <k> |
Per code (overall): <code: %, kappa; the codes the decision depends on first>

## Disagreement patterns
- <pattern in plain words, with the stratum and codes that carry it; one example unit with the human and model codes>

## Stability
- Runs: <n>; run-to-run agreement: <%>; <codes that flipped>

## Decision
**<Accept / Accept with human review / Reject>.** <criteria applied, in two or three sentences>
- Conditions: <strata or codes to be human-reviewed; what triggers a re-audit>

## Audit note for the SIFA declaration
<four or five sentences: what the model did, what the humans did, the agreement figures, the pattern, the decision>

## What to check before relying on this
- <the stratum with the fewest units>
- <whether consent covered machine processing and whether identifying text was sent>
```

## Where it goes wrong

- **Overall agreement read as safety.** An overall 85% can contain a stratum at 55%, and that stratum is often the one the program serves (Ashwin et al. 2025). Never report an overall figure without the per-stratum table beside it.
- **Human codes treated as truth.** Where the two human coders disagreed, the model's "error" may be a defensible reading (Liu et al. 2026). Report human-to-human agreement alongside, and mark disagreements that fall on units the humans also split on.
- **Coders who saw the model's output first.** A coder who reads the model's codes before coding anchors on them, and the agreement is inflated. The reference coding is blind or it is not a reference.
- **Auditing, then editing the prompt.** A prompt tuned after the audit to fix the errors the audit found is a new prompt with no audit. Freeze, audit, decide; if the prompt changes, audit again.
- **A kappa threshold invented for the occasion.** "Kappa above 0.6 is acceptable" is not in the sources this skill draws on. State the figures and the pattern, and write the criteria used as the team's own.
- **Sending what should not be sent.** Transcripts with names, locations, or disclosures of harm go to a third-party model only if consent and data-protection review allow it. If they were already sent, the audit report says so; it does not hide it.

## When to bring in a specialist

Tell the user to consult a qualitative methodologist with experience of machine-assisted coding, plus the organization's safeguarding lead or data-protection officer where relevant, when:
- The transcripts contain safeguarding disclosures (violence, abuse, a child at risk, self-harm) or identifying details, because whether the text should have gone to a model at all is a consent and protection question that precedes the audit
- The stratum with the worst agreement is the population the program is for, because the decision is then whether to use the model at all for the people the work is meant to serve, and that is not a statistic's call
- The codes will support a published claim, a funding decision, or an evaluation finding, because the audit design (units per stratum, coder selection) then needs to stand up to external review

Bring them: the frozen codebook and prompt, the subsample with both human and model codes, the per-stratum agreement table, the disagreement list with its patterns, and the stability runs.
