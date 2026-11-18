# sdlc-mod: local SDLC engagement state

`sdlc-mod` keeps the current conversation's SDLC state visible while you move between requirements, design, implementation, testing and operations. It is a local, session-scoped working aid. It does not replace the ECR, persist project history or grant authority.

The state updates from two sources: explicit `/sdlc` commands, and a guarded inference pass after each completed turn. Inferred entries are marked `~`.

## What it tracks

- current focus thread;
- parallel threads with activity, software type, stopping point and status;
- open and accepted decisions;
- parked work;
- next transition;
- current read/write/publish/implement/deploy authority.

## Views

The compact view is one line under the prompt:

```text
SDLC · design:frontend · 2 threads · 1 open
```

### Sidebar and dialog (OpenCode)

The same state is drawn in a collapsible sidebar section:

```text
▼ SDLC 2 threads · 1 open
● T2 design:frontend
   → design accepted
◐ T1 backend:backend
○ T3 spike:cache              parked
Decisions
✓ D1 use the existing search table
◐ D2 error copy owner
Next
design → implementation
needs seam accepted
Authority
read repo · write —
publish no · implement no · deploy no
```

Click the header, or run the palette command `SDLC: Toggle sidebar section`, to collapse it. The section lives in the session sidebar, so it is only visible while the sidebar is open.

`/sdlc state` opens a large dialog with aligned columns:

```text
Engagement state  2 threads · 1 open
Threads
    ID Activity    Type         Status   Stopping point
● T2   design      frontend     current  design accepted
◐ T1   backend     backend      waiting  seam accepted
Decisions
✓ D1   accepted    use the existing search table   user
◐ D2   open        error copy owner                unowned
Next transition
design → implementation · needs seam accepted
Authority
read        repo
write       —
publish no · implement no · deploy no
Local to this session · not the ECR · Esc closes this view
```

### Markdown (Claude Code and tests)

The core also renders Markdown for hosts and tests:

```markdown
## Engagement state

Focus: T2 — design (frontend)

Threads:
- ● T2 — design — frontend — design accepted — current
- ◐ T1 — backend contract — backend — waiting on seam — waiting

Decisions:
- D1 — accepted — user — use the existing search table
- D2 — open — user — error copy owner

Next transition: design → implementation (needs seam accepted)

Authority: read=repo; write=none; publish=false; implement=false; deploy=false
```

## How it updates

Manual commands are exact and immediate:

```text
/sdlc focus T2
/sdlc decision add user "use the existing search table"
```

Automatic inference runs after a completed turn:

1. OpenCode emits `session.execution.succeeded`; Claude Code fires `turn.complete`.
2. The adapter waits briefly, then sends the current state and the last few messages to the session model.
3. The model returns a JSON patch in the same command vocabulary as `/sdlc`.
4. The patch is filtered before it is applied: unknown or duplicate items, unsupported operations, authority changes, decision resolutions and resets are rejected.
5. The state changes and the sidebar, status line and dialog update.

Rules enforced on inferred changes:

- only focus, thread add/status/park/resume, decision add and transition changes;
- decisions are added as `open`, never accepted or rejected;
- authority is never inferred;
- threads are deduplicated by activity and software type, decisions by statement;
- low-confidence patches are dropped;
- child sessions and extraction-generated turns do not re-trigger extraction.

Inferred entries carry `~` in the sidebar and dialog:

```text
Decisions
◐ ~D1 use the existing search table
Next
~ design → implementation
```

Turn inference off for the current server with `/sdlc auto off`, or set `"auto": false` in the plugin options. Manual commands keep working either way.

The inference call uses the session's model, so it inherits that model's cost and availability. Set `includeMessages` and `debounceMs` to trade context for cost; a failed or slow extraction never blocks the chat.

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
        "includeMessages": 8
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

Or add it to a local marketplace/plugin configuration. `/sdlc` is registered on session start, and the status line appears under the prompt.

## Commands

```text
/sdlc state
/sdlc focus T2
/sdlc thread add design frontend "design accepted"
/sdlc thread park T1 "waiting on seam"
/sdlc thread resume T1
/sdlc thread close T1
/sdlc decision add user "use the existing search table"
/sdlc decision resolve D1
/sdlc decision reopen D1
/sdlc transition design implementation "seam accepted"
/sdlc auto on|off
/sdlc reset
/sdlc help
```

`state` opens the large dialog in OpenCode and the Markdown view in Claude Code. Other commands update the local state, the status line and the sidebar.

The palette command `SDLC: Toggle sidebar section` collapses or expands the sidebar section without a mouse.

## Local-only boundary

- State is held in the OpenCode server process, keyed by session, and mirrored by the TUI over RPC. Claude Code keeps it in the mod process.
- It is discarded when the server or session ends.
- It is not written to the repository, `.sdlc/`, the ECR or a shared service.
- It is not synchronized between sessions or machines.
- It does not grant tool, merge, deploy or publication authority.
- The ECR remains the durable authority for accepted decisions and evidence.

If you need cross-session or cross-agent state, use the ECR engagement-state section or add a separate explicit export mechanism. This package deliberately does not do that.

## Structure

```text
sdlc-mod/
  core/state.js       schema, validation, reducer, Markdown rendering
  core/view.js        glyphs, summaries and authority labels
  core/commands.js    textual command parsing
  core/extract.js     inference prompt, parsing, guards and dedupe
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
