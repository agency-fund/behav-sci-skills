# Citing skills and workflows

Every skill is a fixed, versioned artifact, so a project can record exactly which skills it used, the way analysis code is registered on OSF. Doing so is how users keep the human role visible and how authors get credit.

## Cite a skill

Name the skill, its version, its authors, and the library. Each skill's page on the site has a ready-made "Cite this skill" block.

APA style:

> Wu, Z. (2026). *Cognitive interview script drafter* (Version 0.1.0) [AI skill]. Behavioral Science Skills Library, The Agency Fund and Irrational Labs. https://github.com/agency-fund/behav-sci-skills/tree/main/skills/draft-cognitive-interview-script

In a methods section:

> Interview scripts were drafted with the `draft-cognitive-interview-script` skill (v0.1.0, Behavioral Science Skills Library) in Claude and revised by the research team.

To cite the exact version, link to the git tag or commit rather than `main`: `https://github.com/agency-fund/behav-sci-skills/tree/v0.1.0/skills/<name>`.

## Cite a workflow

> Author(s) (Year). *Workflow title* (Version x.y.z) [AI skill workflow]. Behavioral Science Skills Library. URL

List the skills the workflow ran, with versions, in a supplement.

## Cite the library

See `CITATION.cff` at the repository root; GitHub renders it as a "Cite this repository" button.

## Documenting how humans and AI contributed

The partnership encourages users to follow Busara's SIFA framework, the Statement of Intellectual Fellowship and Accountability, which documents how humans and AI tools each contributed to a piece of work: https://busara.global/our-works/the-sifa-tool-for-a-statement-of-intellectual-fellowship-and-accountability/

A minimal statement:

> *AI contribution.* The following skills from the Behavioral Science Skills Library were used: [list with versions]. The AI produced [drafts / analyses / code]. Human authors [reviewed, revised, decided X]. Responsibility for the final work rests with the human authors.

## Open-science record

For a pre-registration or an OSF project, record:

- Skill names and versions (or the git tag).
- Which model and product you ran them in, and when.
- Any deviations from the skill's procedure.
- The `expected_output` shape from the skill's evals if you used it as a quality check.
