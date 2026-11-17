---
name: saas-supporting-services
description: Select, integrate and assess the supporting services a hosted product
  depends on, including analytics, email, observability, hosting and edge, marketing
  and social automation, search, queues, notifications and support. Use for
  requirement-first build, buy, adopt or defer decisions and the integration contract,
  independently of particular vendors.
license: MIT
metadata:
  kind: method
  origin: local
  pack: technical
  domain: saas
  phase: design
  scope: generic
  invocation: both
  role: support
  references: ../../references/sources.md
user-invocable: true
---

# Choose supporting services from the product requirement

A hosted product needs capabilities that are not its differentiator: somewhere to send
transactional email, a way to see errors, a place to run the frontend, a queue for slow
work. Treat them as supporting services with explicit requirements and contracts rather
than as an architecture assembled from a vendor list.

This method owns the capability map, the acquisition decision and the integration
contract. Billing has its own method (`saas-billing`), and organization/identity authority
has `saas-identity-and-access`; neither is a supporting-service decision. `saas-design`
owns tenancy and lifecycle, and this method preserves its isolation and offboarding rules.

Start with the outcome, the users, the data and the failure the product can tolerate.
Then decide whether to build, buy, adopt an existing platform service or defer. A
vendor already present in the stack is a constraint to inspect, not a requirement to keep.

## Reading path

| Need | Read |
| --- | --- |
| Capability definitions, requirement questions and typical failure/exit concerns | [Capability map](references/capability-map.md) |
| Build, buy, self-host, adopt or defer options and selection criteria | [Selection criteria](references/selection-criteria.md) |
| Webhooks, identity, data mapping, retries, reconciliation and offboarding | [Integration contract](references/integration-contract.md) |
| Dated provider observations for analytics, email, errors, hosting, infrastructure and social publishing | [Vendor notes](references/vendor-notes.md) |
| Tenancy, identity, billing or lifecycle context | `saas-design`, `saas-identity-and-access`, `saas-billing` |
| Customer or operator surfaces for the capability | `saas-dashboard-design` |

Read only the reference that matches the open decision. Vendor notes answer "what should
I verify about this provider", not "which provider is correct".

## Establish the requirement

For each capability the product actually needs, establish the user or customer outcome,
the volume and latency, the data involved, the tenants and regions it touches, and what
must happen when it is unavailable. Distinguish a customer-facing promise from an internal
convenience; they justify different levels of investment and evidence.

- Name the capability, not the product feature that triggered it. "Send a password reset"
  needs delivery, bounce handling and suppression; "have email" does not.
- Decide whether the capability is differentiating, regulatory or commodity. Build only
  where the product has a durable reason; commodity infrastructure usually carries a
  higher operating cost than its visible price.
- Establish the acceptable degraded behavior before choosing a provider. Falling back to
  a second email provider, queueing telemetry or showing a static page are design choices
  with their own failure modes.
- Deferral is a valid outcome. Record what is not provided, what the user sees instead and
  when the decision should be revisited.

## Map the required capabilities

| Capability | Question it answers |
| --- | --- |
| Analytics | What did users and tenants do, and did the product change behavior? |
| Email | Can the product deliver transactional and, where intended, marketing messages? |
| Observability | Can operators see errors, traces, latency, saturation and business signals? |
| Hosting and edge | Where do the application, static assets, functions and routing run? |
| Marketing and social automation | How are external audiences reached and publishing scheduled? |
| Search | Can users find records across their own tenant scope with acceptable relevance? |
| Queues and background work | Can slow, retryable or scheduled work run outside the request path? |
| Notifications | How are in-product, push, SMS or chat events delivered and acknowledged? |
| Support | How do customers get help and how do staff act on their behalf? |

Billing and identity are not in this map. They carry the product's commercial and
authority contracts and remain separate methods. If an adjacent capability is requested,
name the owning method and stop rather than folding it into a vendor comparison.

## Choose an acquisition shape

| Shape | Appropriate when |
| --- | --- |
| Build in-house | The capability is differentiating, small and stable, and the team can own its failure and security. |
| Managed provider | Commodity capability, variable demand and a credible exit path justify handing over operations. |
| Open-source or self-hosted | Data control, customization or cost at scale outweighs patching, scaling and on-call burden. |
| Existing platform service | The selected platform already supplies enough of the capability and its limits are acceptable. |
| Defer | The requirement is not yet real, the current manual process is adequate, or the decision depends on unresolved product facts. |

Compare the candidates against the same eight criteria: fit, data/privacy/residency,
identity and integration, failure and reconciliation, cost, compliance, lock-in and exit,
and operational burden. Read [selection criteria](references/selection-criteria.md) for
the questions behind each. Record the comparison per capability; a decision that fits one
service does not carry to another. A feature matrix is not a decision; the criteria that the
product's commitments actually depend on should dominate.

Do not adopt a provider because it is familiar, because a starter uses it or because its
free tier is convenient. Do not reject a provider solely because a cheaper or more
familiar alternative exists. Record the constraint that decided the choice.

## Specify the integration as a contract

A provider is reached through a boundary that must be designed like any other. For each
selected capability, settle how identity is established, how data maps, what happens on
duplicate or late events, how failures are retried and parked, how cost is attributed and
how the relationship ends.

- Verify webhook authenticity against the raw request and map the event to the intended
  account, environment and tenant before acting on it.
- Give consequential work a stable identity and record durable progress. Receiving an
  event is not evidence that its business effect completed.
- Define ordering, replay and conflict resolution against the source that owns each fact.
- Bound retries, own a dead-letter path and make exhausted work visible to an operator.
- Keep tenant context through provider metadata, credentials, caches and exports; a
  provider that cannot express tenancy needs a local mapping and a leakage test.
- Attribute usage at the point it is created and reconcile provider invoices against
  local meters when cost becomes a product input.
- Define export, credential revocation and deletion before the first customer depends on
  the integration.

Read [integration contract](references/integration-contract.md) for the fields, decisions
and evidence that make this reviewable.

## Keep vendors as evidence, not method

Provider notes are dated observations about current documentation and integration
mechanics. They are not a recommendation, a durable price list or a substitute for the
account's plan terms. Prices, quotas, regional availability and feature gating change;
verify them at the point of commitment and record the date and source.

Use vendor documentation to ask better questions: what identity model, retention period,
export format, retry guarantee and deletion path does this service actually provide?
Marketing claims, status pages and public case studies support awareness, not a security,
residency or reliability conclusion.

## Verify and report

Exercise the integration at the scope of the promise: a successful send, a rejected
signature, a duplicate delivery, a provider timeout, a poisoned message, a tenant-scoped
export and a revoked credential. Distinguish configured behavior from observed behavior.

Return the capability decisions, selected shape, integration contract, evidence and
remaining gaps. Creating a provider account, accepting terms, sending live messages or
changing production configuration requires separate authorization.
