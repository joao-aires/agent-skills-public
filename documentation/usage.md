# Using the plugins

Choose bundles from the [README](../README.md#choose-your-plugins), load them in your client and open the application repository. Ask for a skill by name or let the agent select guidance for the task. Start with the full-stack trio; add AI, operations, strategy or visual communication when needed.

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

Load each plugin directory with its resources and supporting files intact. The builder checks source pins and copies the resources. Application dependencies and client setup are separate; packaging does not execute upstream scripts.

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

Request these skills to start a distinct activity, following Matt Pocock's user/agent distinction. Use plain language where the client supports it; slash-command syntax varies. Routine changes can go straight to implementation.

| Activity | Skill | Example request |
| --- | --- | --- |
| Start or reorganize a project | `project-conventions` | "Set up a booking app with my frontend/backend conventions. Build creating and reopening a booking first." |
| Clarify requirements | `grill-me`, `grill-with-docs`, `to-questionnaire` | "Help me resolve the important unknowns in this feature before implementation." |
| Write a plan | `to-spec` | "Write a concise plan with acceptance criteria and risks. This turn is plan-only." |
| Implement agreed scope | `implement`, `implement-spec` | "Implement the behavior agreed here; no tickets. Verify ownership and persistence." |
| Revisit architecture or process | `improve-codebase-architecture`, `retro` | "Review this application's architecture and propose focused improvements." |
| Learn or hand off | `ask-matt`, `teach`, `wait-what`, `handoff` | "Explain this design decision" or "prepare a handoff of the current work." |
| Configure an optional tracker workflow | `setup-matt-pocock-skills`, `triage`, `to-tickets` | "Configure my chosen tracker" or "turn this plan into tickets." Only when requested. |

Tickets remain optional, including for `implement-spec`: the [workflow guide](../plugins/development-workflow/WORKFLOW.md#project-fit) makes the conversation or a Markdown spec valid scope. Setup is not a prerequisite for ordinary development.

## Skills agents use during your work

Agents use these skills to carry out your request. You can also ask for one by name. Installing a skill gives no permission to publish or start unrelated work.

| Work | Relevant skills | Example request |
| --- | --- | --- |
| Frontend | `frontend-conventions`, shadcn, Tailwind and Vercel expertise | "Follow this screenshot's navigation and density. Keep my brand/components; check mobile, keyboard and failure states." |
| Backend / MCP | `backend-conventions`, modern-python, mcp-builder | "Add tenant-owned saved searches and restart-safe exports, preserving OIDC; verify transactions and recovery." |
| AI / transcription | `build-evaluated-ai`, chosen ADK or LangChain skills | "Add Portuguese transcription; start with a direct adapter if sufficient. Verify model/data terms and separate fixtures from live evaluation." |
| Testing / review | `test-end-to-end`, `deliver-reliable-changes`, `tdd`, `code-review` and relevant security specialists | "Verify this journey against real persistence and review the change against agreed behavior." |
| Debugging / research | `diagnosing-bugs`, `research`, `prototype`, `codebase-design` | "Reproduce disappearing searches, trace the cause and add a regression check." |
| Git / pull requests | `contribute-code`, upstream `pr` | "Develop this feature in a worktree, use Conventional Commits, and open a concise PR in this repository. Do not merge." |
| Docs / foundations | `maintain-documentation`, focused `project-conventions` upkeep, `writing-for-agents`, `humanizer` | "Add a worker and update only affected startup commands, scoped instructions and documentation." |
| Delivery / security | `build-delivery-pipelines`, `design-secure-features` | "Review promotion, rollback, migration compatibility and changed authority boundaries; do not deploy." |
| Recovery / capacity / cost | `protect-and-restore-data`, `plan-application-capacity`, `optimize-application-cost` | "Review restore verification and estimate capacity/EUR costs in my actual region. Separate measurements from assumptions." |
| Product / business | `learn-from-product-feedback`, `business-strategy`, `business-opportunity-analysis` | "Assess this idea or these anonymized support notes; identify evidence, uncertainty and the next useful decision." |
| Visual communication | `architecture-diagraming`, `presentation-building` | "Explain the implemented system visually, marking planned components." |

You can also request strategy or visual work as a standalone activity. These groups describe how to use the skills; enforcement depends on the client. Upstream invocation metadata remains intact.

Use `humanizer` when drafting or editing prose in any phase. Keep the author's voice and preserve facts, code, metadata and link targets. Example: "Use humanizer to edit this PR description without changing its technical claims."

For new projects, I prefer `applications/` for implementation and `documentation/` for knowledge, with short scoped `AGENTS.md` instructions. Keep existing layouts and accepted choices. Screenshots, URLs, repositories, schemas and architecture notes can supply references; record the decisions that affect the project.

## Optional tools and verification

MCP servers provide live tools: shadcn registries, browser automation or the application's standalone FastMCP interface. Configure them only for the actual client and application. A Playwright skill does not install Playwright MCP, and browser tests can use the project's normal runner. No MCP servers or hooks are enabled by these bundles.

Ask which checks ran and what they cover: rendered UI, real persistence, ownership denial, mocked providers and live AI quality, as applicable. Package validation alone says nothing about the application's quality. Detailed coverage and pending operations workflows are in the [SDLC map](sdlc.md).

For legacy skill-only links or renamed skills, use the [migration guide](migration.md).
