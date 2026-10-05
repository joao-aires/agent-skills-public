#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
uv sync --frozen
uv run ruff check src tests ci migrations
uv run mypy src
uv run alembic upgrade head
uv run alembic check
uv run pytest
PYTHONPATH=src uv run python ci/export_schema.py
