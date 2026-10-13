# Deployment and operations

How the site, its server functions, CI, and releases are wired, and the one-time setup steps a maintainer with admin rights must do. Everything here is reversible; nothing touches skill content.

## What runs where

| Thing | Where | Triggered by |
|---|---|---|
| Static site (`site/dist/`) | Vercel | every push to `main` (Vercel's Git integration); preview deploys on pull requests |
| Upload endpoint (`api/submit.py`) | Vercel Python function at `/api/submit` | the website's upload form |
| Sign-in and expert reviews (`api/auth.py`, `api/review.py`, `api/reviews.py`) | Vercel Python functions | the Review this skill panel and the Reviews tab on skill pages |
| Ratings, reviewer sign-ins, server-side analytics events | Supabase (Postgres), reached only by the functions | sign-ins, filed reviews, ratings |
| Database keep-alive (`api/health.py`) | GitHub Actions `keepalive.yml` | every three days, so the free Supabase project isn't paused |
| Structure validation + PR comment | GitHub Actions `ci.yml` | every pull request and push to `main` |
| Inbox unpacking | GitHub Actions `inbox.yml` | pull requests that add files under `inbox/` |
| Navigator catalog snapshot | GitHub Actions `snapshot.yml` | pushes to `main` that change `skills/**` or `taxonomy.yaml` |
| `.skill` downloads | GitHub Releases via `release.yml` | pushing a `v*` tag |

## 1. GitHub repository setup (once)

1. **Create the maintainers team.** In the `agency-fund` org: Settings, Teams, New team, name `besci-maintainers`. Add every person in `MAINTAINERS.md` from both organizations. Give the team **Admin** on this repository. `.github/CODEOWNERS` points at this team; until it exists, review requests are not automatic.
2. **Create labels.** Repository, Issues, Labels: add `skill`, `submitted-via-site`, `skill-proposal`, `bug`, `expert-review`, `review:addressed`, `review:declined`. The upload endpoint and issue templates use these; missing labels are ignored, not fatal. The review endpoint creates the per-review labels itself (`skill:*`, `stage:*`, `verdict:*`, `org:*`).
3. **Branch protection on `main`.** Settings, Branches, Add rule for `main`:
   - Require a pull request before merging, 1 approval.
   - Require status checks to pass: select `validate` (the job in `ci.yml`) once it has run at least once.
   - Do not allow force pushes or deletions.
   - Leave "Require review from Code Owners" off in Phase 1 (the team approval rule already covers it; turn it on in Phase 3).
   - Allow the snapshot bot to push: either tick "Allow specified actors to bypass" for `github-actions`, or accept that the snapshot commit opens a PR instead (change `snapshot.yml` to use `peter-evans/create-pull-request` if you prefer that).
4. **Actions permissions.** Settings, Actions, General: "Read and write permissions" and "Allow GitHub Actions to create and approve pull requests" (needed for the inbox bot to push to PR branches and for sticky comments).

## 2. Vercel project (once)

1. In Vercel, **Add New Project**, import `agency-fund/besci-skills`. Use a Vercel team both orgs can access, or add the IL maintainers as members.
2. Framework preset: **Other**. The repo's `vercel.json` already sets:
   - Install command: `bash scripts/vercel_build.sh install` (runs `uv sync --frozen`; Vercel's build image has a uv-managed Python that rejects plain `pip install`, and the script falls back to `pip --break-system-packages` if uv is ever absent)
   - Build command: `bash scripts/vercel_build.sh build` (runs `uv run --frozen scripts/build_site.py`)
   - Output directory: `site/dist`
   - Python functions: `api/submit.py` (30 s max, 1 GB memory), and `api/auth.py`, `api/review.py`, `api/reviews.py`, `api/health.py`. Files starting with `_` in `api/` are shared code, not routes.
   Vercel detects `api/*.py` and runs them on its Python 3.12 runtime. `requirements.txt` at the root supplies the functions' dependencies (`pyyaml`, `google-auth`, `requests`); `api/requirements.txt` is a fallback some Vercel versions read instead.
3. **Environment variables** (Settings, Environment Variables, apply to Production and Preview):

   | Name | Value | Notes |
   |---|---|---|
   | `CONTRIBUTOR_KEY` | a long random string | Phase 1 gate for the upload form. Generate with `python3 -c "import secrets;print(secrets.token_urlsafe(32))"`. Share with TAF and IL staff over a private channel. |
   | `GITHUB_TOKEN` | fine-grained personal access token | See step 3 below. Mark as **Sensitive**. |
   | `GITHUB_REPO` | `agency-fund/besci-skills` | Repo the endpoint opens PRs on. |
   | `GITHUB_BASE` | `main` | Base branch for PRs. |
   | `SITE_URL` | `https://<your-project>.vercel.app` | The functions refuse writes from any other origin. Also used in PR bodies. Update when you add a custom domain. |
   | `GOOGLE_CLIENT_ID` | `<id>.apps.googleusercontent.com` | The sign-in button's OAuth client (section 9). Not a secret; the build also embeds it in skill pages. |
   | `SESSION_SECRET` | a long random string | Signs the sign-in cookie. Generate like `CONTRIBUTOR_KEY`. Changing it signs everyone out. **Sensitive**. |
   | `SUPABASE_URL` | `https://<project-ref>.supabase.co` | Section 10. |
   | `SUPABASE_SECRET_KEY` | `sb_secret_...` | Section 10. **Sensitive**. Never in the browser, a commit, or chat. |
   | `REVIEW_DOMAINS` | `agency.fund,irrationallabs.com` | Email domains whose staff may file expert reviews. This is the default if unset. |
   | `REVIEWER_EMAILS` | optional, comma-separated | Individual invited reviewers outside those domains. |
   | `ADMIN_EMAILS` | e.g. `michael@agency.fund` | Who may hide or delete rating comments. |

4. Deploy. The first deploy fails if `scripts/build_site.py` is not yet on `main`; it is part of the initial commit.
5. Verify the endpoint: `curl -s https://<project>.vercel.app/api/submit` should return `{"ok": false, "error": "POST a multipart form ..."}` with HTTP 405. A 500 means the function could not import `scripts/besci_validate.py`; check the Function logs. If Vercel pruned the `scripts/` folder from the function bundle, add to `vercel.json`:
   ```json
   "functions": { "api/submit.py": { "maxDuration": 30, "memory": 1024, "includeFiles": "{scripts/**,taxonomy.yaml}" } }
   ```

## 3. The GitHub token for the upload endpoint

The endpoint needs to create branches, commits, and pull requests. Use a **fine-grained personal access token** scoped to this one repository, held by a maintainer account (or a dedicated bot account such as `besci-bot`, which keeps PR authorship clean and survives staff changes; recommended).

1. GitHub, Settings, Developer settings, Personal access tokens, Fine-grained tokens, Generate new token.
2. Resource owner: `agency-fund`. Repository access: Only select repositories, `besci-skills`.
3. Permissions, Repository: **Contents: Read and write**, **Pull requests: Read and write**, **Issues: Read and write** (expert reviews are filed as issues), **Metadata: Read** (added automatically). Nothing else. The account that holds the token must be able to label issues (triage or higher on the repo), or the labels on filed reviews are dropped.
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
/plugin marketplace add agency-fund/besci-skills
/plugin install besci-skills@besci-skills
```

Or in one step on Claude Code 2.1.275 or later:

```
/plugin install besci-skills --marketplace agency-fund/besci-skills
```

For other agents: `npx skills add agency-fund/besci-skills` (reads `.claude-plugin/marketplace.json`). Validate locally before pushing with `claude plugin validate ./`.

## 6. Custom domain (later)

Vercel project, Settings, Domains, add the domain, then add the CNAME or A record it shows at the registrar. Update `SITE_URL` in Vercel, the contact link in `.github/ISSUE_TEMPLATE/config.yml`, the URL in `README.md`, the site URL in `.github/workflows/keepalive.yml`, and the OAuth client's JavaScript origins in Google Cloud (section 9).

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
- `curl -sL https://<site>/api/auth/` returns `{"signed_in": false}`; `curl -sL https://<site>/api/health/` returns `{"ok": true, "db": true}`; `curl -sL https://<site>/api/reviews/` returns `{"ok": true, ...}`.
- On a skill page, click **Review this skill**, sign in with a TAF or IL Google account, and file a short test review. An issue titled `[Expert review] ...` appears with its labels, shows in the skill's Reviews tab within two minutes, and a row appears in `besci_users`. Close the test issue as not planned.
- Sign in with a personal Gmail account: the panel says expert reviews are limited to TAF and IL staff.

Local equivalents: `uv run scripts/besci_validate.py`, `uv run scripts/check_sync.py`, `uv run scripts/package_skills.py`, `uv run python scripts/test_submit.py`, `uv run python scripts/test_feedback.py`.

## 9. Google sign-in (once)

Sign-in only proves who someone is; it asks Google for name and email, nothing else.

1. [Google Cloud console](https://console.cloud.google.com/): create a project (e.g. `besci-skills`).
2. APIs and Services, OAuth consent screen: User type **External** (reviewers come from two different Google Workspace organizations, and raters from anywhere). App name "Behavioral Science Skills", a support email, the site's home page and privacy link (`DISCLOSURE.md`). Scopes: only `openid`, `email`, `profile`; these need no Google verification. Publishing status: **In production**. "Testing" limits sign-in to 100 named test users.
3. Credentials, Create credentials, OAuth client ID, type **Web application**. Authorized JavaScript origins: the site's origin (the value of `SITE_URL`), plus `http://localhost` and `http://localhost:3000` for `vercel dev`. No redirect URIs; the button uses a popup.
4. Copy the client ID into Vercel as `GOOGLE_CLIENT_ID` (Production and Preview) and redeploy, so the build embeds it.

If Google won't accept the `vercel.app` address as an authorized domain (it is a shared public suffix), set up the custom domain first (section 6) and use that. Vercel preview URLs change with every deploy, so sign-in works on production and localhost, not on previews.

## 10. Supabase (once)

The database holds who has signed in, expert-review records, ratings, and server-side analytics events. Only the site's functions use it.

1. Supabase dashboard, the project, SQL Editor, New query: paste `api/schema.sql` and run it. It creates four `besci_` tables with Row Level Security on and no access for the public roles. It is safe to run again.
2. Project Settings, API Keys: create a **secret key** (`sb_secret_...`) named `vercel-besci`. A legacy `service_role` key also works. Put it in Vercel as `SUPABASE_SECRET_KEY` (Sensitive) and the project URL as `SUPABASE_URL`. The publishable (anon) key is not used anywhere.
3. Redeploy, then check `curl -sL https://<site>/api/health/` returns `"db": true`.
4. Free-plan projects pause after about a week without requests. `.github/workflows/keepalive.yml` calls `/api/health` every three days; check its runs if the database ever goes quiet. Moving the project to a paid plan or an organization account removes the concern.

Who has signed up as a reviewer, and other queries, are in `docs/analytics.md`. To delete someone's data on request, delete their rows from `besci_ratings`, `besci_events`, `besci_expert_reviews`, then `besci_users` (the issue they filed stays on GitHub unless a maintainer deletes it).

## 11. Rotating the session secret and keys

- `SESSION_SECRET`: change it in Vercel and redeploy. Everyone is signed out; nothing else is lost.
- `SUPABASE_SECRET_KEY`: create a new secret key in Supabase, update Vercel, redeploy, then delete the old key in Supabase. Do this at once if the key is ever pasted anywhere public.
