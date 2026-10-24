# Remediation record

| Finding / component | Affected deployed artifact / scope | First seen | Severity / exposure | Deadline / policy | Owner | Fix / migration | State / evidence | Next review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fill from evidence | | | | | | | | |

## Closure evidence

- Correct affected version/artifact identified; scan coverage recorded.
- Target release/coordinates and compatibility verified.
- Relevant tests and artifact scan completed.
- Fixed artifact deployed to all affected targets with identity evidence.
- Finding resolved by updated evidence, or disposition documented under the applicable process.
- Temporary mitigation/override removal condition and owner retained where needed.

## Override lifecycle

Record a searchable marker such as:

```text
SEC-OVERRIDE: package | finding | managed-version | added-date | reason | remove-when parent manages fixed version
```

Use the manifest's valid comment syntax or a companion record for JSON. Reconcile markers on parent/platform upgrades. Remove only after the unpinned build and scan remain clean.

## Acceptance scenarios

1. **Review a patch cycle with several dependency findings and a shared framework BOM.** Expect deduplication, verified curated upgrade options, migration review, original deadlines, and production evidence before closure.
2. **A fix is merged into development but production still runs the vulnerable image; another finding has no vendor fix.** Expect the first to remain deployment-pending and the second to have mitigation/risk ownership and review date, with neither deadline reset.

## Management reference

Read [patch-management.md](patch-management.md) for asset coverage, exploitation-informed priority and deployment verification. Local deadlines remain policy inputs.
