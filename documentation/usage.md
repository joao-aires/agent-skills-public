# Using the plugins

Choose bundles from the [README](../README.md#choose-your-plugins), load them in your client and work in the target application repository. You can request a skill by name; the agent also selects task-relevant guidance. Start with the full-stack trio and add AI, operations, strategy or visual communication as needed.

## Build and load

The [quick start](../README.md#quick-start) installs build dependencies and packages the three full-stack bundles. To include AI, explicitly select all four:

```bash
python scripts/build_plugins.py \
  --plugin development-workflow \
  --plugin python-backend \
  --plugin web-frontend \
  --plugin ai-development \
  --destination ./built-plugins-with-ai
```

Explicit `--plugin` arguments replace the default selection. Other bundle names work the same way. Build destinations must be new; to update an installation, rebuild and replace it using your client's supported route.

| Directory | Contents |
| --- | --- |
| `plugins/<name>` | Local guidance and supporting resources |
| `built-plugins/<name>` | Local guidance plus complete pinned upstream skills and license/source notices |

Load individual plugin directories, keeping their resources and supporting files together. The builder verifies source pins and packages resources; it does not execute upstream scripts, install application dependencies or configure your client.

### Client setup and discovery checks

For **Copilot CLI**, session-local loading was tested with version 1.0.95. From the application workspace:

```bash
copilot \
  --plugin-dir /absolute/path/built-plugins/development-workflow \
  --plugin-dir /absolute/path/built-plugins/python-backend \
  --plugin-dir /absolute/path/built-plugins/web-frontend
```

Append `skill list --json` to check discovery without starting a model session. Direct `copilot plugin install` also worked, but that version warns it is deprecated, and a reinstall test dropped an unrelated inventory entry. Session-local loading avoids that persistent-installation route. Consult the [CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) for your version.

For **VS Code** versions supporting Agent Plugins, merge the individual paths into user settings:

```json
{
  "chat.plugins.enabled": true,
  "chat.pluginLocations": {
    "/absolute/path/built-plugins/development-workflow": true,
    "/absolute/path/built-plugins/python-backend": true,
    "/absolute/path/built-plugins/web-frontend": true
  }
}
```

Open the application workspace and check Configure Skills. This route follows [official documentation](https://code.visualstudio.com/docs/agent-customization/agent-plugins#use-local-plugins); it was not exercised here. For other clients, use their documented route. Discovery confirms availability, not model compliance.

## Skills you invoke

Use these to start a deliberate activity, following the user/agent distinction in Matt Pocock's skills. Plain-language requests work where the client supports them; exact slash-command syntax varies. No interview, spec or orchestration workflow is required for a routine change.

| Activity | Skill | Example request |
| --- | --- | --- |
| Start or reorganize a project | `project-conventions` | “Set up a booking app with our frontend/backend conventions. Build creating and reopening a booking first.” |
| Clarify requirements | `grill-me`, `grill-with-docs`, `to-questionnaire` | “Help me resolve the important unknowns in this feature before implementation.” |
| Write a plan | `to-spec` | “Write a concise plan with acceptance criteria and risks. This turn is plan-only.” |
| Implement agreed scope | `implement`, `implement-spec` | “Implement the behavior agreed here; no tickets. Verify ownership and persistence.” |
| Revisit architecture or process | `improve-codebase-architecture`, `retro` | “Review this application's architecture and propose focused improvements.” |
| Learn or hand off | `ask-matt`, `teach`, `wait-what`, `handoff` | “Explain this design decision” or “prepare a handoff of the current work.” |
| Configure an optional tracker workflow | `setup-matt-pocock-skills`, `triage`, `to-tickets` | “Configure our chosen tracker” or “turn this plan into tickets.” Only when requested. |

Tickets remain optional, including for `implement-spec`: the [workflow guide](../plugins/development-workflow/WORKFLOW.md#project-fit) makes the conversation or a Markdown spec valid scope. Setup is not a prerequisite for ordinary development.

## Skills agents use during your work

These guide work already requested. Agents select them when relevant; you can also name them explicitly if selection misses one. Availability does not authorize extra activities or publication.

| Work | Relevant skills | Example request |
| --- | --- | --- |
| Frontend | `frontend-conventions`, shadcn, Tailwind and Vercel expertise | “Follow this screenshot's navigation and density. Keep our brand/components; check mobile, keyboard and failure states.” |
| Backend / MCP | `backend-conventions`, modern-python, mcp-builder | “Add tenant-owned saved searches and restart-safe exports, preserving OIDC; verify transactions and recovery.” |
| AI / transcription | `build-evaluated-ai`, chosen ADK or LangChain skills | “Add Portuguese transcription; start with a direct adapter if sufficient. Verify model/data terms and separate fixtures from live evaluation.” |
| Testing / review | `test-end-to-end`, `deliver-reliable-changes`, `tdd`, `code-review` and relevant security specialists | “Verify this journey against real persistence and review the change against agreed behavior.” |
| Debugging / research | `diagnosing-bugs`, `research`, `prototype`, `codebase-design` | “Reproduce disappearing searches, trace the cause and add a regression check.” |
| Git / pull requests | `contribute-code`, upstream `pr` | “Develop this feature in a worktree, use Conventional Commits, and open a concise PR in this repository. Do not merge.” |
| Docs / foundations | `maintain-documentation`, focused `project-conventions` upkeep, `writing-for-agents` | “Add a worker and update only affected startup commands, scoped instructions and documentation.” |
| Delivery / security | `build-delivery-pipelines`, `design-secure-features` | “Review promotion, rollback, migration compatibility and changed authority boundaries; do not deploy.” |
| Recovery / capacity / cost | `protect-and-restore-data`, `plan-application-capacity`, `optimize-application-cost` | “Review restore verification and estimate capacity/EUR costs in our actual region. Separate measurements from assumptions.” |
| Product / business | `learn-from-product-feedback`, `business-strategy`, `business-opportunity-analysis` | “Assess this idea or these anonymized support notes; identify evidence, uncertainty and the next useful decision.” |
| Visual communication | `architecture-diagraming`, `presentation-building` | “Explain the implemented system visually, marking planned components.” |

The local strategy/visual skills can also start a standalone activity when requested. This grouping describes intended usage, not a portable runtime access control. Upstream invocation metadata remains intact.

For new projects, the conventions prefer `applications/` for implementation and `documentation/` for knowledge, with concise scoped `AGENTS.md` instructions. Existing layouts and accepted choices are preserved. References can be screenshots, URLs, repositories, schemas or architecture notes; only relevant decisions need recording.

## Optional tools and verification

MCP servers provide live tools: shadcn registries, browser automation or the application's standalone FastMCP interface. Configure them only for the actual client and application. A Playwright skill does not install Playwright MCP, and browser tests can use the project's normal runner. No MCP servers or hooks are enabled by these bundles.

Ask for the checks actually performed and their boundaries: rendered UI, real persistence, ownership denial, mocked providers and separate live AI quality evidence as applicable. Package checks do not prove application quality. Detailed coverage and pending operations workflows are in the [SDLC map](sdlc.md).

For legacy skill-only links or renamed skills, use the [migration guide](migration.md).
