# Choose operations guidance

Start with the requested service, environment and outcome. Read its instructions and accepted policies. These skills work during initial setup, affected feature work, an explicit review, or a recurring task already configured by the project. Installing the plugin does not schedule reviews, connect monitoring, configure MCP servers or grant production access.

| Need | Skill |
| --- | --- |
| Define user outcomes, SLIs/SLOs and actionable alerts | `reliability-design` |
| Implement and verify logs, metrics, traces and collection | `observability-operations` |
| Stabilize and investigate current user harm | `incident-response` |
| Write actionable diagnostic/recovery procedures | `runbook-engineering` |
| Reconstruct incidents and derive causal learning | `postmortem-facilitation` |
| Verify learning actions changed deployed behavior | `postmortem-followup` |
| Prove data and application recovery | `protect-and-restore-data` |
| Manage findings and identity lifecycle | `vulnerability-management`, `credential-lifecycle` |
| Plan resources and spending | `plan-application-capacity`, `optimize-application-cost` |
| Run bounded recurring maintenance reviews | `operational-housekeeping` |

Generic guidance fits the actual hosting stack. Seek available matching platform/runtime expertise when implementation needs it; Datadog/Terraform examples are optional adapters, not defaults. Consult current first-party documentation before platform-specific commands. Detailed references support difficult cases; the entry-point instructions carry the common decisions.

Preserve authorization already established by the task. Read-only investigation and local patches can proceed within scope. Live mutations need the intended target/action authority; never infer it from a skill. Communications, incident publication and stakeholder commitments follow the user's instructions. Drafts and simulations stay labeled. Interviews begin only when requested.

For repeated reviews, reuse the project's existing records. Keep stable finding IDs, first-seen dates, evidence windows, owners and dispositions; reconcile before creating duplicate work. A review can conclude no change is needed. Unknown or inaccessible evidence is not a healthy result. Configured, locally tested, live verified and outcome recovered are separate states. Return the relevant evidence and outstanding checks without forcing a ticket system, schema framework or full audit onto a focused change.

Investigate consequential findings before asking the user. Within accepted scope, fix ordinary defects without repeated approval. If resolution changes budget, data exposure, authority, service expectations or loss/recovery tolerance and existing policy does not settle it, present evidence, options and a recommendation, ask the specific decision, and pause only dependent work. Preserve accepted answers; a reported risk is not an accepted risk. Apply the in-package composition guidance; available workflow expertise can deepen the work without becoming a dependency.
