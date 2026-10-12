---
name: adapt-survey-for-phone-mode
description: >-
  Use when a survey built for face-to-face interviews has to run over the
  phone ("we can't travel, can we do the endline by phone?", "convert our
  questionnaire for a call", "set up an IVR survey"), or when a team asks
  how long a phone survey can be, what to do about showcards, or how to
  reach people who share a phone. Produces a phone-ready instrument cut to
  a target call length, visual scales replaced by verbal unfolding scales,
  audio instructions, a call protocol (attempts, call-backs, airtime
  incentives, consent), a phone-ownership check on the sampling frame, and
  a mode-effect comparison plan. Do not use when the items do not exist
  yet; use draft-survey-items. Not for translation
  (translate-survey-instrument), pretesting the phone version
  (draft-cognitive-interview-script), how many numbers to call under
  attrition (estimate-sample-size), choosing an existing validated measure,
  or developing or validating a scale; those last two are separate skills.
license: CC-BY-4.0
metadata:
  title: Move a face-to-face survey to the phone
  type: atomic
  stage: measure
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "measurement, survey-design, quantitative"
  consumes: "survey-items"
  produces: "survey-items"
---

## What it does

Converts a face-to-face survey instrument into a version that can be administered by voice, over a live call or an interactive voice response (IVR) system.

A phone call removes everything the respondent could see, shortens the time they will give, and changes who is reachable: the sample becomes the people who own or answer a phone. This skill rewrites the instrument for those constraints, writes the call protocol around it, checks the sampling frame for who will be missed, and plans a check of whether answers differ by mode. It does not write new items, translate them, or set the sample size.

## When to use it

### Use it when
- A team says "we can't go to the field; can we do the survey by phone?" and has a face-to-face questionnaire in hand
- A questionnaire uses showcards, ladders, visual analog scales, or pictures, and the team asks how to ask those items over a call
- A team is planning computer-assisted telephone interviewing (CATI, a live enumerator calling) or IVR (recorded prompts with keypad or voice answers) in a low-income setting and asks how long the call can be, what incentive to pay, or how many times to try a number
- Someone worries that a phone survey will miss women, poorer households, or people in areas with weak coverage, and wants that checked before fielding

### Do not use it when
- The items do not exist yet; write them with `draft-survey-items`, then convert
- The items need to be in another language; `translate-survey-instrument` does that, before or after the mode change
- The phone version exists and the question is whether respondents understand it over a call; run `draft-cognitive-interview-script` by phone, which this skill hands its output to
- The question is how many numbers to call so that enough complete interviews survive non-response and attrition; that is `estimate-sample-size`
- The team wants to pick an existing validated measure or build and validate a scale; choosing an existing measure and developing or validating a new scale are separate skills

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The face-to-face instrument verbatim, including showcards, visual aids, interviewer instructions, and its current length in minutes.
2. **Required.** The target mode (live call, IVR, or both) and the reason for phone delivery (cost, access, safety, timing), because the reason sets what can be sacrificed.
3. **Required.** The sampling frame: where the phone numbers come from, whose numbers they are (the respondent's own, a household head's, a contact's), and what is known about phone ownership and sharing in this population, by gender.
4. **Required.** Which items are essential to the decision the survey informs. Without a core list, the cut in step 1 is arbitrary.
5. Optional. Budget for airtime incentives; the languages the enumerator pool covers; whether a face-to-face subsample is feasible; which items the team considers sensitive.

If 1 to 4 are missing, ask and stop. If 5 is missing, assume a small airtime incentive is affordable, plan the face-to-face subsample and mark its cost as unconfirmed, and flag any item that looks sensitive.

## What it draws on

- Hoogeveen, J., Dabalen, A., et al. (2016). *Mobile Phone Panel Surveys in Developing Countries: A Practical Guide for Microdata Collection*. World Bank. https://doi.org/10.1596/978-1-4648-0904-0
- Gourlay, S., et al. (2021). Viewpoint: High-frequency phone surveys on COVID-19: Good practices, open questions. *Food Policy*, 105, 102153. https://doi.org/10.1016/j.foodpol.2021.102153
- J-PAL. *Resources for conducting remote surveys*. https://www.povertyactionlab.org/resource/resources-conducting-remote-surveys
- World Bank LSMS and DIME Wiki pages on phone surveys: unverified, author to confirm (the pages returned 403 in the dossier audit; nothing from them is used).

The World Bank guide is the practitioner manual for running panel surveys by mobile phone in developing countries. Gourlay et al. draw good practices and open questions from the high-frequency phone surveys run during COVID-19. J-PAL's remote-survey page covers survey length, respondent tracking, and call scheduling, and states that surveys should be kept to a 30-minute call at most; it does not cover mode effects or IVR, and the "15 to 20 minutes" figure that circulates for phone surveys is unverified, author to confirm, so this skill plans to the 30-minute ceiling and shorter where the population or IVR demands it. The dossier's boundary conditions for this skill, not attributed to a single source, are: replace showcards with verbal unfolding scales; plan the call protocol (scheduling, recording attempts, replacing respondents, matching surveyors by language) and incentives; and test for mode effects against a face-to-face subsample. Judgment calls this skill adds: the gender check on who answers a shared phone, the privacy check before sensitive items, and the IVR guidance in step 3, which is this skill's practitioner judgment rather than something the cited sources were confirmed to cover. See `references/evidence-notes.md`.

**WEIRD skew:** None in the usual sense: both anchor sources are written for and from low- and middle-income country phone surveys. The skew that matters is within the population: phone samples skew toward phone owners, who are more often men, better off, and in covered areas. A user should check ownership and sharing by gender and wealth in their own frame before trusting any phone estimate. **Non-WEIRD evidence:** the World Bank guide (developing-country panel surveys) and the LSMS high-frequency COVID-19 phone surveys reviewed by Gourlay et al.; the dossier records no response-rate or effect numbers from either.

**Replication status:** Procedural; the one finding the dossier records consistently is that phone samples skew toward phone owners. Whether answers themselves differ by mode is left as an open question in the sources, which is why this skill plans a mode-effect check rather than asserting comparability.

## How to do it

1. **Cut to the core and set the target length.** List every item against the decision it feeds; keep the essential ones, move the rest to "drop" or "later wave". Target at or below J-PAL's 30-minute ceiling for a live call; for IVR set the target from a pilot, since no verified IVR length is in the sources.
2. **Convert every visual item.** Showcard rating scales become verbal unfolding scales: ask direction first ("better or worse?"), then intensity ("a little or a lot?"). Ladders and numbered scales get both endpoints read aloud in words. Pictures and visual analog scales become short labeled categories. Record the mapping for each item so the face-to-face and phone versions can be compared.
3. **Rewrite instructions for audio.** Short sentences; options repeated for every item; nothing that depends on something the respondent can see. For IVR: one idea per prompt, a keypad mapping read aloud, a repeat option, and few enough options to hold in memory; pilot the count.
4. **Write the call protocol**: the spoken consent script; identity check; "is this a good time, and can you speak privately?"; number of attempts spread across times of day and days of the week; call-back scheduling; the rule for replacing a number; language matching of enumerators to respondents; a log entry for every attempt; and the airtime incentive, its amount and when it is sent.
5. **Check the frame for who you will reach.** Compare phone ownership and sharing in the population, by gender and wealth, against the program's target group. Decide how the intended respondent is asked for on a shared phone, when to call back, and that the log records who actually answered.
6. **Handle sensitive items.** For each, decide: keep with a privacy check, drop, or escalate. Never ask on speakerphone. If the phone is shared and the item could expose the respondent, the default is drop.
7. **Plan the mode-effect check.** Draw a random face-to-face subsample that answers the same core items; state which items are compared, and pre-specify what size of difference would change the survey's conclusion. If no subsample is feasible, say what is lost and plan at least a comparison with the previous face-to-face round on the overlapping items.
8. **Pretest the phone version by phone** with `draft-cognitive-interview-script`, flagging converted items for extra probes.
9. **Stop here.** How many numbers to call so that enough interviews survive non-response is `estimate-sample-size`'s job; phone attrition is one of its inputs.

See `references/worked-example.md` for a complete run on a Bangladesh mobile money enrollment endline.

## Output template

```markdown
# Phone-mode instrument: <survey name>

**Mode:** <live call / IVR / both>  **Face-to-face length:** <minutes>  **Target call length:** <minutes, at or below 30 for a live call>
**Frame:** <source of numbers; whose numbers; ownership and sharing by gender and wealth as known>
**Why phone:** <cost / access / safety / timing>

## 1. Core items kept, items dropped
| Item | Decision it feeds | Keep / drop / later wave | Why |
|---|---|---|---|
| <1> | <...> | <...> | <...> |

## 2. Converted items
| Item | Face-to-face format | Phone format | Spoken wording |
|---|---|---|---|
| <1> | <showcard, 5 points> | <unfolding: direction, then intensity> | <exact words> |

## 3. Consent script and audio instructions
<spoken consent; identity check; privacy check; instructions as read>

## 4. Call protocol
- Attempts: <n>, spread over <times of day> and <days>
- Call-back rule: <...>
- Replacement rule: <...>
- Enumerator language matching: <...>
- Incentive: <airtime amount; when sent>
- Log per attempt: <fields>

## 5. Who you will reach
<ownership and sharing by gender and wealth; how the intended respondent is asked for; what is recorded about who answered; who the frame will miss>

## 6. Sensitive items
| Item | Keep with privacy check / drop / escalate | Why |
|---|---|---|
| <...> | <...> | <...> |

## 7. Mode-effect check
<subsample size and how drawn; items compared; the difference that would change the conclusion; or what is lost if none is feasible>

## 8. Pretest
<number of phone cognitive interviews; converted items flagged; handed to draft-cognitive-interview-script>

## What to check before relying on this
- <the group the frame most likely misses>
- <the converted item most likely to produce a mode difference>
```

## Where it goes wrong

- **Keeping the whole questionnaire.** The model shortens by trimming words instead of dropping items; a 60-minute face-to-face instrument read faster is still a 60-minute call. The cut is by decision relevance, and the drop list is part of the output.
- **Reading a showcard scale aloud as it stands.** Five or seven points with labels only at the ends cannot be held in memory over a call; every such item is converted to an unfolding scale or labeled categories, and the mapping is recorded.
- **Quoting an unverified length or attributing mode-effect rules to J-PAL.** The verified figure is a 30-minute ceiling; "15 to 20 minutes" is unverified, and J-PAL's page does not cover mode effects or IVR. The skill says so rather than inventing a source.
- **Assuming the number reaches the person.** A number listed for a woman respondent is often a husband's or a neighbor's phone; the protocol asks for the intended respondent, records who answered, and calls back rather than interviewing whoever picked up.
- **Sensitive items on a shared phone.** HIV status, violence, or income at risk from a listener: the skill must not keep these in a phone instrument without a privacy check, and must escalate when the phone is shared.
- **Treating phone results as comparable to the face-to-face baseline without a check.** A change between a face-to-face baseline and a phone endline is a mode difference until the mode-effect comparison says otherwise; the output must say this.

## When to bring in a specialist

Tell the user to consult a survey methodologist with remote data collection experience, and the ethics board, when:
- The survey collects sensitive information (HIV status, intimate partner violence, illegal or hidden income, political views) and respondents may share phones or be overheard; the question is whether the item can be asked by phone at all, not how to word it
- Phone-ownership gaps would exclude the population the program is for (women without their own phone, the poorest households, uncovered areas); a sampling statistician should say whether a phone survey can answer the question or whether a mixed-mode design is needed
- The plan is IVR with a low-literacy, multilingual population and no pilot has run; someone who has fielded IVR in that setting should review the prompt design before any number is called

Bring them: the sampling frame with what is known about ownership and sharing, the list of sensitive items, the draft call protocol, and the mode-effect plan.
