# Analytics

The site has no analytics provider yet. This page lists what is already instrumented so that choosing one later means writing a small adapter, not finding every click again.

## Client events

`site/src/app.js` defines `track(name, props)` (also exposed as `window.besciTrack`). It does nothing until a provider's adapter sets `window.besciAnalytics`:

```html
<script>
  // Example adapter for PostHog; Plausible or Vercel Web Analytics look the same.
  window.besciAnalytics = function (name, props) { posthog.capture(name, props); };
</script>
```

| Event | Fired when | Props |
|---|---|---|
| `tab_view` | A reader switches tabs: the file tabs on a skill page (Skill, Test cases, References, Scripts, Assets, Version history) or the install tabs | `box` (`skill` or `install`), `tab` |

Add a row here whenever you add a `track()` call.

## Choosing a provider

- Vercel Web Analytics: page views on the Hobby plan; custom events need Pro.
- PostHog: free tier, custom events, and per-person views once sign-in exists.
- Plausible: paid, no cookies, custom events supported.

Whatever is chosen, update `DISCLOSURE.md` in the same pull request.
