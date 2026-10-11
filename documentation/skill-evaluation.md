# Evaluation evidence and limits

This page summarizes checks recorded during the plugin refactor and conventions work through 2026-10-11. It is evidence about packaging, discovery and interpretation of guidance, not certification of applications built with it. Earlier revisions and detailed notes remain in Git history.

## Package checks

The latest conventions revision passed nine helper regression tests, metadata/containment validation, both skill-creator checks and local-link/whitespace checks. All seven bundles built with 45 pinned upstream skills (63 skills total); the final frontend/backend framing changes were followed by a rebuild of those two bundles.

Regression coverage includes attribution-preserving metadata conversion, complete pinned acquisition/resources/notices, rejection of malformed metadata, workflow/frontend/backend framing, portable inline adversarial review, refusal to overwrite a build destination, and managed-link repair without replacing unrelated paths. Upstream scripts are not executed during packaging.

Run the maintained checks with:

```bash
python scripts/validate_plugins.py
python -m unittest discover -s tests -v
```

The SDLC SVG was rendered and inspected during its layout revisions. Subsequent changes replaced skill labels without altering geometry.

## Client discovery

GitHub Copilot CLI 1.0.95 was exercised in isolated configuration directories without modifying the user's settings or starting an authenticated model session.

- Before the Tailwind addition, direct installation and repeated session-local `--plugin-dir` loading exposed all seven bundles and 62 skills. Installed package files matched their sources byte-for-byte, including resources, invocation metadata and licenses.
- After the convention rename/Tailwind addition, session-local mounts exposed five frontend and three backend skills, including both new names.
- Direct-install reinstallation dropped an unrelated inventory entry in one configuration. A fresh installation succeeded; usage guidance prefers session-local loading for rebuilt bundles.

VS Code setup follows its official documentation and was not executed here. Discovery does not establish automatic skill selection, instruction enforcement or live tool behavior in every client.

## Independent task exercises

Fresh agents received skills and task-local facts without expected answers or the preceding design discussion. Except for the local Git exercise below, these were plan-only: no application implementation, deployment, provider calls or outreach.

| Scenario | Observed interpretation |
| --- | --- |
| New private appointments application | One persisted slice, scoped instructions, useful docs and practical CI; deferred unrelated features and tracker setup. |
| Unsafe saved-search proposal | Identified ownership, partial-commit and migration issues; distinguished real persistence evidence from mocked browser behavior. |
| Existing shadcn mobile/deletion defect | Reused tokens/components and proposed semantic controls, recovery behavior and relevant keyboard/mobile checks. |
| Portuguese audio transcription | Chose a direct adapter, deterministic authorization and bounded retries; separated fixture checks from live quality and named missing evaluation inputs. |
| EKS/RDS/S3 delivery and recovery | Proposed immutable promotion, staged schema compatibility and isolated restoration; separated code rollback from data recovery. |
| GKE capacity, feedback and sharing | Identified a possible 320-connection budget against a 200 limit, rejected snapshot-based rightsizing, qualified feedback counts and kept AKS guidance out of GKE. |
| New dashboard / existing Vite booking site | Applied appropriate shells while preserving existing Tailwind v3, branding and framework choices. |
| Tenant API with exports / local SQLite AI app | Proposed authority, atomicity, durability and failure checks while preserving contextual persistence and deployment. |
| New MCP interface with existing mypy/pre-commit | Selected standalone FastMCP, preserved tooling and distinguished SDK examples from standalone auth/Context/lifecycle APIs. |

## Git contribution checks

An agent implemented a small sorting feature in a disposable repository with a bare local remote and an unrelated user edit. Independent inspection confirmed a new feature worktree, passing focused checks, a Conventional Commit, a pushed branch and preservation of the original branch/user edit. It prepared a concise PR body without claiming a live GitHub PR.

A separate fork/PR planning exercise reused an existing worktree and PR, selected the correct upstream target and fork head, respected component scopes and an existing issue reference, and disclosed untested recovery. No remote action was executed in that planning case.

## What remains unproven

These checks do not establish a working full-stack application, model quality, deployment/restore success, measured savings, legal compliance or general reliability. The desired 90–95% avoidance of reference browsing is a design goal, not a measured result. Detailed observability/incident/SLO and load/failure-testing guidance remains pending.

Improve guidance from actual application outcomes: inspect the implemented journey, run relevant tests, review rendered UI and docs, then capture observed deviations in the appropriate skill or project check.
