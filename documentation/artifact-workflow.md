# Engineering artifacts and workspaces

Use an engineering change record (ECR) to carry a change from agreed scope to checked outcome. Use a standalone research report to answer a question and support a decision. Keep implemented architecture and operating knowledge with the application. An issue helps someone coordinate or do the work, and a PR helps someone review the actual contribution.

| Need | Owning guidance |
| --- | --- |
| Choose an activity and its stopping point | [Development workflow](../plugins/development/WORKFLOW.md) |
| Choose a PRD, RFC, ADR or research report | [Artifact types](../plugins/development/skills/engineering-artifacts/references/artifact-types.md) |
| Record an engineering change and check its evidence | [ECR content](../plugins/development/skills/engineering-artifacts/references/engineering-change-record.md) and [artifact assurance](../plugins/development/skills/engineering-artifacts/references/assurance.md) |
| Find a home and persist the record | [Engineering workspace](../plugins/development/skills/engineering-workspace/SKILL.md) |
| Hand work to an implementer or reviewer | [Issue and PR views](../plugins/development/skills/engineering-artifacts/references/audience-views.md) |
| Explain structure and interactions with accurate views | [Diagram lifecycle](../plugins/development/skills/engineering-artifacts/references/diagram-lifecycle.md) and [architecture documentation](../plugins/documentation/skills/architecture-documentation/SKILL.md) |
| Improve wording, navigation or presentation | [Documentation writing](../plugins/documentation/skills/documentation-writing/SKILL.md) |

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

**Why.** The consumer's in-process cache loses event identity on restart and cannot coordinate independent workers.

**Scope.** Compare local and shared durable stores. Exercise restart, worker contention and the uncertain result of an external send. Keep the investigation separate from a production implementation.

**Acceptance**

- Compare plausible storage options for one host and multiple hosts.
- Reproduce at least one durable claim and a crash around the receiver effect.
- Explain what the probe establishes, what remains unverified and which decision the team needs next.

**Result.** The local SQLite probe exercised the crash boundary. A production choice still depends on the receiver contract. Link the research report and preserve the acceptance criteria.

## Example architecture handoff

For asynchronous exports, use the repository's current container view and permission checks as the baseline. In the ECR or its RFC, show the proposed queue and worker and the sequence for rechecking permission before dispatch. Keep the diagram editable and confirm reviewers can open the rendered view. Once implementation is checked, update the relevant current views in the application repository and describe any differences from the proposal.

For a local language-selector persistence bug with the same state owner and interaction flow, a compact ECR can state why the existing views are unaffected and point to the failing and passing regression.
