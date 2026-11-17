# Integration contract for a supporting service

Use for each selected provider or self-hosted service that the product's behavior depends
on. The contract makes the boundary reviewable before implementation and testable after it.
Not every row applies to every capability; state which are intentionally absent.

| Concern | Contract decision | Evidence to keep |
| --- | --- | --- |
| Purpose and owner | Which product outcome the integration serves, who owns it and who responds when it fails. | Named owner, dependency entry, runbook or escalation path. |
| Identity and credentials | Which principal calls the provider, with what scope, for which tenant and environment; how secrets are stored and rotated. | Credential inventory, scope policy, rotation record, separate test/live credentials. |
| Endpoint and environment mapping | How the provider's account, project, workspace or region maps to this product's environment and tenant. | Mapping table or configuration; a test that rejects an unmapped event. |
| Data mapping | Canonical identifiers, timestamps, units, enums and tenant fields; which values are derived and which are authoritative locally. | Versioned mapping/schema, sample payloads, contract tests. |
| Webhook authenticity | Which signature or shared secret is verified, over which raw body, with what timestamp tolerance and rotation procedure. | Verification code or configuration; rejected-signature test. |
| Event identity and idempotency | Stable provider event ID plus a local business key; scope of deduplication; what happens when the same business fact arrives under a new event ID. | Unique constraint or inbox record, duplicate-delivery test. |
| Ordering and replay | Which field indicates order, which side wins a conflict, how late events are ignored or repaired, and how an operator replays safely. | Documented precedence, out-of-order test, replay procedure. |
| Durable progress | Which local record proves receipt, which proves completion, and how interrupted work is resumed. | Inbox/outbox state transitions; interrupted-handler test. |
| Failure, retry and dead letter | Timeouts, bounded retry and backoff, poison-message quarantine, alerting, ownership and manual disposition. | Retry configuration, exhausted-work alert, operator procedure. |
| Reconciliation | Which provider facts are authoritative, how often they are compared with local state, and how drift is repaired. | Reconciliation job or checklist, drift report, repair record. |
| Tenancy isolation | How tenant context is carried, whether the provider supports separation, and how cross-tenant access is prevented. | Tenant-scoped credentials or metadata; cross-tenant denial test. |
| Cost attribution | Which unit is metered, where it is recorded, how it maps to tenant/plan and how provider invoices are checked. | Meter definition, allocation dimensions, invoice reconciliation. |
| Offboarding and deletion | How credentials are revoked, data exported, provider-side data deleted and deletion confirmed within the promised period. | Export sample, revocation test, deletion confirmation or procedure. |
| Rate and quota behavior | Which limits apply, what the product does when they are reached, and who can raise them. | Limit configuration, throttling behavior, capacity review. |
| Version and change management | Which API/SDK version is pinned, how deprecations are detected and who reviews provider changes. | Version pin, changelog review owner, upgrade test. |

## Identity and environment

Use a distinct credential per environment and, where the provider supports it, per tenant
or workspace. A shared secret across production and test turns a test action into a
production incident. Prefer a provider-supported workload identity or short-lived token
over a long-lived key when the operational cost is reasonable.

Record what the credential can reach, not only where it is stored. A credential that can
read every tenant is a cross-tenant exposure even if the current code filters correctly.
Rotate on a schedule and on personnel or provider changes; keep an overlap window that
allows both sides to be updated without an outage.

## Data mapping and tenancy

Map the product's canonical IDs to provider IDs explicitly. Do not use an email address or
a display name as the join key when the person or organization can change it. Keep the
tenant on every record, cache entry, queue message and export; a provider object without a
tenant field needs a local mapping table and a test that rejects unmapped input.

Decide which side owns each field. A provider may own delivery status while the product
owns the notification's purpose and recipient. A search index may own relevance while the
database owns the record. When both sides can change a field, define precedence before the
first conflict.

## Events, idempotency and ordering

Verify the provider's signature against the raw request body before parsing or acting.
Reject stale timestamps and unknown accounts. Store the provider event ID with the receipt
time and the handled outcome; a unique constraint on the provider event ID prevents
duplicate processing but does not prove the business effect finished.

For work that crosses the provider boundary, persist the intended effect and enough state
to resume it. If the provider supports an idempotency key, use a stable key derived from
the business operation rather than from the HTTP attempt. If it does not, make the local
effect idempotent or reconcile before retrying.

Do not assume delivery order from arrival order. Use the provider's event time, object
version or a fetch of current state to decide precedence. A late event that would regress a
newer state should be ignored or routed to reconciliation, not applied blindly.

## Failure, retry and dead letter

Set a timeout for every call and a retry budget for every operation. Retry only when the
operation is safe to repeat and the failure is plausibly transient. Back off with jitter and
cap total attempts; unbounded retries turn a provider incident into a local outage.

Park exhausted work in a durable dead-letter record with enough context to diagnose it. Name
the owner, the alert and the procedure for replay or manual resolution. A dead-letter queue
without an alarm is a silent data-loss path.

Define the user-visible behavior while the provider is unavailable. Queueing and later
delivery, a degraded in-product notice and a hard failure are different promises; choose
one and verify it.

## Reconciliation and cost

Reconcile consequential provider facts against local state on a schedule and on demand.
Choose the authoritative source per fact: the provider usually owns payment or delivery
status, while the product owns entitlement and business meaning. Record drift, repair it
through a bounded path and keep an operator-visible exception.

Meter usage where it is created, with tenant and plan dimensions. Reconcile provider
invoices against local meters when cost affects pricing, quotas or unit economics. A bill
that cannot be attributed to a tenant is an unresolved product decision, not only a finance
problem.

## Offboarding and deletion

Before the first customer depends on the integration, establish:

- how the tenant's data is exported in a usable format and within what period;
- how credentials and provider-side access are revoked;
- which provider records are deleted, retained or anonymized, and how deletion is confirmed;
- how backups and derived stores are handled;
- what remains in logs, analytics or support transcripts.

Deletion claims that cover only the application database are incomplete. Test the
representative path, including a restored environment, and record the result.
