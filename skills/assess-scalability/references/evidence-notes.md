# Evidence notes: assess-scalability

Every item below is taken from `docs/plan/2026-10-skill-expansion-dossier.md` (entry `assess-scalability`, plus the cross-cutting caution A4 in section A). Verification tags are the dossier's. Nothing here was added from memory, and nothing may be upgraded from "unverified" without the author's check.

## Anchor sources

### Milat, A. J., et al. (2020). Intervention Scalability Assessment Tool: A decision support tool for health policy makers and implementers. *Health Research Policy and Systems*, 18. https://doi.org/10.1186/s12961-019-0494-2
- Verification: verified-crossref.
- What it says (per the dossier): a decision-support tool for scoring an intervention's readiness to scale, written for health policy makers and implementers. The dossier records "score against ISAT domains" and does not list the domains. No numbers recorded.
- How this skill uses it: the domain-scoring table. Because the domain list is not in the dossier, the six domains in the output template are a generic set written for this library and labeled as such; unverified, author to confirm against the published tool.

### Al-Ubaydli, O., List, J. A., & Suskind, D. (2020). 2017 Klein Lecture: The science of using science: Toward an understanding of the threats to scalability. *International Economic Review*, 61(4), 1387–1409. https://doi.org/10.1111/iere.12476
- Verification: verified-crossref.
- What it says (per the dossier): the threats to scalability, summarized in the dossier as population representativeness, implementer quality, spillovers, and cost. No numbers recorded.
- How this skill uses it: four of the five rows of the threats table. The fifth row, false positive, comes from DellaVigna and Linos (below). The drafting brief for this library also names general-equilibrium effects under spillovers; the dossier does not, so the skill describes spillovers generically (what changes when most people in an area are treated).

### Bold, T., et al. (2018). Experimental evidence on scaling up education reforms in Kenya. *Journal of Public Economics*, 168, 1–20. https://doi.org/10.1016/j.jpubeco.2018.08.007
- Verification: verified-crossref.
- What it says (per the dossier): contract teachers in Kenya; NGO versus government delivery. The dossier records the contrast and gives no effect sizes.
- Direction of the contrast: the drafting brief states that the program worked under NGO delivery and not under government delivery. That direction is not in the dossier's text; unverified, author to confirm from the paper.
- How this skill uses it: the implementer threat, and the rule that "same program, different implementer" is a different program until tested.

### Banerjee, A., et al. (2017). From proof of concept to scalable policies: Challenges and solutions, with an application. *Journal of Economic Perspectives*, 31(4), 73–102. https://doi.org/10.1257/jep.31.4.73
- Verification: verified-crossref.
- What it says (per the dossier): the challenges of moving from proof of concept to scalable policy, with Pratham's Teaching at the Right Level (India) as the application. No effect sizes recorded.
- How this skill uses it: the non-WEIRD case for the whole exercise; the reminder that the test that settles a scale threat is usually a further trial under scale conditions.

### List, J. A. (2022). *The Voltage Effect: How to Make Good Ideas Great and Great Ideas Scale*. Crown. https://openlibrary.org/isbn/9780593239483.json
- Verification: verified-fetch (OpenLibrary record confirms title, subtitle, publisher "Crown/Archetype", 2022; the author name is not in the record).
- What it says (per the dossier): the "voltage" threats for a general audience. No numbers recorded.
- How this skill uses it: background only; nothing is quoted from it.

### DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709
- Verification: verified-crossref (dossier item A4).
- Numbers: 126 RCTs, 23 million people. Academic journal studies average 8.7 percentage points (+33.4%); nudge-unit trials average 1.4 points (+8.0%). About 70% of the gap is explained by selective publication combined with low power. US government units only.
- How this skill uses it: the false-positive threat, and the rule that a single pilot estimate is an upper bound rather than a forecast.

## Numbers the dossier allows
- 8.7 versus 1.4 percentage points; 126 RCTs; 23 million people; about 70% of the gap from selective publication and low power (DellaVigna and Linos).
- No numbers from Bold et al. or Banerjee et al.; do not supply any.

## Unverified items (keep the wording; do not cite as established)
- The ISAT domain list (not in the dossier; the skill's six domains are generic). Author to confirm.
- The direction of the Bold et al. NGO-versus-government contrast (from the drafting brief, not the dossier). Author to confirm.
- The author name on the OpenLibrary record for *The Voltage Effect* (record shows title and publisher only).

## Non-WEIRD evidence
Kenya (Bold et al. 2018; contract-teacher program; NGO versus government delivery) and India (Banerjee et al. 2017; Pratham's Teaching at the Right Level). Both are cited for the contrast or the case, without effect sizes.

## Replication status
Well supported, per the dossier: the threats appear in independent LMIC cases and in the two-nudge-unit comparison; no contesting evidence is recorded. The ISAT is a decision tool, not an effect; whether its scores predict successful scale-up is not reported in these sources.

## Boundary conditions from the dossier
Score against ISAT domains; check the "voltage" threats (population representativeness, implementer quality, spillovers, cost); compare NGO versus government delivery.

## What this skill adds beyond the sources
- The one-line claim as the unit of assessment.
- "Evidence for, evidence against, test that would settle it" for every threat, with "no pilot evidence either way" as a legitimate cell that counts against scaling now.
- The three-way verdict (scale / scale after these tests / do not scale yet) and the "what must be true" list ordered by how much the verdict would change.
- The generic six-domain scoring table.
These are drafting rules for this library, not published criteria, and the reviewer may change them.

## What to check locally
- Who will deliver at scale, and whether their selection, training, supervision, and pay match the pilot's implementer; if not, plan a test under the new implementer before committing.
- Which subgroup carried the pilot effect, and what share of the scale population that subgroup is.
- Whether treating most people in an area changes queues, supplies, prices, or staff time in a way the pilot could not show.
- Which cost lines disappear at scale (research staff, dedicated counselors) and whether any of them was a core component.
- Whether the decision can be reversed; if not, raise the bar for "scale".
