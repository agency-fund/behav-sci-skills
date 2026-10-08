# Contributing a skill

Thank you. This library is only useful if a skill written by one person works for someone else, months later, who never talked to them. The spec, the validator, and the review exist to make that true.

**Who can contribute now:** Phase 1 (October to November 2026) is The Agency Fund and Irrational Labs staff. Phase 2 opens to invited experts and organizations; Phase 3 to everyone. See `GOVERNANCE.md`.

**Before anything else,** read `DISCLOSURE.md`. Your skill's text will be processed by third-party AI systems whenever someone uses it. You choose what to include.

## The six steps

### 1. Claim

Check the [catalog](https://behav-sci-skills.vercel.app) and the partnership's tracker so you are not duplicating a skill. Then propose yours at https://behav-sci-skills.vercel.app/propose/, which opens a pre-filled GitHub issue. A maintainer confirms it is atomic: one thing a behavioral scientist does, in one sentence, no "and". If your sentence needs an "and", you have two skills; the second usually takes the first's output as input.

### 2. Draft

Install `besci-skill-creator` (see the README) and say: *"I want to turn [method] into a skill for the library."* It interviews you one question at a time and writes the whole folder: `SKILL.md` with the eight sections, `evals/evals.json`, `CHANGELOG.md`, and any `references/`. In Claude Code it writes the files; in Claude Desktop it gives you the files and a `.skill` zip.

Or draft by hand: copy `template/skill-template/` to `skills/<your-skill-name>/` and follow `docs/skill-spec.md`.

Naming: verb-first kebab-case (`decompose-comb-barriers`, not `comb-barrier-decomposer`), American spelling, starting with a verb from `taxonomy.yaml`.

### 3. Self-test

The creator runs the validator and one pass of your test cases. For a fuller check, run `besci-eval` on the folder: it checks structure, whether the skill fires on the right requests, and whether outputs match your template. Fix what it finds. Its report is worth pasting into your pull request.

By hand, from the repo root:

```
uv sync
uv run scripts/besci_validate.py skills/<your-skill-name>
```

### 4. Submit

Pick the path that fits you. All three end in a pull request.

**A. Hand it to a maintainer.** Send the `.skill` file to any maintainer in `MAINTAINERS.md` on Slack or Drive. They submit it for you; you stay the author in the metadata and on the commit.

**B. Upload on GitHub's website, no git.** Open https://github.com/agency-fund/behav-sci-skills/tree/main/inbox, click **Add file → Upload files**, drop your `.skill` file, choose **Create a new branch for this commit and start a pull request**, and click **Propose changes**, then **Create pull request**. A bot unpacks the zip into `skills/<name>/`, runs the validator, and posts a plain-language checklist on the pull request. Fix anything it flags by uploading again to the same branch.

**C. Upload on the site.** https://behav-sci-skills.vercel.app/upload/ takes the `.skill` file and a contributor key (ask a maintainer) and opens the pull request for you.

**D. Clone and open a pull request.** Fork or branch, add `skills/<name>/`, run the validator, push, open a PR. The template carries the checklist.

### 5. Review

CI posts the validator's report on the pull request. A maintainer then reviews content: atomicity, the trigger rule, the "Before you start" questions, the evidence (real citations, honest WEIRD skew and replication notes), the output template, the failure modes, the escalation point, and whether the evals read like real users. Expect questions; answer in the thread or push changes.

### 6. Merge and tag

The reviewer sets `metadata.status: published`, fills `reviewed_by`, and merges. The catalog, the navigator's snapshot, and the site update automatically. The next release tag attaches a fresh `.skill` zip.

## Revising a skill

Open a pull request that bumps `metadata.version` and adds a `CHANGELOG.md` entry at the top. Patch for wording, minor for new behavior, major when the output template changes shape. Re-run the evals; the changelog entry should say what changed and why.

## Deprecating a skill

Set `metadata.status: deprecated`, add a changelog entry naming the replacement if any, and open a pull request. Authors may deprecate their own skills at any time.

## Changing the taxonomy

New stage, verb, input/output type, or tag: edit `taxonomy.yaml` in the same pull request as the skill that needs it, and say why in the PR.

## Contributing a workflow

Copy `workflows/WORKFLOW-TEMPLATE.md` to `workflows/<name>.md`. A workflow is an ordered set of existing skills with the relationships between them stated and the human decision points marked. `besci-navigator` can draft one for you in guide mode.

## Style

- Write for someone who has never met a behavioral scientist. Define terms on first use.
- Ask before producing. Name the mechanism, not just the tactic.
- Cite what you draw on. Never invent a citation; mark anything unverified.
- Keep `SKILL.md` under 500 lines; move detail into `references/`.
- No `README.md` inside a skill folder.

## Questions

Open an issue, or ask in the partnership's shared channel. Conduct expectations are in `CODE_OF_CONDUCT.md`.
