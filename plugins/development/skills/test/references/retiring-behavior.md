# Retire a capability without leaving dependencies behind

Use when deprecating or removing a feature, service, interface or operational resource. Establish actual consumers from code/configuration and appropriate usage evidence; absence from sampled telemetry is incomplete evidence of non-use.

1. Define ownership, supported compatibility period, exit criteria and fallback. Migrate callers and account for queued/scheduled work before removing support. Resolve retention, export and recovery obligations before destroying data. Use the project's existing communication process; sending still requires authorization.

2. Inspect related flags, credentials/grants, jobs/routes, infrastructure and documentation. Retire them only after their consumers and obligations are addressed, preserving required recovery access and artifacts. Use the relevant operations guidance for credential revocation, restoration or resource cleanup when available.

3. Verify the intended user/consumer behavior and actual resource state after the change. Record residual obligations and unexecuted steps in existing project records. A removed source file or successful deployment alone does not establish complete retirement.
