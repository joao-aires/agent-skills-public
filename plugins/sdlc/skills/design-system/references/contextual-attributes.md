# Contextual quality attributes

Compatibility, accessibility, compliance and portability are quality attributes that apply only when a product decision, contract, market, platform or regulation makes them apply. Applicability is a requirements decision. Design owns the boundary, the constraint and the evidence that the accepted baseline is met.

Do not treat them as a baseline every project inherits, and do not let a design invent a conformance level, jurisdiction or support matrix. When applicability is unknown, record the assumption and return the question.

## Compatibility

Compatibility asks what must keep working while the system changes: old clients, stored data, partner integrations, exported files, protocols and public interfaces.

- Identify the consumers and the contract they depend on, including clients that update slowly, cached clients and machine consumers.
- Decide the versioning and deprecation boundary: what runs concurrently, for how long, and how a consumer learns of a change.
- Cover data and wire format together. A new field that old readers ignore is not the same as a changed meaning that old readers misread.
- Decide the cutover and rollback for migrations, and which mixed-version states must work during rollout.
- State the compatibility claim and how it will be checked. Use the [compatibility matrix guide](../../guide-compatibility-matrix/SKILL.md) when a matrix is the fitting evidence.

Compatibility obligations follow from the [design](../../design/SKILL.md) seam decision and [software types](../../artifact-system/references/software-types.md); this reference only keeps the dimension visible.

## Accessibility

Accessibility asks whether people using assistive technology, keyboards, different input methods or constrained displays can complete the journey.

- Establish the accepted baseline first: a named standard and level, platform requirements or an internal policy. It comes from requirements, contract or regulation, not from the design author.
- Cover the journey, not the screen: focus order, keyboard operation, error identification and recovery, time limits, motion, contrast, zoom and text alternatives.
- Include states that are easy to miss: loading, disabled, denied, validation failure and asynchronous updates.
- Prefer the platform's semantics and the existing design system over bespoke widgets; a custom control owns the accessibility behavior it replaces.
- Verify with the relevant assistive technology or automated checks appropriate to the claim. Automated checks alone do not establish conformance with a named standard.

Use installed interface, accessibility and UX-writing expertise when available; otherwise use the project's accepted design system, primary accessibility guidance and observed user testing. The design records the affected surfaces and constraints; it does not certify conformance.

## Compliance

Compliance asks which legal, contractual or assurance obligations apply to this service and how the design supports their evidence.

- Separate a legal obligation, a contractual commitment and an engineering safeguard. They have different owners and different proof.
- Identify the service boundary, data classes, jurisdictions, providers, retention and customer commitments that the change touches.
- Design the boundary and data flow that a control depends on; do not invent the control's applicability or claim certification.
- Record the evidence the design will make possible — audit events, access records, retention behavior, residency — and what remains organizational.

[Compliance readiness](../../run-compliance-assessment/SKILL.md) owns applicability, control derivation and assurance evidence. System design supplies the architecture, data flow and provider responsibility split that those controls depend on. An EU region, an encryption toggle or a vendor certificate is not compliance by itself.

## Portability

Portability asks how costly it is to move, replace or leave a platform, provider or environment.

- Identify what is platform-specific: managed services, proprietary APIs, data formats, identity, deployment descriptors, billing commitments and operational tooling.
- Decide whether the design needs a seam at the provider boundary. One adapter is a hypothetical seam; portability claims need a real second implementation or a rehearsed exit.
- Keep authoritative data exportable, and know the export format, completeness and restoration path.
- Record residency, latency, availability and cost consequences of moving, not only the technical difficulty.
- Distinguish portability from multi-cloud ambition. Running the same dependency in two places can increase coupling and cost without reducing risk.

Use [dependencies](../../dependencies/SKILL.md) for dependency substitution and [release](../../release/SKILL.md) for deployment target changes. The design owns the seam and the exit reasoning; a rehearsal or export test is the evidence.

## Selection and evidence

| Attribute | Decide in design | Evidence that can support the claim |
| --- | --- | --- |
| Compatibility | Consumer set, versioning and deprecation window, migration and rollback | Contract tests and a mixed-version or old-client check |
| Accessibility | Accepted baseline, affected surfaces and states | Keyboard and assistive-technology observation; automated checks as a supplement |
| Compliance | Boundary, data flow, control owner and required records | Current operating evidence reviewed by the owning control or assessor |
| Portability | Provider seam, data export and exit path | Rehearsed export or substitution, not an architecture diagram |

Include a contextual attribute only when it changes the design or the evidence plan. Record which attributes were considered and found not applicable, so the decision is visible and can be reopened when the product, market or contract changes.
