# Agent Plugins

Reusable portable plugins for business strategy, visual communication, and consistent application development. Work in progress.

Packages follow [Agent Plugins 1.0.0](https://agent-plugins.org/specification). Each standalone package has plugin.json, skills/, and optional mcp.json. Existing skill names and complete resources are preserved.

## Packages

| Plugin directory | Skills |
| --- | --- |
| plugins/business-strategy | business-strategy v2.2, business-opportunity-analysis compatibility |
| plugins/visual-communication | architecture-diagraming, presentation-building |
| plugins/development-workflow | project-bootstrap, maintain-documentation, maintain-agent-harness, test-end-to-end, deliver-reliable-changes, verify-delivery |
| plugins/python-backend | build-python-backend |
| plugins/web-frontend | build-consistent-frontend |
| plugins/ai-development | build-evaluated-ai |
| plugins/ai-adk / ai-langchain | Optional locked official AI framework skills |
| plugins/security-quality / mcp-development | Optional locked review/testing and MCP builder skills |

The [full-stack profile](profiles/full-stack.json) selects workflow, backend and frontend; AI, strategy and visuals are optional. Profiles are repository conventions, not standard dependency manifests.

## Use

Build packages with `python scripts/install_profile.py --destination /tmp/development-plugins`, then install the resulting plugin directories through your compatible client's documented flow. There is no universal plugin installation command in this standard. Load the three full-stack plugins together and add AI only when needed.

Create conventions in a new/empty project:

```bash
python3 plugins/development-workflow/skills/project-bootstrap/scripts/scaffold.py /path/to/new-project --ai adk --mcp
```

Omit --ai/--mcp for a normal application. This creates governance and documentation, not runnable application code. Fill the PRD, choose compatible dependencies, implement the first end-to-end slice and configure real verification commands.

Legacy skills-only fallback:

```bash
./scripts/sync-skills.sh sync
./scripts/sync-skills.sh status
./scripts/sync-skills.sh remove
```

The script discovers plugins/*/skills/*, repairs owned legacy links and preserves unrelated links. It does not install manifests/MCP. Old root skills/ paths moved to plugins/<package>/skills/<skill>/; update manually configured paths. The legacy business opportunity skill retains its fallback and sibling routing.

## Design and checks

- [Design and migration](documentation/plugin-design.md)
- [Holistic full-stack standard](documentation/full-stack-standard.md)
- [Official and community sources](documentation/upstream-sources.md)

```bash
python3 -m pip install -r requirements-validation.txt
python3 scripts/validate_plugins.py
python3 -m unittest discover -s tests -v
```

Validation covers official manifest schemas, skill metadata, package containment, profile references and scaffold regressions. Structural checks do not establish application correctness or semantic documentation freshness.

Selected upstream skill content is acquired into self-contained built packages. Sources absent from upstream.lock.json remain references. No MCP server is automatically launched; configure optional project integrations with the actual application path.

## Contributing

Keep skills concise and packages self-contained. Use references/templates/scripts for repeated work. Keep docs and evaluations aligned with behavior. Review/pin upstream content and preserve attribution before redistribution. MIT; upstream sources retain their licenses.

## Reproducible upstream packages

The profile builder acquires selected upstream skill directories at locked commits and packages their references and notices inside plugin boundaries. See [installation](documentation/installation.md), [workflow map](documentation/workflow-map.md), and `upstream.lock.json`. Earlier reference-only catalogue descriptions apply only to sources absent from that lock. No MCP runtime is automatically installed.
