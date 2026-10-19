# Agent interaction and generated UI contracts

AG-UI connects an agent runtime with a user-facing client through events. A2UI describes generated surfaces/components/data/actions that a controlled renderer maps to application widgets. An application may use both. Neither replaces domain authorization, the chosen agent framework, MCP tools or a harness's ACP session contract.

Select a compatible SDK, transport, backend adapter and renderer against the accepted protocol revision. Validate messages against the published versioned contracts and exercise a compatible independent renderer/conformance fixture. Application-owned schemas tested only against themselves do not establish interoperability. Private semantics must use the selected protocol's extension mechanism and remain labelled as extensions. Available technical specialists supply actual envelope/API examples.

Define run/session identity, stream ordering, lifecycle, state ownership and cancellation. Bound buffering, resource usage and retries; reconcile reconnects and duplicate/stale events. Test actual stream and rendered action round trips. Use small representative deterministic events to verify integration, and distinguish them from live model-generated UI quality. Do not display private internal reasoning or expose provider credentials in the client.

Validate messages and catalogs before rendering: allowlisted component/action types, safe text/URLs and bindings, bounded structures and tenant/session-scoped data. Unknown, malformed or unsupported messages produce a controlled user-visible fallback. UI actions call deterministic authorized services; an agent-generated form or button cannot grant write permission. Never execute arbitrary model-provided scripts/HTML or turn catalog registration into unrestricted code execution.

For collaborative canvases, use stable object IDs, versions and scoped patches that preserve human edits. Validate a proposal against the current authorized canvas state, distinguish preview/confirmation where the product requires it, preserve undo and define conflict behavior. Test simultaneous edits, interruption, stale patches, attachment removal and reconnect. Through the actual client, verify that saved snapshots restore after reload, session cards and proposed annotations visibly render, and accept/reject/undo preserve human shapes. Stored JSON or a chat message saying a proposal was staged cannot establish those outcomes. Generated surfaces can complement a spatial editor; they do not automatically implement its collaborative editing model.

Verify separately any voice provider, real-time interruption and ACP harness attachment. Check actual session listing/loading/resumption and permission ownership in the selected harness. A demo adapter or transcript replay must remain labelled as a fixture and cannot establish existing-session attachment, spatial grounding or live voice latency.

First-party references:

- [AG-UI overview](https://docs.ag-ui.com/introduction) and [AG-UI source](https://github.com/ag-ui-protocol/ag-ui).
- [A2UI specifications and version status](https://a2ui.org/) and [renderer implementation](https://a2ui.org/guides/renderer-development/).
- [Agent Client Protocol](https://agentclientprotocol.com/) for the separate harness integration contract.
