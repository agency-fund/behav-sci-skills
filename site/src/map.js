/* Behavioral Science Skills: the skill map (/map/). No dependencies.
   Columns are the seven stages plus the meta-skills. An arrow from A to B means
   A produces something B takes in, as the skills declare in produces/consumes.
   Hover previews a skill's links. Click pins it: the highlight stays put, a panel
   lists what it feeds and what feeds it, and ?skill=<name> makes it linkable.
   Esc, a click on empty map, or "Show full map" unpins. */
(function () {
  "use strict";

  var mapEl = document.getElementById("map");
  var panel = document.getElementById("map-panel");
  if (!mapEl || !panel) return;
  var wf = window.besciWorkflow;
  var search = document.getElementById("map-q");
  var live = document.getElementById("wf-live");
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };
  var ic = function (name, cls) { return '<svg' + (cls ? ' class="' + cls + '"' : "") + ' viewBox="0 0 256 256" fill="currentColor" aria-hidden="true"><use href="#i-' + name + '"></use></svg>'; };
  var svgNS = "http://www.w3.org/2000/svg";

  var load = wf ? wf.data() : fetch("/data/skills.json").then(function (r) { return r.json(); });
  load.then(function (data) {
    if (!data || !data.skills) { mapEl.innerHTML = '<p class="map-loading">The map could not load. Try the <a href="/skills/">Skills page</a>.</p>'; return; }
    build(data);
  });

  function build(data) {
    var byName = {}, stageLabel = {}, io = {};
    data.skills.forEach(function (s) { byName[s.name] = s; });
    data.stages.forEach(function (s) { stageLabel[s.id] = s.label; });
    data.io_types.forEach(function (t) { io[t.id] = t; });
    var colOf = function (s) { return s.type === "meta" || !s.stage || s.stage === "other" ? "other" : s.stage; };
    var ioLabel = function (t) { return io[t] ? io[t].label : t.replace(/-/g, " "); };

    // Edges: producer -> consumer, one per pair, remembering the artifacts passed.
    var producers = {};
    data.skills.forEach(function (s) { s.produces.forEach(function (t) { (producers[t] = producers[t] || []).push(s.name); }); });
    var edgeMap = {}, edges = [];
    data.skills.forEach(function (c) {
      c.consumes.forEach(function (t) {
        (producers[t] || []).forEach(function (p) {
          if (p === c.name) return;
          var k = p + ">" + c.name;
          if (!edgeMap[k]) { edgeMap[k] = { from: p, to: c.name, via: [] }; edges.push(edgeMap[k]); }
          edgeMap[k].via.push(t);
        });
      });
    });
    var outOf = {}, inTo = {};
    edges.forEach(function (e) { (outOf[e.from] = outOf[e.from] || []).push(e); (inTo[e.to] = inTo[e.to] || []).push(e); });

    // Columns
    var cols = data.stages.filter(function (s) { return s.id !== "other"; }).map(function (s) { return { id: s.id, label: s.label }; });
    cols.push({ id: "other", label: "Meta-skills" });
    var inner = document.createElement("div");
    inner.className = "map-inner";
    var svg = document.createElementNS(svgNS, "svg");
    svg.setAttribute("class", "map-svg");
    svg.setAttribute("aria-hidden", "true");
    inner.appendChild(svg);
    var nodes = {};
    cols.forEach(function (col) {
      var members = data.skills.filter(function (s) { return colOf(s) === col.id; });
      if (!members.length) return;
      var c = document.createElement("div");
      c.className = "map-col";
      c.setAttribute("data-stage", col.id);
      c.innerHTML = '<h2 class="map-col-head">' + ic("st-" + col.id) + esc(col.label) + "<span>" + members.length + "</span></h2>";
      members.forEach(function (s) {
        var b = document.createElement("button");
        b.type = "button";
        b.className = "map-node";
        b.setAttribute("data-id", s.name);
        b.title = s.name;
        b.innerHTML = "<b>" + esc(s.title) + "</b>";
        c.appendChild(b);
        nodes[s.name] = b;
      });
      inner.appendChild(c);
    });
    mapEl.innerHTML = "";
    mapEl.appendChild(inner);

    // Drawing
    var paths = [];
    function marker(id, cls) {
      var m = document.createElementNS(svgNS, "marker");
      m.setAttribute("id", id); m.setAttribute("class", cls);
      m.setAttribute("viewBox", "0 0 10 10"); m.setAttribute("refX", "9"); m.setAttribute("refY", "5");
      m.setAttribute("markerWidth", "7"); m.setAttribute("markerHeight", "7"); m.setAttribute("orient", "auto-start-reverse");
      m.setAttribute("markerUnits", "userSpaceOnUse");
      var p = document.createElementNS(svgNS, "path"); p.setAttribute("d", "M0,1 L9,5 L0,9 z");
      m.appendChild(p);
      return m;
    }
    function draw() {
      while (svg.firstChild) svg.removeChild(svg.firstChild);
      var defs = document.createElementNS(svgNS, "defs");
      defs.appendChild(marker("arrow", "arrow"));
      defs.appendChild(marker("arrow-hot", "arrow-hot"));
      svg.appendChild(defs);
      paths = [];
      var base = inner.getBoundingClientRect();
      svg.setAttribute("viewBox", "0 0 " + inner.scrollWidth + " " + inner.scrollHeight);
      svg.setAttribute("width", inner.scrollWidth); svg.setAttribute("height", inner.scrollHeight);
      edges.forEach(function (e) {
        var a = nodes[e.from], b = nodes[e.to];
        if (!a || !b) return;
        var ra = a.getBoundingClientRect(), rb = b.getBoundingClientRect();
        var y1 = ra.top - base.top + ra.height / 2, y2 = rb.top - base.top + rb.height / 2, x1, x2, d;
        if (rb.left >= ra.right - 2) {
          x1 = ra.right - base.left; x2 = rb.left - base.left - 1;
          var dx = Math.max(24, (x2 - x1) / 2);
          d = "M" + x1 + "," + y1 + " C" + (x1 + dx) + "," + y1 + " " + (x2 - dx) + "," + y2 + " " + x2 + "," + y2;
        } else {
          // Same column or backward: loop out on the left side.
          x1 = ra.left - base.left; x2 = rb.left - base.left - 1;
          d = "M" + x1 + "," + y1 + " C" + (x1 - 30) + "," + y1 + " " + (x2 - 30) + "," + y2 + " " + x2 + "," + y2;
        }
        var p = document.createElementNS(svgNS, "path");
        p.setAttribute("d", d);
        p.setAttribute("class", "edge");
        p.setAttribute("marker-end", "url(#arrow)");
        p._e = e;
        svg.appendChild(p);
        paths.push(p);
      });
      paint();
    }

    // State
    var hoverId = null, pinId = null;
    function paint() {
      var id = pinId || hoverId;
      mapEl.classList.toggle("is-focus", !!id);
      var on = {};
      if (id) { on[id] = true; (outOf[id] || []).forEach(function (e) { on[e.to] = true; }); (inTo[id] || []).forEach(function (e) { on[e.from] = true; }); }
      Object.keys(nodes).forEach(function (k) {
        nodes[k].classList.toggle("is-on", !!id && !!on[k]);
        nodes[k].classList.toggle("is-sel", !!pinId && k === pinId);
        nodes[k].setAttribute("aria-pressed", k === pinId ? "true" : "false");
      });
      var hot = [];
      paths.forEach(function (p) {
        var h = !!id && (p._e.from === id || p._e.to === id);
        p.classList.toggle("is-hot", h);
        p.setAttribute("marker-end", h ? "url(#arrow-hot)" : "url(#arrow)");
        if (h) hot.push(p);
      });
      hot.forEach(function (p) { svg.appendChild(p); }); // draw highlighted edges on top
    }
    function setUrl(name) {
      var p = new URLSearchParams(location.search);
      if (name) p.set("skill", name); else p.delete("skill");
      var qs = p.toString();
      history.replaceState(null, "", location.pathname + (qs ? "?" + qs : ""));
    }
    function say(text) { if (live) { live.textContent = ""; setTimeout(function () { live.textContent = text; }, 30); } }

    function pin(name, opts) {
      if (!byName[name]) return;
      pinId = name; hoverId = null;
      renderPanel(name);
      var wasOpen = document.body.classList.contains("panel-open");
      document.body.classList.add("panel-open");
      panel.hidden = false;
      panel.scrollTop = 0;
      if (!wasOpen) draw(); else paint();
      setUrl(name);
      if (opts && opts.scroll) reveal(nodes[name]);
      if (opts && opts.focus) nodes[name].focus({ preventScroll: true });
      say("Showing what connects to " + byName[name].title + ".");
    }
    // Bring a node into view: sideways inside the map, then the window if needed.
    // (scrollIntoView would also scroll the page's overflow-hidden body.)
    var smooth = !(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
    function reveal(n) {
      var mr = mapEl.getBoundingClientRect(), nr = n.getBoundingClientRect();
      var cover = document.body.classList.contains("panel-open") && window.innerWidth > 800 ? 420 : 0;
      var room = mr.width - cover;
      if (nr.left < mr.left || nr.right > mr.left + room) mapEl.scrollLeft += nr.left - mr.left - (room - nr.width) / 2;
      if (nr.top < 90 || nr.bottom > window.innerHeight - 110) window.scrollBy({ top: nr.top - window.innerHeight / 3, behavior: smooth ? "smooth" : "auto" });
    }
    function unpin() {
      if (!pinId) return;
      var was = pinId;
      pinId = null;
      panel.hidden = true;
      document.body.classList.remove("panel-open");
      draw();
      setUrl(null);
      if (nodes[was]) nodes[was].focus({ preventScroll: true });
      say("Showing the full map.");
    }

    function row(name) {
      var s = byName[name], st = colOf(s);
      return '<li class="mp-row"><button class="mp-go" type="button" data-pin="' + esc(name) + '" data-stage="' + esc(st) + '">' + ic("st-" + st, "stage-ic") +
        "<span>" + esc(s.title) + "</span></button>" +
        '<a class="icon-only" href="' + esc(s.url) + '" aria-label="Open ' + esc(s.title) + '">' + ic("arrow-right") + "</a>" +
        '<button class="icon-only" type="button" data-add="' + esc(name) + '"></button></li>';
    }
    function groups(list, key) {
      // Group linked skills by the artifact that passes between them.
      var by = {}, order = [];
      list.forEach(function (e) {
        e.via.forEach(function (t) {
          if (!by[t]) { by[t] = []; order.push(t); }
          var other = e[key];
          if (by[t].indexOf(other) === -1) by[t].push(other);
        });
      });
      return order.map(function (t) {
        return '<div class="mp-group"><p class="mp-io"><b>' + esc(ioLabel(t)) + "</b></p><ul class=\"mp-list\">" + by[t].map(row).join("") + "</ul></div>";
      }).join("");
    }
    function renderPanel(name) {
      var s = byName[name], st = colOf(s);
      var outs = outOf[name] || [], ins = inTo[name] || [];
      var produced = {};
      ins.forEach(function (e) { e.via.forEach(function (t) { produced[t] = true; }); });
      var supply = s.consumes.filter(function (t) { return !produced[t] && io[t] && io[t].user_suppliable; });
      var missing = s.consumes.filter(function (t) { return !produced[t] && !(io[t] && io[t].user_suppliable); });
      var html =
        '<div class="mp-top"><span class="mp-stage" data-stage="' + esc(st) + '">' + ic("st-" + st, "stage-ic") + esc(st === "other" ? "Meta-skill" : stageLabel[st] || st) + "</span>" +
        '<button class="mp-close" type="button">' + ic("x") + "Show full map</button></div>" +
        '<h2 id="mp-title">' + esc(s.title) + '</h2><p class="mp-name">' + esc(s.name) + "</p>" +
        '<p class="mp-what">' + esc(s.what_it_does) + "</p>" +
        '<div class="mp-actions"><a class="btn-secondary" href="' + esc(s.url) + '">Open skill page</a>' +
        '<button class="add-btn" type="button" data-add="' + esc(name) + '" data-label-off="Add to workflow"></button></div>';
      if (!outs.length && !ins.length && !supply.length) {
        html += '<section class="mp-sec"><p class="mp-none">This skill has no declared links yet.</p></section>';
      }
      if (outs.length) html += '<section class="mp-sec"><h3>Its output goes to</h3>' + groups(outs, "to") + "</section>";
      if (ins.length || missing.length) {
        html += '<section class="mp-sec"><h3>It takes input from</h3>' + groups(ins, "from") +
          missing.map(function (t) { return '<div class="mp-group"><p class="mp-io"><b>' + esc(ioLabel(t)) + '</b></p><p class="mp-none">No skill in the library produces this yet.</p></div>'; }).join("") + "</section>";
      }
      if (supply.length) {
        html += '<section class="mp-sec"><h3>You can supply</h3><p class="mp-supply">' + esc(supply.map(ioLabel).join(", ")) + "</p></section>";
      }
      panel.innerHTML = html;
      panel.setAttribute("aria-labelledby", "mp-title");
      if (wf) wf.refresh();
    }

    // Workflow step badges on nodes
    function badges() {
      var list = wf ? wf.list() : [];
      Object.keys(nodes).forEach(function (k) {
        var i = list.indexOf(k), b = nodes[k].querySelector(".wf-badge");
        if (i === -1) { if (b) b.remove(); return; }
        if (!b) { b = document.createElement("span"); b.className = "wf-badge"; nodes[k].appendChild(b); }
        b.textContent = String(i + 1);
        b.setAttribute("aria-label", "step " + (i + 1) + " in your workflow");
      });
    }
    if (wf) wf.onChange(badges);
    badges();

    // Events
    inner.addEventListener("mouseover", function (e) {
      var n = e.target.closest(".map-node");
      if (!n || pinId) return;
      hoverId = n.getAttribute("data-id"); paint();
    });
    inner.addEventListener("mouseout", function (e) {
      var n = e.target.closest(".map-node");
      if (!n || pinId) return;
      if (e.relatedTarget && n.contains(e.relatedTarget)) return;
      hoverId = null; paint();
    });
    inner.addEventListener("focusin", function (e) {
      var n = e.target.closest(".map-node");
      if (n && !pinId) { hoverId = n.getAttribute("data-id"); paint(); }
    });
    inner.addEventListener("focusout", function () { if (!pinId) { hoverId = null; paint(); } });
    mapEl.addEventListener("click", function (e) {
      var n = e.target.closest(".map-node");
      if (n) { var id = n.getAttribute("data-id"); if (id === pinId) unpin(); else pin(id); return; }
      if (pinId) unpin();
    });
    panel.addEventListener("click", function (e) {
      if (e.target.closest(".mp-close")) { unpin(); return; }
      var go = e.target.closest("[data-pin]");
      if (go) pin(go.getAttribute("data-pin"), { scroll: true });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key !== "Escape" || !pinId) return;
      if (document.activeElement === search) return;
      unpin();
    });
    if (search) {
      var runSearch = function () {
        var q = search.value.trim().toLowerCase();
        mapEl.classList.toggle("is-search", !!q);
        var matches = [];
        Object.keys(nodes).forEach(function (k) {
          var s = byName[k];
          var hit = !!q && (s.title.toLowerCase().indexOf(q) !== -1 || k.indexOf(q) !== -1);
          nodes[k].classList.toggle("is-match", hit);
          if (hit) matches.push(k);
        });
        return matches;
      };
      search.addEventListener("input", runSearch);
      search.addEventListener("keydown", function (e) {
        if (e.key === "Enter") { var m = runSearch(); if (m.length) { e.preventDefault(); pin(m[0], { scroll: true, focus: true }); } }
        if (e.key === "Escape") { search.value = ""; runSearch(); }
      });
    }

    draw();
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(draw);
    var rt;
    window.addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(draw, 120); });
    window.__redrawMap = draw;

    var start = new URLSearchParams(location.search).get("skill");
    if (start && byName[start]) pin(start, { scroll: true });
  }
})();
