---
status: accepted
date: 2026-10-13
---
# Google sign-in, expert reviews filed as GitHub issues, and ratings in Supabase

ADR 0004 gave the site one server function, the upload form. This adds feedback on each skill page.

- An **expert review**, from staff at The Agency Fund and Irrational Labs. The reviewer signs in with Google and writes the review in a side panel. `api/review.py` files it as a GitHub issue with the server's token, under a fixed title (`[Expert review] <skill> v<version> by <name> (<org>)`) and labels (`expert-review`, `skill:*`, `stage:*`, `verdict:*`, `org:*`), so maintainers and their AI tools can sort and work through reviews.
- A **rating**: 1 to 5 stars and an optional public comment from anyone with a Google account.

**Reviewers don't need GitHub accounts.** Most TAF and IL scientists don't have one, and asking them to make one before they can comment would lose most reviews. The issue body names the reviewer and organization (never the email address), and an optional GitHub username @mentions them so they get replies. If the server can't reach GitHub, the panel falls back to a prefilled `expert-review.yml` issue form.

**Google sign-in.** It is the account both organizations already have. The server checks the ID token with `google-auth` and decides per request who may review: email domain `agency.fund` or `irrationallabs.com`, plus an `REVIEWER_EMAILS` list for invited experts. The browser then holds an HMAC-signed, HttpOnly session cookie for 30 days. No passwords, and no Google data beyond name and email.

**Supabase.** Ratings, the reviewer sign-in log, and server-side analytics events need a database; the static site can't store anything. Supabase (Postgres) is used only as a database. The site's functions reach it over its REST API with a secret key held in Vercel. Every table has Row Level Security on and no policies, so the public key can do nothing, and the browser never talks to Supabase. The project starts on a maintainer's free plan, which pauses after about a week without requests; `.github/workflows/keepalive.yml` pings `/api/health` every three days.

**Answered reviews.** When a new version answers a review, its CHANGELOG entry cites the issue (`Addresses expert review #42`). The site reads those references at build time and marks the review "Answered in v0.2.0", so readers see how the skill responded to criticism.

Expert reviews do not change a skill's `status` or `reviewed_by`. Those still come only from a maintainer's pull-request review (GOVERNANCE.md).

**Rejected alternatives:**

- Prefilled GitHub issue forms only: every reviewer would need a GitHub account.
- Giscus or utterances comments: also need GitHub accounts, and have no star ratings.
- Ratings committed to the repository as JSON: every rating would become a commit and a redeploy.
- Supabase Auth in the browser: adds supabase-js and a second sign-in system next to the one the review function needs anyway.
- A Google Form per skill: no public average, no link back to versions, and answers scattered across 74 forms.
