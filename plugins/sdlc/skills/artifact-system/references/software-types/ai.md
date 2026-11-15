# AI

## What this is

An AI-backed application, agent or model feature: a system whose useful behavior depends on model output, retrieval, tools or an evaluation loop. It may have a UI or a service boundary of its own, but its design evidence is the quality and failure behavior of the AI behavior, not only the surrounding interface.

## Design record must show

- the task and the quality or acceptance bar;
- context and data: sources, retrieval, freshness, permissions and retention;
- model and provider choice, with the reason and the fallback;
- tools, harness, protocols and the authority each tool has;
- the output contract consumed by the UI, service or downstream system;
- evaluation plan: cases, graders, baseline, regression and human review;
- failure behavior: refusal, hallucination, stale context, timeout, rate limit and provider outage;
- cost and latency limits;
- human control: review, correction, escalation and audit;
- a representation that lets a reviewer judge the behavior.

## Representation set

Use the available AI testing method for the evaluation plan: cases, graders, baselines and failure behavior. Typical representations also include context/retrieval/tool flow, a data contract for inputs and stored context, a harness or agent-loop view, a prompt/version and model/provider matrix, and a sequence for a tool call or failure path.

## Seam decisions

When an AI component meets a frontend, backend or external system, decide once:

- output shape and streaming behavior;
- error, refusal, timeout and rate-limit semantics;
- tool authority and permission boundaries;
- fallback and human-review behavior;
- citations, provenance and freshness expectations;
- cost/latency budget the consumer can rely on.

## Variants and constraints

| Variant | Constraint owner |
| --- | --- |
| Provider-independent AI application | `ai-development` — patterns, protocols, harnesses |
| Python provider/FastMCP integration | `ai-python-development` — provider and MCP APIs |
| Google ADK agent | `ai-adk-development` — agent architecture and implementation |
| LangChain/LangGraph | `ai-langchain-development` — graph, persistence and dependencies |
| Evaluation-backed feature | `ai-development` and `ai-testing` — cases, graders, regression |
| AI operations | `ai-operations` — quality signals, drift, cost, recovery |

These are constraints on the AI baseline, not separate software types.

## Verification that counts

- evaluation set run at a named revision, with baseline and result;
- regression and failure cases observed, not assumed;
- cost and latency measured where claimed;
- provider/framework behavior checked against primary sources;
- human-review or escalation path exercised where the design relies on it;
- a local probe distinguished from production behavior.

## Optional specialists

`ai-development`, `ai-testing`, `ai-operations`, `ai-python-development`, `ai-adk-development`, `ai-langchain-development`, plus security/privacy and backend expertise when authority or data boundaries change. If absent, retain the task, evaluation, failure and human-control reasoning.

## Not required

UI screens unless a frontend component is also affected; a service contract unless a backend boundary is also affected; C4 views when the AI behavior can be judged from a context/tool flow and evaluation plan.

## Example

A retrieval-backed assistant:

```markdown
- Affected type: ai
- Task: answer policy questions with cited sources
- Context: workspace documents, permission-filtered retrieval
- Output: answer plus citations; refusal when evidence is insufficient
- Evaluation: 40 cases, citation correctness and refusal behavior
- Failure: provider timeout, empty retrieval, stale document
- Representation: retrieval/tool flow plus evaluation matrix
- Frontend: designed separately; seam is the answer/citation contract
```
