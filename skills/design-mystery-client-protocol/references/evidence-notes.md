# Evidence notes: design-mystery-client-protocol

Every source below comes from `docs/plan/2026-10-skill-expansion-dossier.md` (compiled 2026-10-12). Verification tags are carried over as the dossier gives them; nothing has been upgraded or added from memory. Numbers appear only as the dossier writes them.

## The method

### Das, Holla, Das, Mohanan, Tabak & Chan (2012). In urban and rural India, a standardized patient study showed low levels of provider training and huge quality gaps [verified-crossref]
*Health Affairs*, 31(12), 2774–2784. https://doi.org/10.1377/hlthaff.2011.1356.
- Standardized patients presenting fixed cases to providers in Delhi (urban) and Madhya Pradesh (rural), India.
- Numbers the dossier allows: 926 interactions with 305 providers.
- Result as the dossier and the paper's title record it: low levels of provider training and large quality gaps. The dossier does not give case-level rates (correct diagnosis, correct treatment, unnecessary treatment), so none are quoted in the skill.
- Correction applied in the dossier audit: the author list is Das, Holla, Das, Mohanan, Tabak & Chan; there is no author named Mohpal. Cite exactly as above.

### Kwan et al. (2019). Use of standardised patients for healthcare quality research in low- and middle-income countries [verified-crossref]
*BMJ Global Health*, 4, e001669. https://doi.org/10.1136/bmjgh-2019-001669.
- A plan-only citation: the audit confirmed first author, year, and title; the research reports did not summarize its content.
- Use it as the guide to the method in LMIC settings. Do not attribute a specific recommendation, threshold, or detection figure to it until it has been read.

### "King, Das et al." standardized patient work [unverified, author to confirm]
- Named in the plan with no title; not located in the audit. Not cited in the skill. If the author identifies the paper, it may be added to this file with its tag.

## Practitioner sources
- The dossier entry records none specific to this skill.

## Non-WEIRD evidence
- India: Delhi and rural Madhya Pradesh, 305 providers, 926 interactions (Das et al. 2012).
- The plan also names Kenya and China as settings where the method has been used; the dossier records no citations for either, so the skill says "reported without citation".
- The method is LMIC-native in its main evidence base, which is the reason for the `likely-generalizes` tag.

## Replication status (as the dossier states it)
- Method established.
- Deception ethics and detection rates must be justified for each study.
- No pooled estimate of agreement between standardized patient visits and other measures of practice appears in the dossier.

## Boundary conditions and design rules (from the dossier entry)
- Script the case presentations.
- Recruit and train local standardized patients.
- An essential-checklist rubric.
- Plan ethics waivers and detection checks.

Design choices this skill adds that are not in the dossier (practitioner judgment, to be reviewed):
- The no-harm rule for the client: no medicine taken, no procedure undergone, every purchase kept as evidence.
- Facility- or provider-level advance consent with an opt-out as the default consent model, with a waiver as the alternative the ethics board may grant.
- Aggregate-only reporting as the default, with anything else agreed in writing before fielding.
- A client detection record after every visit plus a provider end-survey, with a pre-set rule for detected visits.
- The visit as the unit of analysis, clustered by provider.
- The transfer to non-health counters (bank, mobile money agent, agro-dealer, government office) is by analogy; the dossier gives no non-health mystery shopper evidence.
- The exclusion of cases needing a child, a pregnancy, a physical sign, or a procedure is a safety rule of this skill, not a finding from the dossier.

## Known corrections and cautions (from the dossier)
- No author "Mohpal" on Das et al. (2012).
- Kwan et al. (2019) is plan-only: existence confirmed, content not summarized.
- "King, Das et al." is unverified and uncited.
- The dossier assigns no io types to this skill in the plan; `measurement-plan` (consumes) is an existing taxonomy id chosen by the drafter; `produces` is left empty because the output is a protocol with no matching io type.

## What to check locally
- Whether a stranger presenting as a client is plausible at these providers; in small communities every client is known, and detection will be high.
- Whether local people of the right age, sex, language, and dress can be recruited and will stay unrecognized across the sampled providers.
- Whether posing as a client carries legal risk here (impersonation rules, purchase of controlled products), and whether a detected client faces anger or violence.
- Whether the providers are public employees, and what the ministry or district office will do with the results; the reporting agreement comes before the first visit.
- Whether the clinical lines of the checklist match the national guideline in force, confirmed by a local clinician.
- Whether the organization's ethics board accepts advance consent with an opt-out, or requires a waiver, for deception of this kind.
