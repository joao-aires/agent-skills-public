---
name: engineering-workspace
description: Discover and manage external-to-code engineering change artifacts using an authorized filesystem folder or optional tracker/document platform, with stable links, ownership and revisions.
user-invocable: false
metadata:
  scope: generic
  invocation: agent
  role: support
---

# Engineering workspace: storage independent of application code

The engineering workspace is the **authoritative home for change-oriented engineering knowledge**, parallel to the application's source repository. It does not prescribe an issue tracker, wiki, folder tree, API schema, or synchronized duplicate store. Read [engineering-artifacts](../engineering-artifacts/SKILL.md) for required ECR content and handoff semantics; this skill handles discovery, identity, persistence, revision and cross-system references only. The requested activity controls when and whether writes are authorized.

## Resolve the workspace before editing

1. Inspect project/user instructions for an existing workspace, ECR/document links, app repository mapping and authorized actions. Inspect the work item's supplied references and existing records before creating one.
2. If configured, use its designated authoritative home. A workspace may be **filesystem files** outside the application repo, a separate Git repo, or supported document/issue services such as Linear or Plane. An integration must actually be connected/available; plugin installation or a product mention does not establish access.
3. **Whenever an engineering activity needs to persist an ECR and no authoritative home or explicit storage preference exists**, an **interactive agent must ask the user which storage they want before choosing one**. This applies to `refine`, `design`, `plan`, `develop` and other phase entry points—not only `setup`. Ask one concise choice: an authorized filesystem folder (possibly a sibling Git repo), an **existing connected** document/tracker service, or **no persistence / inline only**. Offer a sensible filesystem path as a proposal, not an action. If the selected location/path still needs authorization, clarify that boundary before writing. Do **not** choose filesystem or a connected service merely because it exists.
4. **Respect the answer across later phases.** Once the user chooses a usable home, verify access and record a portable discovery pointer in authorized project instructions; never re-ask while that authority remains valid. If the user chooses inline only, return clearly unpersisted results and do not re-ask unless the preference changes. A task explicitly restricted to read-only/inline output already answers the storage question.
5. **Without interactive feedback** (unattended/event task) or when the user has not yet answered, continue independent authorized analysis, return the structured ECR outcome **unpersisted**, and surface the precise storage-choice blocker; do not claim durable completion or write to a guessed root. If a configured authority is temporarily unavailable, preserve that authority and ask about restoring access rather than silently migrating providers.
6. Distinguish authority (where the primary ECR is edited) from visibility (links/previews in tickets, PRs or docs). Never silently switch authorities on provider failure, or create divergent authoritative copies.
4. Distinguish authority (where the primary ECR is edited) from visibility (links/previews in tickets, PRs or docs). Never silently switch authorities on provider failure, or create divergent authoritative copies.

Read [filesystem workspace](references/filesystem.md) for discovery and minimal layout; read [provider-neutral integrations](references/providers.md) when using external documents, trackers or mixed backends. After a first-time choice in **setup or any SDLC phase**, establish a **portable discovery pointer** in existing project instructions when authorized: chosen backend, how to resolve/access the root from a fresh checkout, ECR discovery convention and history/permissions. Prefer relative-to-shared-root references or stable remote URLs over personal machine paths. The pointer only describes an existing authorized authority; it is not a request to create or synchronize a second authority.

## Portable operations — semantics, not an invented API

- **Find:** locate change identity and current ECR, discover relevant PRD/RFC/diagrams, repo baseline and existing issue/PR; detect duplicates.
- **Read:** load exact authoritative content, known revision/status and related decisions before changing it.
- **Create:** when authorized and genuinely absent, use a stable human-readable identity/title and the standard ECR sections. Do not invent a provider key/URL.
- **Update:** preserve unrelated edits/accepted decisions, record material changes and reconcile conflicts against the freshest revision. For concurrent writers use actual provider version/ETag/Git head checks where supported.
- **Link:** preserve canonical targets, readers' access, relevant base revision, affected PRs and source citations.
- **Report:** give the actual verified path/URL/revision or explicitly state not persisted. Surface access/permission/attachment limits without pretending success.

The entry-point task still owns the requested engineering output, source edits and publication scope. Do not use document access as permission to modify issues/PRs, send notifications, merge, deploy, or provision accounts.

## Provider fidelity

Different backends have different capabilities. Do not claim uniform transactional writes, comments, revision history or embedded diagram rendering. If a provider cannot host a diagram source, store it in an authorized file/artifact location and link it; if no such location exists, return it inline with a storage blocker. Filesystem storage needs an explicit durability strategy (prefer an existing Git-backed workspace for teams; otherwise report the absence of revisions). A path outside the app repo remains distinct even when it is on the same disk.

**No mandatory external service.** A local agent should be fully able to maintain an ECR and related Markdown/diagram files in a configured folder without creating an issue, project or remote document.
