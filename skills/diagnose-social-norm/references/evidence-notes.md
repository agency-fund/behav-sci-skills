# Evidence notes: diagnose-social-norm

Every source below comes from `docs/plan/2026-10-skill-expansion-dossier.md` (compiled 2026-10-12). Verification tags are carried over as the dossier gives them; nothing has been upgraded or added from memory. Numbers appear only as the dossier writes them.

## The framework

### Bicchieri (2016). *Norms in the Wild* [verified-crossref]
Oxford University Press. https://doi.org/10.1093/acprof:oso/9780190622046.001.0001. Print year 2016; the Oxford Scholarship Online record says 2017.
- A social norm requires an empirical expectation (belief that others follow it), a normative expectation (belief that others think one should follow it), and a conditional preference to conform.
- The book's diagnostic path separates customs and moral rules (preference independent of others) from descriptive norms (conditional on empirical expectations only) and social norms (conditional on both expectations, usually with sanctions).
- A chapter DOI for "Measuring Norms" (10.1093/acprof:oso/9780190622046.003.0002) was seen in the Crossref search but not separately audited.

### Bicchieri & Mercier (2014). Norms and beliefs: How change occurs [verified-crossref]
In *The Complexity of Social Norms*. Springer. https://doi.org/10.1007/978-3-319-05308-0_3. A plan-only citation: the dossier confirms it exists; the research reports did not summarize its content. Use it as the account of how expectations change; do not quote findings from it.

### Cislaghi & Heise (2018). Theory and practice of social norms interventions: Eight common pitfalls [verified-crossref]
*Globalization and Health*, 14. https://doi.org/10.1186/s12992-018-0398-x.
- The plan gave "Cislaghi & Heise 2018" without a title. Two papers exist; both are verified. This skill cites the *Globalization and Health* paper because its subject, common mistakes in norms work, matches the "Where it goes wrong" section.
- The alternative, not cited here: Cislaghi & Heise (2018). Using social norms theory for health promotion in low-income countries. *Health Promotion International*. https://doi.org/10.1093/heapro/day017 [verified-crossref].
- The dossier records no numbers from either paper.

### UNICEF Innocenti / Penn Social Norms Group (2016). *Why Do People Do What They Do? A Social Norms Manual for Viet Nam, Indonesia and the Philippines* [unverified, author to confirm]
- The labs research report marked it verified, but every UNICEF URL tried in the audit redirected or returned 404; the Penn resources page is behind a login. A Zimbabwe and Swaziland edition is also reported.
- Reported content: the four-question diagnostic (personal belief, empirical expectation, normative expectation, conditional preference) and the classification into norm, custom, or preference. Until the manual is re-fetched, attribute the question structure to Bicchieri (2016) and the manual only as "reported".

## Field evidence that a norm-held practice shifts collectively

### Pickering, Djebbari, Lopez, Coulibaly & Alzua (2015). Mali CLTS cluster-randomized trial [verified-crossref]
*The Lancet Global Health*, 3(11), e701–e711. https://doi.org/10.1016/S2214-109X(15)00144-8.
- Rural Mali; community-led total sanitation (CLTS) evaluated by cluster randomization.
- Result as the dossier records it: no change in diarrhea, but an effect on stunting. This summary is attributed to a Water Institute page (secondary source per the report); the audit did not re-fetch it.

### Cameron, Gertler, Shah, Alzua, Martinez & Patil (2022). Four-country CLTS field experiments [verified-crossref]
*Journal of Development Economics*, 159, 102990. https://doi.org/10.1016/j.jdeveco.2022.102990. The design report cited only a PMC id (PMC11581981); this is the journal version.
- India, Indonesia, Mali, and Tanzania. Private sanitation coverage rose 7 to 39 percentage points across the four countries.
- Child height gained about 0.3 SD once village coverage passed 50 to 75%: a threshold effect, which is the reason this skill asks for the belief-expectation gap and the reference group rather than only a yes-or-no call.
- These trials evaluate the CLTS package, not the four-question diagnosis. They show that a practice held by community expectations can move collectively; they do not validate the classification itself.

## Practitioner sources
- Institute for Reproductive Health, Georgetown University (2020). *Social Norms Exploration Tool (SNET)*. [verified-fetch: https://www.irh.org/social-norms-exploration/]. Field-tested version applied in over 15 settings. The fetched pages do not name countries and do not mention vignettes.
- Penn Center for Social Norms and Behavioral Dynamics: named in the dossier as a practitioner source; no URL recorded.

## Non-WEIRD evidence
- UNICEF trainings on the manual in Viet Nam, Indonesia, the Philippines, Zimbabwe, and Swaziland (labs report; manual unverified).
- CLTS trials in India, Indonesia, Mali, and Tanzania (Cameron et al. 2022; Pickering et al. 2015).

## Replication status
- The measurement approach (four questions, classification) is peer-reviewed through Bicchieri (2016). No study in the dossier tests its reliability or validity as an instrument.
- CLTS: replicated for coverage across four countries; mixed for health outcomes (stunting effect in Mali, no diarrhea effect; height effect only above the coverage threshold).
- A causal claim that expectations hold a practice in place needs factorial variation of empirical and normative cues (see `draft-norms-vignette`); the four questions classify, they do not establish causal weight.

## Known corrections and cautions (from the dossier)
- Cameron et al. is *Journal of Development Economics* 2022, not a PMC-only item.
- Cislaghi & Heise 2018 is ambiguous between two papers; this skill's choice is stated above.
- The UNICEF/Penn manual could not be re-fetched; keep the unverified tag until it is.
- The Mali diarrhea and stunting summary is a secondary source.
- The CLTS shaming-tactics ethical concern that appears in the design report is from memory and unverified; this skill does not cite it and routes ethics questions to `audit-intervention-ethics`.
- Two pooled social-norm meta-analyses mentioned in the design report have unverified authors and may not be cited by any norms skill.

## What to check locally
- Whether respondents will state expectations honestly in front of an outsider, in a group, or in front of the people they name; private individual interviews are the default for the normative-expectation and deviation questions.
- Who the reference group actually is for this practice; it is practice-specific and often not the program's audience.
- Which sanctions are credible here (gossip, exclusion, loss of standing, violence) and who applies them; the severity decides whether a norm is fragile or entrenched.
- Whether the practice is at or near a coverage threshold; the CLTS evidence suggests collective change concentrates once a majority has moved.
- Whether the practice is legally restricted or harmful, which changes the question set and requires the specialist route before fieldwork.
