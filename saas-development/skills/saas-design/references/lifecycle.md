# Tenant and commercial lifecycle decisions

Read when a change affects customer lifecycle, payment state or persisted tenant work. Use only the transitions relevant to the requested product.

| Transition | Establish | Evidence that matters |
| --- | --- | --- |
| Create/join organization | Creator authority, recipient proof, duplicate joins, initial roles and resource ownership | Concurrent creation/invitation, rejected recipients and persisted membership |
| Transfer/remove membership | Grant limits, last-owner policy, active sessions/jobs and resource ownership | Old and new identities after the change, including stale cache/token windows |
| Trial/upgrade/downgrade | Effective time, entitlements, existing data/work, quotas and customer-visible consequences | Before/after capability decisions and in-flight operations |
| Receive provider event | Authentic source, event/business identity, environment mapping and durable progress | Duplicate, delayed, conflicting and interrupted handling; reconciliation to provider state |
| Record usage | Definition/unit, tenant/billing attribution, late/corrected events and idempotency | Reconciliation from authoritative events to aggregated allowance/invoice inputs |
| Suspend/cancel/reactivate | Access versus processing versus billing, grace/retention and reinstatement rules | Existing sessions, jobs, scheduled operations and restored entitlements |
| Export/delete tenant | Requesting authority, retention exceptions, derived stores/providers and backups | Accessible export, scoped deletion and prevention of unintended data reactivation on restore |

## Specify what a transition changes

Treat a transition as a change in the product's promises and permissions. Establish which entity is changing, who can request the change, when it takes effect, and what happens to existing data and work. Decide whether access, processing and billing change together or at different times. Those are product rules to recover from the accepted requirements, not defaults supplied by a payment integration.

Follow the transition through cached decisions, active sessions and queued work. Decide when each needs to observe the new state and what the application may permit while it is stale. Keep the source of each fact explicit so customer administration, service enforcement and provider reconciliation do not compete to overwrite one another.

## Decide when processing is complete

If every required effect is local to one datastore, the business update and its processed-event record can commit together. A failed transaction then leaves neither half committed. If an effect crosses into another system, that transaction cannot establish that the remote work completed. Persist the intended work and enough progress to resume or reconcile it, and give consequential remote operations a stable identity supported by the integration.

On retry, determine whether work is absent, incomplete, complete or uncertain before repeating an effect. A record that an event was received answers a different question from evidence that its business effects finished. An outbox can connect a local state change to durable delivery intent; dispatch still needs duplicate handling and a way to account for exhausted work.

Use atomic local updates, durable intent or reconciliation according to those failure boundaries. A universal workflow engine is unnecessary. Verify provider API versions, identity rules and retries/order guarantees against the selected integration.

For model ownership and lifecycle evidence, inspect the pinned references in the [package source review](../../../references/sources.md). Starter examples illustrate concerns, not complete production contracts.
