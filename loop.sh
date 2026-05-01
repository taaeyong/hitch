#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

if command -v python3 >/dev/null 2>&1; then
  PYTHON=python3
elif command -v python >/dev/null 2>&1; then
  PYTHON=python
else
  echo "python is required" >&2
  exit 1
fi

MODE="${1:-rehearse}"
shift || true

case "$MODE" in
  prepare)
    exec "$PYTHON" -m hitch.demo prepare "$@"
    ;;
  simulation)
    exec "$PYTHON" -m hitch.demo simulation "$@"
    ;;
  demo|telegram)
    exec "$PYTHON" -m hitch.demo demo "$@"
    ;;
  rehearse)
    "$PYTHON" -m hitch.demo prepare
    "$PYTHON" -m hitch.demo simulation "$@"
    "$PYTHON" -m hitch.demo demo --once
    ;;
  loop)
    "$PYTHON" -m hitch.demo prepare
    "$PYTHON" -m hitch.demo simulation --turns 3 "$@"
    "$PYTHON" -m hitch.demo demo --once
    ;;
  *)
    echo "usage: ./loop.sh [prepare|simulation|demo|telegram|rehearse|loop]" >&2
    exit 1
    ;;
esac
