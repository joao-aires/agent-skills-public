# Project fit: scale the activity to the project

Let the requested outcome, existing decisions and actual repository determine the depth. Routine changes can go straight to implementation; interviews, specs, full design ceremonies and parallel orchestration are choices, not prerequisites.

## Proportionality

- A small fix needs a reproduction, a focused repair and observed verification, not a product study or a ticket graph.
- A new product needs enough outcome, feasibility, requirements and design evidence before irreversible commitments.
- An existing feature reuses accepted product, architecture and operating decisions; reopen only the affected ones.
- A subsystemic architecture change earns diagrams and an RFC. A styling fix should explain why they do not apply rather than fabricate them.
- Keep specs proportionate to the feature instead of producing an exhaustive story catalogue.

## Trackers and documents

- A tracker is optional. Use the agreed conversation, a local spec or a plan as scope.
- Use the ECR as the coordination artifact for a change; issues and PRs are audience views, not second authorities.
- Use the artifact system for type, contract, home and evidence. Resolve repository homes with the artifact home map.
- Do not create a ticket, PRD, RFC or ADR merely to fill a field.
- Keep durable project knowledge with its owner and update affected documents when their meaning changes.
- A request for an implementation breakdown stops at the breakdown. A request for a ticket uses the issue contract.

## Implementation and contribution

- Use [Git contributions](../../git-contributions/SKILL.md) for feature isolation, commits and concise PRs. An implementation objective uses its existing feature worktree or creates one.
- Keep source, tests and docs together; preserve unrelated edits.
- Explicit implementation includes creating the requested code, checks and commits within that flow, not only suggesting commands.
- If writing or refactoring is not requested, return findings or design instead.
- A conventional PR is a projection for reviewers, not a second ECR.

## New and existing projects

- For a new application, `develop` owns the end-to-end outcomes in [new-application flow](../../develop/references/new-application-flow.md); `setup` covers technical foundations.
- For an existing project, preserve the established layout, stack, identity, UI and operating constraints. Identify the affected boundary and update only that part.
- A named stack or starter kit does not supply missing product or design decisions.
- Keep docs discoverable: setup establishes the artifact home map; implementation reads it and updates it when a type, home or owner changes.

## UI, backend and operations depth

- For substantive UI work, establish interaction behavior and visual direction before dependent implementation; map affected routes, dialogs and shared patterns; verify coverage afterward.
- For backend work, establish actor authority, invariants, state/failure and public contracts before propagating code.
- For operations, use the affected journey to choose depth: authority, bounded calls/retries, diagnosable failure and recovery come before adding a monitoring platform.
- Ordinary copy, token or minor configuration edits need proportionate checks, not a full design ceremony.

## Stop and hand off

When the requested stopping point is reached, report the outcome, evidence and next decision. Do not continue into a later activity because its skill is available. If the conversation changes the stopping point, say so and apply the new activity explicitly.
