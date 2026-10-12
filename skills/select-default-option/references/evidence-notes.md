# Evidence notes: select-default-option

Every item below comes from `docs/plan/2026-10-skill-expansion-dossier.md` (entry `select-default-option`, section A, section B). The verification tag is the dossier's. Nothing here has been upgraded or added from memory.

## Anchor sources

**Jachimowicz, J. M., Duncan, S., Weber, E. U., Hardisty, D. J., & Johnson, E. J. (2019). When and why defaults influence decisions: A meta-analysis of default effects. *Behavioural Public Policy*, 3(2), 159–186. https://doi.org/10.1017/bpp.2018.43** [verified-crossref]
- 58 studies, pooled N = 73,675; d = 0.68 (95% CI 0.53–0.83); I² ≈ 98%, so nearly all between-study variation is real difference rather than sampling noise.
- Two studies found negative effects. Effects are weaker in environmental domains and can turn negative when a default signals bad intent.
- Names three mechanisms: endorsement, endowment, effort. The dossier says mechanism predicts effect; it does not rank the three, so this skill does not either. The one-line glosses in SKILL.md are this skill's, not the paper's wording.

**Blumenstock, Callen & Ghani (2018). *American Economic Review*, 108(10), 2868–2901. https://doi.org/10.1257/aer.20171676** [verified-crossref]
- Afghanistan, 949 employees paid through mobile money. A 5% default contribution versus a 0% default raised participation by 40 percentage points, equivalent to a 50% employer match.
- The authors attribute the effect to present bias and the cognitive cost of deciding, not to endorsement or inattention. Savings attitudes persisted after the trial.
- Title confirmed against the Crossref record for the DOI during the batch audit (the dossier entry had omitted it).

**Mertens, S., Herberz, M., Hahnel, U. J. J., & Brosch, T. (2022). The effectiveness of nudging: A meta-analysis of choice architecture interventions across behavioral domains. *PNAS*, 119(1). https://doi.org/10.1073/pnas.2107346118** [verified-crossref] (audit year 2021, online-first)
- d = 0.45 (95% CI 0.39–0.52) per the abstract; some secondary sources say 0.43. More than 200 studies, more than 450 effect sizes, N ≈ 2.15 million.
- "Structure" interventions (defaults, choice-set changes) beat "description" and "assistance" interventions. Moderate publication bias.

**Maier, M., Bartoš, F., Stanley, T. D., Shanks, D. R., Harris, A. J. L., & Wagenmakers, E.-J. (2022). No evidence for nudging after adjusting for publication bias. *PNAS*. https://doi.org/10.1073/pnas.2200300119** [verified-crossref]
- Re-analysis of the Mertens literature; the RoBMA bias-corrected average is about d = 0.04. Critics and a rejoinder note the average hides heterogeneity, which matters here because defaults are the strongest sub-class.

**Münscher, R., Vetter, M., & Scheuerle, T. (2016). A review and taxonomy of choice architecture techniques. *Journal of Behavioral Decision Making*, 29(5), 511–524. https://doi.org/10.1002/bdm.1897** [verified-crossref] (audit year 2015, online-first)
- Nine techniques grouped as decision information, decision structure, decision assistance. Defaults are a decision-structure technique; used here only for placement, no numbers.

## Discounting sources (section A)

**DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709** [verified-crossref]
- 126 RCTs, 23 million people. Academic journal studies average 8.7 percentage points (+33.4%); nudge-unit trials average 1.4 points (+8.0%). About 70% of the gap is explained by selective publication combined with low power.

**Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x** [verified-crossref]
- Pooled 0.16 SD, but 0.33 SD in the lab versus 0.02 SD in the field, with publication bias among lab studies. Used as the lab-to-field shrinkage example, not as default-specific evidence.

**Szaszi, B., et al. (2022). No reason to expect large and consistent effects of nudge interventions. *PNAS* (letter). https://doi.org/10.1073/pnas.2200732119** [verified-crossref]
- Bias-adjusted range d ≈ 0.03–0.31; the average is misleading given heterogeneity. Cited in the dossier's cross-cutting cautions; not quoted in SKILL.md.

## Practitioner sources

- Behavioural Insights Team, *EAST*, "Make it easy" [verified-fetch: https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf]. The PDF at this URL is the revised and updated edition (file dated 2024); its preface dates the original to 2014. No individual authors on the cover.
- Dolan, P., Hallsworth, M., Halpern, D., King, D., Metcalfe, R., & Vlaev, I. (2012). Influencing behaviour: The mindspace way. *Journal of Economic Psychology*, 33(1), 264–277. https://doi.org/10.1016/j.joep.2011.10.009 [verified-crossref]. "Defaults" is one of the nine MINDSPACE levers. Framework only.

## Non-WEIRD evidence

- Afghanistan (Blumenstock, Callen & Ghani, 2018), as above. This is the only non-WEIRD default study in the dossier. It is a payroll setting with an employer in the loop, present-biased savers, and a mobile-money rail already in use; a program without those features should not expect the same size.
- The dossier does not break the 58 meta-analyzed studies down by country.

## Known corrections and cautions

- Mertens et al.: quote d = 0.45 (0.39–0.52); the plan's "d ≈ 0.43" is a secondary figure.
- The dossier entry records no corrections specific to this skill.
- Direction is robust; size is not. Never give d = 0.68 or the Afghanistan 40 points as a planning number for a field program.

## What to check locally

1. Who is allowed to set the default in this setting (employer, bank, clinic, program), and whether that party is trusted; endorsement is unavailable without a trusted sponsor.
2. Whether people need the cash or the service at once; present bias cuts both ways, and a default that holds money people need is a harm, not a nudge.
3. Whether a default from this institution reads as the institution taking something; that signal is the documented route to a negative effect.
4. The real cost of opting out, measured by walking the opt-out path as a user.
5. Whether an identifiable group is worse off under the default and can be given an active choice instead.
6. Whether the domain is environmental, where the pooled effect is weaker.
