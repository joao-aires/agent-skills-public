---
name: operational-housekeeping
description: Plan and run recurring operational reviews of capacity, artifact retention,
  backup activity, dependency queues, expiring access, scheduled environments, and
  runbook ownership.
metadata:
  scope: generic
  invocation: both
  version: '2.0'
  role: task
---

# Operational housekeeping

Read [composition guidance](../../COMPOSITION.md) for optional expertise, fallback and scope.

Turn recurring maintenance into a finite, evidence-backed review with owners and follow-up work.

## Modes and general purpose

In interactive work, explain review findings and resolve local policy/ownership decisions. For setup build a risk-based review register and automate stable checks. During features/maintenance update capacity, retention, ownership and procedure requirements affected by the change. In recurring review runs consume the last reviewed revision/register, collect current evidence, update stable findings and prepare bounded remedies. Cleanup/resource mutations need a configured target/action policy; otherwise return candidates and patches rather than deleting anything.

The general value is preventing operational debt and reducing toil, not reproducing a project's calendar. Prefer event-driven checks after configuration/releases/ownership changes, backed by periodic review for drift. Retire checks with no decision value and measure whether automation reduced manual effort without weakening outcomes.

## Establish the review

Discover services/environments, owners, resource inventories, local schedules, quota/retention policy, active incidents, and prior exceptions. Start from the project's actual checklist rather than imposing a fixed weekly/monthly calendar.

For a new checklist, assign cadence based on failure consequence, rate of change, expiry lead time, and available automation. Explicitly label proposed cadence or thresholds until adopted.

Use [references/review-register.md](references/review-register.md) to record the review. Mark inaccessible or incomplete evidence as unknown, not healthy.

## Review relevant domains

| Domain | Check | Deep-work handoff |
| --- | --- | --- |
| Registries/artifact stores | Quota, growth, largest consumers, retention behavior, unexpected repos/tags | Scoped cleanup below |
| Databases/cache/storage | Free capacity, growth rate, utilization, quota/mount pressure, projected exhaustion | `plan-application-capacity`, `incident-response` |
| Backups | Job success, newest point, coverage, retention, restore-test age | `protect-and-restore-data` |
| Dependencies/security | Update queues, failed checks, overdue/unshipped findings | `vulnerability-management` |
| Credentials/access | Expiry lead time, accountable owners, duplicate records, stale grants | `credential-lifecycle`, local access policy |
| Observability | Collection health, repeated errors, noise and silent gaps | `observability-operations`, `reliability-design` |
| Scheduled environments | Sleep/wake behavior, timezone, consumers/jobs, backups, controller conflicts, alerts | `optimize-application-cost`; JVM specialist only for Java |
| Documentation/ownership | Runbook correctness, links, known problems, service/owner changes | Update local guidance or map gaps |

Do not expand a targeted review into every domain unnecessarily. For a comprehensive review, state coverage and skipped areas explicitly.

## Capacity and cleanup

Use trends and growth rate alongside current free space. Estimate time to exhaustion only with sufficient data and state its assumptions. Apply locally defined thresholds; fixed GB or percentage values from another project are not portable.

Before deleting artifacts, establish references from every relevant running/desired deployment, release/rollback inventory, retained builds, and retention obligations. A naming-pattern mismatch does not prove an artifact is unused. Prioritize large candidates, report expected savings, and use supported retention/dry-run tooling when available.

Preserve current and required rollback artifacts, backup recovery points, and unmerged source work. Verify actual storage/object counts and normal image pulls or jobs after cleanup. Cleanup and history rewriting are different operations.

## Scheduled cost optimization

Check which workloads opt in, which controller owns replicas/suspension, and which jobs keep running. Verify wake-up and downstream consumers before expanding schedules. Coordinate monitoring for expected downtime and preserve backup execution. Do not apply development sleep policy to production or shared integration environments by assumption.

## Close the review

Record measured value, timestamp/window, policy comparison, result, action, owner, and due date. Carry forward unresolved exceptions without losing their original date. Automate stable read-only checks where useful and link the deeper runbook for remediation.

Report completed checks, unknowns, material exceptions, changes made, and next review. A housekeeping review is complete when its findings are accountable; deeper remediation can remain explicitly tracked.

For retired features/services, coordinate consumer migration, remaining jobs/data, access revocation and resource/documentation cleanup with change-verification expertise. Age or naming alone is not evidence that a live dependency can be removed. Routine supported-version reviews can identify upgrade work separately from vulnerability deadlines.
