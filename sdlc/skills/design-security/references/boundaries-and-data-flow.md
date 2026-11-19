# Trust boundaries, data flow and exposure

Use this reference when a feature creates or moves a boundary, handles personal or sensitive data, or adds a provider, integration or delegated authority. It supports the security design method; it does not replace judgment about the specific application.

## Name the boundary

For every crossing, establish:

- which components, identities or organizations sit on each side;
- what crosses: requests, files, events, credentials, commands, model output, support actions;
- which trusted component validates the crossing, and what it rejects;
- whether this change creates a boundary, moves one, or changes who is trusted.

A new integration is a boundary even when it is a library call in the same process. A background job, export, admin tool or AI action can reach the same data without an HTTP route, so include it in the trace.

## Build a resource operation matrix

Use a small matrix when several actions need comparison. Trace the operation rather than treating every route as an interchangeable read or write.

| Column | What to establish |
| --- | --- |
| Actor | Human, service, support agent or delegated tool, and how that identity was verified |
| Exact resource | Object, owner, tenant and lifecycle state — not a client-supplied label |
| Precondition | The state in which this action is legitimate |
| Authority | Permission and policy that allow the action, and where it is checked |
| Effect | Data read or changed, side effects, notifications and audit record |
| Conflict and retry | Concurrent change, repeated request, uncertain result and idempotency |
| User-visible outcome | Success, denial, partial completion and what the user is told |

The purpose is to expose differences in authority and consequence that a generic endpoint checklist misses.

- Do not assume every resource permits generic CRUD.
- Publishing, finalizing, amending, revoking and correcting can have different authority and retention rules.
- Keep intended state, observed records and authorized transitions distinct.
- Keep business requirements separate from API implementation choices; scope the matrix to affected resources rather than inventing a universal workflow engine.

## Trace the data lifecycle

For each data class that appears or moves, record its purpose, recipients, storage location, retention and who can access it.

| Data class | Questions that change the design |
| --- | --- |
| Account, contact and profile | Is each field necessary for the journey? Who inside the service can read it? |
| User content and messages | Is raw content needed, or can it be aggregated, redacted or reduced? |
| Telemetry and logs | Which identifiers and payloads are captured, and who can query them? |
| Credentials and tokens | Where are they stored, who can use them, and how are they revoked? |
| Derived and model data | What is sent to a provider, retained there, or reused for another purpose? |
| Backups and exports | Does deletion propagate, and can deleted records return to active use? |

- Prefer minimal fields, aggregation and redaction over capturing raw messages, audio, tokens or search contents.
- Include providers, logs, analytics, caches, exports and backups in the flow; check regional storage and transfer requirements against the actual service configuration.
- Preserve the application's access, deletion and export behavior across integrations. Explain how retention and deletion interact with immutable backups and restoration.
- Treat a policy document as intent, not evidence that the configured service behaves that way.
- Do not present engineering checks as legal compliance. Route applicable obligations and evidence to [run-compliance-assessment](../../run-compliance-assessment/SKILL.md), and escalate unresolved lawful-basis or product choices.

## Follow delegation and credential ownership

Delegation is a design decision about whose authority is used, for which operations, and for how long.

- Trace each credential to its recipient, the operations it authorizes, and any redirect or delegated processor.
- Choose ownership from the deployment: distributed client code cannot keep a confidential application secret merely by receiving it through a build variable.
- Keep runtime read/pull access separate from build write access and administrative access.
- Prefer scoped workload identity or short-lived tokens to a shared long-lived secret for automation. Removing a workload does not automatically revoke a credential it already received.
- Define rotation, revocation and the effect of compromise before the credential is issued.
- When recipients, purposes or stored access change, reassess the applicable disclosure, authorization and consent basis. An ordinary technical edit may need no new consent; an expanded purpose may.

Third-party SDKs and platform features bring their own data handling and defaults. Check the version, configuration and terms actually in use instead of assuming the provider's general description applies.

## Look for exposure in secondary paths

Sensitive data often leaves through a path the feature description did not mention:

- application and access logs, traces, error trackers and analytics;
- caches, search indexes and derived stores;
- exports, reports, support tools and admin consoles;
- CI artifacts, build logs and test fixtures;
- model context, prompts, tool results and agent memory;
- non-production environments populated from production data.

Check redaction at capture and access at query time. Keep telemetry access aligned with the privacy decision, using [observability and monitoring](../../design-system/references/observability-and-monitoring.md) for collection mechanics.

## Evidence questions

- Which boundary is new or moved, and what validates each crossing?
- Which actor can perform each action, on which exact resource, under which lifecycle condition?
- Which data classes are newly collected, exposed, logged, exported or sent to a provider?
- Does the accepted purpose and retention cover the new use, and can deletion reach every copy?
- Which credential is introduced, who can use it, and how is it rotated or revoked?
- What happens when the check cannot be evaluated, the provider is unavailable or the request is repeated?
- Which exposure path remains unchecked, and who owns that decision?
