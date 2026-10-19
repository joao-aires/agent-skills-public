# Install and update plugins

Build complete bundles, load them through your client's supported route, then inspect discovery in the application workspace. You need Git, Python 3.10+ and network access to acquire the pinned upstream resources. Client authentication is separate from building.

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

If you already have a checkout, start there instead of cloning again. The builder acquires pinned upstream skills and their resources for the selected plugin (development by default). The destination must be new. [Additional bundles and rebuilds](#select-additional-bundles) use the same builder.

## Load them in your client

Open the target application repository or an empty project workspace, rather than developing inside this skills repository.

The examples below follow current official client documentation; these routes have not been executed against the revised bundles here. Use the route for your installed client/version and confirm its skill inventory before starting work.

<details open>
<summary>Claude Code</summary>

From the application workspace, in the same terminal:

```bash
claude --plugin-dir "$AGENT_PLUGINS_DIR/development"
```

Then select `/development:develop`, or `/development:workflow-help` for help choosing an activity. Repeat `--plugin-dir` for additional bundles. Pass each complete plugin directory, rather than the parent build directory.

[Claude Code's local-plugin guide](https://code.claude.com/docs/en/plugins/create#develop-without-a-marketplace) documents this route. Its [manifest reference](https://code.claude.com/docs/en/plugins-reference) allows a directory without a Claude manifest: the standard `skills/` layout loads and the directory supplies the plugin name. This route loads skills; it does not translate the portable `mcp.json` into Claude's `.mcp.json` configuration.

</details>

<details>
<summary>Codex</summary>

Use a local marketplace to expose complete built packages. In the application repository, copy development to a new destination. If it already exists, follow the update guidance below instead of overlaying it:

```bash
mkdir -p .local-agent-plugins
cp -R "$AGENT_PLUGINS_DIR/development" .local-agent-plugins/development
```

Add this entry to `.agents/plugins/marketplace.json`, preserving any existing entries:

```json
{
  "name": "project-guidance",
  "interface": { "displayName": "Project guidance" },
  "plugins": [
    {
      "name": "development",
      "source": {
        "source": "local",
        "path": "./.local-agent-plugins/development"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

The source path is relative to the application repository root. In supported Codex desktop clients, restart the app, open the Plugins Directory and install development from Project guidance. Start a new chat, confirm discovery and select `develop` in the skill picker. Add entries only for the additional bundles you choose.

The [official OpenAI documentation](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually) describes the portable manifest and local marketplace route. CLI marketplace management and desktop installation differ; follow that guide for your client. A source checkout's `plugins/` directories omit acquired skills, so point the marketplace at complete built copies.

</details>

<details>
<summary>OpenCode V2</summary>

OpenCode discovers skill sources rather than loading these directories as native executable plugins. Keep the built bundle intact and merge its absolute skill-directory path into `opencode.json` or `opencode.jsonc` in the application repository:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "skills": ["/absolute/path/built-plugins/development/skills"]
}
```

Replace the example path with your build location. Add a skill-directory path for each chosen bundle, then start `opencode` in the application workspace. Confirm discovery and request `@develop` with your brief.

This example follows the [OpenCode V2 skills guide](https://opencode.ai/v2/docs/skills/), including its explicit-source configuration and `@skill-id` invocation. V1 uses different configuration and invocation conventions; use the documentation for your version rather than copying V2 syntax. Skill-source loading does not configure bundled MCP endpoints. Check invocation controls in the installed client; descriptive metadata alone cannot enforce them.

</details>

<details>
<summary>Copilot CLI</summary>

From the application workspace, in the same terminal:

```bash
copilot \
  --plugin-dir "$AGENT_PLUGINS_DIR/development"
```

Append `skill list --json` to inspect discovery without starting a model session. In another terminal, set `AGENT_PLUGINS_DIR` to the absolute build directory first. Session-local loading was checked with CLI 1.0.95; see the [CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) for your version.

</details>

<details>
<summary>Antigravity CLI (agy)</summary>

Install the complete built bundles, then inspect discovery:

```bash
agy plugin install "$AGENT_PLUGINS_DIR/development"
agy plugin list --json
```

An earlier bundle installation with 56 skills was checked with `agy` 1.3.5. Authenticate through the client's sign-in flow before model work. The [generation-trial specification](maintainers/evaluations.md#generation-trials) is harness-independent; `agy` is my local runner choice. The new package identities have not been installed into this client here; installation does not establish execution behavior.

</details>

For another client, use its documented plugin or skill-source loading route. Keep each plugin directory and its resources intact. Discovery establishes availability, not that an agent will follow every instruction. Updating an old installation? Read [migration](migration.md) first.

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

`--all` and `--plugin` are mutually exclusive. Every destination must be new; replace client installations only after preserving local changes. Load each chosen built plugin through the client examples above, repeating its supported flag, marketplace entry, skill-source path or install operation as appropriate. Source directories contain local skills only; built directories also contain pinned acquisitions and notices. Application dependencies and live tools remain separate.

For structural verification of the default build:

```bash
python scripts/check_collection.py --built ./built-plugins --plugin development
```

For a selected multi-plugin build, repeat the checker's `--plugin` arguments to match it. With no checker selection, `--built` expects all 17 packages. These checks establish resources/inventory, not client discovery or agent adherence.

## Verify installation and update

The build should create one directory per selected plugin, containing its manifest, local and acquired skills, resources and source notices. Confirm that the client lists the bundles or skills you selected. If discovery is incomplete, check that you loaded built directories, used absolute paths where required and preserved the complete directory contents.

Discovery verifies availability. Actual execution and adherence need separate [behavior trials](maintainers/evaluations.md). Keep the old installation until its replacement builds and is discoverable; follow [migration](migration.md) for old copies or links. Never overwrite local changes without preserving them.

## Optional Figma connection

The frontend-development bundle declares Figma's optional remote endpoint in [mcp.json](../plugins/frontend-development/mcp.json). Follow [Figma's client setup](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/) when connecting it; avoid duplicate configuration if the official client plugin already supplies the connection. The declaration does not establish authenticated file access.

Connect only when the requested work needs Figma, and verify access to the intended file. The [usage guide](usage.md#optional-figma-connection) explains local design alternatives and Storybook's verification role.

After installation, [choose your first activity](usage.md#skills-you-invoke).
