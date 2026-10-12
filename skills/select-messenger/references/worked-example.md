# Worked example: iron-folate adherence in Malawi

Illustrative run on an invented program. The names, counts, and ratings are made up to show the skill's shape; none is a finding.

**Setting.** "Mayi Wathanzi" (illustrative), an antenatal program working through 12 health-center catchments in Mchinji District, Malawi. The target behavior came from `define-key-behavior`; the barrier was confirmed by a diagnostic round designed with `decompose-comb-barriers` (interviews with 48 women and 12 Health Surveillance Assistants, HSAs, illustrative); the lever brief from `select-intervention-levers` selected a credible-source message that nausea is expected and passes; the audience brief came from `map-audience-context`.

**Inputs supplied.** Confirmed barrier: women stop the tablets in the first weeks because they, and their husbands, read the nausea as a sign the "hospital medicine" is harming the pregnancy, and nobody they trust has told them otherwise. Type: trust. Audience brief: women attend the health center for antenatal visits; most belong to a church women's guild that meets weekly; HSAs visit each village about monthly and reach perhaps a third of households per visit; 55% of households have a phone, usually held by the husband (illustrative). Candidates the program can field: the HSA (current default), the antenatal nurse, the group village headman, the women's guild leader, a mother who completed the course last year, community-nominated hubs, an SMS from the health center. The program covers 12 catchments and can split them.

```markdown
# Messenger choice

**Target behavior:** Pregnant women enrolled at the program's 12 health centers in Mchinji District take one iron-folate tablet daily from their first antenatal visit until delivery.
**Barrier the message addresses:** Women stop in the first weeks because they and their husbands read nausea as harm from "hospital medicine" and no one they trust has said it is expected and passes (diagnostic interviews, 48 women and 12 HSAs, illustrative). **Type:** trust
**Audience and channels:** Women reached at antenatal visits and weekly guild meetings; HSA visits monthly, reaching about a third of households; phones mostly held by husbands (audience brief).

## Candidate messengers
| Candidate | Reach | Similarity | Authority | Trust | Cost per contact | Basis for the ratings |
|---|---|---|---|---|---|---|
| HSA (current default) | medium: monthly visits, a third of households | medium: local, salaried | medium: health worker | medium: women said HSAs "tell us to take it" but do not explain | low: already paid | brief and interviews |
| Antenatal nurse | low: sees women at visits six weeks apart | low: clinic staff, often from elsewhere | high: clinical | medium: respected, but controls antenatal services (power test) | low: already paid | brief and interviews |
| Group village headman | high: can call a meeting | low: male elder | high: traditional | low on this topic: women said he "does not know about pregnancy" | low | interviews, partly assumed |
| Women's guild leader | high: weekly meeting, most women attend | high: a mother in the same village | medium: respected lay leader | high: named by women as who they ask | low: a transport allowance | nomination round |
| Mother who completed the course | low: her own neighbors | high | low | high: "she took them and the baby is fine" | low | interviews, assumed |
| Community-nominated hubs | high by construction | varies: see nomination round | varies | high in the 4 catchments asked | low: airtime and transport | nomination round |
| SMS from the health center | low: phone held by the husband | low | medium | low: an unexplained text from a number | very low | brief |

## Nomination round
- **Question:** "If we wanted everyone in this village to hear news about the pregnancy tablets, who should we tell first?" (to be drafted in Chichewa by the field team)
- **Who is asked, how many:** ten adults per village, five women and five men, spread across hamlets, in all 12 catchments.
- **Tally rule:** anyone named by four or more of the ten is a hub; where no one reaches four, the two most-named are hubs.
- **Status:** done in 4 of 12 catchments (illustrative): the most-named were the women's guild leader in all four, a grocery owner in two, and the HSA in one. Planned for the remaining eight before launch; ratings marked "assumed" stand until then.

## Choice
**Chosen messenger:** community-nominated hubs, which in the four catchments done are mostly the women's guild leaders, delivering a message the antenatal nurse has given them and that names her as its source.
**Why, given the barrier type:** trust, so authority and trust were weighted first. The hubs scored high on trust and reach and medium on authority; naming the nurse as the source supplies the clinical authority they lack without making her the deliverer. The nurse herself scored low on reach and sits behind a power test.
**Power test:** no. Guild leaders and the grocery owner control nothing the women need. The nurse was not chosen as deliverer partly because she controls antenatal services, so agreement in front of her may be compliance.
**Runner-up:** the mother who completed the course: highest on similarity and trust, lowest on reach; she can be invited to speak at the guild session the hub runs.

## Pairing and brief
- **Channel:** in person, a 15-minute talk at the weekly guild meeting once a month for six months, plus being available to be asked between meetings.
- **Paired reminder:** none for now. Phones are held by husbands; `design-reminder-schedule` will decide whether a message to husbands is worth testing, since husbands share the belief.
- **Messenger brief:** say the three sentences agreed with the nurse (nausea is expected, it passes in a few weeks, keep taking the tablet with food); say who told them; invite questions; do not count anyone's tablets or report names to the clinic. Receive airtime and transport (illustrative: MWK 5,000 per month) for six months. Ceiling: this one message; the program will not add other topics.

## Comparison plan
- **Arms:** nominated hubs in 6 catchments vs the HSA default delivering the same three sentences on the monthly visit in the other 6, assigned at random.
- **Unit and count:** health-center catchment; 6 per arm (illustrative; `plan-evaluation-design` to check whether 12 clusters can show anything short of a large difference).
- **Outcome and who records it:** share of women with a pill count above 80% at the second antenatal visit, from the clinic register, recorded by the nurse, who does not know the arm.
- **If no comparison is possible:** monitor pill counts in all 12 before and after; this cannot separate the hubs from the message or the season.

## What to check before relying on this
- The nomination round ran in only 4 of 12 catchments; the choice assumes the other 8 name similar people.
- Guild meetings exclude women who do not attend church; the reach rating is high for members only, and the HSA arm may serve the others better.
- Husbands hold the belief too and are not reached by this messenger; if adherence does not move, the barrier may sit with them.
```

**What happened next (illustrative).** The three sentences went to `draft-lever-content` for a Chichewa draft and pre-test; the comparison went to `plan-evaluation-design`; the question of messaging husbands went to `design-reminder-schedule`. No results are reported here.
