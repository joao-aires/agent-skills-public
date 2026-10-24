# Dashboard decisions

Use this reference for a substantive dashboard design or critique. Apply the concerns that change the user's task; do not turn them into a compulsory page inventory.

| Question | Design consequence |
| --- | --- |
| What must this person decide or complete? | Put the relevant evidence, exceptions and action together; overview cards are optional. |
| Which organization, environment and period are active? | Preserve visible context through navigation, forms, filters and exports. Test tenant switching with cached/in-flight data. |
| Can the value be compared honestly? | State unit, denominator, interval/time zone, freshness and incomplete data. Avoid suggesting improvement from a changed population. |
| Is the user exploring or operating? | Exploration may need comparisons/drill-down; operations may need queues, status, assignment and recovery. |
| How large and uneven is the data? | Compare table density, filtering, pagination, summary and detail using representative long names, missing values, skew and large counts. |
| What does selection mean? | Distinguish visible rows, current page and all matching records; show the effect of filters and permission changes. |
| Who can act and why might an action be unavailable? | Explain permitted paths without leaking restricted resources. UI state reflects server policy; it does not implement it. |
| What happens after submission? | Show validation, pending/partial completion, cancellation or recovery as the actual contract permits. |

## Choose the data interaction

Decide whether the task is to notice an exception, compare a pattern, find a record or perform an operation. Put the evidence and action needed for that task within a coherent reading path. Summaries should lead to an explanation or useful detail when the user needs to investigate; a detail view should preserve enough list context to let the user return to work.

For tables, establish which work happens on the server and what the current result set represents. Make filter, sort and pagination state consistent with exports and bulk actions. A selection can mean the visible rows, a saved set of record identities or all records matching a query; those meanings differ when data or permissions change. Show the supported scope before the user commits the action, and have the server enforce it again.

For metrics, define the population and interval before choosing a visual treatment. A comparison is useful only when the values describe comparable populations and units. Make missing, stale and partially collected data recognizable so an absent value is not mistaken for zero or an improvement.

## Choose an artifact that answers the design question

Produce the most useful artifact for the requested work: a wireframe, interaction/state sketch, implementation or critique. Use available authorized design tooling; an SVG or HTML artifact can establish layout intent when no design service is available. Validate with representative tasks and observed users when a usability study is requested; do not invent research findings.

The [Next.js starter dashboard](https://github.com/nextjs/saas-starter/blob/6e33e58b1e553a41fe22e6b941a7229a002de361/app/%28dashboard%29/dashboard/page.tsx) exposes membership and subscription tasks. [Open SaaS analytics](https://github.com/wasp-lang/open-saas/blob/5859df70e93ddd04d183323934e9c9e2ae1c81c5/template/app/src/admin/dashboards/analytics/AnalyticsDashboardPage.tsx) and its [user table](https://github.com/wasp-lang/open-saas/blob/5859df70e93ddd04d183323934e9c9e2ae1c81c5/template/app/src/admin/dashboards/users/UsersTable.tsx) illustrate metrics, filters and loading/error concerns. These examples supply questions to evaluate; they do not establish accepted visual direction, complete accessibility, authorization or production readiness.
