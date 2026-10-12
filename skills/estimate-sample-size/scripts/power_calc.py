#!/usr/bin/env python3
"""power_calc.py: sample size, minimum detectable effect, and Type S/M risk
for two-arm trials.

Standard normal-approximation formulas for a two-arm, equal-allocation
comparison with individual or cluster randomization and a binary or
continuous outcome. Inflates the sample for imperfect take-up and for
attrition, deflates it for covariate adjustment, and reports Gelman and
Carlin's Type S (wrong sign) and Type M (exaggeration) risk for a stated
true effect. Standard library only; Python 3.8+.

Formulas (z_a = upper alpha/2 normal quantile, z_b = power quantile):
  continuous:  n_ind = 2 * (z_a + z_b)^2 / d^2                  per arm
  binary:      n_ind = (z_a * sqrt(2 * pbar * qbar)
                        + z_b * sqrt(p0*q0 + p1*q1))^2 / (p1 - p0)^2
  design effect: DE = 1 + (m - 1) * icc
  per-arm enrollment: n = n_ind * (1 - r2) * DE / takeup_diff^2 / (1 - attrition)
  clusters per arm: ceil(n / m)
The minimum detectable effect for a fixed sample inverts the same formulas
(closed form for a continuous outcome, bisection for a binary one).

Self-test (python power_calc.py --self-test):
  Continuous outcome, d = 0.20, alpha = 0.05 two-sided, power = 0.80,
  individual randomization: 2 * (1.960 + 0.842)^2 / 0.04 = 392.4, so the
  script returns 393 per arm. Textbook tables that use the t distribution
  give 394; the brief's "about 394 per arm" is the same case.
  Binary outcome, p0 = 0.30, p1 = 0.40, same alpha and power: 356 per arm,
  the standard uncorrected two-proportion result.
  Cluster check: d = 0.20 with m = 40 and icc = 0.10 gives DE = 4.9,
  1923 enrolled per arm (392.4 x 4.9 = 1922.8), 49 clusters per arm.

Examples:
  python power_calc.py --outcome continuous --effect 0.20
  python power_calc.py --outcome binary --p0 0.35 --p1 0.41 --icc 0.05 \
      --cluster-size 40 --attrition 0.10 --r2 0.10
  python power_calc.py --outcome binary --p0 0.35 --p1 0.41 --icc 0.05 \
      --cluster-size 40 --attrition 0.10 --r2 0.10 --clusters-per-arm 30 \
      --sensitivity --true-effect 0.06
"""
from __future__ import annotations

import argparse
import math
import sys
from typing import List, Optional


# ---------------------------------------------------------------------------
# Normal distribution helpers (no scipy)
# ---------------------------------------------------------------------------

def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def norm_pdf(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def norm_ppf(p: float) -> float:
    """Inverse normal CDF by bisection; accurate to about 1e-10."""
    if not 0.0 < p < 1.0:
        raise ValueError("probability must be strictly between 0 and 1")
    lo, hi = -40.0, 40.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if norm_cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------------------
# Core formulas
# ---------------------------------------------------------------------------

def n_ind_continuous(d: float, z_a: float, z_b: float) -> float:
    return 2.0 * (z_a + z_b) ** 2 / (d * d)


def n_ind_binary(p0: float, p1: float, z_a: float, z_b: float) -> float:
    pbar = 0.5 * (p0 + p1)
    num = z_a * math.sqrt(2.0 * pbar * (1.0 - pbar)) + z_b * math.sqrt(p0 * (1.0 - p0) + p1 * (1.0 - p1))
    return num * num / (p1 - p0) ** 2


def design_effect(m: float, icc: float) -> float:
    return 1.0 + (m - 1.0) * icc


def inflate(n_ind: float, r2: float, de: float, takeup_diff: float, attrition: float) -> float:
    """Per-arm enrollment needed so the analyzed sample delivers n_ind of information."""
    return n_ind * (1.0 - r2) * de / (takeup_diff ** 2) / (1.0 - attrition)


def deflate(n_enrolled: float, r2: float, de: float, takeup_diff: float, attrition: float) -> float:
    """Information-equivalent individual-level n from an enrolled per-arm sample."""
    return n_enrolled * (takeup_diff ** 2) * (1.0 - attrition) / ((1.0 - r2) * de)


def mdes_continuous(n_eff: float, z_a: float, z_b: float) -> float:
    return (z_a + z_b) * math.sqrt(2.0 / n_eff)


def mdes_binary(p0: float, n_eff: float, z_a: float, z_b: float, direction: str) -> float:
    """Smallest |p1 - p0| detectable with n_eff per arm, by bisection."""
    sign = 1.0 if direction == "increase" else -1.0
    lo, hi = 1e-6, (1.0 - p0 - 1e-6) if sign > 0 else (p0 - 1e-6)
    if hi <= lo:
        return float("nan")
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if n_ind_binary(p0, p0 + sign * mid, z_a, z_b) > n_eff:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def retrodesign(true_effect: float, se: float, z_a: float) -> dict:
    """Gelman and Carlin (2014): power, Type S, and Type M for a true effect and SE."""
    t = true_effect / se
    p_hi = 1.0 - norm_cdf(z_a - t)
    p_lo = norm_cdf(-z_a - t)
    power = p_hi + p_lo
    type_s = p_lo / power if power > 0 else float("nan")
    # E[|estimate| | significant] in closed form from truncated-normal moments.
    a_hi = (z_a * se - true_effect) / se
    a_lo = (-z_a * se - true_effect) / se
    e_hi = true_effect * (1.0 - norm_cdf(a_hi)) + se * norm_pdf(a_hi)
    e_lo = -true_effect * norm_cdf(a_lo) + se * norm_pdf(a_lo)
    exaggeration = (e_hi + e_lo) / (power * true_effect) if power > 0 and true_effect != 0 else float("nan")
    return {"power": power, "type_s": type_s, "type_m": exaggeration}


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def fmt_effect(args, value: float) -> str:
    if args.outcome == "binary":
        return f"{100 * value:.1f} pp"
    if args.sd:
        return f"{value * args.sd:.3f} raw ({value:.3f} SD)"
    return f"{value:.3f} SD"


def planned_effect(args) -> float:
    if args.outcome == "binary":
        return args.p1 - args.p0
    return args.effect / args.sd if args.sd else args.effect


def n_ind_for(args, effect: float, z_a: float, z_b: float) -> float:
    if args.outcome == "binary":
        return n_ind_binary(args.p0, args.p0 + effect, z_a, z_b)
    return n_ind_continuous(effect, z_a, z_b)


def required_sample(args, effect: float, icc: float, z_a: float, z_b: float) -> dict:
    de = design_effect(args.cluster_size, icc)
    n_ind = n_ind_for(args, effect, z_a, z_b)
    n = inflate(n_ind, args.r2, de, args.takeup - args.control_takeup, args.attrition)
    return {
        "n_ind": n_ind,
        "de": de,
        "n_per_arm": math.ceil(n),
        "clusters_per_arm": math.ceil(n / args.cluster_size),
    }


def mdes_for(args, n_enrolled: float, icc: float, z_a: float, z_b: float) -> float:
    de = design_effect(args.cluster_size, icc)
    n_eff = deflate(n_enrolled, args.r2, de, args.takeup - args.control_takeup, args.attrition)
    if args.outcome == "binary":
        return mdes_binary(args.p0, n_eff, z_a, z_b, args.direction)
    return mdes_continuous(n_eff, z_a, z_b)


def se_for(args, effect: float, n_enrolled: float, icc: float) -> float:
    de = design_effect(args.cluster_size, icc)
    n_eff = deflate(n_enrolled, args.r2, de, args.takeup - args.control_takeup, args.attrition)
    if args.outcome == "binary":
        p1 = args.p0 + effect
        return math.sqrt((args.p0 * (1 - args.p0) + p1 * (1 - p1)) / n_eff)
    return math.sqrt(2.0 / n_eff)


def parse_grid(text: Optional[str], default: List[float]) -> List[float]:
    if not text:
        return default
    return [float(x) for x in text.split(",") if x.strip()]


def run(args) -> int:
    z_a = norm_ppf(1.0 - args.alpha / 2.0)
    z_b = norm_ppf(args.power)
    effect = planned_effect(args)
    takeup_diff = args.takeup - args.control_takeup
    if takeup_diff <= 0:
        sys.stderr.write("take-up in treatment must exceed take-up in control\n")
        return 2
    fixed = args.n_per_arm or (args.clusters_per_arm * args.cluster_size if args.clusters_per_arm else None)

    print(f"outcome: {args.outcome}; alpha {args.alpha} two-sided (z = {z_a:.3f}); power {args.power} (z = {z_b:.3f})")
    if args.outcome == "binary":
        print(f"baseline p0 = {args.p0:.3f}; planned p1 = {args.p1:.3f}; planned effect = {fmt_effect(args, effect)}")
    else:
        print(f"planned effect = {fmt_effect(args, effect)}")
    print(f"cluster size m = {args.cluster_size}; icc = {args.icc}; design effect = {design_effect(args.cluster_size, args.icc):.3f}")
    print(f"take-up diff = {takeup_diff:.2f}; attrition = {args.attrition:.2f}; covariate r2 = {args.r2:.2f}")
    print()

    req = required_sample(args, effect, args.icc, z_a, z_b)
    print("REQUIRED SAMPLE for the planned effect")
    print(f"  individual-level n per arm (no adjustments): {req['n_ind']:.1f}")
    print(f"  x (1 - r2) = {1 - args.r2:.2f}; x DE = {req['de']:.3f}; / takeup_diff^2 = {takeup_diff ** 2:.3f}; / (1 - attrition) = {1 - args.attrition:.2f}")
    print(f"  enrolled per arm: {req['n_per_arm']}")
    if args.cluster_size > 1:
        print(f"  clusters per arm: {req['clusters_per_arm']} (total {2 * req['clusters_per_arm']})")
    print()

    if fixed:
        md = mdes_for(args, fixed, args.icc, z_a, z_b)
        print(f"MINIMUM DETECTABLE EFFECT for {fixed:.0f} enrolled per arm"
              + (f" ({args.clusters_per_arm} clusters per arm)" if args.clusters_per_arm else ""))
        print(f"  MDES = {fmt_effect(args, md)}")
        if args.outcome == "binary":
            sd0 = math.sqrt(args.p0 * (1 - args.p0))
            print(f"  = {md / sd0:.3f} SD of the baseline outcome (sd = sqrt(p0(1-p0)) = {sd0:.3f})")
        verdict = "CAN" if md <= abs(effect) + 1e-12 else "CANNOT"
        print(f"  verdict: the fixed sample {verdict} detect the planned effect of {fmt_effect(args, effect)} at the stated power")
        print()

    if args.sensitivity:
        iccs = parse_grid(args.icc_grid, [0.01, 0.05, 0.10, 0.20] if args.cluster_size > 1 else [args.icc])
        mults = parse_grid(args.effect_grid, [0.5, 0.75, 1.0, 1.5])
        unit = "clusters per arm" if args.cluster_size > 1 else "enrolled per arm"
        print(f"SENSITIVITY: required {unit} by icc (rows) and effect (columns)")
        header = "icc".ljust(8) + "".join(fmt_effect(args, effect * k).rjust(20) for k in mults)
        print("  " + header)
        for icc in iccs:
            row = f"{icc:<8.3f}"
            for k in mults:
                r = required_sample(args, effect * k, icc, z_a, z_b)
                row += str(r["clusters_per_arm"] if args.cluster_size > 1 else r["n_per_arm"]).rjust(20)
            print("  " + row)
        if fixed:
            print(f"  MDES for the fixed sample by icc: "
                  + "; ".join(f"icc {icc:.2f}: {fmt_effect(args, mdes_for(args, fixed, icc, z_a, z_b))}" for icc in iccs))
        print()

    if args.true_effect is not None:
        if not fixed:
            print("TYPE S / TYPE M: give --n-per-arm or --clusters-per-arm so the design is fixed")
        else:
            te = args.true_effect / args.sd if (args.outcome == "continuous" and args.sd) else args.true_effect
            se = se_for(args, te, fixed, args.icc)
            rd = retrodesign(te, se, z_a)
            print(f"TYPE S / TYPE M RISK if the true effect is {fmt_effect(args, te)} (Gelman and Carlin 2014)")
            print(f"  standard error of the estimate: {fmt_effect(args, se)}")
            print(f"  power at that true effect: {rd['power']:.2f}")
            print(f"  Type S: P(wrong sign | significant) = {rd['type_s']:.3f}")
            print(f"  Type M: expected |estimate| / true effect, given significance = {rd['type_m']:.2f}")
            print()
    return 0


def self_test() -> int:
    z_a, z_b = norm_ppf(0.975), norm_ppf(0.80)
    checks = []
    n1 = math.ceil(n_ind_continuous(0.20, z_a, z_b))
    checks.append(("continuous d=0.20 -> 393 per arm", n1 == 393, n1))
    n2 = math.ceil(n_ind_binary(0.30, 0.40, z_a, z_b))
    checks.append(("binary 0.30 -> 0.40 -> 356 per arm", n2 == 356, n2))
    de = design_effect(40, 0.10)
    n3 = math.ceil(n_ind_continuous(0.20, z_a, z_b) * de)
    checks.append(("cluster m=40 icc=0.10 -> DE 4.9, 1923 per arm, 49 clusters", abs(de - 4.9) < 1e-9 and n3 == 1923 and math.ceil(n3 / 40) == 49, (de, n3, math.ceil(n3 / 40))))
    md = mdes_continuous(393, z_a, z_b)
    checks.append(("MDES at 393 per arm -> 0.200 SD", abs(md - 0.20) < 0.001, round(md, 4)))
    rd = retrodesign(0.20, 0.20 / 2.802, z_a)
    checks.append(("retrodesign power ~0.80 when effect = 2.80 SE", abs(rd["power"] - 0.80) < 0.005, round(rd["power"], 3)))
    ok = True
    for label, passed, got in checks:
        print(("PASS " if passed else "FAIL ") + label + f" (got {got})")
        ok = ok and passed
    print("self-test " + ("passed" if ok else "FAILED"))
    return 0 if ok else 1


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter, epilog="\n".join(__doc__.split("\n\n")[1:]))
    ap.add_argument("--outcome", choices=["continuous", "binary"], help="outcome type")
    ap.add_argument("--effect", type=float, help="continuous: planned effect in SD units, or raw units if --sd is given")
    ap.add_argument("--sd", type=float, help="continuous: outcome SD, so --effect and --true-effect are read as raw units")
    ap.add_argument("--p0", type=float, help="binary: control-arm rate (0-1)")
    ap.add_argument("--p1", type=float, help="binary: treatment-arm rate (0-1)")
    ap.add_argument("--alpha", type=float, default=0.05, help="two-sided significance level (default 0.05)")
    ap.add_argument("--power", type=float, default=0.80, help="target power (default 0.80)")
    ap.add_argument("--icc", type=float, default=0.0, help="intracluster correlation (default 0)")
    ap.add_argument("--cluster-size", type=float, default=1, help="units measured per cluster (default 1 = individual randomization)")
    ap.add_argument("--takeup", type=float, default=1.0, help="share of the treatment arm that takes up the treatment (default 1)")
    ap.add_argument("--control-takeup", type=float, default=0.0, help="share of the control arm that gets the treatment anyway (default 0)")
    ap.add_argument("--attrition", type=float, default=0.0, help="share of enrolled units lost before outcome measurement (default 0)")
    ap.add_argument("--r2", type=float, default=0.0, help="share of outcome variance explained by covariates (default 0)")
    ap.add_argument("--n-per-arm", type=float, help="fixed enrolled sample per arm: report the MDES instead of required n")
    ap.add_argument("--clusters-per-arm", type=float, help="fixed clusters per arm (with --cluster-size): report the MDES")
    ap.add_argument("--direction", choices=["increase", "decrease"], default="increase", help="binary MDES: direction of the effect (default increase)")
    ap.add_argument("--sensitivity", action="store_true", help="print the required sample over an icc x effect grid")
    ap.add_argument("--icc-grid", help="comma-separated icc values for --sensitivity")
    ap.add_argument("--effect-grid", help="comma-separated multipliers of the planned effect for --sensitivity (default 0.5,0.75,1,1.5)")
    ap.add_argument("--true-effect", type=float, help="report Type S / Type M risk if this is the true effect (needs a fixed sample)")
    ap.add_argument("--self-test", action="store_true", help="run the known-case checks and exit")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()
    if not args.outcome:
        ap.error("--outcome is required (or use --self-test)")
    if args.outcome == "binary":
        if args.p0 is None or args.p1 is None:
            ap.error("binary outcome needs --p0 and --p1")
        if not (0 < args.p0 < 1 and 0 < args.p1 < 1) or args.p0 == args.p1:
            ap.error("--p0 and --p1 must be between 0 and 1 and differ")
    else:
        if args.effect is None or args.effect == 0:
            ap.error("continuous outcome needs a non-zero --effect")
    if not (0 < args.alpha < 1 and 0 < args.power < 1):
        ap.error("--alpha and --power must be between 0 and 1")
    if args.cluster_size < 1 or not (0 <= args.icc < 1):
        ap.error("--cluster-size must be >= 1 and --icc in [0, 1)")
    if not (0 <= args.attrition < 1 and 0 <= args.r2 < 1):
        ap.error("--attrition and --r2 must be in [0, 1)")
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
