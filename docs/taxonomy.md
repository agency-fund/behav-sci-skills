# Taxonomy

The controlled vocabularies live in `taxonomy.yaml` at the repository root. This page explains them. Change the YAML file in the same pull request as the first skill that needs the change.

## Stage

Where in a project a skill is normally used. Every skill declares one. The seven stages are strong recommendations rather than rules: a skill that fits none uses `other`, which the validator accepts with a warning so maintainers notice recurring gaps.

| Stage | Covers | BIT TEST | Busara AUDAS | TAF four-level evaluation |
|---|---|---|---|---|
| define | Turn a goal, population, or outcome into something specific enough to work on | Target | Assess | Level 0, theory of change |
| diagnose | Explain why the current behavior pattern exists | Explore | Understand | Level 1, formative research |
| design | Produce intervention content, levers, messages, strategy | Solution | Design | Level 1, prototype |
| measure | Choose, adapt, or build instruments | Trial (measurement) | Assess | Level 2, outcome measures |
| test | Plan a pilot, experiment, or evaluation | Trial | Assess | Level 3, experimental evaluation |
| analyze | Analyze data from a test and interpret it | Trial (analysis) | Assess | Levels 3 and 4, analysis |
| implement | Roll out, adapt, scale, and report | Scale | Scale | Level 4, scale and welfare |
| other | Fits none of the above | | | |

The crosswalk is a navigation aid. It does not claim the frameworks are equivalent, and a skill is not required to map to any of them. Sources: Behavioural Insights Team, *Test, Learn, Adapt* (2012) and *EAST* (2014); Busara, AUDAS framework (2025); The Agency Fund, four-level evaluation framework (https://eval.playbook.org.ai/).

Why one axis rather than two: the stage is what a program designer thinks in ("I'm at the point where I need to measure this"), and it is the axis the navigator walks. A second controlled axis for "what kind of operation" mostly restates the first and doubles maintenance. Finer cuts are tags.

## Type

`atomic` for a skill that does one behavioral-science operation; `meta` for a skill that operates on the library itself (the creator, the navigator, the evaluator).

## Status

`draft` while in review or when merged without review; `published` once a maintainer has approved it; `deprecated` when retired. Deprecated skills leave the catalog and plugin but stay in history.

## WEIRD status

How far a skill's evidence base has been tested outside Western, Educated, Industrialized, Rich, Democratic samples: `weird-only`, `mixed-evidence`, `likely-generalizes`, `untested-outside-weird`, or `not-applicable` for procedural and meta skills. Required for atomic skills. The skill's "What it draws on" section says what a user elsewhere should check locally.

## Verbs

The list of verbs a skill name may start with. Verb-first names are the atomicity rule applied to the folder name: if the skill cannot be named with one verb, it is more than one skill. Add a verb to the list in the same pull request as the first skill that needs it.

## Input and output types

An optional vocabulary for `metadata.consumes` and `metadata.produces`. Two skills chain when one produces what the other consumes; the site shows the links and the navigator uses them to order steps. Each type says whether a person can supply it directly (`user_suppliable`). Unknown ids are a warning: add the type to the YAML in the same pull request.

Typed input and output are optional because the atomicity rule is "one sentence without *and*", not "one input, one output". Pipeline-shaped skills chain; lens-shaped skills (a cultural-psychology review, a pre-mortem) stay honest by leaving the fields empty.

## Tags

Free-form, comma-separated. `suggested_tags` in the YAML keeps spelling consistent for common frameworks and methods; any tag is allowed.
