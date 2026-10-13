/* Behavioral Science Skills: the reader's workflow. No dependencies.
   An ordered list of skill names in localStorage, shared by every page:
   Add buttons ([data-add]), the Workflows nav count, the bottom tray,
   "Open in builder" buttons ([data-load-workflow]), and the builder page
   at /workflows/build/. map.js uses window.besciWorkflow. */
(function () {
  "use strict";

  var KEY = "besci:workflow", NAME_KEY = "besci:workflow-name";
  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };
  var ic = function (name) { return '<svg viewBox="0 0 256 256" fill="currentColor" aria-hidden="true"><use href="#i-' + name + '"></use></svg>'; };

  /* ---------- store ---------- */
  var list = read(), listeners = [];
  function read() {
    try {
      var v = JSON.parse(localStorage.getItem(KEY) || "[]");
      return Array.isArray(v) ? v.filter(function (x) { return typeof x === "string"; }) : [];
    } catch (e) { return []; }
  }
  function save(next, message) {
    list = next.filter(function (n, i) { return next.indexOf(n) === i; });
    try { localStorage.setItem(KEY, JSON.stringify(list)); } catch (e) { /* storage unavailable */ }
    changed(message);
  }
  function changed(message) {
    listeners.forEach(function (fn) { fn(list); });
    if (message) announce(message);
  }
  window.addEventListener("storage", function (e) { if (e.key === KEY) { list = read(); changed(); } });

  var live = $("#wf-live");
  function announce(text) { if (live) { live.textContent = ""; setTimeout(function () { live.textContent = text; }, 30); } }

  /* ---------- skill data (titles, stages, hand-offs) ---------- */
  var dataPromise = null, data = null, byName = {};
  function loadData() {
    if (!dataPromise) {
      dataPromise = fetch("/data/skills.json").then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
        if (d && d.skills) { data = d; d.skills.forEach(function (s) { byName[s.name] = s; }); }
        return data;
      }).catch(function () { return null; });
    }
    return dataPromise;
  }
  var title = function (n) { return byName[n] ? byName[n].title : n; };

  var api = {
    list: function () { return list.slice(); },
    has: function (n) { return list.indexOf(n) !== -1; },
    add: function (n) { if (!api.has(n)) save(list.concat([n]), "Added " + title(n) + " as step " + (list.length + 1) + "."); },
    remove: function (n) { if (api.has(n)) save(list.filter(function (x) { return x !== n; }), "Removed " + title(n) + "."); },
    toggle: function (n) { if (api.has(n)) api.remove(n); else api.add(n); },
    move: function (from, to) {
      if (from === to || from < 0 || to < 0 || from >= list.length || to >= list.length) return;
      var next = list.slice(), item = next.splice(from, 1)[0];
      next.splice(to, 0, item);
      save(next, "Moved " + title(item) + " to step " + (to + 1) + ".");
    },
    set: function (names, message) { save(names.slice(), message); },
    clear: function () { save([], "Cleared your workflow."); },
    onChange: function (fn) { listeners.push(fn); },
    data: loadData,
    refresh: function () { syncButtons(); }
  };
  window.besciWorkflow = api;

  /* ---------- Add buttons and the nav count ---------- */
  function syncButtons() {
    $$("[data-add]").forEach(function (b) {
      var n = b.getAttribute("data-add"), i = list.indexOf(n), on = i !== -1;
      var label = b.getAttribute("data-label-off") || "Add";
      b.setAttribute("aria-pressed", on ? "true" : "false");
      b.setAttribute("aria-label", on ? "Remove " + title(n) + " from your workflow (step " + (i + 1) + ")" : "Add " + title(n) + " to your workflow");
      if (b.classList.contains("icon-only")) b.innerHTML = ic(on ? "check" : "plus");
      else b.innerHTML = ic(on ? "check" : "plus") + '<span class="add-label">' + (on ? "Step " + (i + 1) : esc(label)) + "</span>";
    });
    $$("[data-wf-count]").forEach(function (el) { el.textContent = String(list.length); el.hidden = !list.length; });
  }
  document.addEventListener("click", function (e) {
    var b = e.target.closest ? e.target.closest("[data-add]") : null;
    if (!b) return;
    e.preventDefault();
    api.toggle(b.getAttribute("data-add"));
  });
  api.onChange(syncButtons);

  /* ---------- "Open in builder" on workflow pages ---------- */
  document.addEventListener("click", function (e) {
    var b = e.target.closest ? e.target.closest("[data-load-workflow]") : null;
    if (!b) return;
    var names = (b.getAttribute("data-load-workflow") || "").split(",").filter(Boolean);
    if (!replaceOk(names)) return;
    api.set(names, "Loaded " + names.length + " skills.");
    location.href = "/workflows/build/";
  });
  function replaceOk(names) {
    if (!list.length || list.join(",") === names.join(",")) return true;
    return window.confirm("Replace your current workflow (" + list.length + " skill" + (list.length === 1 ? "" : "s") + ") with this one?");
  }

  /* ---------- reorderable rows, shared by the tray and the builder ----------
     Arrow buttons are the keyboard path; dragging the handle is the pointer path. */
  var pendingFocus = null;
  function rowControls(n, i, total) {
    var t = esc(title(n));
    return '<span class="step-ctl">' +
      '<button class="icon-only" type="button" data-move="-1" aria-label="Move ' + t + ' up"' + (i === 0 ? " disabled" : "") + ">" + ic("caret-up") + "</button>" +
      '<button class="icon-only" type="button" data-move="1" aria-label="Move ' + t + ' down"' + (i === total - 1 ? " disabled" : "") + ">" + ic("caret-down") + "</button>" +
      '<button class="icon-only" type="button" data-remove aria-label="Remove ' + t + '">' + ic("x") + "</button></span>";
  }
  function wireRows(container, rowSel) {
    container.addEventListener("click", function (e) {
      var btn = e.target.closest("[data-move],[data-remove]");
      if (!btn || !container.contains(btn)) return;
      var row = btn.closest(rowSel), n = row.getAttribute("data-name"), i = list.indexOf(n);
      if (btn.hasAttribute("data-remove")) {
        var next = row.nextElementSibling || row.previousElementSibling;
        pendingFocus = next ? { name: next.getAttribute("data-name"), sel: "[data-remove]" } : null;
        api.remove(n);
      } else {
        var dir = parseInt(btn.getAttribute("data-move"), 10);
        pendingFocus = { name: n, sel: '[data-move="' + dir + '"]', alt: '[data-move="' + -dir + '"]' };
        api.move(i, i + dir);
      }
    });
    var drag = null;
    container.addEventListener("pointerdown", function (e) {
      var h = e.target.closest(".drag-handle");
      if (!h || !container.contains(h)) return;
      var row = h.closest(rowSel);
      drag = { row: row, from: list.indexOf(row.getAttribute("data-name")), over: null };
      row.classList.add("is-drag");
      h.setPointerCapture(e.pointerId);
      e.preventDefault();
    });
    container.addEventListener("pointermove", function (e) {
      if (!drag) return;
      var el = document.elementFromPoint(e.clientX, e.clientY);
      var over = el && el.closest ? el.closest(rowSel) : null;
      if (over && !container.contains(over)) over = null;
      if (drag.over && drag.over !== over) drag.over.classList.remove("is-over");
      drag.over = over;
      if (over && over !== drag.row) over.classList.add("is-over");
    });
    var end = function () {
      if (!drag) return;
      drag.row.classList.remove("is-drag");
      if (drag.over) {
        drag.over.classList.remove("is-over");
        var to = list.indexOf(drag.over.getAttribute("data-name"));
        if (to !== -1) api.move(drag.from, to);
      }
      drag = null;
    };
    container.addEventListener("pointerup", end);
    container.addEventListener("pointercancel", end);
  }
  function restoreFocus(container) {
    if (!pendingFocus) return;
    var row = $('[data-name="' + (window.CSS && CSS.escape ? CSS.escape(pendingFocus.name) : pendingFocus.name) + '"]', container);
    var b = row && ($(pendingFocus.sel, row) || null);
    if (b && b.disabled && pendingFocus.alt) b = $(pendingFocus.alt, row);
    if (b && !b.disabled) b.focus();
    pendingFocus = null;
  }

  /* ---------- tray (every page except the builder) ---------- */
  var onBuilder = document.body.classList.contains("page-builder");
  var tray = null, trayOpen = false;
  function renderTray() {
    if (onBuilder) return;
    document.body.classList.toggle("has-tray", !!list.length);
    if (!list.length) { if (tray) tray.hidden = true; return; }
    if (!tray) {
      tray = document.createElement("div");
      tray.className = "wf-tray";
      tray.setAttribute("role", "region");
      tray.setAttribute("aria-label", "Your workflow");
      document.body.appendChild(tray);
      tray.addEventListener("click", function (e) {
        if (e.target.closest(".wt-toggle")) { trayOpen = !trayOpen; renderTray(); var t = $(".wt-toggle", tray); if (t) t.focus(); }
        if (e.target.closest(".wt-clear")) { trayOpen = false; api.clear(); }
      });
      wireRows(tray, ".step-row");
    }
    tray.hidden = false;
    var n = list.length;
    var chips = list.map(function (x, i) { return "<li><b>" + (i + 1) + "</b>" + esc(title(x)) + "</li>"; }).join("");
    var rows = list.map(function (x, i) {
      return '<li class="step-row" data-name="' + esc(x) + '"><span class="drag-handle" aria-hidden="true">' + ic("dots-six-vertical") + "</span>" +
        '<span class="step-n">' + (i + 1) + '</span><span class="step-t">' + esc(title(x)) + "</span>" + rowControls(x, i, n) + "</li>";
    }).join("");
    tray.innerHTML =
      '<div class="wt-bar"><span class="wt-title">Your workflow <span>' + n + " skill" + (n === 1 ? "" : "s") + "</span></span>" +
      '<ol class="wt-chips" aria-hidden="true">' + chips + "</ol>" +
      '<div class="wt-actions"><button class="btn-ghost btn-sm wt-toggle" type="button" aria-expanded="' + trayOpen + '" aria-controls="wt-list">' + (trayOpen ? "Done" : "Edit order") + "</button>" +
      '<a class="btn btn-sm" href="/workflows/build/">Build ' + ic("arrow-right") + "</a></div></div>" +
      '<ol class="wt-list" id="wt-list" aria-label="Skills in your workflow"' + (trayOpen ? "" : " hidden") + ">" + rows + "</ol>" +
      '<div class="wt-foot"' + (trayOpen ? "" : " hidden") + '><span>Drag a row or use the arrows.</span><button class="link-quiet wt-clear" type="button">Clear</button></div>';
    restoreFocus(tray);
  }
  api.onChange(renderTray);

  /* ---------- builder page ---------- */
  var builder = $("#builder");
  var stageIndex = {}, stageLabel = {}, ioLabel = {};
  function lowerFirst(s) { return s && s.length > 1 && s[1] === s[1].toLowerCase() ? s[0].toLowerCase() + s.slice(1) : s; }
  function io(t) { return lowerFirst(ioLabel[t] || t.replace(/-/g, " ")); }
  function joinAnd(items) { return items.length < 2 ? items.join("") : items.slice(0, -1).join(", ") + " and " + items[items.length - 1]; }

  // What step i receives: from the step before, from an earlier step, or nothing declared.
  function handoff(i) {
    var cur = byName[list[i]];
    if (!cur) return { kind: "gap", text: "" };
    var prev = byName[list[i - 1]];
    var shared = prev ? prev.produces.filter(function (t) { return cur.consumes.indexOf(t) !== -1; }) : [];
    if (shared.length) return { kind: "pass", text: "Passes on its <b>" + esc(joinAnd(shared.map(io))) + "</b>." };
    for (var k = i - 2; k >= 0; k--) {
      var s = byName[list[k]];
      var got = s ? s.produces.filter(function (t) { return cur.consumes.indexOf(t) !== -1; }) : [];
      if (got.length) return { kind: "pass", text: "Uses the <b>" + esc(joinAnd(got.map(io))) + "</b> from step " + (k + 1) + "." };
    }
    var needs = cur.consumes.length ? " Inputs it expects: " + esc(joinAnd(cur.consumes.map(io))) + "." : "";
    return { kind: "gap", text: "No declared hand-off. Give this step what it needs yourself." + needs };
  }

  // Each skill after the skills it takes input from; stage order breaks ties.
  function suggestOrder() {
    var names = list.filter(function (n) { return byName[n]; });
    var rest = list.filter(function (n) { return !byName[n]; });
    var deps = {};
    names.forEach(function (b) {
      deps[b] = names.filter(function (a) {
        return a !== b && byName[a].produces.some(function (t) { return byName[b].consumes.indexOf(t) !== -1; });
      });
    });
    var rank = function (n) { var st = byName[n].stage || "other"; return (st in stageIndex ? stageIndex[st] : 99) * 1000 + list.indexOf(n); };
    var out = [], left = names.slice();
    while (left.length) {
      var ready = left.filter(function (n) { return deps[n].every(function (d) { return out.indexOf(d) !== -1; }); });
      if (!ready.length) ready = left; // a cycle: fall back to stage order
      ready.sort(function (a, b) { return rank(a) - rank(b); });
      out.push(ready[0]);
      left.splice(left.indexOf(ready[0]), 1);
    }
    return out.concat(rest);
  }

  function copyRow(text, wrap) {
    return '<div class="code-row' + (wrap ? " wrap-code" : "") + '"><pre><code>' + esc(text) + "</code></pre>" +
      '<button class="copy" type="button" data-copy="' + esc(text) + '" aria-label="Copy">' +
      '<svg class="ic-copy" viewBox="0 0 256 256" fill="currentColor" aria-hidden="true"><use href="#i-copy"></use></svg>' +
      '<svg class="ic-check" viewBox="0 0 256 256" fill="currentColor" aria-hidden="true"><use href="#i-check"></use></svg>' +
      '<span class="copy-label">Copy</span></button></div>';
  }

  function workflowName() { try { return localStorage.getItem(NAME_KEY) || ""; } catch (e) { return ""; } }

  function runPrompt(name) {
    var lines = list.map(function (n, i) { return (i + 1) + ". " + n + (byName[n] ? " (" + byName[n].title + ")" : ""); });
    var intro = name ? 'I want to run my workflow "' + name + '". It uses these behavioral-science skills in order:' : "I want to run these behavioral-science skills in order:";
    return intro + "\n" + lines.join("\n") + "\n\nStart with step 1. After each step, show me the result and wait for me before going on. " +
      "Where a step's output fits the next step, use it as that step's input.";
  }

  function proposeUrl(name, gh) {
    var rows = list.map(function (n, i) {
      var h = i ? handoff(i) : null;
      var carries = byName[n] ? byName[n].produces.map(io).join(", ") : "";
      return "| " + (i + 1) + " | `" + n + "` | " + (byName[n] ? byName[n].version : "") + " | " + (i ? "after " + i : "start") + " | " + carries + " | " +
        (h && h.kind === "gap" ? "No declared hand-off from the step before" : "") + " |";
    });
    var body = [
      "### What it is for", "", "<Describe the bigger job this workflow does and who runs it.>", "",
      "### Skills in this workflow", "",
      "| Step | Skill | Version | Relationship | What carries forward | Notes |",
      "|---|---|---|---|---|---|"].concat(rows).concat(["", "_Built with the website's workflow builder._"]).join("\n");
    var p = new URLSearchParams();
    p.set("title", "Workflow proposal: " + (name || list.map(title).slice(0, 2).join(" then ") + (list.length > 2 ? " and more" : "")));
    p.set("body", body);
    return gh + "/issues/new?" + p.toString();
  }

  function renderBuilder() {
    if (!builder) return;
    var repo = builder.getAttribute("data-repo"), plugin = builder.getAttribute("data-plugin"), gh = builder.getAttribute("data-github");
    if (!list.length) {
      builder.innerHTML = '<div class="builder-empty"><p>Nothing here yet. Add skills from the Skills page or the map.</p>' +
        '<p class="b-row b-row-center"><a class="btn" href="/skills/">Browse skills</a> <a class="btn-secondary" href="/map/">Open the map</a></p></div>';
      return;
    }
    var name = workflowName(), n = list.length;
    var steps = list.map(function (x, i) {
      var s = byName[x], h = i ? handoff(i) : null;
      var stage = s ? (s.type === "meta" ? "other" : s.stage || "other") : "other";
      var meta = s ? '<span class="b-meta" data-stage="' + esc(stage) + '"><svg class="stage-ic" viewBox="0 0 256 256" fill="currentColor" aria-hidden="true"><use href="#i-st-' + esc(stage) + '"></use></svg>' +
        esc(s.type === "meta" ? "Meta-skill" : (stageLabel[s.stage] || s.stage)) + "</span>" : "";
      return '<li data-name="' + esc(x) + '">' +
        (h ? '<p class="b-link' + (h.kind === "gap" ? " is-gap" : "") + '">' + h.text + "</p>" : "") +
        '<div class="b-step"><div class="b-num"><span class="step-n">' + (i + 1) + '</span><span class="drag-handle" aria-hidden="true">' + ic("dots-six-vertical") + "</span></div>" +
        "<div>" + meta + "<h3>" + (s ? '<a href="' + esc(s.url) + '">' + esc(s.title) + "</a>" : esc(x)) + "</h3><code>" + esc(x) + "</code>" +
        (s ? "<p>" + esc(s.what_it_does) + "</p>" : '<p class="muted">This skill is not in the library any more.</p>') + "</div>" +
        rowControls(x, i, n) + "</div></li>";
    }).join("");
    var downloads = list.filter(function (x) { return byName[x]; }).map(function (x) {
      return '<li><a href="' + esc(byName[x].download_url) + '" rel="noopener">' + ic("download-simple") + "<code>" + esc(x) + ".skill</code></a></li>";
    }).join("");
    builder.innerHTML =
      '<div class="builder-main">' +
        '<div class="builder-tools"><label for="b-name">Name (optional)<input id="b-name" type="text" maxlength="80" placeholder="My workflow" value="' + esc(name) + '"></label>' +
        '<button class="btn-secondary" type="button" id="b-suggest">Suggest an order</button><button class="btn-ghost" type="button" id="b-clear">Clear</button></div>' +
        '<p class="builder-help">Suggest an order puts each skill after the skills it takes input from.</p>' +
        '<ol class="b-steps" aria-label="Steps">' + steps + "</ol>" +
        '<p class="muted">Add more from the <a href="/skills/">Skills page</a> or <a href="/map/">the map</a>.</p>' +
      "</div>" +
      '<aside class="builder-side">' +
        '<section class="b-box"><h2>Install these skills</h2><p>The Claude Code plugin already includes all of them.</p>' +
          copyRow("/plugin marketplace add " + repo) + copyRow("/plugin install " + plugin + "@" + plugin) +
          "<h3>Codex, Cursor, Copilot and others</h3>" + copyRow("npx skills add " + repo + " " + list.map(function (x) { return "--skill " + x; }).join(" "), true) +
          '<h3>Claude Desktop and claude.ai</h3><p class="muted">Upload each file under Settings, Capabilities, Skills.</p><ul class="b-downloads">' + downloads + "</ul></section>" +
        '<section class="b-box"><h2>Run it</h2><p>Paste this into your assistant.</p>' + copyRow(runPrompt(name), true) + "</section>" +
        '<section class="b-box"><h2>Share it</h2><p>The link opens this list in the builder.</p><div class="b-row">' +
          '<button class="btn-secondary btn-sm" type="button" id="b-share">' + ic("link-simple") + ' <span>Copy link</span></button>' +
          '<a class="btn-ghost btn-sm" id="b-propose" href="' + esc(proposeUrl(name, gh)) + '" target="_blank" rel="noopener">Suggest it for the library</a></div></section>' +
      "</aside>";
    restoreFocus(builder);
  }

  if (builder) {
    wireRows(builder, "li[data-name]");
    builder.addEventListener("click", function (e) {
      if (e.target.closest("#b-suggest")) {
        var next = suggestOrder();
        if (next.join(",") === list.join(",")) announce("This order already follows the hand-offs.");
        else api.set(next, "Reordered so each skill comes after the skills it takes input from.");
      }
      if (e.target.closest("#b-clear") && window.confirm("Remove all " + list.length + " skills from your workflow?")) api.clear();
      var share = e.target.closest("#b-share");
      if (share) {
        var url = location.origin + "/workflows/build/?s=" + list.map(encodeURIComponent).join(",");
        var label = $("span", share);
        (window.__copyText || function (t, done) { done(); })(url, function () {
          if (label) label.textContent = "Link copied";
          setTimeout(function () { if (label) label.textContent = "Copy link"; }, 1600);
        });
      }
    });
    builder.addEventListener("input", function (e) {
      if (e.target.id !== "b-name") return;
      try { localStorage.setItem(NAME_KEY, e.target.value); } catch (err) { /* ignore */ }
      // Update the prompt and the proposal link without re-rendering the input.
      var rows = $$(".b-box .code-row", builder), prompt = rows[rows.length - 1];
      var text = runPrompt(e.target.value);
      if (prompt) { $("code", prompt).textContent = text; $(".copy", prompt).setAttribute("data-copy", text); }
      var pr = $("#b-propose", builder);
      if (pr) pr.href = proposeUrl(e.target.value, builder.getAttribute("data-github"));
    });
    api.onChange(renderBuilder);
  }

  /* ---------- start ---------- */
  syncButtons();
  renderTray();
  var needsData = builder || list.length || document.body.classList.contains("page-map");
  if (needsData) {
    loadData().then(function (d) {
      if (d) {
        d.stages.forEach(function (s, i) { stageIndex[s.id] = i; stageLabel[s.id] = s.label; });
        d.io_types.forEach(function (t) { ioLabel[t.id] = t.label; });
      }
      if (builder) {
        var shared = new URLSearchParams(location.search).get("s");
        if (shared !== null) {
          var names = shared.split(",").map(function (x) { return x.trim(); }).filter(function (x) { return x && (!d || byName[x]); });
          if (names.length && replaceOk(names)) save(names, "Loaded " + names.length + " skills from the link.");
          history.replaceState(null, "", location.pathname);
        }
      }
      syncButtons();
      renderTray();
      renderBuilder();
    });
  } else {
    renderBuilder();
  }
  // Fetch titles once the reader adds a first skill on a page that had none.
  api.onChange(function () { if (list.length && !data) loadData().then(function () { syncButtons(); renderTray(); }); });
})();
