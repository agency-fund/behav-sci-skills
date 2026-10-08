# Governance

This document records how the Behavioral Science Skills Library is owned, maintained, and changed. It follows the Memorandum of Understanding between The Agency Fund (TAF) and Irrational Labs (IL) for the period September 2026 to June 2027.

## Ownership

The library is co-owned by The Agency Fund and Irrational Labs, jointly. Neither organization may relicense, rename, or shut down the library without the other's agreement.

The repository lives in TAF's GitHub organization at `agency-fund/behav-sci-skills`. Admin rights are held by named people from each organization, listed in `MAINTAINERS.md`.

Code is licensed under MIT. Skill content and reference material are licensed under CC BY 4.0. See `LICENSE` and `LICENSE-CONTENT.md`.

## Roles

**Admins** hold repository admin rights, manage branch protection, labels, secrets, and the deployment. At least one from each organization.

**Maintainers** review and merge pull requests, triage issues, run the quarterly review of published skills, and keep the meta-skills and tooling working. Listed in `MAINTAINERS.md`.

**Contributors** author skills and workflows. Who may contribute depends on the phase below.

**Authors** are credited in a skill's `metadata.authors` and its changelog. An author may revise or deprecate their own skill at any time via pull request.

## Contribution phases

- **Phase 1 (Oct to Nov 2026):** TAF and IL staff only. Used to test the submission, validation, and review process on ourselves.
- **Phase 2 (Q1 2027):** invited experts and applied organizations, who may contribute single skills, sets of skills, or full workflows, and may attach expert evaluations.
- **Phase 3:** open contribution. Anyone may open a pull request; maintainers review adherence to the spec and catalog fit.

## Review and merge

Every change to `skills/`, `workflows/`, or `taxonomy.yaml` goes through a pull request. Branch protection on `main` requires:

1. The CI check (validator, bundled-copy sync, site build, packaging) to pass.
2. One approving review from a maintainer or admin.

The reviewer is responsible for content as well as structure: atomicity, the trigger rule, the evidence base, the output template, the failure modes, and the escalation point. The pull request template carries the checklist. On merge, the reviewer sets `metadata.status` to `published` and fills `metadata.reviewed_by`.

Who reviews what is decided at the monthly maintainers' meeting. A skill may be merged with `status: draft` when a reviewer is unavailable; the site flags it, and it is picked up at the next meeting.

Cross-organization review (a reviewer from the other organization than the author) is the stated intent of the MOU and remains the norm; it is not enforced by automation.

## Changing the rules

- Changes to the skill specification (`docs/skill-spec.md`) and the validator require agreement from maintainers of both organizations, recorded in the pull request.
- Changes to `taxonomy.yaml` (new stages, verbs, io types) may be made by any maintainer in the same pull request as the skill that needs them.
- Architectural decisions are recorded in `docs/adr/`.

## Deprecation

A skill is deprecated, not deleted. Set `metadata.status: deprecated`, add a changelog entry saying why and what replaces it, and merge. Deprecated skills leave the catalog and the plugin but stay in git history so that projects which cited a version can still find it.

## Meetings and reviews

- **Monthly** maintainers' meeting: triage, review assignments, taxonomy questions.
- **Quarterly** review: every published skill is checked against the current spec and re-run through `besci-eval` on the current flagship model; outdated skills are flagged or updated.

## Adoption and outreach

TAF and IL share responsibility for promoting the library. For v1, IL leads adoption and outreach with TAF support; TAF leads skill development with IL support. Each organization engages its own networks.

## Contact

The maintainers in `MAINTAINERS.md`. For conduct concerns, see `CODE_OF_CONDUCT.md`.
