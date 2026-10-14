# Expert reviews: how they arrive and how to answer them

An expert review is written feedback on one version of a skill from staff at The Agency Fund or Irrational Labs (CONTEXT.md). Reviewers file it from the skill's page; maintainers answer it with a new version or a reply.

## How a review arrives

1. On a skill page, the reviewer clicks **Review this skill** and signs in with their work Google account. Only `agency.fund` and `irrationallabs.com` addresses (and anyone listed in `REVIEWER_EMAILS`) get the form.
2. They pick a verdict, tick the parts the review concerns, and write the review.
3. `api/review.py` opens a GitHub issue with the site's token. The reviewer needs no GitHub account; if they gave a GitHub username, the issue @mentions them.

If the site can't reach GitHub, the panel offers the same review as a prefilled `.github/ISSUE_TEMPLATE/expert-review.yml` form instead.

Every expert review issue looks the same:

- **Title:** `[Expert review] define-key-behavior v0.1.0 by Jane Doe (IL)`
- **Labels:** `expert-review`, `skill:<name>`, `stage:<stage>`, `verdict:<ready|small-changes|needs-revision|not-suitable>`, `org:<TAF|IL>`. Issues filed by hand through the form get only `expert-review`; add the rest when triaging.
- **Body:** `### Skill`, `### Version reviewed`, `### Content reviewed` (a link to SKILL.md at the exact commit the reviewer read), `### Verdict`, `### Parts this concerns`, `### Review`, `### Evidence or sources`, `### Reviewer`, `### Submitted`, and at the end a hidden `<!-- besci-review v1 {...} -->` JSON record of the same fields.

`api/_review_issue.py` defines this format and parses it back; change it there and in the issue form together (`scripts/test_feedback.py` checks they match).

## Answering a review

Each review ends in one of two ways.

**A new version answers it.**

1. Revise the skill (besci-skill-creator helps), bump `metadata.version`.
2. In the new CHANGELOG entry, cite the issue: `Addresses expert review #42 (Jane Doe): added a cost column to the scoring table.`
3. In the pull request description, write `Closes #42`. Merging closes the issue.

The site reads the CHANGELOG at build time. From then on the review shows **Answered in v0.2.0** on the skill's Reviews tab, quoting that changelog sentence, and the Version history tab links `#42`. One entry can answer several reviews; cite each number.

**No change.** Reply on the issue with the reason, add `review:declined`, and close it as "not planned". The skill page shows it as **Closed without changes**.

If a review is fixed in a pull request but the CHANGELOG doesn't cite it, add `review:addressed` when closing; the page shows **Addressed** but can't say which version.

Expert reviews don't change `status` or `reviewed_by`. A maintainer's merge review still does that (GOVERNANCE.md).

## Finding reviews

```bash
gh issue list --label expert-review --state open                       # everything waiting
gh issue list --label expert-review --label skill:define-key-behavior  # one skill
gh issue list --label expert-review --label verdict:needs-revision     # the serious ones
gh issue list --label expert-review --label stage:define               # one stage
```

On GitHub: Issues, filter `label:expert-review is:open`, and sort by the labels in the sidebar.

## Working through reviews with an AI agent

The format is fixed so an agent can do the clerical work. A prompt for Claude Code or a similar agent in this repository:

> Read the open expert reviews of `<skill-name>`: `gh issue list --label expert-review --label skill:<skill-name> --state open --json number,title,body`. Each body ends with a `besci-review v1` JSON record. List each review's points, grouped by the part of the skill it concerns. For each point, say whether you would change the skill and how, quoting the line it affects. Wait for my decisions, one review at a time. Then revise the skill with besci-skill-creator, bump the version, write a CHANGELOG entry that cites every review it answers ("Addresses expert review #N (reviewer): ..."), run the validator, and open a pull request whose description says "Closes #N" for each. For points we decline, draft a reply for each issue instead.

Keep a person on each decision. Reviews are expert judgment, and the agent's job is to organize it, not to settle it.
