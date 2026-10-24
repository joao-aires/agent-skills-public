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

Connect the foundations into a usable development path. A contributor should be able to obtain the required configuration, install dependencies, start the application and run its checks using the documented commands. Where persistence is part of the slice, include how the local data store is prepared and how schema changes are applied. Use sample configuration that explains required values without containing secrets.

Ask about consequential product/platform choices, then record the accepted choices and working commands in existing instructions/docs. Run the available startup, migration and test paths far enough to expose missing dependencies or mismatched configuration. Distinguish artifacts prepared for a future target from a path actually exercised on that target. Name unresolved targets, missing prerequisites and unavailable tools.

Setup does not establish that an application feature is complete. Use develop when the request is to build the application end to end.
