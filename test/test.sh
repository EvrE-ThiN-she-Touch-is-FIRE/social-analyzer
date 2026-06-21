#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"

if [ -x "$ROOT/.venv/bin/python" ]; then
  PYTHON_BIN="$ROOT/.venv/bin/python"
fi

if ! "$PYTHON_BIN" -c "from importlib import import_module; import_module('social-analyzer')" >/dev/null 2>&1; then
  "$PYTHON_BIN" -m pip install -e "$ROOT" -q
fi

if "$PYTHON_BIN" -m social-analyzer --list 2>&1 | grep -q 'languages.json & sites.json loaded successfully'; then
  echo "Good"
else
  echo "Bad"
  exit 1
fi