/* Behavioral Science Skills: client script. No dependencies.
   Theme (follows the system until the reader picks), mobile menu, copy buttons,
   tabs (install options, and the file tabs on skill pages), the home page's
   hero demo and stage flow chart, workflow graphs (Workflows pages and home
   tiles), catalog search and filters with URL sync, TOC scroll-spy, the propose
   form (prefilled GitHub issue), and the upload form (/api/submit).
   The skill map is in map.js; the workflow tray and builder are in workflow.js. */
(function () {
  "use strict";

  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };
  var reduceMotion = !!(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
  var root = document.documentElement;

  /* ---------- analytics hook ----------
     Does nothing until an analytics provider is chosen. Its adapter sets
     window.besciAnalytics = function (name, props) { ... }. Event names are
     listed in docs/analytics.md. */
  function track(name, props) {
    try { if (typeof window.besciAnalytics === "function") window.besciAnalytics(name, props || {}); } catch (e) { /* ignore */ }
  }
  window.besciTrack = track;

  /* ---------- theme: saved choice, else the system setting ----------
     Toggling to the theme the system already uses forgets the saved choice,
     so the page goes back to following the system. */
  var darkQuery = window.matchMedia ? window.matchMedia("(prefers-color-scheme: dark)") : null;
  var savedTheme = function () { try { var t = localStorage.getItem("theme"); return t === "light" || t === "dark" ? t : null; } catch (e) { return null; } };
  function applyTheme(t) {
    root.setAttribute("data-theme", t);
    var light = t === "light";
    $$(".theme-toggle").forEach(function (b) {
      b.setAttribute("aria-label", light ? "Switch to dark mode" : "Switch to light mode");
      b.setAttribute("title", light ? "Switch to dark mode" : "Switch to light mode");
    });
    if (window.__redrawMap) window.__redrawMap();
  }
  $$(".theme-toggle").forEach(function (b) {
    b.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "light" ? "dark" : "light";
      var system = darkQuery && darkQuery.matches ? "dark" : "light";
      try {
        if (next === system) localStorage.removeItem("theme"); else localStorage.setItem("theme", next);
      } catch (e) { /* storage unavailable */ }
      applyTheme(next);
    });
  });
  if (darkQuery) {
    var onSystem = function (e) { if (!savedTheme()) applyTheme(e.matches ? "dark" : "light"); };
    if (darkQuery.addEventListener) darkQuery.addEventListener("change", onSystem); else if (darkQuery.addListener) darkQuery.addListener(onSystem);
  }
  applyTheme(root.getAttribute("data-theme") === "dark" ? "dark" : "light");


  /* ---------- mobile menu ---------- */
  var menuBtn = $(".menu-btn"), nav = $(".site-nav");
  if (menuBtn && nav) {
    menuBtn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && nav.classList.contains("open")) { nav.classList.remove("open"); menuBtn.setAttribute("aria-expanded", "false"); } });
  }

  /* ---------- copy buttons (delegated, so buttons added later work too) ---------- */
  function fallbackCopy(text) {
    var ta = document.createElement("textarea");
    ta.value = text; ta.setAttribute("readonly", ""); ta.style.position = "absolute"; ta.style.left = "-9999px";
    document.body.appendChild(ta); ta.select();
    try { document.execCommand("copy"); } catch (e) { /* ignore */ }
    document.body.removeChild(ta);
  }
  function copyText(text, done) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, function () { fallbackCopy(text); done(); });
    } else { fallbackCopy(text); done(); }
  }
  window.__copyText = copyText;
  document.addEventListener("click", function (e) {
    var btn = e.target.closest ? e.target.closest(".copy") : null;
    if (!btn) return;
    var text = btn.getAttribute("data-copy") || "";
    var label = $(".copy-label", btn);
    copyText(text, function () {
      btn.setAttribute("data-copied", "1");
      var old = label ? label.textContent : "";
      if (label) label.textContent = "Copied";
      setTimeout(function () { btn.removeAttribute("data-copied"); if (label) label.textContent = old; }, 1600);
    });
  });


  /* ---------- tabs: install options, and the file tabs on skill pages ----------
     A [data-tabs] box owns only the tabs whose nearest [data-tabs] is itself, so the
     install tabs inside a skill page's Skill tab stay separate. Most boxes remember
     the choice in localStorage; data-tabs-url="tab" keeps it in ?tab= instead, so a
     link can open a given tab. Elements with data-tab-for="<tab>" show only with that
     tab (the skill page's per-tab "On this page" lists). A #hash pointing inside a
     hidden panel opens that panel first. */
  $$("[data-tabs]").forEach(function (box) {
    var key = box.getAttribute("data-tabs") || "tabs";
    var urlParam = box.getAttribute("data-tabs-url");
    var own = function (el) { return el.closest("[data-tabs]") === box; };
    var tabs = $$("[role=tab]", box).filter(own);
    var panels = tabs.map(function (t) { return document.getElementById(t.getAttribute("aria-controls")); });
    var followers = $$("[data-tab-for]", box).filter(own);
    var current = -1;
    var nameOf = function (i) { return tabs[i].getAttribute("data-tab") || String(i); };
    function select(i, focus, fromLoad) {
      tabs.forEach(function (t, j) {
        var on = i === j;
        t.setAttribute("aria-selected", on ? "true" : "false");
        t.tabIndex = on ? 0 : -1;
        if (panels[j]) panels[j].hidden = !on;
      });
      var name = nameOf(i);
      followers.forEach(function (el) { el.hidden = el.getAttribute("data-tab-for") !== name; });
      if (focus) tabs[i].focus();
      // On a narrow screen the tab strip scrolls sideways; keep the chosen tab in view.
      var strip = tabs[i].parentElement;
      if (strip.scrollWidth > strip.clientWidth) {
        var left = tabs[i].offsetLeft - strip.offsetLeft, right = left + tabs[i].offsetWidth;
        if (left < strip.scrollLeft || right > strip.scrollLeft + strip.clientWidth) strip.scrollLeft = left - 24;
      }
      if (urlParam) {
        if (!fromLoad) {
          var params = new URLSearchParams(location.search);
          if (i === 0) params.delete(urlParam); else params.set(urlParam, name);
          var qs = params.toString();
          history.replaceState(null, "", location.pathname + (qs ? "?" + qs : ""));
          // Switching tabs further down the page starts the new tab at its top.
          if (box.getBoundingClientRect().top < 0) box.scrollIntoView({ block: "start" });
        }
      } else {
        try { localStorage.setItem("tab:" + key, name); } catch (e) { /* ignore */ }
      }
      if (i !== current && !fromLoad) track("tab_view", { box: key, tab: name });
      current = i;
    }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { select(i, false); });
      t.addEventListener("keydown", function (e) {
        if (e.key === "ArrowRight") { e.preventDefault(); select((i + 1) % tabs.length, true); }
        if (e.key === "ArrowLeft") { e.preventDefault(); select((i - 1 + tabs.length) % tabs.length, true); }
      });
    });
    var indexOf = function (name) {
      var idx = -1;
      tabs.forEach(function (t, i) { if (t.getAttribute("data-tab") === name) idx = i; });
      return idx;
    };
    var panelForHash = function () {
      var id = decodeURIComponent(location.hash.slice(1));
      var el = id && document.getElementById(id);
      if (!el) return -1;
      var idx = -1;
      panels.forEach(function (p, j) { if (p && p.contains(el)) idx = j; });
      return idx;
    };
    var saved = null;
    if (urlParam) saved = new URLSearchParams(location.search).get(urlParam);
    else { try { saved = localStorage.getItem("tab:" + key); } catch (e) { /* ignore */ } }
    var fromHash = urlParam ? panelForHash() : -1;
    var idx = fromHash >= 0 ? fromHash : indexOf(saved);
    select(idx >= 0 ? idx : 0, false, true);
    box.classList.add("is-ready");
    if (fromHash >= 0 && saved !== null && saved !== nameOf(fromHash)) {
      var fixed = new URLSearchParams(location.search);
      if (fromHash === 0) fixed.delete(urlParam); else fixed.set(urlParam, nameOf(fromHash));
      var fqs = fixed.toString();
      history.replaceState(null, "", location.pathname + (fqs ? "?" + fqs : "") + location.hash);
    }
    if (fromHash > 0) {
      var target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
      if (target) target.scrollIntoView();
    }
    if (urlParam) {
      // In-page links to a part of another tab (e.g. a test case, a reference file).
      window.addEventListener("hashchange", function () {
        var j = panelForHash();
        if (j < 0 || j === current) return;
        select(j, false, true);
        var params = new URLSearchParams(location.search);
        if (j === 0) params.delete(urlParam); else params.set(urlParam, nameOf(j));
        var qs = params.toString();
        history.replaceState(null, "", location.pathname + (qs ? "?" + qs : "") + location.hash);
        var el = document.getElementById(decodeURIComponent(location.hash.slice(1)));
        if (el) el.scrollIntoView();
      });
    }
  });

  /* ---------- old links: /?stage=... moved to /skills/, and the map moved to /map/ ---------- */
  if (document.body.classList.contains("page-index") && /[?&](q|stage|type|org|status|tag|view)=/.test(location.search)) {
    location.replace("/skills/" + location.search + location.hash);
    return;
  }
  if (document.body.classList.contains("page-catalog") && /[?&]view=map/.test(location.search)) {
    location.replace("/map/");
    return;
  }


  /* ---------- home: hero demo, a scripted conversation revealed step by step ----------
     The whole transcript is in the HTML. Steps are marked data-step="type|tool|say|rows|note";
     tool steps with data-wf advance the workflow rail. */
  var demoBox = $("[data-demo]");
  if (demoBox) {
    var dTabs = $$("[data-demo-tab]", demoBox);
    var dPanels = $$("[data-demo-panel]", demoBox);
    var dLinks = $$("[data-demo-for]", demoBox);
    var replayBtn = $(".demo-replay", demoBox);
    var players = {}, current = null, demoVisible = true;

    var wrapWords = function (el) {
      var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null), nodes = [], n, out = [];
      while ((n = walker.nextNode())) if (/\S/.test(n.nodeValue)) nodes.push(n);
      nodes.forEach(function (t) {
        var frag = document.createDocumentFragment();
        t.nodeValue.split(/(\s+)/).forEach(function (part) {
          if (!part) return;
          if (!/\S/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
          var w = document.createElement("span"); w.className = "w"; w.textContent = part;
          frag.appendChild(w); out.push(w);
        });
        t.parentNode.replaceChild(frag, t);
      });
      return out;
    };

    var makePlayer = function (panel) {
      var body = $(".demo-body", panel);
      var steps = $$("[data-step]", body);
      var rail = $$(".wf-rail li", panel);
      var acts = [], pos = 0, timer = null, playing = false, paused = false, follow = true;
      var self = { played: false };
      var setRail = function (n) {
        rail.forEach(function (li, j) { li.classList.toggle("is-done", j < n); li.classList.toggle("is-active", j === n); });
      };
      var add = function (fn, d) { acts.push({ fn: fn, d: d }); };

      steps.forEach(function (st) {
        var kind = st.getAttribute("data-step"), wf = st.getAttribute("data-wf");
        var reveal = function () { st.classList.remove("is-pending"); if (wf !== null) setRail(parseInt(wf, 10)); };
        if (kind === "type") {
          var t = $(".t-text", st), full = t.textContent;
          st._full = full;
          var per = Math.max(10, Math.min(28, 1500 / full.length));
          add(reveal, 150);
          for (var c = 1; c <= full.length; c++) add((function (k) { return function () { t.textContent = full.slice(0, k); }; })(c), per);
          add(function () { st.classList.add("is-sent"); }, 550);
        } else if (kind === "tool") {
          add(reveal, 800);
          add(function () { st.classList.add("is-done"); }, 350);
        } else if (kind === "say") {
          st._words = wrapWords(st);
          add(reveal, 60);
          st._words.forEach(function (w) { add(function () { w.classList.add("on"); }, 22); });
          add(function () {}, 450);
        } else if (kind === "rows") {
          add(reveal, 120);
          $$("[data-row]", st).forEach(function (r) { add(function () { r.classList.add("on"); }, 180); });
          add(function () {}, 450);
        } else {
          add(reveal, 750);
        }
      });
      add(function () { setRail(rail.length); }, 0);

      var reset = function () {
        steps.forEach(function (st) {
          st.classList.add("is-pending");
          st.classList.remove("is-sent", "is-done");
          if (st._full !== undefined) $(".t-text", st).textContent = "";
          (st._words || []).forEach(function (w) { w.classList.remove("on"); });
          $$("[data-row]", st).forEach(function (r) { r.classList.remove("on"); });
        });
        setRail(-1);
        body.scrollTop = 0; pos = 0; follow = true;
      };
      var tick = function () {
        if (!playing) return;
        if (pos >= acts.length) { playing = false; return; }
        var a = acts[pos++];
        a.fn();
        if (follow) body.scrollTop = body.scrollHeight;
        timer = setTimeout(tick, a.d);
      };
      self.play = function () { clearTimeout(timer); reset(); playing = true; paused = false; self.played = true; timer = setTimeout(tick, 500); };
      self.pause = function () { if (playing) { clearTimeout(timer); playing = false; paused = true; } };
      self.resume = function () { if (paused) { paused = false; playing = true; tick(); } };

      // Stop following the newest line once the reader scrolls up; follow again at the bottom.
      var userScroll = function () { setTimeout(function () { follow = body.scrollHeight - body.scrollTop - body.clientHeight < 48; }, 80); };
      body.addEventListener("wheel", userScroll, { passive: true });
      body.addEventListener("touchmove", userScroll, { passive: true });
      body.addEventListener("keydown", userScroll);
      reset();
      return self;
    };

    var selectDemo = function (name, focus) {
      dTabs.forEach(function (t) {
        var on = t.getAttribute("data-demo-tab") === name;
        t.setAttribute("aria-selected", on ? "true" : "false");
        t.tabIndex = on ? 0 : -1;
        if (on && focus) t.focus();
      });
      dPanels.forEach(function (p) { p.hidden = p.getAttribute("data-demo-panel") !== name; });
      dLinks.forEach(function (a) { a.hidden = a.getAttribute("data-demo-for") !== name; });
      if (reduceMotion) return;
      if (current && current !== players[name]) current.pause();
      current = players[name];
      if (!current.played) current.play(); else if (demoVisible && !document.hidden) current.resume();
    };

    if (!reduceMotion) {
      demoBox.classList.add("is-anim");
      dPanels.forEach(function (p) { players[p.getAttribute("data-demo-panel")] = makePlayer(p); });
      if (replayBtn) {
        replayBtn.hidden = false;
        replayBtn.addEventListener("click", function () { if (current) current.play(); });
      }
      if ("IntersectionObserver" in window) {
        new IntersectionObserver(function (es) {
          demoVisible = es[0].isIntersecting;
          if (current) { if (demoVisible) current.resume(); else current.pause(); }
        }, { threshold: 0.15 }).observe(demoBox);
      }
      document.addEventListener("visibilitychange", function () {
        if (!current) return;
        if (document.hidden) current.pause(); else if (demoVisible) current.resume();
      });
    }
    dTabs.forEach(function (t, i) {
      t.addEventListener("click", function () { selectDemo(t.getAttribute("data-demo-tab"), false); });
      t.addEventListener("keydown", function (e) {
        var j = e.key === "ArrowRight" ? (i + 1) % dTabs.length : e.key === "ArrowLeft" ? (i - 1 + dTabs.length) % dTabs.length : -1;
        if (j >= 0) { e.preventDefault(); selectDemo(dTabs[j].getAttribute("data-demo-tab"), true); }
      });
    });
    selectDemo(dTabs.length ? dTabs[0].getAttribute("data-demo-tab") : "skill", false);
  }

  /* ---------- home: stage flow chart ----------
     A slow tour lights each stage in turn; hovering or focusing a stage takes over.
     Every node is a plain link to the catalog filtered by its stage. */
  var flow = $("[data-flow]");
  if (flow) {
    var fSteps = $$(".flow-step", flow), fPanels = $$(".flow-panel", flow);
    var fActive = 0, fTimer = null, fHold = false, fStarted = false;
    var fSet = function (i) {
      fActive = i;
      fSteps.forEach(function (s, j) { s.classList.toggle("is-active", j === i); s.classList.toggle("is-done", j < i); });
      fPanels.forEach(function (p, j) { p.hidden = j !== i; });
    };
    var fNext = function () {
      clearTimeout(fTimer);
      if (!fHold && !document.hidden) fSet(fActive >= fSteps.length - 1 ? 0 : fActive + 1);
      fTimer = setTimeout(fNext, 4200);
    };
    fSet(0);
    $$(".flow-node", flow).forEach(function (a) {
      var idx = parseInt(a.getAttribute("data-idx"), 10);
      var take = function () { fHold = true; fSet(idx); };
      a.addEventListener("mouseenter", take);
      a.addEventListener("focus", take);
    });
    flow.addEventListener("mouseleave", function () { fHold = false; });
    flow.addEventListener("focusout", function (e) { if (!flow.contains(e.relatedTarget)) fHold = false; });
    if (!reduceMotion && "IntersectionObserver" in window) {
      flow.classList.add("is-js");
      new IntersectionObserver(function (es) {
        if (!es[0].isIntersecting) return;
        flow.classList.add("in-view");
        if (!fStarted) { fStarted = true; fTimer = setTimeout(fNext, 3200); }
      }, { threshold: 0.3 }).observe(flow);
    }
  }


  /* ---------- workflow graphs: Workflows pages and the home tiles ----------
     Steps sit in a grid built by build_site.py; each lists the steps it runs
     after in data-after. Lines are drawn from ring to ring and redrawn on resize.
     The first time a graph scrolls into view, a highlight runs through the steps
     once and each step's incoming lines draw in. Pointing at a step (full graphs)
     shows what it passes on and where the team decides. */
  var svgNS = "http://www.w3.org/2000/svg";
  var escHtml = function (s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };
  var graphs = $$("[data-wfg]");
  graphs.forEach(function (g, gi) {
    var compact = g.classList.contains("wfg-compact");
    var nodes = $$(".wfg-node", g), byId = {};
    nodes.forEach(function (n) { byId[n.getAttribute("data-step")] = n; });
    var edges = [];
    nodes.forEach(function (n) {
      (n.getAttribute("data-after") || "").split(" ").forEach(function (f) {
        if (byId[f]) edges.push({ from: byId[f], to: n, optional: n.hasAttribute("data-optional") });
      });
    });
    var svg = document.createElementNS(svgNS, "svg");
    svg.setAttribute("class", "wfg-svg");
    svg.setAttribute("aria-hidden", "true");
    var mk = function (id, cls) {
      var m = document.createElementNS(svgNS, "marker");
      m.setAttribute("id", id); m.setAttribute("class", cls);
      m.setAttribute("viewBox", "0 0 10 10"); m.setAttribute("refX", "9"); m.setAttribute("refY", "5");
      m.setAttribute("markerWidth", "6"); m.setAttribute("markerHeight", "6"); m.setAttribute("orient", "auto");
      m.setAttribute("markerUnits", "userSpaceOnUse");
      var p = document.createElementNS(svgNS, "path"); p.setAttribute("d", "M0,1 L9,5 L0,9 z");
      m.appendChild(p);
      return m;
    };
    var arrow = "wfg-a" + gi, arrowHot = "wfg-ah" + gi;
    if (!compact) {
      var defs = document.createElementNS(svgNS, "defs");
      defs.appendChild(mk(arrow, "wfg-arrow")); defs.appendChild(mk(arrowHot, "wfg-arrow-hot"));
      svg.appendChild(defs);
    }
    edges.forEach(function (e) {
      e.path = document.createElementNS(svgNS, "path");
      e.path.setAttribute("class", "is-pending" + (e.optional ? " is-opt" : ""));
      svg.appendChild(e.path);
    });
    g.insertBefore(svg, g.firstChild);

    // Geometry: ring to ring, as a curve; across in wide layouts, down in narrow
    // ones (the CSS stacks full graphs below 720px). The svg is sized in pixels
    // with no viewBox, so a caption that grows the box does not rescale the lines.
    var ringOf = function (n) { return $(".wfg-ring", n); };
    var narrow = window.matchMedia ? window.matchMedia("(max-width: 720px)") : null;
    function draw() {
      var base = g.getBoundingClientRect();
      if (!base.width) return;
      svg.setAttribute("width", base.width); svg.setAttribute("height", base.height);
      var stacked = !compact && narrow && narrow.matches;
      edges.forEach(function (e) {
        var a = ringOf(e.from).getBoundingClientRect(), b = ringOf(e.to).getBoundingClientRect();
        var gap = compact ? 2 : 4, d;
        if (!stacked && b.left >= a.right - 1) {
          var x1 = a.right - base.left + gap, y1 = a.top - base.top + a.height / 2;
          var x2 = b.left - base.left - gap, y2 = b.top - base.top + b.height / 2, k = (x2 - x1) / 2;
          d = "M" + x1 + "," + y1 + " C" + (x1 + k) + "," + y1 + " " + (x2 - k) + "," + y2 + " " + x2 + "," + y2;
        } else {
          var u1 = a.left - base.left + a.width / 2, v1 = a.bottom - base.top + gap;
          var u2 = b.left - base.left + b.width / 2, v2 = b.top - base.top - gap, m = (v2 - v1) / 2;
          d = "M" + u1 + "," + v1 + " C" + u1 + "," + (v1 + m) + " " + u2 + "," + (v2 - m) + " " + u2 + "," + v2;
        }
        e.path.setAttribute("d", d);
      });
      paint();
    }

    // State: which steps have lit up, which step the reader is pointing at.
    var hot = null;
    function paint() {
      g.classList.toggle("is-focus", !!hot);
      nodes.forEach(function (n) {
        var near = !!hot && (n === hot || edges.some(function (e) { return (e.from === hot && e.to === n) || (e.to === hot && e.from === n); }));
        n.classList.toggle("is-near", near);
        n.classList.toggle("is-hot", n === hot);
      });
      edges.forEach(function (e) {
        var h = !!hot && (e.from === hot || e.to === hot);
        e.path.classList.toggle("is-hot", h);
        if (!compact && e.shown) e.path.setAttribute("marker-end", "url(#" + (h ? arrowHot : arrow) + ")");
      });
    }
    function show(e, animate) {
      var p = e.path;
      if (!animate || e.optional) {
        p.classList.remove("is-pending");
        e.shown = true; paint();
        return;
      }
      var len = p.getTotalLength();
      p.style.transition = "none";
      p.style.strokeDasharray = len; p.style.strokeDashoffset = len;
      p.getBoundingClientRect();
      p.classList.remove("is-pending");
      p.style.transition = "";
      p.style.strokeDashoffset = "0";
      setTimeout(function () { p.style.strokeDasharray = ""; p.style.strokeDashoffset = ""; e.shown = true; paint(); }, 520);
    }
    function play() {
      var gapMs = compact ? 170 : 260;
      nodes.forEach(function (n, i) {
        setTimeout(function () {
          var incoming = edges.filter(function (e) { return e.to === n; });
          incoming.forEach(function (e) { show(e, true); });
          setTimeout(function () {
            nodes.forEach(function (m) { m.classList.remove("is-active"); });
            n.classList.add("is-active", "is-done");
            if (i === nodes.length - 1) setTimeout(function () { n.classList.remove("is-active"); }, 900);
          }, incoming.length ? 300 : 0);
        }, i * gapMs);
      });
    }
    function finish() {
      nodes.forEach(function (n) { n.classList.add("is-done"); });
      edges.forEach(function (e) { show(e, false); });
    }

    draw();
    if (reduceMotion || !("IntersectionObserver" in window)) {
      finish();
    } else {
      g.classList.add("is-js");
      var io = new IntersectionObserver(function (es) {
        if (!es[0].isIntersecting) return;
        io.disconnect();
        draw();
        play();
      }, { threshold: 0.4 });
      io.observe(g);
    }

    // Pointing at a step (full graphs only; compact ones sit inside a link).
    var cap = $(".wfg-cap", g);
    if (compact || !cap) { g._draw = draw; return; }
    var hint = '<p class="wfg-hint">' + escHtml(cap.getAttribute("data-hint")) + "</p>";
    var row = function (k, v) { return v ? "<div><dt>" + k + "</dt><dd>" + escHtml(v) + "</dd></div>" : ""; };
    function point(n) {
      if (n === hot) return;
      hot = n;
      paint();
      if (!n) { cap.innerHTML = hint; return; }
      cap.innerHTML = '<p class="wfg-cap-t"><span>Step ' + escHtml(n.getAttribute("data-step")) + "</span>" + escHtml(n.getAttribute("data-title")) +
        (n.hasAttribute("data-optional") ? '<span class="wfg-opt">Optional</span>' : "") + "</p><dl>" +
        row("Runs one of", n.getAttribute("data-alts")) + row("Passes on", n.getAttribute("data-carries")) + row("You decide", n.getAttribute("data-decide")) + "</dl>";
    }
    g.addEventListener("mouseover", function (e) { var n = e.target.closest(".wfg-node"); if (n) point(n); });
    g.addEventListener("mouseleave", function () { if (!g.contains(document.activeElement)) point(null); });
    g.addEventListener("focusin", function (e) { var n = e.target.closest(".wfg-node"); if (n) point(n); });
    g.addEventListener("focusout", function (e) { if (!g.contains(e.relatedTarget)) point(null); });
    g._draw = draw;
  });
  if (graphs.length) {
    var redrawGraphs = function () { graphs.forEach(function (g) { if (g._draw) g._draw(); }); };
    var gt;
    window.addEventListener("resize", function () { clearTimeout(gt); gt = setTimeout(redrawGraphs, 120); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(redrawGraphs);
  }


  /* ---------- catalog: search, stage chips, filters ----------
     With nothing filtered, cards sit under stage headings; any filter or search
     flattens the grid. */
  var grid = $("#grid");
  if (grid) {
    var cards = $$(".card", grid);
    var q = $("#q");
    var fields = { stage: $("#f-stage"), type: $("#f-type"), org: $("#f-org"), status: $("#f-status"), tag: $("#f-tag") };
    var count = $("#f-count");
    var noResults = $("#no-results");
    var stageBtns = $$(".stage-chip");
    var stageDesc = $("#stage-desc");
    var moreFilters = $(".more-filters");

    function readUrl() {
      var p = new URLSearchParams(location.search);
      if (q) q.value = p.get("q") || "";
      Object.keys(fields).forEach(function (k) { if (fields[k]) fields[k].value = p.get(k) || ""; });
      if (moreFilters && ["type", "org", "status", "tag"].some(function (k) { return p.get(k); })) moreFilters.open = true;
    }
    function writeUrl() {
      var p = new URLSearchParams();
      if (q && q.value) p.set("q", q.value);
      Object.keys(fields).forEach(function (k) { if (fields[k] && fields[k].value) p.set(k, fields[k].value); });
      var qs = p.toString();
      history.replaceState(null, "", location.pathname + (qs ? "?" + qs : "") + location.hash);
    }
    function showStageDesc(b) {
      if (!stageDesc) return;
      if (b && b.getAttribute("data-label")) {
        stageDesc.innerHTML = "";
        var bold = document.createElement("b"); bold.textContent = b.getAttribute("data-label") + ": ";
        stageDesc.appendChild(bold);
        stageDesc.appendChild(document.createTextNode(b.getAttribute("data-desc") || ""));
      } else {
        stageDesc.textContent = stageDesc.getAttribute("data-default") || "";
      }
    }
    function syncStageChips() {
      var val = fields.stage ? fields.stage.value : "";
      stageBtns.forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-stage") === val ? "true" : "false"); });
      showStageDesc(val ? stageBtns.filter(function (b) { return b.getAttribute("data-stage") === val; })[0] : null);
    }
    function apply() {
      var text = (q && q.value || "").trim().toLowerCase();
      var terms = text ? text.split(/\s+/) : [];
      var filtered = !!terms.length;
      var shown = 0;
      Object.keys(fields).forEach(function (k) { if (fields[k] && fields[k].value) filtered = true; });
      cards.forEach(function (c) {
        var ok = true;
        Object.keys(fields).forEach(function (k) {
          var val = fields[k] && fields[k].value;
          if (!val) return;
          if (k === "tag") {
            if ((c.getAttribute("data-tags") || "").split(" ").indexOf(val) === -1) ok = false;
          } else if (c.getAttribute("data-" + k) !== val) ok = false;
        });
        if (ok && terms.length) {
          var hay = c.getAttribute("data-search") || "";
          ok = terms.every(function (t) { return hay.indexOf(t) !== -1; });
        }
        c.hidden = !ok;
        if (ok) shown++;
      });
      grid.classList.toggle("is-filtered", filtered);
      if (count) count.textContent = shown === cards.length ? cards.length + " skills" : shown + " of " + cards.length;
      if (noResults) noResults.hidden = shown !== 0;
      syncStageChips();
      writeUrl();
    }

    // Stage headings stick under the header. Mark the stuck one, which sits just
    // above the observer's top edge, so it gets its backdrop.
    if ("IntersectionObserver" in window) {
      var headerH = parseFloat(getComputedStyle(root).getPropertyValue("--header-h")) || 64;
      var stuck = new IntersectionObserver(function (es) {
        es.forEach(function (en) { en.target.classList.toggle("is-stuck", en.intersectionRatio < 1 && en.boundingClientRect.top < headerH + 1); });
      }, { rootMargin: "-" + (headerH + 1) + "px 0px 0px 0px", threshold: [0, 1] });
      $$(".group-head", grid).forEach(function (h) { stuck.observe(h); });
    }

    readUrl();
    apply();
    if (q) q.addEventListener("input", apply);
    Object.keys(fields).forEach(function (k) { if (fields[k] && fields[k].tagName === "SELECT") fields[k].addEventListener("change", apply); });
    stageBtns.forEach(function (b) {
      b.addEventListener("click", function () {
        var val = b.getAttribute("data-stage");
        if (fields.stage) fields.stage.value = val && fields.stage.value !== val ? val : "";
        apply();
      });
      b.addEventListener("mouseenter", function () { if (fields.stage && !fields.stage.value) showStageDesc(b); });
      b.addEventListener("mouseleave", function () { syncStageChips(); });
    });
    var clear = function () {
      if (q) q.value = "";
      Object.keys(fields).forEach(function (k) { if (fields[k]) fields[k].value = ""; });
      apply();
    };
    var c1 = $("#f-clear"), c2 = $("#f-clear-2");
    if (c1) c1.addEventListener("click", clear);
    if (c2) c2.addEventListener("click", clear);
    document.addEventListener("click", function (e) { if (moreFilters && moreFilters.open && !moreFilters.contains(e.target)) moreFilters.open = false; });
    document.addEventListener("keydown", function (e) {
      var typing = /input|textarea|select/i.test(document.activeElement.tagName);
      if (e.key === "/" && q && !typing) { e.preventDefault(); q.focus(); q.select(); }
      if (e.key === "Escape" && q && document.activeElement === q) { q.value = ""; apply(); q.blur(); }
      if (e.key === "Escape" && moreFilters && moreFilters.open) moreFilters.open = false;
    });
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
