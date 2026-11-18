# sdlc-mod: local SDLC engagement state

`sdlc-mod` keeps the current conversation's SDLC state visible while you move between requirements, design, implementation, testing and operations. It is a local, session-scoped working aid. It does not replace the ECR, persist project history or grant authority.

A thread is a unit of work with a short name and a current phase. It may carry a local id (`T1`), a tracker ticket (`PROJ-142`), a software type, a stopping point and artifact links. The state updates from explicit `/sdlc` commands and a guarded inference pass after each completed turn. Inferred entries are marked `~`.

## What it tracks

- current focus thread;
- parallel threads with name, phase, ticket, status, stopping point and artifacts;
- open and accepted decisions, optionally linked to a thread and artifacts;
- parked work.

It does not track a separate next transition or authority. A blocked decision or a thread status carries that information. Authority belongs with permissions and the ECR, not with a local cache the model can update.

## Views

The compact view is one line under the prompt:

```text
SDLC · pagination works · 3 threads · 1 open
```

### Sidebar and dialog (OpenCode)

```text
▼ SDLC 3 threads · 1 open
        T1      T2      T3
      PRJ-142 PRJ-151
✓ req     ✓       ✓       ✓
✓ des     ✓       ◐       ✓
▶ imp     ●       ·       ✓
○ tst     ·       ·       ✓
○ ops     ·       ·       ○
● T1 · PRJ-142 pagination works
  implementation · waiting
  ↗ api-contract.md
Decisions
◐ D1 Reuse the existing search table
```

The matrix shows phases as rows and thread codes as columns; the ticket sits under the code. Cells are `✓` done, `●` focus, `◐` waiting, `!` blocked, `○` parked, `·` not reached. The focus block below carries the work name, phase, status and artifacts. Up to three threads get columns; additional threads are counted below.

Click the header, or run the palette command `SDLC: Toggle sidebar section`, to collapse it. Collapse hides artifacts and decisions; the matrix and focus block stay. The section lives in the session sidebar, so it is only visible while the sidebar is open.

`/sdlc state` opens a large dialog with aligned columns:

```text
Engagement state  3 threads · 1 open
Threads
    ID             Work              Phase           Status   Stopping point
● ~T1 · PROJ-142   pagination works  implementation  waiting  pagination works
◐ T2 · PROJ-151    API contract      design          waiting  API contract
○ T3               cache spike       operations      parked   return after v1
Decisions
◐ ~D1  open  Reuse the existing search table  T1
Local to this session · not the ECR · Esc closes this view
```

### Markdown (Claude Code and tests)

The core renders Markdown for hosts and tests:

```markdown
## Engagement state

Focus: T1 — pagination works (implementation, backend)

Threads:
- ● T1 [PROJ-142] — pagination works — implementation (backend) — waiting — pagination works — api-contract.md
- ◐ T2 [PROJ-151] — API contract — design — waiting — API contract
- ○ T3 — cache spike — operations — parked

Decisions:
- D1 — open — user — Reuse the existing search table — T1
```

## How it updates

Manual commands are exact and immediate:

```text
/sdlc focus T1
/sdlc thread phase T1 testing
/sdlc decision add user "use the existing search table"
```

Automatic inference runs after a completed turn:

1. OpenCode emits `session.execution.succeeded`; Claude Code fires `turn.complete`.
2. OpenCode asks the free decision model (`opencode/jev-1.13-free`) whether anything changed, what kind of change it was, which phase is active and which thread should have focus. Claude Code skips this gate.
3. If the gate reports no change, the text pass is skipped.
4. Otherwise the adapter sends the current state, the last few messages and the gate hints to the session model.
5. The model returns a JSON patch in the same command vocabulary as `/sdlc`.
6. The patch is filtered before it is applied: unknown or duplicate items, unsupported operations, decision resolutions, thread closes and resets are rejected.
7. The state changes and the sidebar, status line and dialog update.

Rules enforced on inferred changes:

- only focus, thread add/status/phase/park/resume and decision add;
- a thread is deduplicated by work name; the phase is a property of the thread, not part of its identity;
- decisions are added as `open`, never accepted or rejected;
- authority is not part of this state and can never be inferred;
- tickets and artifacts are not inferred; add them explicitly;
- low-confidence patches are dropped;
- child sessions and extraction-generated turns do not re-trigger extraction.

Inferred entries carry `~` in the sidebar and dialog:

```text
Decisions
◐ ~D1 Reuse the existing search table
```

Turn inference off for the current server with `/sdlc auto off`, or set `"auto": false` in the plugin options. Manual commands keep working either way.

The gate is free and fast; the text pass uses the session's model only when the gate reports a change. Set `includeMessages`, `debounceMs`, `gateMessages` and `gateThreshold` to trade context and sensitivity for cost. If the decision model is unavailable, the adapter falls back to the text pass instead of dropping the update. A failed or slow extraction never blocks the chat.

## Install

### OpenCode

The package has a server part and a TUI part. Register the server part in `opencode.json` so inference and state live in the session server:

```json
{
  "plugins": [
    {
      "package": "/absolute/path/to/integrations/sdlc-mod",
      "options": {
        "auto": true,
        "debounceMs": 1500,
        "minConfidence": 0.7,
        "includeMessages": 8,
        "gate": true,
        "gateThreshold": 0.5,
        "gateMessages": 2,
        "decisionModel": "opencode/jev-1.13-free"
      }
    }
  ]
}
```

Register the TUI part in `cli.json`:

```json
{
  "plugins": ["/absolute/path/to/integrations/sdlc-mod"]
}
```

Reload OpenCode. The status line appears under the prompt, the SDLC section appears in the session sidebar, and `/sdlc` is available in the command palette. Manual commands and inference share the server-side state over RPC.

If only the TUI part is registered, the status line and dialog cannot reach the state store and `/sdlc` commands report an error.

### Claude Code

Load the directory as a plugin for one session:

```bash
claude --plugin-dir /absolute/path/to/integrations/sdlc-mod
```

Or add it to a local marketplace/plugin configuration. `/sdlc` is registered on session start, and the status line appears under the prompt. Claude Code has no decision-model gate; it runs the text pass after each completed turn.

## Commands

```text
/sdlc state
/sdlc focus T2
/sdlc thread add "pagination works" implementation backend "pagination works"
/sdlc thread phase T1 testing
/sdlc thread ticket T1 PROJ-142
/sdlc thread artifact T1 api-contract.md file:///path/to/api-contract.md
/sdlc thread block T1
/sdlc thread park T1 "waiting on seam"
/sdlc thread resume T1
/sdlc thread close T1
/sdlc decision add user "use the existing search table"
/sdlc decision thread D1 T1
/sdlc decision artifact D1 PROJ-151 https://linear.app/acme/issue/PROJ-151
/sdlc decision resolve D1
/sdlc decision reopen D1
/sdlc auto on|off
/sdlc reset
/sdlc help
```

`state` opens the large dialog in OpenCode and the Markdown view in Claude Code. Other commands update the local state, the status line and the sidebar.

The palette command `SDLC: Toggle details` collapses or expands artifacts and decisions without a mouse.

## Local-only boundary

- State is held in the OpenCode server process, keyed by session, and mirrored by the TUI over RPC. Claude Code keeps it in the mod process.
- It is discarded when the server or session ends.
- It is not written to the repository, `.sdlc/`, the ECR or a shared service.
- It is not synchronized between sessions or machines.
- It does not grant tool, merge, deploy or publication authority.
- Authority is not part of this state; permissions and the ECR remain the authority.
- The ECR remains the durable authority for accepted decisions and evidence.

If you need cross-session or cross-agent state, use the ECR engagement-state section or add a separate explicit export mechanism. This package deliberately does not do that.

## Structure

```text
sdlc-mod/
  core/state.js       schema, validation, reducer, Markdown rendering
  core/view.js        glyphs, summaries, thread codes
  core/commands.js    textual command parsing
  core/extract.js     inference prompt, parsing, guards and dedupe
  core/decision.js    decision gate questions and interpretation
  core/*.test.js      Node test suites
  src/rpc.ts          shared RPC schema
  src/server.ts       OpenCode server part: state, inference, RPC
  src/tui.tsx         OpenCode TUI part: status line, sidebar, dialog
  hooks/register.js   Claude Code mod adapter
  .claude-plugin/     Claude Code manifest
  hooks/hooks.json    Claude Code hooks module declaration
```

## Development

Core tests use only Node.js:

```bash
cd integrations/sdlc-mod
npm test
```

The host adapters import `@opencode/plugin` or run inside Claude Code; they are not exercised by the core test suite. Test them in an installed host session.

## Safety

- Treat inferred entries (`~`) as proposals, not facts; correct them with `/sdlc` commands.
- Turn inference off with `/sdlc auto off` or `"auto": false` when the extra model call is unwanted.
- Inference sends the recent transcript to the session model; do not enable it where that is unacceptable.
- Do not put secrets, credentials or customer data in state.
- Treat the status line as a reading aid, not proof of authority.
- The mod never approves a tool call, merge, release or deployment.
- A local state reset does not change the ECR or project history.
