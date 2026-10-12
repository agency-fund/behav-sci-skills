# Evidence notes: design-social-recognition

Every source below comes from `docs/plan/2026-10-skill-expansion-dossier.md` (compiled 2026-10-12). Verification tags are carried over as the dossier gives them; nothing has been upgraded or added from memory. Numbers appear only as the dossier writes them.

## Anchor trials (both in low-income settings)

### Karing (2016). Social signaling in childhood immunization: Evidence from a field experiment in Sierra Leone [verified-crossref, registry record]
AEA RCT Registry. https://doi.org/10.1257/rct.1299.
- Bracelets signaling timely vaccination raised timely, complete vaccination by 14.4 points, about 56% to 71% (search snippet per the report).
- Verification state: the dossier verified the AEA registry record, dated 2016 (the plan had said 2018). No journal version was located in Crossref; the journal version is [unverified, author to confirm] (dossier unverified item 17; corrections 21). The skill quotes the number with that caveat and never as a journal finding.
- Source of the "timely completion" rule and the wearable-token option.

### Ashraf, Bandiera & Jack (2014). No margin, no mission? A field experiment on incentives for public service delivery [verified-crossref]
*Journal of Public Economics*, 120, 1–17. https://doi.org/10.1016/j.jpubeco.2014.06.014.
- Zambia. Non-financial rewards (public recognition) improved hairdressers' condom sales, more for prosocially motivated agents. Effect size unverified in the dossier; the skill quotes the direction only.
- Source of the note that recognition works most for people already motivated to serve, and of the agent-performance use case.

## Mechanism

### Bénabou & Tirole (2006). Incentives and prosocial behavior [verified-crossref, plan-only citation]
*American Economic Review*, 96(5). https://doi.org/10.1257/aer.96.5.1652.
- The dossier carries this as a plan-only citation with no "what to quote". The skill uses it for the mechanism only: prosocial behavior driven partly by the wish to be seen as a good person. That one-sentence summary is the drafter's reading and is marked author to confirm in the skill.

### Dolan, Hallsworth, Halpern, King, Metcalfe & Vlaev (2012). Influencing behaviour: The mindspace way [verified-crossref]
*Journal of Economic Psychology*, 33(1), 264–277. https://doi.org/10.1016/j.joep.2011.10.009.
- Nine levers: Messenger, Incentives, Norms, Defaults, Salience, Priming, Affect, Commitments, Ego. The skill names Ego and Norms as the two a visible token works through. The dossier gives the lever names only; the gloss on each is the drafter's.

## Cross-cutting cautions (dossier section A)

### DellaVigna & Linos (2022). RCTs to scale: Comprehensive evidence from two nudge units [verified-crossref]
*Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709.
- 126 RCTs, 23 million people. Academic journal studies average 8.7 percentage points (+33.4%); nudge-unit trials average 1.4 points (+8.0%). About 70% of the gap is explained by selective publication combined with low power.

### Ferraro & Tracy (2022). Loss-framed incentive contracts: meta-analysis and real-effort experiment [verified-crossref]
*Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x.
- Pooled 0.16 SD, but 0.33 SD in the lab versus 0.02 SD in the field, with publication bias among lab studies. Used with DellaVigna & Linos for the "discount published effects" point; for this skill the nearer concern is single-trial variance, since both anchors are already field trials.

## Non-WEIRD evidence, summarized
- Sierra Leone (Karing 2016): bracelets, +14.4 points, about 56% to 71%; registry record only.
- Zambia (Ashraf, Bandiera & Jack 2014): public recognition improved condom sales, more for prosocially motivated agents; effect size unverified.
- Nigeria (Ekiti): the World Bank eMBeD unit compared social recognition with lottery incentives for health record-keeping; effect size not retrieved. Mentioned as existence only.
- The evidence base is non-WEIRD throughout, hence `weird: likely-generalizes`; what does not travel automatically is the meaning of a particular token in a particular place.

## Practitioner sources
- eMBeD Results Portfolio (documents.worldbank.org 688661608104181834): existence only per the report; not fetched. Do not quote from it.

## Replication status
- Two strong LMIC RCTs per the plan, in different behaviors (child vaccination, agent sales) and countries; each is a single study for its setting. The Sierra Leone paper is verified only as a registry entry; the Zambia effect size is unverified. Direction supported; size unknown for any new setting.

## Known corrections and cautions (from the dossier)
- Karing: registry record dated 2016, not 2018; journal version unverified, author to confirm.
- Ashraf, Bandiera & Jack: effect size unverified.
- Bénabou & Tirole: plan-only citation; no numbers; mechanism summary is the drafter's reading.
- Ekiti: effect size not retrieved; do not quote a result.
- The dossier has no source on harm to non-recipients from recognition schemes; the non-recipient plan and the harm measurement are this skill's design rules, not a cited finding. The CLTS shaming concern noted elsewhere in the dossier is unverified and is not cited here.

## What to check locally
- Whether completion can be verified by someone with a record, and whether tokens could be obtained any other way.
- Whose regard the people doing the behavior actually track (run `map-reference-network`), and whether that group values the behavior or finds it suspect.
- Whether the behavior is one people want seen; a private or stigmatized behavior fails the screen regardless of design.
- Whether the token's form or color already belongs to a party, a church, a caste marker, or another program.
- The share of non-completion that is involuntary (distance, stockouts, cost); where it is most of it, the token marks circumstance.
- Where the reference group would actually see the token: the market, the meeting, the clinic, the home.
- Whether people without the token are teased, excluded, or questioned, which is why the harm questions are in the measurement plan.
