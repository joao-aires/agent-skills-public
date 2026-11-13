# Artifact homes: where an artifact lives

A **plane** is the artifact's role; a **home** is the place where its authoritative copy lives. They are different attributes. Architecture is a system-knowledge artifact; it usually lives in the application repository under `docs/architecture/`, but it may live in a separate architecture repository. A runbook is also system knowledge; it may live in `ops/<application>/runbooks/` rather than the application repository.

Use this reference to resolve the home before creating, moving or linking an artifact. The generic method belongs here. The actual home map belongs to the repository.

## Default homes and alternates

| Artifact | Default home | Allowed alternates |
| --- | --- | --- |
| Product brief / PRD | Product/project workspace | Application repository `docs/product/` when the team keeps product docs with code |
| Roadmap | Product/project workspace | Application repository `docs/product/roadmap.md` |
| ECR | Engineering workspace | Connected document provider; authorized filesystem or Git-backed workspace |
| Research report | Engineering workspace | Application repository only when the report is durable project knowledge and that home is authorized |
| RFC | Engineering workspace | Application repository `docs/decisions/` or `docs/rfcs/` when the proposal is durable project knowledge |
| Issue | Configured tracker | Application repository issue file only when explicitly agreed |
| PR | Git provider | — |
| Architecture set | Application repository `docs/architecture/` | Dedicated architecture repository for a multi-repo system |
| ADR / PDR | Application repository `docs/decisions/` | Engineering workspace while the decision is still proposed |
| API reference | Generated from the contract source, linked from `docs/reference/` | Dedicated reference site |
| Runbook | Operations repository `ops/<application>/runbooks/` | Application repository `docs/operations/` |
| SLO | Monitoring system or operations repository | Application repository `docs/operations/` |
| Release note / changelog | Git provider release or `CHANGELOG.md` | Application repository `docs/releases/` |
| README | Application repository root | Repo root plus component READMEs |
| Guide / tutorial | Application repository `docs/guides/` | Dedicated docs site |
| Glossary | Application repository `docs/glossary.md` | Docs site glossary |
| Code / tests / migrations | Application repository | Monorepo path or package repository |

The table gives a default, not a mandate. Preserve an established home. A second copy is not allowed to become a competing authority.

## Resolve the home

1. **Read project instructions and the existing documentation index.** Look for `AGENTS.md`, `CLAUDE.md`, the docs index, an artifact home map and explicit artifact links.
2. **Identify the artifact type and primary plane** using the [catalog](catalog.md) and [model](model.md).
3. **Use the established authoritative home** if one exists for that artifact and concern.
4. **If none exists**, choose the type's default home from the table above, within authorized scope. Ask before creating a new durable root, provider project or repository.
5. **Record a portable pointer** when the home is not obvious: in `AGENTS.md` for the repository, or in the project instructions for the engineering workspace. Prefer a repository-relative path or stable remote URL over a personal absolute path.
6. **Verify read/write access** and report the actual verified path, URL or revision. A tool call is not proof that the reader can open the artifact.
7. **Never create a competing authority** because another home is available or the configured one is temporarily unavailable. Report the blocker.

For coordination artifacts, [engineering workspace](../../engineering-workspace/SKILL.md) owns the storage mechanics and provider behavior. For repository artifacts, [project conventions](../../project-conventions/SKILL.md) owns the repository structure that contains them.

## Repository artifact home map

The repository should contain a small map that answers: where does each artifact type live, who owns it, and when must it change? Put a short pointer in `AGENTS.md` and the full map in `docs/README.md` or `docs/artifact-homes.md`.

```markdown
## Artifact homes

| Artifact | Home | Authority | Owner | Update when |
| --- | --- | --- | --- | --- |
| Product brief / PRD | `docs/product/` | Canonical product intent | Product lead | Outcome, scope or priority changes |
| Architecture set | `docs/architecture/` | Canonical implemented architecture | Architect | Boundary, interface or deployment changes |
| ADRs | `docs/decisions/` | Canonical decision history | Architect / tech lead | A consequential decision is accepted or superseded |
| API reference | Generated from `openapi/`, linked from `docs/reference/` | Canonical contract | Backend lead | Contract changes |
| Runbooks | `ops/<application>/runbooks/` | Canonical operations | SRE | Failure, recovery or escalation changes |
| Guides / tutorials | `docs/guides/` | Canonical how-to | Docs owner | Workflow or command changes |
| ECR | `../engineering/changes/<name>/ecr.md` | Canonical change record | Change owner | Each phase |
| Issue / PR | Tracker / Git provider | Views of the change | Change owner | Status or diff changes |
| Code / tests | `src/`, `tests/` | Canonical implementation | Engineering | Every change |
```

The map is an artifact with its own qualities:

- It is discoverable from `AGENTS.md` and the docs index.
- It names the authoritative home, not every possible copy.
- It records the owner and the update trigger.
- It is updated when a new artifact type, home or owner appears, or when a home moves.
- It does not copy the artifacts themselves.

Start with the types the project actually uses. Do not create an empty folder checklist. A tiny project may need only a README, a docs index and an ADR folder.

## Update triggers

| Change | Check and update |
| --- | --- |
| User-visible behavior or scope | PRD, acceptance criteria, affected UX or journey |
| System boundary, dependency or interface | Architecture set, contracts, consequential ADR |
| Persistence or ownership | Data model, generated schema or API contract, migration and recovery notes |
| Configuration or deployment | Setup commands, environment variables, runbook |
| Verification boundary | Journey coverage, known gaps, test evidence |
| Critical journey, dependency or retry behavior | SLO/indicators, telemetry gaps, alert and runbook assumptions |
| Release or incident | Release note, runbook, postmortem, follow-up decision |
| New or moved artifact home | Repository artifact home map and its `AGENTS.md` pointer |

## Setup and implementation

- **Setup** establishes or verifies the map. It should not invent a full documentation portfolio; it starts with the artifact types that exist.
- **Develop and implementation** read the map before creating or moving a durable artifact, resolve the intended home and authority, and update the map when a home or owner changes.
- **Release and operations** update the mapped release note, runbook, SLO or incident record.
- **Assurance** checks the map for drift, competing authorities and stale triggers.

## Local-only and published homes

A local-only artifact is not automatically a durable authority. If a revision is not published, write `repo/path@<full-sha>`, the branch and worktree, and "not published; no URL". If the artifact is published, use a resolvable link in that publication context. The [quality bar](quality-bar.md#4-resolvable-navigation) owns the link forms.

Do not migrate a configured authority because it is temporarily unavailable. Preserve the identity, report the access blocker and continue independent work. If migration is genuinely required, make it an explicit authorized decision.
