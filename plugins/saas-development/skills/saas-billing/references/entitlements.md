# Entitlement and commercial-state model

Use when defining what a plan promises, how paid access is decided, or how a transition
changes behavior. The entitlement is a product decision; the payment provider supplies
commercial facts that inform it.

## Define the vocabulary

| Term | Meaning to settle |
| --- | --- |
| Plan | A named commercial package with a customer-visible promise. |
| Price | A provider-side billing arrangement for a plan, interval, currency and quantity. |
| Feature | A capability the product can allow or deny. |
| Limit or quota | A numeric bound on usage, seats, storage or rate. |
| Entitlement | The product's decision that a subject may use a capability or consume up to a limit now. |
| Meter | The local definition and unit of observed usage. |
| Trial | Time-bounded access without a completed purchase, with explicit expiry behavior. |
| Grace | Temporary access after a payment failure or before suspension, with an end condition. |
| Override | A scoped, attributable, time-bounded exception to the normal entitlement. |

Keep plan names, provider product names and entitlement keys distinct. Renaming a plan
should not require a data migration; changing a provider price should not silently change
the product promise.

## Model an entitlement decision

Record enough to answer "why did this subject have this capability at this time":

| Field | Purpose |
| --- | --- |
| Subject | Organization, workspace, user or service account the decision applies to. |
| Capability or limit | Stable product key, not a display label. |
| Value | Boolean, numeric limit, tier or feature set. |
| Source | Provider subscription, local grant, contract override or trial. |
| Effective window | When the decision starts and ends. |
| Version or computed time | Which state was used, so stale decisions are recognizable. |
| Reason and actor | Why an override exists and who authorized it. |

An entitlement can be computed from several sources. Store the inputs and the resulting
decision, or a versioned snapshot, so support can explain a denial without reconstructing
history from provider events.

## Establish precedence

Decide which source wins for each fact, and write it down:

| Fact | Usual authority | Notes |
| --- | --- | --- |
| Purchased plan and quantity | Provider subscription | The provider is authoritative for what was bought and paid. |
| Payment, refund and dispute status | Provider | Local state mirrors it and must not invent a successful payment. |
| Local grant, contract term or support override | Product | Time-bounded, attributed and auditable; does not overwrite provider payment facts. |
| Role and administrative authority | `saas-identity-and-access` | Paying does not grant organization ownership or administrative rights. |
| Observed consumption | Product meter | Informs limits and invoices; does not grant access by itself. |

Do not let observed usage quietly become permission. If a customer exceeds a limit, the
product's chosen behavior is a product decision: block, degrade, bill overage or notify.
Each option needs a visible outcome and a recovery path.

## Trials, upgrades and downgrades

For a trial, establish who is eligible, what is included, whether a payment method is
required, when reminders are sent, what happens at expiry and whether data is retained.
Provider trial periods and local trial grants can diverge; choose one authority and
reconcile the other.

For an upgrade, decide whether the new entitlement applies immediately or at the next
period, how proration is handled and what happens to work already in flight. For a
downgrade, decide when the lower limit applies, how existing data above the limit remains
readable, which seats or resources are removed and how the customer is warned.

Proration is a provider billing behavior; entitlement timing is a product behavior. They
can differ, but the customer-visible result must be explainable.

## Dunning, cancellation and refunds

Dunning is a sequence of payment retries and customer notices. Define the grace window,
what remains available during it, when the account is suspended and what is deleted or
retained. Do not equate a failed payment with immediate data deletion.

Cancellation ends the commercial commitment; it does not necessarily end access at once.
Establish access until period end, renewal behavior, reactivation and the retention period.
A refund or chargeback may reverse payment without reversing every service already
delivered; decide the access consequence and record who authorized it.

## Overrides and operator actions

Support or finance may need to grant a credit, extend a trial or restore access. Treat
these as domain operations:

- scope to a subject and capability;
- set an expiry or review date;
- record the actor and reason;
- make the override visible in the customer's billing or admin surface where appropriate;
- prevent an override from masking a broken provider integration indefinitely.

An override without expiry becomes a permanent shadow plan.

## Enforcement and staleness

Enforce entitlement in trusted server-side code at the action or resource boundary. Pass
the verified subject and tenant into the decision; never trust a client-supplied plan or
role. Apply the same semantics to API calls, jobs, exports, bulk operations and AI/tool
actions.

Cached entitlement decisions need a bounded staleness window. Define how a plan change
reaches active sessions, long-running jobs and cached feature flags. If immediate
revocation is promised, the cache and session design must support it.

## Evidence

Exercise representative allow/deny decisions at each boundary and record what was
observed:

- trial before, at and after expiry;
- upgrade and downgrade with in-flight work;
- failed payment through grace to suspension and recovery;
- cancellation, reactivation and tenant closure;
- over-limit behavior for seats, storage and metered usage;
- a stale cache or session after a plan change;
- an override with and without expiry.

A dashboard showing the right plan is not evidence that enforcement uses it. A passing
component test is not evidence that the customer journey behaves correctly.
