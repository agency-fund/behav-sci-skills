# Design session record, 2026-10-08

A structured interview between Zezhen (Michael) Wu, The Agency Fund, and Claude, run with the grill-me discipline: one question at a time, a recommended answer each time, every branch of the design resolved before building. Source material: the TAF–IL Memorandum of Understanding (with its comment threads), the skill template doc, the progress tracker, Joe Speed's prototype repository, Matt Pocock's and Anthropic's skills repositories, the Agent Skills specification, and the `npx skills` CLI documentation.

Each entry: the question, the options considered, the decision, and why. Decisions marked ADR are recorded in `docs/adr/`.

## 1. Relationship to Joe Speed's prototype (ADR 0001)

Options: fork or transfer the prototype and restructure in place; build fresh and port its ideas; build fresh and treat it as unrelated.
**Decision:** build from scratch; the prototype is Joe's own project; port his individual skills later, one at a time.
**Why:** the structure and skill format needed to be defined from first principles for this partnership. The prototype's frontmatter sits outside the Agent Skills spec and it lacked evals, dual licensing, plugin packaging, meta-skills, and MOU governance material.

## 2. Repository and plugin name

Options: keep `behav-sci-skills`; rename to `besci-skills`; rename to the MOU's `behavioral-science-skills`.
**Decision:** keep `behav-sci-skills` for the repo, the plugin, and the marketplace. The `besci-` prefix stays on the meta-skills only.
**Why:** it already exists and is descriptive; one name, no aliases.

## 3. Scope of this build pass

Options: structure, rules, validator, meta-skills only; the same plus a working site scaffold; the same plus full branding and a workflow builder.
**Decision:** structure, rules, validator, three meta-skills at v1, and a working site generated from the skills, deployed, with simple visuals.
**Why:** the site proves the pipeline end to end and is what non-technical users touch. Branding and the workflow builder wait for a bigger catalog.

## 4. Directory layout (ADR 0005)

Options: flat `skills/<name>/`; by category `skills/<category>/<name>/`; by type (`skills/`, `meta/`, `workflows/`).
**Decision:** flat, with `type: meta` in metadata for meta-skills; a separate `workflows/` directory.
**Why:** the taxonomy will move; a flat layout makes reclassification a metadata edit rather than a move that breaks links.

## 5. Where machine-readable facets live (ADR 0002)

Options: flat `metadata` strings in frontmatter; a sidecar YAML; nested custom top-level keys.
**Decision:** flat `metadata` strings; structured prose in mandated body sections.
**Why:** spec compliance, one file per skill, nothing to drift.

## 6. Typed inputs and outputs for chaining

Options: required controlled vocabulary (Joe's model); optional `consumes`/`produces` with warnings; none.
**Decision:** optional, from a vocabulary in `taxonomy.yaml`; unknown ids warn, not fail.
**Why:** the atomicity rule is "one sentence without *and*", not "one input, one output"; many claimed skills are lens-shaped. Pipeline-shaped skills still chain and the navigator can use the edges.

## 7. Mandated body sections

Options: seven sections all required; two optional for meta-skills; fewer sections folded together.
**Decision (revised in discussion):** eight sections in fixed order: What it does; When to use it; Before you start; What it draws on; How to do it; Output template; Where it goes wrong; When to bring in a specialist. "Before you start" and "When to bring in a specialist" may read "Not applicable: <reason>", and the reason is mandatory and non-trivial.
**Why:** the author's points: some skills just run and need no questions; some narrow technical skills have no escalation point; but authors should justify the omission rather than leave it blank. The heading is always present so the validator and the evaluator have a uniform shape.

## 7b. Where the trigger rule lives

Options: description only; description plus a "When to use it" body section; body only.
**Decision:** both. The `description` is the compressed rule that actually fires the skill (it is the only thing a model sees before loading). The body section holds the full list of should-fire and should-not-fire phrasings, which doubles as the evaluator's trigger test set.
**Why:** the description is capped at 1024 characters; the full rule is longer and serves humans and evaluation.

## 8. Test cases

Options: per-skill `evals/evals.json` in Anthropic's skill-creator schema; our own YAML; cases inside SKILL.md.
**Decision:** `evals/evals.json`, at least three cases, Anthropic's schema.
**Why:** cases in the body waste context and show the model the answers; Anthropic's format works with their tooling and is familiar.

## 9. Version history

Options: `metadata.version` plus per-skill `CHANGELOG.md`; derive from git log; one repo-wide changelog.
**Decision:** semver in metadata plus a per-skill changelog whose top entry must match.
**Why:** zip users have no git history; squash merges lose detail; a hand-written line is what a reviewer and a citing researcher need.

## 10. Skill naming

Options: verb-first imperative; noun-phrase agent names; free.
**Decision:** verb-first kebab-case from a verb allowlist in the taxonomy; meta-skills keep `besci-` names. American spelling.
**Why:** the atomicity test applied to the folder name; reads as a command and in navigator recommendations.

## 11. Taxonomy

Options: one controlled axis (`stage`) plus free tags with a crosswalk to TEST, AUDAS, and TAF's four-level framework; two controlled axes; tags only.
**Decision:** one axis, seven stages strongly recommended rather than dictated (define, diagnose, design, measure, test, analyze, implement) plus `other`, accepted with a validator warning.
**Why:** the author's point: verb-based skills may not fall neatly into the seven; the warning lets maintainers see the gaps and extend the list.

## 12. Workflows

Options: reserve `workflows/` with a template now and ship none; reserve nothing; make workflows orchestrating skills.
**Decision:** reserve the directory and template; ship none; drop the separate "stack" concept. Any recommended set of skills, even lightly ordered, is a workflow.
**Why:** the author's point: even a bundle of favorite skills has an order or stated lack of one, so one concept suffices. An executable form can come later once hand-written workflows exist.

## 13. Navigator: one skill or two

Options: one `besci-navigator` with route and guide modes; two skills, a quiet router and an interviewer.
**Decision:** one skill, two modes, chosen from the request and overridable by the user; must not fire when the user names a method or skill.
**Why:** in Claude Desktop nobody types slash commands, so Matt Pocock's user-invoked/model-invoked split does not map; one install, one mental model, one catalog snapshot. Split later if evals show interference.

## 14. Distribution

Options: one plugin with everything, CI-built `.skill` zips on releases; two plugins (meta and all); committed zips.
**Decision:** one plugin; zips built by CI on tags and attached to GitHub Releases; nothing committed.
**Why:** fifty skills' descriptions are well within budget; committed zips go stale.

## 15. Website stack

Options: framework-free static site from a Python build script; Astro; a docs framework.
**Decision:** framework-free; one builder script, pre-rendered pages, small client-side search and filter.
**Why:** a catalog, not an app; maintainers are scientists; pre-rendered pages give link previews for outreach.

## 16. Contribution paths

**Decision:** three paths, all ending in a pull request: hand the `.skill` to a maintainer; upload via GitHub's web UI into `inbox/` with a bot that unpacks and validates; clone and PR. Plus a site form.
**Why:** the author's concern: scientists who are not comfortable with GitHub need a smooth path, and the author wants to be the content reviewer on every submission.

## 17. Submission backend (ADR 0004; ADR 0003)

Options: Vercel for site plus a Python function; GitHub Pages plus a Cloudflare Worker; no server.
**Decision:** Vercel hosts both. The same Python validator runs locally, in CI, and in the function. Phase 1 gate is a shared contributor key.
**Why:** the author wanted the upload form now, not in Phase 3, so internal scientists can test the experience; one deploy, one validator.

## 18. Review enforcement

Options: automated cross-org check; branch protection with one approval and CODEOWNERS; none.
**Decision (author's choice):** admins from both organizations; branch protection with one approval and green CI; the monthly meeting decides who reviews what; no cross-org automation. Statuses `draft`, `published`, `deprecated`.
**Why:** the author judged the automated cross-org check unnecessary for Phase 1.

## 19. besci-skill-creator scope

**Decision:** interview, draft the whole folder, run the validator, one in-conversation self-test pass over the evals with one revision offer, package, explain submission paths, hand off to besci-eval for more.
**Why:** self-testing is where skills stall; one pass while intent is fresh catches the obvious misses.

## 20. besci-eval scope

**Decision:** three checks (structure, triggering with precision and recall, output quality graded by a rubric derived from the skill's own sections), in-conversation on Desktop and via an API script across models in Claude Code. Expert ratings deferred.
**Note from the author:** v1 is a starting point; the partnership will think more deeply together about what belongs in the evaluator.

## 21. Navigator's catalog knowledge

**Decision:** a CI step regenerates `references/catalog.md` inside the navigator on every merge and commits it; the navigator notes the snapshot date and offers a live fetch when stale.
**Author's follow-up:** recommend plugin install with auto-update for Claude Code and similar tools; zip users must re-download. Agreed; mitigations recorded (version stamps, snapshot-age nudge, What's new page and feed, Claude for Work org upload).

## 22. Seed skills

**Decision:** the three meta-skills, the template, and one real atomic skill from the author's own tracker claim (`draft-cognitive-interview-script`), status draft, as the reference everyone copies.
**Why:** a catalog with zero atomic skills cannot be navigated or evaluated; drafting other people's claims would pre-empt their interviews.

## 23. Site branding

**Decision:** neutral, co-branded with both logos and links; iterate on design later.

## Assumptions stated and accepted

Code under MIT, content under CC BY 4.0; `DISCLOSURE.md` for users and contributors linked from README, install page, contributing guide, and PR checkbox; a "Cite this skill" block on each skill page with a SIFA pointer; the eval script targets the Claude API only in v1; CI runs the validator, evals run on demand; the author creates the GitHub team, labels, token, and Vercel environment; the seed skill is Claude's draft of the author's claim, for the author to revise.
