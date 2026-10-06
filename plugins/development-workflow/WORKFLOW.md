# Choose a skill for the task

Local guidance sets project defaults; upstream skills supply techniques. Read the project's AGENTS.md and accepted decisions, then select the skills relevant to the requested work. Having a skill available does not require running its workflow.

## Invocation

**Agent-invoked** guidance helps execute an existing request and remains manually invocable. **User-invoked** skills start a distinct activity only when explicitly requested. A request in plain language can count where the client supports it; slash-command syntax is client-specific. Routers suggest user-invoked skills rather than starting them.

| Task | Skills available |
| --- | --- |
| Organize a project | Local `project-bootstrap` (user-invoked) |
| Apply project conventions | Local documentation, E2E and delivery skills (agent-invoked); backend/frontend/AI guidance in the corresponding bundles |
| Clarify an idea | `grill-me`, `grill-with-docs`, `to-questionnaire` (user); `grilling`, `domain-modeling` support the requested session |
| Investigate or explore | `research`, `prototype`, `codebase-design` (agent, when relevant) |
| Plan substantial work | `to-spec`, `to-tickets`, `wayfinder` (user) |
| Execute agreed work | `implement`, `implement-spec` (user); `tdd` and `code-review` support execution |
| Debug and review | `diagnosing-bugs`, `code-review`, `pr` (agent); use security/property-based specialists when warranted |
| Improve the environment | `improve-codebase-architecture`, `retro` (user); `writing-for-agents` (agent) |
| Navigate, hand off or learn | `ask-matt`, `handoff`, `wait-what`, `teach` (user) |
| Configure tools or tracker | `setup-matt-pocock-skills`, `triage` (user); `wizard` helps with requested human-only setup steps |

## Project fit

- Let scope and existing project decisions determine depth. Routine changes can go straight to implementation; specs, tickets, interviews and parallel orchestration are choices for work that benefits from them.
- `implement` relies on `tdd` and `code-review`; `implement-spec` also needs agreed tickets, tracker configuration and subagent/worktree support. Check capabilities before choosing a workflow. If a client lacks them, report the limitation and use a simpler supported approach rather than claiming orchestration ran.
- Retain existing answers and authorization. Resolve material ambiguity; do not repeat an upstream confirmation step when the user already settled the decision.
- In new projects, keep persistent knowledge under `documentation/`. Built Matt skills use `documentation/engineering/` for tracker/domain configuration and `documentation/decisions/adr/` for ADRs. Existing documented paths take precedence; preserve one authoritative glossary, which may remain at the root.
- Invoke setup only when choosing tracker-based workflows and configuration is needed. Local files are an option; no external tracker is mandatory. Packaging never runs setup, creates tickets, sends messages, commits application work or enables integrations.
- Authorization remains part of the application and client. Upstream instructions do not grant permission to publish, merge, send messages or access services beyond the user's requested scope.

Matt's released engineering/productivity skills are acquired with all resources and native invocation metadata. Their Markdown receives a pointer to this guide and the two documentation-path substitutions, recorded in the acquisition notices. Deprecated, experimental and miscellaneous tool-specific skills are excluded.
