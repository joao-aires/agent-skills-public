---
name: setup
description: Establish a new application or adopt an existing repository, discover
  working commands and accepted constraints, and prepare a useful first slice. Use
  for explicit project setup or adoption; preserve an existing project layout and
  tooling.
user-invocable: true
disable-model-invocation: true
metadata:
  scope: generic
  invocation: user
  role: task
---

# Setup

Read [task guidance](../../TASKS.md). Read [git-contributions](../git-contributions/SKILL.md) before foundation writes. Seek available delivery expertise for CI, artifact and recovery decisions. Read [project-conventions](../project-conventions/SKILL.md) for repository foundations and working commands. Load the optional stack/domain guidance selected by task guidance only when relevant and available.

Setup is technical foundation work, not a substitute for product discovery. Before architecture-dependent writes, establish the intended usage, bounded journey and material platform/licensing/budget constraints. For a rough idea needing end-to-end development, use the outcomes in [new-application flow](../develop/references/new-application-flow.md) within the requested scope; a setup-only request does not authorize feature implementation or an unsolicited full business study.

## Establish useful foundations

Use project-conventions to discover the repository, accepted stack, commands, identity model, environments and critical journey.

| Project context | Foundation work |
| --- | --- |
| New project | Establish useful foundations for the requested first slice. Satisfy the [applicable foundation contract](../project-conventions/SKILL.md#complete-new-project-foundations), including authored onboarding, checks/tests, packaging and delivery artifacts. |
| Existing project | Preserve working foundations, identify missing context and address the requested gaps without restructuring the application. |

## Select a durable engineering workspace (only if not already configured)

During initial setup or adoption—and consistently in subsequent SDLC entry points—use [engineering-workspace](../engineering-workspace/SKILL.md) to discover **where ECRs and proposed designs will live outside the application code repository**, or whether the user has explicitly chosen inline-only output. Prefer an existing authorized workspace; do not replace its authority or ask for the same choice again. If none is configured, offer **one focused decision** between (a) a filesystem directory under a known authorized parent, possibly an independent Git repository, and (b) an existing connected document/tracker service when the user wants it. Suggest a practical sibling folder only as a **proposal**; never create it outside the authorized scope without approval. A tracker, remote account or special directory layout is not required.

Once a location is selected and writable within scope, verify it can be discovered and accessed, note its revision/history strategy and link conventions, then record a **portable workspace pointer** in the project's existing contributor/project instructions (such as scoped `AGENTS.md`) when editing those instructions is authorized. Include the backend, how to resolve the root from a clean checkout, how to locate a change ECR, and any independent versioning/visibility constraints. Avoid machine-specific absolute paths, credentials, creating an empty ECR, or making the application repository a second ECR authority. If selection or access is unavailable, report a specific pending setup choice while completing unrelated authorized foundations; don't claim durable handoffs are configured.

Connect the foundations into a usable development path. A contributor should be able to obtain the required configuration, install dependencies, start the application and run its checks using the documented commands. Where persistence is part of the slice, include how the local data store is prepared and how schema changes are applied. Use sample configuration that explains required values without containing secrets.

Ask about consequential product/platform choices, then record the accepted choices and working commands in existing instructions/docs. Run the available startup, migration and test paths far enough to expose missing dependencies or mismatched configuration. Distinguish artifacts prepared for a future target from a path actually exercised on that target. Name unresolved targets, missing prerequisites and unavailable tools.

Setup does not establish that an application feature is complete. Use develop when the request is to build the application end to end.
