# Evidence dossier for the October 2026 skill expansion

Purpose: this file is the only source from which the 52 new atomic skills (and their `references/evidence-notes.md`) may cite. It consolidates the three research reports from the planning session (design-thread, labs-diagnose-thread, measure-test-analyze-implement-thread) and a Crossref/DataCite audit of every DOI plus WebFetch checks of non-DOI sources, run 2026-10-11/12.
Rule: a skill cites only what is here, with the tag shown. Nothing may be upgraded from "unverified" by a drafter; nothing may be added from memory. Numbers are quoted only as written here.
Date: 2026-10-12. Compiled for Zezhen Wu's review.

How to read the tags:
- `[verified-crossref]`: the DOI resolved in the Crossref (or DataCite) audit and the first author, year and title match the report. Where the audit's year differs from the citation year (online-first vs print), the print year is kept and the audit year noted.
- `[verified-fetch: URL]`: no DOI; the publisher or repository page at that URL was fetched and confirms existence, author or organization, year and title. Any gap (e.g., author not shown on the page) is noted.
- `[unverified, author to confirm]`: neither check succeeded, or the report itself marked the item as from memory. Keep the report's wording; do not cite as established.
- Numbers: a number appears only if a report marked it verified (fetched page or search snippet). "effect size unverified" means the report could not confirm the magnitude. "(secondary source per report)" means the number came from a summary page (aidsmap, J-PAL evaluation page, Education Week, Water Institute, Cenfri) that this audit did not re-fetch.
- Citation-form conventions: volume, issue and pages are given only where a report gave them; the audit did not return them. Dates in `[verified-crossref]` lines are the print year the reports use.

---

## A. Cross-cutting cautions every skill may cite

A1. Mertens, S., Herberz, M., Hahnel, U. J. J., & Brosch, T. (2022). The effectiveness of nudging: A meta-analysis of choice architecture interventions across behavioral domains. *Proceedings of the National Academy of Sciences*, 119(1). https://doi.org/10.1073/pnas.2107346118 [verified-crossref] (audit year 2021, online-first).
- What to quote: d = 0.45 (95% CI 0.39–0.52) per the abstract; some secondary sources say 0.43. More than 200 studies, more than 450 effect sizes, N ≈ 2.15 million. "Structure" interventions (defaults, choice-set changes) beat "description" and "assistance" interventions; food is the most responsive domain. Moderate publication bias.

A2. Maier, M., Bartoš, F., Stanley, T. D., Shanks, D. R., Harris, A. J. L., & Wagenmakers, E.-J. (2022). No evidence for nudging after adjusting for publication bias. *Proceedings of the National Academy of Sciences*. https://doi.org/10.1073/pnas.2200300119 [verified-crossref]
- What to quote: the RoBMA bias-corrected average is about d = 0.04. Critics and a rejoinder note the average hides heterogeneity.

A3. Szaszi, B., et al. (2022). No reason to expect large and consistent effects of nudge interventions. *Proceedings of the National Academy of Sciences* (letter). https://doi.org/10.1073/pnas.2200732119 [verified-crossref] (audit confirms first author, year and title; co-authors not captured by the audit).
- What to quote: bias-adjusted range d ≈ 0.03–0.31; the average is misleading given heterogeneity.

A4. DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709 [verified-crossref]
- What to quote: 126 RCTs, 23 million people. Academic journal studies average 8.7 percentage points (+33.4%); nudge-unit trials average 1.4 points (+8.0%). About 70% of the gap is explained by selective publication combined with low power.

A5. Beshears, J., & Kosowsky, H. (2020). Nudging: Progress to date and future directions. *Organizational Behavior and Human Decision Processes*, 161(Suppl.), 3–19. https://doi.org/10.1016/j.obhdp.2020.09.001 [verified-crossref]
- What to quote: reviews 174 articles, including failures.

A6. Szaszi, B., Palinkas, A., Palfi, B., Szollosi, A., & Aczel, B. (2018). A systematic scoping review of the choice architecture movement: Toward understanding when and why nudges work. *Journal of Behavioral Decision Making*, 31(3), 355–366. https://doi.org/10.1002/bdm.2035 [verified-crossref] (audit year 2017, online-first; DOI located in this audit, the report had not confirmed it).
- What to quote: 156 studies, 422 interventions; 74% only tested effectiveness, 24% examined moderators; 7% used a power analysis; none were preregistered.

A7. Hummel, D., & Maedche, A. (2019). How effective is nudging? A quantitative review on the effect sizes and limits of empirical nudging studies. *Journal of Behavioral and Experimental Economics*, 80, 47–58. https://doi.org/10.1016/j.socec.2019.03.005 [verified-crossref]
- What to quote: 100 publications, 317 effect sizes. Also supplies the eight-dimension "morphological box" for describing a nudge.

A8. Bryan, C. J., Tipton, E., & Yeager, D. S. (2021). Behavioural science is unlikely to change the world without a heterogeneity revolution. *Nature Human Behaviour*, 5(8), 980–989. https://doi.org/10.1038/s41562-021-01143-3 [verified-crossref]
- What to quote: expect heterogeneous effects; avoid "haphazard convenience samples"; use probability samples with moderators measured. The fetched text did not explicitly discuss WEIRD samples, so do not attribute a WEIRD claim to it.

A9. Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity: A meta-analysis and a real-effort experiment. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x [verified-crossref] (DOI located in this audit).
- What to quote: pooled 0.16 SD, but 0.33 SD in the lab versus 0.02 SD in the field, with publication bias among lab studies. Use as the lab-to-field shrinkage example.

A10. Milkman, K. L., et al. (2021). Megastudies improve the impact of applied behavioural science. *Nature*, 600, 478–483. https://doi.org/10.1038/s41586-021-04128-4 [verified-crossref]
- What to quote: 61,293 people, 54 interventions (US gym); 45% raised visits by 9–27%; only 8% of interventions produced effects that persisted after the program; expert forecasts failed.

A11. Hallsworth, M. (2023). A manifesto for applying behavioural science. *Nature Human Behaviour*. https://doi.org/10.1038/s41562-023-01555-3 [verified-crossref] (report had the DOI as unverified; audit resolves it).
- What to quote: use for the "field needs to move beyond the nudge-and-test template" framing; no numbers.

Pattern to state in any technique skill: the lab-to-field shrinkage in loss framing (0.33 to 0.02 SD) and the academic-versus-unit gap (8.7 vs 1.4 points) point the same way; published lab or academic effects should be discounted when transferred.

---

## B. Frameworks and taxonomies

B1. Michie, S., et al. (2013). The behavior change technique taxonomy (v1) of 93 hierarchically clustered techniques: Building an international consensus for the reporting of behavior change interventions. *Annals of Behavioral Medicine*, 46(1), 81–95. https://doi.org/10.1007/s12160-013-9486-6 [verified-crossref]. Use: code active ingredients into 93 BCTs in 16 clusters.

B2. Michie, S., van Stralen, M. M., & West, R. (2011). The behaviour change wheel: A new method for characterising and designing behaviour change interventions. *Implementation Science*, 6, 42. https://doi.org/10.1186/1748-5908-6-42 [verified-crossref]. Use: COM-B to 9 intervention functions and 7 policy categories. The labs report notes a 2011 reliability check in two domains.

B3. Cane, J., O'Connor, D., & Michie, S. (2012). Validation of the theoretical domains framework for use in behaviour change and implementation research. *Implementation Science*, 7, 37. https://doi.org/10.1186/1748-5908-7-37 [verified-crossref]. 14 domains; sort-study validation.

B4. Behavioural Insights Team (2014; revised and updated edition, c. 2024). *EAST: Four simple ways to apply behavioural insights*. London: BIT. [verified-fetch: https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf] (the PDF at this URL is the revised edition: cover "Revised and updated edition", preface "We released the EAST framework back in 2014"; chapters Make it easy / attractive / social / timely; no individual authors on the cover. The labs report attributes the 2014 original to Service, Hallsworth, Halpern et al.; the revised edition flags studies that "have not held up to scrutiny").

B5. Dolan, P., Hallsworth, M., Halpern, D., King, D., Metcalfe, R., & Vlaev, I. (2012). Influencing behaviour: The mindspace way. *Journal of Economic Psychology*, 33(1), 264–277. https://doi.org/10.1016/j.joep.2011.10.009 [verified-crossref]. Nine levers (Messenger, Incentives, Norms, Defaults, Salience, Priming, Affect, Commitments, Ego).

B6. Bartholomew, L. K., Parcel, G. S., & Kok, G. (1998). Intervention Mapping: A process for developing theory- and evidence-based health education programs. *Health Education & Behavior*, 25(5), 545–563. https://doi.org/10.1177/109019819802500502 [verified-crossref]. Matrix of performance objectives × determinants → change methods. (Kelly's tracker claim "message customizer: intervention mapping" is adjacent; skills may cite the framework but not build the customizer.)

B7. Fogg, B. J. (2009). A behavior model for persuasive design. *Proceedings of the 4th International Conference on Persuasive Technology*. https://doi.org/10.1145/1541948.1541999 [verified-crossref]. Motivation, ability, prompt.

B8. Walton, G. M., & Wilson, T. D. (2018). Wise interventions: Psychological remedies for social and personal problems. *Psychological Review*, 125(5), 617–655. https://doi.org/10.1037/rev0000115 [verified-crossref].

B9. Münscher, R., Vetter, M., & Scheuerle, T. (2016). A review and taxonomy of choice architecture techniques. *Journal of Behavioral Decision Making*, 29(5), 511–524. https://doi.org/10.1002/bdm.1897 [verified-crossref] (audit year 2015, online-first). Nine techniques in decision information / structure / assistance.

B10. Datta, S., & Mullainathan, S. (2014). Behavioral design: A new approach to development policy. *Review of Income and Wealth*, 60(1), 7–35. https://doi.org/10.1111/roiw.12093 [verified-crossref]. Earlier version: Datta & Mullainathan (2012). *Behavioral Design: A New Approach to Development Policy*. CGD Policy Paper 016, November 2012. [verified-fetch: https://www.cgdev.org/sites/default/files/Datta_Mullainathan_Behavioral_Design.pdf] (title page read: authors, "CGD Policy Paper 016, November 2012"; §4.1 "Finding the Behavioral Bottleneck: Diagnosis"). Define → Diagnose → Design → Test; outputs DEFINED PROBLEM → ACTIONABLE BOTTLENECKS → SCALABLE INTERVENTION; behavioral mapping "generates questions".

B11. World Bank (2015). *World Development Report 2015: Mind, Society, and Behavior*. https://doi.org/10.1596/978-1-4648-0342-0 [verified-crossref] (audit year 2014, no author field). Thinking automatically, socially, with mental models.

B12. OECD (2019). *Tools and Ethics for Applied Behavioural Insights: The BASIC Toolkit*. https://doi.org/10.1787/9ea76a8f-en [verified-crossref] (Crossref title "OECD Behavioural Insights Toolkit and Ethical Framework"; no author field; developed with Pelle Guldborg Hansen per the labs report; the "ABCD" sub-tool is unverified; the full report returned 403 in the research session).

B13. Bicchieri, C. (2016). *Norms in the Wild: How to Diagnose, Measure, and Change Social Norms*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780190622046.001.0001 [verified-crossref] (Oxford Scholarship Online record, year 2017; print 2016). A social norm requires an empirical expectation, a normative expectation, and a conditional preference to conform. Chapter DOI for "Measuring Norms": 10.1093/acprof:oso/9780190622046.003.0002 (seen in the Crossref search; not separately audited).

B14. Presseau, J., et al. (2019). Action, actor, context, target, time (AACTT): A framework for specifying behaviour. *Implementation Science*, 14, 102. https://doi.org/10.1186/s13012-019-0951-x [verified-crossref]. Peer-reviewed framework; no reliability data.

B15. Gauri, V., et al. (2018). eMBeDding for impact and scale in developing contexts. *Behavioural Public Policy*, 2(2), 256–262. https://doi.org/10.1017/bpp.2018.11 [verified-crossref] (DOI located in this audit; first author Gauri). eMBeD cycle: definition and diagnosis → design → implementation and evaluation → adaptation (the cycle itself was seen only in a third-party graphic).

B16. Practitioner process frameworks with no peer-reviewed validation (attribute to the organization, do not describe as validated): BIT TESTS (Target, Explore, Solution, Trial, Scale) per Gyani, Tindall & Gallagher (2022) *Explore Field Guide* [verified-fetch: https://www.bi.team/wp-content/uploads/2022/11/BIT-Explore-Field-Guide.pdf] (title page and TESTS definitions read); Irrational Labs 3B (Behavior, Barriers, Benefits), https://irrationallabs.com/content/uploads/2025/02/3B-Framework_2025.pdf [unverified, author to confirm] (report read the PDF; not re-fetched here); BETA 4D; BWA *The Method*; UNICEF Behavioural Drivers Model (Petit 2019); CCP P Process and SBC Flow Chart; FHI 360 C-Modules; CORE Group DBC; Rare's six levers; Surgo CUBES (Engl & Sgaier 2019, *Gates Open Research* 3:886 [unverified, author to confirm], a peer-reviewed description, not a validation). "AUDAS" (Busara) and "INSPIRE" (BehaviourWorks) were not found; do not use those names.

---

## C. Per-skill entries

Order follows the plan: define, diagnose, design, measure, test, analyze, implement. "Suggested io types" quotes the plan's taxonomy section; "none assigned in the plan" means the plan did not name a type (leave both fields empty, per `docs/taxonomy.md`, unless the drafter can justify an existing type).

### define

### `draft-theory-of-change` (stage: define; proposed weird: likely-generalizes, with a procedural note)
- **Anchor citations:**
  - Mayne, J. (2015). Useful theory of change models. *Canadian Journal of Program Evaluation*. https://doi.org/10.3138/cjpe.230 [verified-crossref]
  - W.K. Kellogg Foundation (2004). *Logic Model Development Guide*. [verified-fetch: https://wkkf.issuelab.org/resource/logic-model-development-guide.html] (page dates it 2004; "practical assistance to nonprofits")
  - TAF four-level evaluation framework (Level 0): internal document in `tools/taf-skills/behavioral-science/`; not a publication, cite by repo path only.
- **Numbers to quote:** none (procedural skill).
- **Non-WEIRD evidence:** none found in the three reports; the labs report marks "common in donor M&E" as [U].
- **Replication status:** framework, no effect. Practitioner or methodological; no validation study.
- **Boundary conditions and backfire:** none in the reports.
- **Practitioner sources:** OES, eMBeD and 3ie use theories of change (labs report, no URL); OES analysis plan template July 2021 [verified-fetch: https://oes.gsa.gov/assets/files/AnalysisPlan.pdf] shows how a project description feeds hypotheses.
- **Corrections / cautions for the drafter:** none.
- **Suggested io types:** produces `theory-of-change` (new; consumed by `build-user-funnel`, `plan-evaluation-design`).

### `score-candidate-behaviors` (stage: define; proposed weird: weird-only)
- **Anchor citations:**
  - Kneebone, S., Smith, L., & Fielding, K. (2017). The Impact-Likelihood Matrix: A policy tool for behaviour prioritisation. *Environmental Science & Policy*, 70, 9–20. https://doi.org/10.1016/j.envsci.2016.11.013 [verified-crossref]
  - Selinske, M. J., et al. (2020). Identifying and prioritizing human behaviors that benefit biodiversity. *Conservation Science and Practice*. https://doi.org/10.1111/csp2.249 [verified-crossref]
  - BehaviourWorks Australia. *The Method* (book; chapter 5 "Getting ready to Deep Dive: Defining, identifying and prioritising behaviours"). [verified-fetch: https://www.behaviourworksaustralia.org/resources/the-method-book] (page gives phases Exploration ch. 1–4, Deep Dive ch. 5–8, Application ch. 9–12; no authors or year on the page; a BWA blog names Slattery & Kneebone per the labs report)
  - Presseau et al. (2019) AACTT, B14 [verified-crossref] (named in BWA ch. 5 as a supporting tool).
- **Numbers to quote:** none. The matrix scores impact, likelihood of adoption and current penetration.
- **Non-WEIRD evidence:** none found in the three reports (validated on Australian domestic water behaviours; BWA has used it for recycling, food waste and bushfire safety).
- **Replication status:** single-country tool; peer-reviewed, validated only in one Australian application.
- **Boundary conditions and backfire:** expert or literature scoring of impact; audience survey for likelihood; prevalence data for penetration. BWA's working definition of a behaviour: "WHO does WHAT with WHAT, WHERE and WHEN".
- **Practitioner sources:** BWA *The Method* (above); BIT TESTS "Target: identify and prioritise the specific behaviours to change" [verified-fetch: https://www.bi.team/wp-content/uploads/2022/11/BIT-Explore-Field-Guide.pdf]; OECD BASIC criteria (B12).
- **Corrections / cautions for the drafter:** "INSPIRE" is not a BWA framework; do not use. Fogg's "Focus Mapping" / *Tiny Habits* (2019) was seen only via secondary sources and is not citable here.
- **Suggested io types:** none assigned in the plan.

### `assess-evidence-transferability` (stage: define; proposed weird: likely-generalizes; **adjacent** to Patricia's "cultural psychology lens")
- **Anchor citations:**
  - Szaszi, B., et al. (2025). Generalizability of choice architecture interventions. *Nature Reviews Psychology*. https://doi.org/10.1038/s44159-025-00471-9 [verified-crossref] (plan-only citation, not in the three reports; audit confirms first author, year, title; the plan's co-author list "Goldstein, Soman & Michie" is not confirmed by this audit)
  - Henrich, J., Heine, S. J., & Norenzayan, A. (2010). The weirdest people in the world? *Behavioral and Brain Sciences*, 33, 61. https://doi.org/10.1017/S0140525X0999152X [verified-crossref]
  - Bryan, Tipton & Yeager (2021), A8 [verified-crossref]
  - DellaVigna & Linos (2022), A4 [verified-crossref]
  - Blumenstock, J., Callen, M., & Ghani, T. (2018). Why do defaults affect behavior? Experimental evidence from Afghanistan. *American Economic Review*, 108(10), 2868–2901. https://doi.org/10.1257/aer.20171676 [verified-crossref]; NBER w23590 https://doi.org/10.3386/w23590 [verified-crossref]
  - Gauri et al. (2018) eMBeD essay, B15 [verified-crossref]
  - Singh, A. (2023). *Before You Wreck Yourself: A Guide to Facing the Hard Truth That We Are All One Level Removed*. Busara and MIT GOV/LAB. [verified-fetch: https://mitgovlab.org/resources/before-you-wreck-yourself/] (24 experts across 22 organizations interviewed Sept–Nov 2022)
  - Busara "5 Learnings" incl. "biases are local" (Compass for SBC page) [unverified, author to confirm] (report marked V; no URL recorded)
- **Numbers to quote:** DellaVigna & Linos: 8.7 vs 1.4 points (A4). Ferraro & Tracy: 0.33 lab vs 0.02 field SD (A9). Blumenstock: 949 employees of one firm (Roshan, mobile money); a 5% default contribution versus 0% raised participation by 40 points, equivalent to a 50% employer match; mechanism was present bias and the cognitive cost of deciding, not endorsement or inattention.
- **Non-WEIRD evidence:** Afghanistan default (Blumenstock) as the worked contrast; eMBeD states proven nudges "aren't always effective in developing countries" (report, verified page, no URL). A National Academies slide claim that "1% of published psychology papers have African PIs or African samples" is [unverified, author to confirm] (slide claim only).
- **Replication status:** conceptual (it is the lens).
- **Boundary conditions and backfire:** Bryan et al.'s fetched text did not discuss WEIRD samples explicitly; attribute the WEIRD argument to Henrich et al. Compare sample vs target on culture, institutions, literacy and infrastructure; check LMIC replications; flag assumptions (labs report procedure).
- **Practitioner sources:** Busara / MIT GOV/LAB guide (above); eMBeD essay (B15).
- **Corrections / cautions for the drafter:** This probes one study's fit (units, treatments, outcomes, settings); it does not do cultural theory. Say so in "Do not use when".
- **Suggested io types:** none (lens-shaped).

### diagnose

### `draft-tdf-interview-guide` (stage: diagnose; proposed weird: weird-only)
- **Anchor citations:**
  - Atkins, L., et al. (2017). A guide to using the Theoretical Domains Framework of behaviour change to investigate implementation problems. *Implementation Science*, 12, 77. https://doi.org/10.1186/s13012-017-0605-9 [verified-crossref]
  - Cane, O'Connor & Michie (2012), B3 [verified-crossref]
  - Presseau et al. (2019) AACTT, B14 [verified-crossref]
  - Huijg, J. M., et al. (2014). Discriminant content validity of a theoretical domains framework questionnaire for use in implementation research. *Implementation Science*, 9, 11. https://doi.org/10.1186/1748-5908-9-11 [verified-crossref] (related: item bank for TDF domains)
- **Numbers to quote:** Huijg: items for 11 of 14 domains showed discriminant content validity; Reinforcement, Goals and Behavioural regulation did not.
- **Non-WEIRD evidence:** none found in the three reports (labs report: "mostly HIC health services" [U]). TAF's `/behavioral-science` COM-B probe sets are internal seed content, not evidence.
- **Replication status:** domain validity shown (Cane 2012 sort study); AACTT has no reliability data.
- **Boundary conditions and backfire:** domains overlap; developed in UK health care. Procedure: specify the behaviour (AACTT), 1–3 questions per domain, deductive coding, identify relevant domains.
- **Practitioner sources:** UCL Centre for Behaviour Change; BIT *Explore Field Guide* interview structure, "four steps of Interview", "Five probes", questions to avoid [verified-fetch: https://www.bi.team/wp-content/uploads/2022/11/BIT-Explore-Field-Guide.pdf].
- **Corrections / cautions for the drafter:** none.
- **Suggested io types:** produces `interview-guide`.

### `draft-barrier-analysis-questionnaire` (stage: diagnose; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Kittle, B. (2013; 2nd ed. 2017). *A Practical Guide to Conducting a Barrier Analysis*. Helen Keller International. [verified-fetch: https://coregroup.org/resource-library/a-practical-guide-to-conducting-a-barrier-analysis/] (page shows HKI, "YEAR PUBLISHED 2013", "Second Edition (2017)"; author name not shown on the page; the labs report attributes it to Kittle)
  - Davis, T. (2010). *Barrier Analysis Facilitator's Guide*. Food for the Hungry. [verified-fetch: https://coregroup.org/resource-library/barrier-analysis-facilitators-guide/] (page shows Food for the Hungry, 2010; author not shown; page describes the tool as "built around eight determinants")
  - CORE Group (2013). *Designing for Behavior Change: For Agriculture, Natural Resource Management, Health and Nutrition*. CORE Group, Food Security and Nutrition Network, USAID. [verified-fetch: https://coregroup.org/resource-library/designing-for-behavior-change-for-agriculture-natural-resource-management-health-and-nutrition/] (2013; built on AED's BEHAVE framework; page does not mention TOPS)
- **Numbers to quote:** the 12 determinants per the labs report: self-efficacy, social norms, positive and negative consequences, access, cues for action, perceived susceptibility, perceived severity, action efficacy, divine will, policy, culture. Sample rule: 45 Doers and 45 Non-Doers, derived from a case-control calculation (RR 3.0, 80% power) in Kittle 2013.
- **Non-WEIRD evidence:** origin is LMIC WASH and nutrition programming; Zambia facility births (People in Need) cited in the labs report; "widely used" in many LMICs. CORE Group's "Powerful to Change" analysis links Barrier Analysis or Doer/Non-Doer use to the highest behaviour change: an association, not a validation.
- **Replication status:** practitioner method; no psychometric validation found.
- **Boundary conditions and backfire:** always include self-efficacy, social norms and positive/negative consequences; pilot the questionnaire.
- **Practitioner sources:** CORE Group, Food for the Hungry, HKI; Save the Children use [unverified, author to confirm]; DBC key concepts: Priority Group, Influencing Group, Determinants, "Bridges to Activities".
- **Corrections / cautions for the drafter:** the 2010 Facilitator's Guide page says "eight determinants" while the 2013 Practical Guide uses 12; state which edition the questionnaire follows. Author names are from the report, not the fetched pages.
- **Suggested io types:** produces `interview-guide`.

### `diagnose-social-norm` (stage: diagnose; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Bicchieri (2016) *Norms in the Wild*, B13 [verified-crossref]
  - UNICEF Innocenti / Penn Social Norms Group (2016). *Why Do People Do What They Do? A Social Norms Manual for Viet Nam, Indonesia and the Philippines*. [unverified, author to confirm] (labs report marked V; every UNICEF URL tried in this audit redirected or returned 404; a Zimbabwe & Swaziland edition is also reported)
  - Cislaghi, B., & Heise, L. (2018). Theory and practice of social norms interventions: Eight common pitfalls. *Globalization and Health*, 14. https://doi.org/10.1186/s12992-018-0398-x [verified-crossref]; or Cislaghi, B., & Heise, L. (2018). Using social norms theory for health promotion in low-income countries. *Health Promotion International*. https://doi.org/10.1093/heapro/day017 [verified-crossref]. The plan gives "Cislaghi & Heise 2018" with no title; both papers exist. The drafter must pick one and say which.
  - Pickering, A. J., Djebbari, H., Lopez, C., Coulibaly, M., & Alzua, M. L. (2015). Effect of a community-led sanitation intervention on child diarrhoea and child growth in rural Mali: A cluster-randomised controlled trial. *The Lancet Global Health*, 3(11), e701–e711. https://doi.org/10.1016/S2214-109X(15)00144-8 [verified-crossref]
  - Cameron, L., Gertler, P., Shah, M., Alzua, M. L., Martinez, S., & Patil, S. (2022). The dirty business of eliminating open defecation: The effect of village sanitation on child height from field experiments in four countries. *Journal of Development Economics*, 159, 102990. https://doi.org/10.1016/j.jdeveco.2022.102990 [verified-crossref] (the design report cited only the PMC id PMC11581981; this is the journal version)
  - Bicchieri, C., & Mercier, H. (2014). Norms and beliefs: How change occurs. In *The Complexity of Social Norms*. Springer. https://doi.org/10.1007/978-3-319-05308-0_3 [verified-crossref] (plan-only citation)
- **Numbers to quote:** CLTS across India, Indonesia, Mali and Tanzania: private sanitation coverage rose 7–39 points; child height gained about 0.3 SD once village coverage passed 50–75%. Mali: no change in diarrhoea but an effect on stunting (Water Institute summary; secondary source per report).
- **Non-WEIRD evidence:** UNICEF trainings in Viet Nam, Indonesia, Philippines, Zimbabwe and Swaziland (labs report); CLTS RCTs above.
- **Replication status:** measurement approach is peer-reviewed; causal claims about norms need the vignette variation (see `draft-norms-vignette`).
- **Boundary conditions and backfire:** measure personal belief, empirical expectations, normative expectations and conditional preference, then classify (norm vs custom vs preference). Threshold effects in CLTS.
- **Practitioner sources:** UNICEF/Penn manual (unverified above); IRH SNET [verified-fetch: https://www.irh.org/social-norms-exploration/]; Penn Center for Social Norms and Behavioral Dynamics.
- **Corrections / cautions for the drafter:** Cameron et al. is JDE 2022, not a PMC-only item. Cislaghi & Heise ambiguity above. The UNICEF manual could not be re-fetched.
- **Suggested io types:** produces `social-norm-diagnosis` (new; consumed by `map-reference-network`, `plan-collective-pledge`, `write-social-norm-message`).

### `map-reference-network` (stage: diagnose; proposed weird: likely-generalizes)
- **Anchor citations:**
  - UNICEF Innocenti / Penn (2016) manual [unverified, author to confirm] (reported to cover full-network, snowball and egocentric designs)
  - Institute for Reproductive Health, Georgetown University (2020). *Social Norms Exploration Tool (SNET)*. [verified-fetch: https://www.irh.org/social-norms-exploration/] (Phase 2 "Identify Reference Groups — those who matter to individuals and the way they behave"; "applied in over 15 settings"; ALIGN platform record dated 27 January 2020 at https://www.alignplatform.org/resources/social-norms-exploration-tool-snet also fetched)
  - Bicchieri (2016), B13 [verified-crossref]
- **Numbers to quote:** SNET field-tested version applied in over 15 settings.
- **Non-WEIRD evidence:** 15+ SNET settings. The labs report names DRC; the fetched pages do not name countries.
- **Replication status:** practitioner.
- **Boundary conditions and backfire:** choose full-network, snowball or egocentric design; elicit names and roles; verify with the community. SNET uses participatory exercises and "speed interviews".
- **Practitioner sources:** SNET Training Package, SNET Factsheet, and "Engaging Communities in Exploring Social Norms: Learnings from the SNET" are listed at https://www.irh.org/?s=social+norms+exploration+tool [verified-fetch] (titles only; years not shown).
- **Corrections / cautions for the drafter:** DRC pilot not confirmed on the fetched pages; say "15+ settings".
- **Suggested io types:** consumes `social-norm-diagnosis`.

### `identify-wise-intervention-target` (stage: diagnose; proposed weird: mixed-evidence; **adjacent** to "psychological needs auditor" (SDT): different framework, different question)
- **Anchor citations:**
  - Walton & Wilson (2018), B8 [verified-crossref]
  - Walton, G. M., et al. (2023). Where and with whom does a brief social-belonging intervention promote progress in college? *Science*, 380(6644), 499–505. https://doi.org/10.1126/science.ade4420 [verified-crossref] (Crossref also lists an erratum, 10.1126/science.ads9718, 2024; author to check what it changes)
  - Baranov, V., Haushofer, J., & Jang, C. (2020). Can positive psychology improve psychological well-being and economic decision-making? Experimental evidence from Kenya. *Economic Development and Cultural Change*. https://doi.org/10.1086/702860 [verified-crossref]
  - Cohen, G. L., & Sherman, D. K. (2014). The psychology of change: Self-affirmation and social psychological intervention. *Annual Review of Psychology*, 65, 333–371. https://doi.org/10.1146/annurev-psych-010213-115137 [verified-crossref]
  - Hall, C. C., Zhao, J., & Shafir, E. (2014). Self-affirmation among the poor: Cognitive and behavioral implications. *Psychological Science*, 25(2), 619–625. https://doi.org/10.1177/0956797613510949 [verified-crossref] (audit year 2013, online-first)
  - Hanselman, P., Rozek, C. S., Grigg, J., & Borman, G. D. (2017). New evidence on self-affirmation effects and theorized sources of heterogeneity from large-scale replications. *Journal of Educational Psychology*, 109(3). https://doi.org/10.1037/edu0000141 [verified-crossref]
  - Yeager et al. (2019), Outes-León et al. (2020), Ganimian (2020): see `adapt-growth-mindset-message`.
- **Numbers to quote:** Walton 2023: 26,911 students at 22 institutions; raised full-time first-year completion only where the group was afforded opportunities to belong. Hanselman 2017: large-scale replication ruled out affirmation effects larger than 0.10. Hall 2014 (US soup kitchen): oral affirmation improved executive control and fluid intelligence and raised willingness to seek benefits; no effect among the wealthy. Kibera, Nairobi (Baranov): N = 220, affirmation bundled with gratitude and aspirations exercises; gratitude rose 0.3 SD; no effect on wellbeing, aspirations, cognitive control or discounting.
- **Non-WEIRD evidence:** Kenya (Baranov, null on the targeted outcomes); Peru and Argentina growth-mindset trials as cautions (see design entry).
- **Replication status:** contested per family. Belonging: replicated with conditions. Affirmation: contested (large replication rules out > 0.10; Protzko & Aronson 2016 failed replication seen only as a snippet and is [unverified, author to confirm]). Mindset: contested.
- **Boundary conditions and backfire:** context affordance (Walton 2023); replication fragile, so pre-register; use oral formats where literacy is low; time it right before the identity threat.
- **Practitioner sources:** none in the reports.
- **Corrections / cautions for the drafter:** state the meaning-making question (belonging, ability, self-integrity, trust) and the condition under which each family has shown effects; do not promise an effect size.
- **Suggested io types:** none assigned in the plan.

### `identify-positive-deviants` (stage: diagnose; proposed weird: likely-generalizes, as inquiry)
- **Anchor citations:**
  - Pascale, R. T., Sternin, J., & Sternin, M. (2010). *The Power of Positive Deviance*. Harvard Business Press. [verified-fetch: https://openlibrary.org/isbn/9781422110669.json] (record gives subtitle "how improbable innovators solve the world's toughest problems"; the design report wrote "unlikely innovators"; confirm wording before quoting the subtitle)
  - Marsh, D. R., et al. (2004). The power of positive deviance. *BMJ*, 329, 1177. https://doi.org/10.1136/bmj.329.7475.1177 [verified-crossref]
  - Bisits Bullen (2011). The positive deviance/hearth approach to reducing child malnutrition: Systematic review. *Tropical Medicine & International Health*. https://doi.org/10.1111/j.1365-3156.2011.02839.x [verified-crossref] (the plan's "Bullen 2011"; author name is "Bisits Bullen")
  - Triatmaja et al. (2023). Effectiveness of positive deviance approach to reduce malnutrition among under five children: A systematic review and meta-analysis of interventional studies. *Nutrients*, 15(8), 1961. https://doi.org/10.3390/nu15081961 [verified-crossref] (the plan's "2023 Nutrients meta")
- **Numbers to quote:** the 2023 meta-analysis found no significant growth z-score differences (report; effect sizes not quoted). The 2011 review's included studies were mostly uncontrolled.
- **Non-WEIRD evidence:** Vietnam malnutrition origin (Save the Children); many LMIC uses.
- **Replication status:** weak as an intervention (state it); fine as an inquiry method.
- **Boundary conditions and backfire:** define the outcome, screen for outliers, inquire into practices, verify with the community. Do not promise nutrition gains.
- **Practitioner sources:** Save the Children (Vietnam) per the labs report; no URL.
- **Corrections / cautions for the drafter:** author-name and subtitle corrections above.
- **Suggested io types:** none assigned in the plan.

### `plan-trials-of-improved-practices` (stage: diagnose; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Manoff Group. Trials of Improved Practices (TIPs). [unverified, author to confirm] (manoffgroup.com now redirects to jsi.org; no page confirming TIPs was reachable)
  - Dickin, K., Griffiths, M., & Piwoz, E. (1997). *Designing by Dialogue: A Program Planners' Guide to Consultative Research for Improving Young Child Feeding*. AED/SARA Project. [unverified, author to confirm] (USAID DEC unreachable; no OpenLibrary record; labs report marked V)
  - Alive & Thrive formative research guides. [unverified, author to confirm] (site returned 403)
  - CORE Group (2013) DBC guide [verified-fetch] (see `draft-barrier-analysis-questionnaire`; the labs report lists CORE among TIPs users)
- **Numbers to quote:** none.
- **Non-WEIRD evidence:** labs report lists TIPs use in Indonesia, Zambia, Malawi, Pakistan, Peru, Dominican Republic and Rwanda (report V; no citations).
- **Replication status:** practitioner method; no validation study.
- **Boundary conditions and backfire:** procedure per the labs report: visit 1 assesses current practice; negotiate 1–3 options; trial period (about a week); follow-up visit assesses acceptability and modifications.
- **Practitioner sources:** Manoff, Alive & Thrive, CORE (all above).
- **Corrections / cautions for the drafter:** all three primary sources are unverified by this audit; cite them with the tag and keep the method description generic. This is the household-level cousin of `design-pilot-feasibility-study`.
- **Suggested io types:** none assigned in the plan.

### `audit-process-friction` (stage: diagnose; proposed weird: mixed-evidence)
- **Anchor citations:**
  - Sunstein, C. R. (2020). Sludge audits. *Behavioural Public Policy*. https://doi.org/10.1017/bpp.2019.32 [verified-crossref]
  - Sunstein, C. R. (2021). *Sludge: What Stops Us from Getting Things Done and What to Do about It*. MIT Press. https://doi.org/10.7551/mitpress/13859.001.0001 [verified-crossref]
  - Bettinger, E. P., Long, B. T., Oreopoulos, P., & Sanbonmatsu, L. (2012). The role of application assistance and information in college decisions: Results from the H&R Block FAFSA experiment. *The Quarterly Journal of Economics*, 127(3), 1205–1242. https://doi.org/10.1093/qje/qjs017 [verified-crossref]
  - BIT, *EAST*, "Make it easy", B4 [verified-fetch]
  - Duflo, E., Kremer, M., & Robinson, J. (2011). Nudging farmers to use fertilizer: Theory and experimental evidence from Kenya. *American Economic Review*, 101(6), 2350–2390. https://doi.org/10.1257/aer.101.6.2350 [verified-crossref]; NBER w15131 https://doi.org/10.3386/w15131 [verified-crossref]
  - Banerjee, A. V., Duflo, E., Glennerster, R., & Kothari, D. (2010). Improving immunisation coverage in rural India: Clustered randomised controlled evaluation of immunisation campaigns with and without incentives. *BMJ*, 340, c2220. https://doi.org/10.1136/bmj.c2220 [verified-crossref]
  - Datta & Mullainathan (2012/2014), B10 [verified-crossref / verified-fetch]
- **Numbers to quote:** FAFSA assistance raised two-year college completion from 28% to 36%; information alone had no effect. Rajasthan "reliable camps" (supply-side reliability alone) raised full immunization from 6% to 18%. Kenya fertilizer: the "small hassle cost of travel" framing (Datta & Mullainathan on Duflo, Kremer & Robinson); numbers under `choose-delivery-moment`.
- **Non-WEIRD evidence:** Kenya (Duflo, Kremer & Robinson), India (Banerjee 2010). A Kenya "account opened at the place of business" snippet (2% still using after 2 months, via Cenfri) is [unverified, author to confirm]. No dedicated LMIC sludge-audit RCT was found.
- **Replication status:** replicated for assisted completion in the US; general principle widely supported; mixed-evidence as a transfer claim.
- **Boundary conditions and backfire:** information without assistance often fails. Walk the process as a user; count steps, documents, trips, time; tag each as necessary or removable; pre-fill or assist; re-measure.
- **Practitioner sources:** Irrational Labs 3B "barriers include every click, field and decision" [unverified, author to confirm]; ideas42, Daminger, Hayes, Barrows & Wright (2015), *Poverty Interrupted* ("poverty is a tax… in time, money and cognition"; published 2015, not 2016) [unverified, author to confirm] (report V; not re-fetched); BIT *Explore Field Guide* administrative-data analysis, four steps [verified-fetch: https://www.bi.team/wp-content/uploads/2022/11/BIT-Explore-Field-Guide.pdf].
- **Corrections / cautions for the drafter:** none beyond the unverified items.
- **Suggested io types:** none assigned in the plan.

### `assess-scarcity-load` (stage: diagnose; proposed weird: mixed-evidence)
- **Anchor citations:**
  - Mullainathan, S., & Shafir, E. (2013). *Scarcity: Why Having Too Little Means So Much*. Henry Holt / Picador. [verified-fetch: https://openlibrary.org/isbn/9780805092646.json]
  - Mani, A., Mullainathan, S., Shafir, E., & Zhao, J. (2013). Poverty impedes cognitive function. *Science*, 341, 976. https://doi.org/10.1126/science.1238041 [verified-crossref] (abstract not fetched in the research session; effect size unverified)
  - Kaur, S., Mullainathan, S., Oh, S., & Schilbach, F. (2025). Do financial concerns make workers less productive? *The Quarterly Journal of Economics*, 140(1), 635–689. https://doi.org/10.1093/qje/qjae038 [verified-crossref] (published-version details from the NBER page https://www.nber.org/papers/w28338, fetched; audit year 2024, online-first); NBER w28338 https://doi.org/10.3386/w28338 [verified-crossref]
  - O'Donnell, M., et al. (2021). Empirical audit and review and an assessment of evidentiary value in research on the psychological consequences of scarcity. *Proceedings of the National Academy of Sciences*. https://doi.org/10.1073/pnas.2103313118 [verified-crossref]
  - Haushofer, J., & Fehr, E. (2014). On the psychology of poverty. *Science*. https://doi.org/10.1126/science.1232491 [verified-crossref] (content not fetched)
- **Numbers to quote:** Kaur et al.: paying workers earlier raised output by 7% (0.11 SD) and reduced costly, unintentional mistakes; effects concentrated among the most financially constrained (NBER abstract, fetched). Mani et al.: effect size unverified. O'Donnell et al.: audit of 20 scarcity-priming studies gave mixed results.
- **Non-WEIRD evidence:** India sugarcane farmers (Mani); India low-income piece-rate manufacturing workers (Kaur).
- **Replication status:** contested for the original lab priming effects (2013 *Science* comment; O'Donnell audit); strong for field pay timing (Kaur).
- **Boundary conditions and backfire:** map the timing of financial stress (pre-harvest, pre-payday); move complex asks to slack periods; cut steps and memory demands; time cash to arrive when constraints bind.
- **Practitioner sources:** ideas42 *Poverty Interrupted* (2015) [unverified, author to confirm].
- **Corrections / cautions for the drafter:** do not quote a Mani effect size. The report's "replication critiques exist" is covered by O'Donnell et al.; do not cite other critiques from memory.
- **Suggested io types:** none assigned in the plan.

### design

Positioning rule from the plan: `select-intervention-levers` chooses the function and BCT; `draft-lever-content` is the generic writer. Each technique skill owns one technique's boundary conditions and backfire evidence; its "Do not use when" names `draft-lever-content` and the neighbouring technique skills. Every technique skill produces `intervention-draft`.

### `select-default-option` (stage: design; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Jachimowicz, J. M., Duncan, S., Weber, E. U., Hardisty, D. J., & Johnson, E. J. (2019). When and why defaults influence decisions: A meta-analysis of default effects. *Behavioural Public Policy*, 3(2), 159–186. https://doi.org/10.1017/bpp.2018.43 [verified-crossref] (report gave the RePEc page; DOI located in this audit)
  - Mertens et al. (2022), A1; Maier et al. (2022), A2 [verified-crossref]
  - Blumenstock, Callen & Ghani (2018) *AER* 108(10), 2868–2901, https://doi.org/10.1257/aer.20171676 [verified-crossref]
  - Münscher, Vetter & Scheuerle (2016), B9 [verified-crossref]
- **Numbers to quote:** d = 0.68 (95% CI 0.53–0.83), 58 studies, pooled N = 73,675; I² ≈ 98%; two studies found negative effects. Mertens: "structure" interventions including defaults outperform other categories. Afghanistan: 949 employees; 5% vs 0% default raised participation by 40 points, equivalent to a 50% employer match; present bias and the cognitive cost of deciding, not endorsement or inattention; savings attitudes persisted after the trial.
- **Non-WEIRD evidence:** Afghanistan (Blumenstock, Callen & Ghani), as above.
- **Replication status:** replicated; direction robust, size varies widely.
- **Boundary conditions and backfire:** weaker in environmental domains; can be negative when a default signals bad intent; the default must serve the chooser; keep opting out easy and visible; monitor opt-out rates; check which mechanism (endorsement, endowment, effort) the default relies on because mechanism predicts effect.
- **Practitioner sources:** EAST "Make it easy" (B4); MINDSPACE "Defaults" (B5).
- **Corrections / cautions for the drafter:** none.
- **Suggested io types:** produces `intervention-draft`.

### `draft-implementation-intention-prompt` (stage: design; proposed weird: untested-outside-weird)
- **Anchor citations:**
  - Gollwitzer, P. M., & Sheeran, P. (2006). Implementation intentions and goal achievement: A meta-analysis of effects and processes. *Advances in Experimental Social Psychology*, 38, 69–119. https://doi.org/10.1016/S0065-2601(06)38002-1 [verified-crossref]
  - Milkman, K. L., Beshears, J., Choi, J. J., Laibson, D., & Madrian, B. C. (2011). Using implementation intentions prompts to enhance influenza vaccination rates. *Proceedings of the National Academy of Sciences*, 108(26), 10415–10420. https://doi.org/10.1073/pnas.1103170108 [verified-crossref]
  - Nickerson, D. W., & Rogers, T. (2010). Do you have a voting plan? Implementation intentions, voter turnout, and organic plan making. *Psychological Science*, 21(2), 194–199. https://doi.org/10.1177/0956797609359326 [verified-crossref]
  - Carrera, M., et al. (2018). The limits of simple implementation intentions: Evidence from a field experiment on making plans to exercise. *Journal of Health Economics*. https://doi.org/10.1016/j.jhealeco.2018.09.002 [verified-crossref] (report had only a PDF sighting; DOI located in this audit)
  - Buttenheim et al. (2022). Planning and commitment prompts to encourage reporting of HIV self-test results: A cluster randomized pragmatic trial in Tshwane District, South Africa. *PLOS Global Public Health*. https://doi.org/10.1371/journal.pgph.0001196 [verified-crossref] (results not retrieved in the research session)
- **Numbers to quote:** d = 0.65 across 94 independent tests. Flu shots: the date-plus-time prompt added 4.2 points over a 33.1% baseline; the date-only prompt added 1.5 points (not significant). Voting: a plan raised turnout 4.1 points (N = 287,228) and 9.1 points in single-voter households.
- **Non-WEIRD evidence:** South Africa (Buttenheim 2022): trial exists; result not retrieved, so no number may be quoted. A savings implementation-intention study via Cenfri (numeric goals did worse than general commitments; country unconfirmed) is [unverified, author to confirm]. No LMIC field RCT with a confirmed effect was found.
- **Replication status:** replicated for one-off actions; a tight null for repeated behaviour (Carrera exercise trial); mixed overall.
- **Boundary conditions and backfire:** fails for repeated or habitual behaviours; weaker where people already plan "organically" (multi-voter households); meta-analytic effect probably inflated relative to field trials; confirm people already intend to act; ask for date, time and place; attach to an existing reminder.
- **Practitioner sources:** EAST "Make it timely" (B4).
- **Corrections / cautions for the drafter:** the plan's "verify result" for the South Africa trial remains open; cite existence only.
- **Suggested io types:** produces `intervention-draft`.

### `design-reminder-schedule` (stage: design; proposed weird: mixed-evidence)
- **Anchor citations:**
  - Thakkar, J., et al. (2016). Mobile telephone text messaging for medication adherence in chronic disease: A meta-analysis. *JAMA Internal Medicine*. https://doi.org/10.1001/jamainternmed.2015.7667 [verified-crossref] (DOI located in this audit)
  - Free, C., et al. (2013). The effectiveness of mobile-health technology-based health behaviour change or disease management interventions for health care consumers: A systematic review. *PLoS Medicine*, 10(1), e1001362. https://doi.org/10.1371/journal.pmed.1001362 [verified-crossref]
  - Karlan, D., McConnell, M., Mullainathan, S., & Zinman, J. (2016). Getting to the top of mind: How reminders increase saving. *Management Science*, 62(12), 3393–3411. https://doi.org/10.1287/mnsc.2015.2296 [verified-crossref]
  - Pop-Eleches, C., et al. (2011). Mobile phone technologies improve adherence to antiretroviral treatment in a resource-limited setting: A randomized controlled trial of text message reminders. *AIDS*, 25(6), 825–834. https://doi.org/10.1097/QAD.0b013e32834380c1 [verified-crossref] (PMC3718389)
  - Gibson, D. G., et al. (2017). Mobile phone-delivered reminders and incentives to improve childhood immunisation coverage and timeliness in Kenya (M-SIMU): A cluster randomised controlled trial. *The Lancet Global Health*, 5(4), e428–e438. https://doi.org/10.1016/S2214-109X(17)30072-4 [verified-crossref]
  - Banerjee, A., Chandrasekhar, A. G., Dalpath, S., Duflo, E., Floretta, J., Jackson, M. O., et al. (2025). Selecting the most effective nudge: Evidence from a large-scale experiment on immunization. *Econometrica*, 93(4), 1183–1223. https://doi.org/10.3982/ECTA19739 [verified-crossref]; NBER w28726 https://doi.org/10.3386/w28726 [verified-crossref]
  - Horvath, T., et al. (2012). Mobile phone text messaging for promoting adherence to antiretroviral therapy in patients with HIV infection. *Cochrane Database of Systematic Reviews*, CD009756. https://doi.org/10.1002/14651858.CD009756 [verified-crossref]
- **Numbers to quote:** Thakkar: OR 2.11 (95% CI 1.52–2.93), 16 RCTs, N = 2,742; bias-adjusted OR 1.68; adherence estimated to rise from 50% to 67.8%. Free: 75 trials, mostly low quality, nearly all in high-income countries. Kenya ART (Chulaimbo clinic): weekly SMS raised the share reaching 90% adherence by about 13–16 points over 48 weeks (aidsmap summary; secondary source per report). Cochrane (Horvath) rated two Kenyan weekly-SMS RCTs as high-quality evidence. Haryana: SMS reminders alone had no impact; SMS plus information-hub ambassadors was the most cost-effective bundle (+9.1% immunizations per dollar; J-PAL page, secondary source per report). Bolivia, Peru, Philippines (Karlan): reminders raised savings-goal attainment; messages naming the goal plus the incentive worked best; loss vs gain framing made no difference; effect size unverified. M-SIMU Kenya: SMS plus incentives improved coverage and timeliness in a high-coverage setting; effect size unverified.
- **Non-WEIRD evidence:** Kenya (Pop-Eleches; Gibson), India (Banerjee 2025), Bolivia/Peru/Philippines (Karlan).
- **Replication status:** replicated for ART adherence; mixed for immunization.
- **Boundary conditions and backfire:** effects decay; reminders alone fail where the barrier is supply or trust (Haryana). "Daily messages were less effective than weekly in Kenya" is from memory in the report: [unverified, author to confirm].
- **Practitioner sources:** EAST "Make it timely" (B4); 3ie gap-map entry for Pop-Eleches (report).
- **Corrections / cautions for the drafter:** the Pop-Eleches "53%" figure could not be found; use 13–16 points. Do not state the weekly-vs-daily contrast as a finding.
- **Suggested io types:** produces `intervention-draft`.

### `write-social-norm-message` (stage: design; proposed weird: mixed-evidence)
- **Anchor citations:**
  - Schultz, P. W., Nolan, J. M., Cialdini, R. B., Goldstein, N. J., & Griskevicius, V. (2007). The constructive, destructive, and reconstructive power of social norms. *Psychological Science*, 18(5), 429–434. https://doi.org/10.1111/j.1467-9280.2007.01917.x [verified-crossref]
  - Allcott, H. (2011). Social norms and energy conservation. *Journal of Public Economics*, 95(9–10), 1082–1095. https://doi.org/10.1016/j.jpubeco.2011.03.003 [verified-crossref]
  - Hallsworth, M., List, J. A., Metcalfe, R. D., & Vlaev, I. (2017). The behavioralist as tax collector: Using natural field experiments to enhance tax compliance. *Journal of Public Economics*, 148, 14–31. https://doi.org/10.1016/j.jpubeco.2017.02.003 [verified-crossref]
  - Kettle, S., Hernandez, M., Ruda, S., & Sanders, M. (2016). Behavioral interventions in tax compliance: Evidence from Guatemala. World Bank Policy Research Working Paper 7690. https://doi.org/10.1596/1813-9450-7690 [verified-crossref] (handle http://hdl.handle.net/10986/24530; book-chapter version 2017, https://doi.org/10.1596/978-1-4648-1120-3_ch2 [verified-crossref])
  - Cialdini, R. B., & Jacobson, R. P. (2021). Influences of social norms on climate change-related behaviors. *Current Opinion in Behavioral Sciences*. https://doi.org/10.1016/j.cobeha.2021.01.005 [verified-crossref] (plan-only citation given as author-year; resolved to this paper by Crossref; drafter to confirm it is the intended one)
  - Bicchieri (2016), B13 [verified-crossref]
  - Del Carpio, L. Peru (Lima) property-tax norm disclosure. [unverified, author to confirm] (search snippet only; no citation details located)
- **Numbers to quote:** Opower: −2.0% energy use; top decile cut 6.3%, bottom decile 0.3%. UK tax: norm and public-goods messages raised payment; descriptive norms beat injunctive. Guatemala: 43,387 taxpayers; the norm letter cited the 64.5% who had already paid; about US$760k additional revenue, 36 times the letter cost; effects persisted at 12 months. Peru: about 20% higher compliance vs control (snippet; unverified). A tax-RCT review found only half of 22 non-deterrence-message studies significant (snippet; no citation; do not cite as a study).
- **Non-WEIRD evidence:** Guatemala (Kettle), Peru (Del Carpio, unverified).
- **Replication status:** replicated in direction, small in magnitude; boomerang documented.
- **Boundary conditions and backfire:** boomerang among low users without an injunctive cue (Schultz); backfires if the true norm is unfavourable; never publicize a high prevalence of the undesired behaviour; choose a close, concrete reference group.
- **Practitioner sources:** BIT Guatemala and Indonesia tax work (Indonesia: >10 million taxpayers, early filing +7%, overall filing +2%; report V, no citation); EAST "Make it social" (B4).
- **Corrections / cautions for the drafter:** two pooled social-norm meta-analyses mentioned in the design report (d = 0.35 from 9 articles; a 200-study consumer meta) have unverified authors and may not be cited.
- **Suggested io types:** consumes `social-norm-diagnosis`; produces `intervention-draft`.

### `plan-collective-pledge` (stage: design; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Bicchieri (2016), ch. 4–5, B13 [verified-crossref]; Bicchieri & Mercier (2014) [verified-crossref] (see `diagnose-social-norm`)
  - Pickering et al. (2015) *Lancet Global Health* 3(11), e701–e711 [verified-crossref]
  - Cameron et al. (2022) *Journal of Development Economics* 159, 102990 [verified-crossref]
- **Numbers to quote:** as `diagnose-social-norm`: coverage +7–39 points across four countries; ~0.3 SD child height once coverage passed 50–75%; Mali no diarrhoea change, effect on stunting.
- **Non-WEIRD evidence:** the evidence base is non-WEIRD (India, Indonesia, Mali, Tanzania).
- **Replication status:** replicated for coverage, mixed for health.
- **Boundary conditions and backfire:** threshold effects; plan first movers and media; the CLTS shaming-tactics ethical concern is from memory in the report: [unverified, author to confirm]; route the ethics question to `audit-intervention-ethics`.
- **Practitioner sources:** UNICEF/Penn manual [unverified]; Penn Center for Social Norms and Behavioral Dynamics.
- **Corrections / cautions for the drafter:** do not cite a specific CLTS-shaming paper; none was verified.
- **Suggested io types:** consumes `social-norm-diagnosis`; produces `intervention-draft`.

### `design-commitment-device` (stage: design; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Bryan, G., Karlan, D., & Nelson, S. (2010). Commitment devices. *Annual Review of Economics*, 2, 671–698. https://doi.org/10.1146/annurev.economics.102308.124324 [verified-crossref]
  - Ashraf, N., Karlan, D., & Yin, W. (2006). Tying Odysseus to the mast: Evidence from a commitment savings product in the Philippines. *The Quarterly Journal of Economics*, 121(2), 635–672. https://doi.org/10.1162/qjec.2006.121.2.635 [verified-crossref]
  - Giné, X., Karlan, D., & Zinman, J. (2010). Put your money where your butt is: A commitment contract for smoking cessation. *American Economic Journal: Applied Economics*, 2(4), 213–235. https://doi.org/10.1257/app.2.4.213 [verified-crossref]
- **Numbers to quote:** SEED (Butuan, Green Bank): 1,777 clients surveyed, 710 offered the product; 28.4% took it up; savings balances rose 81 percentage points versus control at 12 months. CARES (Mindanao): 11% take-up; those offered were 3.3–5.8 points more likely to pass the 6-month urine test, persisting at 12 months; 66% of committers still failed.
- **Non-WEIRD evidence:** both canonical trials are Philippine.
- **Replication status:** mixed: several LMIC successes, no meta-analysis found (narrative review only), low take-up, many committers fail.
- **Boundary conditions and backfire:** people who commit and fail lose their stake; take-up usually 10–30%; confirm present bias or temptation is the barrier; offer as opt-in; choose soft or hard stakes; set a verifiable goal; plan for failers.
- **Practitioner sources:** MINDSPACE "Commitments" (B5).
- **Corrections / cautions for the drafter:** none.
- **Suggested io types:** produces `intervention-draft`.

### `choose-delivery-moment` (stage: design; proposed weird: mixed-evidence)
- **Anchor citations:**
  - Dai, H., Milkman, K. L., & Riis, J. (2014). The fresh start effect: Temporal landmarks motivate aspirational behavior. *Management Science*, 60(10), 2563–2582. https://doi.org/10.1287/mnsc.2014.1901 [verified-crossref]
  - Duflo, Kremer & Robinson (2011) *AER* 101(6), 2350–2390, https://doi.org/10.1257/aer.101.6.2350 [verified-crossref]
  - Karlan et al. (2016) *Management Science* 62(12), 3393–3411 [verified-crossref]
  - BIT *EAST*, "Make it timely", B4 [verified-fetch]
- **Numbers to quote:** Western Kenya, 1,230 maize farmers: the post-harvest offer (small time-limited free-delivery offer) raised fertilizer use by 14 points (base 24%) in season 1 and 18 points (base 26%) in season 2; later discounts worked less well. Fresh start: archival evidence only (diet searches, gym visits, stickK commitments rise after temporal landmarks); no meta-analysis.
- **Non-WEIRD evidence:** Kenya (Duflo, Kremer & Robinson); Bolivia, Peru, Philippines reminder timing (Karlan; effect size unverified).
- **Replication status:** fresh-start effect is archival only; harvest-timing is a single RCT with conceptual support from the commitment literature.
- **Boundary conditions and backfire:** map the income calendar (harvest, payday); the local landmarks list in the report (new year including local calendars, Ramadan/Eid, school term, birthday, harvest) is procedure, not evidence; no non-WEIRD test of fresh-start was found.
- **Practitioner sources:** EAST "Timely"; J-PAL Kenya fertilizer evaluation page (report, no URL).
- **Corrections / cautions for the drafter:** do not generalize the fresh-start effect to LMIC calendars without saying it is untested there.
- **Suggested io types:** produces `intervention-draft`.

### `specify-earmark-label` (stage: design; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Dupas, P., & Robinson, J. (2013). Why don't the poor save more? Evidence from health savings experiments. *American Economic Review*, 103(4), 1138–1171. https://doi.org/10.1257/aer.103.4.1138 [verified-crossref]
  - Benhassine, N., Devoto, F., Duflo, E., Dupas, P., & Pouliquen, V. (2015). Turning a shove into a nudge? A "labeled cash transfer" for education. *American Economic Journal: Economic Policy*, 7(3), 86–125. https://doi.org/10.1257/pol.20130225 [verified-crossref] (the report had the DOI as unverified; audit confirms)
  - Thaler, R. H. (1999). Mental accounting matters. *Journal of Behavioral Decision Making*, 12(3). https://doi.org/10.1002/(SICI)1099-0771(199909)12:3<183::AID-BDM318>3.0.CO;2-F [verified-crossref] (plan-only citation)
- **Numbers to quote:** Kenya: a safe box raised health savings 66%; earmarking helped only for emergencies or for people frequently "taxed" by kin; earmarking for preventive health reduced savings in the working paper. Morocco (Tayssir): an unconditional transfer labeled for education produced large gains in school participation; adding conditionality or paying mothers made almost no difference; parents came to value education more. The "76% dropout reduction" figure is unverified: do not quote.
- **Non-WEIRD evidence:** Kenya and Morocco (above).
- **Replication status:** two strong LMIC RCTs; backfire when liquidity is tied.
- **Boundary conditions and backfire:** labels that tie up liquidity can reduce saving; name the target expense; provide a separate "pot"; do not lock funds unless commitment is wanted; pair with a lockbox where kin pressure is high.
- **Practitioner sources:** J-PAL Morocco evaluation page (report, no URL).
- **Corrections / cautions for the drafter:** Benhassine "76%" unverified.
- **Suggested io types:** produces `intervention-draft`.

### `design-incentive-scheme` (stage: design; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Baird, S., Ferreira, F. H. G., Özler, B., & Woolcock, M. (2014). Conditional, unconditional and everything in between: A systematic review of the effects of cash transfer programmes on schooling outcomes. *Journal of Development Effectiveness*. https://doi.org/10.1080/19439342.2014.890362 [verified-crossref]
  - Mantzari, E., et al. (2015). Personal financial incentives for changing habitual health-related behaviors: A systematic review and meta-analysis. *Preventive Medicine*. https://doi.org/10.1016/j.ypmed.2015.03.001 [verified-crossref]
  - Gneezy, U., Meier, S., & Rey-Biel, P. (2011). When and why incentives (don't) work to modify behavior. *Journal of Economic Perspectives*, 25(4), 191–210. https://doi.org/10.1257/jep.25.4.191 [verified-crossref]
  - Banerjee, Duflo, Glennerster & Kothari (2010) *BMJ* 340, c2220 [verified-crossref]
  - Banerjee et al. (2025) *Econometrica* 93(4), 1183–1223 [verified-crossref]; Gibson et al. (2017) M-SIMU [verified-crossref]
- **Numbers to quote:** Baird: 35 studies (75 reports); unconditional or unmonitored transfers raised the odds of enrolment 18–25%; explicitly monitored conditional transfers raised them about 60%; test-score effects small at best. Mantzari: 34 RCTs; OR 1.53 up to 18 months and OR 2.11 three months after the incentive ended; larger under high deprivation (OR 2.17). Rajasthan: full immunization 39% with camps plus lentils, 18% with camps alone, 6% in control; RR 6.7 vs control; cost per fully immunized child fell from $55.83 to $27.94. Haryana: incentives plus ambassadors plus SMS raised immunizations 44% (J-PAL page, secondary source per report).
- **Non-WEIRD evidence:** India (Rajasthan, Haryana), Kenya (M-SIMU; effect size unverified).
- **Replication status:** replicated, especially for one-off health actions and enrolment; crowding-out and decay documented.
- **Boundary conditions and backfire:** crowding out of intrinsic motivation (Gneezy); effects dissipate after removal; a US "regret lottery" (Philadelphia) found no pooled effect; prefer certain, immediate rewards over lotteries for complex behaviours; set the amount relative to the hassle; decide whether to monitor conditions; plan what happens when the incentive stops.
- **Practitioner sources:** J-PAL Rajasthan and Haryana pages (report, no URLs).
- **Corrections / cautions for the drafter:** the lottery meta-analyses in the design report (certain ES 0.55 vs uncertain 0.17; a 35-RCT network meta with lottery RR 1.43) have unverified authors; do not cite them.
- **Suggested io types:** produces `intervention-draft`.

### `choose-message-frame` (stage: design; proposed weird: mixed-evidence)
- **Anchor citations:**
  - Gallagher, K. M., & Updegraff, J. A. (2012). Health message framing effects on attitudes, intentions, and behavior: A meta-analytic review. *Annals of Behavioral Medicine*, 43, 101–116. https://doi.org/10.1007/s12160-011-9308-7 [verified-crossref] (audit year 2011, online-first; an erratum exists, 10.1007/s12160-012-9446-6, seen in the Crossref search)
  - Ferraro & Tracy (2022), A9 [verified-crossref]
  - Fryer, R. G., Levitt, S. D., List, J., & Sadoff, S. (2022). Enhancing the efficacy of teacher incentives through framing: A field experiment. *American Economic Journal: Economic Policy*. https://doi.org/10.1257/pol.20190287 [verified-crossref]; working paper: Fryer et al. (2012). Enhancing the efficacy of teacher incentives through loss aversion: A field experiment. NBER w18237. https://doi.org/10.3386/w18237 [verified-crossref]
  - Bulte, E., List, J. A., & van Soest, D. (2020). Toward an understanding of the welfare effects of nudges: Evidence from a field experiment in the workplace. *The Economic Journal*. https://doi.org/10.1093/ej/ueaa054 [verified-crossref] (NBER w26286 title says "...in Uganda", https://doi.org/10.3386/w26286 [verified-crossref]; the published title says "in the Workplace")
  - Karlan et al. (2016) [verified-crossref]; Hallsworth et al. (2017) [verified-crossref]
- **Numbers to quote:** message framing: 94 studies, 189 effect sizes; gain frames beat loss frames for prevention behaviour, r = 0.083; no effect on attitudes or intentions, or for detection behaviour. Loss-framed contracts: pooled 0.16 SD; lab 0.33 vs field 0.02 SD; publication bias among lab studies. Fryer: 0.20–0.40 SD in the 2012 working paper, revised to 0.124 SD in the 2022 published version, with no effect in wave 2. Uganda: about 1,000 peri-urban workers; loss-framed contracts raised productivity at modest welfare cost; effect size unverified; most workers prefer gain contracts and the gain appeared only among the roughly 20% who chose loss framing. Karlan reminders: no loss/gain difference. UK tax: no loss-frame advantage.
- **Non-WEIRD evidence:** Uganda (Bulte, List & van Soest); Bolivia/Peru/Philippines (Karlan, no frame effect).
- **Replication status:** contested; effects shrink sharply in the field.
- **Boundary conditions and backfire:** classify the behaviour as prevention or detection; default to gain frames for prevention; treat loss-framed contracts as low-yield in the field; A/B test rather than assume.
- **Practitioner sources:** none specific.
- **Corrections / cautions for the drafter:** Fryer revision (0.124 SD) must be the number quoted; title differences between the NBER and EJ versions of Bulte et al.
- **Suggested io types:** produces `intervention-draft`.

### `design-feedback-report` (stage: design; proposed weird: mixed-evidence)
- **Anchor citations:**
  - Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. *Psychological Bulletin*, 119, 254–284. https://doi.org/10.1037/0033-2909.119.2.254 [verified-crossref]
  - Allcott, H., & Rogers, T. (2014). The short-run and long-run effects of behavioral interventions: Experimental evidence from energy conservation. *American Economic Review*, 104(10), 3003–3037. https://doi.org/10.1257/aer.104.10.3003 [verified-crossref]
  - Muralidharan, K., & Sundararaman, V. (2010). The impact of diagnostic feedback to teachers on student learning: Experimental evidence from India. *The Economic Journal*. https://doi.org/10.1111/j.1468-0297.2010.02373.x [verified-crossref] (plan-only citation; the plan's result claim "null" is not in the three reports: author to confirm from the paper before stating it)
  - Schultz et al. (2007); Allcott (2011): see `write-social-norm-message`.
- **Numbers to quote:** d = 0.41 across 607 effect sizes, but more than one-third of feedback interventions reduced performance. Opower "action and backsliding": when reports stop after 2 years, effects decay 10–20% per year.
- **Non-WEIRD evidence:** India (Muralidharan & Sundararaman): citation verified; result to be confirmed. Otherwise none verified in the reports.
- **Replication status:** replicated, high heterogeneity; self-focused feedback backfires.
- **Boundary conditions and backfire:** keep feedback task-focused, not about the self; include a comparison with an injunctive cue; repeat it because effects decay when it stops; watch for performance falls among people already doing well.
- **Practitioner sources:** none specific.
- **Corrections / cautions for the drafter:** do not write "null" for the India study until confirmed.
- **Suggested io types:** produces `intervention-draft`.

### `design-habit-anchor` (stage: design; proposed weird: untested-outside-weird)
- **Anchor citations:**
  - Lally, P., van Jaarsveld, C. H. M., Potts, H. W. W., & Wardle, J. (2010). How are habits formed: Modelling habit formation in the real world. *European Journal of Social Psychology*, 40, 998–1009. https://doi.org/10.1002/ejsp.674 [verified-crossref] (audit year 2009, online-first)
  - Gardner, B., Lally, P., & Wardle, J. (2012). Making health habitual: The psychology of 'habit-formation' and general practice. *British Journal of General Practice*, 62(605), 664–666. https://doi.org/10.3399/bjgp12X659466 [verified-crossref]
  - Wood, W., & Neal, D. T. (2007). A new look at habits and the habit–goal interface. *Psychological Review*, 114(4). https://doi.org/10.1037/0033-295X.114.4.843 [verified-crossref] (report had it from memory; DOI located in this audit)
  - Milkman et al. (2021) megastudy, A10 [verified-crossref]
  - Blumenstock, Callen & Ghani (2018) [verified-crossref]
- **Numbers to quote:** median 66 days to automaticity, range 18–254 days; 96 volunteers, some missing data, self-reported automaticity. Megastudy: only 8% of 54 interventions produced effects that persisted after the program (US sample). Afghanistan: default savings led to persistent savings attitudes/habits after the trial.
- **Non-WEIRD evidence:** Afghanistan persistence (Blumenstock) only; no LMIC habit-formation study found.
- **Replication status:** mixed; the timeline rests on a small study.
- **Boundary conditions and backfire:** choose a stable existing cue ("after breakfast"); shrink the behaviour to its minimum version; supply a tick-sheet; plan for roughly 2–3 months rather than 21 days.
- **Practitioner sources:** none specific.
- **Corrections / cautions for the drafter:** do not cite "21 days" as evidence-based.
- **Suggested io types:** produces `intervention-draft`.

### `adapt-growth-mindset-message` (stage: design; proposed weird: mixed-evidence)
- **Anchor citations:**
  - Yeager, D. S., et al. (2019). A national experiment reveals where a growth mindset improves achievement. *Nature*, 573, 364–369. https://doi.org/10.1038/s41586-019-1466-y [verified-crossref]
  - Sisk, V. F., Burgoyne, A. P., Sun, J., Butler, J. L., & Macnamara, B. N. (2018). To what extent and under which circumstances are growth mind-sets important to academic achievement? Two meta-analyses. *Psychological Science*, 29(4), 549–571. https://doi.org/10.1177/0956797617739704 [verified-crossref]
  - Macnamara, B. N., & Burgoyne, A. P. (2023). Do growth mindset interventions impact students' academic achievement? A systematic review and meta-analysis with recommendations for best practices. *Psychological Bulletin*, 149(3–4), 133–173. https://doi.org/10.1037/bul0000352 [verified-crossref]
  - Burnette, J. L., et al. (2023). A systematic review and meta-analysis of growth mindset interventions: For whom, how, and why might such interventions work? *Psychological Bulletin*, 149(3–4), 174–205. https://doi.org/10.1037/bul0000368 [verified-crossref]
  - Outes-León, I., Sánchez, A., & Vakis, R. (2020). The power of believing you can get smarter: The impact of a growth-mindset intervention on academic achievement in Peru. World Bank Policy Research Working Paper 9141. https://doi.org/10.1596/1813-9450-9141 [verified-crossref]
  - Ganimian, A. J. (2020). Growth-mindset interventions at scale: Experimental evidence from Argentina. *Educational Evaluation and Policy Analysis*, 42(3), 417–438. https://doi.org/10.3102/0162373720938041 [verified-crossref]
  - Bettinger, E., Ludvigsen, S., Rege, M., Solli, I. F., & Yeager, D. (2018). Increasing perseverance in math: Evidence from a field experiment in Norway. *Journal of Economic Behavior & Organization*, 146, 1–15. https://doi.org/10.1016/j.jebo.2017.11.032 [verified-crossref]
- **Numbers to quote:** Sisk: d = 0.08 (k = 43, N = 57,155); about 0.19 for high-risk students and 0.34 for low-SES students, on limited evidence. Macnamara & Burgoyne: 94% of interventions were confounded; authors with financial incentives reported larger effects. Burnette: positive effects for those expected to benefit, with large variation. US national study: about +0.10 GPA among lower achievers (Education Week, secondary source per report). Peru (¡Expande tu Mente!, 90 minutes, about $0.20 per pupil, more than 50,000 students): math gains of 0.14 SD by the World Bank's figure, 0.05–0.25 depending on estimator, larger outside Lima; the World Bank summary says about 0.2 SD. These figures conflict; quote the range and say so. Argentina (Salta, 202 schools): null, with small effects ruled out. Norway: improved perseverance.
- **Non-WEIRD evidence:** Peru (positive, modest), Argentina (null); Indonesia replication "Semua Bisa Pintar!" (about 160,000 students) and a South Africa adaptation exist per the labs report, with no results cited.
- **Replication status:** contested.
- **Boundary conditions and backfire:** target lower-achieving students; check that peer and teacher norms support the message (Yeager 2019); deliver in one session; measure grades or test scores rather than beliefs.
- **Practitioner sources:** World Bank eMBeD Peru brief (report, no URL).
- **Corrections / cautions for the drafter:** state the conflicting Peru estimates rather than one number.
- **Suggested io types:** produces `intervention-draft`.

### `draft-belonging-story` (stage: design; proposed weird: untested-outside-weird)
- **Anchor citations:**
  - Walton, G. M., & Cohen, G. L. (2011). A brief social-belonging intervention improves academic and health outcomes of minority students. *Science*, 331(6023), 1447–1451. https://doi.org/10.1126/science.1198364 [verified-crossref]
  - Walton et al. (2023) *Science* 380(6644), 499–505 [verified-crossref] (erratum noted above)
  - Walton & Wilson (2018), B8 [verified-crossref]
- **Numbers to quote:** original study N = 92; the achievement gap roughly halved over 3 years. 2023: 26,911 students, 22 institutions; raised full-time first-year completion only where the group was afforded opportunities to belong.
- **Non-WEIRD evidence:** none found in the three reports.
- **Replication status:** replicated, with conditions (context affordance).
- **Boundary conditions and backfire:** collect real stories from older peers; frame difficulty as normal and improvable; include the "saying-is-believing" step (recipient writes advice to future peers); deliver before the transition; check the context affords belonging.
- **Practitioner sources:** none.
- **Corrections / cautions for the drafter:** all evidence is US college; say so.
- **Suggested io types:** produces `intervention-draft`.

### `design-social-recognition` (stage: design; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Karing, A. (2016). Social signaling in childhood immunization: Evidence from a field experiment in Sierra Leone. AEA RCT Registry. https://doi.org/10.1257/rct.1299 [verified-crossref] (registry record; the plan's "Karing 2018, verify journal version": no journal version was located in Crossref, so cite the registry and tag the journal version [unverified, author to confirm])
  - Ashraf, N., Bandiera, O., & Jack, B. K. (2014). No margin, no mission? A field experiment on incentives for public service delivery. *Journal of Public Economics*, 120, 1–17. https://doi.org/10.1016/j.jpubeco.2014.06.014 [verified-crossref]
  - Bénabou, R., & Tirole, J. (2006). Incentives and prosocial behavior. *American Economic Review*, 96(5). https://doi.org/10.1257/aer.96.5.1652 [verified-crossref] (plan-only citation)
- **Numbers to quote:** Sierra Leone: bracelets raised timely, complete vaccination by 14.4 points (about 56% to 71%) (search snippet per report). Zambia: non-financial rewards (public recognition) improved hairdressers' condom sales, more for prosocially motivated agents; effect size unverified.
- **Non-WEIRD evidence:** the evidence base is non-WEIRD (Sierra Leone, Zambia); eMBeD Nigeria (Ekiti) compared social recognition vs lottery incentives for health record-keeping, effect size not retrieved.
- **Replication status:** two strong LMIC RCTs (plan); the Sierra Leone paper is verified only as a registry entry.
- **Boundary conditions and backfire:** choose a culturally meaningful visible token; tie it to verified completion; make sure the signal is valued locally; watch for stigma among people who do not receive it.
- **Practitioner sources:** eMBeD Results Portfolio (documents.worldbank.org 688661608104181834; existence only per report).
- **Corrections / cautions for the drafter:** Karing journal version unverified.
- **Suggested io types:** produces `intervention-draft`.

### `select-messenger` (stage: design; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Dolan et al. (2012) MINDSPACE, B5 [verified-crossref] ("Messenger")
  - Banerjee, A., Chandrasekhar, A. G., Duflo, E., & Jackson, M. O. (2019). Using gossips to spread information: Theory and evidence from two randomized controlled trials. *The Review of Economic Studies*. https://doi.org/10.1093/restud/rdz008 [verified-crossref] (plan-only citation; the design report calls the related network work "unverified"; this audit confirms the citation, not its results)
  - Banerjee et al. (2025) *Econometrica* 93(4), 1183–1223 [verified-crossref]
- **Numbers to quote:** Haryana: information-hub ambassadors plus SMS were the most cost-effective option (+9.1% immunizations per dollar); hubs improved full immunization; SMS alone had no impact (J-PAL page, secondary source per report).
- **Non-WEIRD evidence:** India (Haryana); Karnataka "gossips" trials (citation verified, results not in the reports); Indonesia named in the plan without a citation in the reports.
- **Replication status:** replicated in India (Haryana plus the gossips trials); single large study for the ambassador bundle.
- **Boundary conditions and backfire:** nominate central people with the "gossip"/information-hub question; brief them; pair with SMS reminders; compare against randomly chosen messengers.
- **Practitioner sources:** J-PAL Haryana page (report, no URL).
- **Corrections / cautions for the drafter:** do not quote gossips-trial numbers; none are in the reports.
- **Suggested io types:** produces `intervention-draft`.

### `audit-intervention-ethics` (stage: design; proposed weird: not-applicable, procedural)
- **Anchor citations:**
  - OECD (2022). *Good practice principles for ethical behavioural science in public policy*. OECD Public Governance Policy Papers. https://doi.org/10.1787/e19a9be9-en [verified-crossref] (DOI located in this audit; published 5 Oct 2022 per the labs report)
  - Sunstein, C. R. (2015). The ethics of nudging. *Yale Journal on Regulation*, 32(2), 413. [verified-fetch: https://www.yalejreg.com/print/the-ethics-of-nudging/] (page gives vol. 32, issue 2; year and starting page from the PDF filename); SSRN version https://doi.org/10.2139/ssrn.2526341 [verified-crossref] (2014)
  - OECD (2019) BASIC toolkit, B12 [verified-crossref] (ethics section)
  - Lades, L. K., & Delaney, L. (2022). Nudge FORGOOD. *Behavioural Public Policy*, 6(1). https://doi.org/10.1017/bpp.2019.53 [verified-crossref] (audit year 2020, online-first; plan-only citation)
  - Related, from the labs report: Mathur, A., et al. (2019). Dark patterns at scale. *Proceedings of the ACM on Human-Computer Interaction*, 3(CSCW), 81. https://doi.org/10.1145/3359183 [verified-crossref]; Gray, C. M., et al. (2018). The dark (patterns) side of UX design. *CHI 2018*. https://doi.org/10.1145/3173574.3174108 [verified-crossref]
- **Numbers to quote:** none (normative). Mathur: 15 dark-pattern types in 7 categories from ~11k sites; Gray: 5 categories from 118 practitioner examples (labs report).
- **Non-WEIRD evidence:** none; the CLTS shaming literature is a case but no specific paper was verified.
- **Replication status:** normative.
- **Boundary conditions and backfire:** apply OECD principles; autonomy, welfare and dignity tests (Sunstein); transparency; data and consent; FORGOOD: the reports give only the acronym and title; do not expand the acronym into dimensions without reading the paper.
- **Practitioner sources:** OECD; BIT.
- **Corrections / cautions for the drafter:** the plan dates Lades & Delaney 2022; it appeared online 2020 in BPP.
- **Suggested io types:** none assigned in the plan (consuming `intervention-draft` is natural; confirm with the taxonomy).

### measure

Steers around Patricia's "existing measure finder" and "ad hoc psychometric development guide": nothing here finds or validates a scale.

### `translate-survey-instrument` (stage: measure; proposed weird: likely-generalizes; **adjacent** to Patricia's psychometric guide: translation, not scale development)
- **Anchor citations:**
  - International Test Commission (2018). ITC Guidelines for Translating and Adapting Tests (Second Edition). *International Journal of Testing*, 18(2), 101–134. https://doi.org/10.1080/15305058.2017.1398166 [verified-crossref] (audit year 2017, online-first; no author field in Crossref; the report credits Bartram, Berberoglu, Grégoire, Hambleton, Muñiz & van de Vijver)
  - Beaton, D. E., et al. (2000). Guidelines for the process of cross-cultural adaptation of self-report measures. *Spine*, 25(24), 3186–3191. https://doi.org/10.1097/00007632-200012150-00014 [verified-crossref]
  - Sousa, V. D., & Rojjanasrirat, W. (2011). Translation, adaptation and validation of instruments or scales for use in cross-cultural health care research: A clear and user-friendly guideline. *Journal of Evaluation in Clinical Practice*, 17(2), 268–274. https://doi.org/10.1111/j.1365-2753.2010.01434.x [verified-crossref]
  - Harkness, J. A. (2003). TRAPD (Translation, Review, Adjudication, Pretest, Documentation), in Harkness, van de Vijver & Mohler (eds.), *Cross-Cultural Survey Methods*. Wiley. [unverified, author to confirm] (the edited book exists per OpenLibrary, https://openlibrary.org/search.json?title=cross-cultural+survey+methods&author=harkness, first publish year 2002/2003; the TRAPD chapter attribution was not confirmed)
  - J-PAL, *Survey design* resource (translation section: a fluent speaker translates, then an independent back-translation) [verified-fetch: https://www.povertyactionlab.org/resource/survey-design]
- **Numbers to quote:** ITC: 18 guidelines in 6 sections.
- **Non-WEIRD evidence:** a systematic review of Beaton use in Brazil (Revista Mundo da Saúde) exists per the report, with no citation details: [unverified, author to confirm]. The plan's "WHO instrument-translation process" is not in the three reports; do not cite it.
- **Replication status:** back-translation is debated: the TRAPD/Harkness school treats it as weak QA; Beaton keeps it as a core stage; J-PAL recommends it.
- **Boundary conditions and backfire:** two or more independent forward translations; reconcile in committee; optional back-translation; pretest with cognitive interviews (existing `draft-cognitive-interview-script`); document every decision.
- **Practitioner sources:** J-PAL survey design (above); EGAP "10 Things to Know About Survey Design" [verified-fetch: https://egap.org/resource/10-things-to-know-about-survey-design/] (listed on the methods-guides page; the guide itself was not fetched).
- **Corrections / cautions for the drafter:** none beyond the unverified items.
- **Suggested io types:** produces `survey-items`.

### `draft-survey-items` (stage: measure; proposed weird: mixed-evidence)
- **Anchor citations:**
  - Krosnick, J. A., & Presser, S. (2010). Question and questionnaire design. In P. V. Marsden & J. D. Wright (Eds.), *Handbook of Survey Research* (2nd ed.). Emerald. [verified-fetch: https://openlibrary.org/search.json?title=handbook+of+survey+research&author=marsden] (the handbook record, Marsden & Wright, first publish year 2009, is confirmed; the chapter itself was not seen, its title and authors are from the report)
  - Tourangeau, R., Rips, L. J., & Rasinski, K. (2000). *The Psychology of Survey Response*. Cambridge University Press. https://doi.org/10.1017/CBO9780511819322 [verified-crossref] (report had it from memory; DOI located in this audit)
  - Laajaj, R., & Macours, K. (2021). Measuring skills in developing countries. *Journal of Human Resources*, 56(4), 1254–1295. https://doi.org/10.3368/jhr.56.4.1018-9805R1 [verified-crossref] (audit year 2019, online-first)
  - Harzing, A.-W. (2006). Response styles in cross-national survey research: A 26-country study. *International Journal of Cross Cultural Management*, 6(2), 243–266. https://doi.org/10.1177/1470595806066332 [verified-crossref] (related: acquiescence and extreme responding)
  - J-PAL *Survey design* [verified-fetch: https://www.povertyactionlab.org/resource/survey-design] ("Each question should be SMART"; Likert, ranked, numeracy and frequency scales; central tendency bias; sensitive-question techniques)
  - EGAP "10 Things to Know About Survey Design" [verified-fetch: https://egap.org/resource/10-things-to-know-about-survey-design/] (listing confirmed; guide not fetched)
- **Numbers to quote:** none verified. The Kenya finding ("standard noncognitive scales showed weak reliability and validity"; acquiescence bias) is attributed to Laajaj & Macours but the report marks the specific finding as from memory: [unverified, author to confirm] the wording before quoting.
- **Non-WEIRD evidence:** Kenya (Laajaj & Macours), with the caution above.
- **Replication status:** evidence base mostly US and Europe; Kenya shows the failure modes.
- **Boundary conditions and backfire:** no double-barreled items; balanced options; labeled scale points; sensible option order; choose the number of scale points; reverse-keyed items can themselves cause problems in low-literacy samples; pretest with cognitive interviews.
- **Practitioner sources:** J-PAL and EGAP (above); BIT *Explore Field Guide* survey section (three steps, response rates) [verified-fetch: https://www.bi.team/wp-content/uploads/2022/11/BIT-Explore-Field-Guide.pdf].
- **Corrections / cautions for the drafter:** Dillman *Tailored Design Method* and DeVellis were unverified in the report and are not in this dossier.
- **Suggested io types:** produces `survey-items`.

### `adapt-survey-for-phone-mode` (stage: measure; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Hoogeveen, J., Dabalen, A., et al. (2016). *Mobile Phone Panel Surveys in Developing Countries: A Practical Guide for Microdata Collection*. World Bank. https://doi.org/10.1596/978-1-4648-0904-0 [verified-crossref]
  - Gourlay, S., et al. (2021). Viewpoint: High-frequency phone surveys on COVID-19: Good practices, open questions. *Food Policy*, 105, 102153. https://doi.org/10.1016/j.foodpol.2021.102153 [verified-crossref]
  - J-PAL, *Resources for conducting remote surveys* [verified-fetch: https://www.povertyactionlab.org/resource/resources-conducting-remote-surveys]
- **Numbers to quote:** J-PAL: "surveys should be kept to a 30 minute call at most" (fetched). The report's "shorten to about 15–20 minutes" is [U]: do not quote.
- **Non-WEIRD evidence:** both sources are LMIC-specific (LSMS high-frequency phone surveys).
- **Replication status:** phone samples skew toward phone owners.
- **Boundary conditions and backfire:** replace showcards with verbal unfolding scales; plan call protocol (scheduling, recording attempts, replacing respondents, matching surveyors by language) and incentives; test for mode effects against a face-to-face subsample.
- **Practitioner sources:** J-PAL (above): covers survey length, respondent tracking and call scheduling; it does not cover mode effects or IVR. World Bank LSMS and DIME Wiki [unverified, author to confirm] (DIME returned 403 in the research session).
- **Corrections / cautions for the drafter:** do not attribute mode-effect or IVR guidance to the J-PAL page.
- **Suggested io types:** none assigned in the plan.

### `design-list-experiment` (stage: measure; proposed weird: mixed-evidence)
- **Anchor citations:**
  - Blair, G., & Imai, K. (2012). Statistical analysis of list experiments. *Political Analysis*, 20(1), 47–77. https://doi.org/10.1093/pan/mpr048 [verified-crossref]
  - Blair, G., Coppock, A., & Moor, M. (2020). When to worry about sensitivity bias: A social reference theory and evidence from 30 years of list experiments. *American Political Science Review*, 114(4), 1297–1315. https://doi.org/10.1017/S0003055420000374 [verified-crossref]
  - Chuang, E., Dupas, P., Huillery, E., & Seban, J. (2021). Sex, lies, and measurement: Consistency tests for indirect response survey methods. *Journal of Development Economics*. https://doi.org/10.1016/j.jdeveco.2020.102582 [verified-crossref] (the report's recalled DOI returned 404; this DOI located in this audit)
- **Numbers to quote:** Blair, Coppock & Moor: sensitivity bias is usually under 10 points; list experiments cost variance (report).
- **Non-WEIRD evidence:** Cameroon / Côte d'Ivoire (Chuang et al.); vote-buying studies across many countries in the 30-year meta-analysis.
- **Replication status:** low power; does not always beat direct questions; comprehension problems in low-literacy samples.
- **Boundary conditions and backfire:** 3–5 control items without floor or ceiling problems; randomize the sensitive item into the treatment list; power for a difference in means; analyze with design-effect tests (the `list` R package).
- **Practitioner sources:** EGAP "10 Things to Know About Survey Experiments" [verified-fetch: https://egap.org/resource/10-things-to-know-about-survey-experiments/] (listing only). IPA / J-PAL use [U].
- **Corrections / cautions for the drafter:** Chuang DOI corrected.
- **Suggested io types:** none assigned in the plan.

### `design-mystery-client-protocol` (stage: measure; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Das, J., Holla, A., Das, V., Mohanan, M., Tabak, D., & Chan, B. (2012). In urban and rural India, a standardized patient study showed low levels of provider training and huge quality gaps. *Health Affairs*, 31(12), 2774–2784. https://doi.org/10.1377/hlthaff.2011.1356 [verified-crossref]
  - Kwan, A., et al. (2019). Use of standardised patients for healthcare quality research in low- and middle-income countries. *BMJ Global Health*, 4, e001669. https://doi.org/10.1136/bmjgh-2019-001669 [verified-crossref] (plan-only citation; audit confirms first author, year, title)
  - "King, Das et al." (plan) [unverified, author to confirm] (no title given; not located)
- **Numbers to quote:** 926 interactions, 305 providers, Delhi and Madhya Pradesh.
- **Non-WEIRD evidence:** LMIC-native method (India; the plan also names Kenya and China without citations in the reports).
- **Replication status:** method established; deception ethics and detection rates must be justified.
- **Boundary conditions and backfire:** script the case presentations; recruit and train local SPs; essential-checklist rubric; plan ethics waivers and detection checks.
- **Practitioner sources:** none specific.
- **Corrections / cautions for the drafter:** author list is Das, Holla, Das, Mohanan, Tabak & Chan; there is no author named Mohpal.
- **Suggested io types:** none assigned in the plan.

### `draft-norms-vignette` (stage: measure; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Atzmüller, C., & Steiner, P. M. (2010). Experimental vignette studies in survey research. *Methodology*, 6(3), 128–138. https://doi.org/10.1027/1614-2241/a000014 [verified-crossref]
  - Bicchieri (2016), ch. 2 "Measuring Norms", B13 [verified-crossref]
  - IRH SNET (2020) [verified-fetch: https://www.irh.org/social-norms-exploration/] (the report says it includes a sample vignette and a rapid-analysis template; the fetched page does not mention vignettes)
- **Numbers to quote:** none.
- **Non-WEIRD evidence:** SNET pilots (15+ settings); UNICEF trainings in Viet Nam, Indonesia, Philippines (labs report).
- **Replication status:** factorial-vignette design guidance is peer-reviewed; causal claims about norms need the factorial variation of empirical and normative cues.
- **Boundary conditions and backfire:** fix the dilemma; vary empirical and normative cues factorially; ask what others would do or think; analyze accordingly.
- **Practitioner sources:** SNET; UNICEF/Penn manual [unverified].
- **Corrections / cautions for the drafter:** the SNET sample vignette is asserted by the report, not confirmed by this audit.
- **Suggested io types:** none assigned in the plan.

### test

### `estimate-expected-effect` (stage: test; proposed weird: mixed-evidence)
- **Anchor citations:** Mertens et al. (2022), A1; Maier et al. (2022), A2; Szaszi et al. (2022), A3; DellaVigna & Linos (2022), A4; Ferraro & Tracy (2022), A9; Hummel & Maedche (2019), A7; Milkman et al. (2021), A10 [all verified-crossref]; Kraft, M. A. (2020). Interpreting effect sizes of education interventions. *Educational Researcher*, 49, 241–253. https://doi.org/10.3102/0013189X20912798 [verified-crossref]; Brandon et al. (2017) persistence, see E12 [verified-crossref].
- **Numbers to quote:** d = 0.45 (0.39–0.52) per the Mertens abstract, 0.43 in some secondary sources; bias-corrected ≈ 0.04 (Maier); 0.03–0.31 range (Szaszi 2022); 8.7 vs 1.4 points, ~70% of the gap from selective publication and low power (DellaVigna & Linos); 0.33 lab vs 0.02 field SD (Ferraro & Tracy); 8% of 54 interventions persisted (Milkman 2021). Kraft's benchmarks are US education RCTs.
- **Non-WEIRD evidence:** DellaVigna & Linos covers US units only; the plan's "LMIC benchmarks from J-PAL evidence per domain" are not in the reports and must be added by the author.
- **Replication status:** the whole point: effects shrink in the field; mixed-evidence.
- **Boundary conditions and backfire:** benchmarks are domain-specific; do not apply Cohen's labels.
- **Practitioner sources:** J-PAL power calculations page notes effect sizes are usually set too optimistically (report) [verified-fetch: https://www.povertyactionlab.org/resource/power-calculations].
- **Corrections / cautions for the drafter:** the plan writes "d≈0.43" for Mertens; the abstract says 0.45.
- **Suggested io types:** produces `effect-size-benchmark` (new; consumed by `estimate-sample-size`).

### `estimate-sample-size` (stage: test; proposed weird: not-applicable, procedural; note US ICC skew)
- **Anchor citations:**
  - Bloom, H. S. (1995). Minimum detectable effects. *Evaluation Review*, 19(5), 547–556. https://doi.org/10.1177/0193841X9501900504 [verified-crossref]
  - McConnell, B., & Vera-Hernández, M. (2025). Going beyond simple sample size calculations: A practitioner's guide. *Fiscal Studies*, 46(3), 323–348. https://doi.org/10.1111/1475-5890.70005 [verified-crossref]; IFS Working Paper W15/17, https://doi.org/10.1920/wp.ifs.2015.1517 [verified-crossref] (Crossref year metadata reads 2026; the report dates the WP 2015)
  - Vera Hernández, A., & McConnell, B. (2024). *Sample size calculators (Going beyond simple sample size calculations: a practitioner's guide)*. UCL figshare. https://doi.org/10.5522/04/25373830.v1 [verified-fetch: https://api.datacite.org/dois/10.5522%2F04%2F25373830.v1] (DataCite record: UCL, 2024)
  - Hedges, L. V., & Hedberg, E. C. (2007). Intraclass correlation values for planning group-randomized trials in education. *Educational Evaluation and Policy Analysis*, 29(1), 60–87. https://doi.org/10.3102/0162373707299706 [verified-crossref] (US data)
  - Gelman, A., & Carlin, J. (2014). Beyond power calculations. *Perspectives on Psychological Science*, 9(6), 641–651. https://doi.org/10.1177/1745691614551642 [verified-crossref] (Type S and Type M errors)
  - J-PAL, *Power calculations* [verified-fetch: https://www.povertyactionlab.org/resource/power-calculations] (MDE, ICC, clustered designs, attrition, take-up; links a power calculator and Stata/R code)
  - EGAP "10 Things to Know About Statistical Power" [verified-fetch: https://egap.org/resource/10-things-to-know-about-statistical-power/] (listing only)
- **Numbers to quote:** design effect 1 + (m − 1)ρ (standard formula, report). No empirical numbers.
- **Non-WEIRD evidence:** the IFS authors' calculators come from LMIC-experienced authors; LMIC ICC compilations are scarce. Kelcey, Shen & Spybrook (2016) sub-Saharan ICCs is [unverified, author to confirm]. Cohen (1988) is unverified and not needed.
- **Replication status:** uncontested method.
- **Boundary conditions and backfire:** effect sizes in power calculations are usually set too optimistically; US ICCs may not transfer; report MDES rather than only N; adjust for covariates, take-up and attrition.
- **Practitioner sources:** J-PAL and EGAP (above); World Bank "Power Dashboard" (Kondylis & Loeser) is linked from the J-PAL page.
- **Corrections / cautions for the drafter:** none.
- **Suggested io types:** consumes `effect-size-benchmark`; produces `power-calculation` (new; consumed by `plan-evaluation-design`, `design-evidential-experiment`).

### `choose-trial-design` (stage: test; proposed weird: not-applicable)
- **Anchor citations:**
  - Hemming, K., et al. (2015). The stepped wedge cluster randomised trial: Rationale, design, analysis, and reporting. *BMJ*, 350, h391. https://doi.org/10.1136/bmj.h391 [verified-crossref]
  - Hayes, R. J., & Moulton, L. H. (2009). *Cluster Randomised Trials*. Chapman & Hall/CRC. https://doi.org/10.1201/9781584888178 [verified-crossref] (report had it from memory; book DOI located in this audit)
  - Collins, L. M. (2018). *Optimization of Behavioral, Biobehavioral, and Biomedical Interventions: The Multiphase Optimization Strategy (MOST)*. Springer. https://doi.org/10.1007/978-3-319-72206-1 [verified-crossref]
  - EGAP "10 Things to Know About Cluster Randomization" [verified-fetch: https://egap.org/resource/10-things-to-know-about-cluster-randomization/] (listing only); "...Multisite or Block-Randomized Trials" at https://egap.org/resource/10-things-to-know-about-multisite-or-block-randomized-trials/
- **Numbers to quote:** none.
- **Non-WEIRD evidence:** stepped-wedge suits phased rollouts common in LMIC programs (Hemming abstract, per report).
- **Replication status:** stepped-wedge is confounded with time trends; factorial designs assume mostly additive component effects.
- **Boundary conditions and backfire:** list constraints (spillovers, rollout, ethics); map each to a design; check the power implications.
- **Practitioner sources:** EGAP (above); J-PAL "Randomization" page (report V, not fetched here).
- **Corrections / cautions for the drafter:** none.
- **Suggested io types:** none assigned in the plan.

### `design-adaptive-message-experiment` (stage: test; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Offer-Westort, M., Coppock, A., & Green, D. P. (2021). Adaptive experimental design: Prospects and applications in political science. *American Journal of Political Science*. https://doi.org/10.1111/ajps.12597 [verified-crossref]
  - Kasy, M., & Sautmann, A. (2021). Adaptive treatment assignment in experiments for policy choice. *Econometrica*, 89(1), 113–132. https://doi.org/10.3982/ECTA17527 [verified-crossref]
  - EGAP "10 Things to Know About Adaptive Experimental Design" [verified-fetch: https://egap.org/resource/10-things-to-know-about-adaptive-experimental-design/] (listing only)
  - Banerjee et al. (2025) *Econometrica* [verified-crossref] (75 arms; treatment-variant aggregation with a winner's-curse correction)
- **Numbers to quote:** none beyond Haryana (see `select-messenger`).
- **Non-WEIRD evidence:** Kasy & Sautmann application: agricultural extension recruitment in India; Precision Development lists the paper (report).
- **Replication status:** standard errors after adaptive assignment are biased; the report recalls a published correction to the Kasy & Sautmann optimality result: [unverified, author to confirm].
- **Boundary conditions and backfire:** define arms and reward metric; pick an algorithm (Thompson sampling, exploration sampling); set the batch schedule; pre-specify inference that accounts for adaptive assignment.
- **Practitioner sources:** EGAP (above); PxD practice (report).
- **Corrections / cautions for the drafter:** do not state that a correction to Kasy & Sautmann exists unless confirmed.
- **Suggested io types:** none assigned in the plan.

### `design-pilot-feasibility-study` (stage: test; proposed weird: not-applicable)
- **Anchor citations:**
  - Eldridge, S. M., et al. (2016). CONSORT 2010 statement: Extension to randomised pilot and feasibility trials. *BMJ*, 355, i5239. https://doi.org/10.1136/bmj.i5239 [verified-crossref]
  - Bowen, D. J., et al. (2009). How we design feasibility studies. *American Journal of Preventive Medicine*, 36(5), 452–457. https://doi.org/10.1016/j.amepre.2009.02.002 [verified-crossref]
  - EGAP "10 Things to Know About Pilot Studies" [verified-fetch: https://egap.org/resource/10-things-to-know-about-pilot-studies/] (listing only)
- **Numbers to quote:** none.
- **Non-WEIRD evidence:** none specific in the reports; TIPs (diagnose) is the household-level LMIC cousin.
- **Replication status:** method guidance; pilots are often wrongly used to estimate effect sizes for power.
- **Boundary conditions and backfire:** define feasibility questions (recruitment, retention, fidelity, acceptability); set go/no-go progression thresholds; size for estimation, not significance.
- **Practitioner sources:** EGAP (above); J-PAL questionnaire piloting resource (report V, not fetched).
- **Corrections / cautions for the drafter:** none.
- **Suggested io types:** none assigned in the plan.

### `write-pre-analysis-plan` (stage: test; proposed weird: not-applicable)
- **Anchor citations:**
  - Olken, B. A. (2015). Promises and perils of pre-analysis plans. *Journal of Economic Perspectives*, 29(3), 61–80. https://doi.org/10.1257/jep.29.3.61 [verified-crossref]
  - Coffman, L. C., & Niederle, M. (2015). Pre-analysis plans have limited upside, especially where replications are feasible. *Journal of Economic Perspectives*, 29(3), 81–98. https://doi.org/10.1257/jep.29.3.81 [verified-crossref]
  - Banerjee, A., et al. (2020). In praise of moderation: Suggestions for the scope and use of pre-analysis plans for RCTs in economics. NBER Working Paper 26993. https://doi.org/10.3386/w26993 [verified-crossref] (the plan and report say "Duflo et al."; Crossref lists Banerjee as first author; co-authors not captured by the audit)
  - AEA RCT Registry [verified-fetch: https://www.socialscienceregistry.org/] ("The American Economic Association's registry for randomized controlled trials")
  - Office of Evaluation Sciences (2021). *Analysis Plan* template, July 2021. [verified-fetch: https://oes.gsa.gov/assets/files/AnalysisPlan.pdf] (sections read: project description, preregistration details, hypotheses, data and data structure, outcomes, transformations, exclusion, missing data, descriptive statistics, statistical models and hypothesis tests; "finalized and date-stamped before we take possession of outcome data")
  - J-PAL, *Pre-analysis plans* [verified-fetch: https://www.povertyactionlab.org/resource/pre-analysis-plans] ("A PAP should be concise and focused, rather than attempt to be exhaustive"; populated PAP as a separate document)
  - EGAP "10 Things to Know About Pre-Analysis Plans" [verified-fetch: https://egap.org/resource/10-things-to-know-about-pre-analysis-plans/] (listing only)
- **Numbers to quote:** none.
- **Non-WEIRD evidence:** development-economics origin (Olken; Banerjee et al.).
- **Replication status:** debated level of detail: Coffman & Niederle see limited upside; Banerjee et al. argue for moderation; OES pre-specifies and date-stamps.
- **Boundary conditions and backfire:** fill the AEA registry fields; add detail only where it matters (subgroups, vested interests); later publish a populated PAP. Christensen & Miguel (2018) *JEL* is unverified and not included.
- **Practitioner sources:** OES, J-PAL, EGAP, AEA registry (above); OES "six-gate evaluation policy" (labs report).
- **Corrections / cautions for the drafter:** first author of the "moderation" paper is Banerjee. The measure/test report flags possible overlap with the existing `plan-evaluation-design`; keep this skill to the analysis-plan document.
- **Suggested io types:** consumes `evaluation-design`; produces `analysis-plan`.

### analyze

### `analyze-doer-nondoer-differences` (stage: analyze; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Kittle (2013; 2nd ed. 2017), lessons 5 and 12 [verified-fetch: https://coregroup.org/resource-library/a-practical-guide-to-conducting-a-barrier-analysis/] (see `draft-barrier-analysis-questionnaire`)
  - CORE Group (2013) DBC guide [verified-fetch: https://coregroup.org/resource-library/designing-for-behavior-change-for-agriculture-natural-resource-management-health-and-nutrition/]
- **Numbers to quote:** 45 Doers vs 45 Non-Doers (case-control calculation, RR 3.0, 80% power); flag a determinant when the Doer/Non-Doer gap is at least 15 percentage points or p < .05 in the Barrier Analysis Excel tabulation sheet; write "Bridges to Activities" for flagged determinants.
- **Non-WEIRD evidence:** LMIC-native (same as the questionnaire skill).
- **Replication status:** heuristic thresholds; no validation.
- **Boundary conditions and backfire:** the 15-point rule is a convention; CORE's association between tool use and behaviour change is not a validation.
- **Practitioner sources:** CORE Group, Food for the Hungry.
- **Corrections / cautions for the drafter:** none.
- **Suggested io types:** produces `barrier-diagnosis`.

### `synthesize-interview-findings` (stage: analyze; proposed weird: not-applicable)
- **Anchor citations:**
  - Gale, N. K., et al. (2013). Using the framework method for the analysis of qualitative data in multi-disciplinary health research. *BMC Medical Research Methodology*, 13, 117. https://doi.org/10.1186/1471-2288-13-117 [verified-crossref]
  - Vindrola-Padros, C., & Johnson, G. A. (2020). Rapid techniques in qualitative research: A critical review of the literature. *Qualitative Health Research*, 30(10), 1596–1604. https://doi.org/10.1177/1049732320921835 [verified-crossref]
  - Atkins et al. (2017) [verified-crossref] (TDF coding)
  - Braun, V., & Clarke, V. (2019). Reflecting on reflexive thematic analysis. *Qualitative Research in Sport, Exercise and Health*, 11(4), 589–597. https://doi.org/10.1080/2159676X.2019.1628806 [verified-crossref] (the contrast: reflexive TA rejects coding-reliability metrics); Braun & Clarke (2006), *Qualitative Research in Psychology*, 3(2), 77–101, https://doi.org/10.1191/1478088706qp063oa [verified-crossref]
  - Hamilton, A. B., & Finley, E. P. (2019). Qualitative methods in implementation research: An introduction. *Psychiatry Research*. https://doi.org/10.1016/j.psychres.2019.112516 [verified-crossref] (whether it covers rapid analysis is unconfirmed)
- **Numbers to quote:** none.
- **Non-WEIRD evidence:** "rapid methods are used in humanitarian settings" is [U] in the report: [unverified, author to confirm].
- **Replication status:** speed-versus-depth trade-off; method guidance, not an effect.
- **Boundary conditions and backfire:** build a summary template keyed to domains (COM-B or TDF); summarize each transcript; fill the matrix; compare across sites; TDF domains overlap.
- **Practitioner sources:** J-PAL "integrating qualitative methods" resource (report V, not fetched).
- **Corrections / cautions for the drafter:** none.
- **Suggested io types:** consumes `qualitative-data`; produces `barrier-diagnosis`.

### `audit-llm-qualitative-coding` (stage: analyze; proposed weird: mixed-evidence)
- **Anchor citations:**
  - Ashwin, J., Chhabra, A., & Rao, V. (2025). Using large language models for qualitative analysis can introduce serious bias. *Sociological Methods & Research*. https://doi.org/10.1177/00491241251338246 [verified-crossref] (DOI located in this audit); World Bank Policy Research Working Paper 10597 (2023), https://doi.org/10.1596/1813-9450-10597 [verified-crossref]
  - Than, N., Fan, L., Law, T., Nelson, L. K., & McCall, L. (2025). Updating "The Future of Coding": Qualitative coding with generative large language models. *Sociological Methods & Research*, 54(3), 849–888. https://doi.org/10.1177/00491241251339188 [verified-crossref] (co-authors and pages from the report; audit confirms first author, year, title)
  - Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement is not quality: Blind expert verification of human and LLM qualitative coding when human consensus is not ground truth. arXiv:2607.28890 (submitted 30 July 2026). [verified-fetch: https://arxiv.org/abs/2607.28890] (the report's "agreement-is-not-validity preprint")
- **Numbers to quote:** Ashwin et al.: LLM coding errors were not random with respect to respondent traits (Rohingya refugee and Bangladeshi host transcripts). Liu et al.: human–LLM agreement is lower than human–human agreement, but a blind expert found no reliable quality difference; "agreement-based evaluation is therefore insufficient for automation decisions".
- **Non-WEIRD evidence:** Ashwin et al. is an LMIC case (Bangladesh).
- **Replication status:** new method; state it.
- **Boundary conditions and backfire:** double-code a stratified subsample by hand; compute agreement by subgroup; test whether errors correlate with respondent traits; check run-to-run stability; agreement with humans is not validity.
- **Practitioner sources:** none.
- **Corrections / cautions for the drafter:** the preprint is a 2026 arXiv item; cite as a preprint.
- **Suggested io types:** consumes `qualitative-data`.

### `analyze-heterogeneous-effects` (stage: analyze; proposed weird: not-applicable)
- **Anchor citations:**
  - Bryan, Tipton & Yeager (2021), A8 [verified-crossref]
  - Wager, S., & Athey, S. (2018). Estimation and inference of heterogeneous treatment effects using random forests. *Journal of the American Statistical Association*, 113(523), 1228–1242. https://doi.org/10.1080/01621459.2017.1319839 [verified-crossref]
  - Chernozhukov, V., Demirer, M., Duflo, E., & Fernández-Val, I. (2025). Fisher–Schultz Lecture: Generic machine learning inference on heterogeneous treatment effects in randomized experiments, with an application to immunization in India. *Econometrica*, 93, 1121–1164. https://doi.org/10.3982/ECTA19303 [verified-crossref] (DOI located in this audit; a reply to comments also exists, 10.3982/ECTA23706); NBER w24678 (2018), https://doi.org/10.3386/w24678 [verified-crossref]
  - EGAP "10 Things to Know About Heterogeneous Treatment Effects" [verified-fetch: https://egap.org/resource/10-things-to-know-about-heterogeneous-treatment-effects/] (listing only)
- **Numbers to quote:** none.
- **Non-WEIRD evidence:** Chernozhukov et al. applications: immunization nudges in India (the Haryana experiment) and microcredit.
- **Replication status:** ML HTE is exploratory unless pre-specified; low power for subgroups.
- **Boundary conditions and backfire:** pre-specify theory-driven moderators; run causal forest or "generic ML" with sample splitting; report best linear predictor, effects by impact group, and characteristics of the most and least affected.
- **Practitioner sources:** EGAP (above).
- **Corrections / cautions for the drafter:** none.
- **Suggested io types:** none assigned in the plan.

### `adjust-for-multiple-comparisons` (stage: analyze; proposed weird: not-applicable)
- **Anchor citations:**
  - Anderson, M. L. (2008). Multiple inference and gender differences in the effects of early intervention: A reevaluation of the Abecedarian, Perry Preschool, and Early Training Projects. *Journal of the American Statistical Association*, 103(484), 1481–1495. https://doi.org/10.1198/016214508000000841 [verified-crossref]
  - Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B*, 57(1), 289–300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x [verified-crossref]
  - List, J. A., Shaikh, A. M., & Xu, Y. (2019). Multiple hypothesis testing in experimental economics. *Experimental Economics*, 22(4), 773–793. https://doi.org/10.1007/s10683-018-09597-5 [verified-crossref]
  - EGAP "10 Things to Know About Multiple Comparisons" [verified-fetch: https://egap.org/resource/10-things-to-know-about-multiple-comparisons/] (listing only)
- **Numbers to quote:** none.
- **Non-WEIRD evidence:** standard in development RCTs (no specific study cited in the reports).
- **Replication status:** FWER vs FDR is a judgment call.
- **Boundary conditions and backfire:** define outcome families; build standardized indices (Anderson); apply FDR (Benjamini–Hochberg or sharpened q-values) or FWER (List–Shaikh–Xu); pre-specify in the analysis plan.
- **Practitioner sources:** EGAP (above).
- **Corrections / cautions for the drafter:** none.
- **Suggested io types:** none assigned in the plan.

### `estimate-cost-effectiveness` (stage: analyze; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Dhaliwal, I., Duflo, E., Glennerster, R., & Tulloch, C. (2013). Comparative cost-effectiveness analysis to inform policy in developing countries. In *Education Policy in Developing Countries* (pp. 285–338). University of Chicago Press. https://doi.org/10.7208/chicago/9780226078854.003.0008 [verified-crossref]
  - J-PAL, *Conducting cost-effectiveness analysis (CEA)* (Bhula, Mahoney & Murphy) [verified-fetch: https://www.povertyactionlab.org/resource/conducting-cost-effectiveness-analysis-cea] ("A ten percent discount rate is applied for costs incurred over multiple years"; counts "the monetary value of both cash and in-kind transfers"; links costing guidelines and template)
  - Kraft (2020) [verified-crossref] (interpreting magnitude)
- **Numbers to quote:** Rajasthan: cost per fully immunized child fell from $55.83 to $27.94 with incentives (Banerjee 2010). Guatemala: about 36 times the letter cost (Kettle 2016). Haryana: +9.1% immunizations per dollar for hubs plus SMS (secondary source per report). J-PAL applies a 10% discount rate.
- **Non-WEIRD evidence:** LMIC-native (J-PAL comparative CEA).
- **Replication status:** treatment of transfers and discount rates is contested.
- **Boundary conditions and backfire:** ingredients-based costing; pick perspective, discount rate and currency year; compute impact per $100; run sensitivity analysis (the J-PAL page has no dedicated sensitivity section; it points to a guide on key decisions and assumptions).
- **Practitioner sources:** J-PAL (above).
- **Corrections / cautions for the drafter:** none.
- **Suggested io types:** none assigned in the plan.

### implement

### `assess-scalability` (stage: implement; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Milat, A. J., et al. (2020). Intervention Scalability Assessment Tool: A decision support tool for health policy makers and implementers. *Health Research Policy and Systems*, 18. https://doi.org/10.1186/s12961-019-0494-2 [verified-crossref]
  - Al-Ubaydli, O., List, J. A., & Suskind, D. (2020). 2017 Klein Lecture: The science of using science: Toward an understanding of the threats to scalability. *International Economic Review*, 61(4), 1387–1409. https://doi.org/10.1111/iere.12476 [verified-crossref]
  - Bold, T., et al. (2018). Experimental evidence on scaling up education reforms in Kenya. *Journal of Public Economics*, 168, 1–20. https://doi.org/10.1016/j.jpubeco.2018.08.007 [verified-crossref] (contract teachers, NGO vs government delivery)
  - Banerjee, A., et al. (2017). From proof of concept to scalable policies: Challenges and solutions, with an application. *Journal of Economic Perspectives*, 31(4), 73–102. https://doi.org/10.1257/jep.31.4.73 [verified-crossref] (Pratham Teaching at the Right Level)
  - List, J. A. (2022). *The Voltage Effect: How to Make Good Ideas Great and Great Ideas Scale*. Crown. [verified-fetch: https://openlibrary.org/isbn/9780593239483.json] (record confirms title, subtitle, publisher "Crown/Archetype", 2022; the author name is not in the record)
  - DellaVigna & Linos (2022), A4 [verified-crossref]
- **Numbers to quote:** none from the LMIC papers in the reports (Bold et al. and Banerjee et al. are cited for the NGO-vs-government contrast, no effect sizes given). DellaVigna & Linos: 8.7 vs 1.4 points.
- **Non-WEIRD evidence:** strong LMIC base: Kenya (Bold et al.), India (Banerjee et al. 2017).
- **Replication status:** well supported.
- **Boundary conditions and backfire:** score against ISAT domains; check the "voltage" threats (population representativeness, implementer quality, spillovers, cost); compare NGO vs government delivery.
- **Practitioner sources:** none specific beyond the above.
- **Corrections / cautions for the drafter:** none.
- **Suggested io types:** produces `scalability-assessment` (new; consumed by `plan-scale-up-strategy`).

### `plan-scale-up-strategy` (stage: implement; proposed weird: likely-generalizes)
- **Anchor citations:**
  - World Health Organization & ExpandNet (2010). *Nine steps for developing a scaling-up strategy*. WHO. [verified-fetch: https://www.who.int/publications/i/item/9789241500319] (dated 20 September 2010; 41 pages; ISBN 978 92 4 150031 9; "The aim of this guide is to facilitate systematic planning for scaling up")
  - Management Systems International, *Scaling Up Management* framework. [unverified, author to confirm] (msiworldwide.com redirects to Tetra Tech; no page located)
  - Milat et al. (2020) ISAT [verified-crossref] (for the assessment that precedes the strategy)
- **Numbers to quote:** none.
- **Non-WEIRD evidence:** built for LMIC health systems.
- **Replication status:** practice guidance, not trial evidence.
- **Boundary conditions and backfire:** the ExpandNet elements per the report: innovation, user organization, environment, resource team, strategic choices.
- **Practitioner sources:** WHO/ExpandNet (above); BWA cites the SINTS Scale Up Toolkit (labs report, no URL).
- **Corrections / cautions for the drafter:** MSI unverified.
- **Suggested io types:** consumes `scalability-assessment`.

### `specify-intervention-adaptations` (stage: implement; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Wiltsey Stirman, S., Baumann, A. A., & Miller, C. J. (2019). The FRAME: An expanded framework for reporting adaptations and modifications to evidence-based interventions. *Implementation Science*, 14, 58. https://doi.org/10.1186/s13012-019-0898-y [verified-crossref]
  - Moore, G., et al. (2021). Adapting interventions to new contexts: The ADAPT guidance. *BMJ*, 374, n1679. https://doi.org/10.1136/bmj.n1679 [verified-crossref]
  - Movsisyan, A., et al. (2019). Adapting evidence-informed complex population health interventions for new contexts: A systematic review of guidance. *Implementation Science*, 14. https://doi.org/10.1186/s13012-019-0956-5 [verified-crossref]
- **Numbers to quote:** none.
- **Non-WEIRD evidence:** none specific; ADAPT addresses cross-context transfer.
- **Replication status:** fidelity-versus-adaptation debate.
- **Boundary conditions and backfire:** code each adaptation with FRAME (what, who, when, why, fidelity-consistent or not); for planned transfer to a new context follow ADAPT.
- **Practitioner sources:** none in the reports.
- **Corrections / cautions for the drafter:** none.
- **Suggested io types:** produces `adaptation-record` (new).

### `design-fidelity-monitoring` (stage: implement; proposed weird: likely-generalizes)
- **Anchor citations:**
  - Carroll, C., et al. (2007). A conceptual framework for implementation fidelity. *Implementation Science*, 2, 40. https://doi.org/10.1186/1748-5908-2-40 [verified-crossref]
  - Dane, A. V., & Schneider, B. H. (1998). Program integrity in primary and early secondary prevention: Are implementation effects out of control? *Clinical Psychology Review*, 18(1), 23–45. https://doi.org/10.1016/S0272-7358(97)00043-3 [verified-crossref]
  - J-PAL, *Implementation monitoring* (M. Gibson, updated Feb 2021) [verified-fetch: https://www.povertyactionlab.org/resource/implementation-monitoring] ("Implementation requires careful monitoring to ensure that the program maintains fidelity to its design"; CART principle for indicators; threats: attrition, compliance, spillovers, contamination)
  - Moore, G. F., et al. (2015). Process evaluation of complex interventions: Medical Research Council guidance. *BMJ*, 350, h1258. https://doi.org/10.1136/bmj.h1258 [verified-crossref]
- **Numbers to quote:** none.
- **Non-WEIRD evidence:** the J-PAL resource is LMIC-informed.
- **Replication status:** uncontested method; tension between fidelity and adaptation.
- **Boundary conditions and backfire:** identify essential components; define observable indicators; set sampling frequency; set a feedback loop to implementers; the J-PAL page defers monitoring-plan detail to a companion resource.
- **Practitioner sources:** J-PAL (above).
- **Corrections / cautions for the drafter:** none.
- **Suggested io types:** produces `fidelity-plan` (new).

### `draft-intervention-description` (stage: implement; proposed weird: not-applicable)
- **Anchor citations:**
  - Hoffmann, T. C., et al. (2014). Better reporting of interventions: Template for intervention description and replication (TIDieR) checklist and guide. *BMJ*, 348, g1687. https://doi.org/10.1136/bmj.g1687 [verified-crossref]
  - Michie et al. (2013) BCTTv1, B1 [verified-crossref]
  - Grant, S., et al. (2018). CONSORT-SPI 2018 Explanation and Elaboration: Guidance for reporting social and psychological intervention trials. *Trials*, 19, 406. https://doi.org/10.1186/s13063-018-2735-z [verified-crossref] (Crossref has no author field; first author from the report)
- **Numbers to quote:** 12 TIDieR items (report).
- **Non-WEIRD evidence:** none (reporting standard).
- **Replication status:** uncontested.
- **Boundary conditions and backfire:** document "how well" as planned versus actual; code active ingredients with BCTTv1.
- **Practitioner sources:** none.
- **Corrections / cautions for the drafter:** none.
- **Suggested io types:** produces `intervention-description` (new).

---

## D. Held for colleagues (do not build)

Reserved for Patricia Andrews Fearon's "film as intervention" claim. Carry the citations; do not draft a skill from them.

- Bernard, T., Dercon, S., Orkin, K., & Taffesse, A. S. (2014). The future in mind: Aspirations and forward-looking behaviour in rural Ethiopia. CSAE/CEPR working paper; SSRN version https://doi.org/10.2139/ssrn.2514590 [verified-crossref] (Crossref lists the first author as "Tanguy", a name-order glitch for Tanguy Bernard). Numbers (report): 64 villages; aspirations rose at 6 months, with effects on savings, credit and children's schooling spending. Note: Crossref also lists a 2026 published version, Bernard et al., "The future in mind: Aspirations and long-term outcomes in rural Ethiopia", *The Quarterly Journal of Economics*, https://doi.org/10.1093/qje/qjag002 [verified-crossref]; not in the reports, so the colleague should read it before citing.
- Riley, E. (2024). Role models in movies: The impact of Queen of Katwe on students' educational attainment. *The Review of Economics and Statistics*, 106(2), 334–351. https://doi.org/10.1162/rest_a_01153 [verified-crossref]. Numbers (report): Uganda; exam performance rose, especially in math and among girls; upper-secondary scores rose about 0.13 SD (working-paper figure); girls stayed in school longer.
- Banerjee, A., La Ferrara, E., & Orozco-Olvera, V. H. (2019). The entertaining way to behavioral change: Fighting HIV with MTV. NBER Working Paper 26096. https://doi.org/10.3386/w26096 [verified-crossref] (a World Bank PRWP 8998 version also appears in Crossref, 10.1596/1813-9450-8998). Numbers (report): urban Nigeria; HIV testing doubled at 8 months; STDs fell among women; social-norm add-ons gave no extra effect.
- La Ferrara, E. (2016). Mass media and social change: Can we use television to fight poverty? *Journal of the European Economic Association*, 14(4), 791–827. https://doi.org/10.1111/jeea.12181 [verified-crossref].
- Related (aspirations framework, from the design report): Lybbert, T. J., & Wydick, B. (2018). Poverty, aspirations, and the economics of hope. *Economic Development and Cultural Change*, 66(4), 709–753. https://doi.org/10.1086/696968 [verified-crossref]; Glewwe, P., Ross, P. H., & Wydick, B. (2018). Developing hope among impoverished children: Using child self-portraits to measure poverty program impacts. *Journal of Human Resources*, 53(2), 330–355. https://doi.org/10.3368/jhr.53.2.0816-8112R1 [verified-crossref] (Indonesia child sponsorship RD: happiness 0.42, self-efficacy 0.29, hope 0.66, units likely SD per report).
- Replication note for the colleague: mixed; two LMIC RCTs for role models plus one strong edutainment RCT; the Kenya aspirations arm was null (Baranov, Haushofer & Jang 2020, see `identify-wise-intervention-target`).

---

## E. Bench skills (swap-ins only)

- E1 `design-anchoring-vignettes`: King, G., Murray, C. J. L., Salomon, J. A., & Tandon, A. (2004). Enhancing the validity and cross-cultural comparability of measurement in survey research. *American Political Science Review*, 98(1), 191–207. https://doi.org/10.1017/S000305540400108X [verified-crossref]. King & Wand (2007) *Political Analysis* and the vignette bank (gking.harvard.edu/files/vign-bank_1.pdf) were seen but not fetched: [unverified, author to confirm]. WHO multi-country data origin [U].
- E2 `adapt-comb-questionnaire`: Keyworth, C., et al. (2020). Acceptability, reliability, and validity of a brief measure of capabilities, opportunities, and motivations ("COM-B"). *British Journal of Health Psychology*, 25(3), 474–501. https://doi.org/10.1111/bjhp.12417 [verified-crossref]. Tested in a low-SES UK sample, not LMIC.
- E3 `draft-mcii-exercise` (WOOP): Wang, G., Wang, Y., & Gai, X. (2021). A meta-analysis of the effects of mental contrasting with implementation intentions on goal attainment. *Frontiers in Psychology*. https://doi.org/10.3389/fpsyg.2021.565202 [verified-crossref]. g = 0.336 (21 studies, 24 effect sizes, N = 15,907), publication bias noted; interactive delivery g = 0.465 vs document-based g = 0.277. Health-specific MCII g = 0.28, k = 7 (Cross & Sheffield 2019, *Health Psychology Review*, seen as a snippet: [unverified, author to confirm]). No non-WEIRD evidence found.
- E4 `write-goal-setting-prompt`: Epton, T., Currie, S., & Armitage, C. J. (2017). Unique effects of setting goals on behavior change: Systematic review and meta-analysis. *Journal of Consulting and Clinical Psychology*, 85(12), 1182–1198. https://doi.org/10.1037/ccp0000260 [verified-crossref]. d = 0.34 (95% CI 0.28–0.41), 141 papers, 384 effect sizes, N = 16,523; larger for difficult, public and group goals. Locke, E. A., & Latham, G. P. (2002). Building a practically useful theory of goal setting and task motivation: A 35-year odyssey. *American Psychologist*, 57(9), 705. https://doi.org/10.1037/0003-066X.57.9.705 [verified-crossref] (report had it from memory; DOI located in this audit). Non-WEIRD: a Western Kenya affirmation and goal-setting trial (Orkin et al., AEA registry) exists, results not retrieved: [unverified, author to confirm].
- E5 `plan-field-observation`: Gyani, A., Tindall, K., & Gallagher, R. (2022). *Explore Field Guide: A practical tool to map and unpack behaviour*. BIT. [verified-fetch: https://www.bi.team/wp-content/uploads/2022/11/BIT-Explore-Field-Guide.pdf] (Observation & Participation: three steps; what to watch out for). Beyer & Holtzblatt (1998) *Contextual Design* [unverified, author to confirm].
- E6 `design-diary-study`: Bolger, N., Davis, A., & Rafaeli, E. (2003). Diary methods: Capturing life as it is lived. *Annual Review of Psychology*, 54, 579–616. https://doi.org/10.1146/annurev.psych.54.101601.145030 [verified-crossref]. Financial diaries in LMICs [unverified, author to confirm].
- E7 `draft-tpb-elicitation-questions` (adjacent to Kelly's TPB customizer): Francis, J. J., Eccles, M. P., Johnston, M., Walker, A. E., Grimshaw, J. M., Foy, R., Kaner, E. F. S., Smith, L., & Bonetti, D. (2004). *Constructing questionnaires based on the theory of planned behaviour: A manual for health services researchers*. Centre for Health Services Research, University of Newcastle upon Tyne. ISBN 0-9540161-5-7. [verified-fetch: https://openaccess.city.ac.uk/id/eprint/1735/]. Sutton et al. (2003) wording effects and a Sri Lankan farmers study are report-verified without citation details: [unverified, author to confirm].
- E8 `design-mechanism-check`: Bullock, J. G., Green, D. P., & Ha, S. E. (2010). Yes, but what's the mechanism? (Don't expect an easy answer). *Journal of Personality and Social Psychology*, 98(4), 550–558. https://doi.org/10.1037/a0018933 [verified-crossref]; Imai, K., Keele, L., Tingley, D., & Yamamoto, T. (2011). Unpacking the black box of causality: Learning about causal mechanisms from experimental and observational studies. *American Political Science Review*, 105(4), 765–789. https://doi.org/10.1017/S0003055411000414 [verified-crossref]; EGAP "10 Things to Know About Mechanisms" [verified-fetch: https://egap.org/resource/10-things-to-know-about-mechanisms/] (listing only).
- E9 `estimate-attrition-bounds`: Lee, D. S. (2009). Training, wages, and sample selection: Estimating sharp bounds on treatment effects. *Review of Economic Studies*, 76(3), 1071–1102. https://doi.org/10.1111/j.1467-937X.2009.00536.x [verified-crossref]. WWC attrition brief exists; threshold values not confirmed: [unverified, author to confirm].
- E10 `select-implementation-strategies`: Powell, B. J., et al. (2015). A refined compilation of implementation strategies: Results from the Expert Recommendations for Implementing Change (ERIC) project. *Implementation Science*, 10, 21. https://doi.org/10.1186/s13012-015-0209-1 [verified-crossref] ("73 strategies" is [U]). Aarons, Hurlburt & Horwitz (2011) EPIS, https://doi.org/10.1007/s10488-010-0327-7 [verified-crossref] (audit year 2010); May & Finch (2009) NPT, *Sociology*, 43(3), 535–554, https://doi.org/10.1177/0038038509103208 [verified-crossref].
- E11 `design-process-evaluation`: Moore et al. (2015) MRC guidance, *BMJ* 350:h1258 [verified-crossref]; Skivington, K., et al. (2021). A new framework for developing and evaluating complex interventions: Update of Medical Research Council guidance. *BMJ*. https://doi.org/10.1136/bmj.n2061 [verified-crossref].
- E12 `estimate-effect-persistence`: Allcott & Rogers (2014) [verified-crossref]; Frey, E., & Rogers, T. (2014). Persistence. *Policy Insights from the Behavioral and Brain Sciences*, 1(1), 172–179. https://doi.org/10.1177/2372732214550405 [verified-crossref]; Brandon, A., et al. (2017). Do the effects of nudges persist? Theory and evidence from 38 natural field experiments. NBER Working Paper 23277 (revised 2022). https://doi.org/10.3386/w23277 [verified-crossref]. There is no PNAS version. Crossref now also lists a 2026 *Review of Economic Studies* version, https://doi.org/10.1093/restud/rdag012 [verified-crossref], not in the reports. Evidence is mostly US energy and utility data (weird-only).

---

## F. Verification log

Method. Every DOI in the three reports was checked against Crossref with `scratchpad/tools/crossref_check.py` (160 OK in `doi_audit.tsv`; the six DOIs containing parentheses re-checked OK in `doi_audit_retry.tsv`). Citations the reports gave without a DOI were searched on Crossref's bibliographic endpoint (`crossref_search.py`, 70 queries) and every candidate DOI was then re-run through `crossref_check.py` (`doi_audit_batch2.tsv`, 66 DOIs; `batch3`, 3; `batch4`, 1; all OK). One DOI (UCL figshare calculators) resolved through api.datacite.org. Non-DOI items were fetched at the publisher or repository URL; when a lab page failed, an alternate page on the same organization's site, the OpenLibrary ISBN API, or the NBER working-paper page was used. PDFs that WebFetch returned as binary (BIT EAST, BIT Explore Field Guide, CGD Datta & Mullainathan, OES analysis plan) were read from the downloaded file. WebSearch was not used.

### Counts
- Distinct DOIs cited in this dossier: 197. All resolve: 196 Crossref OK, 1 DataCite OK. Of these, 13 are secondary versions of a work already cited by its journal DOI (NBER, SSRN, World Bank WP or later journal versions of Blumenstock 2018, Duflo et al. 2011, Kaur et al. 2025, Banerjee et al. 2025, Fryer et al. 2022, Bulte et al. 2020, Kettle et al. 2016, Sunstein 2015, Ashwin et al. 2025, Chernozhukov et al. 2025, Bernard et al. 2014, Brandon et al. 2017, McConnell & Vera-Hernández 2025), so the dossier rests on about 184 distinct DOI-bearing works.
- Distinct items verified by fetch (no DOI): 37 URLs, covering 33 distinct sources (the EGAP guides are confirmed as listings on the methods-guides page; the individual guides were not opened).
- Distinct items left unverified: 33 (listed below). Tag occurrences in the text: `[verified-crossref]` 241, `[verified-fetch: …]` 51, `[unverified, author to confirm]` 36 (some items are tagged in more than one skill).
- Every citation in the 52 skill entries, section D and section E traces to one of the three reports or to the plan; the 12 plan-only citations (Szaszi et al. 2025; Cislaghi & Heise 2018 ×2; Bicchieri & Mercier 2014; Cialdini & Jacobson 2021; Thaler 1999; Muralidharan & Sundararaman 2010; Bénabou & Tirole 2006; Banerjee et al. 2019 gossips; Lades & Delaney; Kwan et al. 2019; "King, Das et al.") are flagged as such where they appear. Two items found only during the audit (QJE 2026 version of Bernard et al.; REStud 2026 version of Brandon et al.) are noted as pointers, not used as anchors.

### Unverified items (33)
1. Irrational Labs *3B Framework* PDF (2025) and the quoted "barriers include every click, field and decision" (report read the PDF; not re-fetched).
2. Engl & Sgaier (2019) CUBES, *Gates Open Research* 3:886.
3. Busara "5 Learnings" / "biases are local" (Compass for SBC page; no URL recorded).
4. National Academies slide claim "1% of published psychology papers have African PIs or African samples".
5. Save the Children use of Barrier Analysis.
6. UNICEF Innocenti / Penn (2016) *Why Do People Do What They Do? A Social Norms Manual for Viet Nam, Indonesia and the Philippines* (and the Zimbabwe & Swaziland edition).
7. Protzko & Aronson (2016) failed affirmation replication.
8. Manoff Group, Trials of Improved Practices method page.
9. Dickin, Griffiths & Piwoz (1997) *Designing by Dialogue*.
10. Alive & Thrive formative research guides.
11. Cenfri snippet: Kenya account opened at the place of business, 2% still using after 2 months.
12. ideas42, Daminger et al. (2015) *Poverty Interrupted*.
13. Cenfri snippet: savings implementation intentions, numeric goals underperformed general commitments.
14. "Weekly SMS beat daily" contrast in Kenya ART reminders (report: from memory).
15. Del Carpio, Peru (Lima) property-tax norm disclosure (~20%).
16. CLTS shaming-tactics ethics concern (no specific paper).
17. Karing (Sierra Leone bracelets), journal version; registry record verified.
18. Harkness (2003) TRAPD chapter in *Cross-Cultural Survey Methods* (book exists; chapter attribution unconfirmed).
19. Brazil systematic review of Beaton guideline use (Revista Mundo da Saúde).
20. Laajaj & Macours (2021) Kenya finding wording ("weak reliability and validity"; acquiescence) (paper verified; the specific finding was from memory in the report).
21. World Bank LSMS and DIME Wiki pages (403).
22. "King, Das et al." standardized-patient work (plan, no title).
23. Kelcey, Shen & Spybrook (2016) sub-Saharan African education ICCs.
24. A published correction to Kasy & Sautmann (2021).
25. "Rapid qualitative methods are used in humanitarian settings".
26. Management Systems International, *Scaling Up Management*.
27. King & Wand (2007) and the Gary King vignette bank; WHO multi-country data origin of anchoring vignettes.
28. Cross & Sheffield (2019), *Health Psychology Review*, MCII g = 0.28.
29. Orkin et al., Western Kenya affirmation and goal-setting trial (AEA registry; results not retrieved).
30. Beyer & Holtzblatt (1998) *Contextual Design*.
31. Financial diaries in LMICs (diary-study LMIC use).
32. Sutton et al. (2003) wording effects and the Sri Lankan farmers TPB study.
33. WWC attrition brief threshold values.
Also not included because the reports marked them unverified and no check was run: Cohen (1988); Dillman *Tailored Design Method*; DeVellis *Scale Development*; Christensen & Miguel (2018); Michie, Atkins & West (2014) book (not needed by any entry); Fogg *Tiny Habits* (2019); Oettingen and Duckworth primary MCII studies; Scheibehenne et al. (2010); Noar et al. (2007); Sailer & Homner (2020); Falk (2007); Kirgios & Milkman gym replication; the two pooled social-norm meta-analyses and the two lottery meta-analyses with unnamed authors.

### Corrections applied (from the reports, confirmed or extended by this audit)
1. Pop-Eleches et al. (2011): the "53%" figure was not found; use "about 13–16 points" (aidsmap summary).
2. Benhassine et al. (2015): "76% dropout reduction" unverified; do not quote.
3. Brandon et al., "Do the effects of nudges persist?": NBER w23277 (2017, revised 2022); no PNAS version. Crossref now also lists a 2026 *Review of Economic Studies* version (10.1093/restud/rdag012).
4. Das et al. (2012): authors are Das, Holla, Das, Mohanan, Tabak & Chan; no Mohpal. DOI 10.1377/hlthaff.2011.1356.
5. Fryer et al.: 0.20–0.40 SD in the 2012 NBER paper, revised to 0.124 SD in the 2022 *AEJ: Economic Policy* version, no effect in wave 2; title changed from "through Loss Aversion" to "through Framing".
6. "AUDAS" (Busara) and "INSPIRE" (BehaviourWorks) do not exist as named frameworks.
7. Cameron et al. CLTS four-country paper is *Journal of Development Economics* 159:102990 (2022), not a PMC-only item.
8. Bulte, List & van Soest: published *Economic Journal* title says "…Field Experiment in the Workplace"; the NBER w26286 title says "…in Uganda".
9. "In praise of moderation" (NBER w26993): first author is Banerjee, not Duflo.
10. Positive-deviance review author is "Bisits Bullen" (2011, *TMIH*); the 2023 *Nutrients* meta-analysis is Triatmaja et al.; the Pascale et al. subtitle reads "how improbable innovators…" in the OpenLibrary record (report wrote "unlikely").
11. Chuang et al. (2021) DOI is 10.1016/j.jdeveco.2020.102582 (the report's recalled DOI returned 404).
12. Mertens et al.: the abstract says d = 0.45 (0.39–0.52); the plan's "d≈0.43" is a secondary figure.
13. Kaur, Mullainathan, Oh & Schilbach: published as *QJE* 140(1), 635–689 (2025), DOI 10.1093/qje/qjae038 (NBER page).
14. Cislaghi & Heise (2018) is ambiguous between the *Globalization and Health* "eight common pitfalls" paper and the *Health Promotion International* paper; both verified; drafter chooses.
15. Cialdini & Jacobson (2021) resolved to *Current Opinion in Behavioral Sciences* "Influences of social norms on climate change-related behaviors"; drafter confirms.
16. Lades & Delaney, "Nudge FORGOOD": online 2020 in *BPP*; the plan's 2022 is the print issue.
17. Online-first vs print years to state consistently: Mertens (2021/2022), Szaszi scoping review (2017/2018), Gallagher & Updegraff (2011/2012), Hall et al. (2013/2014), Lally et al. (2009/2010), ITC (2017/2018), Laajaj & Macours (2019/2021), Münscher (2015/2016), Bicchieri *Norms in the Wild* (print 2016, OSO record 2017), Aarons et al. (2010/2011), Kaur et al. (2024/2025), WDR 2015 (Crossref 2014), IFS WP W15/17 (Crossref metadata 2026).
18. Davis (2010) *Barrier Analysis Facilitator's Guide* page says "eight determinants"; Kittle (2013) uses 12.
19. Walton et al. (2023) has an erratum (10.1126/science.ads9718, 2024); Gallagher & Updegraff has an erratum (10.1007/s12160-012-9446-6).
20. Muralidharan & Sundararaman (2010): citation verified; the plan's "null" result is not in any report and must be confirmed from the paper.
21. Karing: the registry record is dated 2016 (plan said 2018); no journal version located.
22. The EAST PDF at the report's URL (bi.team/…/2014/04/BIT-EAST.pdf) is the "Revised and updated edition" (file dated 2024), whose preface dates the original to 2014.
23. Bernard et al. (2014): Crossref lists first author as "Tanguy" (name-order glitch); a 2026 *QJE* version exists (10.1093/qje/qjag002).
24. Peru growth-mindset effect: 0.14 SD (World Bank figure), 0.05–0.25 depending on estimator, about 0.2 SD in the World Bank summary; quote the range.
25. Szaszi et al. (2025): only first author, year and title confirmed; the plan's co-author list is unconfirmed.
26. J-PAL remote-survey page: "30 minute call at most"; the report's "15–20 minutes" is unverified; the page does not cover mode effects or IVR.
27. IRH SNET fetched pages do not mention vignettes or name DRC; say "15+ settings".
28. Kettle et al. (2016) also exists as a 2017 World Bank book chapter (10.1596/978-1-4648-1120-3_ch2).
29. Co-author lists that the reports did not give are written as "et al."; initials are standard bibliographic form and were not independently audited.

### Fetches that failed (URL, result; what was used instead)
- https://www.fsnnetwork.org/resource/practical-guide-conducting-barrier-analysis, /barrier-analysis-facilitators-guide, /designing-behavior-change-practical-field-guide: 403. Used coregroup.org resource-library pages.
- https://coregroup.org/resource-library/designing-for-behavior-change-a-practical-field-guide/ and …-2/: 404. Used the 2013 multi-sector title URL on coregroup.org.
- https://www.unicef-irc.org/research/social-norms/ (301 to unicef.org/innocenti); https://www.unicef-irc.org/publications/pdf/Social_Norms_Manual_Viet_Nam_Indonesia_Philippines.pdf (301); https://www.unicef.org/innocenti/reports/why-do-people-do-what-they-do (404); https://www.unicef.org/innocenti/reports/why-do-people-do-what-they-do-social-norms-manual-viet-nam-indonesia-and-philippines (404); https://www.unicef.org/innocenti/search?q=social+norms+manual (403); https://web.sas.upenn.edu/pennsong/resources/ (login wall). UNICEF manual left unverified.
- https://www.irh.org/resource-library/social-norms-exploration-tool-snet/ (404); https://www.irh.org/resource-library/social-norms-exploration-tool/ (404); https://irh.org/wp-content/uploads/2020/04/Social_Norms_Exploration_Tool_SNET.pdf (404). Used https://www.irh.org/social-norms-exploration/ and the ALIGN record.
- https://www.bi.team/publications/east-four-simple-ways-to-apply-behavioural-insights/ (403); https://www.bi.team/wp-content/uploads/2015/07/BIT-Publication-EAST_FA_WEB.pdf (403). Used the report's own PDF URL (revised edition).
- https://openknowledge.worldbank.org/handle/10986/24530 (403). Used Crossref DOI 10.1596/1813-9450-7690.
- https://www.oecd.org/en/publications/good-practice-principles-for-ethical-behavioural-science-in-public-policy_0a1b6fb2-en.html (403). Used Crossref DOI 10.1787/e19a9be9-en.
- https://pdf.usaid.gov/pdf_docs/PNACB810.pdf (DNS failure); https://www.manoffgroup.com/approach/trials-of-improved-practices/, /resources/summarytips.pdf, /documents/DesigningbyDialogue.pdf (all 302 to jsi.org); https://openlibrary.org/search.json?title=designing+by+dialogue&author=dickin (no records). Dickin 1997 and Manoff TIPs left unverified.
- https://www.aliveandthrive.org/en/resources (403). Left unverified.
- https://www.penguinrandomhouse.com/books/613966/the-voltage-effect-by-john-a-list/ (404); https://us.macmillan.com/books/9781250056115/scarcity/ (403); https://store.hbr.org/product/the-power-of-positive-deviance-how-unlikely-innovators-solve-the-world-s-toughest-problems/2600 (404); all Google Books API calls (429). Used OpenLibrary ISBN records.
- https://www.msiworldwide.com/our-work/scaling-up (301 to tetratech.com); https://www.googleapis.com/books/v1/volumes?q=intitle:%22scaling+up+management%22… (429). MSI left unverified.
- https://openlibrary.org/search.json?title=cross-cultural+survey+methods&author=harkness: book record found, TRAPD chapter not confirmable from it.
- https://www.nber.org/papers/w28338: succeeded (used for the QJE publication line).
