---
name: deliver-reliable-changes
description: Implement, review and deliver application changes with focused verification, practical CI/CD and clear operational considerations.
---

Read [workflow framing](../../WORKFLOW.md) for skill selection and invocation boundaries.


# Deliver useful changes

- Read the relevant project instructions and existing patterns. Keep the change focused on the requested outcome and preserve accepted architecture and design decisions.
- Diagnose failures from evidence before patching symptoms. Use relevant upstream debugging, review or security skills when the change benefits from them; scale the depth to the risk.
- Run the checks that establish the changed behavior: lint/types/build, focused tests and important end-to-end journeys as applicable. Do not claim checks that were not run.
- Keep local and CI verification aligned. Prefer a small fast pipeline, minimal permissions, protected secrets and reproducible dependencies. Add delivery automation when the deployment target is known.
- Treat configuration, authorization, migrations, sensitive data and external side effects as application responsibilities. Use timeouts and bounded retries; plan recovery for meaningful data or deployment changes.
- Make failures diagnosable with useful logs and basic health signals. Add deeper monitoring, performance testing and backup/restore checks when operational needs justify them.
- Keep affected documentation current. Explain what changed, why, the verification evidence and remaining limitations in the PR. Capture recurring mistakes in concise project guidance.

Optimize for a working, maintainable application. Add process and infrastructure when they solve an observed problem.
