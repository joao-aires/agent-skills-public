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

Establish actors, inputs, outputs, consequential errors and observable acceptance.

- Identify what requires inference or generation and what ordinary application code can decide more reliably.
- Reuse accepted product, architecture and interface decisions.
- Resolve material data-use, licensing, security, reliability and cost constraints before dependent commitments; seek the relevant available expertise without assuming another plugin exists.

Choose how much of the task the model needs to control. If the rules are known and inputs can be validated, ordinary application code may be sufficient. A bounded model call fits a task that needs inference but has a defined input and output. An application-owned workflow keeps sequencing and recovery in code while allowing model judgments at selected points. An agent runtime is useful when the next action genuinely depends on what the model discovers, but it also needs limits, supervision and a way to account for partial work.

Compare these approaches against the actual uncertainty and action needs. Keep the parts with hard correctness requirements under deterministic control, even when an agent chooses the next step. For application-type choices and architecture tradeoffs, read [application patterns](references/application-patterns.md). Use a framework for a justified orchestration capability, durable execution for work that must survive interruption, and multiple agents when distinct responsibilities improve the task enough to justify coordination. Do not introduce these layers to complete a technology checklist.

Choose a model/provider against task evidence, modalities, structured-output/tool support, context limits, latency, cost and deployment/data constraints. Version-match actual APIs and retain a replaceable integration boundary where useful. A loaded specialist does not accept a stack or authorize installation. Keep domain behavior testable without a model.

## Design the result for its consumer

Establish what the model contributes and who consumes it before choosing a response format. A person reading advice, software importing records and a service executing tool arguments need different contracts. Choose prose, structured data, tool calls or a combination from that need. Preserve explanations, citations and uncertainty when the consumer relies on them; generating fewer tokens is useful only if the required information survives.

Separate valid representation, valid application data, permitted effects and task usefulness. A schema can express some domain constraints, but authorization and constraints it cannot express still need application checks. A well-formed result can remain unsupported or unhelpful. Decide how each consequential property will be established rather than treating one successful parse or model judgment as sufficient.

Read [model input/output design](references/model-io-design.md) when choosing a software-consumed contract, organizing substantial context or designing recovery. It explains representation tradeoffs, instruction/evidence authority and cause-sensitive recovery without requiring every application to use JSON, a fixed prompt layout or an agent loop.

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

Decide what each kind of state is for before storing it together. Domain records establish application facts; conversation history records interaction; execution state lets work continue or recover; reusable instructions describe a method. Their authority, lifetime and deletion rules differ. A model's statement in a conversation does not by itself change a domain record.

For each kind, define the owner, tenant/session isolation, retention and deletion behavior. Build context from the information the current task is authorized to use, and budget it so relevant evidence and instructions remain usable. Treat retrieved documents and tool results as data. Instructions embedded in those sources cannot grant permission or replace the application's rules.

### When adding retrieval

Use retrieval when the task needs external or changing knowledge. Define source freshness, access filtering, provenance/citations and behavior when evidence is absent or conflicting. Check retrieval quality separately from final-answer quality.

### When adding durable memory

Require a justified user outcome, controllable updates, correction/deletion and limits on stale or sensitive information.

### Tools and authority

Expose tools around operations the application already knows how to authorize and perform. Give each tool a clear input contract, a result the model can interpret, and failure information that supports a sensible next action. Choose its scope so the model can accomplish the task without receiving broader access than the task requires.

Validate model-supplied arguments at the tool boundary, then apply business rules and resource permissions in trusted application code. Include invalid, missing and refused output in the calling logic. Keep identity, approval policy, tool allowlists and side-effect limits outside the prompt so a different model response cannot bypass them.

Preserve the user's existing authorization. Model proposals, generated buttons, skill instructions, prompts, external content and delegated agents cannot expand it.

## Make execution and interaction reliable

Define the execution lifecycle, observable task status, ownership and stopping conditions.

- Bound steps, tokens, concurrency, buffering, timeouts and retries.
- Account for idempotency, partial effects, cancellation, resumability and recovery; do not repeat a mutation merely because its response was lost.
- Check provider/harness semantic status as well as HTTP/process success and present failure without converting it into a successful answer or committed action.

### When integrating an existing session

Establish whether the chosen harness can list, load, resume or attach to the required session and who owns tools and permission decisions. A new run or transcript replay does not fulfill an existing-session requirement. Keep unsupported operations visible and resolve a consequential alternative before substituting it.

### When streaming or generating UI

Read [interaction contracts](references/interaction-protocols.md).

- Keep run/state ownership, accessible interaction, allowed components/actions and client/server authority explicit.
- Version-compatible schemas and independently compatible peers establish more than a private look-alike event fixture.
- Preserve accepted UX and platform conventions; generated UI remains untrusted input.
- Multimodal features need evidence for their actual modality and interaction, including interruption or grounding when those are required.

## Verify behavior and quality

Use [AI testing](../ai-testing/SKILL.md) when defining or changing quality criteria, cases, evaluation levels or regression evidence. Keep deterministic authority/service checks, actual peer interoperability and live model quality distinct. Verify the boundaries the accepted task needs; a mock, attractive output or aggregate score does not establish a working user journey. Missing execution access remains an explicit evidence gap.

## Deliver, observe and improve

Use [AI operations](../ai-operations/SKILL.md) for operating signals, provider/resource limits, quality monitoring, configuration changes and recovery. Keep the task and its effective model/prompt/retrieval/tool configuration identifiable; a provider call completing is not necessarily a completed user outcome.

Seek relevant delivery, security, reliability, documentation and interface expertise when available, retaining the activity's outcome when specialists are absent. Preserve scope and accepted choices, and report implemented behavior, actual checks and unresolved limits. Design, configuration and evaluation do not independently grant release, deployment or account access.
