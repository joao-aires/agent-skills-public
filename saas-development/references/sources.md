# SaaS project sources and interpretation

These original skills use public starter/project patterns as research examples. No application code, UI, upstream skill or framework defaults are redistributed. Both starter repositories declare MIT at the reviewed revisions. Selected file inspection does not establish that either starter meets a particular product's security, accessibility or operating requirements.

| Project at reviewed revision | Inspected paths | Information used |
| --- | --- | --- |
| [Next.js SaaS starter](https://github.com/nextjs/saas-starter/tree/6e33e58b1e553a41fe22e6b941a7229a002de361) | lib/db/schema.ts; app/(login)/actions.ts; app/(dashboard)/dashboard/page.tsx; app/api/stripe/webhook/route.ts | Distinct users, teams, memberships, invitations, activity and subscriptions; customer administration and signed-provider-event boundaries. Starter simplifications are not adopted as complete lifecycle or authority rules. |
| [Wasp Open SaaS](https://github.com/wasp-lang/open-saas/tree/5859df70e93ddd04d183323934e9c9e2ae1c81c5) | template/app/src/payment/processedWebhookEvent.ts; payment/stripe/webhook.ts; admin/dashboards/analytics/AnalyticsDashboardPage.tsx; admin/dashboards/users/UsersTable.tsx | Duplicate delivery, subscription mapping, metrics, table filtering and loading/error surfaces. Recording an event does not by itself establish crash-safe completion of business effects; durable progress/reconciliation need their own design. |

## Primary references for implementation and verification

- For a selected billing integration: [Stripe webhook behavior](https://docs.stripe.com/webhooks), [idempotent requests](https://docs.stripe.com/api/idempotent_requests) and [subscription events](https://docs.stripe.com/billing/subscriptions/webhooks). These illustrate contracts to verify with the actual provider; Stripe is not required.
- For authority: [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) and the selected identity/provider documentation. Domain membership and commercial entitlement remain application decisions.
- For accessible dashboard implementation: [WCAG](https://www.w3.org/TR/WCAG22/) and [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/). Automated checks, visual inspection and task/usability evidence establish different properties.

Consult the actual version, deployment and feature/edition terms before implementation. The source references in skill metadata identify research context; they do not install a framework, configure a provider or grant publication authority.
