# Evidence notes: draft-theory-of-change

Every item below is taken from `docs/plan/2026-10-skill-expansion-dossier.md` (entry `draft-theory-of-change`, plus the cross-cutting cautions in section A). Verification tags are the dossier's. Nothing here was added from memory, and nothing may be upgraded from "unverified" without the author's check.

## Anchor sources

### Mayne, J. (2015). Useful theory of change models. *Canadian Journal of Program Evaluation*. https://doi.org/10.3138/cjpe.230
- Verification: verified-crossref.
- What it says: a theory of change earns its keep by making the assumptions and risks behind each causal link explicit, so that evaluation can target the links rather than the whole program. Methodological paper, no effect size, no study population.
- How this skill uses it: the per-link assumption column and the rule that a link without a stated assumption is incomplete.

### W.K. Kellogg Foundation (2004). *Logic Model Development Guide*. https://wkkf.issuelab.org/resource/logic-model-development-guide.html
- Verification: verified-fetch at the URL above; the page dates it 2004 and describes it as practical assistance to nonprofits.
- What it says: the logic model's columns (resources, activities, outputs, outcomes, impact) and how to fill them. Practitioner guide, US nonprofit audience, no evaluation of the method.
- How this skill uses it: the activity-to-output-to-outcome spine, with the correction that an output is not an outcome.

### The Agency Fund, four-level evaluation framework, Level 0 (theory of change)
- Verification: practice guidance at https://eval.playbook.org.ai/ (verified-fetch in the dossier's crosswalk source list); not a publication.
- What it says: Level 0 is the theory of change; Levels 1 to 3 test its links (formative research, outcome measures, experimental evaluation); Level 4 concerns scale and welfare. See the stage crosswalk in `taxonomy.yaml`.
- How this skill uses it: positions the output as the thing later evaluations test, which is why the strength column matters.

### Office of Evaluation Sciences (2021). Analysis plan template, July 2021. https://oes.gsa.gov/assets/files/AnalysisPlan.pdf
- Verification: verified-fetch (PDF read from the downloaded file).
- What it says: a US government evaluation unit's template in which a project description feeds the hypotheses an analysis will test.
- How this skill uses it: as the practitioner example of a chain written before the test, not after.

## Practitioner use
- The labs report records that OES, eMBeD, and 3ie work from theories of change (no URL given).
- "Common in donor M&E": the labs report marks this claim [U]. Unverified, author to confirm.

## Cross-cutting cautions carried into the strength column
- DellaVigna, S., & Linos, E. (2022). RCTs to scale. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709 [verified-crossref]. Across 126 RCTs and 23 million people, academic journal studies averaged 8.7 percentage points (+33.4%) against 1.4 points (+8.0%) in nudge-unit trials; about 70% of the gap is explained by selective publication combined with low power. This is why a published finding from elsewhere is capped at "tested elsewhere" and why the skill sends it to `assess-evidence-transferability` before any rating rises.
- Ferraro, P. J., & Tracy, J. D. (2022). *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x [verified-crossref]. Loss-framed incentive contracts: pooled 0.16 SD, but 0.33 SD in the lab versus 0.02 SD in the field. The lab-to-field shrinkage example.

## Numbers
None for the method itself; the dossier records this as a procedural skill with no numbers to quote.

## Non-WEIRD evidence
None found in the three research reports consolidated in the dossier. eMBeD and 3ie apply the method in low- and middle-income country programs; this is practice, not a study of the method.

## Replication status
Framework, no effect. Practitioner or methodological; no validation study.

## Boundary conditions and backfire
None recorded in the dossier. The failure modes in SKILL.md (outputs as outcomes, chains with no person, invented evidence, rating inflation) are this skill's authors' observations, not published findings.

## Corrections and cautions from the dossier
None for this entry.

## What this skill adds beyond the sources
- The chain must pass through at least one named behavior (who does what, when).
- Four strength labels: tested here, tested elsewhere, plausible mechanism, assumption.
- The evidence cell is filled only from what the user supplied or an evidence scan brief contains.
These are drafting rules for this library, not published criteria, and the reviewer may change them.

## What to check locally
- Whether each evidence cell's source was produced in this population; if not, the rating is at most "tested elsewhere".
- Whether the behaviors inferred by the skill are the ones the team actually relies on; a chain through the wrong behavior tests the wrong thing.
- Whether the outcome as stated is an outcome for the people the program serves or an output for the funder.
- Whether the activities listed are the ones running, not the ones planned.
