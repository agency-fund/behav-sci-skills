---
name: draft-values-affirmation
description: >-
  Use when people are likely to feel judged at a key moment, for example
  about money, school results, or a health condition, and the program wants
  to reduce that stress before asking them to engage. Also use when someone
  asks for "something to help people feel less judged or defensive about X
  before we ask them to do Y". Drafts a values-affirmation exercise: a short
  writing task where people pick a value that matters to them and write
  about it, which has eased defensiveness in some studies. Includes a
  locally adapted value list, the two-part writing prompt, timing and
  frequency guidance, and two mandatory cautions. Do not use when the real
  barrier is practical or structural (cost, access, time, a process that
  exposes people by design); an affirmation buffers the feeling, it does not
  change the fact. Route those to select-intervention-levers. Not for other
  kinds of message or script (draft-lever-content).
license: CC-BY-4.0
metadata:
  title: Write an exercise to help people feel less judged
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Joe Speed"
  org: IL
  weird: mixed-evidence
  tags: "self-affirmation, wise-interventions"
  consumes: "affirmation-context, audience-context-brief"
  produces: "intervention-draft"
---

## What it does

Drafts a values-affirmation exercise, a short writing task about a personally important value, tailored to one audience facing one specific evaluative threat.

People pick the value most important to them from a locally adapted list, then write why it matters and about a specific time it mattered. The output includes the value list, the selection prompt, the two-part writing prompt, timing and frequency guidance, and two mandatory cautions: the exercise does not replace fixing practical barriers, and its effect varies across contexts.

## When to use it

### Use it when
- A population is about to face, or repeatedly faces, a specific moment where a stigmatized or evaluative concern (financial shame, academic underperformance, a health stigma) could trigger defensiveness that works against the program's goal
- Someone asks for "something to help people feel less judged or defensive about X before we ask them to do Y"
- A program has fixed what it can structurally and wants to reduce the psychological threat that remains at the moment of engagement
- A team is about to copy a published affirmation exercise's US value list straight into a different population

### Do not use it when
- The actual problem is that a service is unaffordable, inaccessible, unavailable, or exposes people by its design (a visible location, a public list, a conspicuous process); an affirmation buffers the response to that fact, it does not change the fact. Route the structural or design problem to `select-intervention-levers`
- The team needs other intervention copy (messages, scripts, signage) for a chosen technique; that is `draft-lever-content`
- The team does not yet know whether people feel judged or why they disengage; diagnose first with `decompose-comb-barriers`
- The population is in acute distress or the stigma is clinical; see "When to bring in a specialist" before drafting anything

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The target population and the specific evaluative or stigmatized domain the exercise needs to buffer against (financial shame, academic underperformance, a health stigma), in the user's words.
2. **Required.** The moment: when the threat-relevant evaluation happens (the start of a workshop, an advising session, a test, a clinic visit) and how the exercise can be administered before it (written or verbal, paper or phone, the literacy level).
3. **Required.** What, if anything, is known about which values are meaningful to this population, and whether an audience and context brief from `map-audience-context` exists. Without either, the value list is a guess and will be labeled one.
4. Optional. Whether a structural or material barrier also sits behind the disengagement, so the non-substitute caution can name it.
5. Optional. How often the same person will encounter the exercise (once, each session, over months), which sets the frequency ceiling.

If 1 or 2 is missing, ask and stop. If 3 is missing, proceed with the standard list adapted by best guess, label it an unconfirmed adaptation, and recommend confirming it with someone from or close to the population. If 4 is missing, write the caution in general terms. If 5 is missing, assume one or two administrations.

## What it draws on

- Cohen, G. L., & Sherman, D. K. (2014). The psychology of change: Self-affirmation and social psychological intervention. *Annual Review of Psychology*, 65, 333–371.
- Sherman, D. K., & Cohen, G. L. (2006). The psychology of self-defense: Self-affirmation theory. *Advances in Experimental Social Psychology*, 38, 183–242.
- Hanselman, P., Sinclair, K. R., & Borman, G. D. (2017). New evidence on self-affirmation effects and theorized sources of heterogeneity from large-scale replications. *Journal of Educational Psychology*, 109(3), 405–424.
- Henrich, J., Heine, S. J., & Norenzayan, A. (2010). The weirdest people in the world? *Behavioral and Brain Sciences*, 33(2-3), 61–83.

Cohen and Sherman's applied self-affirmation protocol: ask someone to identify a personally important value unrelated to the threatened domain, then write briefly about why it matters and a specific time it mattered to them. Sherman and Cohen's account of the mechanism is that affirming a valued self-domain broadens perspective and reduces the need to defensively dismiss threatening information in an unrelated domain. That is why the writing prompt's two-part structure (why it matters, a specific time) is not optional decoration; a vaguer prompt ("write about something you value") does not reliably produce the self-affirming effect the mechanism depends on. Hanselman et al.'s replication findings are the basis for the mandatory heterogeneity caveat: the effect size varies by factors not fully mapped even within similar populations, so the output must flag that variation rather than imply a guaranteed effect.

If no audience and context brief is available, the value list is this skill's own best guess at cultural fit, not a locally grounded adaptation. The output must say so explicitly and recommend confirming the list with someone from or close to the target population before it is used, rather than presenting an unconfirmed guess with the same confidence as a brief-informed adaptation. The frequency-ceiling guidance in the delivery notes is drawn from single- or few-session study designs; for a delivery pattern the cited literature does not cover (for example a recurring outreach contact over months), say that explicitly and mark the stated ceiling as an extrapolated program judgment, not a literature-derived number.

**WEIRD skew:** The overwhelming majority of self-affirmation randomized trials were run in US school settings (Henrich, Heine, & Norenzayan, 2010), and Hanselman et al.'s large-scale replications found the effect itself is heterogeneous even within that WEIRD population, moderated by factors not fully understood. Treat a positive published effect as "worked in some US school contexts, with real variation", not as a universal effect this skill's output can guarantee anywhere.

**Replication status:** Mixed and heterogeneous. Hanselman, Sinclair, and Borman (2017) ran large-scale replications and found that the self-affirmation effect varies by factors not fully understood, even within the US school populations most of the original studies used. A null pilot result should be read against those moderators before anyone concludes the technique failed.

## How to do it

1. **Restate the population and threat domain**, condensed and close enough to verbatim that nothing is misrepresented.
2. **Build the value category list.** Use the standard US-derived list (relationships, religion, art, humor, spontaneity, social skills, athletics, music, career, education, creativity) only as a reference. Adapt it to what is locally and culturally meaningful for this population, using the audience and context brief if available. Actively drop any category that could reinforce the threat rather than merely fail to resonate, for example a faith-linked category where the stigma itself is partly moral or religious. If no brief is available, say so in the list and label it an unconfirmed adaptation pending local confirmation.
3. **Write the selection prompt**: a verbatim instruction asking the person to identify, from the list, the value most personally important to them, not the one they think they should pick.
4. **Write the two-part writing prompt**: (1) why this value is important to you; (2) a specific time this value mattered to you. Both parts are required; the two-part structure is the mechanism.
5. **Write the delivery notes.** Timing must precede the threat-relevant evaluative moment, not follow it; an affirmation written after the threatening event has already occurred does not buffer it. Duration is brief, roughly 5 to 10 minutes in the source protocol. State a frequency ceiling with the risk of diminishing or reversed effect if administered too often to the same person. If the delivery pattern is outside what the cited studies cover, mark the ceiling as an extrapolated program judgment.
6. **Write the non-substitute caution.** Name the structural, material, or design barrier this exercise does not fix (resource scarcity, a visibly exposing process, a community-level norm) and say it must not be presented or relied on as if it did.
7. **Write the heterogeneity caveat.** Name what about this population or context is unconfirmed relative to the published studies, per Hanselman et al., and say that a null pilot result should be checked against those factors before concluding the technique itself failed.

See `references/worked-example.md` for a complete run on a financial-literacy program for first-generation college students.

## Output template

```markdown
# Values-affirmation script

**Target population and threat domain (as given):** <condensed restatement of the input, not a mid-sentence quote; close enough to verbatim that nothing is misrepresented>

## Value category list
<adapt to what is locally and culturally meaningful for this population, using any input from an audience and context brief if available. Do not transplant the standard US-derived list (relationships, religion, art, humor, spontaneity, social skills, athletics, music, career, education, creativity) uncritically if there is reason to think it does not fit, and actively drop any category that could reinforce the threat rather than merely fail to resonate. If no audience and context brief is available, say so explicitly here and label this list an unconfirmed adaptation pending local confirmation.>
- <value 1>
- <value 2>
- <...>

## Selection prompt
<verbatim instruction asking the person to identify, from the list above, the value most personally important to them>

## Writing prompt (two-part structure; both parts required)
1. <why this value is important to you>
2. <describe a specific time this value mattered to you>

## Delivery notes
- **Timing:** <must precede the threat-relevant evaluative moment, not follow it>
- **Duration:** <brief; the source protocol uses roughly 5 to 10 minutes>
- **Frequency ceiling:** <state the risk of diminishing or reversed effect if administered too often to the same person, per the source literature; mark as extrapolated if the delivery pattern is outside what the studies cover>

## Non-substitute caution (mandatory)
<state plainly what structural, material, or design barrier, if any, this exercise does NOT fix, and that it should not be presented or relied on as if it did>

## Heterogeneity caveat (mandatory)
<name what about this specific population or context is unconfirmed relative to the published studies, per Hanselman et al.'s documented effect variation; a null pilot result should be checked against these factors before concluding the technique itself failed>
```

## Where it goes wrong

- **Uncritical list transplant.** Using the standard US-derived value list without checking whether it reflects what this population values is the most common way this skill's output looks complete but is not locally grounded.
- **Vague writing prompt.** A prompt that skips the "why it matters" or "specific time" part, or merges them into one vague instruction, is not the protocol this skill's evidence base validated; the two-part structure is the mechanism, not decoration.
- **Wrong-moment delivery.** Administering the exercise after the threatening moment (after a student has already been embarrassed in a session) cannot buffer an event that already happened.
- **Over-frequent administration.** Repeating the exercise until its effect wears off or reverses, with no stated frequency ceiling, is a documented risk the delivery notes exist to flag.
- **Used as a structural substitute.** Presenting this exercise as if it addresses the underlying material or structural barrier is the single most serious misuse, and the reason the non-substitute caution is mandatory.
- **Null result treated as universal failure.** Concluding "self-affirmation doesn't work for this population" from one pilot's null result, without checking it against the documented heterogeneity moderators, mistakes one context's result for a general finding.
- **Unflagged guesswork.** Producing a locally-adapted-looking value list when no audience and context brief was available, with the same confident framing as a brief-informed adaptation, misrepresents an unconfirmed guess as grounded research.
- **Structural barrier mistaken for the only kind.** Treating "structural or material barrier" as limited to resource scarcity (cost, access, time) misses design-driven exposure risk (a visibly parked van, a public sign-up list) and community-level norm barriers. Both are just as far outside this skill's scope as a funding gap, and the non-substitute caution must name them when they are the actual barrier.

## When to bring in a specialist

Tell the user to consult a clinical psychologist, a counselor, or a safeguarding lead when:
- The stigmatized domain is clinical or carries acute risk (mental illness, HIV status, suicidality, experience of violence); the writing prompt can surface distress, and the exercise needs clinical review and a referral path before use
- The participants are minors and the exercise will be delivered by school or program staff; consent, supervision, and what happens to the written responses need a child-protection review
- The population has recent collective trauma (displacement, conflict, disaster), where asking people to recall "a specific time this value mattered" can land on traumatic memory
- A pilot shows a negative or reversed effect; a specialist should read the moderators in the replication literature before any redeployment

Bring them: the condensed population and threat statement, the value list with its adaptation reasoning, the writing prompt, the delivery notes, and any pilot data.
