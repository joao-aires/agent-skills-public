# Choose a skill for the task

Read the project's AGENTS.md and accepted decisions, then choose skills for the requested work. Local guidance sets defaults; upstream skills supply compatible techniques. The [usage guide](https://github.com/joao-aires/agent-skills-public/blob/main/documentation/usage.md) lists activities, sources and generic/stack-specific labels.

Read [task guidance](TASKS.md) for the task menu, end-to-end develop flow and interactive/unattended execution. Explicit-only tasks are not automatic substeps; supporting guidance supplies methods within the authorized objective.

## Invocation

User-invoked activities begin on request. Agent-invoked guidance supports work already requested. Local skills marked `both` can do either; their descriptions still define scope. For example, `project-conventions` starts full setup/reorganization only on request and guides focused upkeep during ordinary work. A plain-language request can express intent; client command syntax and enforcement vary.

Local activities include system mapping, interactive architecture exploration, reliability and observability reviews, incident response and learning, runbooks, credential and vulnerability reviews, operational upkeep, strategy, feedback analysis, architecture diagrams, presentations, security reviews, delivery design, recovery, capacity and cost planning. They can be requested directly. Frontend/backend/AI guidance, documentation, testing and contributions also support related work automatically.

Retained upstream user activities are `grill-me`, `grill-with-docs`, `to-questionnaire`, `to-spec`, `implement`, `implement-spec`, `improve-codebase-architecture`, `retro` and `handoff`. Supporting techniques are `grilling`, `domain-modeling`, `codebase-design`, `research`, `prototype`, `tdd`, `code-review`, `diagnosing-bugs` and `writing-for-agents`. Prose-editing expertise can support relevant work when available.

## Compose activities, methods and technical guidance

Activities own the requested engagement and stopping point. Reusable disciplines own decisions and evidence independent of a framework. Technical conventions apply those decisions to the accepted stack. Select only relevant guidance through TASKS.md and the observed inventory; a plugin is a delivery bundle and may contain more than one kind of expertise.

Product priorities, engineering requirements, system design and implementation sequencing are different decisions. Seek appropriate expertise for the concern and implementation evidence for the accepted stack through the client's observed inventory. Describe the needed capability rather than maintaining specialist names or plugin identifiers as a routing list. Read relevant guidance when available, check its fit and carry useful conclusions into the work. Native invocation controls and the requested stopping point still apply.

The requested activity owns the outcome. Without a matching specialist, use project instructions, accepted decisions, repository evidence, general expertise and appropriate primary sources, then verify against the same acceptance criteria. Missing guidance alone neither blocks work nor lowers the required design, implementation or verification standard. A real unresolved product decision or unavailable execution target can block dependent work; investigate facts, continue independent authorized work and state that precise boundary. Do not install, migrate, ask repeated permission or claim execution merely to work around an absent skill.

Use only supported discovery within the authorized workspace/client inventory. Descriptions are the portable selection surface; applicability metadata helps where exposed and does not implement routing or permissions. Required files within a bundle retain precise links. Optional cross-package expertise is found by capability, not a filesystem path or a dependency resolver.

A method may compare technologies when the choice is unresolved, but loading it does not accept a stack or replace existing project choices. Reuse sufficient accepted context and stop at the requested outcome. Workflow-help recommends a next activity without executing it; develop coordinates only an explicitly requested end-to-end engagement. No global router or scheduler is supplied.

## Project fit

- Let scope and existing decisions determine depth. Routine changes can go straight to implementation; interviews, specs and parallel orchestration are choices. Keep specs proportionate to the feature instead of producing an exhaustive story catalogue.
- Tickets and trackers are optional. Use the agreed conversation, Markdown spec or plan as scope. Treat the work graph in `implement-spec` as dependency-ordered slices; this can stay in a local plan without creating tickets. Use tracker operations only when explicitly requested and already configured. No upstream setup skill is required.
- `implement` uses `tdd` where appropriate and finishes with `code-review`. `implement-spec` needs supported subagents/worktrees for parallel execution; use a simpler supported approach otherwise. Research and review can run inline if the client cannot delegate. Do not claim unavailable orchestration ran.
- Retain existing answers and authorization. Ask about unresolved product/authority decisions; choose reversible implementation details without repeated confirmation. Routine test boundaries already established by the project/request need no fresh approval.
- Apply `git-contributions` for feature development and Git/PR work. Use the worktree already serving the objective or create one from the intended base. Keep implementation, tests and docs together. Its concise PR conventions govern descriptions; add a diagram only when useful. No separate upstream PR template is bundled.
- Preserve project domain vocabulary, even when a design technique uses its own terms. Prototype artifacts and generated visual reports serve the requested exploration, not a mandatory workflow. A prototype's in-memory demo does not prove application persistence; record useful findings without requiring an issue.
- In new projects, keep knowledge under `documentation/`; preserve existing documented paths. Create glossary/ADR files only when useful. Built references map `docs/agents/` to `documentation/engineering/` and `docs/adr/` to `documentation/decisions/adr/`.
- For architecture documentation and breakdowns, seek expertise in evidence-backed explanation: structural views, runtime/lifecycles, interfaces, deployment and evidence. Preserve existing formats and scope; diagrams alone do not establish coverage.
- For persistent product and engineering documents, seek reader-oriented writing and knowledge-upkeep expertise. Useful authoring methods cover reader purpose, explanation, examples, accuracy and presentation while preserving document responsibilities.
- Use available prose-editing expertise for text and `writing-for-agents` for instruction structure. Preserve the author's voice, supported claims, commands, metadata and link targets. For questionnaire work, draft the requested document; sending it needs explicit authorization.
- Upstream guidance grants no additional permission to publish, merge, deploy, send messages or access services. Packaging copies resources without running setup or integrations.

Assess affected contracts and operating consequences before implementing a change; use project-conventions without repeating project setup. Deliver-reliable-changes defines proportionate acceptance evidence and separates locally verified behavior from deployment claims. Service behavior/contracts and interface direction need their own design reasoning, supported by matching expertise when available. Technical conventions own the selected framework, persistence, configuration and runtime details. Preserve established answers and avoid making evaluation cases or record formats prerequisites for application work.

## Working boundaries

Keep chosen outputs and discovery inside the supplied scope, including during read-only assessment. Use the permitted destination for authored scripts, screenshots and reports; disclose a host-enforced conflict before substituting another location. Client-managed caches are distinct from outputs the agent chooses to write.

Establish integration capabilities through supported inventory, public documentation and the named authorized resource. Treat missing tools/authentication as a reported limit. Diagnostics require their own permitted scope; client profiles, unrelated conversations/logs and credential stores are not implied discovery sources.

## Protect changed boundaries

For affected identities, data and valuable actions, establish verified actor/resource authority, tenant boundaries, minimal data use and relevant failure/abuse cases. Enforce permissions at trusted boundaries, keep secrets out of public clients and logs, and verify relevant allowed/denied operations and sensitive-data handling. Available security/privacy expertise deepens this work; its absence does not remove these outcomes. Match the depth to the change and preserve accepted constraints.

## Resolve consequential findings

Apply this throughout product definition, architecture, implementation, testing, release and operation. Assess the actual changed boundaries and dependencies proportionately; a small edit does not trigger an exhaustive audit. Use relevant specialists to investigate licensing/usage, security/privacy, reliability/recovery, cost, compatibility, accessibility and other material constraints. New evidence can reopen an earlier decision.

Distinguish a fact to investigate, an implementation defect to fix within accepted constraints, and a tradeoff the user must decide. Verify technical facts from appropriate primary sources, code, configuration or bounded tests. Do not ask the user to guess those facts or treat an unexplained uncertainty as permission. Correct an ordinary defect and choose reversible implementation details within the established scope without repeated approval.

Ask when resolving a finding would change intended usage/distribution, budget or provider commitments, data handling/exposure, authorization, loss/recovery tolerance, service expectations, required functionality, or an accepted product/architecture decision—and the current instructions do not already settle it. A requested library or service does not imply acceptance of undisclosed obligations. Do not silently choose a weaker security/reliability outcome or change the product to fit a convenient dependency. Required safeguards and established authority remain constraints, not optional preferences to waive casually.

Present the concrete finding, its evidence and effect on the requested outcome, feasible options with tradeoffs, a recommendation and the specific unresolved decision. Record proposed versus accepted status in existing project notes; a risk mentioned in a report is not an accepted risk. Pause only work depending on that decision, continue independent authorized work and carry the answer into affected requirements, design, tests and delivery. Reuse existing answers; re-ask only when new evidence materially changes their premise. In unattended work return the precise needs-decisions result instead of inventing an answer or proceeding through the blocker.

Specialist skills own detection methods and technical evidence; this shared workflow owns when to ask, how to present the decision and what work may continue. No finding or skill expands authorization to purchase, accept terms, expose data, deploy, publish or contact others.

## Metadata and upstream adaptations

`metadata.scope` distinguishes `generic` from `stack-specific`; `metadata.stack` names relevant technologies. `metadata.invocation` records preferred `user`, `agent` or `both` usage. These are standard string metadata labels, not a custom execution engine. Native upstream invocation controls remain intact.

The bundle retains 18 reviewed Matt skills with their dependency resources. It excludes the router, tracker workflows, teaching workspace, clarification shortcut, scripted setup wizard and overlapping PR template; see [the review](https://github.com/joao-aires/agent-skills-public/blob/main/documentation/maintainer-reference.md#matt-pocock-selection). Packaging adds this workflow pointer and labels, adjusts the two documentation paths, and removes stale setup prerequisites from three retained skills. Inline differential review uses its included methodology instead of an unavailable named agent.

Compatibility and effective configuration belong in affected change assessment; seek matching service/delivery expertise for their checks. Use suitable workload expertise for demand and resilience-testing for scoped failure/recovery. Suite upkeep, routine upgrades and retirement extend normal engineering work without requiring new platforms or a ticket system.
