#!/usr/bin/env bash
# Install and build steps for Vercel (called from vercel.json).
# Vercel's build image ships a uv-managed Python, which refuses plain
# `pip install` (PEP 668). Use uv when present; fall back to pip otherwise.
#
#   bash scripts/vercel_build.sh install
#   bash scripts/vercel_build.sh build
set -euo pipefail
mode="${1:-build}"

if command -v uv >/dev/null 2>&1; then
  case "$mode" in
    install) uv sync --frozen --no-dev ;;
    build)   uv run --frozen scripts/build_site.py ;;
    *) echo "unknown mode: $mode" >&2; exit 2 ;;
  esac
else
  case "$mode" in
    install) python3 -m pip install --break-system-packages -r requirements.txt ;;
    build)   python3 scripts/build_site.py ;;
    *) echo "unknown mode: $mode" >&2; exit 2 ;;
  esac
fi
