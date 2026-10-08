---
status: accepted
date: 2026-10-08
---
# Vercel hosts the static site and the upload-to-pull-request function

The site was first planned for GitHub Pages. The decision to let non-technical contributors upload a `.skill` file on the website and have a pull request opened for them requires a server-side function holding a GitHub token, which GitHub Pages cannot run.

Vercel hosts both: the static site built from `site/src/` and `skills/` into `site/dist/`, and `api/submit.py`, a Python function that checks a contributor key, runs the shared validator, and opens the pull request through GitHub's REST API. One repository, one deploy, one place for secrets. Alternatives were GitHub Pages plus a Cloudflare Worker (two deploy targets and accounts) or an issue-attachment flow with no server (barely easier than GitHub's own upload UI). The Vercel project is owned by one organization's account; admin access for the other organization is a manual step recorded in `docs/deployment.md`. The GitHub web-upload path into `inbox/` and the maintainer-handoff path remain as fallbacks that need no server.
