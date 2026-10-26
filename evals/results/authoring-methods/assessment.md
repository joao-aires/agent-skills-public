# Authoring and workflow probes

These are three bounded independent guidance probes, not application-generation trials, participant research or a comparison with the previous skills. Each actor used a separate context and isolated raw artifacts. The evaluator supplied the tasks and inspected the outputs and changed bytes against criteria kept outside actor scope.

[Inputs and criteria](inputs-and-criteria.json) retain the raw fixture files, requests, source base and candidate bundle fingerprints. Source and built-resource checks identify the candidate; actor-declared read lists do not establish native client routing or automatic skill discovery. Model/version metadata was not exposed. There was no coordinator repair or second generation.

## Results

| Case | Criterion results | Evidence and limitation |
| --- | --- | --- |
| Feature exploration and handoff | 4 pass | [Design and plan](workflow/result.md) traces the actual CLI, service and JSON store, labels proposed additions, orders useful increments and keeps the help-text correction small. Existing three tests ran; archive/restore was neither implemented nor verified. |
| Repository instruction maintenance | 3 pass, 1 partial | [Actor report](instructions/result.md) preserves privacy, owner isolation and the unique compatibility-file requirement, corrects commands and excludes temporary/unaccepted session advice. [Actual changed bytes](instructions/actual-changes.json) confirms only the three allowed instruction files changed. Its displayed report diff contains one stale phrase absent from the final nested file, so the reporting criterion is partial. |
| Skill authoring by purpose | 4 pass | [Rationale](authoring/result.md), [spacing revision](authoring/component-spacing/SKILL.md) and [diagnostic revision](authoring/job-failure-diagnosis/SKILL.md) retain different structures. The diagnosis now links evidence, explanations and distinguishing checks; spacing remains a compact craft method. No actual component or background job was exercised. |

The maintenance reporting discrepancy concerns the nested file's command introduction: the actor's displayed diff includes “run tests before delivering a change,” while the final nested file says only “Run from the repository root.” The root instruction still contains the delivery requirement, so no required constraint was lost. The actual final file contents are authoritative; the report was not edited to conceal the discrepancy. This observation alone does not establish a defect in the instruction-maintenance method or justify another universal rule.

## Evaluator checks

- Compared every workflow and authoring input byte against the raw fixture record: unchanged.
- Compared maintenance inputs: only AGENTS.md, tests/AGENTS.md and CLAUDE.md changed. Application source, tests, data, canonical docs and session notes were unchanged.
- Re-ran the maintenance fixture's standard-library unittest command with bytecode disabled: all three tests passed. These are fixture service tests, not feature acceptance or importer/export tests.
- Reviewed the outputs against each case's four criteria. No aggregate score hides the partial reporting result.

## Evidence limits

No baseline run, reliability estimate, unfamiliar client installation, live model/provider integration or broad collection adherence is established. These probes support only the recorded authoring, planning and local instruction-editing outcomes. The candidate fingerprints and fixture records permit a repeat with the same inputs. Complete-package checks and the repository regression suite establish different properties.
