# Evidence notes: audit-llm-qualitative-coding

Every item below is taken from `docs/plan/2026-10-skill-expansion-dossier.md` (section C entry for this skill). The verification tags are the dossier's. Nothing was added from memory; where the dossier gives no number, none is quoted.

## Anchor sources

### Ashwin, J., Chhabra, A., & Rao, V. (2025). Using large language models for qualitative analysis can introduce serious bias. *Sociological Methods & Research*. https://doi.org/10.1177/00491241251338246 [verified-crossref] (DOI located in the audit)
- Earlier version: World Bank Policy Research Working Paper 10597 (2023). https://doi.org/10.1596/1813-9450-10597 [verified-crossref]. The dossier counts this among secondary versions of a work cited by its journal DOI.
- What the dossier records: on Rohingya refugee and Bangladeshi host-community transcripts, LLM coding errors were not random with respect to respondent traits.
- Sample sizes, agreement statistics, and the model used are not recorded in the dossier and are not quoted in the skill.
- This is the LMIC case (Bangladesh) that sets the skill's `weird: mixed-evidence`.

### Than, N., Fan, L., Law, T., Nelson, L. K., & McCall, L. (2025). Updating "The Future of Coding": Qualitative coding with generative large language models. *Sociological Methods & Research*, 54(3), 849–888. https://doi.org/10.1177/00491241251339188 [verified-crossref]
- Co-authors and pages come from the report; the audit confirms first author, year, and title.
- The dossier records no numbers or findings from it beyond its subject. The skill cites it as the methods update on generative-model coding and quotes nothing from it.

### Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement is not quality: Blind expert verification of human and LLM qualitative coding when human consensus is not ground truth. arXiv:2607.28890 (submitted 30 July 2026). [verified-fetch: https://arxiv.org/abs/2607.28890]
- The report's "agreement-is-not-validity preprint". Dossier caution: a 2026 arXiv item; cite as a preprint. The skill does.
- What the dossier records: human–LLM agreement is lower than human–human agreement, but a blind expert found no reliable quality difference; "agreement-based evaluation is therefore insufficient for automation decisions".
- No sample, domain, or agreement figures are recorded; none are quoted.

## Numbers quoted in the skill, and where they come from
- None. The dossier gives qualitative findings only. The percent agreement and kappa figures in the worked example are illustrative, and the skill states no pass threshold for either statistic because the sources give none.
- Cohen's kappa and percent agreement are named as the usual statistics; their definitions are standard and no source is claimed for them.

## Non-WEIRD evidence
- Ashwin, Chhabra & Rao (2025): Bangladesh, Rohingya refugee and host-community transcripts; errors not random with respect to respondent traits.
- Consequence for the skill: `weird: mixed-evidence`, the dossier's proposed value. The motivating study is LMIC; the other two sources' data are not described in the dossier.

## Replication status (as recorded)
- "New method; state it." The skill says so in its Replication status line and in the report template's framing.
- Single-study for the differential-error finding; the agreement-is-not-quality finding is a preprint.
- No effect size, so no publication-bias correction applies.

## Boundary conditions and cautions from the dossier
- Double-code a stratified subsample by hand.
- Compute agreement by subgroup.
- Test whether errors correlate with respondent traits.
- Check run-to-run stability.
- Agreement with humans is not validity.
- Caution for the drafter: cite the preprint as a preprint.

## Practitioner sources
- None recorded in the dossier for this entry.

## What the skill adds beyond the sources (judgment calls, not evidence)
- Freezing the codebook and prompt before the audit, and re-auditing after any change.
- The minimum strata: target subgroup, language or dialect, original versus translated text, short versus long answers.
- Blind independent coding by two humans with reconciliation, keeping the pre-reconciliation codes as the human–human baseline.
- Classifying each disagreement (missed, added, wrong code, human error on reflection) before looking for a pattern.
- A three-way decision (accept; accept with human review of named strata or codes; reject) with the criteria written out.
- An audit note sized for `draft-sifa-declaration`.
- The consent and safeguarding question asked before any text goes to a model.

## What to check locally
- Which language, dialect, and code-switching patterns appear in the data, and whether the audit strata cover them.
- Whether the text the model saw was the original or a translation, and who translated.
- Which subgroup the program serves, and whether that stratum has enough units to show more than gross failure.
- Whether consent covered machine processing, and whether identifying details or disclosures of harm were sent to a third-party model.
- Whether the codes the decision depends on are the ones with the worst agreement.
