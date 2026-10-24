# Agent interaction and generated UI contracts

AG-UI connects an agent runtime with a user-facing client through events. A2UI describes generated surfaces, components, data and actions that a controlled renderer maps to application widgets. An application may use both, or keep a static interface. Neither replaces domain authorization, the chosen runtime, MCP tools or a harness's session-access contract. Use [capability selection](capability-selection.md) when that boundary is still undecided.

## Establish a compatible interaction contract

Select a compatible SDK, transport, backend adapter and renderer against the accepted protocol revision. Validate messages against published versioned contracts and exercise a compatible independent peer or conformance fixture. Application-owned schemas tested only against themselves do not establish interoperability. Private semantics use the selected protocol's extension mechanism and remain labelled as extensions. Seek matching available implementation expertise for actual APIs and message envelopes.

Define run/session identity, stream ordering, lifecycle, state ownership and cancellation. Bound buffering, resource usage and retries; reconcile reconnects and duplicate/stale events. Verify actual stream and rendered action round trips. Use representative deterministic events to check integration and distinguish them from live model-generated UI quality. Keep private internal reasoning and provider credentials out of client-visible events.

## Keep generated surfaces within application authority

Validate messages and catalogs before rendering: allowlisted component/action types, safe text/URLs and bindings, bounded structures and tenant/session-scoped data. Unknown, malformed or unsupported messages produce a controlled user-visible fallback. UI actions call deterministic authorized services; a generated form or button cannot grant write permission. Do not execute arbitrary model-provided scripts/HTML or turn catalog registration into unrestricted code execution.

The product still owns accessible interactions, understandable status/error language, accepted visual direction and appropriate confirmation. A renderer accepting a message does not establish that a person can complete the intended action. Verify important states and layouts through the actual client, including the resulting service state where persistence or side effects matter.

## Preserve shared state and human control

For collaborative or spatial products, establish stable object identity, versions, state ownership and scoped patches that preserve human edits. Validate proposals against current authorized state, distinguish preview/confirmation where required, preserve undo and define conflict behavior. Select cases from the concurrency and recovery model: simultaneous edits, interruption, stale proposals, changed attachments and reconnects.

Verify visible proposals and accept/reject/undo behavior through the actual client, and saved-state restoration after reload when the task requires it. Stored JSON or a message claiming that a proposal was staged proves only that narrower boundary. Generated surfaces can complement a shared editor; they do not implement its collaboration model automatically.

## Verify runtime and modality boundaries separately

Check actual session listing/loading/resumption and permission ownership in the selected harness when existing-session integration is required. A demo adapter or transcript replay remains a fixture and cannot establish attachment to a real session. Verify spatial grounding and reference ownership separately from a generated explanation.

For voice or other real-time modalities, verify the actual provider and client path, including latency, turn-taking and interruption where relevant. Uploaded-file processing, event playback and live interaction establish different outcomes; one must not inherit the others' evidence.

## Primary references

- [AG-UI overview](https://docs.ag-ui.com/introduction) and [AG-UI source](https://github.com/ag-ui-protocol/ag-ui).
- [A2UI specifications and version status](https://a2ui.org/) and [renderer implementation](https://a2ui.org/guides/renderer-development/).
- [Agent Client Protocol](https://agentclientprotocol.com/) for the separate harness integration contract.
