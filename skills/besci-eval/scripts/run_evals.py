#!/usr/bin/env python3
"""
run_evals.py — run a library skill's evals through the Claude API and grade them.

Usage:
  python run_evals.py path/to/skill [--models claude-opus-5-5 claude-sonnet-5-5]
                                    [--runs 3] [--judge claude-opus-5-5]
                                    [--baseline path/to/old-skill] [--catalog path/to/catalog.md]
                                    [--skip-trigger] [--skip-output] [--effort medium]
                                    [--out DIR] [--dry-run]

What it does:
  1. Structure: runs besci_validate.py (bundled next to this script).
  2. Triggering: for every "Use it when" / "Do not use it when" phrase and every
     eval prompt, asks a judge model whether it would load this skill given the
     description and the neighbors' descriptions from the catalog snapshot.
  3. Output quality: for each eval case, runs the prompt with SKILL.md as the
     system prompt on each model, N times, then grades each output with the
     rubric in references/rubric.md using the judge model.

Writes <skill>-workspace/eval-<timestamp>/report.md and results.json.

Requires: pip install anthropic pyyaml. Credentials: ANTHROPIC_API_KEY, or an
`ant auth login` profile (the SDK picks it up with no env var).

Cost: roughly (cases x models x runs x 2) + (phrases) calls. Use --dry-run to
see the plan and estimated call count without spending anything.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import statistics
import sys
from typing import Dict, List, Optional

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import besci_validate as bv  # noqa: E402

DEFAULT_MODEL = "claude-opus-5-5"
RUBRIC_PATH = os.path.join(os.path.dirname(HERE), "references", "rubric.md")

CRITERIA = ["asked_first", "template", "evidence", "mechanism", "escalation", "plain_language", "no_invention", "failure_modes"]


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------

def get_client():
    try:
        import anthropic
    except ImportError:
        sys.stderr.write("pip install anthropic\n")
        sys.exit(2)
    return anthropic.Anthropic()


def call(client, model: str, system: str, user: str, effort: str, max_tokens: int = 16000) -> Dict:
    """One non-streaming Messages call. Returns {text, stop_reason, usage}."""
    resp = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system,
        output_config={"effort": effort},
        messages=[{"role": "user", "content": user}],
    )
    text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
    return {
        "text": text,
        "stop_reason": resp.stop_reason,
        "input_tokens": resp.usage.input_tokens,
        "output_tokens": resp.usage.output_tokens,
    }


def parse_json(text: str) -> Optional[dict]:
    """Find the first JSON object in a response; tolerate fences and prose."""
    m = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


# ---------------------------------------------------------------------------
# Catalog neighbors (for trigger judgement)
# ---------------------------------------------------------------------------

def neighbor_descriptions(catalog_path: Optional[str], this_name: str) -> List[Dict[str, str]]:
    """Pull name + description pairs out of the navigator's catalog.md snapshot."""
    if not catalog_path or not os.path.exists(catalog_path):
        return []
    text = open(catalog_path, encoding="utf-8").read()
    out = []
    for block in re.split(r"^### ", text, flags=re.MULTILINE)[1:]:
        name = block.split("\n", 1)[0].strip().strip("`")
        if name == this_name:
            continue
        m = re.search(r"\*\*Description:\*\*\s*(.+?)(?:\n\n|\n\*\*)", block, flags=re.DOTALL)
        if m:
            out.append({"name": name, "description": " ".join(m.group(1).split())})
    return out


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_structure(skill_dir: str) -> Dict:
    tax = bv.load_taxonomy()
    skills = bv.validate_path(skill_dir, tax)
    return {"report": bv.report_text(skills), "ok": all(not s.errors for s in skills)}


def trigger_cases(skill: bv.Skill) -> List[Dict]:
    should, should_not = bv.trigger_phrases(skill)
    cases = [{"phrase": p, "should_fire": True, "source": "use-it-when"} for p in should]
    cases += [{"phrase": p, "should_fire": False, "source": "do-not-use-it-when"} for p in should_not]
    for c in (skill.evals or {}).get("evals", []):
        expected = str(c.get("expected_output", "")).lower()
        fires = not any(k in expected for k in ("does not fire", "should not fire", "not a library skill", "points the user to"))
        cases.append({"phrase": c["prompt"], "should_fire": fires, "source": f"eval-{c.get('id')}"})
    return cases


TRIGGER_SYSTEM = (
    "You are the skill-selection step of an AI assistant. You see a user's request and the "
    "descriptions of the skills installed. Decide whether you would load the skill named "
    "TARGET for this request. Answer with JSON only: {\"fire\": true|false, \"reason\": \"one line\"}."
)


def check_trigger(client, judge: str, skill: bv.Skill, neighbors: List[Dict], effort: str, dry: bool) -> Dict:
    cases = trigger_cases(skill)
    desc = str(skill.frontmatter.get("description", ""))
    neigh = "\n".join(f"- {n['name']}: {n['description']}" for n in neighbors) or "- (no other skills installed)"
    results = []
    for c in cases:
        user = (
            f"TARGET skill: {skill.name}\nTARGET description: {desc}\n\nOther installed skills:\n{neigh}\n\n"
            f"User request: {c['phrase']}\n\nWould you load TARGET? JSON only."
        )
        if dry:
            results.append({**c, "fired": None, "reason": "dry run"})
            continue
        r = call(client, judge, TRIGGER_SYSTEM, user, effort, max_tokens=512)
        j = parse_json(r["text"]) or {}
        results.append({**c, "fired": bool(j.get("fire")), "reason": str(j.get("reason", r["text"][:200]))})
    fired = [r for r in results if r["fired"]]
    correct_fired = [r for r in fired if r["should_fire"]]
    should = [r for r in results if r["should_fire"]]
    precision = len(correct_fired) / len(fired) if fired else None
    recall = len(correct_fired) / len(should) if should else None
    return {"cases": results, "precision": precision, "recall": recall}


def load_rubric() -> str:
    if os.path.exists(RUBRIC_PATH):
        return open(RUBRIC_PATH, encoding="utf-8").read()
    return "Score eight criteria 0-2: asked_first, template, evidence, mechanism, escalation, plain_language, no_invention, failure_modes."


GRADER_SYSTEM = (
    "You grade one AI output against a skill's own rubric. Be strict and quote the output in each "
    "justification. Return JSON only with this shape: {\"scores\": {\"asked_first\": 0-2, \"template\": 0-2, "
    "\"evidence\": 0-2, \"mechanism\": 0-2, \"escalation\": 0-2, \"plain_language\": 0-2, \"no_invention\": 0-2, "
    "\"failure_modes\": 0-2}, \"justifications\": {same keys: one line each}, \"matches_expected\": true|false, "
    "\"blocking\": [\"...\"], \"excerpt\": \"the single most telling quote\"}"
)


def check_output(client, models: List[str], runs: int, judge: str, skill: bv.Skill, skill_md: str,
                 effort: str, dry: bool, label: str = "candidate") -> Dict:
    rubric = load_rubric()
    cases = (skill.evals or {}).get("evals", [])
    out = {"label": label, "models": {}}
    for model in models:
        per_case = []
        for c in cases:
            run_results = []
            for i in range(runs):
                if dry:
                    run_results.append({"run": i + 1, "total": None, "scores": {}, "dry": True})
                    continue
                r = call(client, model, skill_md, c["prompt"], effort)
                if r["stop_reason"] == "refusal":
                    run_results.append({"run": i + 1, "total": 0, "scores": {}, "blocking": ["model refused the request"], "output": ""})
                    continue
                grade_user = (
                    f"RUBRIC:\n{rubric}\n\nSKILL.md (for the sections the rubric refers to):\n{skill_md}\n\n"
                    f"USER PROMPT:\n{c['prompt']}\n\nEXPECTED OUTPUT (shape):\n{c.get('expected_output','')}\n\n"
                    f"ACTUAL OUTPUT:\n{r['text']}\n\nGrade it. JSON only."
                )
                g = call(client, judge, GRADER_SYSTEM, grade_user, effort, max_tokens=4000)
                j = parse_json(g["text"]) or {}
                scores = {k: int(j.get("scores", {}).get(k, 0) or 0) for k in CRITERIA}
                run_results.append({
                    "run": i + 1,
                    "scores": scores,
                    "total": sum(scores.values()),
                    "justifications": j.get("justifications", {}),
                    "matches_expected": j.get("matches_expected"),
                    "blocking": j.get("blocking", []),
                    "excerpt": j.get("excerpt", ""),
                    "output": r["text"],
                    "tokens": {"in": r["input_tokens"], "out": r["output_tokens"]},
                })
            totals = [x["total"] for x in run_results if x.get("total") is not None]
            per_case.append({
                "id": c.get("id"),
                "prompt": c["prompt"][:160],
                "runs": run_results,
                "median": statistics.median(totals) if totals else None,
                "range": (min(totals), max(totals)) if totals else None,
                "blocking": sorted({b for x in run_results for b in x.get("blocking", [])}),
            })
        medians = [p["median"] for p in per_case if p["median"] is not None]
        out["models"][model] = {
            "cases": per_case,
            "median": statistics.median(medians) if medians else None,
            "blocking": sorted({b for p in per_case for b in p["blocking"]}),
        }
    return out


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def fmt(x) -> str:
    return "n/a" if x is None else (f"{x:.2f}" if isinstance(x, float) else str(x))


def write_report(path: str, skill: bv.Skill, args, structure: Dict, trigger: Optional[Dict],
                 output: Optional[Dict], baseline: Optional[Dict]) -> None:
    version = skill.metadata.get("version", "?")
    lines = [f"# Evaluation: {skill.name} v{version}  ({dt.date.today().isoformat()}, {', '.join(args.models)}, {args.runs} run(s) per case)", ""]
    blocking = []
    if output:
        for m, d in output["models"].items():
            blocking += [f"{m}: {b}" for b in d["blocking"]]
    if not structure["ok"]:
        verdict, why = "not gradable", "the validator reports errors; fix structure first"
    elif blocking:
        verdict, why = "fix first", "blocking findings in output quality"
    elif output and all((d["median"] or 0) >= 14 for d in output["models"].values()) and (trigger is None or ((trigger["recall"] or 0) >= 0.8 and (trigger["precision"] or 0) >= 0.8)):
        verdict, why = "ready to submit", "structure passes, triggering is precise, outputs match the template"
    elif args.dry_run:
        verdict, why = "dry run", "no calls were made"
    else:
        verdict, why = "fix first", "see the lowest-scoring criteria and trigger misses below"
    lines += [f"**Verdict:** {verdict}", f"**Why:** {why}", "", "## 1. Structure", "", "```", structure["report"], "```", ""]
    if trigger:
        lines += ["## 2. Triggering", "", f"Precision {fmt(trigger['precision'])}, recall {fmt(trigger['recall'])}", "",
                  "| Phrase | Should fire | Fired | Reason |", "|---|---|---|---|"]
        for c in trigger["cases"]:
            lines.append(f"| {c['phrase'][:90].replace('|','/')} | {'yes' if c['should_fire'] else 'no'} | {fmt(c['fired'])} | {str(c['reason'])[:120].replace('|','/')} |")
        misses = [c for c in trigger["cases"] if c["fired"] is not None and c["fired"] != c["should_fire"]]
        lines += ["", "Misses and false alarms:"] + ([f"- {c['phrase'][:120]} (should fire: {c['should_fire']})" for c in misses] or ["- none"]) + [""]
    if output:
        lines += ["## 3. Output quality", ""]
        for m, d in output["models"].items():
            lines += [f"### {m}  (median {fmt(d['median'])}/16)", "", "| Case | " + " | ".join(CRITERIA) + " | Matches expected | Median (range) |", "|---|" + "---|" * (len(CRITERIA) + 2)]
            for p in d["cases"]:
                first = next((r for r in p["runs"] if r.get("scores")), {})
                sc = first.get("scores", {})
                lines.append(f"| {p['id']} | " + " | ".join(str(sc.get(k, '-')) for k in CRITERIA) + f" | {fmt(first.get('matches_expected'))} | {fmt(p['median'])} {p['range'] or ''} |")
            lines += ["", "Blocking findings: " + ("; ".join(d["blocking"]) or "none"), ""]
            ex = next((r.get("excerpt") for p in d["cases"] for r in p["runs"] if r.get("excerpt")), "")
            if ex:
                lines += [f"Representative excerpt: > {ex[:400]}", ""]
    if output and len(output["models"]) > 1 or baseline:
        lines += ["## 4. Model comparison", "", "| Model | Trigger P/R | Quality median | Blocking |", "|---|---|---|---|"]
        for m, d in (output or {}).get("models", {}).items():
            lines.append(f"| {m} | {fmt(trigger['precision']) if trigger else 'n/a'}/{fmt(trigger['recall']) if trigger else 'n/a'} | {fmt(d['median'])} | {len(d['blocking'])} |")
        if baseline:
            for m, d in baseline["models"].items():
                lines.append(f"| baseline {m} | - | {fmt(d['median'])} | {len(d['blocking'])} |")
        lines.append("")
    lines += ["## Next actions for the author", ""]
    acts = []
    if not structure["ok"]:
        acts.append("Fix the validator errors above with besci-skill-creator.")
    if trigger and trigger["cases"]:
        misses = [c for c in trigger["cases"] if c["fired"] is not None and c["fired"] != c["should_fire"]]
        if misses:
            acts.append(f"Tighten the description for: {misses[0]['phrase'][:80]}")
    if blocking:
        acts.append("Resolve the blocking findings before anything else.")
    if output:
        for m, d in output["models"].items():
            for p in d["cases"]:
                first = next((r for r in p["runs"] if r.get("scores")), None)
                if first:
                    worst = min(first["scores"].items(), key=lambda kv: kv[1])
                    if worst[1] == 0:
                        acts.append(f"Case {p['id']} on {m}: criterion '{worst[0]}' scored 0: {first.get('justifications', {}).get(worst[0], '')[:120]}")
    if not acts:
        acts.append("None. Submit, and note this report in the pull request.")
    lines += [f"{i+1}. {a}" for i, a in enumerate(acts[:8])]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def load_skill(path: str) -> bv.Skill:
    tax = bv.load_taxonomy()
    s = bv.validate_skill(bv.parse_skill(path), tax)
    return s


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("skill")
    ap.add_argument("--models", nargs="+", default=[DEFAULT_MODEL])
    ap.add_argument("--judge", default=DEFAULT_MODEL)
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--baseline", help="Path to an older version of the skill folder to compare against")
    ap.add_argument("--catalog", help="Path to catalog.md (default: besci-navigator/references/catalog.md if found)")
    ap.add_argument("--effort", default="medium", choices=["low", "medium", "high", "xhigh", "max"])
    ap.add_argument("--skip-trigger", action="store_true")
    ap.add_argument("--skip-output", action="store_true")
    ap.add_argument("--out", help="Output directory (default: <skill>-workspace/eval-<timestamp>)")
    ap.add_argument("--dry-run", action="store_true", help="Plan only; make no API calls")
    args = ap.parse_args()

    skill = load_skill(args.skill)
    if not skill.name:
        sys.stderr.write("Not a skill folder (no valid SKILL.md).\n")
        return 2
    skill_md = open(os.path.join(skill.path, "SKILL.md"), encoding="utf-8").read()
    structure = check_structure(skill.path)
    n_cases = len((skill.evals or {}).get("evals", []))
    if n_cases < 3:
        sys.stderr.write(f"{skill.name} has {n_cases} evals; at least 3 are required. Use besci-skill-creator to add them.\n")
        return 1

    catalog = args.catalog
    if not catalog:
        root = bv.find_repo_root(skill.path) or os.getcwd()
        cand = os.path.join(root, "skills", "besci-navigator", "references", "catalog.md")
        catalog = cand if os.path.exists(cand) else None
    neighbors = neighbor_descriptions(catalog, skill.name)

    n_trigger = 0 if args.skip_trigger else len(trigger_cases(skill))
    n_output = 0 if args.skip_output else n_cases * len(args.models) * args.runs * 2
    n_base = 0 if not args.baseline or args.skip_output else n_cases * len(args.models) * args.runs * 2
    print(f"Plan: {skill.name} v{skill.metadata.get('version','?')} | models {args.models} | judge {args.judge} | runs {args.runs}")
    print(f"Calls: trigger {n_trigger}, output {n_output}, baseline {n_base}, total {n_trigger + n_output + n_base}")

    client = None if args.dry_run else get_client()
    trigger = None if args.skip_trigger else check_trigger(client, args.judge, skill, neighbors, args.effort, args.dry_run)
    output = None if args.skip_output else check_output(client, args.models, args.runs, args.judge, skill, skill_md, args.effort, args.dry_run)
    baseline = None
    if args.baseline and not args.skip_output:
        b = load_skill(args.baseline)
        b_md = open(os.path.join(b.path, "SKILL.md"), encoding="utf-8").read()
        baseline = check_output(client, args.models, args.runs, args.judge, b, b_md, args.effort, args.dry_run, label="baseline")

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    out_dir = args.out or os.path.join(os.path.dirname(skill.path), f"{skill.name}-workspace", f"eval-{stamp}")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "results.json"), "w", encoding="utf-8") as fh:
        json.dump({"skill": skill.name, "version": skill.metadata.get("version"), "args": vars(args),
                   "structure": structure, "trigger": trigger, "output": output, "baseline": baseline}, fh, indent=2, default=str)
    write_report(os.path.join(out_dir, "report.md"), skill, args, structure, trigger, output, baseline)
    print(f"Wrote {out_dir}/report.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
