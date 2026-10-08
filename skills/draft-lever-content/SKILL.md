---
name: draft-lever-content
description: >-
  Use when a specific behavior change technique has been chosen and the team
  needs the actual words: the text message, agent script, poster, sign, or
  app wording. Also use when a field team is about to write intervention
  copy ad hoc without checking that it delivers the technique the lever was
  selected for. Drafts the content, links each element to the part of the
  technique it delivers, adds delivery notes and an EAST check, and sets out
  the comprehension pre-test the draft must pass before launch. Do not use
  when the lever brief stops at a function name ("Environmental
  restructuring") with no named technique; finish select-intervention-levers
  first. Not for values-affirmation exercises (draft-values-affirmation),
  and not for choosing between levers or techniques.
license: CC-BY-4.0
metadata:
  title: Write an intervention's messages and scripts
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Joe Speed"
  org: IL
  weird: mixed-evidence
  tags: "behavior-change-techniques, east, message-design"
  consumes: "intervention-levers, audience-context-brief"
  produces: "intervention-draft"
---

## What it does

Drafts what a field team will deliver, such as text messages, script lines, signs, or app wording, from one chosen behavior change technique.

Each element of the draft is traced to the part of the technique's definition it delivers, so a reader can tell copy that instantiates the technique from copy that merely sounds persuasive. The output also carries delivery notes, an EAST check, and the comprehension pre-test the draft must pass; until that passes, the draft is working copy, not final copy.

## When to use it

### Use it when
- `select-intervention-levers` has produced a brief whose Selected lever names a concrete BCTTv1 technique, and the next question is "what do we actually say, show, or print?"
- A field team is about to write intervention copy ad hoc (an SMS, a poster, an agent script) without checking that the copy delivers the technique the lever was selected for
- Someone asks for "the message", "the script", "the sign", or "the app copy" for an intervention whose mechanism has already been chosen
- Draft copy already exists and the team wants to check whether it delivers the technique or is just well written

### Do not use it when
- The lever brief stops at a function name with no named BCT; that brief is not finished. Route back to `select-intervention-levers`, whose output template requires one
- The exercise to draft is a values affirmation; `draft-values-affirmation` owns that protocol end to end, including its value-list adaptation and delivery cautions
- The team still needs to choose between levers or techniques; that decision happened upstream, and this skill takes exactly one named technique
- The team wants to pretest survey items rather than intervention copy; that is `draft-cognitive-interview-script`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The intervention lever brief from `select-intervention-levers`, or at minimum the selected technique by BCTTv1 number and name, with the confirmed barrier and target behavior it addresses. If the brief stops at a function name, say so and send it back.
2. **Required.** The delivery channel and format (SMS, agent script, signage, interface copy), and whether it has been confirmed as one this population actually uses. If an audience and context brief from `map-audience-context` exists, ask for it; it also supplies the decision moment that sets timing.
3. **Required.** The language the final copy must be in, the reading level of the audience, and who on the team is a native speaker of that language.
4. Optional. Any data the team holds that could support a truthful social-norm claim (for example, the actual share of vendors who already deposit). Without it, no norm claim will be made.
5. Optional. Existing draft copy, if any, so the fidelity trace can be run on it rather than starting from scratch.

If 1 is missing or stops at a function, ask and stop. If 2 is missing, ask once; if the channel is still unconfirmed, proceed and flag it UNCONFIRMED throughout. If 3 is missing, assume English working copy that must be redrafted natively, and say so. If 4 is missing, make no social-norm claim.

## What it draws on

- Michie, S., Richardson, M., Johnston, M., et al. (2013). The Behavior Change Technique Taxonomy (v1) of 93 hierarchically clustered techniques. *Annals of Behavioral Medicine*, 46(1), 81–95.
- Service, O., Hallsworth, M., Halpern, D., et al. (2014). *EAST: Four Simple Ways to Apply Behavioural Insights*. The Behavioural Insights Team, London.
- Whittingham, J. R. D., Ruiter, R. A. C., Castermans, D., Huiberts, A., & Kok, G. (2008). Designing effective health education materials: experimental pre-testing of a theory-based brochure to increase knowledge. *Health Education Research*, 23(3), 414–426.

The Behavior Change Technique Taxonomy (BCTTv1) defines each technique's active ingredient: what must actually be present for the technique to be the one delivered. That definition is this skill's fidelity anchor. A draft instantiates a technique only if some concrete content element delivers the defined ingredient; copy that is persuasive, on-topic, and well written but contains no such element is a different (unselected, undiagnosed) intervention wearing the selected one's name. The BCTTv1 defines techniques, not copy. The mapping from a definition to an actual sentence, sign, or script line is this skill's own operationalization, and the fidelity trace exists so that mapping is inspectable rather than asserted.

EAST supplies the delivery-design checklist. Easy: one action, low reading level, no ambiguity about what to do. Attractive: salient at the moment of delivery. Social: only with a truthful, named data source, because an invented social norm is both unethical and a documented backfire risk. Timely: delivered at the decision moment the audience and context brief identified, not whenever the channel is convenient.

Pre-testing (Whittingham et al., 2008) is why the output ends with a required pre-test rather than a launch recommendation: materials that looked fine to their designers can fail comprehension checks with the actual population, so the draft is a hypothesis until a named check passes.

**WEIRD skew:** The BCTTv1's definitions are stated as mechanism descriptions and travel reasonably well, but EAST's worked examples are drawn almost entirely from UK government trials, and most message-design evidence (framing, salience, personalization effects) comes from WEIRD, high-literacy, high-SMS-penetration populations. Register, idiom, reading level, and channel norms are all local. A draft produced by this skill is working copy for local adaptation and pre-testing, never final copy, and final copy should be drafted natively in the delivery language by a local speaker, not translated from this skill's output.

**Replication status:** The BCTTv1 is a taxonomy rather than an effect. EAST is a practitioner checklist distilled from the Behavioural Insights Team's own trials rather than a tested theory. Whittingham et al. (2008) is a single experimental pre-test study; the broader claim that designer-approved materials routinely fail comprehension checks is practice knowledge rather than a replicated effect (unverified, author to confirm). Message-design effects such as framing and personalization are mixed across contexts, which is why the draft is treated as a hypothesis until its pre-test passes.

## How to do it

1. **Carry the technique over verbatim** from the lever brief: BCT number, name, and its BCTTv1 definition. The definition is the fidelity anchor for everything below.
2. **Fix the delivery channel and timing** from the audience and context brief where available: the confirmed channel, and the decision moment the copy must land at. Otherwise state the assumed channel and flag it UNCONFIRMED.
3. **Write the language note**: what language the final copy must be drafted in and by whom. If this draft's language differs, label it working copy. Final copy is drafted natively by a local speaker, not translated.
4. **Draft the content**: the literal copy, at the target population's reading level, requesting one action.
5. **Run the fidelity trace.** For every content element, name the specific clause of the BCTTv1 definition it delivers. An element that delivers nothing is decoration: cut it, or justify it explicitly as delivery scaffolding (a greeting). Then apply the tip-off test: delete the technique's name from the top of the draft; if nothing about the copy now seems mismatched, the trace was asserted, not real.
6. **Write the delivery notes**: the sender or messenger and why that source is credible to this population; timing relative to the decision moment; a frequency ceiling before fatigue or reactance outweighs marginal effect.
7. **Run the EAST check.** Easy: the one action requested and the reading-level check. Attractive: what makes it salient at the delivery moment. Social: a norm claim only with a truthful, named data source; otherwise write "no social-norm claim made" and why. Timely: how delivery lands at the decision moment.
8. **Specify the required pre-test** with n and a pass criterion, for example 5 to 10 members of the target population shown the draft cold restate the requested action in their own words, pass = all name the intended action. The pre-test runs on the final-language version.
9. **State what the draft does not do**: content supports the structural or environmental change, it does not substitute for it.

See `references/worked-example.md` for a complete run on the kiosk partition at the Nairobi markets.

## Output template

```markdown
# Intervention content draft

**Technique being instantiated:** <BCT number + name, carried verbatim from the lever brief's Selected lever, plus its BCTTv1 definition>
**Delivery channel:** <channel and format, from the audience and context brief where available; otherwise state the assumed channel and flag it UNCONFIRMED>
**Language note:** <what language the final copy must be drafted in, by whom; this draft's language is working copy only if it differs>

## Draft content
<the literal copy: message text, script lines, sign wording, interface strings, at the target population's reading level, one requested action>

## Fidelity trace
| Content element | Part of the technique's definition it delivers |
|---|---|
| "<quoted element>" | <the specific clause of the BCTTv1 definition> |
<elements that deliver nothing are decoration: cut or justify>

## Delivery notes
- **Sender/messenger:** <who the content appears to come from, and why that source is credible to this population>
- **Timing:** <when, relative to the decision moment>
- **Frequency ceiling:** <how many exposures before fatigue or reactance risk outweighs marginal effect>

## EAST check
- **Easy:** <the one action requested, and the reading-level check>
- **Attractive:** <what makes it salient at the delivery moment>
- **Social:** <the norm claim made, with the named data source that makes it true; or "no social-norm claim made", with why>
- **Timely:** <how delivery lands at the decision moment>

## Required pre-test before launch
<the specific comprehension or acceptability check, with n and a pass criterion, e.g. "5 to 10 members of the target population, shown the draft cold, restate the requested action in their own words; pass = all restatements name the intended action">

## What this draft does not do
<explicit limits, e.g. content supports the environmental or structural change, it does not substitute for it>
```

## Where it goes wrong

- **Technique-shaped decoration.** The copy is persuasive, on-brand, and never delivers the BCT's defined active ingredient. Tip-off: delete the technique's name from the top of the draft; if nothing about the copy now seems mismatched, the fidelity trace was asserted rather than real.
- **Researcher-register copy.** Drafting at the team's own reading level, idiom, or formality, or shipping a translation of the working copy instead of natively drafted local-language copy. The language note and pre-test exist to catch this, but only if the pre-test runs on the final-language version.
- **Default-channel assumption.** Writing an SMS because SMS is what behavioral-science examples use, when the audience and context brief names a different confirmed channel, or when no brief exists and the channel was never confirmed at all. An UNCONFIRMED channel flag that survives into launch is a failure of the process, not a formality.
- **Invented social proof.** An EAST Social line like "9 out of 10 vendors already deposit daily" with no data source behind it. If the claim is false it is unethical; if it is merely unverified it risks a descriptive-norm backfire (normalizing the undesired behavior, or collapsing trust when people compare notes). No named source, no norm claim.
- **Multiple techniques in one draft.** Folding a bonus technique into the copy ("while we're at it, add a commitment prompt") delivers an intervention nobody selected or diagnosed. One draft instantiates one named technique; a second technique means a second lever decision upstream.
- **Out of scope: no named technique.** A lever brief whose selected lever is still a bare function name has not finished `select-intervention-levers`' own template. Send it back rather than guessing which technique was meant.

## When to bring in a specialist

Tell the user to consult the relevant specialist when:
- The copy makes a health, financial, or legal claim (a dosage, an interest rate, an entitlement); a clinician, a financial-services compliance lead, or a lawyer must check the claim before any pre-test, because a comprehension test does not check truth
- Final copy must be in a language no one on the team speaks natively; a local writer drafts it rather than a translator, and the pre-test runs on that version with a bilingual reviewer who can separate translation problems from comprehension problems
- The content will reach children, people in crisis, or a stigmatized group, where accurate and well-targeted copy can still cause harm; a safeguarding or community advisory review comes before the pre-test
- The pre-test fails twice; a communications specialist or qualitative researcher should look at whether the technique, the channel, or the copy is the problem before a third redraft

Bring them: the technique definition, the draft with its fidelity trace, the delivery notes, and the pre-test results so far.
