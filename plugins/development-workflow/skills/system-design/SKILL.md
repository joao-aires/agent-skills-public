---
name: system-design
description: Choose and evolve application architecture from product outcomes, existing
  system evidence and operating constraints. Use after product refinement for a new
  system or before planning a feature that changes service, data, client or integration
  boundaries; avoid architecture ceremony for small local edits.
user-invocable: false
metadata:
  scope: generic
  invocation: both
  role: support
---

# Design the system around the outcome

Use this phase after business/product refinement and before dependent implementation planning. Revisit it when a new feature changes boundaries, persistence, identity, integrations, deployment or important quality attributes. For a small change, a brief assessment of the affected contract can be sufficient. Preserve accepted architecture in existing projects.

Read the product context and repository evidence. Use [system-mapping](../system-mapping/SKILL.md) for the current system and [security-and-privacy-design](../security-and-privacy-design/SKILL.md) for authority and data flows. Distinguish the current architecture, proposed changes and unresolved assumptions. Ask about missing product/authority decisions; investigate technical facts and make reversible choices within scope.

## Make decisions the user can assess

Identify the useful journey, actors, data ownership, consumers and external dependencies. Establish constraints that affect the design: supported clients, offline behavior, synchronization, latency/concurrency, budget, deployment environment, recovery and team capabilities. Mark unmeasured demand and unknown platform support explicitly.

Compare plausible options against those constraints. Explain the recommendation, rejected alternatives, consequences and what evidence would reopen the choice. Start with the simplest system that meets the accepted outcome; add service splits, queues, shared caches or additional frameworks for a demonstrated responsibility. Use installed codebase-design for interfaces/test seams and domain-modeling for complex domain concepts. A named pattern or popular framework does not establish suitability.

Describe system context and important service/client responsibilities, deployment boundaries and the critical request/event sequence. Specify contracts, authority checks, persistence/transaction ownership, retries/idempotency, failure/cancellation, compatibility and configuration. Include test seams, diagnostic signals, artifact/release strategy and recovery. Use the relevant backend, frontend/native-client, AI and operations guidance when installed. Architecture diagrams or a flow explorer clarify a decision when requested or useful; a drawing alone is not a design.

For desktop/mobile distinguish native shell and client responsibilities from Python backend services. For AI separate model/runtime orchestration, AG-UI interaction transport, A2UI rendering and MCP/ACP integrations; verify actual SDK/protocol and harness capabilities before proposing reuse. Existing-session attachment, concurrent edits and voice interruption need explicit supported contracts.

## Verify consequential technical claims

For a critical dependency or integration, verify a coherent version, required capabilities, interoperability, operating limits and usage terms against current primary sources. Distinguish demonstrated support, vendor claims, proposed adapters and unavailable behavior. Test uncertain contract boundaries with a bounded authorized spike before committing dependent work. Examples, starter kits and protocol labels establish only the capabilities/terms they actually cover; verify the component and intended use separately.

Use supported interfaces and the named disposable target for capability checks, following [integration discovery boundaries](../../WORKFLOW.md#working-boundaries). A proposed adapter or demo cannot establish access to an existing runtime/session. Carry unresolved support into the alternatives comparison.

## Resolve consequential dependency constraints

Use the shared [consequential finding policy](../../WORKFLOW.md#resolve-consequential-findings) to decide when a finding requires the user and which work depends on it. Architecture evidence should connect actual licensing/distribution terms, security/privacy, reliability, cost and platform support to intended personal, internal or commercial use. Keep these checks proportionate to the critical dependency and changed boundary.

Where a fact or restriction changes an accepted constraint, present supported alternatives and the concrete decision. Continue independent work while dependent work waits. Preserve the required user capability when reopening architecture; a different technical solution can satisfy it without silently changing the product or accepting new terms/costs. Label evaluation spikes separately from production commitments.

## Carry the design into delivery

Keep the consequential decisions in the project's existing architecture note or ADRs, with links to evidence and acceptance. Carry them into the implementation plan, interactions, setup, tests and release process. Avoid duplicating the same architecture across documents. Validate uncertain choices with a bounded spike or contract test before committing dependent work; label prototype behavior and untested claims.

Return a recommended/proposed design, meaningful alternatives, material questions and a useful next increment. Design-only authority does not permit feature edits or deployment. Reassess the affected decision when new evidence arrives; do not force a complete redesign for each feature.

For substantive architecture explanations or current/target views, use [architecture documentation](../architecture-documentation/SKILL.md). System-design owns the design choices; architecture-documentation explains their structure, runtime, interface and evidence boundaries, without claiming a proposed design is implemented.
