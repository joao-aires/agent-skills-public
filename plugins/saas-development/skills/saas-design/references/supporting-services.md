# Supporting service design

Use the smallest set of services that can support the intended customer journey. Treat named providers as candidates and verify their current capabilities against official documentation when making a selection.

| Journey | Design decision | Candidate examples |
| --- | --- | --- |
| Signup and first use | Establish membership before granting tenant access. Separate essential email from campaigns. Track meaningful activation with tenant-scoped, minimized data. | Resend, PostHog |
| Daily use and support | Correlate incidents to authorized tenant context without copying sensitive content. Give operators actionable alerts and scoped support access. | Sentry, Datadog |
| Hosting and storage | Assign compute, identity and data ownership. Compare isolation, regional commitments, deployment, restore and cost for each component. | Cloudflare Pages, Hetzner, Supabase |
| Purchase and renewal | Identify payment authority and local entitlement authority. Map customers and subscriptions to tenants. Reconcile missed, repeated and delayed events. | Stripe, Superwall where its purchase channels fit |
| Marketing and retention | Establish who can authorize campaigns and publish content. Apply consent and suppression before dispatch. | Zernio for social publishing where applicable |
| Cancellation and closure | Define end-of-access and export windows, stop communications as applicable, and complete retention or deletion across the services that hold customer data. | Existing systems of record |

At each boundary record the owner, identifiers, data sent, permissions, visibility across tenants, failure policy and what the customer sees. Define who handles retries or manual repair. Record the effect of external outages on core product availability. Compare providers by these requirements, exportability, operational load and cost per active customer or tier.

Exercise a second tenant alongside the happy path. Simulate delayed billing, unavailable email or telemetry, and interrupted closure. Check that tenant isolation holds, essential access follows the product contract and an operator can find incomplete work.
