# Analytics

The site has no analytics provider yet. Two things are in place so that adding one later is a small change:

- server-side events in the database
- a client-side hook that does nothing until a provider is plugged in

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

`site/src/app.js` defines `track(name, props)` (also exposed as `window.besciTrack`). It does nothing until a provider's adapter sets `window.besciAnalytics`:

```html
<script>
  // Example adapter for PostHog; Plausible or Vercel Web Analytics look the same.
  window.besciAnalytics = function (name, props) { posthog.capture(name, props); };
</script>
```

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

## Choosing a provider

- **Vercel Web Analytics**: page views on the Hobby plan. Custom events need Pro.
- **PostHog**: free tier, with custom events. It can tie events to the signed-in person if `identify` is called after sign-in.
- **Plausible**: paid, no cookies, supports custom events.

Whatever is chosen, update `DISCLOSURE.md` in the same pull request.
