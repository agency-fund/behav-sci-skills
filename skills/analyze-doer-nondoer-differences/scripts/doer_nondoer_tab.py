#!/usr/bin/env python3
"""doer_nondoer_tab.py: tabulate Doer and Non-Doer responses from a Barrier
Analysis and flag the determinants that separate the two groups.

Reads a CSV with one row per determinant and response category and these
columns (header required, any order):
  determinant, response, doer_count, nondoer_count, n_doers, n_nondoers
doer_count is the number of Doers who gave that response; n_doers is the
number of Doers interviewed (the denominator), and likewise for Non-Doers.
A respondent who gave two responses to one determinant appears in two rows;
a respondent counts at most once per row.

For each row the script prints the percentage of each group giving the
response, the difference in percentage points (Doer minus Non-Doer), a
two-sided Fisher exact p-value, and a flag. The flag follows the convention
in Kittle's Practical Guide to Conducting a Barrier Analysis (2013; 2nd ed.
2017): an absolute difference of at least 15 points, or p < .05. The rule is
a screening heuristic with no validation; the p-value describes the gap in
this sample and is not a confirmatory test (twelve determinants with several
responses each produce many comparisons). The guide's tabulation sheet
reports a p-value; the sources available to this skill do not record which
test it uses, so the Fisher exact test here is this script's own choice.

The Fisher test compares the 2x2 table
  [doer_count, n_doers - doer_count; nondoer_count, n_nondoers - nondoer_count]
and sums the hypergeometric probabilities of every table with the same
margins that is at most as probable as the observed one. Exact integer
arithmetic with math.comb; standard library only; Python 3.8+.

Usage:
  python doer_nondoer_tab.py tally.csv
  python doer_nondoer_tab.py tally.csv --markdown     # table for the output template
  python doer_nondoer_tab.py tally.csv --threshold 15 --alpha 0.05
  python doer_nondoer_tab.py --self-test

Self-test (python doer_nondoer_tab.py --self-test):
  30 of 45 Doers vs 12 of 45 Non-Doers: 66.7% vs 26.7%, a difference of
  40.0 points, p well below .05 (the test checks p < .001); flagged.
  20 of 45 vs 16 of 45: 44.4% vs 35.6%, 8.9 points, p above .05; not flagged.
  Identical columns (10 of 45 vs 10 of 45): difference 0.0, p = 1.0.
  70 of 400 vs 42 of 400: 7.0 points, so below the 15-point line, but
  p < .05; reported as flagged by p only, so the user sees which part of
  the rule fired.
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
from typing import Dict, List, Optional

REQUIRED_COLUMNS = ["determinant", "response", "doer_count", "nondoer_count", "n_doers", "n_nondoers"]


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------

def fisher_exact_two_sided(a: int, b: int, c: int, d: int) -> float:
    """Two-sided Fisher exact p-value for the 2x2 table [[a, b], [c, d]].

    Rows are the groups (Doers, Non-Doers); columns are gave / did not give
    the response. Sums the probabilities of all tables with the same margins
    whose probability is at most that of the observed table.
    """
    for v in (a, b, c, d):
        if v < 0:
            raise ValueError("counts must be non-negative")
    r1, r2, k = a + b, c + d, a + c
    n = r1 + r2
    if n == 0 or r1 == 0 or r2 == 0:
        return 1.0
    denominator = math.comb(n, k)
    observed = math.comb(r1, a) * math.comb(r2, k - a)
    total = 0
    for x in range(max(0, k - r2), min(r1, k) + 1):
        weight = math.comb(r1, x) * math.comb(r2, k - x)
        if weight <= observed:
            total += weight
    return min(1.0, total / denominator)


# ---------------------------------------------------------------------------
# Tabulation
# ---------------------------------------------------------------------------

def tabulate_row(determinant: str, response: str, doer_count: int, nondoer_count: int,
                 n_doers: int, n_nondoers: int, threshold: float = 15.0, alpha: float = 0.05) -> Dict[str, object]:
    if n_doers <= 0 or n_nondoers <= 0:
        raise ValueError(f"{determinant} / {response}: n_doers and n_nondoers must be positive")
    if doer_count > n_doers or nondoer_count > n_nondoers:
        raise ValueError(f"{determinant} / {response}: a count exceeds its group size")
    doer_pct = 100.0 * doer_count / n_doers
    nondoer_pct = 100.0 * nondoer_count / n_nondoers
    diff = doer_pct - nondoer_pct
    p = fisher_exact_two_sided(doer_count, n_doers - doer_count, nondoer_count, n_nondoers - nondoer_count)
    by_gap = abs(diff) >= threshold
    by_p = p < alpha
    if by_gap and by_p:
        flag = "yes (gap and p)"
    elif by_gap:
        flag = "yes (gap only)"
    elif by_p:
        flag = "yes (p only)"
    else:
        flag = "no"
    if diff > 0:
        direction = "more common among Doers (enabler to reinforce)"
    elif diff < 0:
        direction = "more common among Non-Doers (barrier to remove)"
    else:
        direction = "no difference"
    return {
        "determinant": determinant, "response": response,
        "doer_count": doer_count, "n_doers": n_doers, "doer_pct": doer_pct,
        "nondoer_count": nondoer_count, "n_nondoers": n_nondoers, "nondoer_pct": nondoer_pct,
        "diff": diff, "p": p, "flag": flag, "flagged": by_gap or by_p, "direction": direction,
    }


def read_tally(path: str) -> List[Dict[str, object]]:
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            raise ValueError("the CSV has no header row")
        header = [h.strip() for h in reader.fieldnames]
        missing = [c for c in REQUIRED_COLUMNS if c not in header]
        if missing:
            raise ValueError(f"missing column(s): {', '.join(missing)}; need {', '.join(REQUIRED_COLUMNS)}")
        rows = []
        for i, raw in enumerate(reader, start=2):
            row = {k.strip(): (v or "").strip() for k, v in raw.items() if k is not None}
            if not row.get("determinant") and not row.get("response"):
                continue
            try:
                rows.append({
                    "determinant": row["determinant"], "response": row["response"],
                    "doer_count": int(row["doer_count"]), "nondoer_count": int(row["nondoer_count"]),
                    "n_doers": int(row["n_doers"]), "n_nondoers": int(row["n_nondoers"]),
                })
            except (KeyError, ValueError) as exc:
                raise ValueError(f"line {i}: could not read counts ({exc})") from exc
    return rows


def tabulate(rows: List[Dict[str, object]], threshold: float = 15.0, alpha: float = 0.05) -> List[Dict[str, object]]:
    return [tabulate_row(r["determinant"], r["response"], r["doer_count"], r["nondoer_count"],  # type: ignore[arg-type]
                         r["n_doers"], r["n_nondoers"], threshold, alpha) for r in rows]  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def fmt_p(p: float) -> str:
    return "<.001" if p < 0.001 else f"{p:.3f}"


def render_text(results: List[Dict[str, object]], threshold: float, alpha: float) -> str:
    lines = [f"Flag rule: |difference| >= {threshold:g} points or Fisher exact p < {alpha:g} "
             "(Kittle 2013/2017 convention; a screening heuristic, not a confirmatory test)", ""]
    for r in results:
        lines.append(f"{r['determinant']} | {r['response']}")
        lines.append(f"  Doers {r['doer_count']}/{r['n_doers']} ({r['doer_pct']:.1f}%)  "
                     f"Non-Doers {r['nondoer_count']}/{r['n_nondoers']} ({r['nondoer_pct']:.1f}%)  "
                     f"difference {r['diff']:+.1f} points  p {fmt_p(r['p'])}  flag: {r['flag']}")
        if r["flagged"]:
            lines.append(f"  direction: {r['direction']}")
    n_flag = sum(1 for r in results if r["flagged"])
    lines += ["", f"{len(results)} row(s); {n_flag} flagged. Rank flagged rows by gap, then by coverage, "
              "then by whether the program can act on them."]
    return "\n".join(lines)


def render_markdown(results: List[Dict[str, object]]) -> str:
    lines = ["| Determinant | Response category | Doers n (%) | Non-Doers n (%) | Difference (points) | p | Flag |",
             "|---|---|---|---|---|---|---|"]
    for r in results:
        lines.append(f"| {r['determinant']} | {r['response']} | {r['doer_count']} ({r['doer_pct']:.1f}) | "
                     f"{r['nondoer_count']} ({r['nondoer_pct']:.1f}) | {r['diff']:+.1f} | {fmt_p(r['p'])} | {r['flag']} |")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def self_test() -> bool:
    ok = True

    def check(label: str, cond: bool) -> None:
        nonlocal ok
        print(("  ok   " if cond else "  FAIL ") + label)
        ok = ok and cond

    r = tabulate_row("Self-efficacy", "example", 30, 12, 45, 45)
    check(f"30/45 vs 12/45: {r['doer_pct']:.1f}% vs {r['nondoer_pct']:.1f}%, {r['diff']:+.1f} points, p {fmt_p(r['p'])}, flag {r['flag']}",
          abs(r["diff"] - 40.0) < 1e-9 and r["p"] < 0.001 and r["flag"] == "yes (gap and p)")
    r = tabulate_row("Access", "example", 20, 16, 45, 45)
    check(f"20/45 vs 16/45: {r['diff']:+.1f} points, p {fmt_p(r['p'])}, flag {r['flag']}",
          abs(r["diff"] - 8.9) < 0.05 and r["p"] > 0.05 and r["flag"] == "no")
    r = tabulate_row("Norms", "example", 10, 10, 45, 45)
    check(f"10/45 vs 10/45: {r['diff']:+.1f} points, p {r['p']:.3f}", r["diff"] == 0.0 and abs(r["p"] - 1.0) < 1e-12)
    r = tabulate_row("Cues", "example", 70, 42, 400, 400)
    check(f"70/400 vs 42/400: {r['diff']:+.1f} points, p {fmt_p(r['p'])}, flag {r['flag']}",
          abs(r["diff"] - 7.0) < 1e-9 and r["p"] < 0.05 and r["flag"] == "yes (p only)")
    # the sum over all tables with the same margins is 1
    total = sum(math.comb(45, x) * math.comb(45, 42 - x) for x in range(0, 43)) / math.comb(90, 42)
    check(f"hypergeometric mass sums to 1 ({total:.12f})", abs(total - 1.0) < 1e-12)
    print("self-test " + ("passed" if ok else "FAILED"))
    return ok


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__.split("\n\n")[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="\n\n".join(__doc__.split("\n\n")[1:]),
    )
    ap.add_argument("csv", nargs="?", help="tally CSV: determinant, response, doer_count, nondoer_count, n_doers, n_nondoers")
    ap.add_argument("--threshold", type=float, default=15.0, help="percentage-point gap that flags a row (default 15)")
    ap.add_argument("--alpha", type=float, default=0.05, help="p-value that flags a row (default 0.05)")
    ap.add_argument("--markdown", action="store_true", help="print the tabulation as a markdown table")
    ap.add_argument("--self-test", action="store_true", help="run the known-case checks and exit")
    args = ap.parse_args(argv)

    if args.self_test:
        return 0 if self_test() else 1
    if not args.csv:
        ap.error("a CSV path is required (or use --self-test)")
    try:
        results = tabulate(read_tally(args.csv), args.threshold, args.alpha)
    except (OSError, ValueError) as exc:
        sys.stderr.write(f"error: {exc}\n")
        return 2
    if not results:
        sys.stderr.write("error: the CSV has no data rows\n")
        return 2
    print(render_markdown(results) if args.markdown else render_text(results, args.threshold, args.alpha))
    return 0


if __name__ == "__main__":
    sys.exit(main())
