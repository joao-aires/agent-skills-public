---
name: guide-ecr
description: Guide to writing an Engineering Change Record. Covers overview, problem, requirements, solution design, implementation, verification and decisions across a change.
user-invocable: true
metadata:
  kind: guide
  domain: development
  phase: cross-phase
  scope: generic
  invocation: both
---

# ECR guide

An Engineering Change Record (ECR) is the evolving account of one coherent change: why it exists, what it must do, how it is designed, how it is built and what evidence supports the claims. It is the coordination spine, not the only artifact.

## Reader questions

1. What is changing, for whom, and why?
2. What is in scope and out of scope?
3. What must be true for the change to be accepted?
4. What was proposed, and which alternatives were rejected?
5. What has actually been built or checked, at which revision?
6. What has been released, and what is still pending?
7. What decisions were made, by whom, and what remains open?

## Minimum content

- overview, status and change identity;
- problem, scope and non-goals;
- requirements and observable acceptance;
- solution design, alternatives and linked design artifacts;
- implementation strategy and actual changes;
- verification and review evidence, with revision and environment;
- decision history, references and open items.

## Structure and quality

- Keep the current state first in every section; put old checkpoints in a history subsection.
- Write evidence in the past tense; “will verify” is a plan.
- Link the authoritative source instead of copying it.
- Separate proposed, implemented, verified and released claims.
- Record deviations from the design and their consequence.
- Keep the record compact for a small change and detailed for a consequential one.
- Update the record as the work moves; do not leave stale sections above newer evidence.
- Use one ECR per coherent change, not one per task or phase.

## Requirements set in practice

Section 3 of the contract owns the shape. This guide covers when to use each form, how to distinguish the kinds and how to review the result.

### Full or compact

Use the full form when any apply:

- more than one affected area, or a boundary, migration or external consumer;
- a non-functional target that must be observed (latency, availability, security, cost, accessibility, compliance);
- a user-facing or contract surface whose behavior the design must settle;
- requirements that design, test and release will cite by ID.

Use the compact form for a local, reversible change with one area and one evident approach. It still names the behavior, the applicable constraint and the check; it just skips tables that would hold one row.

### Functional, non-functional and design

| Kind | Answers | Fails when |
| --- | --- | --- |
| Functional | What the actor can do, under which conditions, with what observable result and denial path | It is a feature name with no observable result |
| Non-functional | How well the behavior must hold, for which population and conditions, observed how | It states a target with no observation point, or a dimension with no decision |
| Design | What the user-facing or contract surface must show, say or accept | It repeats the implementation shape or copies the design specification |

Design requirements are not a preview of implementation. "The error names the failed item and offers retry" is a design requirement; "retry uses exponential backoff" is implementation. Design resolves the first and links the artifact that settles it; the second belongs in solution design.

### Stable identification

Use the contract prefixes — `FR-<area>-###`, `NFR-<dimension>-###`, `DR-<surface>-###`, `AC-###`, `DEC-###`/`ASM-###` — with the area or dimension encoded so a reader can see where the requirement applies. Once design, tests or release cite an ID, treat it as immutable. Add a new ID for a changed commitment and mark the old one superseded; do not reuse a retired number. The compact `R<n>` list is for a record nothing outside depends on.

### Evidence mapping

Each acceptance row cites the requirement IDs it checks and states environment, revision, result and evidence. Evidence can be a test command, CI run, benchmark, monitor, contract probe, journey recording or linked design artifact; link the authority rather than pasting its output. One check may cover several IDs. A requirement with no acceptance row is a gap, not an accepted requirement. Non-functional evidence names the observation point and window; a passing functional test does not establish a latency or availability target.

### Worked rows

| ID | Area | Requirement | Priority | Status |
| --- | --- | --- | --- | --- |
| FR-export-001 | member export | An authorized member can request an export of their permitted records; a denied member sees no record count or partial file | Must | Accepted |
| FR-export-002 | member export | A permission change after request removes newly unauthorized records from the result | Must | Proposed |

| ID | Dimension | Area | Target or tolerance | Conditions | Priority | Evidence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NFR-performance-001 | performance | member export | Completion within an agreed dataset band; target unresolved | 10k records, single region | Must | DEC-002, benchmark pending | Open |

| ID | Surface | Type | Requirement | Evidence |
| --- | --- | --- | --- | --- |
| DR-export-status-001 | export status | Functional | Status distinguishes queued, running, ready, expired and failed, and states what the member can do next | design spec §3.2 |

The contract owns the columns; these rows show the kind of content each expects.

## Common failures

- seven headings with no answers;
- “see issue” or “as discussed” without context;
- a status that claims more than the evidence;
- a design section with no alternatives or failure behavior;
- verification that lists commands but not results;
- a release claim based on a merge or build;
- history rewritten to make the change look cleaner than it was;
- requirements tables with headers and no rows, or every row left `TBD`;
- a quality checklist that names dimensions but records no target, decision or omission reason;
- design requirements that copy the design specification instead of stating the obligation and linking it;
- invented numeric targets, owners or regulatory commitments;
- requirements that restate the implementation, or acceptance rows with no requirement IDs or evidence;
- IDs renumbered to match implementation order.

## Review

Read the ECR as a reviewer who was not in the conversation:

- Can you explain the change and its scope?
- Can you tell what is accepted, proposed, implemented and verified?
- Are the design and verification evidence sufficient?
- Are open decisions and owners visible?
- Does every claim have a revision, target or link?
- Can you name the affected areas and which requirement IDs apply to each?
- Does every accepted requirement have an acceptance row, and every open one a decision owner?
- Do design requirements link the artifact that settles them without duplicating it?
- Do non-functional targets state conditions, observation point and evidence?
- Does the record show which dimensions were excluded and why?

## Handoff

The next phase needs the current outcome, accepted decisions, evidence and open items. A phase handoff may also use a design specification, architecture view, test result or runbook; the ECR summarizes and links them. Do not copy every artifact into the record.
