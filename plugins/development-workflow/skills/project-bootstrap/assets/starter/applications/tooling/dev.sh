#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../.."
uv run --directory applications/api uvicorn notes.main:app --app-dir src --host 127.0.0.1 --port 8000 &
api_pid=$!
pnpm --dir applications/web dev &
web_pid=$!
trap 'kill "$api_pid" "$web_pid" 2>/dev/null || true' EXIT INT TERM
wait -n "$api_pid" "$web_pid"
