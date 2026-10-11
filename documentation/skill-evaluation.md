# Evaluation evidence and limits

Checks through 2026-10-11 cover packaging, client discovery and how agents interpreted the guidance. They do not establish the quality of applications built with the plugins. Git history contains the earlier revisions and detailed notes.

## Package checks

The conventions revision before curation passed nine helper regression tests, metadata/containment validation, both skill-creator checks and local-link/whitespace checks. All seven bundles built with 45 pinned upstream skills (63 skills total); the final frontend/backend framing changes were followed by a rebuild of those two bundles.

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

Fresh agents received the skills and facts for each task, without expected answers or the prior design discussion. Only the local Git exercise executed changes. The other exercises produced plans, with no implementation, deployment, provider calls or outreach.

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

Application implementation, model quality, deployment, restoration, savings and legal compliance still need their own evidence. I have not measured the target of avoiding reference browsing in 90 to 95% of routine uses. Detailed observability/incident/SLO and load/failure-testing guidance remains pending.

Improve guidance from actual application outcomes: inspect the implemented journey, run relevant tests, review rendered UI and docs, then capture observed deviations in the appropriate skill or project check.

## Humanizer and personal voice

Humanizer was installed in the working agent environment and applied to the README, documentation pages and workflow prose. The edit preserves technical claims, commands, code, metadata and existing link targets. Repository-author references now use "I" and "my"; business/team quotations retain their speakers' voice.

Its MIT source is pinned at `225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8`, with complete resources and a workflow pointer in built bundles. Ten helper tests passed, including root-skill acquisition and rejection of a mismatched tree. All seven bundles built with 46 upstream skills (64 skills total), and Copilot CLI discovered Humanizer in the workflow plugin. The revised lifecycle image was rendered and inspected. These checks cover packaging and availability; prose quality was reviewed manually, without an AI-detection score.

## Usage labels and upstream curation

A review of all 27 imported Matt skills retained 18 and removed nine workflows that duplicate local guidance or assume a router, tracker or separate workspace. Standard string metadata now labels each local/acquired skill's generic or stack-specific scope and preferred invocation, without changing native upstream invocation controls. MCP builder moved to the AI plugin; MCP-only work remains independent of model selection/evaluation.

Thirteen helper tests passed, including metadata-label integrity, removal of stale setup calls and self-contained AI framing. Seven bundles built with 37 upstream skills (55 skills total). Copilot CLI discovered all 55 plugin-sourced skills, with no excluded entries and MCP builder in the AI bundle. Independent plan-only exercises handled MCP without model dependencies and spec implementation without a tracker or parallel agents. Neither exercise implemented or ran an application.
