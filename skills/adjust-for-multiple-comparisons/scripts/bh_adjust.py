#!/usr/bin/env python3
"""bh_adjust.py: Benjamini-Hochberg q-values and Bonferroni-adjusted p-values
for one family of tests.

Reads p-values from command-line arguments or from a file (one p-value per
line, or "label,p" per line; blank lines and lines starting with # are
ignored) and prints a table with the unadjusted p, the Bonferroni-adjusted
p, the Benjamini-Hochberg q-value, and whether each test is rejected at the
chosen level under each method. Run it once per family; never pool families.
Standard library only; Python 3.8+.

Definitions (m = number of tests in the family):
  Bonferroni:  p_adj(i) = min(1, m * p(i)). Controls the family-wise error
               rate, the probability of at least one false positive in the
               family. Reject when p_adj(i) <= alpha.
  Benjamini-Hochberg: sort the p-values ascending, p(1) <= ... <= p(m), and
               set q(i) = min over j >= i of min(1, m * p(j) / j). Controls
               the false discovery rate, the expected share of rejected
               tests that are false positives. A test is a discovery at
               level alpha when q(i) <= alpha.

Self-test (python bh_adjust.py --self-test):
  Case 1: p = 0.01, 0.02, 0.03, 0.04, 0.05 with m = 5. Every m * p(i) / i
          equals 0.05, so Benjamini-Hochberg gives q = 0.05 for all five;
          Bonferroni gives 0.05, 0.10, 0.15, 0.20, 0.25.
  Case 2: p = 0.001, 0.01, 0.04, 0.2 with m = 4. Benjamini-Hochberg gives
          q = 0.004, 0.02, 0.0533, 0.2 (0.04 * 4 / 3 = 0.0533; the step-up
          minimum carries nothing smaller down from 0.2). Bonferroni gives
          0.004, 0.04, 0.16, 0.8.
  Case 3: ties and the cap: p = 0.5, 0.5, 0.9 with m = 3. Bonferroni caps
          at 1.0 for all three; Benjamini-Hochberg gives q = 0.75, 0.75,
          0.9.
  Case 4: input order does not matter: p = 0.41, 0.004, 0.045, 0.012 gives
          q = 0.41, 0.016, 0.06, 0.024, matching the sorted computation.

Examples:
  python bh_adjust.py 0.004 0.012 0.045 0.41
  python bh_adjust.py 0.004 0.012 0.045 0.41 --labels "deposits,days,balance,withdrawals"
  python bh_adjust.py --file family_b.csv --alpha 0.10
"""
from __future__ import annotations

import argparse
import sys
from typing import List, Optional, Sequence, Tuple


# ---------------------------------------------------------------------------
# Procedures
# ---------------------------------------------------------------------------

def bonferroni(pvalues: Sequence[float]) -> List[float]:
    """min(1, m * p) for each p, in input order."""
    m = len(pvalues)
    return [min(1.0, m * p) for p in pvalues]


def benjamini_hochberg(pvalues: Sequence[float]) -> List[float]:
    """Benjamini-Hochberg q-values, returned in input order."""
    m = len(pvalues)
    order = sorted(range(m), key=lambda i: pvalues[i])
    q_sorted = [0.0] * m
    running = 1.0
    # Walk from the largest p down so each q is the minimum of everything above it.
    for rank in range(m, 0, -1):
        idx = order[rank - 1]
        running = min(running, min(1.0, m * pvalues[idx] / rank))
        q_sorted[rank - 1] = running
    q = [0.0] * m
    for rank, idx in enumerate(order, start=1):
        q[idx] = q_sorted[rank - 1]
    return q


# ---------------------------------------------------------------------------
# Input
# ---------------------------------------------------------------------------

def read_file(path: str) -> Tuple[List[str], List[float]]:
    labels: List[str] = []
    values: List[float] = []
    with open(path, "r", encoding="utf-8") as fh:
        for n, raw in enumerate(fh, start=1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split(",")]
            try:
                if len(parts) == 1:
                    labels.append(f"test {len(values) + 1}")
                    values.append(float(parts[0]))
                else:
                    labels.append(parts[0] or f"test {len(values) + 1}")
                    values.append(float(parts[-1]))
            except ValueError:
                raise SystemExit(f"{path}:{n}: cannot read a p-value from '{line}'")
    return labels, values


def check(pvalues: Sequence[float]) -> None:
    if not pvalues:
        raise SystemExit("no p-values given")
    for p in pvalues:
        if not (0.0 <= p <= 1.0):
            raise SystemExit(f"p-value {p} is not between 0 and 1")


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def table(labels: Sequence[str], pvalues: Sequence[float], alpha: float) -> str:
    bonf = bonferroni(pvalues)
    bh = benjamini_hochberg(pvalues)
    m = len(pvalues)
    width = max(len(l) for l in labels)
    lines = [f"family of m = {m} tests; alpha = {alpha:g}",
             f"{'test':<{width}}  {'p':>8}  {'bonferroni':>10}  {'bh q':>8}  {'reject FWER':>11}  {'reject FDR':>10}"]
    for lab, p, b, q in zip(labels, pvalues, bonf, bh):
        lines.append(f"{lab:<{width}}  {p:>8.4g}  {b:>10.4g}  {q:>8.4g}  {('yes' if b <= alpha else 'no'):>11}  {('yes' if q <= alpha else 'no'):>10}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def _close(a: Sequence[float], b: Sequence[float], tol: float = 1e-4) -> bool:
    return len(a) == len(b) and all(abs(x - y) <= tol for x, y in zip(a, b))


def self_test() -> int:
    cases = [
        ([0.01, 0.02, 0.03, 0.04, 0.05], [0.05] * 5, [0.05, 0.10, 0.15, 0.20, 0.25]),
        ([0.001, 0.01, 0.04, 0.2], [0.004, 0.02, 0.0533, 0.2], [0.004, 0.04, 0.16, 0.8]),
        ([0.5, 0.5, 0.9], [0.75, 0.75, 0.9], [1.0, 1.0, 1.0]),
        ([0.41, 0.004, 0.045, 0.012], [0.41, 0.016, 0.06, 0.024], [1.0, 0.016, 0.18, 0.048]),
    ]
    failures = 0
    for n, (p, want_q, want_b) in enumerate(cases, start=1):
        got_q, got_b = benjamini_hochberg(p), bonferroni(p)
        ok = _close(got_q, want_q) and _close(got_b, want_b)
        failures += 0 if ok else 1
        print(f"case {n}: {'ok' if ok else 'FAIL'}  p={p}")
        print(f"  bh q      got {[round(x, 4) for x in got_q]} want {want_q}")
        print(f"  bonferroni got {[round(x, 4) for x in got_b]} want {want_b}")
    print("self-test passed" if failures == 0 else f"self-test FAILED ({failures} case(s))")
    return 0 if failures == 0 else 1


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description="Benjamini-Hochberg q-values and Bonferroni-adjusted p-values for one family of tests.",
        epilog="Run once per family. See the module docstring for the definitions and the self-test cases.")
    ap.add_argument("pvalues", nargs="*", type=float, help="unadjusted p-values, one per test in the family")
    ap.add_argument("--file", help="read p-values from a file: one per line, or 'label,p' per line")
    ap.add_argument("--labels", help="comma-separated labels for the p-values given as arguments")
    ap.add_argument("--alpha", type=float, default=0.05, help="rejection level for both methods (default 0.05)")
    ap.add_argument("--self-test", action="store_true", help="run the known-case checks and exit")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()
    if args.file and args.pvalues:
        ap.error("give p-values as arguments or with --file, not both")
    if args.file:
        labels, pvalues = read_file(args.file)
    else:
        pvalues = list(args.pvalues)
        labels = [f"test {i + 1}" for i in range(len(pvalues))]
    if args.labels:
        given = [s.strip() for s in args.labels.split(",")]
        if len(given) != len(pvalues):
            ap.error(f"--labels has {len(given)} names for {len(pvalues)} p-values")
        labels = given
    if not pvalues:
        ap.error("no p-values given (or use --self-test)")
    if not (0 < args.alpha < 1):
        ap.error("--alpha must be between 0 and 1")
    check(pvalues)
    print(table(labels, pvalues, args.alpha))
    return 0


if __name__ == "__main__":
    sys.exit(main())
