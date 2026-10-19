# AI application patterns and architecture tradeoffs

Classify the user task and failure costs before choosing a runtime or protocol. These patterns overlap; choose only the responsibilities the product needs and preserve a simpler accepted architecture when it suffices.

| Application pattern | Design decisions | Useful boundaries and evidence |
| --- | --- | --- |
| Bounded classification, extraction, summarization or generation | Output contract, uncertainty/refusal, validation and human correction; compare deterministic rules and a direct model call | Typed application adapter, representative task outputs and harmful-error cases; an agent loop is not implied |
| Knowledge assistant or search/RAG | Corpus ownership/freshness, authorized retrieval, provenance, answerability and conflicting sources | Retrieval and grounding evaluated separately; MCP only when a shared external context/tool interface is useful |
| Interactive copilot or action assistant | Conversation state, task continuity, human control, tool authority and observable completion | Static application UI may suffice; AG-UI for shared interaction events, A2UI for justified generated surfaces, MCP for compatible reusable tools |
| Durable automation or long-running agent | Work ownership, retries/idempotency, approvals, checkpoints, deadlines and partial effects | Runtime/durable-workflow support, actual action outcomes and trajectory evidence; resume state without replaying committed side effects |
| Coding-agent client or session companion | Existing/new session requirements, workspace isolation, artifact ownership and permission delegation | Supported harness API or ACP capability intersection, real session resumption and tool effects; a transcript replay is a narrower fixture |
| Distributed agent service | Independent deployment, task ownership, identity and delegated authority | A2A when peers require interoperability; test task/artifact lifecycle and remote failures, not just local delegation |
| Voice, visual, spatial or other multimodal interaction | Modality-specific inputs, latency, interruption, grounding, accessibility and shared-state ownership | Real media/client/provider path and meaningful task outcomes; event playback or file processing cannot establish live interaction |

## Make consequential architecture tradeoffs explicit

- **Model call versus agent:** bounded inference is easier to predict, test and operate. A tool-using loop can handle variable work but adds state, cost, authority and termination concerns. Use an agent when the required behavior benefits from those choices.
- **Application-owned flow versus framework/harness:** direct control can keep domain boundaries clear; a runtime can supply useful orchestration, checkpoints and extensions. Check its real recovery, permission and operating semantics and the cost of replacing or adapting it.
- **One agent versus multiple:** divide work for a concrete expertise, ownership or parallelism benefit. Account for communication, inconsistent context, delegated authority, aggregate budgets and failure coordination. More actors do not establish better quality.
- **Retrieval versus larger context or training:** compare knowledge freshness, access control, provenance, latency, data rights and maintenance. Curate context before introducing a new store or pipeline. Training or fine-tuning requires representative licensed data and independent quality evidence; it does not replace authorization or current knowledge access.
- **Deterministic workflow versus durable agent state:** place irreversible business transitions in authoritative application code. Decide what can be safely retried, what must be checkpointed and how a human can intervene or recover. Conversation history alone is not an execution ledger.
- **Static UI versus generated UI:** a stable interface offers predictable interactions and accessibility. Generated surfaces can adapt to a task but require catalog governance, version-compatible rendering, bounded input and useful fallback. Keep product interaction and permission rules independent of model output.
- **Direct integration versus protocol:** a direct call can avoid compatibility and operating overhead. A protocol can improve reuse across real peers, at the cost of capability/version negotiation, transport/authentication and integration tests. Choose from the required boundary using [capability selection](capability-selection.md).
- **Managed versus self-hosted model/runtime:** compare quality, data handling, licensing, isolation, operational expertise, elasticity and total cost. A nominally cheaper call or open model is not a complete availability, privacy or cost assessment.

Keep unresolved consequential choices and their evidence in the project's existing design/decision record. Separate an option, accepted architecture, implementation and verified operating behavior. Use appropriate specialist expertise when available without making another package a prerequisite.
