# Engineering artifacts and workspaces

Every durable engineering output is an artifact: an ECR, PRD, roadmap, RFC, ADR, issue, PR, architecture view, runbook, README, guide, code module, test suite or release note. Each has a type, a primary plane, a home, an authority, a maturity and relations. The ECR is the coordination spine for a change, not the only artifact.

| Need | Owning guidance |
| --- | --- |
| Understand the artifact model, planes and relations | [Artifact model](../plugins/development/skills/artifact-system/references/model.md) |
| Choose the type, plane and contract | [Artifact catalog](../plugins/development/skills/artifact-system/references/catalog.md) |
| Resolve where an artifact lives, or establish the repository map | [Artifact homes](../plugins/development/skills/artifact-system/references/homes.md) and [project conventions](../plugins/development/skills/project-conventions/SKILL.md) |
| Choose an activity and its stopping point | [Activity system](../plugins/development/skills/activity-system/SKILL.md) |
| Record an engineering change and check its evidence | [ECR contract](../plugins/development/skills/artifact-system/references/contracts/ecr.md) and [artifact assurance](../plugins/development/skills/artifact-system/references/assurance.md) |
| Persist a coordination record | [Coordination storage](../plugins/development/skills/artifact-system/references/storage/coordination.md) |
| Hand work to an implementer or reviewer | [Issue contract](../plugins/development/skills/artifact-system/references/contracts/issue.md) and [PR contract](../plugins/development/skills/artifact-system/references/contracts/pr.md) |
| Document architecture as a set | [Architecture-set contract](../plugins/development/skills/artifact-system/references/contracts/architecture-set.md) and [system documentation](../plugins/development/skills/system-documentation/SKILL.md) |
| Write a runbook, README, guide or release note | [Runbook](../plugins/development/skills/artifact-system/references/contracts/runbook.md), [README](../plugins/development/skills/artifact-system/references/contracts/readme.md), [guide](../plugins/development/skills/artifact-system/references/contracts/guide.md), [release note](../plugins/development/skills/artifact-system/references/contracts/release-note.md) |
| Check sufficiency, links and rendered output | [Artifact quality bar](../plugins/development/skills/artifact-system/references/quality-bar.md) |
| Explain structure and interactions with accurate views | [Diagram lifecycle](../plugins/development/skills/artifact-system/references/diagram-lifecycle.md) |
| Improve wording, navigation or presentation | [Technical writing](../plugins/documentation/skills/technical-writing/SKILL.md) |

See the [SDLC overview](sdlc.md) for the seven outcomes and how evidence passes between them.

## Example workspace instructions

A project might record these instructions after authorizing a separate folder.

```text
Engineering workspace: resolve ../engineering from the application checkout.
Change records: reuse the existing record under changes/<name>/ecr.md.
Research: retain decision-oriented reports under research/.
Implemented architecture, contracts and runbooks: use the application's docs.
History: the engineering folder is independently versioned.
```

A connected document project can serve the same purpose. For the first storage choice, provider limits and access failures, follow the workspace method. In a mixed setup, an issue can repeat acceptance criteria and link the authoritative record even when the issue and record live in different tools.

## Planes and homes

Every artifact has a **primary plane** and a **home**:

- Intent: PRD, roadmap, product decision.
- Coordination: ECR, research report, RFC, issue, PR.
- System knowledge: architecture set, ADR, API reference, runbook, SLO.
- Implementation: code, tests, migrations, configuration.
- Delivery and operations: release note, deployment record, incident, postmortem.
- Entry and knowledge: README, guide, tutorial, glossary.

The plane is the artifact's role. The home is where its authoritative copy lives. They are different: an architecture view is system knowledge that usually lives in the application repository; a runbook is system knowledge that may live in an operations repository; an ECR is coordination knowledge that lives in the engineering workspace.

Read [artifact homes](../plugins/development/skills/artifact-system/references/homes.md) for the default homes, alternates and resolution method.

## Example repository artifact home map

A repository should record where its durable artifacts live. Put a short pointer in `AGENTS.md` and the full map in `docs/README.md` or `docs/artifact-homes.md`.

| Artifact | Home | Authority | Owner | Update when |
| --- | --- | --- | --- | --- |
| Product brief / PRD | `docs/product/` | Canonical product intent | Product lead | Outcome, scope or priority changes |
| Architecture set | `docs/architecture/` | Canonical implemented architecture | Architect | Boundary, interface or deployment changes |
| ADRs | `docs/decisions/` | Canonical decision history | Architect / tech lead | A consequential decision is accepted or superseded |
| Runbooks | `ops/<application>/runbooks/` | Canonical operations | SRE | Failure, recovery or escalation changes |
| Guides | `docs/guides/` | Canonical how-to | Docs owner | Workflow or command changes |
| ECR | `../engineering/changes/<name>/ecr.md` | Canonical change record | Change owner | Each phase |
| Issue / PR | Tracker / Git provider | Views of the change | Change owner | Status or diff changes |
| Code / tests | `src/`, `tests/` | Canonical implementation | Engineering | Every change |

`setup` establishes or verifies the map. Implementation reads it before creating or moving a durable artifact and updates it when a type, home or owner changes. A missing map is a project-foundation gap, not permission to choose an arbitrary path.

## Example research report

This example concerns a synthetic webhook consumer. Its question is whether the system can deduplicate work across process restarts and workers.

**Recommendation.** Use a durable receipt and dispatch intent in SQLite for a modest single-host installation. For multiple hosts, assess the existing relational primary. Confirm the real receiver's idempotency and lookup contract before accepting either design.

| Option | Fit | Main limit |
| --- | --- | --- |
| In-process map | One disposable worker | Restarts and separate workers lose shared identity |
| SQLite | Workers on one host with a durable local volume | Writer contention and volume recovery need testing |
| Shared relational database | Workers on multiple hosts | Availability and failover depend on the actual deployment |

**Observed evidence.** In the local probe, retry after an ambiguous send produced two effects with an unkeyed receiver and one effect when the simulated receiver enforced a stable key. Link the runnable probe and primary sources below the decision material. Keep measured local behavior separate from assumptions about the real receiver.

**Open decision.** The integration owner needs to confirm key scope, expiry and lookup semantics. The service owner needs to decide how to handle ambiguous sends. The recommendation remains proposed.

## Example issue

### Investigate durable webhook deduplication

**Context.** The consumer's in-process cache loses event identity on restart and cannot coordinate independent workers. The failing restart case and the current consumer baseline are linked in the research record.

**Intended outcome.** The team has a recommended durable storage approach for one host and a clear decision about the multi-host case, supported by observed evidence.

**Scope.** Compare local and shared durable stores. Exercise restart, worker contention and the uncertain result of an external send. Keep the investigation separate from a production implementation. Out of scope: changing the production consumer or deploying a database.

**Acceptance**

- Compare plausible storage options for one host and multiple hosts on the same dimensions.
- Reproduce at least one durable claim and a crash around the receiver effect.
- Explain what the probe establishes, what remains unverified and which decision the team needs next.

**Verification.** Run the local probe at the recorded fixture revision and retain its source and output. Record the exact environment and the cases the simulated receiver does not establish.

**References.** Research report, consumer baseline, receiver contract documentation and the related ECR if implementation follows.

**Result.** The local SQLite probe exercised the crash boundary. A production choice still depends on the receiver contract. Link the research report and preserve the acceptance criteria.

**Status.** Ready for investigation; owner to be assigned. The production choice remains blocked on the receiver contract.

## Example architecture handoff

For asynchronous exports, use the repository's current container view and permission checks as the baseline. In the ECR or its RFC, show the proposed queue and worker and the sequence for rechecking permission before dispatch. Keep the diagram editable and confirm reviewers can open the rendered view. Once implementation is checked, update the relevant current views in the application repository and describe any differences from the proposal.

For a local language-selector persistence bug with the same state owner and interaction flow, a compact ECR can state why the existing views are unaffected and point to the failing and passing regression.
