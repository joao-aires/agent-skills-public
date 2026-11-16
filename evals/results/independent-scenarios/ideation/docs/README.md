# Documentation

This directory holds the durable records for the local habit tracker. The code and tests live at the repository root; this index records where each concern is authoritative.

Current state: first slice **implemented and verified locally** on 2026-11-15. Not released, not packaged, and not measured in real use. See the [verification limits](evidence/verification.md#limits-and-unverified-claims).

## Artifact homes

| Artifact | Home | Authority | Owner | Update when |
| --- | --- | --- | --- | --- |
| Product intent | [`product/prd.md`](product/prd.md) | Problem, audience, outcome, scope, success signal | Requester | Outcome, scope or priority changes |
| Design proposal | [`design/design-proposal.md`](design/design-proposal.md) | Streak/missed-day decision, options, surface, tradeoffs | Requester (delegated) | Semantics, surface or compatibility changes |
| Streak specification | [`design/streak-cases.md`](design/streak-cases.md) | Worked cases and reader-visible streak results | Engineering | Streak rule or display changes |
| Change record | [`change/ecr.md`](change/ecr.md) | Requirements, acceptance, implementation, verification, decisions | Engineering | Each material change to this slice |
| Verification | [`evidence/verification.md`](evidence/verification.md) | Commands, actual results, review findings, limits | Engineering | A check is run or a limit changes |
| Raw test output | [`evidence/test-output.txt`](evidence/test-output.txt) | Observed `unittest` run | Engineering | Test suite changes; regenerate |
| CLI transcript | [`evidence/cli-transcript.md`](evidence/cli-transcript.md) | Observed command outputs and exit codes | Engineering | CLI behavior changes; regenerate |
| Help text | [`evidence/help.txt`](evidence/help.txt) | Observed `--help` output | Engineering | CLI surface changes; regenerate |
| README | [`../README.md`](../README.md) | Entry path and command summary | Engineering | Setup, commands or status changes |
| Code and tests | `../habits.py`, `../test_habits.py` | Implemented behavior and regression coverage | Engineering | Every behavior change |

No separate architecture set, ADR, issue, PR or runbook exists. The project is one local script with no service boundary, deployment target or multi-person coordination. The design proposal records the one consequential decision; the ECR carries the change account.

## Reading order

1. [README](../README.md) — what it is and how to run it.
2. [Product outcome](product/prd.md) — why it exists and what is excluded.
3. [Design proposal](design/design-proposal.md) — why the streak rule is defined this way.
4. [Streak cases](design/streak-cases.md) — the exact expected behavior.
5. [ECR](change/ecr.md) — requirements, implementation and claim status.
6. [Verification](evidence/verification.md) — what actually ran and what did not.

## Maturity

| Record | Maturity |
| --- | --- |
| Product outcome | Proposed first slice; no separate product review |
| Design proposal | Accepted for the first slice |
| ECR | Implemented and verified locally per requirement; release not applicable |
| Verification | Local evidence at the recorded content hashes; real use unmeasured |
| README and docs index | Current for this workspace |

This directory is not a Git repository. Revisions are local content hashes, not commits, and nothing here is published.
