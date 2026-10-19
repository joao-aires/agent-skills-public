---
name: ai-development
description: Design, build and operate AI-enabled applications and agent integrations independently of a provider. Use for model/tool workflows, context and retrieval, skills, harnesses, MCP, agent interaction or generated UI, and their evaluation and delivery; apply technical guidance only to the accepted stack.
metadata:
  scope: generic
  invocation: both
  role: support
user-invocable: false
---

# Develop AI applications and integrations

Start from the user outcome, operating constraints and existing system. Choose the smallest combination of models, deterministic services, agent capabilities and interfaces that can meet it. This method supports focused design, implementation, review and operating work; it does not start a full application lifecycle or authorize live actions on its own. MCP-only and skill-authoring work need no model or agent framework merely to use this guidance.

## Define the task and system boundary

Establish actors, inputs, outputs, consequential errors and observable acceptance. Identify what requires inference or generation and what ordinary application code can decide more reliably. Reuse accepted product, architecture and interface decisions. Resolve material data-use, licensing, security, reliability and cost constraints before dependent commitments; seek the relevant available expertise without assuming another plugin exists.

Compare a deterministic solution, a bounded model call, an application-owned workflow and an agent runtime against the actual uncertainty and action needs. For application-type choices and architecture tradeoffs, read [application patterns](references/application-patterns.md). Use a framework for a justified orchestration capability, durable execution for work that must survive interruption, and multiple agents when distinct responsibilities improve the task enough to justify coordination. Do not introduce these layers to complete a technology checklist.

Choose a model/provider against task evidence, modalities, structured-output/tool support, context limits, latency, cost and deployment/data constraints. Version-match actual APIs and retain a replaceable integration boundary where useful. A loaded specialist does not accept a stack or authorize installation. Keep domain behavior testable without a model.

## Compose the required capabilities

Choose each mechanism for the boundary it serves:

| Need | Candidate and decision |
| --- | --- |
| Task-specific reusable instructions and resources | Agent skills; check discovery, applicability, context loading and the host's invocation controls |
| A reusable external tool/context interface | MCP; compare with direct functions or an existing API before adding a protocol boundary |
| A runtime to execute agent work | A harness or framework; verify state, tool execution, permissions, cancellation and recovery in that actual runtime |
| A client controlling a coding-agent session | A supported harness API or Agent Client Protocol (ACP), when both peers implement the required operations |
| Independently hosted agents exchanging tasks | Agent-to-Agent (A2A), when remote agent interoperability is a requirement |
| Typed interaction between an agent and application UI | AG-UI for relevant run/message/state/tool interaction events |
| Generated interface structure using controlled application widgets | A2UI with a compatible renderer and approved component/action catalog |
| An interactive view carried by an MCP integration | MCP Apps, when the intended host supports the extension and its UI/security model |

These mechanisms can compose, but none implies that the others are needed. Read [capability and protocol selection](references/capability-selection.md) when selecting or changing these boundaries, implementing a skill/tool integration or attaching to a harness. Verify actual peer support, discovery, negotiated capabilities and the chosen revision rather than inferring interoperability from a product name or similar event fields. Select matching technical specialists for SDK/adapter implementation when available; otherwise use project evidence and appropriate primary documentation.

## Design context, state and tools

Separate durable user/domain state, conversation history, temporary execution state and reusable instructions. Define ownership, tenant/session isolation, retention and deletion for each. Give the model only authorized, relevant context within a deliberate budget; retrieved documents and tool results are data, not new authority.

Add retrieval when the task needs external or changing knowledge. Define source freshness, access filtering, provenance/citations and behavior when evidence is absent or conflicting. Check retrieval quality separately from final-answer quality. Add durable memory only for a justified user outcome, with controllable updates, correction/deletion and limits on stale or sensitive information.

Expose narrow typed tools over authorized services. Validate schemas and business invariants, including invalid, missing or refused model output. Enforce identity, resource authorization, approval policy, tool allowlists and side-effect limits in deterministic code. Preserve the user's existing authorization; a model proposal or generated button cannot grant permission. Skill instructions, prompts, external content and delegated agents cannot expand that authority.

## Make execution and interaction reliable

Define the execution lifecycle, observable task status, ownership and stopping conditions. Bound steps, tokens, concurrency, buffering, timeouts and retries. Account for idempotency, partial effects, cancellation, resumability and recovery; do not repeat a mutation merely because its response was lost. Check provider/harness semantic status as well as HTTP/process success and present failure without converting it into a successful answer or committed action.

For existing-session work, establish whether the chosen harness can list, load, resume or attach to the required session and who owns tools and permission decisions. A new run or transcript replay does not fulfill an existing-session requirement. Keep unsupported operations visible and resolve a consequential alternative before substituting it.

For streaming or generated UI, read [interaction contracts](references/interaction-protocols.md). Keep run/state ownership, accessible interaction, allowed components/actions and client/server authority explicit. Version-compatible schemas and independently compatible peers establish more than a private look-alike event fixture. Preserve accepted UX and platform conventions; generated UI remains untrusted input. Multimodal features need evidence for their actual modality and interaction, including interruption or grounding when those are required.

## Verify behavior and quality

Define useful acceptance criteria and a representative case set before comparing candidates. Keep deterministic checks for contracts, authority, isolation, failures, tool effects and recovery separate from live model quality. Protocol conformance, skill discovery and harness/session interoperability are separate boundaries again; exercise the relevant real peer and rendered user journey when available.

Use [evaluation methods](references/evaluation-references.md) when defining or changing AI behavior: assess components, complete tasks, trajectories, conversations, protocol integrations and user journeys at the relevant levels rather than treating one score as system validation. Preserve versioned datasets, prompts, rubrics and per-case evidence; include relevant ambiguity, adversarial conditions and provider failure. Use provisional thresholds explicitly when none are agreed. Keep holdouts where useful, report sample size/variability and calibrate subjective model judging against accepted human examples. Do not weaken acceptance or hide failed authority/task constraints behind an aggregate score. A mock proves only its simulated boundary; missing provider access leaves live quality unverified.

## Deliver, observe and improve

Keep model, prompt, retrieval, tool, skill and protocol configuration revisions identifiable with the application and evaluation evidence. Define deployment compatibility, rollback/recovery and handling of changed provider behavior. Protect secrets and sensitive content in telemetry; observe logical task/tool outcomes, latency, usage/cost, failures and relevant quality signals rather than treating a successful model call as a completed user outcome.

Use relevant delivery, security, reliability, documentation and interface expertise when available, retaining the activity's outcome when specialists are absent. Run appropriate deterministic checks after meaningful changes and authorized live comparisons when relevant. Turn observed failures and user feedback into privacy-preserving regression cases and scoped improvements. Report implemented behavior, actual checks, live versus fixture evidence and unresolved limits; setup, configuration or attractive samples do not establish a working production integration.
