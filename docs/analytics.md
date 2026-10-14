# Analytics

Three things are in place:

- page views, counted by Vercel Web Analytics on its free plan
- server-side events in the database: who signs in, reviews, and rates
- a client-side hook for engagement events that does nothing until a provider is plugged in

## Page views: Vercel Web Analytics

`scripts/build_site.py` adds Vercel's script to every page when the site is built on Vercel. It is turned on once in the Vercel dashboard (docs/deployment.md, section 12). It sets no cookies; Vercel tells visitors apart by a hash of the request that it discards after 24 hours.

**Where to look.** Vercel, the `besci-skills` project, Analytics. Leave the environment on Production.

| Question | Panel |
|---|---|
| How many people visit, and is it growing? | Visitors and Page Views at the top; change the period at the top right |
| Which skills get read? | Pages. Every skill is `/skills/<name>/` and every workflow `/workflows/<name>/`; the panel's full view lists every page, not just the top few. |
| Where do readers come from (Slack, GitHub, search, a newsletter)? | Referrers. Visits from links in Slack or email often show as no referrer. |
| Who reads, roughly? | Countries, Devices, Operating Systems, Browsers |
| Which links are broken? | Pages, filtered to paths that don't exist. The 404 page is counted at the address the reader tried. |
| What does one skill's audience look like? | Click its row in Pages; the other panels then show only that page's visitors. |

**What it counts.** One page view per page load. Switching tabs on a skill page, typing in the catalog search, and changing filters don't count, because they change the address with `replaceState`, which Vercel's script ignores. Bots that announce themselves as automated are left out.

**What it doesn't do.** No time on page, scroll depth, tab views, copy clicks, or downloads. Those are custom events, which need the Pro plan (below). No data older than one month: the free plan's reporting window is a month, so note anything you want to keep, for example a monthly screenshot of the Pages panel.

**The monthly allowance.** 50,000 events a month, shared by every project on the same Vercel account. Past it, Vercel stops collecting after a three-day grace period until the next month. Vercel emails when usage gets close; check Usage in the account settings.

**Leaving out your own visits.** Open any page with `?notrack=1` added to the address, for example `https://besci-skills.vercel.app/?notrack=1`. That browser's visits stop counting until you open a page with `?notrack=0`. It is stored in the browser, so do it once per browser and device. Maintainers should do this so their checking doesn't inflate the numbers.

## Server-side: who signs in, reviews, and rates

The site's functions write to Supabase (docs/deployment.md, section 10). This needs no third-party tool, and it is the authoritative record of reviewers.

| Table | One row per |
|---|---|
| `besci_users` | person who has signed in: name, email, domain, org, `can_review`, first and last sign-in, sign-in count |
| `besci_expert_reviews` | expert review filed from the site, with its GitHub issue number |
| `besci_ratings` | rating: skill, version rated, stars, comment, anonymous, hidden |
| `besci_events` | event: `sign_in` (props: `can_review`, `purpose`), `review_denied_domain` (someone outside TAF and IL tried to review), `review_filed`, `rating_saved` (props: `stars`, `anonymous`, `comment`), `rating_hidden`, `rating_shown`, `rating_deleted` |

Queries for the Supabase SQL editor:

```sql
-- Everyone who has signed up as an expert reviewer, most recent first
select name, email, org, first_seen, last_seen, sign_ins
from besci_users where can_review order by last_seen desc;

-- Expert reviews filed per organization per month
select date_trunc('month', r.created_at) as month, u.org, count(*)
from besci_expert_reviews r join besci_users u on u.id = r.user_id
group by 1, 2 order by 1 desc, 2;

-- Skills with the most expert reviews
select skill, count(*) from besci_expert_reviews group by skill order by 2 desc;

-- Ratings per skill: average, count, and how many came from TAF and IL staff
select r.skill, round(avg(r.stars), 2) as average, count(*) as ratings,
       count(*) filter (where u.org in ('TAF', 'IL')) as from_staff
from besci_ratings r join besci_users u on u.id = r.user_id
group by r.skill order by ratings desc;

-- People outside TAF and IL who tried to file an expert review, by email domain
select props->>'domain' as domain, count(*) from besci_events
where name = 'review_denied_domain' group by 1 order by 2 desc;
```

## Client-side events

`site/src/app.js` defines `track(name, props)` (also exposed as `window.besciTrack`). The calls below are already in the code; they do nothing until a provider's adapter sets `window.besciAnalytics` (next section).

| Event | Fired when | Props |
|---|---|---|
| `tab_view` | A reader switches tabs: the file tabs on a skill page (Skill, Test cases, References, Scripts, Assets, Version history, Reviews) or the install tabs | `box` (`skill` or `install`), `tab` |
| `review_panel_open` | The Review this skill panel opens | `skill` |
| `sign_in_start` | The Google button is shown in a panel | `purpose` (`review` or `rate`) |
| `sign_in` | Sign-in succeeded | `purpose`, `can_review` |
| `review_filed` | An expert review was filed | `skill`, `verdict` |
| `rate_panel_open` | The Rate this skill panel opens | `skill` |
| `rating_saved` | A rating was saved | `skill`, `stars`, `comment` (true or false), `anonymous` |

Add a row here whenever you add a `track()` call.

## Adding engagement events later

The free Vercel plan counts page views only. To record the events above, pick one of these and add its adapter to `ANALYTICS_SCRIPT` in `scripts/build_site.py`:

- **Vercel Pro** (about $20 a month plus $0.03 per 1,000 events): custom events appear in the same Analytics page, with 12 months of history. Each event may carry two properties, so trim `props` to the two that matter (for most events, `skill` and one more).
  ```js
  window.besciAnalytics = function (name, props) { window.va("event", { name: name, data: props }); };
  ```
- **PostHog** (free tier): custom events, funnels, and retention. It sets a cookie unless configured with `persistence: "memory"`. It can tie events to the signed-in person if `identify` is called after sign-in; say so in `DISCLOSURE.md` if you do.
- **Plausible** (paid, no cookies): custom events with properties.
- **Supabase**: a small function could store one anonymous summary per page view in `besci_events`. Free, keeps all history, and joins with ratings, at the cost of code to maintain.

Whatever is chosen, update `DISCLOSURE.md` in the same pull request.
