#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../.."
: "${DATABASE_URL:?Set DATABASE_URL}"
: "${POSTGRES_PASSWORD:?Set local POSTGRES_PASSWORD}"
docker compose up -d --wait database
(cd applications/api && uv sync --frozen && uv run alembic upgrade head)
(cd applications/web && pnpm install --frozen-lockfile)
