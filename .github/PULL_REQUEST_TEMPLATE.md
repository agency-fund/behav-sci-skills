<!-- Thanks for contributing. Keep what applies, delete the rest. -->

## What this PR adds or changes

<!-- One or two sentences. For a new skill: its name and the one-sentence "what it does". For a change: what moved and why. -->

## Skill checklist (author)

- [ ] `uv run scripts/besci_validate.py skills/<name>` passes locally, or the besci-skill-creator check passed
- [ ] Name is verb-first, kebab-case, and atomic (one thing, no "and")
- [ ] `description` has a "Use when ..." clause and a "Do not use when ..." clause
- [ ] All eight sections are present, in order: What it does, When to use it, Before you start, What it draws on, How to do it, Output template, Where it goes wrong, When to bring in a specialist
- [ ] Any "Not applicable:" section gives a real reason
- [ ] `evals/evals.json` has at least three realistic prompts with expected output shapes
- [ ] `CHANGELOG.md` top entry matches `metadata.version`
- [ ] Evidence is cited, with WEIRD skew and replication status stated
- [ ] I have read `DISCLOSURE.md` and understand that skill content may be processed by third-party AI systems when others use it

## Reviewer checklist (maintainer)

- [ ] Atomic: one thing a behavioral scientist does, no "and"
- [ ] Trigger rule (`description` + "When to use it") is precise and names adjacent intents
- [ ] "Before you start" asks the right questions, or its "Not applicable" reason holds up
- [ ] Evidence is real, cited correctly, with WEIRD skew and replication status
- [ ] Output template is complete enough to judge a run by
- [ ] Failure modes are honest and specific
- [ ] Escalation point is concrete, or its "Not applicable" reason holds up
- [ ] Evals are realistic prompts, at least three
- [ ] At merge: set `metadata.status: published`, fill `metadata.reviewed_by`, confirm the CHANGELOG entry names the reviewer
