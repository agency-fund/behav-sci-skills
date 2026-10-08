# Next steps

Ordered. "Owner" follows the MOU's roles: Michael (TAF) leads skill development, Chaning (IL) leads adoption and outreach, both organizations share review. Adjust at the first monthly meeting.

## A. Make the repository live (this week)

1. **Push the initial commit** to `agency-fund/behav-sci-skills` and confirm CI runs green on GitHub. Owner: Michael.
2. **GitHub setup** per `docs/deployment.md` §1: create the `behav-sci-maintainers` team and add admins from both orgs; create labels `skill`, `submitted-via-site`, `skill-proposal`, `bug`; branch protection on `main` (one approval, CI required, no force push); allow Actions to write and open PRs. Owner: Michael, with Chaning added as admin.
3. **Fill `MAINTAINERS.md`** with GitHub handles. Owner: Michael, Chaning.
4. **Vercel project** per `docs/deployment.md` §2–3: import the repo, set `CONTRIBUTOR_KEY`, `GITHUB_TOKEN` (fine-grained PAT on a bot or maintainer account), `GITHUB_REPO`, `GITHUB_BASE`, `SITE_URL`; confirm `/api/submit` answers 405 to GET and the site renders. Give IL access to the Vercel project. Owner: Michael.
5. **Update the site URL** wherever the default `behav-sci-skills.vercel.app` appears if the real URL differs (`.github/ISSUE_TEMPLATE/config.yml`, `CITATION.cff`, `README.md`, `SITE_URL` env). Owner: Michael.
6. **Cut `v0.1.0`**: bump `.claude-plugin/plugin.json` if needed, `git tag v0.1.0 && git push --tags`, confirm the release carries the four `.skill` zips so the site's download links work. Owner: Michael.
7. **Verify installs** on Claude Code (`/plugin marketplace add agency-fund/behav-sci-skills`), on Claude Desktop (zip upload), and with `npx skills add`. Record what each tool does about updates and correct `docs/deployment.md` §5 and the install page where the current wording is uncertain (Codex, Copilot). Owner: Michael, Joe.

## B. Dogfood the process (Oct–Nov 2026, MOU Phase 1)

8. **Run the three submission paths for real** with one TAF scientist and one IL scientist who are not maintainers: maintainer handoff, GitHub web upload into `inbox/`, and the site form. Fix whatever confuses them before anyone else is invited. Owner: Michael (TAF tester), Chaning (IL tester).
9. **Revise the seed skill** `draft-cognitive-interview-script`: it is Claude's draft of Michael's claim. Michael reviews the evidence base and probes, bumps to 0.2.0, and it becomes the first `published` skill. Owner: Michael; reviewer from IL.
10. **Interview-test `besci-skill-creator`** by building two claimed skills from the tracker with their claimants (suggested: `define-key-behavior` with Nikhil, `decompose-comb-barriers` with Nikhil, both IL; or `find-existing-measure` with Patricia, TAF). Note every place the interview asks a bad question or drafts a weak section; fix the skill, bump the version. Owner: Michael with claimants.
11. **Deepen `besci-eval` together.** The author flagged this as needing more thought. Once three or four real skills exist, run the evaluator on them, look at the rubric scores against human judgement, decide what the trigger judge should see (catalog neighbors only, or all installed skills), and decide whether the model-comparison script needs non-Claude providers. Owner: Michael, Chaning; Joe on the script.
12. **Deepen `besci-navigator`** once the catalog has ten or more skills: check route-mode accuracy on realistic requests, check that guide mode's workflow drafts are usable, and draft the first `workflows/<name>.md` from a real guide-mode session. Decide whether the agency-centered variant (Patricia's suggestion) is a second navigator or a mode. Owner: Michael, Patricia.
13. **Taxonomy review** at the first monthly meeting: are the seven stages right, which verbs are missing, which io types are being used. Owner: both.
14. **Port Joe's skills.** Joe picks the first two or three from his prototype to migrate through the normal process (creator interview or hand conversion to the eight sections, evals added, cross-org review). Owner: Joe; reviewer from TAF.
15. **Claim and build toward the tracker.** Update the progress tracker with the new skill names (verb-first) and point claimants at `CONTRIBUTING.md`. Target: enough skills by the end of November that the navigator has something to route to in every stage. Owner: Michael.

## C. Launch readiness (early Dec 2026, MOU Phase 2)

16. **Site design pass** with both brands' input: real logos, a palette, a home page that explains the library to a program officer in thirty seconds. Decide on a custom domain. Owner: Chaning with TAF support.
17. **Install paths verified again** on the then-current Claude Desktop and Claude Code; check whether TAF or IL have Claude for Work so an org admin can push skills to everyone. Owner: Michael.
18. **Outreach material**: blog post, LinkedIn content, a webinar outline, a short tutorial video using the navigator. Owner: Chaning, with Michael.
19. **Quarterly review ritual**: schedule the first one; it re-runs `besci-eval` on every published skill on the current flagship model. Owner: both.

## D. Later (Q1 2027 onward, MOU Phase 3)

20. Expert co-building: invite named academics and applied teams (ideas42, BIT, IDinsight, IPA, J-PAL, Busara, CEGA, UNICEF BIRD Lab) to contribute skills and workflows; design the expert-rating data model and show ratings on the site.
21. Replace the contributor key with GitHub login on the upload form when contribution opens to the public.
22. A Workflow Builder page on the site, once workflows exist and the typed input/output vocabulary has settled.
23. Find My BeSci integration as an on-ramp from the navigator's escalation points to practitioners.
24. Consider an executable workflow form (a skill that orchestrates skills) once hand-written workflows have proven their human decision points.

## Open questions to settle at the first meeting

- Who holds the bot account and token for the upload endpoint, and who rotates the contributor key?
- Does the snapshot bot commit directly to `main` under branch protection, or open a PR? (`docs/deployment.md` §1 explains the choice.)
- What is the review turnaround we promise contributors in Phase 1?
- Which model is the reference model for `besci-eval` reports, and how often do we re-run?
