# Choose a skill for the task

Local guidance sets project defaults; upstream skills supply techniques. Read the project's AGENTS.md and accepted decisions, then select the skills relevant to the requested work. Having a skill available does not require running its workflow.

## Invocation

**Agent-invoked** guidance helps execute an existing request and remains manually invocable. **User-invoked** skills start a distinct activity only when explicitly requested. A request in plain language can count where the client supports it; slash-command syntax is client-specific. Routers suggest user-invoked skills rather than starting them.

| Task | Skills available |
| --- | --- |
| Establish or maintain project foundations | Local `project-conventions`: full setup/reorganization on request; focused upkeep when the requested change affects conventions |
| Apply project conventions | Local documentation, E2E and delivery skills (agent-invoked); backend/frontend/AI guidance in the corresponding bundles |
| Clarify an idea | `grill-me`, `grill-with-docs`, `to-questionnaire` (user); `grilling`, `domain-modeling` support the requested session |
| Investigate or explore | `research`, `prototype`, `codebase-design` (agent, when relevant) |
| Plan substantial work | `to-spec`, `to-tickets`, `wayfinder` (user) |
| Execute agreed work | `implement`, `implement-spec` (user); `tdd` and `code-review` support execution |
| Develop and publish a contribution | Local `contribute-code` (agent): feature worktree, Conventional Commits and concise PR; upstream `pr` supports preparation |
| Build delivery infrastructure | Local `build-delivery-pipelines` (agent); GitHub Actions hardening supports detailed review |
| Design data and authority boundaries | Local `design-secure-features` (agent); security diff/dependency specialists when relevant |
| Plan recovery, capacity or cost | Local skills in `application-operations` (agent); AKS specialist only on AKS |
| Evaluate product outcomes | Local `learn-from-product-feedback` in `business-strategy` (agent for requested analysis) |
| Debug and review | `diagnosing-bugs`, `code-review`, `pr` (agent); use security/property-based specialists when warranted |
| Improve the environment | `improve-codebase-architecture`, `retro` (user); `writing-for-agents` (agent) |
| Navigate, hand off or learn | `ask-matt`, `handoff`, `wait-what`, `teach` (user) |
| Configure tools or tracker | `setup-matt-pocock-skills`, `triage` (user); `wizard` helps with requested human-only setup steps |

Research and clarification can support any phase or surrounding product activity. `research` is task-matched; `grill-me` remains an explicitly requested interaction, not an automatic questioning step. Project foundations and delivery pipelines are established once and maintained when relevant, while the SDLC repeatedly uses those capabilities.

## Project fit

- Let scope and existing project decisions determine depth. Routine changes can go straight to implementation; specs, tickets, interviews and parallel orchestration are choices for work that benefits from them.
- Tickets and issue trackers are optional. Use the agreed conversation, Markdown spec or plan as the scope. When a bundled skill requires tickets or tracker setup, apply it using that scope instead. Create or update tickets only when explicitly requested. This plugin guidance takes precedence over upstream ticket prerequisites.
- `implement` relies on `tdd` and `code-review`; parallel `implement-spec` execution needs subagent/worktree support. Check capabilities before choosing a workflow. If a client lacks them, report the limitation and use a simpler supported approach rather than claiming orchestration ran.
- Retain existing answers and authorization. Resolve material ambiguity; do not repeat an upstream confirmation step when the user already settled the decision.
- Apply `contribute-code` by default for feature development and Git/PR work. Create a feature worktree from the intended repository/base, or reuse the workspace already serving that objective; keep implementation, tests and docs there. Use it as the integration worktree for `implement`/`implement-spec`. Prefer CLI operations with MCP fallback; use optional issue references and concise PR explanations. These local contribution rules frame upstream implementation/PR skills without requiring tickets or another orchestration layer.
- In new projects, keep persistent knowledge under `documentation/`. Built Matt skills use `documentation/engineering/` for tracker/domain configuration and `documentation/decisions/adr/` for ADRs. Existing documented paths take precedence; preserve one authoritative glossary, which may remain at the root.
- Invoke setup only when choosing tracker-based workflows and configuration is needed. Local files are an option; no external tracker is mandatory. Packaging never runs setup, creates tickets, sends messages, commits application work or enables integrations.
- Authorization remains part of the application and client. Upstream instructions do not grant permission to publish, merge, send messages or access services beyond the user's requested scope.

Matt's released engineering/productivity skills are acquired with all resources and native invocation metadata. Their Markdown receives a pointer to this guide and the two documentation-path substitutions; `pr` credit values are normalized to standard string metadata. Differential security review uses its included inline adversarial methodology rather than an unregistered upstream agent. Ticket preferences live in this guide; upstream ticket instructions are preserved and interpreted using the project-fit rules above. Deprecated, experimental and miscellaneous tool-specific skills are excluded.
