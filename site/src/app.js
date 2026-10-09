/* Behavioral Science Skills — client script. No dependencies.
   Theme toggle (dark by default), mobile menu, copy buttons, install tabs,
   hero typewriter, count-up stats, catalog search/filter with URL sync,
   stage strip, cards/map view toggle, the skill-chain map, TOC scroll-spy,
   the propose form (prefilled GitHub issue), and the upload form (/api/submit). */
(function () {
  "use strict";

  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };
  var reduceMotion = !!(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
  var root = document.documentElement;

  /* ---------- theme (dark by default) ---------- */
  function applyThemeLabel() {
    var light = root.getAttribute("data-theme") === "light";
    $$(".theme-toggle").forEach(function (b) {
      b.setAttribute("aria-label", light ? "Switch to dark mode" : "Switch to light mode");
      b.setAttribute("title", light ? "Switch to dark mode" : "Switch to light mode");
    });
  }
  $$(".theme-toggle").forEach(function (b) {
    b.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "light" ? "dark" : "light";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) { /* storage unavailable */ }
      applyThemeLabel();
      if (window.__redrawMap) window.__redrawMap();
    });
  });
  applyThemeLabel();

  /* ---------- mobile menu ---------- */
  var menuBtn = $(".menu-btn"), nav = $(".site-nav");
  if (menuBtn && nav) {
    menuBtn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && nav.classList.contains("open")) { nav.classList.remove("open"); menuBtn.setAttribute("aria-expanded", "false"); } });
  }

  /* ---------- copy buttons ---------- */
  function fallbackCopy(text) {
    var ta = document.createElement("textarea");
    ta.value = text; ta.setAttribute("readonly", ""); ta.style.position = "absolute"; ta.style.left = "-9999px";
    document.body.appendChild(ta); ta.select();
    try { document.execCommand("copy"); } catch (e) { /* ignore */ }
    document.body.removeChild(ta);
  }
  $$(".copy").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy") || "";
      var label = $(".copy-label", btn);
      var done = function () {
        btn.setAttribute("data-copied", "1");
        var old = label ? label.textContent : "";
        if (label) label.textContent = "Copied";
        setTimeout(function () { btn.removeAttribute("data-copied"); if (label) label.textContent = old; }, 1600);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { fallbackCopy(text); done(); });
      } else { fallbackCopy(text); done(); }
    });
  });

  /* ---------- tabs (install options) ---------- */
  $$("[data-tabs]").forEach(function (box) {
    var key = box.getAttribute("data-tabs") || "tabs";
    var tabs = $$("[role=tab]", box), panels = $$("[role=tabpanel]", box);
    function select(i, focus) {
      tabs.forEach(function (t, j) {
        var on = i === j;
        t.setAttribute("aria-selected", on ? "true" : "false");
        t.tabIndex = on ? 0 : -1;
        if (panels[j]) panels[j].hidden = !on;
      });
      if (focus) tabs[i].focus();
      try { localStorage.setItem("tab:" + key, tabs[i].getAttribute("data-tab") || String(i)); } catch (e) { /* ignore */ }
    }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { select(i, false); });
      t.addEventListener("keydown", function (e) {
        if (e.key === "ArrowRight") { e.preventDefault(); select((i + 1) % tabs.length, true); }
        if (e.key === "ArrowLeft") { e.preventDefault(); select((i - 1 + tabs.length) % tabs.length, true); }
      });
    });
    var saved = null;
    try { saved = localStorage.getItem("tab:" + key); } catch (e) { /* ignore */ }
    var idx = -1;
    tabs.forEach(function (t, i) { if (t.getAttribute("data-tab") === saved) idx = i; });
    select(idx >= 0 ? idx : 0, false);
  });

  /* ---------- hero typewriter ---------- */
  var demo = $("#demo-text");
  if (demo) {
    var examples = [];
    try { examples = JSON.parse(demo.getAttribute("data-examples") || "[]"); } catch (e) { examples = []; }
    if (!examples.length) examples = ["Where do I start?"];
    if (reduceMotion) {
      demo.textContent = examples[0];
    } else {
      var ei = 0, ci = 0, deleting = false, timer;
      var tick = function () {
        var full = examples[ei];
        if (!deleting) {
          ci++;
          demo.textContent = full.slice(0, ci);
          if (ci >= full.length) { deleting = true; timer = setTimeout(tick, 3200); return; }
          timer = setTimeout(tick, 22 + Math.random() * 30);
        } else {
          ci = Math.max(0, ci - 3);
          demo.textContent = full.slice(0, ci);
          if (ci === 0) { deleting = false; ei = (ei + 1) % examples.length; timer = setTimeout(tick, 350); return; }
          timer = setTimeout(tick, 14);
        }
      };
      timer = setTimeout(tick, 500);
      document.addEventListener("visibilitychange", function () {
        if (document.hidden) clearTimeout(timer); else timer = setTimeout(tick, 300);
      });
    }
  }

  /* ---------- count-up stats ---------- */
  $$("[data-count]").forEach(function (el) {
    var target = parseInt(el.getAttribute("data-count"), 10) || 0;
    if (reduceMotion || !("IntersectionObserver" in window)) { el.textContent = String(target); return; }
    el.textContent = "0";
    var io = new IntersectionObserver(function (entries) {
      if (!entries[0].isIntersecting) return;
      io.disconnect();
      var start = null, dur = 900;
      var step = function (ts) {
        if (!start) start = ts;
        var p = Math.min(1, (ts - start) / dur);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = String(Math.round(target * eased));
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    }, { threshold: 0.4 });
    io.observe(el);
  });

  /* ---------- catalog: search, filters, stage strip, view toggle ---------- */
  var grid = $("#grid");
  var catalogData = null;
  if (grid) {
    var cards = $$(".card", grid);
    var q = $("#q");
    var selects = { stage: $("#f-stage"), type: $("#f-type"), org: $("#f-org"), status: $("#f-status"), tag: $("#f-tag") };
    var count = $("#f-count");
    var noResults = $("#no-results");
    var stageBtns = $$(".stage-btn");
    var stageDesc = $("#stage-desc");
    var viewBtns = $$(".view-toggle button");
    var mapEl = $("#map");
    var index = {};

    cards.forEach(function (c) { index[c.getAttribute("data-name")] = c.getAttribute("data-search") || ""; });

    function readUrl() {
      var p = new URLSearchParams(location.search);
      if (q) q.value = p.get("q") || "";
      Object.keys(selects).forEach(function (k) { if (selects[k]) selects[k].value = p.get(k) || ""; });
      return p.get("view") || "";
    }
    function writeUrl() {
      var p = new URLSearchParams();
      if (q && q.value) p.set("q", q.value);
      Object.keys(selects).forEach(function (k) { if (selects[k] && selects[k].value) p.set(k, selects[k].value); });
      if (currentView === "map") p.set("view", "map");
      var qs = p.toString();
      history.replaceState(null, "", location.pathname + (qs ? "?" + qs : "") + location.hash);
    }
    function syncStageStrip() {
      var val = selects.stage ? selects.stage.value : "";
      stageBtns.forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-stage") === val ? "true" : "false"); });
      if (stageDesc) {
        var active = stageBtns.filter(function (b) { return b.getAttribute("data-stage") === val; })[0];
        if (active) {
          stageDesc.innerHTML = "";
          var b = document.createElement("b"); b.textContent = active.getAttribute("data-label") + ": ";
          stageDesc.setAttribute("data-stage", val);
          stageDesc.appendChild(b);
          stageDesc.appendChild(document.createTextNode(active.getAttribute("data-desc") || ""));
        } else {
          stageDesc.removeAttribute("data-stage");
          stageDesc.textContent = stageDesc.getAttribute("data-default") || "";
        }
      }
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
      if (count) count.textContent = shown === cards.length ? cards.length + " skills" : shown + " of " + cards.length;
      if (noResults) noResults.hidden = shown !== 0 || currentView === "map";
      syncStageStrip();
      writeUrl();
    }

    var currentView = "cards";
    function setView(v, scroll) {
      currentView = v === "map" ? "map" : "cards";
      viewBtns.forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-view") === currentView ? "true" : "false"); });
      grid.hidden = currentView === "map";
      if (mapEl) mapEl.hidden = currentView !== "map";
      if (currentView === "map") ensureMap();
      if (noResults) noResults.hidden = currentView === "map" || noResults.hidden;
      writeUrl();
      if (scroll) { var h = $("#catalog"); if (h) h.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" }); }
    }
    viewBtns.forEach(function (b) { b.addEventListener("click", function () { setView(b.getAttribute("data-view"), false); }); });

    var initialView = readUrl();
    apply();
    if (initialView === "map") setView("map", false);

    fetch("/data/catalog.json").then(function (r) { return r.ok ? r.json() : null; }).then(function (data) {
      if (!data || !data.skills) return;
      catalogData = data;
      data.skills.forEach(function (s) {
        index[s.name] = [s.name, s.title, s.description, s.what_it_does, (s.tags || []).join(" "), (s.use_when || []).join(" "), (s.authors || []).join(" ")].join(" ").toLowerCase();
      });
      apply();
      if (currentView === "map") ensureMap();
    }).catch(function () { /* offline: fall back to data-search */ });

    if (q) q.addEventListener("input", apply);
    Object.keys(selects).forEach(function (k) { if (selects[k]) selects[k].addEventListener("change", apply); });
    stageBtns.forEach(function (b) {
      b.addEventListener("click", function () {
        var val = b.getAttribute("data-stage");
        if (selects.stage) selects.stage.value = selects.stage.value === val ? "" : val;
        if (currentView === "map") setView("cards", false);
        apply();
        var h = $("#catalog");
        if (h && selects.stage && selects.stage.value) h.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
      });
      b.addEventListener("mouseenter", function () {
        if (!stageDesc || (selects.stage && selects.stage.value)) return;
        stageDesc.innerHTML = "";
        var bb = document.createElement("b"); bb.textContent = b.getAttribute("data-label") + ": ";
        stageDesc.setAttribute("data-stage", b.getAttribute("data-stage"));
        stageDesc.appendChild(bb);
        stageDesc.appendChild(document.createTextNode(b.getAttribute("data-desc") || ""));
      });
      b.addEventListener("mouseleave", function () { if (selects.stage && !selects.stage.value) syncStageStrip(); });
    });
    var clear = function () {
      if (q) q.value = "";
      Object.keys(selects).forEach(function (k) { if (selects[k]) selects[k].value = ""; });
      apply();
    };
    var c1 = $("#f-clear"), c2 = $("#f-clear-2");
    if (c1) c1.addEventListener("click", clear);
    if (c2) c2.addEventListener("click", clear);
    document.addEventListener("keydown", function (e) {
      var typing = /input|textarea|select/i.test(document.activeElement.tagName);
      if (e.key === "/" && q && !typing) { e.preventDefault(); q.focus(); q.select(); }
      if (e.key === "Escape" && q && document.activeElement === q) { q.value = ""; apply(); q.blur(); }
    });

    /* ---------- skill-chain map ---------- */
    var mapBuilt = false;
    function ensureMap() {
      if (mapBuilt || !mapEl) return;
      if (!catalogData) { mapEl.innerHTML = '<p class="muted" style="padding:1.25rem">Loading the catalog…</p>'; return; }
      mapBuilt = true;
      renderMap(mapEl, catalogData);
    }
    function renderMap(container, data) {
      var tax = data.taxonomy || {};
      var stages = (tax.stages || []).filter(function (s) { return s && s.id && s.id !== "other"; });
      var io = {};
      (tax.io_types || []).forEach(function (t) { if (t && t.id) io[t.id] = t; });
      var skills = data.skills || [];
      var producers = {};
      skills.forEach(function (s) { (s.produces || []).forEach(function (t) { (producers[t] = producers[t] || []).push(s.name); }); });
      var inputs = [];
      skills.forEach(function (s) { (s.consumes || []).forEach(function (t) {
        if (io[t] && io[t].user_suppliable && !producers[t] && inputs.indexOf(t) < 0) inputs.push(t);
      }); });

      var cols = [{ id: "you", label: "You supply", stage: "", nodes: inputs.map(function (t) { return { id: "io:" + t, label: t, title: io[t].label, io: true }; }) }];
      stages.forEach(function (st) {
        cols.push({ id: st.id, label: st.label, stage: st.id, nodes: skills.filter(function (s) { return s.stage === st.id && s.type !== "meta"; }).map(function (s) { return { id: s.name, label: s.name, title: s.title, url: s.url, stage: st.id }; }) });
      });
      var meta = skills.filter(function (s) { return s.type === "meta" || s.stage === "other"; });
      cols.push({ id: "other", label: "Meta skills", stage: "other", nodes: meta.map(function (s) { return { id: s.name, label: s.name, title: s.title, url: s.url, stage: "other" }; }) });

      var edges = [];
      skills.forEach(function (c) { (c.consumes || []).forEach(function (t) {
        (producers[t] || []).forEach(function (p) { if (p !== c.name) edges.push({ from: p, to: c.name, via: t }); });
        if (inputs.indexOf(t) >= 0) edges.push({ from: "io:" + t, to: c.name, via: t });
      }); });

      container.innerHTML = "";
      var inner = document.createElement("div"); inner.className = "map-inner";
      var svgNS = "http://www.w3.org/2000/svg";
      var svg = document.createElementNS(svgNS, "svg"); svg.setAttribute("class", "map-svg"); svg.setAttribute("aria-hidden", "true");
      inner.appendChild(svg);
      var nodeEls = {};
      cols.forEach(function (col) {
        if (!col.nodes.length) return;
        var c = document.createElement("div"); c.className = "map-col"; c.setAttribute("data-stage", col.stage);
        var h = document.createElement("h4");
        var d = document.createElement("span"); d.className = "dot"; if (col.id === "you") d.style.display = "none";
        h.appendChild(d); h.appendChild(document.createTextNode(col.label));
        var n = document.createElement("span"); n.className = "muted"; n.style.marginLeft = "auto"; n.style.fontFamily = "var(--mono)"; n.textContent = String(col.nodes.length);
        h.appendChild(n);
        c.appendChild(h);
        col.nodes.forEach(function (nd) {
          var el = document.createElement(nd.url ? "a" : "div");
          el.className = "map-node" + (nd.io ? " io" : "");
          if (nd.url) el.href = nd.url;
          el.setAttribute("data-id", nd.id);
          el.setAttribute("data-stage", nd.stage || "");
          el.appendChild(document.createTextNode(nd.label));
          if (nd.title) { var sm = document.createElement("small"); sm.textContent = nd.title; el.appendChild(sm); }
          el.addEventListener("mouseenter", function () { highlight(nd.id); });
          el.addEventListener("mouseleave", function () { highlight(null); });
          el.addEventListener("focus", function () { highlight(nd.id); });
          el.addEventListener("blur", function () { highlight(null); });
          c.appendChild(el);
          nodeEls[nd.id] = el;
        });
        inner.appendChild(c);
      });
      container.appendChild(inner);
      var legend = document.createElement("div"); legend.className = "map-legend";
      legend.innerHTML = '<span><i></i> one skill\'s output feeds the next</span><span><i class="hot"></i> hover a skill to trace its chain</span><span><em></em> something you can supply yourself</span><span class="muted">Scroll sideways if the map is wider than your screen.</span>';
      container.appendChild(legend);

      var pathEls = [];
      function draw() {
        while (svg.firstChild) svg.removeChild(svg.firstChild);
        pathEls = [];
        var base = inner.getBoundingClientRect();
        svg.setAttribute("viewBox", "0 0 " + inner.scrollWidth + " " + inner.scrollHeight);
        svg.setAttribute("width", inner.scrollWidth); svg.setAttribute("height", inner.scrollHeight);
        edges.forEach(function (e) {
          var a = nodeEls[e.from], b = nodeEls[e.to];
          if (!a || !b) return;
          var ra = a.getBoundingClientRect(), rb = b.getBoundingClientRect();
          var x1, y1, x2, y2, d;
          y1 = ra.top - base.top + ra.height / 2; y2 = rb.top - base.top + rb.height / 2;
          if (rb.left >= ra.right - 2) {
            x1 = ra.right - base.left; x2 = rb.left - base.left;
            var dx = Math.max(24, (x2 - x1) / 2);
            d = "M" + x1 + "," + y1 + " C" + (x1 + dx) + "," + y1 + " " + (x2 - dx) + "," + y2 + " " + x2 + "," + y2;
          } else {
            x1 = ra.left - base.left; x2 = rb.left - base.left;
            var bulge = 26;
            d = "M" + x1 + "," + y1 + " C" + (x1 - bulge) + "," + y1 + " " + (x2 - bulge) + "," + y2 + " " + x2 + "," + y2;
          }
          var p = document.createElementNS(svgNS, "path");
          p.setAttribute("d", d);
          p.setAttribute("data-from", e.from); p.setAttribute("data-to", e.to);
          var t = document.createElementNS(svgNS, "title"); t.textContent = e.from + " → " + e.to + " (" + e.via + ")";
          p.appendChild(t);
          svg.appendChild(p);
          pathEls.push(p);
        });
      }
      function highlight(id) {
        var connected = {};
        if (id) {
          connected[id] = true;
          edges.forEach(function (e) { if (e.from === id) connected[e.to] = true; if (e.to === id) connected[e.from] = true; });
        }
        Object.keys(nodeEls).forEach(function (k) {
          nodeEls[k].classList.toggle("is-hot", !!id && !!connected[k] && k !== id);
          nodeEls[k].classList.toggle("is-dim", !!id && !connected[k]);
        });
        pathEls.forEach(function (p) {
          var hot = !!id && (p.getAttribute("data-from") === id || p.getAttribute("data-to") === id);
          p.classList.toggle("is-hot", hot);
          p.classList.toggle("is-dim", !!id && !hot);
        });
      }
      draw();
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(draw);
      var rt;
      window.addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(draw, 120); });
      window.__redrawMap = draw;
    }
  }

  /* ---------- skill page: TOC scroll-spy ---------- */
  var toc = $(".toc");
  if (toc && "IntersectionObserver" in window) {
    var links = $$("a[href^='#']", toc);
    var targets = links.map(function (a) { return document.getElementById(a.getAttribute("href").slice(1)); }).filter(Boolean);
    var setActive = function (id) { links.forEach(function (a) { a.classList.toggle("is-active", a.getAttribute("href") === "#" + id); }); };
    var visible = {};
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { visible[en.target.id] = en.isIntersecting; });
      var first = targets.filter(function (t) { return visible[t.id]; })[0];
      if (first) setActive(first.id);
    }, { rootMargin: "-80px 0px -65% 0px", threshold: 0 });
    targets.forEach(function (t) { spy.observe(t); });
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
