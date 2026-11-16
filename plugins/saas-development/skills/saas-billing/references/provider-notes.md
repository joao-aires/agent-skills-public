# Billing provider notes

**Reviewed:** 2026-11-16. **Basis:** public documentation only; no accounts, live prices,
fees, plan entitlements or country availability were verified. Prices and fees change and
are not recorded here as durable facts. Confirm the account's current terms, tax settings
and supported payment methods before promising behavior.

## Stripe for web billing

Public docs cover subscriptions, prices, invoices, payment intents and charges, refunds and
disputes, webhooks, idempotent requests, API versioning, test clocks, usage-based meter
events, tax and the customer portal.

| Integration area | What to establish |
| --- | --- |
| Object mapping | Which provider customer, price, subscription and invoice correspond to which local organization, plan and period. |
| API version | Pin the account's API version and record the version used by each integration; behavior and object shapes are versioned. |
| Checkout | Which flow is used, what is collected, how the return URL behaves and what the application may show before the webhook confirms state. |
| Webhooks | Signing secret, raw-body verification, event selection, retry behavior and the handler's own retry/reconciliation. |
| Idempotency | Which operations use a provider idempotency key and which rely on local idempotency; key lifetime and reuse rules. |
| Test mode | How test clocks or test data model trials, renewals and failures; separation from live objects and secrets. |
| Usage metering | The meter definition, event identity, aggregation window and how meter results map to invoices and entitlements. |
| Tax and SCA | Account tax configuration, invoice display, exemption handling and strong customer authentication in the actual payment flow. |
| Customer portal | Which changes customers may make, what the application learns and when, and which changes require its own approval. |

Provider cautions:

- Webhooks can be delivered more than once and not in business order. Verify and reconcile
  rather than assuming a sequence.
- A completed checkout redirect is not proof of a settled payment or of local entitlement.
- Test-mode behavior is not evidence that the live account, tax configuration or payment
  methods work.
- Fees, payout timing and method availability vary by account, country and transaction;
  they are commercial facts to check, not method assumptions.

Stripe is the selected web provider for this collection's method. The design principles
remain provider-neutral; do not treat a Stripe object model as the product's domain model.

## Superwall for mobile paywalls

Use only after asking whether the product uses Superwall. If the answer is no or no answer
is available, do not add it. Store billing, subscription rules and entitlement decisions
still apply when it is used.

Public docs describe paywalls, placements, campaigns, A/B tests, audience filters,
webhooks, SDKs for several mobile frameworks, and web checkout via Stripe.

| Integration area | What to establish |
| --- | --- |
| Placement taxonomy | Which product moments map to placements, and which paywall or campaign each may show. |
| Campaign and holdout | How experiments are assigned, how exposure is recorded and how a holdout is kept comparable. |
| Purchase and restore | How store purchases, restoration and cross-device entitlement are handled; what the app shows if restoration fails. |
| Webhooks | Authenticity, event types, retry behavior and mapping to the local subscription/entitlement state. |
| Store rules | Which subscription products, offers and paywall content the stores permit, and how review requirements affect iteration. |
| Web checkout | Whether it is available for the account, how it relates to store entitlements and which provider owns the payment. |
| Analytics boundary | Which paywall metrics are product analytics and which are billing truth. |

Provider cautions:

- The product is mobile-first; some documentation and features are marked beta or vary by
  plan and platform.
- Paywall experiments do not change store billing rules or grant entitlement by themselves.
- Plan entitlements, web-checkout eligibility and platform support must be verified for the
  actual account.

## Using provider notes

Record the documentation page and retrieval date for any behavior a decision depends on.
Keep provider accounts, live prices, tax settings and refund authority outside design work
unless the request explicitly authorizes them.
