# Deployment and operations

How the site, the upload endpoint, CI, and releases are wired, and the one-time setup steps a maintainer with admin rights must do. Everything here is reversible; nothing touches skill content.

## What runs where

| Thing | Where | Triggered by |
|---|---|---|
| Static site (`site/dist/`) | Vercel | every push to `main` (Vercel's Git integration); preview deploys on pull requests |
| Upload endpoint (`api/submit.py`) | Vercel Python function at `/api/submit` | the website's upload form |
| Structure validation + PR comment | GitHub Actions `ci.yml` | every pull request and push to `main` |
| Inbox unpacking | GitHub Actions `inbox.yml` | pull requests that add files under `inbox/` |
| Navigator catalog snapshot | GitHub Actions `snapshot.yml` | pushes to `main` that change `skills/**` or `taxonomy.yaml` |
| `.skill` downloads | GitHub Releases via `release.yml` | pushing a `v*` tag |

## 1. GitHub repository setup (once)

1. **Create the maintainers team.** In the `agency-fund` org: Settings, Teams, New team, name `behav-sci-maintainers`. Add every person in `MAINTAINERS.md` from both organizations. Give the team **Admin** on this repository. `.github/CODEOWNERS` points at this team; until it exists, review requests are not automatic.
2. **Create labels.** Repository, Issues, Labels: add `skill`, `submitted-via-site`, `skill-proposal`, `bug`. The upload endpoint and issue templates use these; missing labels are ignored, not fatal.
3. **Branch protection on `main`.** Settings, Branches, Add rule for `main`:
   - Require a pull request before merging, 1 approval.
   - Require status checks to pass: select `validate` (the job in `ci.yml`) once it has run at least once.
   - Do not allow force pushes or deletions.
   - Leave "Require review from Code Owners" off in Phase 1 (the team approval rule already covers it; turn it on in Phase 3).
   - Allow the snapshot bot to push: either tick "Allow specified actors to bypass" for `github-actions`, or accept that the snapshot commit opens a PR instead (change `snapshot.yml` to use `peter-evans/create-pull-request` if you prefer that).
4. **Actions permissions.** Settings, Actions, General: "Read and write permissions" and "Allow GitHub Actions to create and approve pull requests" (needed for the inbox bot to push to PR branches and for sticky comments).

## 2. Vercel project (once)

1. In Vercel, **Add New Project**, import `agency-fund/behav-sci-skills`. Use a Vercel team both orgs can access, or add the IL maintainers as members.
2. Framework preset: **Other**. The repo's `vercel.json` already sets:
   - Install command: `python3 -m pip install -r requirements.txt`
   - Build command: `python3 scripts/build_site.py`
   - Output directory: `site/dist`
   - Python function: `api/submit.py`, 30 s max, 1 GB memory
   Vercel detects `api/*.py` and runs it on its Python 3.12 runtime. `requirements.txt` at the root supplies the function's dependencies (`pyyaml`); `api/requirements.txt` is a fallback some Vercel versions read instead.
3. **Environment variables** (Settings, Environment Variables, apply to Production and Preview):

   | Name | Value | Notes |
   |---|---|---|
   | `CONTRIBUTOR_KEY` | a long random string | Phase 1 gate for the upload form. Generate with `python3 -c "import secrets;print(secrets.token_urlsafe(32))"`. Share with TAF and IL staff over a private channel. |
   | `GITHUB_TOKEN` | fine-grained personal access token | See step 3 below. Mark as **Sensitive**. |
   | `GITHUB_REPO` | `agency-fund/behav-sci-skills` | Repo the endpoint opens PRs on. |
   | `GITHUB_BASE` | `main` | Base branch for PRs. |
   | `SITE_URL` | `https://<your-project>.vercel.app` | Used for the CORS preflight and the link in PR bodies. Update when you add a custom domain. |

4. Deploy. The first deploy fails if `scripts/build_site.py` is not yet on `main`; it is part of the initial commit.
5. Verify the endpoint: `curl -s https://<project>.vercel.app/api/submit` should return `{"ok": false, "error": "POST a multipart form ..."}` with HTTP 405. A 500 means the function could not import `scripts/besci_validate.py`; check the Function logs. If Vercel pruned the `scripts/` folder from the function bundle, add to `vercel.json`:
   ```json
   "functions": { "api/submit.py": { "maxDuration": 30, "memory": 1024, "includeFiles": "{scripts/**,taxonomy.yaml}" } }
   ```

## 3. The GitHub token for the upload endpoint

The endpoint needs to create branches, commits, and pull requests. Use a **fine-grained personal access token** scoped to this one repository, held by a maintainer account (or a dedicated bot account such as `besci-bot`, which keeps PR authorship clean and survives staff changes; recommended).

1. GitHub, Settings, Developer settings, Personal access tokens, Fine-grained tokens, Generate new token.
2. Resource owner: `agency-fund`. Repository access: Only select repositories, `behav-sci-skills`.
3. Permissions, Repository: **Contents: Read and write**, **Pull requests: Read and write**, **Metadata: Read** (added automatically). Nothing else.
4. Expiration: 1 year. Put the expiry date in the maintainers' calendar.
5. Copy the token into Vercel as `GITHUB_TOKEN`. Never commit it.

If the org requires approval for fine-grained tokens, an org owner approves it under Settings, Personal access tokens.

**Later option:** a GitHub App installed on the repo, with the function minting installation tokens from the app's private key. Same permissions, no expiry to track, PRs show as "besci-bot[bot]". Worth doing in Phase 3 when outside contributors arrive.

## 4. Cutting a release

Releases produce the `.skill` downloads for Claude Desktop users and pin a plugin version for Claude Code.

```bash
# bump the version in .claude-plugin/plugin.json, commit to main, then:
git tag v0.1.0
git push origin v0.1.0
```

`release.yml` validates every skill, packages them, and creates a GitHub Release with `dist/*.skill` and `dist/manifest.json` attached, plus auto-generated notes. The site's install page links to the latest release's assets.

Use patch tags (`v0.1.1`) for skill fixes, minor tags (`v0.2.0`) when skills are added, major when the spec changes.

## 5. Installing from the marketplace (what to put in docs)

```
/plugin marketplace add agency-fund/behav-sci-skills
/plugin install behav-sci-skills@behav-sci-skills
```

Or in one step on Claude Code 2.1.275 or later:

```
/plugin install behav-sci-skills --marketplace agency-fund/behav-sci-skills
```

For other agents: `npx skills add agency-fund/behav-sci-skills` (reads `.claude-plugin/marketplace.json`). Validate locally before pushing with `claude plugin validate ./`.

## 6. Custom domain (later)

Vercel project, Settings, Domains, add the domain, then add the CNAME or A record it shows at the registrar. Update `SITE_URL` in Vercel, the contact link in `.github/ISSUE_TEMPLATE/config.yml`, and the URL in `README.md`.

## 7. Rotating the contributor key

1. Generate a new value and update `CONTRIBUTOR_KEY` in Vercel (Production and Preview).
2. Redeploy (Deployments, Redeploy on the latest) so the function picks it up.
3. Send the new key to staff; the old one stops working immediately.

Rotate when someone leaves either organization or the key is posted anywhere public.

## 8. Checking that everything works

- Open a test pull request that edits a comment in the seed skill: the `validate` check runs and a "Skill structure check" comment appears.
- Upload the seed skill's `.skill` (from `uv run scripts/package_skills.py`, in `dist/`) into `inbox/` through the GitHub web UI on a new branch: the inbox bot should fail with "A folder named ... already exists", which proves the path works; then try with a renamed copy.
- Submit the same archive through the website form with the contributor key: a `submit/<name>-<timestamp>` branch and PR appear with the `submitted-via-site` label.
- Push a tag `v0.0.1-test`, confirm a Release appears with assets, then delete the tag and release.

Local equivalents: `uv run scripts/besci_validate.py`, `uv run scripts/check_sync.py`, `uv run scripts/package_skills.py`, `uv run python scripts/test_submit.py`.
