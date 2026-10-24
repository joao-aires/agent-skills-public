---
name: release
description: Prepare or execute a named application release/deployment with artifact,
  configuration, compatibility and recovery verification. Use for deployment readiness
  or an explicitly authorized target action; bare invocation prepares and reports
  rather than deploying.
user-invocable: true
disable-model-invocation: true
metadata:
  scope: generic
  invocation: user
  role: task
---

# Release

Read [task guidance](../../TASKS.md). Seek available delivery expertise for readiness, promotion and recovery. Load the optional stack/domain guidance selected by task guidance only when relevant and available.

## Establish the release boundary

Resolve the requested stopping point:

| Request | Result and execution boundary |
| --- | --- |
| Preparation or readiness review | Return a concise release assessment by default. |
| Authorized publish, deploy or recover action | Execute against the identified target through the established CLI/MCP/pipeline. |

Identify exactly what is being released, where it will run or be distributed, and which configuration belongs to that target. Connect the artifact to its source revision and check results. Review the changes that survive replacing application code, especially schema/data changes and effects in external systems, because these determine whether rollback is sufficient.

Establish what success will look like in the target and how a failed rollout will be contained or recovered. Use delivery expertise and relevant stack/operations guidance for immutable artifact identity, configuration, schema/data/consumer compatibility, test gates and recovery. Preserve established authorization without repeated ceremony; an unspecified target/action blocks execution.


## Execute an authorized action and verify

1. Serialize mutations as required and record their actual effects.
2. Verify the served revision, critical journeys and async/cache paths. A successful job alone does not establish customer success.
3. Report prepared, locally checked, released, deployed and target-verified states separately.

A generic release request does not automatically authorize merging, production deployment or data restoration.
