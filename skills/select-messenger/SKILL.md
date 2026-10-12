---
name: select-messenger
description: >-
  Use when the open question is who should deliver a message: "should the
  nurse say this or the village elder?", "who do people here actually listen
  to?", "would a peer land better than our staff?". Also use when a team has
  defaulted to its own staff as the messenger without checking whether the
  audience trusts them, or wants to recruit community "ambassadors" and needs
  a way to pick them. Scores candidates on reach, similarity, authority,
  trust, and cost, picks one by barrier type, and plans a comparison against
  a random messenger, drawing on the MINDSPACE Messenger lever and the
  Haryana immunization trial, where community-nominated information hubs
  plus SMS were the most cost-effective arm. Do not use when the question is
  whose opinion the audience weighs for a norm; that is map-reference-network,
  which this skill takes as input. Not for when or how often to send
  (design-reminder-schedule), the norm message (write-social-norm-message),
  or the message text (draft-lever-content).
license: CC-BY-4.0
metadata:
  title: Choose who delivers the message
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "message-design, social-norms, network"
  consumes: "intervention-levers, audience-context-brief"
  produces: ""
---

## What it does

Picks who should deliver a message to a given audience, with the reasons on paper.

The same words land differently depending on who says them: people weight information by the messenger's perceived authority, similarity to themselves, and trustworthiness (the Messenger lever in MINDSPACE), and a message travels further when it starts with people who talk to many others. This skill lists the messengers a program could field, has the community rather than the program name the well-connected ones, rates each candidate on five criteria, weights the criteria by the barrier the message addresses, and plans a comparison so the program learns whether the choice mattered. It does not write the message or set the reminder cadence.

## When to use it

### Use it when
- A message, script, or outreach is planned and someone asks "who should say this?", "should it come from the clinic or from someone in the village?", or "would a peer be more convincing than our staff?"
- A program has defaulted to its own staff (the program officer, the community health worker, the SMS sender name) as the messenger without checking whether the audience hears from them or trusts them
- A program wants to recruit community "ambassadors", "champions", or "mobilizers" and needs a defensible way to pick them rather than taking volunteers or the chief's nominees
- A lever brief from `select-intervention-levers` names modeling, a credible source, or social support as the technique, where the deliverer is the active ingredient

### Do not use it when
- The question is whose opinion the audience weighs when deciding whether to follow a norm; that is `map-reference-network` (diagnose stage), and its influencers and gatekeepers are candidates here
- The question is when and how often a reminder goes, or through which channel; `design-reminder-schedule` sets that, and this skill only says who the reminder appears to come from
- The team needs the norm message or the message text; `write-social-norm-message` and `draft-lever-content` write the words once the messenger is chosen
- The barrier is supply, cost, or distance rather than information, norms, or trust; no messenger fixes a stock-out. Go back to `select-intervention-levers`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The target behavior (who, what, when) and the confirmed barrier the message addresses, with its type: information (people do not know what, where, or when), norm (people doubt that others do or approve of it), or trust (people doubt the source, the product, or the service). The type decides which messenger property matters most. If the barrier is supply or cost, say so and stop.
2. **Required.** Who the audience is, which channels already reach them, and who currently talks to them about this topic, from the audience and context brief if `map-audience-context` produced one.
3. **Required.** The messengers the program could actually field, with a rough cost per contact for each, and whether any of them holds power over the audience (employer, lender, landlord, official, teacher).
4. Optional. A reference-network map from `map-reference-network`, whose named influencers and gatekeepers become candidates.
5. Optional. Whether the program covers enough villages, clinics, or groups to run two messenger types side by side, and what outcome it already records.

If 1 is missing, ask and stop. If 2 is missing, ask once; if still thin, proceed and mark the channel and current-contact cells "assumed". If 3 is missing, list the program's own staff plus a community-nominated messenger as the minimum set and say so. If 4 and 5 are missing, assume no map exists and that a comparison at the cluster level is feasible, and flag both.

## What it draws on

- Dolan, P., Hallsworth, M., Halpern, D., King, D., Metcalfe, R., & Vlaev, I. (2012). Influencing behaviour: The mindspace way. *Journal of Economic Psychology*, 33(1), 264–277. https://doi.org/10.1016/j.joep.2011.10.009
- Banerjee, A., Chandrasekhar, A. G., Duflo, E., & Jackson, M. O. (2019). Using gossips to spread information: Theory and evidence from two randomized controlled trials. *The Review of Economic Studies*. https://doi.org/10.1093/restud/rdz008 (citation verified; its results are not recorded in the dossier, so none are quoted here)
- Banerjee, A., Chandrasekhar, A. G., Dalpath, S., Duflo, E., Floretta, J., Jackson, M. O., et al. (2025). Selecting the most effective nudge: Evidence from a large-scale experiment on immunization. *Econometrica*, 93(4), 1183–1223. https://doi.org/10.3982/ECTA19739
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709

MINDSPACE (Dolan et al. 2012) lists Messenger first among its nine levers: people weight information by who delivers it, giving more to messengers they see as authoritative, as similar to themselves, or whom they like. The network studies add a second property, reach: a message spreads through conversation, so starting it with people who talk to many others carries it further, and a community can name those people when asked who is good at spreading news (the "gossip" nomination used in Banerjee et al. 2019). In Haryana (Banerjee et al. 2025), information-hub "ambassadors" nominated by community members improved full immunization, and ambassadors paired with SMS reminders were the most cost-effective arm, at +9.1% immunizations per dollar; SMS alone had no impact (J-PAL evaluation page, a secondary source per the dossier). See `references/evidence-notes.md` for the annotated list.

Judgment calls this skill adds: the five-criterion table, the rule that barrier type sets the weights (information: reach first; norm: similarity first; trust: authority and trust first), the power test on the leading candidate, and the random-messenger comparison arm, which the dossier recommends but no source specifies. The sources document no backfire for messenger choice; the cautions under "Where it goes wrong" are the authors' practice judgments.

**WEIRD skew:** MINDSPACE was written for the UK government and its Messenger examples are British and American. The trial evidence this skill rests on is Indian, which is why the status is likely-generalizes rather than mixed. What to check locally: whether "who is good at spreading news" names the same people as "who do you trust about this", whether those people are willing, and whether they coincide with the gatekeepers in a reference map. **Non-WEIRD evidence:** India, Haryana (Banerjee et al. 2025): community-nominated information hubs improved full immunization, and hubs plus SMS were the most cost-effective arm at +9.1% immunizations per dollar (secondary source). The Karnataka gossips trials (Banerjee et al. 2019) are citation-verified with results not in the dossier. Indonesia is named in the plan with no citation and is not cited.

**Replication status:** Replicated in India (Haryana plus the gossips trials, per the dossier); single large study for the ambassador-plus-SMS bundle, with the cost-effectiveness figure from a secondary source. Untested elsewhere as far as this skill's sources go. Discount for a field program: nudge-unit trials averaged 1.4 percentage points against 8.7 in academic journals (DellaVigna & Linos 2022); plan for a few points, not a headline.

## How to do it

1. **Carry over the target behavior, the barrier, and the barrier type verbatim.** If the barrier is supply or cost, stop; a messenger cannot deliver what is not there.
2. **List at least four candidates the program could field**, always including the current default and a community-nominated messenger. Typical candidates: program staff or community health worker, clinic staff, religious or traditional leader, a peer who already does the behavior, a community-nominated information hub, a public figure, an automated sender (SMS from a named office).
3. **Write the nomination round rather than guessing reach.** Draft the question ("If we wanted everyone in this village to hear about X, who should we tell first?"), say who to ask (for example ten adults per village, spread across hamlets and sexes), and how to tally (people named by many respondents are hubs). Haryana's hubs came from community nomination; a staff-drawn list is an assumption until the round runs.
4. **Rate every candidate on five criteria** with a one-clause reason each: reach, perceived similarity, perceived authority, trust, cost per contact. Use high, medium, low, and mark any rating that rests on the team's impression "assumed" until the nomination round or the audience brief confirms it.
5. **Weight by barrier type.** Information: reach first, then trust. Norm: similarity first, because a norm claim from someone the audience does not count as "one of us" says nothing about "us" (see `write-social-norm-message`). Trust: authority and trust first, with step 6 mandatory.
6. **Run the power test on the leading candidate.** Does this messenger control something the audience needs (wages, credit, land, permits, grades, clinic access)? If yes, write it down and route to the specialist section; what looks like trust may be compliance, and the behavior may not outlast the messenger's attention.
7. **Pair the messenger with the channel.** The messenger carries the message in person or by voice; a reminder channel can sit beside it, as SMS did beside the hubs in Haryana. `design-reminder-schedule` sets the cadence; `draft-lever-content` writes the words.
8. **Plan the comparison.** Where the program covers enough units, give the nominated messenger to some and a randomly chosen or default messenger to others, and name the outcome and who records it. Without a comparison the program cannot tell nomination from attention. If no comparison is possible, say what will be monitored instead.
9. **Write the messenger brief:** what they are asked to say, to whom, how often, for how long, what they receive, and the ceiling on what they are asked to carry.
10. **Stop here.** `draft-lever-content` writes the message; `design-reminder-schedule` sets any paired reminder; `plan-evaluation-design` turns the comparison into a test.

See `references/worked-example.md` for a complete run on antenatal iron-folate adherence in Malawi.

## Output template

```markdown
# Messenger choice

**Target behavior:** <who + what + when, carried over verbatim>
**Barrier the message addresses:** <verbatim, with its evidence> **Type:** <information / norm / trust>
**Audience and channels:** <from the audience and context brief, or "assumed">

## Candidate messengers
| Candidate | Reach | Similarity | Authority | Trust | Cost per contact | Basis for the ratings |
|---|---|---|---|---|---|---|
| <current default> | <high/medium/low: reason> | <...> | <...> | <...> | <...> | <nomination round / brief / assumed> |
| <community-nominated hub> | <...> | <...> | <...> | <...> | <...> | <...> |
| <...> | | | | | | |

## Nomination round
- **Question:** <the exact wording, in the local language where known>
- **Who is asked, how many:** <...>
- **Tally rule:** <...>
- **Status:** <done, with the roles that emerged / planned; ratings above are assumed until it runs>

## Choice
**Chosen messenger:** <role or person type>
**Why, given the barrier type:** <which criteria were weighted first and how the chosen candidate scored on them>
**Power test:** <does the messenger control anything the audience needs? no / yes: what, and see the specialist note>
**Runner-up:** <candidate and why it lost>

## Pairing and brief
- **Channel:** <in person, group meeting, voice call, named SMS sender>
- **Paired reminder:** <none / yes, cadence to be set by design-reminder-schedule>
- **Messenger brief:** <what they say, to whom, how often, for how long, what they receive, the ceiling on what they are asked to carry>

## Comparison plan
- **Arms:** <nominated messenger vs randomly chosen or default messenger>
- **Unit and count:** <villages, clinics, groups; n per arm>
- **Outcome and who records it:** <...>
- **If no comparison is possible:** <what is monitored instead, and what that cannot show>

## What to check before relying on this
- <the assumption most likely to be wrong, usually a rating marked "assumed">
```

## Where it goes wrong

- **Reach read off the org chart.** The program lists its community health worker as the hub because the program employs her, while the community would name a shopkeeper or a church elder. Haryana's hubs were nominated by the community; a staff list is an assumption and must be marked as one.
- **Authority mistaken for trust.** The district officer has authority; whether the audience trusts him on this topic is a separate question with its own cell. Rating them together hides the case where the audience obeys and disbelieves.
- **A messenger for a supply barrier.** No messenger fixes a stock-out, a closed clinic, or a price. If the barrier evidence points there, stop rather than pick a persuasive person to deliver news people cannot act on.
- **A messenger with power over the audience.** A lender telling borrowers to save, an employer telling workers to enroll, a teacher telling pupils' parents to pay: uptake under power is compliance, can reverse when attention lapses, and can expose the audience. The power test is mandatory on the leading candidate.
- **Declaring the messenger "worked" without a comparison.** A rise after a popular messenger's visits cannot be separated from the visits themselves. The dossier's own guidance is to compare against randomly chosen messengers.
- **Overloading the hubs.** The same three well-connected people get every program's message. Being a hub is a cost to them, and a tired hub stops spreading; the brief must say what they receive and when it ends. This is a practice judgment, not a documented finding.

## When to bring in a specialist

Tell the user to consult a behavioral scientist, and where noted a safeguarding lead or a local qualitative researcher, when:
- The leading messenger holds power over the audience (employer, lender, landlord, official, teacher), because trust under power is hard to tell from compliance and the audience may not be free to ignore the message; a safeguarding lead reviews the choice before anything is delivered
- The topic is stigmatized (HIV, contraception, debt, mental health) or the audience includes children; a central messenger spreads who was asked along with what was said, and a local qualitative researcher should check whether being approached is itself a cost
- Religious or traditional leaders are the leading candidates in a setting the team does not know well, where an endorsement can arrive with conditions the program did not agree to
- The comparison will be the program's main evidence claim, where the unit of randomization and the outcome need an evaluation specialist (`plan-evaluation-design`) before the first messenger is briefed

Bring them: the candidate table with its basis column, the nomination question and any results, the power test, and the comparison plan.
