---
name: select-default-option
description: >-
  Use when people are not acting because doing nothing leaves them out
  ("nobody enrolls", "they never opt in") and the team wants to change what
  a person gets when they take no action. Also use when a team is about to
  flip a program from opt-in to opt-out and must decide the default, for
  whom, and how opting out works. Chooses the pre-set option and names the
  mechanism it relies on (endorsement, endowment, or effort), because the
  mechanism predicts both the effect size and whether the default is
  defensible; draws on the Jachimowicz et al. (2019) meta-analysis and the
  Afghanistan mobile-money default trial. Do not use when the problem is
  hassle inside the process rather than inaction at one decision point; run
  audit-process-friction instead. Not for restrictions a person places on
  their own future self (design-commitment-device), not for the enrollment
  notice wording (draft-lever-content), and not for deciding whether a
  default is the right technique (select-intervention-levers).
license: CC-BY-4.0
metadata:
  title: Choose what people get by default
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: likely-generalizes
  tags: "defaults, choice-architecture, behavior-change-techniques"
  consumes: "intervention-levers, barrier-diagnosis"
  produces: "intervention-draft"
---

## What it does

Chooses the pre-set option people receive when they take no action at one decision point.

It names the mechanism the default relies on (endorsement, endowment, or effort), because the mechanism predicts both how large the effect will be and whether the default is defensible. It also specifies how a person opts out and the opt-out rate above which the team should assume the default is wrong for the people receiving it. A default is a structural change to the choice, not a message; the notice that announces it is drafted afterwards by `draft-lever-content`.

## When to use it

### Use it when
- A confirmed barrier is inertia at one decision point: people say they want the thing, the option is available, and the no-action path leaves them without it ("nobody enrolls", "the form sits unsigned", "they never switch")
- A team is about to flip a program from opt-in to opt-out ("let's just auto-enroll everyone") and has not decided which option becomes the default, for whom, or how opting out works
- An enrollment, contribution, or consent step already has a default (there always is one, usually "nothing") and the team wants to check whether it serves the people who receive it
- The lever brief from `select-intervention-levers` names a default or pre-set option as the technique

### Do not use it when
- The problem is friction inside the process (many fields, documents, trips) rather than inaction at one point; a default does not remove the steps after it. Run `audit-process-friction`
- The person is meant to restrict their own future choices, such as a locked savings account they choose to open; that is an opt-in restriction, owned by `design-commitment-device`
- The team needs the words of the enrollment notice or the opt-out message; that is `draft-lever-content`, run after this skill
- No lever has been selected, or the barrier is motivation, cost, or supply rather than inertia; a default cannot create a want or supply a missing service. Go back to `select-intervention-levers`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The target behavior (who, what, when) and the confirmed barrier with its evidence, from `select-intervention-levers` or `decompose-comb-barriers`. The barrier must be inertia at a decision point: people intend to act, the option exists, and inaction is what stops them. If the barrier is friction, motivation, or supply, say so and stop.
2. **Required.** The decision point: where the no-action path lands a person today, what the current default is, and who controls that setting (the program, an employer, a bank, a clinic).
3. **Required.** Whether the default would move money, medical treatment, or legal status (a wage deduction, a test, a consent). This decides whether the ethics check can be closed here or needs a specialist.
4. Optional. What the team knows about who would be worse off under the proposed default (people with debts, people who need the cash at once, people for whom a treatment is contraindicated), because the default must serve the chooser, not the program.
5. Optional. Whether a trusted source stands behind the default, which decides whether the endorsement mechanism is available.

If 1 or 2 is missing, ask and stop. If 3 is missing, ask once; if still unclear, proceed and treat the default as one that moves money. If 4 is missing, proceed and list "who may be worse off" as the first open question. If 5 is missing, assume no trusted source and do not rely on endorsement.

## What it draws on

- Jachimowicz, J. M., Duncan, S., Weber, E. U., Hardisty, D. J., & Johnson, E. J. (2019). When and why defaults influence decisions: A meta-analysis of default effects. *Behavioural Public Policy*, 3(2), 159–186. https://doi.org/10.1017/bpp.2018.43
- Mertens, S., Herberz, M., Hahnel, U. J. J., & Brosch, T. (2022). The effectiveness of nudging: A meta-analysis of choice architecture interventions across behavioral domains. *Proceedings of the National Academy of Sciences*, 119(1). https://doi.org/10.1073/pnas.2107346118
- Maier, M., Bartoš, F., Stanley, T. D., Shanks, D. R., Harris, A. J. L., & Wagenmakers, E.-J. (2022). No evidence for nudging after adjusting for publication bias. *Proceedings of the National Academy of Sciences*. https://doi.org/10.1073/pnas.2200300119
- Blumenstock, J., Callen, M., & Ghani, T. (2018). Why Do Defaults Affect Behavior? Experimental Evidence from Afghanistan *American Economic Review*, 108(10), 2868–2901. https://doi.org/10.1257/aer.20171676
- Münscher, R., Vetter, M., & Scheuerle, T. (2016). A review and taxonomy of choice architecture techniques. *Journal of Behavioral Decision Making*, 29(5), 511–524. https://doi.org/10.1002/bdm.1897
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709
- Ferraro, P. J., & Tracy, J. D. (2022). A reassessment of the potential for loss-framed incentive contracts to increase productivity: A meta-analysis and a real-effort experiment. *Experimental Economics*, 25(5), 1441–1466. https://doi.org/10.1007/s10683-022-09754-x
- Behavioural Insights Team (2014; revised and updated edition, c. 2024). *EAST: Four simple ways to apply behavioural insights*, "Make it easy". London: BIT. https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf

A default is the option a person gets by taking no action. Jachimowicz et al. (2019) pool 58 studies (N = 73,675) and find d = 0.68 (95% CI 0.53–0.83) with I² ≈ 98% (nearly all the variation between studies is real difference, not sampling noise) and two studies where the default pushed people the wrong way. They distinguish three mechanisms, which this skill makes the user choose between; the labels are theirs and the one-line glosses are this skill's: endorsement (the default is read as what a trusted party recommends), endowment (people treat the pre-set option as already theirs and dislike giving it up), and effort (switching needs a decision and an action that people put off). Münscher, Vetter & Scheuerle (2016) place defaults among the "decision structure" techniques, and Mertens et al. (2022) find structure interventions the strongest class of nudge (overall d = 0.45, 95% CI 0.39–0.52, more than 200 studies, N ≈ 2.15 million, moderate publication bias). Discount for a field program: Maier et al. (2022) put the bias-corrected nudge average at about d = 0.04; DellaVigna & Linos (2022) find academic trials average 8.7 percentage points where nudge-unit trials average 1.4, with about 70% of the gap explained by selective publication and low power; the loss-framing literature shrinks from 0.33 SD in the lab to 0.02 SD in the field (Ferraro & Tracy, 2022). Plan for a fraction of the published effect. The judgment calls this skill adds are the mandatory mechanism line, the opt-out monitoring threshold, and the rule that a default which would leave an identifiable minority worse off is replaced by an active choice for that group.

**WEIRD skew:** The dossier does not break the 58 pooled studies down by country, and the nudge meta-analyses it sits beside record moderate publication bias and large heterogeneity, so treat the pooled numbers as untested in your setting until checked locally: who is allowed to set defaults there, whether the sponsor is trusted (endorsement is unavailable otherwise), whether people need the cash or service at once, and whether a default from an institution reads as that institution taking something. **Non-WEIRD evidence:** Afghanistan (Blumenstock, Callen & Ghani, 2018): 949 employees paid through mobile money; a 5% default contribution versus a 0% default raised participation by 40 percentage points, equivalent to a 50% employer match; the authors trace the effect to present bias and the cognitive cost of deciding, not to endorsement or inattention, and savings attitudes persisted after the trial.

**Replication status:** replicated; the direction is robust across 58 studies, but the size varies widely (I² ≈ 98%), two studies found negative effects, effects are weaker in environmental domains, and the planning number for a field program is well below d = 0.68.

## How to do it

1. **Carry the target behavior and confirmed barrier over verbatim**, and check that the barrier is inertia at a decision point. If people do not want the thing, cannot reach it, or are stuck in the steps after the decision, a default is the wrong technique; say so and route back.
2. **Locate the decision point and name the current default.** Write what happens today to a person who does nothing, and who controls that setting. There is always a default; the question is whether the current one serves people.
3. **Decide the welfare-maximizing option and for whom.** State who gains under the proposed default and who could be worse off (needs the cash now, treatment contraindicated, already covered elsewhere). If an identifiable group would be worse off, specify an active choice (the person must pick; nothing is pre-set) or a different default for that group. The default must serve the chooser, not the program's enrollment target.
4. **Name the mechanism** the default relies on: endorsement, endowment, or effort. Give the evidence from the setting that supports it (a trusted sponsor for endorsement; a visible balance or entitlement for endowment; a decision people postpone for effort) and what would show a different mechanism is at work. The Afghanistan result ran on effort and present bias, not endorsement; do not assume endorsement where no trusted source stands behind the default.
5. **Design the opt-out so it is easy, visible, and free.** One step, no penalty, no waiting period, stated in the same place the default is announced. A default with a hidden or costly opt-out is coercion dressed as a nudge.
6. **Set the opt-out monitoring threshold.** State the opt-out rate above which the team will treat the default as wrong for this population and review it, and how the team will learn whether people who stayed in are worse off (complaints, reversals, hardship withdrawals).
7. **Run the ethics check.** Does the default serve the chooser; is it transparent; could it be read as the organization taking something (the bad-intent signal behind the negative studies)? If the default moves money, medical treatment, or legal status, send the specification to `audit-intervention-ethics` and the specialist named below before any pilot.
8. **State the expected effect, discounted.** Quote the meta-analytic numbers with their corrections, then say what the team should plan for in a field program and why it is smaller. Never give d = 0.68 or the Afghanistan 40 points as the planning number.
9. **Stop here.** The notice that announces the default and the opt-out wording are drafted by `draft-lever-content`; the test is designed by `plan-evaluation-design`.

See `references/evidence-notes.md` for the annotated sources and `references/worked-example.md` for a complete run on a Bangladesh payroll savings default.

## Output template

```markdown
# Default option specification

**Target behavior:** <who + what + when, carried over verbatim>
**Confirmed barrier:** <the inertia barrier and the evidence that confirmed it>
**Decision point:** <where the no-action path lands a person today, what the current default is, who controls it>

## The default
- **Proposed default:** <the option a person gets by doing nothing>
- **Who receives it:** <the population, or the segment, it applies to>
- **Who it is not for:** <people who could be worse off, and the active choice or different default they get; or "none identified, see open questions">

## Mechanism
- **Relied on:** <endorsement / endowment / effort>
- **Why this setting supports it:** <the local evidence>
- **What would show a different mechanism:** <an observable sign>

## Opt-out
- **How:** <the one step>
- **Where it is shown:** <same place as the default announcement>
- **Cost to the person:** <none, or state it and justify>

## Monitoring
- **Opt-out threshold:** <rate above which the default is reviewed, and who reviews>
- **Harm check:** <how the team learns whether those who stayed in are worse off>

## Ethics check
- **Serves the chooser because:** <...>
- **Bad-intent signal:** <could the default read as the organization taking something; how that is avoided>
- **Transparency:** <how the person is told, before the default applies>
- **Escalation:** <none needed / sent to audit-intervention-ethics and <specialist> because it moves money, treatment, or legal status>

## Expected effect
<the published numbers with their corrections, then the discounted planning range for this program and why>

## What to check before relying on this
- <the assumption most likely to be wrong>
- <open questions for the pilot>
```

## Where it goes wrong

- **A default that serves the program.** Auto-enrolling people in a fee-bearing product, a data-sharing consent, or a contribution rate set to hit a target is the program using inertia against the chooser. If the honest answer to "who is this default for?" is the organization, refuse and say why.
- **Opt-out in name only.** An opt-out that needs a visit, a form, a waiting period, or a conversation with a supervisor is not an opt-out. The opt-out lines in the template are a hard requirement, not a formality.
- **Assuming endorsement.** Writing "people will trust the recommendation" when no trusted party stands behind the default. The Afghanistan effect ran on effort and present bias; a default from an unknown or distrusted sponsor can read as a grab, which is the documented route to a negative effect.
- **Planning on the meta-analytic number.** d = 0.68 is the pooled published effect with I² ≈ 98%; the bias-corrected nudge average is near zero and nudge-unit trials run far below academic ones. A pilot powered on d = 0.68 will be underpowered.
- **Running on the wrong barrier.** Defaults act on inertia at one point. Where people lack intention, access, or trust, or where the hassle sits in the steps after the decision, the default changes who is enrolled on paper and nothing else.
- **One default for everyone.** Keeping a single default where a known group is worse off under it (needs the cash, cannot take the treatment) because segmenting is harder. Harder is not a reason; specify an active choice for that group.

## When to bring in a specialist

Tell the user to consult the relevant specialist, and to run `audit-intervention-ethics`, when:
- The default moves money (a wage or benefit deduction, a contribution rate, a fee, a loan feature); a financial-services compliance lead must check the opt-out and the disclosure against consumer-protection rules before a pilot
- The default sets medical treatment or testing (a default test, a default prescription, a default referral); a clinician must confirm that the opt-out path is safe and that the default is appropriate for everyone who receives it
- The default changes legal status or consent (data sharing, enrollment in a scheme with obligations, a signed agreement); a lawyer must confirm that consent by inaction is valid in that jurisdiction
- The default sits in an environmental domain or the sponsor is distrusted; a behavioral scientist should judge whether a default is the right technique, given the weaker and sometimes negative results there

Bring them: the specification with its mechanism line, the opt-out design, the monitoring threshold, and the list of who could be worse off.
