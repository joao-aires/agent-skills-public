#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
pnpm install --frozen-lockfile
pnpm schema
pnpm lint
pnpm check
pnpm build
pnpm test:e2e
