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

Use [AI testing](../ai-testing/SKILL.md) when defining or changing quality criteria, cases, evaluation levels or regression evidence. Keep deterministic authority/service checks, actual peer interoperability and live model quality distinct. Verify the boundaries the accepted task needs; a mock, attractive output or aggregate score does not establish a working user journey. Missing execution access remains an explicit evidence gap.

## Deliver, observe and improve

Use [AI operations](../ai-operations/SKILL.md) for operating signals, provider/resource limits, quality monitoring, configuration changes and recovery. Keep the task and its effective model/prompt/retrieval/tool configuration identifiable; a provider call completing is not necessarily a completed user outcome.

Seek relevant delivery, security, reliability, documentation and interface expertise when available, retaining the activity's outcome when specialists are absent. Preserve scope and accepted choices, and report implemented behavior, actual checks and unresolved limits. Design, configuration and evaluation do not independently grant release, deployment or account access.
