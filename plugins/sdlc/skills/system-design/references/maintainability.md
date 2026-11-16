# Maintainability and operability design

Maintainability is the cost of the next change. Operability is the cost of running what exists. Both are design properties: they come from where responsibility sits, how change crosses seams, what the system emits, and how it is upgraded and diagnosed — not from documentation added afterwards.

Treat them as constraints on the design when the change affects a long-lived system, a shared module, a platform dependency or a team other than the author's. A prototype may legitimately defer them; say so rather than appearing to satisfy them.

## Modifiability

- Identify the axes of likely change from the accepted outcome and product direction: a new client, provider, format, tenant rule, pricing model, locale or integration.
- Place seams where variation is real. Use the [codebase design](../../codebase-design/SKILL.md) vocabulary — module, interface, seam, depth, leverage, locality — and its tests: would deleting this abstraction concentrate complexity or merely move it, and are there two real adapters or only one hypothetical one?
- Prefer locality: a change that touches one module and its tests is cheaper than one that edits every caller. A shared abstraction that forces a coordinated release across consumers has moved the coupling, not removed it.
- Keep interfaces small and honest about invariants, errors, ordering and configuration. A wide interface with pass-through behavior is cost without leverage.
- Decide what may be removed. Designs that can only accrete accumulate dead paths; name the replacement and deprecation boundary for the old one.

For a deliberate architecture improvement, use [improve codebase architecture](../../improve-codebase-architecture/SKILL.md) to scan for deepening opportunities and [improve](../../improve/SKILL.md) to act on an accepted objective; use this design phase to decide the target shape and its obligations.

## Testability

Testability is a design output, not a test-team input.

- Put the test surface at the same seam callers use. If a behavior can only be verified by reaching past the interface, the module shape is probably wrong.
- Accept dependencies rather than constructing them, and return results rather than mutating hidden state, so behavior can be exercised without a full environment.
- Make time, identifiers, randomness and external effects injectable or observable where determinism matters.
- Define the contract tests for each seam, including error and denial mapping, retries and compatibility. Unit coverage of internals is not evidence that the seam contract holds.
- Decide test data ownership and isolation, and the boundary between fixtures and live dependencies. A test that requires production-like data is a design constraint, not a testing convenience.

[Test](../../test/SKILL.md) owns check selection, execution and completion evidence. This reference decides what the design must make testable.

## Operability and observability

- Decide how the change is deployed, configured, rolled back and, where relevant, feature-flagged. State the blast radius of a bad release and the time to reverse it.
- Name the signals that distinguish the important failure modes: the operation, its population, the dependency or stage that failed and the work left unfinished. Signal contracts and instrumentation belong to [observability](../../observability/SKILL.md).
- Define the runbook need at design time: what an operator must check, which authority they need and what must not be done under pressure. Use the [runbook guide](../../guide-runbook/SKILL.md) for the procedure.
- Avoid designs that require undocumented manual repair for normal operation. Manual steps are acceptable when bounded, named and owned; they are not a substitute for recovery behavior.
- Bound on-call load: an alert that fires without an action, or a failure that pages the wrong team, is an operability defect.

Availability, latency, freshness and recovery targets and their evidence belong to [reliability](reliability.md). This reference covers the diagnosability and operating burden that make them achievable.

## Dependency and upgrade path

Every dependency is a standing obligation. Establish:

- the supported version range and the cadence of security and major upgrades;
- what pins, vendoring or lockfiles hold it, and how an update is rehearsed and rolled back;
- the license and distribution terms that affect the product's intended use;
- the interface or adapter that isolates it, and the exit path if it is replaced or withdrawn;
- the data and schema migration path when the dependency owns durable state.

A dependency that cannot be upgraded without a coordinated outage is a design risk. So is one whose data cannot be exported. Use [dependencies](../../dependencies/SKILL.md) for update review and vulnerability remediation evidence, and [release](../../release/SKILL.md) for the deployment and rollback path.

## Onboarding and legibility

A design should let a new contributor find where a behavior lives and why. Name the entry point, the authoritative record and the boundary that would otherwise require archaeology. Keep current-system documentation aligned through [system documentation](../../system-documentation/SKILL.md) rather than duplicating architecture in this design.

Legibility is not a request for more documents. It is the ability to answer "where does this happen, what may I change, and how would I know I broke it?" from the design and the code.

## Evidence questions

The design has addressed maintainability and operability when these can be answered without guessing:

- How long would it take to add the next plausible variation, and how many modules would change?
- What is the blast radius of a defect in this design, and how is it detected and reversed?
- Can the critical behavior be tested through its interface, including failure and denial, without a production-like environment?
- Can an operator diagnose the main failure modes from emitted signals, and is there a bounded procedure?
- Can each material dependency be upgraded and, if necessary, replaced within an accepted outage or cost?
- Could someone who did not write this find the entry point and the record?

A measured answer is stronger than an assertion. A refactor rehearsal, a test-seam probe or an upgrade dry run is evidence; "the code is clean" is not.
