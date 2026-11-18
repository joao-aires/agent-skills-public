# sdlc-mod: local SDLC engagement state

`sdlc-mod` keeps the current conversation's SDLC state visible while you move between requirements, design, implementation, testing and operations. It is a local, session-scoped working aid. It does not replace the ECR, persist project history or grant authority.

## What it tracks

- current focus thread;
- parallel threads with activity, software type, stopping point and status;
- open and accepted decisions;
- parked work;
- next transition;
- current read/write/publish/implement/deploy authority.

The compact view is one line:

```text
SDLC · design:frontend · 2 threads · 1 open
```

The full view is Markdown for the current conversation:

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

## Install

### OpenCode

This is a TUI-only plugin. Add the package to `cli.json`:

```json
{
  "plugins": ["/absolute/path/to/integrations/sdlc-mod"]
}
```

Reload the TUI. The status line appears under the prompt, and `/sdlc` is available in the command palette.

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
/sdlc reset
/sdlc help
```

`state` shows the Markdown view. Other commands update the local state and the status line.

## Local-only boundary

- State is held in OpenCode TUI memory or in the Claude Code mod process.
- It is discarded when the session/TUI ends.
- It is not written to the repository, `.sdlc/`, the ECR or a shared service.
- It is not synchronized between sessions or machines.
- It does not grant tool, merge, deploy or publication authority.
- The ECR remains the durable authority for accepted decisions and evidence.

If you need cross-session or cross-agent state, use the ECR engagement-state section or add a separate explicit export mechanism. This package deliberately does not do that.

## Structure

```text
sdlc-mod/
  core/state.js       schema, validation, reducer, rendering
  core/commands.js    textual command parsing
  core/state.test.js  Node test suite
  src/tui.tsx         OpenCode TUI adapter
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

- Do not put secrets, credentials or customer data in state.
- Treat the status line as a reading aid, not proof of authority.
- The mod never approves a tool call, merge, release or deployment.
- A local state reset does not change the ECR or project history.
