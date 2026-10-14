# Local environment references

- [Compose profiles](https://docs.docker.com/compose/how-tos/profiles/): optional services; verify required dependencies are included for each invocation.
- [Compose startup order](https://docs.docker.com/compose/how-tos/startup-order/): health conditions and one-shot initialization.
- [Compose project names](https://docs.docker.com/compose/how-tos/project-name/): isolate feature worktrees and test runs; also isolate explicitly published ports and shared/external resources.
- [SigNoz Docker installation](https://signoz.io/docs/install/docker/): use the currently supported self-hosted installation and sizing. Older bundled deployment files may be deprecated; verify release-specific instructions before implementation.
- [Langfuse Docker Compose](https://langfuse.com/self-hosting/deployment/docker-compose): optional AI evaluation backend with its own dependencies; local Compose is not production high availability or backup design.

Author application-specific Compose services, profiles, fixtures and scripts in the target repository. This skill supplies guidance, not a generated stack. An existing stack can satisfy the same startup, isolation, readiness and diagnostic contract.
