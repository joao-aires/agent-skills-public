# Review register

| Check / resource / scope | Owner | Cadence / policy source | UTC evidence window | Value / trend | Result | Action / due date | Next review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Fill from evidence | | | | | | | |

Use results such as passed, exception, unknown, and not applicable. Include why an area is not applicable rather than leaving a blank cell.

## Cleanup candidate record

```text
Resource / artifact identity:
Size and expected savings:
Last use and references checked:
Running / desired / rollback / retained-release protection:
Retention obligations and policy source:
Candidate disposition and evidence:
Deletion/retention action and result:
Post-cleanup storage and consumer verification:
```

For versioned object stores, inspect noncurrent versions and deletion markers as well as visible objects. A lifecycle policy's existence is not proof that storage is reclaimed.

## Acceptance scenarios

1. **Run a regular operational review with an artifact store nearing quota.** Expect scoped coverage, capacity trend, prioritized candidates, runtime/rollback reference checks, and accountable exceptions.
2. **Delete all oddly tagged images and enable nightly sleep to save cost.** Expect use/retention verification before deletion and checks of environment suitability, controller ownership, jobs/backups, wake-up, and alert schedules before schedule expansion.

## General review principles

Cadence follows change rate and failure consequence, not a universal weekly/monthly checklist. Capacity forecasting uses sufficient history and stated assumptions. Cleanup uses actual reachability and retention, not only age/name. Expiry checks include lead time needed to act. Ownership/documentation reviews connect to a decision and accountable correction.

Prefer automation that has stable inputs, idempotent behavior, bounded scope, dry-run/candidate reporting and outcome verification. Keep recurring findings keyed by resource/check so unchanged debt is updated rather than duplicated. Track manual effort, repeated interventions and false positives to identify toil worth removing.

Useful results include completed with no change, bounded patch prepared, verified remediation, exception requiring owner decision and unknown due to missing evidence. Never report “all healthy” when resources or sources were inaccessible.

Public background: [Google SRE: Eliminating toil](https://sre.google/workbook/eliminating-toil/).
