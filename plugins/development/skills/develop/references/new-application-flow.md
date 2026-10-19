# Start a new application from the intended outcome

Use this when develop starts from a new application idea. For an existing feature, resume at the affected decisions and preserve accepted work. Scale the depth: a personal tool needs a short purpose/constraints assessment, not a fabricated startup business plan. Use installed product discovery and prioritization expertise when the problem, useful scope or priorities need shaping; use business strategy expertise for unresolved commercial direction or viability. Keep these decisions separate from engineering requirements and implementation sequencing; supporting methods do not automatically invoke explicit-only tasks.

## Establish enough evidence before dependent work

| Stage | Useful result before proceeding |
| --- | --- |
| Purpose and business context | Intended user, problem, current workaround, personal/internal/commercial use, desired outcome and important cost/distribution constraints. Separate evidence from demand/revenue hypotheses. |
| Product definition | Use product discovery and prioritization expertise when available for the decision: bounded first useful experience, main jobs/journeys, scope/non-goals and a success signal. Preserve accepted decisions; propose unaccepted choices explicitly. |
| Requirements | Observable acceptance, realistic content, identity/ownership, failure states, supported platforms, relevant quality attributes and operating constraints. A concise brief/PRD is sufficient. |
| Feasibility and system design | Compare plausible options; verify consequential licensing, pricing, platform/protocol and integration claims. Resolve architecture-changing blockers before dependent scaffolding. Use system-design. |
| UX and visual design | Task flows, hierarchy, states and contextual visual direction; inspect a representative real screen or proportionate prototype using visual direction and semantic-token design expertise and interaction design expertise, then the selected stack conventions. Carry the requirements into the design. |
| Implementation plan and foundations | Small dependency-ordered increments with tests, chosen commands, complete applicable setup, CI/artifacts and release/recovery consequences. Reconcile the plan after design decisions. |
| Implementation, verification and repair | Commit meaningful tests with increments; run component/API and actual platform journeys, accessibility and rendered visual review. Preserve/reproduce findings and repair/recheck rather than lowering acceptance. |
| Delivery and learning | Review completion against the original outcomes; distinguish implemented/verified/blocked/released. Prepare delivery foundations, execute remote actions only when authorized, and feed observed product results into the next iteration. |

These are decision dependencies, not separate required meetings, task invocations or documents. Keep a concise record of accepted decisions, material assumptions, evidence, unresolved blockers and acceptance in the project's existing notes. A file bearing a phase name or a generated diagram does not prove that phase was completed. Small technical spikes may settle feasibility within scope; label them as disposable evidence rather than architecture or production commitments.

## Carry consequential decisions across phases

Use the shared [consequential finding policy](../../../WORKFLOW.md#resolve-consequential-findings) whenever an issue changes the product or operating constraints. It applies throughout the lifecycle, including existing systems; this new-product flow is only an early opportunity to discover the issues. Specialists investigate facts and options, and the shared policy determines whether a user decision is needed. Keep proposed and accepted choices distinct, and carry answers into dependent requirements, design, tests and delivery.

If the user rejects a critical dependency's terms or capabilities, preserve the product requirement and reopen the affected architecture. Compare replacements against the required behavior, portability, collaboration, embedding, accessibility and maintenance needs. Do not silently change the product or assume a prototype is production-suitable. A bounded technical spike remains evaluation evidence rather than an accepted production commitment.
