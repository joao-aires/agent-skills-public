# Real-stack verification

Committed journey: applications/web/tests/e2e/notes.spec.ts. Runs production Next.js plus FastAPI against a migrated isolated PostgreSQL database, actual Argon2/DB session authentication, and no internal API route mocks. Assertions: registration, note creation, reload persistence, logout denial, login persistence, second-account isolation and direct-ID denial, invalid-input rejection, cross-origin rejection, mobile overflow. API tests additionally prove session revocation. External providers are absent from this slice.

Use uv/pnpm frozen locks, run API ci/check.sh then web ci/check.sh. Playwright retains failure traces/screenshots in artifacts/e2e; reports in artifacts/report. Do not weaken assertions, skip the journey or accept new screenshots to make a failure pass. Artifacts may contain synthetic credentials/session data: keep retention short and access restricted.
