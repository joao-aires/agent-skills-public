# Installation and upstream acquisition

The source repository contains local policy skills and locked acquisition recipes. Build once to obtain self-contained packages: upstream repositories are cloned into a cache, selected complete skill directories are copied into plugin boundaries, and commit/tree identities are checked. No symlinks to the cache survive. Nothing is fetched by the package builder from floating branches or by a universal `skills add ...@latest` installer.

```bash
python -m pip install -r requirements-validation.txt
python scripts/install_profile.py --destination /tmp/my-development-plugins
# Choose exactly one AI framework when needed:
python scripts/install_profile.py --include ai-development --include ai-adk --destination /tmp/my-adk-plugins
# Additional opt-in packages: ai-langchain, security-quality, mcp-development,
# business-strategy, visual-communication.
```

Install each resulting directory using your client's documented local portable-plugin installation route. Destination is a distribution directory, not an automatically discovered universal client location. For a client supporting project `.agents/skills`, use:

```bash
python scripts/install_profile.py --skills-only --destination /path/to/project/.agents/skills
```

The destination must not exist. Build into a new directory when updating, review the diff, then replace your installation. This avoids overwriting unrelated user skills. `sync-skills.sh` remains the local-policy legacy symlink route; it does not acquire the upstream lock or install MCPs.

## Policy and licensing

Root/plugin MIT licenses apply to locally authored files. Every acquired skill has `UPSTREAM.json`, its complete references, and its applicable license notice; `UPSTREAM-NOTICES.json` lists each package's sources. The two acquired Vercel skills declare MIT in skill frontmatter rather than a repository license file; that declaration is preserved. Trail of Bits material retains CC-BY-SA-4.0. Built mixed packages identify `LicenseRef-Mixed`; review component licenses before redistributing. The builder preserves bytes and does not silently modify upstream guidance.

Load local contract skills first. Upstream provider examples do not change the Gemini test preference; upstream interviews/approval conventions do not override explicit user authorization; browser tooling does not replace committed E2E tests. Skills may request live documentation or runtime commands: pinned skill source is not a pinned application dependency. Lock project dependencies separately and review execution/network behavior. Some ADK instructions assume the ADK source tree: consult the locked source cache for internals, not nonexistent application paths. Do not claim optional cross-skill suggestions are installed unless listed in notices.

## MCP and runtime tools

No MCP server is automatically enabled by these packages. Skills, executable tools, and MCP servers are separate installations.

| Capability | Skill/package | Runtime setup |
| --- | --- | --- |
| Component discovery | shadcn in web-frontend | Optional official shadcn MCP; initialize in `applications/web` against its components.json; pin a reviewed shadcn release in project tooling |
| Browser exploration | playwright-cli in development-workflow | Install a reviewed Playwright CLI version/browser explicitly; normal CI runs committed Playwright Test suites |
| Browser MCP | Optional alternative | Configure official Playwright MCP in your client if required; avoid duplicate browser orchestrators |
| App tools | Local backend + optional mcp-development | Implement project-specific FastMCP server only when needed; configure its real URL/auth in client settings |
| AI tool integration | Optional ADK or LangChain | Explicit tool allowlist/auth/budget at application boundaries; credentials via environment/secret store |

Official setup: https://ui.shadcn.com/docs/mcp, https://github.com/microsoft/playwright-cli, https://github.com/microsoft/playwright-mcp, https://gofastmcp.com/. Runtime versions, endpoints and credentials are deliberately project-specific. The portable manifest does not invent dependency semantics or a universal client configuration.

Vercel web-design-guidelines remains reference-only: its selected source declares no license and dynamically fetches current guidelines. The locked React/composition skills supply redistributable frontend guidance; local UX policy supplies the consistent design contract. UI/UX Pro Max and existing private UI skills are not copied or installed by this public repository.
