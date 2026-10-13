# Choose a skill for the task

Read the project's AGENTS.md and accepted decisions, then choose skills for the requested work. Local guidance sets defaults; upstream skills supply compatible techniques. The [usage guide](https://github.com/joao-aires/agent-skills-public/blob/main/documentation/usage.md) lists activities, sources and generic/stack-specific labels.

## Invocation

User-invoked activities begin on request. Agent-invoked guidance supports work already requested. Local skills marked `both` can do either; their descriptions still define scope. For example, `project-conventions` starts full setup/reorganization only on request and guides focused upkeep during ordinary work. A plain-language request can express intent; client command syntax and enforcement vary.

Local activities include system mapping, interactive architecture exploration, reliability and observability reviews, incident response and learning, runbooks, credential and vulnerability reviews, operational upkeep, strategy, feedback analysis, architecture diagrams, presentations, security reviews, delivery design, recovery, capacity and cost planning. They can be requested directly. Frontend/backend/AI guidance, documentation, testing and contributions also support related work automatically.

Retained upstream user activities are `grill-me`, `grill-with-docs`, `to-questionnaire`, `to-spec`, `implement`, `implement-spec`, `improve-codebase-architecture`, `retro` and `handoff`. Supporting techniques are `grilling`, `domain-modeling`, `codebase-design`, `research`, `prototype`, `tdd`, `code-review`, `diagnosing-bugs` and `writing-for-agents`. `humanizer` edits prose across the lifecycle.

## Project fit

- Let scope and existing decisions determine depth. Routine changes can go straight to implementation; interviews, specs and parallel orchestration are choices. Keep specs proportionate to the feature instead of producing an exhaustive story catalogue.
- Tickets and trackers are optional. Use the agreed conversation, Markdown spec or plan as scope. Treat the work graph in `implement-spec` as dependency-ordered slices; this can stay in a local plan without creating tickets. Use tracker operations only when explicitly requested and already configured. No upstream setup skill is required.
- `implement` uses `tdd` where appropriate and finishes with `code-review`. `implement-spec` needs supported subagents/worktrees for parallel execution; use a simpler supported approach otherwise. Research and review can run inline if the client cannot delegate. Do not claim unavailable orchestration ran.
- Retain existing answers and authorization. Ask about unresolved product/authority decisions; choose reversible implementation details without repeated confirmation. Routine test boundaries already established by the project/request need no fresh approval.
- Apply `contribute-code` for feature development and Git/PR work. Use the worktree already serving the objective or create one from the intended base. Keep implementation, tests and docs together. Its concise PR conventions govern descriptions; add a diagram only when useful. No separate upstream PR template is bundled.
- Preserve project domain vocabulary, even when a design technique uses its own terms. Prototype artifacts and generated visual reports serve the requested exploration, not a mandatory workflow. A prototype's in-memory demo does not prove application persistence; record useful findings without requiring an issue.
- In new projects, keep knowledge under `documentation/`; preserve existing documented paths. Create glossary/ADR files only when useful. Built references map `docs/agents/` to `documentation/engineering/` and `docs/adr/` to `documentation/decisions/adr/`.
- Use `humanizer` for prose edits and `writing-for-agents` for instruction structure. Preserve the author's voice, supported claims, commands, metadata and link targets. For questionnaire work, draft the requested document; sending it needs explicit authorization.
- Upstream guidance grants no additional permission to publish, merge, deploy, send messages or access services. Packaging copies resources without running setup or integrations.

Assess affected contracts and operating consequences before implementing a change; use project-conventions without repeating project setup. Deliver-reliable-changes defines proportionate acceptance evidence and separates locally verified behavior from deployment claims. Backend/frontend conventions own production migration, job and runtime details. Preserve established answers and avoid making evaluation cases or record formats prerequisites for application work.

## Metadata and upstream adaptations

`metadata.scope` distinguishes `generic` from `stack-specific`; `metadata.stack` names relevant technologies. `metadata.invocation` records preferred `user`, `agent` or `both` usage. These are standard string metadata labels, not a custom execution engine. Native upstream invocation controls remain intact.

The bundle retains 18 reviewed Matt skills with their dependency resources. It excludes the router, tracker workflows, teaching workspace, clarification shortcut, scripted setup wizard and overlapping PR template; see [the review](https://github.com/joao-aires/agent-skills-public/blob/main/documentation/maintainer-reference.md#matt-pocock-selection). Packaging adds this workflow pointer and labels, adjusts the two documentation paths, and removes stale setup prerequisites from three retained skills. Inline differential review uses its included methodology instead of an unavailable named agent.

Compatibility and effective configuration belong in affected change assessment; use backend and delivery guidance for their checks. Use test-application-performance for demand and test-application-resilience for scoped failure/recovery. Suite upkeep, routine upgrades and retirement extend normal engineering work without requiring new platforms or a ticket system.
