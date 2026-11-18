# sdlc-mod: local SDLC engagement state

`sdlc-mod` keeps the current conversation's SDLC state visible while you move between requirements, design, implementation, testing and operations. It is a local, session-scoped working aid. It does not replace the ECR, persist project history or grant authority.

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

## Install

### OpenCode

This is a TUI-only plugin. Add the package to `cli.json`:

```json
{
  "plugins": ["/absolute/path/to/integrations/sdlc-mod"]
}
```

Reload the TUI. The status line appears under the prompt, the SDLC section appears in the session sidebar, and `/sdlc` is available in the command palette.

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

`state` opens the large dialog in OpenCode and the Markdown view in Claude Code. Other commands update the local state, the status line and the sidebar.

The palette command `SDLC: Toggle sidebar section` collapses or expands the sidebar section without a mouse.

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
  core/state.js       schema, validation, reducer, Markdown rendering
  core/view.js        glyphs, summaries and authority labels
  core/commands.js    textual command parsing
  core/*.test.js      Node test suites
  src/tui.tsx         OpenCode TUI adapter: status line, sidebar, dialog
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
