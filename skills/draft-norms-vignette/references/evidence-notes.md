# Evidence notes: draft-norms-vignette

Every source below comes from `docs/plan/2026-10-skill-expansion-dossier.md` (compiled 2026-10-12). Verification tags are carried over as the dossier gives them; nothing has been upgraded or added from memory. Numbers appear only as the dossier writes them.

## The method

### Atzmüller & Steiner (2010). Experimental vignette studies in survey research [verified-crossref]
*Methodology*, 6(3), 128–138. https://doi.org/10.1027/1614-2241/a000014.
- The peer-reviewed design guidance for experimental vignette studies: short, systematically varied descriptions of a situation whose factors are manipulated and whose versions are assigned to respondents at random, so that differences in judgment can be attributed to the varied factors.
- Supplies the factorial logic this skill uses (two factors at two levels each, all combinations) and the distinction between a vignette experiment and a story followed by questions.
- The dossier records no numbers from this paper.

### Bicchieri (2016). *Norms in the Wild*, chapter 2, "Measuring Norms" [verified-crossref]
Oxford University Press. https://doi.org/10.1093/acprof:oso/9780190622046.001.0001. Print year 2016; the Oxford Scholarship Online record says 2017. Chapter DOI 10.1093/acprof:oso/9780190622046.003.0002, seen in the audit's Crossref search but not separately audited.
- A social norm requires an empirical expectation (belief that others follow the practice), a normative expectation (belief that others think one should), and a conditional preference to conform.
- The measurement consequence this skill rests on: showing that a practice is a social norm means showing the preference is conditional, which requires varying the expectations and observing whether the predicted behavior changes. The four-question diagnosis in `diagnose-social-norm` classifies; the vignette variation tests the causal weight.
- The dossier records no quantitative findings from the chapter.

## Practitioner sources

### Institute for Reproductive Health, Georgetown University (2020). *Social Norms Exploration Tool (SNET)* [verified-fetch: https://www.irh.org/social-norms-exploration/]
- A participatory tool for exploring norms with communities; the dossier (via the `map-reference-network` entry) records that the field-tested version has been applied in over 15 settings.
- Caution carried from the dossier: the research report says SNET includes a sample vignette and a rapid-analysis template, but the pages fetched in the audit do not mention vignettes. This skill therefore does not claim that SNET contains a sample vignette and cites it only for the participatory exploration approach.
- The fetched pages do not name countries; say "15 or more settings".

### UNICEF Innocenti / Penn Social Norms Group (2016). *Why Do People Do What They Do? A Social Norms Manual for Viet Nam, Indonesia and the Philippines* [unverified, author to confirm]
- The labs report marked it verified, but every UNICEF URL tried in the audit redirected or returned 404; the Penn resources page is behind a login. A Zimbabwe and Swaziland edition is also reported.
- Reported, not confirmed: training use in Viet Nam, Indonesia, and the Philippines. Keep the unverified tag until the manual is re-fetched; attribute the measurement logic to Bicchieri (2016).

## Non-WEIRD evidence
- SNET pilots in 15 or more settings (practitioner; countries not named on the fetched pages).
- UNICEF trainings in Viet Nam, Indonesia, and the Philippines (labs report; manual unverified).
- The dossier records no quantitative result from a norms vignette study in any setting, so the skill quotes no effect size and no prediction-validity figure.

## Replication status (as the dossier states it)
- Factorial vignette design guidance is peer-reviewed (Atzmüller & Steiner 2010).
- Causal claims about norms need the factorial variation of empirical and normative cues (Bicchieri 2016).
- No pooled estimate of how well vignette answers predict real behavior appears in the dossier; treat any given practice as a single-study question.

## Boundary conditions and design rules (from the dossier entry)
- Fix the dilemma.
- Vary the empirical and normative cues factorially.
- Ask what others would do or think.
- Analyze accordingly: compare predicted behavior across versions.

Design choices this skill adds that are not in the dossier (practitioner judgment, to be reviewed):
- A named protagonist who shares the respondents' situation, with the questions kept in the third person.
- Three fixed questions after every version (what the protagonist will do; what most of the reference group would do; what the reference group would think of her), and a personal normative belief question asked before the scene.
- The two-by-two between-respondent design as the default, with an optional no-cue version and a within-respondent fallback for small samples.
- A base scene of about 30 seconds read aloud, and a single simple quantifier in the empirical cue.
- The reading rule (empirical-cue shift only = descriptive norm; normative-cue shift = social norm; neither = custom or moral rule, read with the personal belief) follows Bicchieri's classification but is this skill's operationalization, not a published decision rule.
- The exclusion of distressing scenes for harmful practices before specialist review is a safety rule of this skill.

## Known corrections and cautions (from the dossier)
- The SNET sample vignette is asserted by the research report, not confirmed by the audit; do not claim it.
- The UNICEF/Penn manual could not be re-fetched; keep the unverified tag.
- The Bicchieri chapter DOI was seen in a Crossref search and not separately audited.
- The dossier assigns no io types to this skill in the plan; `social-norm-diagnosis` (consumes) and `survey-items` (produces) are existing taxonomy ids chosen by the drafter.

## What to check locally
- Whether respondents are used to reasoning about a hypothetical third person; where they are not, the pretest will show answers drifting to "it depends on the person".
- Whether the base scene is plausible here (the place, the protagonist's situation, the decision moment); an implausible scene produces answers about the story, not the norm.
- Whether respondents answer about the protagonist or about themselves; add a pretest probe asking whom they were thinking of.
- Whether the empirical cue is heard as an expectation or as new information about facts; the two produce different shifts, and only the pretest can tell them apart.
- Whether interviews can be held in private when the reference group is the household's authority; a mother-in-law in the room changes every answer.
- Whether the practice is harmful, illegal, or stigmatized, which routes the scene to a local researcher and an ethics reviewer before any wording is fixed.
