---
name: build-delivery-pipelines
description: Create or review CI/CD, Dockerfiles and GitHub Actions for application verification, artifact promotion, deployment and rollback or roll-forward. Apply when delivery infrastructure changes, within the requested repository and environment scope.
---

# Build delivery pipelines

## Separate verification, artifacts and deployment

Read the application commands, environment model and accepted deployment decisions. Keep workflows small enough to explain: CI verifies a change; release produces a versioned artifact; deployment promotes that artifact to an environment. Combine stages for a small application when clearer. Share repeated mechanics through reusable workflows or composite actions with explicit inputs, permissions and outputs; avoid a generic pipeline framework.

Keep GitHub entrypoints in `.github/workflows/`; keep application-specific scripts and Dockerfiles beside their application. Run the same meaningful checks locally and in CI. Provide fast feedback before expensive integration/E2E checks, retain useful failure evidence, and make required checks stable across path filters. Do not let a skipped workflow leave a required check permanently pending.

## Use readable names

For new workflows, use `<activity>-<application>.yml`, such as `ci-api.yml`, `release-api.yml` and `deploy-api.yml`. Display names use `CI / API`, `Release / API`, `Deploy / API`; include the target and artifact in deployment run names. Use lowercase job IDs describing the responsibility (`unit-tests`, `build-image`, `deploy-staging`, `verify-production`) and human-readable job names. Give steps short verb-object names: `Install dependencies`, `Run API tests`, `Publish image`, `Verify deployment`. Follow a consistent existing convention rather than renaming everything. Names should explain purpose without opening the implementation.

## Build reproducible containers

Use trusted, maintained base images, explicit versions/digests with an update process, locked application dependencies, multi-stage builds where useful, and a minimal runtime containing only required files. Exclude secrets, local environments and irrelevant build inputs with `.dockerignore`. Order dependency and source layers for useful caching. Use build secret mounts; do not bake credentials into arguments, environment layers or copied files. Run as a non-root user where supported, make ownership explicit and preserve graceful termination. Verify the actual image starts with the deployment's command/configuration; a successful build is insufficient.

## Promote and recover deliberately

Build once and promote the same immutable artifact/digest through environments. Keep environment configuration and secrets separate from the artifact. Use scoped deployment credentials, environment protection appropriate to the project, and concurrency controls that prevent overlapping promotions; do not cancel a deployment mid-migration casually. Record the deployed revision and artifact, run post-deploy smoke checks against the real target, and stop promotion on failure.

Every delivery path should have a usable rollback or roll-forward route: retain the previous artifact/configuration, identify compatibility constraints, and expose a clear recovery input or job. Review schema compatibility before rollout; use expand/migrate/contract when needed. Rolling back application code does not undo data changes. Prefer a compatible forward fix when reversal would lose data; point to the application's data-recovery runbook when restoration is necessary. Verify the recovery mechanics in a safe environment and keep them current with migrations and infrastructure changes. Do not claim production recovery from a YAML review alone.

## Protect the pipeline

Use installed `github-actions-hardening` for detailed review. Keep permissions minimal, pin third-party actions to reviewed full commit SHAs with update automation, prefer OIDC to long-lived cloud keys, and treat PR content as untrusted. Separate untrusted validation from privileged publishing/deployment. Do not execute fork code with production credentials. Bound job duration and distinguish caches from deployable artifacts.

Report which checks and recovery paths were actually exercised, target environments and remaining gaps. Consult current [GitHub security guidance](https://docs.github.com/en/actions/reference/security/secure-use) and [Docker build guidance](https://docs.docker.com/build/building/best-practices/) for the project's versions and platform.
