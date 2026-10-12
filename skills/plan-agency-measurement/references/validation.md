# Testing and interpreting agency measures (next steps 3 and 4)

Use this to choose the checks for each measure in the plan and to say what their results would mean. A measure earns trust only when it has been checked, and the check should be proportionate: name the cheapest credible next step for the claim the team will make, not a full psychometric program. Full citations and verification status are in `evidence-notes.md`.

## The properties

- **Reliability:** the measure gives consistent results under similar conditions. It is a precondition for validity, not a substitute.
- **Construct validity:** it captures agency as the plan defines it, not a neighbor such as mood, satisfaction, engagement, or knowledge.
- **Content validity:** it covers the parts of agency that matter here, not only the parts that are easy to ask about.
- **Criterion validity:** its scores line up with real-world outcomes or behaviors the team has reason to trust, either at the same time (concurrent) or later (predictive).
- **Convergent and discriminant validity:** it correlates with measures of the same thing and not with measures of different things.

## Proportionality

| The claim the team will make | What is usually enough |
|---|---|
| Internal product iteration ("version B seems to support more student revision") | Face and content review by people who know the users; a hand-read sample of what each log signal or LLM code flags; one agreement check for any coded measure |
| A comparison between versions or arms | The above, plus the same instrument and coding applied identically in every arm, and reliability reported per arm |
| A funder-facing, public, or published claim that agency changed | The above, plus a pretested and, where needed, translated instrument; reliability and structure checked in this population; a criterion check against a trusted outcome; a specialist's review (see the skill's escalation section) |
| A comparison across languages, countries, or genders | All of the above, plus a measurement invariance test before any scores are compared |

## By tool type

### Surveys (in-app or off-platform)
- **Content:** expert review of each item against the definition, plus cognitive interviews with the users themselves. Boateng et al. (2018) suggest 5 to 15 interviewees over 2 to 3 rounds; hand this to `draft-cognitive-interview-script`.
- **Translation:** two independent forward translations and reconciliation, through `translate-survey-instrument`, before any pretest in a new language.
- **Reliability and structure:** internal consistency (alpha or omega) and, for multi-item scales, factor structure. Boateng et al. give a rule of thumb of 10 respondents per item or 200 to 300 observations for structure. Developing or validating a new scale is beyond this skill; bring in a psychometrician.
- **Comparing groups, languages, or time points:** test measurement invariance in sequence (configural, then metric, then scalar) before comparing means (Vandenberg & Lance, 2000; Putnick & Bornstein, 2016), including longitudinal invariance for before-and-after designs, since the tool itself can change how users read the scale. Partial invariance is common: it appeared in about a third of published tests. Anchoring vignettes (users rate short stories about hypothetical people on the same scale as themselves) detect and correct differences in how groups use a scale (King et al., 2004); in Uganda, vignettes also made autonomy items easier to understand (Donald et al., 2020).
- **Low- and middle-income settings:** expect systematic rather than random error. In Western Kenya, noncognitive self-reports showed acquiescence bias, enumerator effects, and test-retest correlations below standard thresholds even after correction (Laajaj & Macours, 2021), and Big Five items largely failed in face-to-face surveys across 23 countries (Laajaj et al., 2019). Pilot cognitively, check test-retest, randomize or hold enumerators constant across arms, and balance item keying only where respondents can handle reverse-worded items (see `draft-survey-items` for the low-literacy caution).
- **Short modules:** a short module can be built by benchmarking candidate items against coded qualitative interviews and keeping the few that track them best (Jayachandran, Biradavolu & Cooper, 2023), and self-reports can be checked against intensive qualitative follow-up with a random subsample (Blattman et al., 2016).
- **Self-report cautions:** directive questions that make the topic obvious inflate answers among people who identify with the goal (Brenner & DeLamater, 2016), and product-referencing items carry halo effects (AI Evaluation Playbook). Self-reported use tracks logged use only moderately (Parry et al., 2021, r = 0.38), so measure use from logs and perceptions from surveys.

### Observation and rubrics
- Train raters on anchored examples; double-score a sample and report inter-rater reliability (Cohen's or Fleiss' kappa, Krippendorff's alpha, or the intraclass correlation); revise anchors where raters disagree.

### Interviews and qualitative data
- An explicit codebook, a second coder on a subset, and triangulation with another source. Coding at scale with a language model follows the LLM protocol below.

### Administrative and outcome records
- Check data quality and coverage, and check that the agency measure comes before the outcome it is supposed to predict.

### Digital traces and logs
- Name the likely error sources for each log signal (the questions in `measurement-options.md`, from Sen et al., 2021).
- Hand-read a random sample of the events each signal flags to confirm they mean what the plan says.
- Link surveys to logs through a platform identifier, not one the user types; Kizilcec et al. (2017) lost 1,450 of 6,709 survey responses because typed identifiers could not be matched to logs.

### LLM-as-a-measure (experimental)
Validate for this prompt, this model version, these settings, these users, and this language. Good results elsewhere do not transfer: in a replication of 27 annotation tasks, 9 had precision or recall below 0.5 despite a high median (Pangakis et al., 2023), and in the GABRIEL benchmark the tenth-percentile task was around 0.5 accuracy (Asirvatham et al., 2026).

1. **Write a codebook both humans and the model can use:** definition, inclusion and exclusion rules, low, medium, and high anchors, and examples. Run label-free checks first (does the code change if the codebook order changes? does accuracy hold if the label "agency" is swapped for a neutral word?), following Halterman & Keith (2026).
2. **Draw the gold-standard sample at random, with recorded sampling probabilities,** stratified by the subgroups and arms the plan will compare. A random sample lets the human codes both validate the model and correct downstream estimates with design-based supervised learning or prediction-powered inference (Egami et al., 2023; Angelopoulos et al., 2023).
3. **Establish human agreement first.** Two trained coders code the sample independently; resolve the codebook until they agree. The AI Evaluation Playbook suggests agreement above 0.8 before trusting a judge; treat that as a practitioner rule of thumb.
4. **Compare the model with the human consensus, and report it beside human-human agreement** (Chatterji et al., 2025, report a human Fleiss' kappa of 0.60 against a model-human kappa of 0.74 on their taxonomy; Asirvatham et al., 2026, compare model and individual humans against the consensus).
5. **Examine disagreements by subgroup.** Regress coding errors on user characteristics; LLM errors in Bangladesh interviews were not random with respect to refugee status, gender, education, income, or trauma history (Ashwin, Chhabra & Rao, 2026). Check each language separately; LLM judges can perform poorly in low-resource languages (AI Evaluation Playbook), and machine translation adds its own error.
6. **Fix and record the model, version, prompt, and temperature, and test repeat stability;** identical inputs can produce different codes (Reiss, 2023; Törnberg, 2024).
7. **Guard against judge biases:** randomize option order, control for response length, and do not let a model from the same family as the deployed tool judge the tool's conversations (Zheng et al., 2023).
8. **State the reach.** A transcript can show a user setting a goal, not whether they followed through, and transcripts miss much of what users intend; frontier models inferred users' private reasons and reactions only partly in ThoughtTrace (Jin et al., 2026). Pair any transcript measure with in-the-moment self-report or an off-platform check.
9. **Protect the data.** Consent that covers this use, de-identification before transcripts reach any external model, a retention limit, and a privacy-preserving pipeline where human reading of raw transcripts is itself a risk (Tamkin et al., 2024, describe one).

Hand the full check to `audit-llm-qualitative-coding` once the model has coded the sample.

## Signals that move the wrong way

- **Approval is not agency.** Designs that most reduced over-reliance on AI got the lowest user ratings (Buçinca et al., 2021), and conversations with more disempowerment potential got more thumbs-up (Sharma et al., 2026). Never use ratings as a validation criterion for an agency measure.
- **Assisted performance is not capability.** In a Turkish high-school trial, practice scores rose with an unguarded GPT-4 tutor while unassisted exam scores fell 17%, and students did not perceive that they had learned less (Bastani et al., 2025). Where the end goal is capability, validate against an unassisted outcome measured after the tool is removed.

## Interpreting the evidence

What the checks can tell the team, and what to do next. These are reasoning rules, not cut-offs; where a number is given it is a practitioner rule of thumb.

| What the check shows | What it suggests | Next move |
|---|---|---|
| In cognitive interviews, users read an item differently from the definition | The item measures something else here | Reword or drop it; if many items fail the same way, the construct may not hold locally: revisit it with `define-agency-construct` |
| Low internal consistency or poor test-retest | Noise from wording, translation, response format, or enumerators, or items that do not belong together | Check translation, response options, and enumerator effects before dropping items |
| The factor structure differs from the published one | The construct is organized differently in this population | Do not sum items into the published subscales; report items or a locally supported structure, and consider rethinking the construct |
| The one-item in-app check does not track the off-platform multi-item version | The pulse is not a proxy for the battery | Keep it as a separate signal or drop it; do not report it as the construct |
| The measure does not relate to an outcome the team trusts | It may capture a neighbor (mood, satisfaction, knowledge) or the outcome may not depend on agency | Check what it does correlate with; revisit the construct before scaling the measure |
| Invariance fails across groups, languages, or arms | Scores do not mean the same thing across them | Do not compare means; report within groups, or test partial invariance with a specialist |
| Model-human agreement on LLM codes is well below human-human agreement, or errors cluster in a subgroup | The model is not measuring the construct, at least for that subgroup | Do not use model codes for that claim or subgroup; revise the codebook, or keep human coding |
| Log signals and self-reports move in opposite directions | Users may feel more agentic while relying more on the tool, or the reverse | Report both; this is the pattern the 2x2 agency framework is built to catch, not noise to average away |

Evidence that keeps contradicting the definition is a finding in itself: record it and take it back to `define-agency-construct` rather than forcing the data into the original construct.
