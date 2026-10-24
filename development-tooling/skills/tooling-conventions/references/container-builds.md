# Docker build and runtime checks

Apply when containers are the accepted build/runtime boundary. Preserve an existing compatible engine and distribution policy.

- Use trusted, maintained base images, explicit versions/digests with an update process, locked application dependencies, multi-stage builds where useful, and a minimal runtime containing only required files.
- Exclude secrets, local environments and irrelevant build inputs with `.dockerignore`.
- Order dependency and source layers for useful caching.
- Use build secret mounts; do not bake credentials into arguments, environment layers or copied files.
- Run as a non-root user where supported, make ownership explicit and preserve graceful termination.
- Verify the actual image starts with the deployment's command/configuration; a successful build is insufficient.


Use the selected image with actual initialization, readiness, graceful termination and configuration. Read [local environment](local-environment.md) for Compose isolation and [artifact defaults](artifact-defaults.md) for chosen publication.
