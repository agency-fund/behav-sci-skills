# Evidence notes: design-reminder-schedule

Every item below comes from `docs/plan/2026-10-skill-expansion-dossier.md` (entry `design-reminder-schedule`, section A, section B). The verification tag is the dossier's. Nothing here has been upgraded or added from memory. "Secondary source per report" means the number came from a summary page (aidsmap, J-PAL) that the dossier's audit did not re-fetch.

## Anchor sources

**Thakkar, J., et al. (2016). Mobile telephone text messaging for medication adherence in chronic disease: A meta-analysis. *JAMA Internal Medicine*. https://doi.org/10.1001/jamainternmed.2015.7667** [verified-crossref] (DOI located in the audit)
- 16 RCTs, N = 2,742. Odds ratio 2.11 (95% CI 1.52–2.93) for medication adherence; bias-adjusted OR 1.68.
- Adherence was estimated to rise from 50% to 67.8%. Quote the adjusted number alongside the raw one, never the raw one alone.

**Free, C., et al. (2013). The effectiveness of mobile-health technology-based health behaviour change or disease management interventions for health care consumers: A systematic review. *PLoS Medicine*, 10(1), e1001362. https://doi.org/10.1371/journal.pmed.1001362** [verified-crossref]
- 75 trials, mostly low quality, nearly all in high-income countries. Used here as the WEIRD-skew statement for the mHealth literature; no pooled effect quoted.

**Karlan, D., McConnell, M., Mullainathan, S., & Zinman, J. (2016). Getting to the top of mind: How reminders increase saving. *Management Science*, 62(12), 3393–3411. https://doi.org/10.1287/mnsc.2015.2296** [verified-crossref]
- Bolivia, Peru, Philippines. Reminders raised savings-goal attainment; messages naming the goal plus the incentive worked best; loss versus gain framing made no difference.
- Effect size unverified in the dossier; do not quote a number. The content rule (name the goal, skip framing work) comes from here.

**Pop-Eleches, C., et al. (2011). Mobile phone technologies improve adherence to antiretroviral treatment in a resource-limited setting: A randomized controlled trial of text message reminders. *AIDS*, 25(6), 825–834. https://doi.org/10.1097/QAD.0b013e32834380c1** [verified-crossref] (PMC3718389)
- Kenya, Chulaimbo clinic. Weekly SMS raised the share of patients reaching 90% adherence by about 13 to 16 points over 48 weeks (aidsmap summary; secondary source per report).
- Correction: a "53%" figure for this trial could not be found; use 13 to 16 points.

**Horvath, T., et al. (2012). Mobile phone text messaging for promoting adherence to antiretroviral therapy in patients with HIV infection. *Cochrane Database of Systematic Reviews*, CD009756. https://doi.org/10.1002/14651858.CD009756** [verified-crossref]
- Rated two Kenyan weekly-SMS RCTs as high-quality evidence. No pooled number quoted in the dossier.

**Gibson, D. G., et al. (2017). Mobile phone-delivered reminders and incentives to improve childhood immunisation coverage and timeliness in Kenya (M-SIMU): A cluster randomised controlled trial. *The Lancet Global Health*, 5(4), e428–e438. https://doi.org/10.1016/S2214-109X(17)30072-4** [verified-crossref]
- Kenya. SMS plus incentives improved coverage and timeliness in a high-coverage setting. Effect size unverified; do not quote a number. Note that the positive arm bundled incentives with reminders.

**Banerjee, A., Chandrasekhar, A. G., Dalpath, S., Duflo, E., Floretta, J., Jackson, M. O., et al. (2025). Selecting the most effective nudge: Evidence from a large-scale experiment on immunization. *Econometrica*, 93(4), 1183–1223. https://doi.org/10.3982/ECTA19739** [verified-crossref]; NBER w28726 https://doi.org/10.3386/w28726 [verified-crossref]
- Haryana, India. SMS reminders alone had no impact; SMS plus information-hub ambassadors was the most cost-effective bundle (+9.1% immunizations per dollar; J-PAL page, secondary source per report).
- This is the boundary-condition source: reminders fail where the barrier is not forgetting, and a messenger can supply what a message cannot.

## Discounting sources (section A)

**DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709** [verified-crossref]
- 126 RCTs, 23 million people. Academic journal studies average 8.7 percentage points (+33.4%); nudge-unit trials average 1.4 points (+8.0%). About 70% of the gap is explained by selective publication combined with low power.

**Ferraro, P. J., & Tracy, J. D. (2022). *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x** [verified-crossref]
- 0.33 SD in the lab versus 0.02 SD in the field for loss framing. Cited in the dossier's cross-cutting cautions as the lab-to-field example; not quoted in SKILL.md because most reminder evidence is already from the field.

## Practitioner sources

- Behavioural Insights Team, *EAST*, "Make it timely" [verified-fetch: https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf]. The PDF at this URL is the revised and updated edition (file dated 2024); the preface dates the original to 2014. No individual authors on the cover.
- 3ie gap-map entry for Pop-Eleches (report; no URL recorded).

## Non-WEIRD evidence

- Kenya: Pop-Eleches et al. (2011), about 13 to 16 points on 90% ART adherence over 48 weeks with weekly SMS; Gibson et al. (2017), SMS plus incentives improved immunization coverage and timeliness, effect size unverified.
- India: Banerjee et al. (2025), Haryana, SMS alone no impact; SMS plus ambassadors most cost-effective.
- Bolivia, Peru, Philippines: Karlan et al. (2016), reminders raised savings-goal attainment, effect size unverified.
- The non-WEIRD evidence here is stronger than the WEIRD meta-analytic base, which is why the `weird` value is mixed-evidence rather than untested.

## Known corrections and cautions

- "Weekly SMS beat daily" in Kenya is from memory in the report: [unverified, author to confirm] (dossier unverified item 14). SKILL.md does not use it to set cadence and tells the model not to state it as a finding.
- The Pop-Eleches "53%" figure could not be found; use 13 to 16 points.
- The Haryana and Kenya ART figures are secondary-source numbers per the report; say so when quoting them.
- Effects decay; the dossier records no reminder backfire study, so the frequency ceiling and stop rule in SKILL.md are practitioner cautions, not documented backfire.

## What to check locally

1. That the barrier is forgetting: whether people act when prompted in person, and whether stock, fees, distance, or distrust came up in the diagnosis.
2. Who holds the phone, whether it is shared, and what a message could disclose to whoever reads it.
3. Whether SMS is read at all, or voice or a visit is needed (literacy, language, network).
4. Whether the program reliably knows each person's due date; a reminder on the wrong date is worse than none.
5. Whether a messenger or incentive is what the setting needs (the Haryana test), before spending on messages alone.
6. How fast the effect decays here, measured at fixed intervals rather than assumed.
