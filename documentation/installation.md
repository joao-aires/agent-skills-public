# Install and update plugins

Build complete bundles, load them through your client's supported route, then inspect discovery in the application workspace. You need Git to clone this repository and Python 3.10+ with the validation dependencies installed. Building then uses committed resources without upstream access or Node.js. Client authentication is separate from building.

[Build](#build-the-bundles) · [Load in a client](#load-them-in-your-client) · [Additional bundles](#select-additional-bundles) · [Optional Figma connection](#optional-figma-connection)

## Build the bundles

With Git and Python 3.10+ available, run in a POSIX shell:

```bash
git clone https://github.com/joao-aires/agent-skills-public.git
cd agent-skills-public
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-validation.txt
python scripts/build_plugins.py --destination ./built-plugins
export AGENT_PLUGINS_DIR="$(pwd)/built-plugins"
```

If you already have a checkout, start there instead of cloning again. The builder uses committed upstream skills and their resources for the selected plugin (development by default), applying adaptations only in its output. It does not fetch upstream repositories. The destination must be new. [Additional bundles and rebuilds](#select-additional-bundles) use the same builder.

## Load them in your client

Open the application repository or an empty project workspace. The `claude-marketplace` distribution branch contains built bundles, a Claude Code catalog at `.claude-plugin/marketplace.json` and a Codex catalog at `.agents/plugins/marketplace.json`. They reference the same complete packages. The [publish workflow](../.github/workflows/publish-claude-marketplace.yml) runs the full validation workflow at the same revision before publishing from `main`; a failed validation prevents publication. Publications retain Git history so an existing clone can fast-forward, and remove files no longer present in the build. Forks publish under their own owner when their Actions configuration permits it.

The client routes below were checked against primary documentation. Catalog generation and resource closure are tested locally; installation, discovery and updates in each native client still need verification for your installed version. Marketplace publication is separate from listing in a public plugin directory.

### Claude Code

Add the published marketplace and install a bundle:

```bash
claude plugin marketplace add joao-aires/agent-skills-public#claude-marketplace
claude plugin install development@agent-skills-public
```

Choose `/development:develop` in a new session, or `/development:workflow-help` for help choosing an activity. Install additional bundles by qualified name, such as `strategy@agent-skills-public`.

Third-party marketplaces have automatic updates disabled by default. In `/plugin`, open Marketplaces, select this marketplace and enable auto-update if desired. To update manually:

```bash
claude plugin marketplace update agent-skills-public
claude plugin update development@agent-skills-public
```

Refreshing the marketplace catalog alone does not update installed plugins. Run `/reload-plugins` in the active session, or start a new session, after an update. See [Claude Code's installation and update guide](https://code.claude.com/docs/en/discover-plugins#keep-plugins-updated).

For a local build, from the application workspace in the terminal where `AGENT_PLUGINS_DIR` is set:

```bash
claude --plugin-dir "$AGENT_PLUGINS_DIR/development"
```

Repeat `--plugin-dir` for additional bundles. Pass each complete plugin directory, not its parent build directory. The [manifest reference](https://code.claude.com/docs/en/plugins-reference) documents standard `skills/` discovery without a Claude-specific manifest. This loads skills; it does not translate portable `mcp.json` into Claude's `.mcp.json` configuration.

### Codex and ChatGPT desktop

Codex has a separate marketplace catalog format, generated alongside the Claude catalog. Register the distribution source:

```bash
codex plugin marketplace add joao-aires/agent-skills-public --ref claude-marketplace
codex plugin marketplace list
```

In a supported client, open the Plugins Directory, choose Agent Skills Public and install development. Codex CLI also provides `/plugins`. Start a new chat/session and select `develop`. Supported ChatGPT desktop Work/Codex surfaces can use repo or personal marketplaces; registering a source does not publish it to the universal directory or your organization's managed catalog. Workspace-wide GitHub imports follow the administrator's separate setup.

Refresh the registered Git marketplace with:

```bash
codex plugin marketplace upgrade agent-skills-public
```

Then check the installed plugin in the client and start a new session. Source registration, marketplace refresh and activation in an existing session are different steps; do not assume a changed source is already loaded. Follow the [official OpenAI packaging and marketplace guide](https://developers.openai.com/plugins/build/plugins) and [supported plugin surfaces](https://learn.chatgpt.com/docs/plugins) for your client. The Codex IDE extension is not a plugin installation surface in that guide; use supported skill discovery or the host's documented plugin support instead.

For a local build, copy the complete bundle to a new directory in the application repository:

```bash
mkdir -p .local-agent-plugins
cp -R "$AGENT_PLUGINS_DIR/development" .local-agent-plugins/development
```

Add or merge the following into `.agents/plugins/marketplace.json`, preserving existing entries:

```json
{
  "name": "project-guidance",
  "interface": { "displayName": "Project guidance" },
  "plugins": [
    {
      "name": "development",
      "source": { "source": "local", "path": "./.local-agent-plugins/development" },
      "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" },
      "category": "Productivity"
    }
  ]
}
```

Paths are relative to the marketplace root, not `.agents/plugins/`. Restart the desktop app, install development from Project guidance and start a new chat. For local updates, replace only a preserved, deliberately managed bundle copy and restart as described in the official guide. Add entries for other chosen bundles. Raw source directories contain unadapted upstream snapshots; expose built packages instead.

### OpenCode

OpenCode skill sources are different from its executable JavaScript plugins. Keep the built bundles intact and load their skill directories.

For **OpenCode V2**, merge absolute directories into the `skills` array in `opencode.json` or `opencode.jsonc`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "skills": ["/absolute/path/built-plugins/development/skills"]
}
```

Start `opencode` in the application workspace, confirm discovery and request `@develop`. Replace the example path and add one source for each chosen bundle. Rebuild into a new destination when updating, repoint the configured sources and start a new session. The [V2 skill guide](https://opencode.ai/v2/docs/skills/) documents these sources and invocation controls.

For **V1**, use the locations and permissions in its [skill guide](https://docs.opencode.ai/docs/skills/), rather than V2 configuration. A skill-directory link in a supported source such as `.opencode/skills/<name>` can retain the complete built package at its original location, so relative resources remain available. Preserve existing entries and confirm how your installed version resolves links and invocation controls. Skill-source loading does not configure MCP endpoints.

### Pi coding agent

Pi can read skill directories without converting these bundles into executable extensions or Pi packages. Merge absolute paths into the `skills` array in the application repository's `.pi/settings.json`:

```json
{
  "skills": ["/absolute/path/built-plugins/development/skills"]
}
```

Start Pi in the application workspace, inspect startup diagnostics and explicitly invoke `/skill:develop`. Add directories for other chosen bundles. After rebuilding, update these paths and run `/reload`, then confirm discovery. Absolute paths avoid confusing project settings paths, which resolve from `.pi`. Keep the surrounding package and its resources intact. This route does not install MCP services or JavaScript extensions. See Pi's [skills](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md) and [resource settings](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/settings.md#resources).

### VS Code with GitHub Copilot

VS Code is the editor; the selected agent harness determines which customizations it loads. For Copilot's plugin support, merge this into your settings while preserving other marketplaces:

```json
{
  "chat.plugins.marketplaces": ["joao-aires/agent-skills-public#claude-marketplace"]
}
```

Open the Agent Customizations editor or search `@agentPlugins` in Extensions, then find and install development. Marketplace settings are experimental and may be controlled by your organization. VS Code uses the Claude-compatible catalog on this branch; it does not require the Codex catalog.

For local builds, register complete plugin directories instead:

```json
{
  "chat.pluginLocations": {
    "/absolute/path/built-plugins/development": true
  }
}
```

Check discovery in the selected harness. For updates, use Extensions: Check for Extension Updates, or the update operation in the interface where you installed the plugin. Do not assume separate plugin management interfaces share an inventory. The [VS Code plugin guide](https://code.visualstudio.com/docs/agent-customization/agent-plugins) covers marketplace refs, local directories and update behavior. For skill-only discovery, consult the [Agent Skills guide](https://code.visualstudio.com/docs/agent-customization/agent-skills); preserve package-relative resources rather than copying only `SKILL.md`. Other harnesses in VS Code follow their own client guidance.

### Other clients

For Copilot CLI, load a built package with `copilot --plugin-dir "$AGENT_PLUGINS_DIR/development"` and inspect available skills with the [CLI's plugin commands](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference).

For Antigravity CLI, the prior trial route was `agy plugin install "$AGENT_PLUGINS_DIR/development"`, followed by `agy plugin list --json`. Confirm these commands against the installed version before relying on them. Client authentication and discovery do not establish workflow adherence.

For any skill-only client, retain the complete built package and use supported directory sources or links. Copying a skill away from package-root framing can break relative references. Check explicit invocation controls rather than treating metadata as enforcement. Read [migration](migration.md) before replacing old installations.

## Select additional bundles

Explicit `--plugin` arguments replace the default selection; repeat development when you want it included. For a Python/React application with generic interface/service/delivery methods:

```bash
python scripts/build_plugins.py \
  --plugin development \
  --plugin frontend-development \
  --plugin backend-development \
  --plugin delivery \
  --plugin backend-python-development \
  --plugin frontend-reactjs-development \
  --destination ./built-python-react
```

Add strategy for product/business work, documentation or visualization for those capabilities, and operations for operating work. AI-development supplies generic AI methods without a provider framework; select ai-python-development, ai-adk-development or ai-langchain-development only for an accepted implementation. Tool and infrastructure expertise are explicit additions too. See the [plugin catalogue](../README.md#choose-your-plugins).

To inspect every package rather than choose an application stack:

```bash
python scripts/build_plugins.py --all --destination ./built-all-plugins
```

`--all` and `--plugin` are mutually exclusive. Every destination must be new; replace client installations only after preserving local changes. Load each chosen built plugin through the client examples above, repeating its supported flag, marketplace entry, skill-source path or install operation as appropriate. Source directories contain authored skills and raw acquired snapshots; builds apply the collection’s adaptations and add provenance notices. Application dependencies and live tools remain separate.

For structural verification of the default build:

```bash
python scripts/check_collection.py --built ./built-plugins --plugin development
```

For a selected multi-plugin build, repeat the checker's `--plugin` arguments to match it. With no checker selection, `--built` expects the full collection. These checks establish resources/inventory, not client discovery or agent adherence.

## Verify installation and update

The build should create one directory per selected plugin, containing its manifest, local and acquired skills, resources and source notices. Confirm that the client lists the bundles or skills you selected. If discovery is incomplete, check that you loaded built directories, used absolute paths where required and preserved the complete directory contents.

Discovery verifies availability. Actual execution and adherence need separate [behavior trials](maintainers/evaluations.md). Keep the old installation until its replacement builds and is discoverable; follow [migration](migration.md) for old copies or links. Never overwrite local changes without preserving them.

## Optional Figma connection

The frontend-development bundle declares Figma's optional remote endpoint in [mcp.json](../plugins/frontend-development/mcp.json). Follow [Figma's client setup](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/) when connecting it; avoid duplicate configuration if the official client plugin already supplies the connection. The declaration does not establish authenticated file access.

Connect only when the requested work needs Figma, and verify access to the intended file. The [usage guide](usage.md#optional-figma-connection) explains local design alternatives and Storybook's verification role.

After installation, [choose your first activity](usage.md#skills-you-invoke).
