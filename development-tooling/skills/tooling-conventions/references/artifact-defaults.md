# Artifact and delivery defaults

For my new GitHub-hosted projects, use GitHub Actions for CI/release and GHCR for container images. Preserve accepted providers in existing projects. Author usable workflows beside the application build/start/test commands and validate their actual behavior. Publication and deployment remain separate authorized actions.

| Artifact | Default destination | Required local/release checks |
| --- | --- | --- |
| API/web/worker container | GHCR | Locked build inputs, .dockerignore, minimal non-root runtime, startup/readiness, immutable digest/version and source provenance |
| Distributable Python library/tool | PyPI | Wheel/sdist build, metadata validation and clean-environment install/behavior tests; supported Trusted Publishing for release |
| Distributable JS/TS package | npm | Package-content review, types/export contracts, clean install and supported provenance/trusted publishing |
| Rust crate or another ecosystem package | crates.io or the ecosystem's established registry | Resolve actual package identity, supported registry/auth flow and package-specific tests |
| Tauri installer or mobile binary | Platform artifacts; release download/update channel or app store when agreed | Native build, signing/notarization/provisioning prerequisites, identity/version, install/upgrade and recovery tests |

PyPI is a registry; pip is an installer. A Python service need not be publicly distributed merely because its source is packaged. Default registries do not establish a namespace, package ownership, visibility or publication permission. Derive names from the actual repository/account and accepted distribution scope; identify missing consequential information before publishing.

CI runs language checks, configuration/schema checks, unit/integration/component tests and the critical journey with owned stores. Build artifacts without registry writes on untrusted PRs. Keep trusted release jobs separate, minimal permissions, reviewed full-SHA actions, bounded execution and failure evidence. Test workflow syntax with actionlint and relevant YAML checks; lint/build Dockerfiles and start the built image when the environment supports it. A YAML parser cannot establish a valid workflow or a working image.

Document how a verified artifact is promoted to an agreed environment, how migrations run once, how configuration is supplied, how outcome verification gates promotion and how compatible recovery works. If no deployment target is selected, record the unresolved decision and prepare the target-independent process. Do not invent cloud resources or claim an unconfigured deploy job is ready.

Use current first-party references for implementation; examples must be adapted and actions pinned to reviewed revisions:

- [GitHub container publication](https://docs.github.com/en/actions/tutorials/publish-packages/publish-docker-images).
- [PyPA GitHub Actions and Trusted Publishing](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/).
- [npm Trusted Publishing](https://docs.npmjs.com/trusted-publishers/).
- [Docker build practices](https://docs.docker.com/build/building/best-practices/).
