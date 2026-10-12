# Worked example: fertilizer top-dressing timing in Western Kenya

Illustrative run on an invented program. The names, counts, and shares are made up to show the skill's shape; none is a finding.

**Setting.** "Shamba Bora" (illustrative), an input-and-training program for smallholder maize farmers in Kimilili sub-county, Bungoma County. The target behavior came from `define-key-behavior`; the diagnosis from `diagnose-social-norm` (a survey of 180 enrolled farmers, illustrative); the lever brief from `select-intervention-levers` selected social comparison delivered by SMS from the field officer.

**Inputs supplied.** Field-officer records from the last long-rains season: 64% of enrolled farmers in Kimilili top-dressed within the recommended window (illustrative). Survey: the median farmer believed about 4 in 10 neighbors top-dress on time; 82% said a farmer who top-dresses on time is "doing what a good farmer should" (illustrative). Channel: SMS in Kiswahili from the named field officer, sent two weeks after recorded planting. The program knows which enrolled farmers top-dressed on time last season.

```markdown
# Social norm message draft

**Target behavior:** Smallholder maize farmers enrolled in Shamba Bora in Kimilili sub-county apply CAN top-dressing fertilizer to their maize between the third and fifth week after planting, each long-rains season.
**True descriptive norm:** 64% of enrolled farmers in Kimilili sub-county top-dressed within the window last long-rains season (field-officer plot records, season ending August 2025; illustrative).
**Belief being corrected:** Farmers believe about 4 in 10 neighbors top-dress on time (survey median, illustrative); 82% say on-time top-dressing is what a good farmer should do. The gap is empirical, not normative.
**Norm type:** Descriptive lead, with an injunctive cue. The belief gap is about what others do; the cue protects the 64% who were already on time last season.

## Message
Habari, <farmer name>. Last season, more than 6 out of every 10 Shamba Bora farmers in Kimilili top-dressed their maize by week 5. Asante if you were one of them. Your maize was planted on <date>: top-dress by <date + 35 days>. Field officer <name>.

## Injunctive cue
"Asante if you were one of them." A farmer who was on time last season reads this as thanks for continuing, not as a signal that being above average means they can relax this season. It sits before the request so the request lands as the next step, not as a correction.

## Reference group check
- Group named in the message: Shamba Bora farmers in Kimilili sub-county
- Group the number actually describes: enrolled farmers in Kimilili sub-county, last long-rains season
- Match: same. A ward-level figure would be closer still; the records can be cut by ward and the team should check whether every ward is above half before using ward figures.

## Backfire checks
- Majority check: yes, 64% is above half. If any ward is below half, that ward receives the sub-county message, not a ward figure.
- Unwanted-behavior prevalence: the message does not state or imply how many farmers were late. "More than 6 out of 10" is the only share given.
- Sensitivity: not sensitive. Top-dressing timing carries no stigma or legal exposure in this setting.

## Delivery notes
- Sender: the named field officer, whose visits already make them the person farmers expect judgment from on agronomy; approval from them is credible because they see the plots.
- Timing: two weeks after recorded planting, so the window is still open and the action is one specific day away, not a season away.
- Exposures: one SMS. A second reminder at week 4 may be added only if the pilot shows no boomerang; no third.

## Boomerang measurement plan
- Baseline split: last season's plot records identify farmers who top-dressed on time (above norm) and those who did not (below norm) before the SMS goes out.
- Outcome by group: on-time top-dressing this season from the same plot records, compared with a randomly held-out set of farmers in each group who receive the plain reminder without the norm line.
- Decision rule: if the on-time group's rate falls relative to its held-out counterpart by more than the pilot's pre-set margin, the cue failed and the norm line is removed; if the below-norm group's rate rises, the message is kept.

## What to check before relying on this
- The belief gap is the main assumption: the survey median is 4 in 10, but if farmers in some wards already know most are on time, the message does nothing there.
- The 64% is from program records, which cover enrolled farmers only; a farmer whose "people like me" are non-enrolled neighbors may discount it.
- The expected effect is a point or two of on-time top-dressing, not the Guatemala headline; the pilot sample must be sized for that.
```

**What happened next (illustrative).** The draft went to `draft-lever-content`'s comprehension pre-test with eight farmers in Kiswahili; the measurement plan went to `plan-evaluation-design` for the held-out comparison. No results are reported here.
