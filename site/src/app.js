/* Behavioral Science Skills — client script. No dependencies.
   Handles: theme toggle, copy buttons, catalog search/filter (with URL sync),
   the propose form (prefilled GitHub issue), and the upload form (/api/submit). */
(function () {
  "use strict";

  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };

  /* ---------- theme ---------- */
  var toggle = $(".theme-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var root = document.documentElement;
      var current = root.getAttribute("data-theme");
      var prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
      var isDark = current === "dark" || (!current && prefersDark);
      var next = isDark ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) { /* storage unavailable */ }
    });
  }

  /* ---------- copy buttons ---------- */
  $$(".copy").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy") || "";
      var done = function () {
        btn.setAttribute("data-copied", "1");
        var old = btn.textContent;
        btn.textContent = "Copied";
        setTimeout(function () { btn.removeAttribute("data-copied"); btn.textContent = old; }, 1500);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { fallbackCopy(text); done(); });
      } else { fallbackCopy(text); done(); }
    });
  });
  function fallbackCopy(text) {
    var ta = document.createElement("textarea");
    ta.value = text; ta.setAttribute("readonly", ""); ta.style.position = "absolute"; ta.style.left = "-9999px";
    document.body.appendChild(ta); ta.select();
    try { document.execCommand("copy"); } catch (e) { /* ignore */ }
    document.body.removeChild(ta);
  }

  /* ---------- catalog search + filter ---------- */
  var grid = $("#grid");
  if (grid) {
    var cards = $$(".card", grid);
    var q = $("#q");
    var selects = { stage: $("#f-stage"), type: $("#f-type"), org: $("#f-org"), status: $("#f-status"), tag: $("#f-tag") };
    var count = $("#f-count");
    var noResults = $("#no-results");
    var index = {}; // name -> searchable text (from catalog.json when available)

    cards.forEach(function (c) { index[c.getAttribute("data-name")] = c.getAttribute("data-search") || ""; });

    fetch("/data/catalog.json").then(function (r) { return r.ok ? r.json() : null; }).then(function (data) {
      if (!data || !data.skills) return;
      data.skills.forEach(function (s) {
        var text = [s.name, s.title, s.description, s.what_it_does, (s.tags || []).join(" "), (s.use_when || []).join(" ")].join(" ").toLowerCase();
        index[s.name] = text;
      });
      apply();
    }).catch(function () { /* offline: fall back to data-search */ });

    function readUrl() {
      var p = new URLSearchParams(location.search);
      if (q) q.value = p.get("q") || "";
      Object.keys(selects).forEach(function (k) { if (selects[k]) selects[k].value = p.get(k) || ""; });
    }
    function writeUrl() {
      var p = new URLSearchParams();
      if (q && q.value) p.set("q", q.value);
      Object.keys(selects).forEach(function (k) { if (selects[k] && selects[k].value) p.set(k, selects[k].value); });
      var qs = p.toString();
      history.replaceState(null, "", location.pathname + (qs ? "?" + qs : ""));
    }
    function apply() {
      var text = (q && q.value || "").trim().toLowerCase();
      var terms = text ? text.split(/\s+/) : [];
      var shown = 0;
      cards.forEach(function (c) {
        var ok = true;
        Object.keys(selects).forEach(function (k) {
          var val = selects[k] && selects[k].value;
          if (!val) return;
          if (k === "tag") {
            var tags = (c.getAttribute("data-tags") || "").split(" ");
            if (tags.indexOf(val) === -1) ok = false;
          } else if (c.getAttribute("data-" + k) !== val) ok = false;
        });
        if (ok && terms.length) {
          var hay = index[c.getAttribute("data-name")] || c.getAttribute("data-search") || "";
          ok = terms.every(function (t) { return hay.indexOf(t) !== -1; });
        }
        c.hidden = !ok;
        if (ok) shown++;
      });
      if (count) count.textContent = shown === cards.length ? "" : shown + " of " + cards.length + " shown";
      if (noResults) noResults.hidden = shown !== 0;
      writeUrl();
    }
    readUrl(); apply();
    if (q) q.addEventListener("input", apply);
    Object.keys(selects).forEach(function (k) { if (selects[k]) selects[k].addEventListener("change", apply); });
    var clear = function () {
      if (q) q.value = "";
      Object.keys(selects).forEach(function (k) { if (selects[k]) selects[k].value = ""; });
      apply();
    };
    var c1 = $("#f-clear"), c2 = $("#f-clear-2");
    if (c1) c1.addEventListener("click", clear);
    if (c2) c2.addEventListener("click", clear);
    document.addEventListener("keydown", function (e) {
      if (e.key === "/" && q && document.activeElement !== q && !/input|textarea|select/i.test(document.activeElement.tagName)) {
        e.preventDefault(); q.focus();
      }
    });
  }

  /* ---------- propose form -> prefilled GitHub issue ---------- */
  var propose = $("#propose-form");
  if (propose) {
    propose.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = propose.elements;
      var repo = propose.getAttribute("data-repo");
      var get = function (n) { return (f[n] && f[n].value || "").trim(); };
      var stageSel = f["stage"];
      var stageLabel = stageSel && stageSel.options[stageSel.selectedIndex] ? stageSel.options[stageSel.selectedIndex].text.split(":")[0] : get("stage");
      var title = "Skill proposal: " + get("title");
      var body = [
        "### What it does (one sentence, no \"and\")", get("what"), "",
        "### Stage", get("stage") + (stageLabel ? " (" + stageLabel + ")" : ""), "",
        "### Why it is atomic", get("atomicity"), "",
        "### Evidence base", get("evidence"), "",
        "### Proposed by", get("contact"), "",
        "_Submitted from the website propose form._"
      ].join("\n");
      var p = new URLSearchParams();
      p.set("template", "propose-skill.yml");
      p.set("labels", "skill-proposal");
      p.set("title", title);
      p.set("body", body);
      // Field ids for the issue form, if it uses matching ids.
      p.set("what", get("what"));
      p.set("stage", get("stage"));
      p.set("atomicity", get("atomicity"));
      p.set("evidence", get("evidence"));
      p.set("contact", get("contact"));
      var url = "https://github.com/" + repo + "/issues/new?" + p.toString();
      window.open(url, "_blank", "noopener");
    });
  }

  /* ---------- upload form -> /api/submit ---------- */
  var upload = $("#upload-form");
  if (upload) {
    var result = $("#upload-result");
    var spinner = $("#upload-spinner");
    var submit = $("#upload-submit");
    var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };
    var render = function (cls, html) { result.innerHTML = '<div class="' + cls + '">' + html + "</div>"; };
    upload.addEventListener("submit", function (e) {
      e.preventDefault();
      var fd = new FormData(upload);
      if (!fd.get("disclosure_ack")) { render("result-err", "Please confirm you have read the disclosure."); return; }
      var file = fd.get("file");
      if (file && file.size > 10 * 1024 * 1024) { render("result-err", "The file is over 10 MB."); return; }
      submit.disabled = true; spinner.hidden = false; result.innerHTML = "";
      fetch(upload.getAttribute("action") || "/api/submit", { method: "POST", body: fd })
        .then(function (r) { return r.json().then(function (j) { return { status: r.status, json: j }; }).catch(function () { return { status: r.status, json: { ok: false, error: "The server returned something that was not JSON (HTTP " + r.status + ")." } }; }); })
        .then(function (res) {
          var j = res.json || {};
          var report = j.report ? '<pre class="result-report">' + esc(j.report) + "</pre>" : "";
          if (j.ok) {
            render("result-ok", "<strong>Pull request opened.</strong> A maintainer will review it. " +
              (j.pr_url ? '<a href="' + esc(j.pr_url) + '" rel="noopener" target="_blank">' + esc(j.pr_url) + "</a>" : "") +
              (j.skill_name ? "<br>Skill: <code>" + esc(j.skill_name) + "</code>" : "") + report);
          } else {
            render("result-err", "<strong>Not submitted.</strong> " + esc(j.error || ("HTTP " + res.status)) + report);
          }
        })
        .catch(function (err) { render("result-err", "Network error: " + esc(err && err.message)); })
        .then(function () { submit.disabled = false; spinner.hidden = true; });
    });
  }
})();
