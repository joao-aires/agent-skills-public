# Choose AI capabilities and integration boundaries

Start from the accepted task and the actual peers. Choose only mechanisms that solve a present boundary; a runtime, instruction package, tool protocol, interaction protocol and renderer have different responsibilities. Reuse a simpler accepted integration when it already meets the requirement.

## Skills and runtime responsibilities

An Agent Skill packages instructions and optional resources for a task. Use skills to make useful expertise discoverable and load details when applicable. Describe triggers and scope clearly, keep required resources available, and review executable helpers and source/licensing before distribution. A skill is not a remotely callable service, scheduler, permission grant or proof of tool availability. Plugins can distribute skills and integrations together without making every packaged capability mandatory.

Inspect the host's real discovery and invocation behavior. Metadata may aid selection but does not guarantee enforcement. Keep project instructions authoritative at their applicable scope, and avoid injecting every skill into every turn. Match needed expertise to available descriptions; missing optional guidance does not authorize installation or reduce required outcomes.

A harness is the runtime around an agent: model interaction, context management, tools, permissions and execution/session lifecycle. A framework supplies building blocks an application may use to implement those responsibilities. Compare supported capabilities, extension APIs, isolation, recoverability and operational fit rather than choosing by popularity or assuming all harnesses expose the same controls.

For a runtime integration, establish whether work starts a new run, resumes durable state or attaches to an existing session. Check actual version/configuration, permitted session discovery, tool/approval ownership, event flow, persistence, cancellation and failure semantics. Use documented APIs; ACP is a candidate only where both peers implement the required session operations. A private session store or desktop process is not automatically an attachment API. Unsupported access remains an integration limit, not permission to inspect unrelated accounts or substitute a replay.

## Protocol responsibilities

| Mechanism | Boundary and reason to use it | Compatibility to establish |
| --- | --- | --- |
| MCP | Discoverable tools, resources and prompts shared with compatible hosts | Protocol revision, peer capabilities, SDK/transport, identity, authorization and operational lifecycle |
| ACP | Communication between a coding-agent client and a compatible agent runtime | Supported session lifecycle, prompt/content forms, permissions, updates and optional capabilities |
| A2A | Task and message exchange between independent agent services | Discovery/capabilities, authentication, task/artifact lifecycle and supported transports |
| AG-UI | Agent/application interaction through typed events | Runtime adapter, client event semantics, state ownership, ordering and lifecycle |
| A2UI | Declarative generated surfaces rendered through an application-controlled catalog | Message revision, renderer/catalog compatibility, bindings, action handling and fallback |
| MCP Apps | Interactive app views exposed through an MCP integration | Host support, resource/tool contract, bridge, isolation and authorized UI actions |

For tool interfaces, compare a direct application function or existing service API before introducing MCP. Keep business authorization in the service; discovering a tool or accepting its schema does not authorize its effects. MCP-only implementation needs protocol and service checks, not an LLM evaluation. Define discovery/capabilities, typed contracts, transport and lifecycle before choosing an SDK. Verify denied/missing credentials, resource ownership, side effects, error semantics and transport/lifespan cleanup against the actual compatible client.

For UI integrations, separate the transport/event channel, generated surface description and actual interaction behavior. AG-UI and A2UI can work together; a static UI can use agent events without generated surfaces. MCP Apps is another host-mediated UI integration, with a distinct contract. Choose from the intended host/client experience and trust boundary, rather than adding all available protocols.

For distributed agents, use A2A when independently deployed peers need a shared task interface. In-process delegation or an application-owned workflow may suffice otherwise. Define identity, delegated authority, task ownership and failure recovery before introducing additional actors; a remote agent's reported completion still needs the application's outcome evidence.

## Establish real interoperability

Record the supported revision/capability intersection for each peer and verify through the published contract and an actual compatible peer or independent conformance fixture. Preserve compatible installed versions; changing them is a scoped migration. Use the protocol's extension mechanism for private semantics and label unsupported/mocked paths explicitly.

Exercise the boundary that matters: tool discovery and authorized effects, actual session resumption, independent task exchange, stream interruption/recovery or rendered action round trips. A schema defined and tested only by the application cannot establish external compatibility. Fixture handling and live model quality remain separate evidence.

## Primary references

- [Agent Skills specification](https://agentskills.io/specification) for instruction/resource packaging and progressive disclosure.
- [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture) and the [MCP Apps extension](https://apps.extensions.modelcontextprotocol.io/) for tool/context and interactive-view contracts.
- [Agent Client Protocol](https://agentclientprotocol.com/get-started/introduction) for compatible coding-agent clients and runtimes.
- [A2A specification](https://a2a-protocol.org/latest/) for independent agent services.
- [AG-UI overview](https://docs.ag-ui.com/introduction) and [A2UI specifications](https://a2ui.org/) for their separate interaction and rendering responsibilities.

Check versioned specifications and SDK/adapter documentation for implementation. These references do not establish that a particular harness or renderer supports a capability.
