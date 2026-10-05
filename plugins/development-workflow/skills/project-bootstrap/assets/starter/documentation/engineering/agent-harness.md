# Agent harness

Read root/scoped AGENTS and skill-routing, PRD, affected docs and package locks. Commands: bash applications/tooling/setup.sh; bash applications/tooling/dev.sh; bash applications/api/ci/check.sh; (cd applications/web && bash ci/check.sh). API/web checks are shared with CI. No mocked internal API in E2E. Changes to ORM require migration and data/schema docs; auth behavior requires negative tests; UI changes preserve semantic tokens/components and include mobile/keyboard review.
