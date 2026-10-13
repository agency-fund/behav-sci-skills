---
status: accepted
date: 2026-10-13
---
# Rename the repository, site, and plugin to `besci-skills`

The 2026-10-08 design session (docs/plan/2026-10-08-grill-session.md, question on naming) kept `behav-sci-skills` for the repository, the plugin, and the marketplace, with `besci-` only on the meta-skills. In practice the two spellings sat side by side everywhere: `besci-navigator` installed from `behav-sci-skills`, at `behav-sci-skills.vercel.app`. We now use one name, `besci-skills`, for:

- the GitHub repository, `agency-fund/besci-skills`;
- the Vercel project and its address, `besci-skills.vercel.app`;
- the Claude Code marketplace and plugin, so installs read `/plugin install besci-skills@besci-skills` and skills show as `besci-skills:<skill>`;
- the Python project name, the all-skills bundle (`besci-skills-all.skill`), and the maintainers team (`besci-maintainers`).

The library's display name, "Behavioral Science Skills Library", does not change.

**Consequences.** GitHub redirects the old repository's web, git, and API read URLs, so old links and clones keep working as long as no new repository takes the old name. API writes to the old name get a 307 that the upload endpoint's `urllib` does not follow, so `GITHUB_REPO` in Vercel must change at the same time as the repository. The old `behav-sci-skills.vercel.app` address redirects to the new one; `SITE_URL` and the Google OAuth client's JavaScript origins name the new address. Sign-in cookies and browser storage are per address, so people signed in on the old one sign in once more. Anyone who installed the plugin under the old name removes the `behav-sci-skills` marketplace and adds `agency-fund/besci-skills`.

The grill-session record stays as written; this ADR supersedes its naming decision.
