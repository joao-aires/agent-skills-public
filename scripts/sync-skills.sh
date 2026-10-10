#!/usr/bin/env bash
# Legacy skills-only fallback; does not install manifests or MCP components.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/sync_skills.py" "$@"
