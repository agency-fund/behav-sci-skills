---
name: map-reference-network
description: >-
  Use when a social norm has been confirmed for a practice and the team needs
  to know exactly whose behavior and approval the people doing it actually
  track: "who are they really listening to?", "who would have to change for
  them to change?", "who do we need in the room?". Also use when a program
  suspects it is talking to the wrong people, for example counseling pregnant
  women when the decision sits with husbands and mothers-in-law. Chooses a
  network design (full-network, snowball, or egocentric), writes the
  name-generator questions, and produces a table of reference-group members
  by role and influence, with the implication for who must be reached. Do not
  use when it is not yet known whether the practice is a norm at all; run
  diagnose-social-norm first. Not for describing the audience itself, its
  decision moment, or its channels (map-audience-context), and not for
  choosing who delivers a message (select-messenger).
license: CC-BY-4.0
metadata:
  title: Find out whose opinion really matters
  type: atomic
  stage: diagnose
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "social-norms, qualitative, network"
  consumes: "social-norm-diagnosis"
  produces: ""
---

## What it does

Identifies whose behavior or approval the people doing a practice actually track when they decide whether to follow it.

A reference group is the set of people whose behavior and opinion a person weighs for one practice. It is practice-specific: the people a woman tracks for how she feeds her baby are not the people she tracks for whether she votes. This skill finds that set empirically, by asking the actors to name them, instead of assuming it is the program's beneficiaries, its community health workers, or "the community". It separates people whose approval would move the actor (influence) from people who can permit or block the behavior (gatekeeping), because the two call for different responses.

## When to use it

### Use it when
- `diagnose-social-norm` returned "social norm" or "descriptive norm" and named a provisional reference group that needs confirming
- Someone asks "who are they really listening to?", "who would have to change for them to change?", or "who needs to be in the room when we discuss this?"
- A program suspects it is addressing the wrong people, for example counseling the pregnant woman when the decision sits with her husband or mother-in-law
- A pledge, community declaration, or norm message is being planned and the team needs to know who must take part for it to carry weight

### Do not use it when
- It is not yet known whether the practice is held by expectations at all; run `diagnose-social-norm` first, because a custom or a moral rule has no reference group to map
- The question is who the audience is, where the decision happens, or which channels reach them; that is `map-audience-context`
- The question is who should deliver a message; that is `select-messenger` (design stage), which often takes this map as its input
- The team wants to plan the pledge or declaration itself; that is `plan-collective-pledge`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The social norm diagnosis: the practice, the call, the provisional reference group, and the sanctions. If none exists, or the call was custom or moral rule, stop and route to `diagnose-social-norm`.
2. **Required.** The population's size and boundary: a bounded group (a village of 200 households, one school, one cooperative) or an open population (a city district, everyone attending a clinic). And the budget: how many interviews, over what time. These two facts choose the design.
3. **Required.** Who the program currently reaches and assumes it is talking to, so the output can say whether the reference group differs.
4. Optional. Existing interview data that already names people (the diagnosis often does).
5. Optional. Whether naming people carries risk for respondents (sanctioners who use violence, an illegal practice).

If 1 is missing, ask and stop. If 2 is missing, ask once; if still unknown, default to an egocentric design and say why (it works at any population size). If 3 is missing, ask once; if unknown, mark the comparison section "program audience not stated".

## What it draws on

- Institute for Reproductive Health, Georgetown University (2020). *Social Norms Exploration Tool (SNET)*. https://www.irh.org/social-norms-exploration/ (ALIGN platform record dated 27 January 2020: https://www.alignplatform.org/resources/social-norms-exploration-tool-snet)
- UNICEF Innocenti / Penn Social Norms Group (2016). *Why Do People Do What They Do? A Social Norms Manual for Viet Nam, Indonesia and the Philippines*. Unverified, author to confirm: reported to cover full-network, snowball, and egocentric designs; the manual could not be re-fetched in the evidence audit.
- Bicchieri, C. (2016). *Norms in the Wild: How to Diagnose, Measure, and Change Social Norms*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780190622046.001.0001

Bicchieri's account makes the reference group part of the definition of a social norm: the empirical and normative expectations that hold a practice in place are expectations about particular people, not about everyone. SNET, a practitioner tool field-tested in over 15 settings, puts "Identify Reference Groups" (those who matter to individuals and the way they behave) as its Phase 2, run through participatory exercises and short "speed interviews", with the community checking the result. The UNICEF/Penn manual is reported to lay out three designs for collecting that information: full-network, where everyone in a bounded group names everyone they track, giving the whole structure; snowball, where a few actors name people, those people are interviewed, and the chain is followed, which finds influential or hidden people in a large population but over-represents the well-connected; and egocentric, where each actor names their own set with no linking across respondents, which is the cheapest and gives the typical reference group but not the structure. This skill adds four judgment calls: influence (the actor would change if this person did) is recorded separately from gatekeeping (this person can permit or block); every named role gets the "if they changed, would you?" probe; the map is compared with the program's assumed audience; and the table uses roles, not names, outside the team.

**WEIRD skew:** The method is practitioner-developed for programs in low- and middle-income countries and is not derived from WEIRD samples, so the risk is not transfer but validity: name-generator questions depend on respondents being willing to name people, which varies with trust in the interviewer and the sensitivity of the practice. Check locally whether respondents name anyone at all, whether women name men freely, and whether "the community leader" is an honest answer or a polite one. **Non-WEIRD evidence:** SNET applied in over 15 settings (the fetched pages do not name the countries); UNICEF manual trainings reported in Viet Nam, Indonesia, the Philippines, Zimbabwe, and Swaziland (manual unverified). No evaluation of the mapping method's accuracy was found in the sources this skill draws on.

**Replication status:** Practitioner method; no published validation of reference-group mapping as a measurement, and the three-design account rests on one unverified source. Treat the map as a field finding to verify with the community, not a measurement with a known error.

## How to do it

1. **Carry over the practice, the call, and the provisional reference group** from the diagnosis, verbatim, at the top.
2. **Choose the design and write why.** Full-network needs a bounded group small enough to census and someone who can analyze the structure. Snowball suits a large or open population where the aim is to find the influential few. Egocentric suits any population size when the aim is the typical reference group and the budget is small; it is the default. State what the chosen design cannot show.
3. **Write the name-generator questions for this practice**, not generic ones. Use: "When you decide whether to X, whose opinion matters?"; "Who would notice if you did or did not X?"; "Whose approval would you want before X?"; "Who would you ask about X?"; and, for each person named, "If they changed their mind about X, would you change?" The last is the influence check. Then write the name-interpreter questions asked about each person named: their role and relationship, how often the actor sees them, whether they do X, whether they approve, and whether they can stop or permit the actor.
4. **Specify who answers.** The actors, chosen across the sub-groups the diagnosis found to differ (younger and older women, each hamlet). In a snowball design, also the people they name, for a stated number of waves.
5. **Collect, or extract from existing transcripts, and tabulate by role:** how many respondents named the role, influence (yes if actors said they would change with them), gatekeeping (can permit or block), whether they do X, whether they approve. See `references/worked-example.md` for the filled table.
6. **Identify the influential nodes and the gatekeepers separately.** A role named by many is salient; it is influential only if actors said they would change with it. A gatekeeper may be named by few but can block the behavior outright (a husband who controls transport money). Also list roles named often that are not influential, because programs tend to over-invest in them.
7. **Compare with the program's assumed audience:** who is in the reference group that the program does not reach, and who the program reaches that nobody named.
8. **Verify with the community.** Show the role table, without names, to a small group of actors and ask what is wrong or missing. Record what they corrected. If this has not been done, say so.
9. **Write the implication:** which roles must be present, in what capacity, at the point where the norm is addressed.
10. **Stop here.** Do not choose the messenger or plan the pledge. `select-messenger` picks who delivers; `plan-collective-pledge` decides who pledges and in what order.

`references/evidence-notes.md` lists the sources and their verification state.

## Output template

```markdown
# Reference network map

**Practice:** <who does what, when, carried over verbatim>
**Diagnosis call:** <social norm | descriptive norm>, from diagnose-social-norm (<date>); provisional reference group: <...>
**Program's assumed audience:** <who the program reaches now, through which channel>

## Design
**Chosen:** <full-network | snowball | egocentric>
**Why:** <population size and boundary; budget; what this design can and cannot show>
**Sample:** <who answers, how many, how chosen; for snowball, the seeds and the number of waves>

## Name-generator questions
1. <question, with X spelled out>
2. <...>
**Name-interpreter questions (per person named):** <role and relationship; frequency of contact; does X; approves X; can permit or block>

## Reference group by role

| Role (no names) | Named by (n of N) | Influence: actor would change if they did | Gatekeeping: can permit or block | Does X | Approves X |
|---|---|---|---|---|---|
| <role> | <n of N> | <yes/partly/no, with the evidence> | <yes/no, how> | <yes/no/mixed> | <yes/no/mixed> |

## Influential nodes and gatekeepers
- **Influential:** <roles, and why>
- **Gatekeepers:** <roles, and what they control>
- **Named often but not influential:** <roles, and the risk of over-investing in them>

## Does the reference group match the program's audience?
<who is in the reference group that the program does not reach; who the program reaches that nobody named>

## Community verification
<who reviewed the table, what they corrected; or "not yet done">

## Who must be in the room
<roles, in what capacity, at which step; stated as a requirement for the design stage, not as a messenger choice>

## What to check before relying on this
- <the sub-group whose answers were thinnest>
- <the role most likely named out of politeness>
```

## Where it goes wrong

- **Mapping the program's own contacts.** Community health workers, village heads, and the program's volunteers appear in the map because the team knows them, not because actors named them. Only names given in answer to the name-generator questions count.
- **Asking a generic question.** "Who do you talk to?" maps friendship; "whose opinion matters when you decide whether to X" maps the reference group for X. They differ, and the first is useless here.
- **Treating salience as influence.** The most-named role may be named because it is visible. Without the "if they changed, would you?" check, the table ranks visibility and the program will court the wrong people.
- **Running a full-network census on an open population.** It cannot be completed, and the partial result looks like structure. Switch to snowball or egocentric and say so.
- **Dropping distant decision-makers.** A mother-in-law in another village, an employer, a religious authority, a migrant husband who sends money: absent from the room, present in the decision. If a respondent names someone who is not local, keep them.
- **Exposing respondents.** A table that records who sanctions whom can travel. Use roles outside the team, keep names only where the sampling needs them, and only with consent.

## When to bring in a specialist

Tell the user to consult a social norms researcher or a network analyst, together with a local qualitative researcher, when:
- The design is full-network, because the structural measures (who bridges groups, who is central) need analysis software and someone who can read its output
- Naming sanctioners carries risk (violence, legal exposure, loss of livelihood), because the name-generator questions need rewording and the data need a storage and consent plan before collection starts
- The map splits into two groups that track different people (two religious or ethnic communities, in-migrants and long-term residents), because a pledge or message would then need a design per group and a sampling plan to match

Bring them: the diagnosis, the chosen design and the reason for it, the name-generator questions, and the raw role table.
