# C4, user journeys and sequence diagrams across SDLC phases

Diagrams are **source-controlled knowledge and proposed designs**, not decorations automatically reproduced in every handoff. A current implemented-state baseline belongs in the application's established documentation on a stable branch. Target/future diagrams and draft sequence/journey views belong in the engineering workspace's ECR or linked RFC until actual implementation is reconciled.

## Who owns what

- **system-documentation** traces current entry points, runtime relations, data journeys and evidence, and establishes or maintains canonical C4 context/container and relevant component views, sequences, state/dataflow and deployment boundaries. These are evidence-backed descriptions of **what currently exists**, not intended design.
- **requirements-engineering / interface-design** define user intent, journey/wireflows, actors, branches and observable outcomes; they do not turn a proposed queue or database into a requirement.
- **system-design / design** own proposed responsibilities/architecture, tradeoffs, affected C4 context/container/component views and critical user-to-system sequence diagrams. Diagrams must label *proposed* and the baseline revision.
- **plan** uses accepted target views to order slices, migrations and verification; it references them instead of copying them.
- **implement/test/review** compare actual change with proposal at a specific revision, adjust design decisions and canonical documentation as warranted, and expose unresolved variance.
- **release/operations** distinguish merged application code from deployed observed targets; reconcile deployment/operations views based on real evidence rather than commit existence alone.

## Required conditional outputs

| Change | Expected diagram work |
| --- | --- |
| New app/service | Initial **proposed** C4 context and container + one or more representative user journeys and critical runtime sequences; establish initial current-state canonical views with implemented evidence |
| Boundary-changing feature / rearchitecture | Read current C4/sequence baseline at revision; produce focused **target** affected views, including key failure/retry/migration branches; record delta and alternatives |
| Major UX journey change | User journey or wireflow with state/error paths, and technical sequence when service/data boundaries matter |
| Local fix/refactor without boundary or journey change | State "baseline diagrams unaffected" with a reason; no invented or unnecessary new diagram |
| Runtime/release-only change | Update impacted deployment/operating diagrams with actual target state where verified |

C4 context/container are default views for a new system; component zooms appear where ownership ambiguity justifies them. Do not insist on every C4 level or a sequence for every endpoint. Diagram labels, nodes, directed edges and message order must be consistent with accompanying prose and API/ownership contracts.

## Handoff pattern — prose, not a rigid manifest

At design completion, record **baseline** (path/link + commit), **target** (proposed view link/attachment), **what changes** (responsibility/relationship), **open decision** and **how to check it**. Example:

> Current: `docs/architecture/containers.md` at base commit. Proposed: Export scheduling in the linked ECR C4 container view and a sequence showing authorization/retry/completion. The new worker owns delayed execution; the existing API remains the authorization boundary. Verify cancel/revoke/duplicate deliveries before promoting this design to implemented state.

A reviewer can follow these links from issue or PR; no duplicate diagrams in every stage.

## Reconciliation

Before merging implementation that changes actual system boundaries, update relevant **canonical application-repo docs in the same change**, reflecting observed implementation at the checked revision, and link the ECR's proposed views/decisions. Do not merge projected target diagrams into a current-state page unchanged if code deviated. A merged revision is not deployment proof. Keep accepted prospective ADR status explicit. If design was not implemented, keep the target in the workspace and the canonical baseline untouched. Check identifiers and relationships against the contract and actual source. Inspect the affected view as the reader receives it.


## Verify the view the reader can open

Check that source persists, the target view renders, and the intended audience can access it. For a consequential diagram, inspect the rendered view for legible labels, visible boundaries and correctly ordered interactions, including failure paths that affect acceptance. Keep an editable source alongside the view or at a stable authorized link.

If the workspace displays diagram source as code, link a verified rendering from a location the audience can access. If rendering or access cannot be checked within scope, give a concise textual account of the relationships and state the limitation. Keep proposed and implemented labels on the view itself and tie it to the applicable source baseline or revision.
