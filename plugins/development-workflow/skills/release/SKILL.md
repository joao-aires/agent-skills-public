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

Resolve the objective: prepare/readiness review or an authorized publish/deploy/recover action against an identified target. Use delivery expertise and relevant stack/operations guidance for immutable artifact identity, actual configuration, schema/data/consumer compatibility, test gates and recovery. Preserve established authorization without repeated ceremony; an unspecified target/action stays a blocker to execution.

Prepare a concise release assessment by default. For an authorized execution, use the established CLI/MCP/pipeline, serialize mutations as required and record actual effects. Verify served revision, critical journeys and async/cache paths rather than treating a successful job as customer success. Report prepared, locally checked, released, deployed and target-verified states separately. Do not automatically merge, deploy production or restore data from a generic release request.
