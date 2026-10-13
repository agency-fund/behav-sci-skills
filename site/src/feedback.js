/* Behavioral Science Skills: expert reviews and ratings on skill pages. No dependencies.
   - One side panel, two modes. "Review this skill": Google sign-in (Google's
     script loads only when needed), then a form that /api/review files as a
     GitHub issue; reviewers need no GitHub account. "Rate this skill": the same
     sign-in for anyone, then stars, an optional comment, and name or anonymous.
   - The Reviews tab: expert reviews from /api/reviews, each marked with the
     version that answered it (from the CHANGELOG, in #skill-data), and ratings
     and comments from /api/ratings, with hide and delete for maintainers.
   Server side: api/auth.py, api/review.py, api/reviews.py, api/ratings.py.
   Without the API (a local build, or an outage) the page keeps its plain links. */
(function () {
  "use strict";

  var dataEl = document.getElementById("skill-data");
  if (!dataEl) return;
  var skill;
  try { skill = JSON.parse(dataEl.textContent); } catch (e) { return; }

  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };
  var track = window.besciTrack || function () {};
  var GITHUB = "https://github.com/" + skill.repo;

  // Keep in step with VERDICTS and PARTS in api/_review_issue.py (scripts/test_feedback.py checks).
  var VERDICTS = [
    ["ready", "Ready to publish"],
    ["small-changes", "Publish after small changes"],
    ["needs-revision", "Needs substantial revision"],
    ["not-suitable", "Not suitable for the library"]
  ];
  var PARTS = ["What it does", "When to use it", "Before you start", "What it draws on",
    "How to do it", "Output template", "Where it goes wrong", "When to bring in a specialist",
    "Test cases", "References", "Scripts", "Whole skill"];
  var MIN_REVIEW = 20, MAX_REVIEW = 20000;

  /* ---------- helpers ---------- */
  function h(tag, attrs, kids) {
    var el = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) {
      var v = attrs[k];
      if (v === null || v === undefined || v === false) return;
      if (k === "text") el.textContent = v;
      else if (k === "class") el.className = v;
      else if (k.slice(0, 2) === "on") el.addEventListener(k.slice(2), v);
      else el.setAttribute(k, v === true ? "" : v);
    });
    (kids || []).forEach(function (c) {
      if (c === null || c === undefined || c === false) return;
      el.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
    });
    return el;
  }
  function icon(name) {
    var ns = "http://www.w3.org/2000/svg";
    var svg = document.createElementNS(ns, "svg");
    svg.setAttribute("viewBox", "0 0 256 256");
    svg.setAttribute("fill", "currentColor");
    svg.setAttribute("aria-hidden", "true");
    var use = document.createElementNS(ns, "use");
    use.setAttribute("href", "#i-" + name);
    svg.appendChild(use);
    return svg;
  }
  function store(key, value) {
    try { if (value === null) localStorage.removeItem(key); else localStorage.setItem(key, JSON.stringify(value)); } catch (e) { /* ignore */ }
  }
  function recall(key) {
    try { return JSON.parse(localStorage.getItem(key) || "null"); } catch (e) { return null; }
  }
  function formatDate(iso) {
    var d = new Date(iso);
    if (isNaN(d)) return "";
    return d.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" });
  }
  // Paths end in "/": the site adds trailing slashes (vercel.json), so "/api/auth/" would cost a redirect.
  function api(method, path, body) {
    var opts = { method: method, credentials: "same-origin", headers: {} };
    if (body !== undefined) { opts.headers["Content-Type"] = "application/json"; opts.body = JSON.stringify(body); }
    return fetch(path, opts).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (j) { j._status = r.status; return j; });
    }, function () { return { _status: 0 }; });
  }
  function githubUrl(params) {
    var q = Object.keys(params).map(function (k) { return encodeURIComponent(k) + "=" + encodeURIComponent(params[k]); }).join("&");
    return GITHUB + "/issues/new?" + q;
  }
  function bugReportUrl() {
    return githubUrl({ template: "bug.yml", title: "Problem with " + skill.name + ": ", skill: skill.name, version: skill.version });
  }
  function contentUrl() {
    return skill.commit ? GITHUB + "/blob/" + skill.commit + "/skills/" + skill.name + "/SKILL.md" : "";
  }

  /* ---------- who is signed in ---------- */
  // The session cookie is HttpOnly, so this flag is how a page knows to ask who is
  // signed in (to show maintainers their moderation controls) without asking every time.
  var SIGNED_IN = "besci:signed-in";
  var user = null; // null until asked; then the /api/auth view, or {signed_in:false, unavailable:true}
  function setUser(u) {
    user = u;
    store(SIGNED_IN, u && u.signed_in ? true : null);
    return u;
  }
  function loadUser() {
    return api("GET", "/api/auth/").then(function (u) {
      return setUser(u._status === 200 ? u : { signed_in: false, unavailable: true });
    });
  }
  function signOut() {
    var wasAdmin = user && user.is_admin;
    api("DELETE", "/api/auth/").then(function () {
      setUser({ signed_in: false });
      try { window.google.accounts.id.disableAutoSelect(); } catch (e) { /* ignore */ }
      if (wasAdmin) loadRatings(true);
      showMode();
    });
  }

  /* Google Identity Services: loaded on first use, initialized once. */
  var gisPromise = null, gisInitialized = false, afterSignIn = null, signInPurpose = "";
  function loadGoogle() {
    if (gisPromise) return gisPromise;
    gisPromise = new Promise(function (resolve, reject) {
      var s = document.createElement("script");
      s.src = "https://accounts.google.com/gsi/client";
      s.async = true;
      s.onload = function () {
        if (window.google && window.google.accounts && window.google.accounts.id) resolve(window.google.accounts.id);
        else reject(new Error("unavailable"));
      };
      s.onerror = function () { gisPromise = null; reject(new Error("blocked")); };
      document.head.appendChild(s);
    });
    return gisPromise;
  }
  function onCredential(resp) {
    api("POST", "/api/auth/", { credential: resp.credential, purpose: signInPurpose }).then(function (u) {
      if (u._status === 200 && u.signed_in) {
        setUser(u);
        track("sign_in", { purpose: signInPurpose, can_review: !!u.can_review });
        if (u.is_admin) loadRatings(true);
        if (afterSignIn) afterSignIn();
      } else {
        showMessage(u.error || "Sign-in didn't work. Please try again.");
      }
    });
  }
  function googleButton(purpose, then) {
    var box = h("div", { class: "fb-google" }, [h("p", { class: "muted", text: "Loading Google sign-in…" })]);
    signInPurpose = purpose;
    afterSignIn = then;
    loadGoogle().then(function (gid) {
      if (!gisInitialized) {
        gid.initialize({ client_id: skill.google_client_id, callback: onCredential, ux_mode: "popup", auto_select: false });
        gisInitialized = true;
      }
      box.textContent = "";
      var dark = document.documentElement.getAttribute("data-theme") === "dark";
      gid.renderButton(box, { type: "standard", theme: dark ? "filled_black" : "outline", size: "large", text: "signin_with", shape: "pill", width: 260 });
      track("sign_in_start", { purpose: purpose });
    }, function () {
      box.textContent = "";
      box.appendChild(h("p", { class: "fb-error", text: "Google sign-in didn't load. An ad or privacy blocker may be stopping accounts.google.com; allow it on this site and try again." }));
    });
    return box;
  }

  /* ---------- the side panel ---------- */
  var panel, panelTitle, panelBody, opener, mode = "review";
  function ensurePanel() {
    if (panel) return;
    panelTitle = h("h2", { id: "fb-title", class: "fb-title", tabindex: "-1" });
    panelBody = h("div", { class: "fb-body", "aria-live": "polite" });
    var close = h("button", { type: "button", class: "icon-btn fb-close", "aria-label": "Close", onclick: closePanel }, [icon("x")]);
    panel = h("aside", { class: "fb-panel", id: "fb-panel", role: "dialog", "aria-labelledby": "fb-title", hidden: true },
      [h("div", { class: "fb-head" }, [panelTitle, close]), panelBody]);
    document.body.appendChild(panel);
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !panel.hidden) closePanel(); });
  }
  function openPanel(which, btn) {
    ensurePanel();
    opener = btn || null;
    mode = which === "rate" ? "rate" : "review";
    panel.hidden = false;
    $$("[data-panel-open]").forEach(function (b) { b.setAttribute("aria-expanded", String(b.getAttribute("data-panel-open") === mode)); });
    showMode();
    track(mode + "_panel_open", { skill: skill.name });
    panelTitle.focus();
  }
  function showMode() { if (mode === "rate") showRate(); else showReview(); }
  function closePanel() {
    panel.hidden = true;
    $$("[data-panel-open]").forEach(function (b) { b.setAttribute("aria-expanded", "false"); });
    if (location.hash === "#review" || location.hash === "#rate") history.replaceState(null, "", location.pathname + location.search);
    if (opener) opener.focus();
  }
  function setBody(nodes) {
    panelBody.textContent = "";
    nodes.forEach(function (n) { if (n) panelBody.appendChild(n); });
  }
  function clearMessage() {
    var old = $(".fb-error", panelBody);
    if (old) old.remove();
  }
  function showMessage(text) {
    clearMessage();
    panelBody.insertBefore(h("p", { class: "fb-error", role: "alert", text: text }), panelBody.firstChild);
  }

  /* ---------- review: which screen to show ---------- */
  function showReview() {
    panelTitle.textContent = "Review this skill";
    if (!skill.google_client_id) return renderUnavailable();
    setBody([h("p", { class: "muted", text: "Checking whether you're signed in…" })]);
    (user ? Promise.resolve(user) : loadUser()).then(function (u) {
      if (u.unavailable) return renderUnavailable();
      if (!u.signed_in) return renderSignIn();
      if (!u.can_review) return renderNotEligible();
      renderForm();
    });
  }

  function target() {
    return h("p", { class: "fb-target" }, ["You're reviewing ", h("code", { text: skill.name }), " version " + skill.version + "."]);
  }

  function renderUnavailable() {
    setBody([
      target(),
      h("p", { text: "Signing in isn't available on this copy of the site, so reviews can't be filed from here." }),
      h("p", {}, ["If you're on the staff of The Agency Fund or Irrational Labs and have a GitHub account, ",
        h("a", { href: githubUrl({ template: "expert-review.yml", title: "[Expert review] " + skill.name + " v" + skill.version + " by ", skill: skill.name, version: skill.version, content: contentUrl() }), rel: "noopener", target: "_blank", text: "post your review on GitHub" }),
        " instead."]),
      h("p", {}, [h("a", { href: bugReportUrl(), rel: "noopener", target: "_blank", text: "Report a problem with this skill" })])
    ]);
  }

  function renderSignIn() {
    setBody([
      target(),
      h("p", { text: "Expert reviews are open to staff at The Agency Fund and Irrational Labs. Sign in with your work Google account to start." }),
      h("p", { class: "muted", text: "You don't need a GitHub account. The site posts your review to GitHub for you, with your name and organization, where maintainers track and answer it." }),
      googleButton("review", showReview),
      h("p", { class: "fb-fine", text: "We keep your name, email address, and when you signed in, so we know who reviewed what. Your email is never shown publicly." })
    ]);
  }

  function renderNotEligible() {
    setBody([
      h("p", {}, ["You're signed in as ", h("b", { text: user.email }), "."]),
      h("p", { text: "Expert reviews are limited to staff at The Agency Fund and Irrational Labs for now. You can still rate this skill and leave a comment, or report a problem on GitHub." }),
      h("p", { class: "fb-links" }, [
        h("button", { type: "button", class: "btn-secondary", onclick: function () { openPanel("rate", opener); }, text: "Rate this skill" }),
        h("a", { href: bugReportUrl(), rel: "noopener", target: "_blank", text: "Report a problem" }),
        h("button", { type: "button", class: "link-btn", onclick: signOut, text: "Sign out" })
      ])
    ]);
  }

  /* ---------- review: the form ---------- */
  var draftKey = "besci:review-draft:" + skill.name;

  function renderForm() {
    var draft = recall(draftKey) || {};
    var form = h("form", { class: "fb-form", novalidate: true });

    var verdicts = h("fieldset", { class: "fb-field" }, [h("legend", { text: "Your verdict" })].concat(VERDICTS.map(function (v) {
      return h("label", { class: "fb-radio" }, [
        h("input", { type: "radio", name: "verdict", value: v[0], checked: draft.verdict === v[0] }), " " + v[1]
      ]);
    })));
    var parts = h("fieldset", { class: "fb-field" }, [
      h("legend", {}, ["Which parts does it concern? ", h("span", { class: "fb-opt", text: "Optional" })]),
      h("div", { class: "fb-chips" }, PARTS.map(function (p) {
        return h("label", { class: "fb-chip" }, [h("input", { type: "checkbox", name: "parts", value: p, checked: (draft.parts || []).indexOf(p) >= 0 }), h("span", { text: p })]);
      }))
    ]);
    var review = h("textarea", { id: "fb-review", name: "review", rows: "10", maxlength: String(MAX_REVIEW), required: true, "aria-describedby": "fb-review-hint" });
    review.value = draft.review || "";
    var evidence = h("textarea", { id: "fb-evidence", name: "evidence", rows: "3", maxlength: "5000" });
    evidence.value = draft.evidence || "";
    var name = h("input", { id: "fb-name", name: "name", type: "text", maxlength: "80", autocomplete: "name", required: true });
    name.value = draft.name || user.name || "";
    var gh = h("input", { id: "fb-github", name: "github", type: "text", maxlength: "39", autocomplete: "off", spellcheck: "false", "aria-describedby": "fb-github-hint" });
    gh.value = draft.github || recall("besci:github") || "";
    var submit = h("button", { class: "btn", type: "submit", text: "Submit review" });

    form.appendChild(h("p", { class: "fb-who" }, ["Signed in as ", h("b", { text: user.name || user.email }), " (" + user.org_name + "). ",
      h("button", { type: "button", class: "link-btn", onclick: signOut, text: "Sign out" })]));
    form.appendChild(target());
    form.appendChild(verdicts);
    form.appendChild(parts);
    form.appendChild(h("div", { class: "fb-field" }, [
      h("label", { for: "fb-review", text: "Your review" }),
      h("p", { id: "fb-review-hint", class: "fb-hint", text: "What works, what's wrong or missing, and what you would change. Quote the line you mean when you can. Markdown formatting works." }),
      review
    ]));
    form.appendChild(h("div", { class: "fb-field" }, [
      h("label", { for: "fb-evidence" }, ["Evidence or sources ", h("span", { class: "fb-opt", text: "Optional" })]), evidence
    ]));
    form.appendChild(h("div", { class: "fb-field" }, [h("label", { for: "fb-name", text: "Your name, as shown on the review" }), name]));
    form.appendChild(h("div", { class: "fb-field" }, [
      h("label", { for: "fb-github" }, ["GitHub username ", h("span", { class: "fb-opt", text: "Optional" })]),
      h("p", { id: "fb-github-hint", class: "fb-hint", text: "Add it and GitHub will email you when a maintainer replies. No account? Leave it blank; this page shows when your review is answered." }),
      gh
    ]));
    form.appendChild(h("p", { class: "fb-fine", text: "Your review is posted publicly on GitHub with your name and organization. Your email address is not." }));
    form.appendChild(submit);

    function values() {
      var v = $("input[name=verdict]:checked", form);
      return {
        verdict: v ? v.value : "",
        parts: $$("input[name=parts]:checked", form).map(function (i) { return i.value; }),
        review: review.value.trim(),
        evidence: evidence.value.trim(),
        name: name.value.trim(),
        github: gh.value.trim().replace(/^@/, "")
      };
    }
    form.addEventListener("input", function () { store(draftKey, values()); });
    form.addEventListener("change", function () { store(draftKey, values()); });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = values();
      clearMessage();
      if (!f.verdict) return showMessage("Choose a verdict.");
      if (f.review.length < MIN_REVIEW) { review.focus(); return showMessage("The review is too short. Say what works, what doesn't, and what you'd change."); }
      if (!f.name) { name.focus(); return showMessage("Add your name; it appears on the review."); }
      if (f.github && !/^[A-Za-z0-9](?:[A-Za-z0-9]|-(?=[A-Za-z0-9])){0,38}$/.test(f.github)) { gh.focus(); return showMessage("That isn't a valid GitHub username. Leave it blank if you don't have one."); }
      submit.disabled = true;
      submit.textContent = "Filing your review…";
      f.skill = skill.name;
      f.commit = skill.commit;
      api("POST", "/api/review/", f).then(function (res) {
        if (res._status === 200 && res.ok) {
          store(draftKey, null);
          if (f.github) store("besci:github", f.github);
          track("review_filed", { skill: skill.name, verdict: f.verdict });
          renderFiled(res, f);
          addFiledReview(res, f);
          return;
        }
        submit.disabled = false;
        submit.textContent = "Submit review";
        if (res._status === 401) { user = null; return showReview(); }
        showMessage(res.error || "The review couldn't be filed. Your text is saved in this browser; try again in a minute.");
        if (res.fallback || res._status === 0 || res._status >= 500) renderFallback(form, f);
      });
    });

    setBody([form]);
  }

  /* If the site can't reach GitHub: the same review as a prefilled issue form. */
  function renderFallback(form, f) {
    if ($(".fb-fallback", form)) return;
    var params = {
      template: "expert-review.yml",
      title: "[Expert review] " + skill.name + " v" + skill.version + " by " + f.name + " (" + user.org + ")",
      skill: skill.name, version: skill.version, content: contentUrl(),
      review: f.review, evidence: f.evidence, reviewer: f.name + ", " + user.org_name
    };
    var url = githubUrl(params), tooLong = url.length > 7000;
    if (tooLong) { params.review = "(Paste your review here.)"; url = githubUrl(params); }
    var copy = h("button", { type: "button", class: "btn-secondary", text: "Copy your review" });
    copy.addEventListener("click", function () {
      var done = function () { copy.textContent = "Copied"; };
      if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(f.review).then(done, function () {});
    });
    form.appendChild(h("div", { class: "fb-fallback" }, [
      h("p", { text: "You can post it on GitHub yourself instead. You'll need a free GitHub account; the form opens filled in" + (tooLong ? ", except the review itself, which is too long to pass along. Copy it first, then paste it in." : ".") }),
      h("p", { class: "fb-links" }, [h("a", { class: "btn-secondary", href: url, rel: "noopener", target: "_blank", text: "Post on GitHub" }), tooLong ? copy : null])
    ]));
  }

  function renderFiled(res, f) {
    setBody([
      h("p", { class: "fb-done" }, [h("b", { text: "Filed as issue #" + res.number + "." })]),
      h("p", { text: "It's listed under Reviews on this page and on GitHub, where maintainers will answer it. " +
        (f.github ? "GitHub will email @" + f.github + " when someone replies." : "When a new version of the skill answers it, the review here will say so.") }),
      h("p", { class: "fb-links" }, [
        h("a", { class: "btn-secondary", href: res.url, rel: "noopener", target: "_blank", text: "Open #" + res.number + " on GitHub" }),
        h("button", { type: "button", class: "link-btn", onclick: closePanel, text: "Close" })
      ])
    ]);
  }

  /* ---------- the Reviews tab ---------- */
  var list = $("[data-expert-reviews]");
  var summary = $("[data-review-summary]");
  var countEl = $("[data-review-count]");
  var shown = [];

  function statusOf(r) {
    var ref = (skill.changelog_refs || {})[String(r.number)];
    if (ref) return { kind: "answered", text: "Answered in v" + ref.version, ref: ref };
    var labels = r.labels || [];
    if (r.state === "closed" && (labels.indexOf("review:declined") >= 0 || r.state_reason === "not_planned")) return { kind: "declined", text: "Closed without changes" };
    if (r.state === "closed") return { kind: "closed", text: labels.indexOf("review:addressed") >= 0 ? "Addressed" : "Closed" };
    return { kind: "open", text: "Open" };
  }

  // The same rough Markdown-to-text as the server's excerpt (api/_review_issue.py).
  function plain(md) {
    var t = md.replace(/```[\s\S]*?```/g, " ").replace(/!\[[^\]]*\]\([^)]*\)/g, "").replace(/\[([^\]]*)\]\([^)]*\)/g, "$1")
      .replace(/^\s{0,3}(#{1,6}\s+|>\s?|[-*+]\s+|\d+\.\s+)/gm, "").replace(/\*\*|__|`/g, "").replace(/\n{3,}/g, "\n\n").trim();
    return t.length > 600 ? t.slice(0, 600).replace(/\s+\S*$/, "") + "…" : t;
  }

  function reviewCard(r) {
    var st = statusOf(r);
    var older = r.version && r.version !== skill.version;
    var link = r.url ? h("a", { href: r.url, rel: "noopener", text: "Read the full review on GitHub (#" + r.number + (r.comments ? ", " + r.comments + (r.comments === 1 ? " reply" : " replies") : "") + ")" }) : null;
    return h("article", { class: "review-card", id: "review-" + r.number }, [
      h("header", { class: "review-head" }, [
        h("b", { text: r.name || "A reviewer" }),
        r.org_name ? h("span", { text: r.org_name }) : null,
        r.created_at ? h("time", { datetime: r.created_at, text: formatDate(r.created_at) }) : null
      ]),
      h("p", { class: "review-meta" }, [
        h("span", { class: "review-state state-" + st.kind, text: st.text }),
        r.verdict_label ? h("span", { class: "pill", text: r.verdict_label }) : null,
        r.version ? h("span", { class: "pill", text: (older ? "Reviewed on v" : "v") + r.version }) : null
      ]),
      r.parts && r.parts.length ? h("p", { class: "review-parts", text: "Concerns: " + r.parts.join(", ") }) : null,
      r.excerpt ? h("p", { class: "review-excerpt", text: r.excerpt }) : null,
      st.ref ? h("p", { class: "review-answer" }, [h("b", { text: "Version " + st.ref.version + ": " }), st.ref.text]) : null,
      link ? h("p", { class: "review-link" }, [link]) : null
    ]);
  }

  function renderReviews(items) {
    shown = items;
    if (!list) return;
    list.textContent = "";
    if (!items.length) list.appendChild(h("p", { class: "muted", text: "No expert reviews of this skill yet." }));
    items.forEach(function (r) { list.appendChild(reviewCard(r)); });
    var answered = items.filter(function (r) { return statusOf(r).kind === "answered"; }).length;
    if (countEl) countEl.textContent = items.length ? String(items.length) : "";
    if (summary) {
      summary.hidden = !items.length;
      summary.textContent = items.length + (items.length === 1 ? " expert review" : " expert reviews") + (answered ? ", " + answered + " answered by a later version" : "") + ".";
    }
  }

  function addFiledReview(res, f) {
    if (shown.some(function (r) { return r.number === res.number; })) return;
    var verdict = VERDICTS.filter(function (v) { return v[0] === f.verdict; })[0];
    renderReviews([{
      number: res.number, url: res.url, state: "open", labels: [], comments: 0, created_at: new Date().toISOString(),
      name: f.name, org_name: user.org_name, version: skill.version, verdict: f.verdict, verdict_label: verdict ? verdict[1] : "",
      parts: f.parts, excerpt: plain(f.review)
    }].concat(shown));
  }

  function loadReviews() {
    if (!list) return;
    fetch("/api/reviews/", { credentials: "omit" }).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
      if (!d || !d.ok) return;
      renderReviews((d.skills || {})[skill.name] || []);
      // Reviews load in above the ratings; keep a #ratings link on target.
      var target = location.hash === "#ratings" && document.getElementById("ratings");
      if (target && !target.closest("[hidden]")) target.scrollIntoView();
    }).catch(function () { /* keep the link to GitHub */ });
  }

  /* ---------- ratings ---------- */
  var ratingsBox = $("[data-ratings]");
  var ratingSummary = $("[data-rating-summary]");
  var ratings = null; // the last /api/ratings answer
  var STAR_WORDS = ["", "Poor", "Fair", "Good", "Very good", "Excellent"];

  function starsEl(n, label) {
    var wrap = h("span", { class: "stars", role: "img", "aria-label": label || n + " out of 5 stars" });
    for (var i = 1; i <= 5; i++) wrap.appendChild(icon(i <= n ? "star-fill" : "star"));
    return wrap;
  }
  function plural(n, one, many) { return n + " " + (n === 1 ? one : many); }

  function loadRatings(fresh) {
    if (!ratingsBox && !ratingSummary) return Promise.resolve();
    var admin = !!(user && user.is_admin);
    // A fresh query string skips the minute-long CDN cache after you rate.
    var url = "/api/ratings/?skill=" + encodeURIComponent(skill.name) + (admin ? "&admin=1" : "") + (fresh ? "&fresh=" + Date.now() : "");
    return fetch(url, { credentials: admin ? "same-origin" : "omit" }).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
      if (d && d.ok) { ratings = d; renderRatings(); }
    }).catch(function () { /* keep the placeholder */ });
  }

  function renderRatings() {
    var d = ratings;
    if (ratingSummary) {
      ratingSummary.textContent = "";
      if (d.count) {
        ratingSummary.appendChild(starsEl(Math.round(d.average), "Rated " + d.average.toFixed(1) + " out of 5"));
        ratingSummary.appendChild(h("b", { text: d.average.toFixed(1) }));
        ratingSummary.appendChild(h("span", { text: "(" + plural(d.count, "rating", "ratings") + ")" }));
      } else {
        ratingSummary.appendChild(h("span", { text: "No ratings yet" }));
      }
      ratingSummary.hidden = false;
    }
    if (!ratingsBox) return;
    ratingsBox.textContent = "";
    var rateBtn = h("button", { type: "button", class: "btn-secondary", onclick: function () { openPanel("rate", rateBtn); } }, [icon("star"), "Rate this skill"]);
    if (!d.count) {
      ratingsBox.appendChild(h("p", { class: "muted", text: "No ratings yet. If you've used this skill, yours would be the first." }));
      ratingsBox.appendChild(rateBtn);
      return;
    }
    var bars = h("div", { class: "rating-bars" });
    for (var n = 5; n >= 1; n--) {
      var k = d.distribution[String(n)] || 0;
      bars.appendChild(h("div", { class: "rating-bar" }, [
        h("span", { text: plural(n, "star", "stars") }),
        h("span", { class: "bar", "aria-hidden": "true" }, [h("span", { style: "width:" + Math.round(100 * k / d.count) + "%" })]),
        h("span", { class: "bar-n", text: String(k) })
      ]));
    }
    ratingsBox.appendChild(h("div", { class: "rating-overview" }, [
      h("div", { class: "rating-big" }, [
        h("b", { text: d.average.toFixed(1) }),
        starsEl(Math.round(d.average), "Rated " + d.average.toFixed(1) + " out of 5"),
        h("span", { text: plural(d.count, "rating", "ratings") })
      ]),
      bars,
      rateBtn
    ]));
    if (!d.comments.length) ratingsBox.appendChild(h("p", { class: "muted", text: "No comments yet." }));
    d.comments.forEach(function (cm) { ratingsBox.appendChild(commentCard(cm)); });
  }

  function commentCard(cm) {
    var admin = user && user.is_admin;
    var tools = null;
    if (admin) {
      tools = h("p", { class: "rating-admin" }, [
        h("button", { type: "button", class: "link-btn", text: cm.hidden ? "Show comment" : "Hide comment", onclick: function () {
          api("PATCH", "/api/ratings/", { id: cm.id, hidden: !cm.hidden }).then(function (r) { if (r.ok) loadRatings(true); });
        } }),
        h("button", { type: "button", class: "link-btn", text: "Delete rating", onclick: function () {
          if (window.confirm("Delete this rating and its comment? This can't be undone.")) {
            api("DELETE", "/api/ratings/", { id: cm.id }).then(function (r) { if (r.ok) loadRatings(true); });
          }
        } })
      ]);
    }
    return h("article", { class: "rating-card" + (cm.hidden ? " is-hidden" : "") }, [
      h("header", { class: "review-head" }, [
        starsEl(cm.stars),
        h("b", { text: cm.name }),
        cm.badge ? h("span", { class: "rating-badge", text: cm.badge }) : null,
        cm.date ? h("time", { datetime: cm.date, text: formatDate(cm.date) }) : null,
        cm.version ? h("span", { text: "v" + cm.version }) : null
      ]),
      h("p", { class: "review-excerpt", text: cm.comment }),
      cm.hidden ? h("p", { class: "fb-fine", text: "Hidden from readers by a maintainer." }) : null,
      tools
    ]);
  }

  /* ---------- rate: which screen to show ---------- */
  function rateTarget() {
    return h("p", { class: "fb-target" }, ["You're rating ", h("code", { text: skill.name }), " version " + skill.version + "."]);
  }

  function showRate() {
    panelTitle.textContent = "Rate this skill";
    if (!skill.google_client_id) return rateUnavailable();
    setBody([h("p", { class: "muted", text: "Checking whether you're signed in…" })]);
    (user ? Promise.resolve(user) : loadUser()).then(function (u) {
      if (u.unavailable) return rateUnavailable();
      if (!u.signed_in) return rateSignIn();
      api("GET", "/api/ratings/?skill=" + encodeURIComponent(skill.name) + "&mine=1").then(function (m) {
        if (m._status !== 200) return rateUnavailable();
        rateForm(m.mine || null);
      });
    });
  }

  function rateUnavailable() {
    setBody([rateTarget(), h("p", { text: "Ratings aren't available on this copy of the site yet." }),
      h("p", {}, [h("a", { href: bugReportUrl(), rel: "noopener", target: "_blank", text: "Report a problem with this skill on GitHub" })])]);
  }

  function rateSignIn() {
    setBody([
      rateTarget(),
      h("p", { text: "Sign in with Google to rate. Any Google account works." }),
      h("p", { class: "muted", text: "Each person rates a skill once; rate again any time to change it. You choose whether your name appears." }),
      googleButton("rate", showRate),
      h("p", { class: "fb-fine", text: "We keep your name, email address, and when you signed in, so each person rates once. Your email is never shown publicly." })
    ]);
  }

  function rateForm(mine) {
    var form = h("form", { class: "fb-form", novalidate: true });
    var chosen = mine ? mine.stars : 0;
    var word = h("span", { class: "star-word", "aria-hidden": "true", text: STAR_WORDS[chosen] });
    var starLabels = [];
    var paint = function (n) {
      starLabels.forEach(function (lb, i) { lb.classList.toggle("on", i < n); });
      word.textContent = STAR_WORDS[n] || "";
    };
    var starRow = h("div", { class: "star-input", onmouseleave: function () { paint(chosen); } });
    for (var i = 1; i <= 5; i++) {
      (function (n) {
        var input = h("input", { type: "radio", name: "stars", value: String(n), class: "sr-only", checked: n === chosen,
          onchange: function () { chosen = n; paint(n); clearMessage(); } });
        var lb = h("label", { title: STAR_WORDS[n], onmouseenter: function () { paint(n); } },
          [input, icon("star-fill"), h("span", { class: "sr-only", text: plural(n, "star", "stars") + ", " + STAR_WORDS[n] })]);
        starLabels.push(lb);
        starRow.appendChild(lb);
      })(i);
    }
    starRow.appendChild(word);
    paint(chosen);

    var comment = h("textarea", { id: "fb-comment", name: "comment", rows: "4", maxlength: "2000", "aria-describedby": "fb-comment-hint" });
    comment.value = mine ? mine.comment : "";
    var shownName = user.name || user.email.split("@")[0];
    var anonYes = h("input", { type: "radio", name: "anonymous", value: "1", checked: !!(mine && mine.anonymous) });
    var anonNo = h("input", { type: "radio", name: "anonymous", value: "0", checked: !(mine && mine.anonymous) });
    var submit = h("button", { class: "btn", type: "submit", text: mine ? "Update rating" : "Save rating" });

    form.appendChild(h("p", { class: "fb-who" }, ["Signed in as ", h("b", { text: shownName }), ". ",
      h("button", { type: "button", class: "link-btn", onclick: signOut, text: "Sign out" })]));
    form.appendChild(rateTarget());
    if (mine) {
      form.appendChild(h("p", { class: "fb-note", text: "You rated this " + plural(mine.stars, "star", "stars") + " on version " + mine.version +
        ". Saving replaces that rating." + (mine.hidden ? " A maintainer has hidden your comment from readers." : "") }));
    }
    form.appendChild(h("fieldset", { class: "fb-field" }, [h("legend", { text: "Your rating" }), starRow]));
    form.appendChild(h("div", { class: "fb-field" }, [
      h("label", { for: "fb-comment" }, ["Comment ", h("span", { class: "fb-opt", text: "Optional" })]),
      h("p", { id: "fb-comment-hint", class: "fb-hint", text: "What worked or didn't when you used it. Comments are public." }),
      comment
    ]));
    form.appendChild(h("fieldset", { class: "fb-field" }, [
      h("legend", { text: "Show with my rating" }),
      h("label", { class: "fb-radio" }, [anonNo, " My name (" + shownName + (user.org ? ", " + user.org + " staff" : "") + ")"]),
      h("label", { class: "fb-radio" }, [anonYes, " Anonymous"]),
      h("p", { class: "fb-hint", text: "Anonymous hides your name on the site. Maintainers can still see who posted, to stop duplicate ratings and abuse." })
    ]));
    var actions = h("p", { class: "fb-links" }, [submit]);
    if (mine) {
      actions.appendChild(h("button", { type: "button", class: "link-btn", text: "Remove my rating", onclick: function () {
        api("DELETE", "/api/ratings/", { skill: skill.name }).then(function (r) {
          if (!r.ok) return showMessage(r.error || "The rating couldn't be removed.");
          setBody([h("p", { class: "fb-done", text: "Your rating is removed." }), h("p", {}, [h("button", { type: "button", class: "link-btn", onclick: closePanel, text: "Close" })])]);
          loadRatings(true);
        });
      } }));
    }
    form.appendChild(actions);

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      clearMessage();
      if (!chosen) return showMessage("Choose from one to five stars.");
      submit.disabled = true;
      submit.textContent = "Saving…";
      var body = { skill: skill.name, stars: chosen, comment: comment.value.trim(), anonymous: anonYes.checked };
      api("POST", "/api/ratings", body).then(function (r) {
        if (r._status === 200 && r.ok) {
          track("rating_saved", { skill: skill.name, stars: chosen, comment: !!body.comment, anonymous: body.anonymous });
          setBody([
            h("p", { class: "fb-done" }, [h("b", { text: "Saved. Thanks for rating this skill." })]),
            h("p", { text: body.comment ? "Your comment shows under Reviews on this page." : "Your rating counts toward the average now." }),
            h("p", { class: "fb-links" }, [
              h("a", { href: "#ratings", onclick: closePanel, text: "See ratings and comments" }),
              h("button", { type: "button", class: "link-btn", onclick: closePanel, text: "Close" })
            ])
          ]);
          loadRatings(true);
          return;
        }
        submit.disabled = false;
        submit.textContent = mine ? "Update rating" : "Save rating";
        if (r._status === 401) { setUser(null); return showRate(); }
        showMessage(r.error || "The rating couldn't be saved. Please try again in a minute.");
      });
    });
    setBody([form]);
  }

  /* ---------- wiring ---------- */
  $$("[data-panel-open]").forEach(function (b) {
    b.setAttribute("aria-expanded", "false");
    b.addEventListener("click", function () { openPanel(b.getAttribute("data-panel-open"), b); });
  });
  // /skills/<name>/#review (or #rate) opens the panel, so a request to review can be one link.
  if (location.hash === "#review" || location.hash === "#rate") {
    var which = location.hash.slice(1);
    openPanel(which, $("[data-panel-open=" + which + "]"));
  }
  loadReviews();
  loadRatings();
  // Someone who signed in before: check the session once, so maintainers see their moderation controls.
  if (recall(SIGNED_IN) && !user) loadUser().then(function (u) { if (u.is_admin) loadRatings(true); });
})();
