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

<details>
<summary>VS Code</summary>

For versions supporting Agent Plugins, merge the individual absolute paths into user settings:

```json
{
  "chat.plugins.enabled": true,
  "chat.pluginLocations": {
    "/absolute/path/built-plugins/development": true
  }
}
```

Open the application workspace and inspect Configure Skills. This route follows [VS Code documentation](https://code.visualstudio.com/docs/agent-customization/agent-plugins#use-local-plugins); it has not been exercised here.

</details>

For another client, use its documented plugin-loading route. Keep each plugin directory and its resources intact. Discovery establishes availability, not that an agent will follow every instruction. Updating an old installation? Read [migration](migration.md) first.

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

`--all` and `--plugin` are mutually exclusive. Every destination must be new; replace client installations only after preserving local changes. Load each chosen built plugin through the client examples above, repeating its supported flag/settings/install operation as appropriate. Source directories contain local skills only; built directories also contain pinned acquisitions and notices. Application dependencies and live tools remain separate.

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
