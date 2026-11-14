# External document/tracker providers and mixed workspaces

Treat Linear, Plane, GitHub Issues/Projects, Notion, other document services, and filesystem folders as **possible storage/coordination capabilities**. Their support for full documents, attachments, accessible diagrams, comments, revisions or APIs differs. **Discover real connected tool capabilities** before using them; do not pretend every provider has the same operations, nor require any one integration.

## Configuration as intent, not mandatory machine-readable schema

Existing project/user instructions may specify:
- The **authoritative ECR home** (filesystem root, document collection, work item description or dedicated document).
- Optional PRD/product and RFC homes, associated application repos and how stable links are exposed.
- Preferred storage for editable Mermaid/C4/sequence diagrams, who may read them, and versioning expectations.
- Existing tracker for issues, git host for PRs and permissions for each kind of write.

These can be written as prose in `AGENTS.md`, an existing project convention or user-provided instructions. No required YAML adapter config; do not automatically connect, subscribe to, publish to or mutate third-party systems based on their names.

## Mapping without false equivalence

| Workspace surface | ECR representation | Limit |
| --- | --- | --- |
| Filesystem folder / independent Git repo | Canonical Markdown document + optional linked RFC/diagram files | Revision history only when supported/enabled; file path access must be authorized |
| Document platform (e.g. Linear/Plane **when supported by connected account**) | Canonical project/issue document, or linked document set | Confirm actual document APIs, rich text/attachments, visibility and revision handling |
| Issue-only platform (e.g. GitHub Issues) | Bounded ECR in issue body *if suitable*; for large ECR use a linked authorized document/file home | Issue title/body/comments may not be a good home for large editable diagrams |
| Hybrid environment | Choose one authoritative home per document, with references in other systems | Avoid competing copies; edits and permissions may not synchronize |

When a provider is unavailable mid-run, **do not silently switch its authority** to filesystem or copy private contents into public issues. Preserve the original record identity and give a precise blocker, local non-authoritative draft only if authorized, or inline outcome.

## Read, write and reconcile

For each provider, establish its actual find/read/create/update/link capability and whether it exposes a version, revision or concurrency guard. Do not infer an API from a vendor brand. Resolve actual identifiers from supplied links or returned tool data. Re-read before writes and preserve edits; on version conflict reconcile and retry safely rather than overwriting.

**Plane Pages integration observation (2026-11-10):** A private project Page supported create → retrieve → update → retrieve with the seven-section ECR intact, but Plane's rich-text editor normalized heading/paragraph HTML (added attributes), so inspect semantic structure rather than raw HTML equality. The connected `page update` action replaces the **whole HTML body** and exposes no compare-and-swap/ETag argument; a controlled sequential stale edit overwrote a newer change with no conflict error. **Read-before-write alone does not eliminate this race.** For shared/concurrent Plane ECRs, only edit after reading the latest version; check for intervening changes immediately before the update, preserve the latest body and avoid claiming atomic conflict safety. If competing writes are plausible and no serialization/conditional update is available, explicitly warn that changes can still be lost; choose an independently versioned authority or an agreed single-writer coordination policy for consequential concurrent edits. Do not claim a reliable provider revision lock from `updated_at`, or silently migrate records. The disposable test Page was deleted. See [bounded Plane ECR observation](https://github.com/joao-aires/agent-skills-public/blob/5eb72b2d1f64845d159d743232a2bfdab4312aad/evals/results/engineering-artifact-workspace/plane-pages.md).

Read the saved record back to check headings, lists, links and evidence. For important diagrams, confirm what the intended reader can open. A Plane Page can preserve Mermaid in a code block while showing plain text in the editor. Use the [diagram lifecycle](../diagram-lifecycle.md#verify-the-view-the-reader-can-open) to resolve that limitation. Use only authorized destinations and respect visibility when linking to private records from issues or PRs.

## Example dual-backend work

A team keeps a PRD in its project documentation service and an ECR with editable diagrams in a separate Git-backed engineering folder. Plane holds implementation issues, GitHub holds PRs, and the application repo holds current architecture. The ECR references PRD, issues, accepted target diagrams and code baseline. Issues/PRs show audience-specific summaries and canonical links. **There is one ECR authority**, not one copy in each tool.

No custom adapter runtime, account provisioning or background synchronization is provided by these instructions; integrations use only available connected tools with the user's actual permission.
