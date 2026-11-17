# Provider events, signatures and reconciliation

Use when a payment provider can change commercial state asynchronously. The goal is to
make receipt, processing and completion distinguishable, and to recover when any of them
fails.

## Event ingress

| Check | Decision |
| --- | --- |
| Authenticity | Which signing secret is used, over which raw body, with what tolerance for the timestamp, and how the secret is rotated. |
| Environment | How test/live mode and the provider account map to this deployment; reject events for an unmapped account. |
| Event identity | The provider event ID, event type, API version and object ID used for deduplication and diagnosis. |
| Tenant and subject | How the provider customer/object resolves to a local organization, workspace or user. |
| Freshness | Whether the event is old enough to be ignored or routed to reconciliation rather than applied. |
| Payload retention | What is stored, for how long, and how sensitive payment data is excluded. |

Verify before acting. A handler that parses first and verifies later has already processed
attacker-controlled input.

## Receipt is not completion

Persist the event in a local inbox with a unique provider event ID, the received time, the
relevant object/account and a processing state. Then apply the business effect and record
the outcome. A unique constraint prevents duplicate receipt; it does not prove that the
effect completed.

Use explicit states such as received, processing, applied, ignored and failed. A handler
that crashes between the state change and the effect must leave enough evidence for a retry
or a reconciliation to determine what happened.

For work that also calls the provider or another service, give the operation a stable
idempotency key derived from the business intent. If the provider does not support one,
make the local effect idempotent or check current state before repeating it.

## Ordering and replay

Provider events are not guaranteed to arrive in the order the business facts occurred.
Use the provider's event time, object version or a fetch of current state to decide
precedence. Do not regress a newer local state because an older event arrived late.

When an event is ambiguous or conflicts with local state, reconcile against the provider's
current object rather than choosing between payloads. Replaying an event is a deliberate
operator action with a recorded reason; it must not repeat consequential effects such as an
email, credit or invoice adjustment.

An event type that the application does not handle should still be recorded as ignored with
the reason, so a later investigation can distinguish "not relevant" from "lost".

## Retry, dead letter and alerting

- Bound retries and use backoff with jitter.
- Retry only transient failures; a validation or mapping error needs correction, not more
  attempts.
- Park exhausted events in a durable dead-letter record with payload reference, error and
  attempt history.
- Alert the owner and provide a replay or manual-resolution procedure.
- Prevent one poison event from blocking unrelated events for the same account where the
  ordering requirement allows it.

A provider may also retry its own delivery. The local handler must tolerate both provider
retries and internal retries without duplicating effects.

## Reconciliation

Reconcile on a schedule and on demand:

| Fact | Provider authority | Local mirror |
| --- | --- | --- |
| Subscription and quantity | Current subscription and items | Entitlement snapshot and effective window |
| Invoice and payment | Invoice/payment status | Customer-visible billing state and access decision |
| Refund or dispute | Refund/dispute record | Access consequence and support note |
| Customer mapping | Provider customer ID | Local organization/workspace mapping |

Record drift, the source used to resolve it and the repair action. Reconciliation should
be able to detect a missing event, a duplicated effect, a stale entitlement and an
unmapped customer. It should not silently overwrite local grants or identity authority.

## Security and isolation

- Keep provider secrets in the deployment's secret store; separate test and live.
- Restrict who can replay events, issue refunds or change prices.
- Do not log full payloads containing payment details; retain only what diagnosis needs.
- Verify that an event for one tenant cannot change another tenant's entitlement.
- Rate-limit and monitor the webhook endpoint; an unauthenticated flood is still an
  availability event.

## Evidence

| Behavior | Evidence |
| --- | --- |
| Valid event applied | Inbox state, entitlement decision and customer-visible result. |
| Invalid signature rejected | Rejected request and no state change. |
| Duplicate delivery | One business effect, second delivery recorded as duplicate. |
| Out-of-order delivery | Newer state preserved; older event ignored or reconciled. |
| Interrupted handler | State shows incomplete work; retry completes it once. |
| Exhausted retries | Dead-letter entry, alert and documented resolution. |
| Reconciliation | Drift detected and repaired against provider state. |
| Cross-tenant event | Rejected or mapped only to the authorized tenant. |

A configured webhook endpoint, a successful test event and a green dashboard are different
levels of evidence. Report which behaviors were actually exercised.
