---
name: saas-billing
description: Design or assess SaaS commercial state, entitlements and billing-provider
  integration. Use for plans, prices, trials, upgrades, dunning, cancellation, refunds,
  tax and the event, reconciliation and entitlement contracts behind paid access.
  Independently of a particular provider except where the platform selects one.
license: MIT
metadata:
  kind: method
  domain: saas
  phase: design
  scope: generic
  invocation: both
  references: ../../references/sources.md
user-invocable: true
---

# Make paid access a contract, not a redirect

Billing answers a commercial question and an access question at the same time: what the
customer bought, what the product currently permits, and how those two facts stay aligned
when a payment fails, an event repeats or a plan changes. Treat the payment provider as
one source of facts, not as the product's entitlement model.

This method owns plans, prices, entitlements, commercial transitions and provider-event
handling. `saas-design` owns customer lifecycle and tenancy; `saas-identity-and-access`
owns who may administer the account; `saas-supporting-services` owns non-billing supporting
capabilities. Reuse their accepted decisions rather than duplicating them here.

## Reading path

| Need | Read |
| --- | --- |
| Entitlement model, precedence, trials, transitions and enforcement evidence | [Entitlements](references/entitlements.md) |
| Webhook authenticity, idempotency, ordering, replay, retries and reconciliation | [Provider events](references/provider-events.md) |
| Dated Stripe and Superwall observations and verification questions | [Provider notes](references/provider-notes.md) |
| Customer lifecycle and tenant closure | `saas-design` |
| Organization roles and administrative authority | `saas-identity-and-access` |

Read only the reference that matches the open decision. Provider notes do not override the
commercial model and do not record durable prices.

## Establish the commercial promise

Define what is sold before defining how it is charged:

- the plans and the capability, limit or service level each one promises;
- who buys (person, organization, workspace) and which entity owns the invoice;
- the billing interval, currency, tax treatment and supported payment methods;
- what a trial includes, how it ends and what the customer sees at the boundary;
- how seats, usage or credits are counted and when they become billable;
- what happens to existing data and work on downgrade, cancellation or non-payment.

Keep the product's plan and entitlement vocabulary separate from provider objects such as
prices, products or subscription items. Map them explicitly. A provider price ID can change
without changing the product promise; a product promise can change without creating a new
provider price.

Ask about unresolved commercial commitments rather than inventing a grace period, a refund
policy or a tax stance. Those are product, finance and legal decisions with customer-visible
consequences.

## Select the provider by platform

For a web purchase flow, use Stripe as the selected billing provider where it is available
for the account, entity and jurisdiction. If it is not, record the constraint and the
unresolved provider decision rather than silently substituting another service. Verify the
account's country, tax configuration, payment methods and API version before promising
behavior; availability and fees vary by account and jurisdiction.

For a mobile purchase flow, ask whether Superwall is used. If the answer is no or no answer
is available, do not add Superwall. Use the store's billing and entitlement evidence and the
existing paywall approach. If Superwall is used, treat it as a paywall, placement and
experiment layer over store billing; store review, subscription rules and entitlement
decisions still apply.

Do not add a second billing provider because it appears in a reference project. Do not
replace an accepted provider without an explicit migration decision and an exit path.

## Keep three states distinct

| State | Owns | Does not establish |
| --- | --- | --- |
| Provider state | Checkout completion, subscription status, invoice/payment status, refund or dispute facts. | That the local account has the promised capability, or that usage was recorded correctly. |
| Local entitlement state | The product's decision about which capability, limit or service level applies to a subject at a time, including grants and overrides. | The customer actually paid, or that usage stayed within the limit. |
| Observed usage | What the product actually consumed or delivered, attributed to a tenant and meter. | Permission to exceed a purchased limit, or a substitute for provider payment state. |

Define precedence for each fact and a reconciliation path when the three disagree. A
successful checkout redirect is a navigation event, not authoritative proof of paid access.
A webhook receipt proves arrival, not completion of the local effect.

## Model the lifecycle transitions

| Transition | Establish | Evidence that matters |
| --- | --- | --- |
| Trial start/end | Entitlement during trial, reminder timing, required payment method, conversion and expiry. | Access before, at and after expiry; no accidental charge or silent lockout. |
| Upgrade | Proration or immediate charge, effective time, new limits and in-flight work. | Before/after capability decisions; invoice and entitlement agree. |
| Downgrade | Effective time, data/usage over the new limit, seat reduction and customer communication. | Existing records remain readable; excess work has a defined outcome. |
| Failed payment/dunning | Retry schedule, grace access, suspension and deletion rules. | Customer notice, access during grace, recovery and final state. |
| Cancellation/reactivation | Access until period end, data retention, reactivation and re-subscription. | Existing sessions/jobs observe the change; restoration is not a new tenant. |
| Refund/chargeback | Who decides, access consequence, evidence and fraud handling. | Provider state, local entitlement and customer communication stay consistent. |
| Tax and SCA | Tax calculation, invoice display, strong customer authentication and exemption handling. | Checkout completion and invoice correctness under the actual account configuration. |

Read [entitlements](references/entitlements.md) for the state model and transition
questions. Use the accepted lifecycle decisions in `saas-design` for suspend, cancel and
tenant closure; do not create a parallel policy here.

## Process provider events as a contract

Verify the signature against the raw request, map the event to the intended account and
environment, and reject events that do not belong. Record the provider event ID and a
durable processing state before applying business effects. Use an idempotency key or an
idempotent local effect for consequential operations.

Provider events can arrive more than once, late, or after a newer state change. Resolve
ordering against current provider state rather than arrival order. Give failures a bounded
retry and a visible dead-letter path, and reconcile subscriptions, invoices and entitlements
on a schedule.

Read [provider events](references/provider-events.md) for the ingress, ordering,
reconciliation and evidence details.

## Verify and report

Exercise the behaviors the promise depends on:

- a completed checkout and the access it actually grants;
- a duplicate event and an out-of-order event;
- an invalid signature and an unmapped account;
- an interrupted handler and a retried effect;
- a failed payment, grace period and recovery;
- an upgrade, downgrade, cancellation and reactivation;
- a refund or chargeback and its access consequence;
- a reconciliation that repairs drift between provider and local state.

Separate configured behavior from observed behavior. A test-mode checkout, a dashboard
setting or a passing unit test establishes only its own boundary.

Return the plan/entitlement model, provider mapping, event contract, reconciliation
approach, evidence and remaining gaps. Creating a provider account, setting live prices,
issuing refunds or changing tax configuration requires separate authorization.
