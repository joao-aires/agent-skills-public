---
name: saas-dashboard-design
description: Design or improve SaaS customer and operator dashboards around decisions,
  tenant context and actionable workflows. Use for dashboard information architecture,
  metrics, tables, administration and realistic interface states across frontend stacks.
license: MIT
metadata:
  scope: generic
  invocation: both
  role: support
  references: ../../references/sources.md
user-invocable: true
---

# Design dashboards for decisions and work

Identify the audience, their recurring tasks, the decisions this surface should support and the cost of acting on the wrong context. Separate customer workspaces, customer administration and internal operator tools. Reuse sufficient product evidence and accepted visual direction; a dashboard request does not automatically reopen branding or select a UI library. Read [dashboard decisions](references/dashboard-decisions.md) for data/interaction tradeoffs and the [source review](../../references/sources.md) for inspected open-source examples.

## Establish context and hierarchy

Begin with the work this audience returns to do. Determine what needs attention, what information explains the situation, and which action follows. Use that relationship to choose the starting view and navigation. An overview is useful when it helps prioritize work; a task list or detailed workspace may be the better starting point when users already know what they need to do.

Make organization/workspace, time range, environment and relevant resource scope recognizable before consequential actions. Preserve that context through drill-downs and return navigation so a user can investigate a record without rebuilding their filters or losing their place.

Give each summary or metric a decision it supports. Establish what a change in the value would lead the user to do, then choose the surrounding explanation and route to detail. Compare layouts using realistic data distributions, including long names, large counts and uneven activity, rather than arranging identical cards around invented metrics.

Derive hierarchy, typography, density, color and interaction language from the product's purpose and accepted design system. Seek available interface craft, interaction, accessibility and writing expertise by capability. When absent, make and inspect a coherent direction with project evidence and appropriate references. Use the accepted stack's components/tokens; the skill does not require a framework, design tool or chart library.

## Make data and actions interpretable

Define units, denominators, aggregation, time zone, comparison period, freshness and missing-data meaning for consequential metrics.

- Distinguish zero, unavailable, stale and incomplete results.
- Choose a chart, table or direct value according to the question; permit accessible interpretation without relying only on color or hover.
- Connect summaries to the records or task that explains them where useful.

For operational tables, define search/filter/sort/pagination behavior and scope.

- Make selection across pages and bulk-action impact explicit.
- Support detail/recovery without losing useful list state.
- Availability and entitlements should produce understandable routes, while enforcement remains on the server.
- Avoid exposing restricted records in aggregates, counts, exports or hidden UI payloads.

## Cover the actual journey

Design first-use, loading, useful empty, filtered-empty, partial/stale, denied, failed, pending and completed states where the journey encounters them.

- Provide appropriate recovery and distinguish accepted work from completed effects.
- Destructive or privileged actions need understandable scope and consequences, not a confirmation dialog on every click.
- Customer billing/identity/support actions should use clear domain language and preserve tenant context.

## Verify the design at the requested boundary

Verify realistic content, keyboard/focus, accessible names, zoom, responsive layouts and the primary task under relevant success/failure states.

When implementing, inspect the rendered target; a component story or screenshot does not establish full functional behavior. Check server isolation and persisted outcomes separately.

Return the design rationale, affected states and actual evidence at the requested stopping point.
