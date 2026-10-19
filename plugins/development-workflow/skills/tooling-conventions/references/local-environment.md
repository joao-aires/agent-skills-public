# Local environment references

- [Compose profiles](https://docs.docker.com/compose/how-tos/profiles/): optional services; verify required dependencies are included for each invocation.
- [Compose startup order](https://docs.docker.com/compose/how-tos/startup-order/): health conditions and one-shot initialization.
- [Compose project names](https://docs.docker.com/compose/how-tos/project-name/): isolate feature worktrees and test runs; also isolate explicitly published ports and shared/external resources.
- [SigNoz Docker installation](https://signoz.io/docs/install/docker/): use the currently supported self-hosted installation and sizing. Older bundled deployment files may be deprecated; verify release-specific instructions before implementation.
- [Langfuse Docker Compose](https://langfuse.com/self-hosting/deployment/docker-compose): optional AI evaluation backend with its own dependencies; local Compose is not production high availability or backup design.

Author application-specific Compose services, profiles, fixtures and scripts in the target repository. This skill supplies guidance, not a generated stack. An existing stack can satisfy the same startup, isolation, readiness and diagnostic contract.

For an explicitly chosen container-based development setup, prefer app-specific Compose services for the real frontend/API/workers and required databases, queues, object storage or local email capture. Host-native hot reload can use those dependencies. Isolate Compose project names, published ports, credentials and volumes per worktree/test run; check initialization and application readiness beyond container order. Document safe stop/reset and never remove shared volumes implicitly.

For my selected local diagnostics setup, prefer SigNoz when its supported footprint fits a unified view, or Langfuse for an actual AI dataset/experiment workflow. These are technical preferences, not generic setup requirements. An optional profile/companion stack needs explicit connectivity, resource/retention limits and real received-signal evidence. Preserve an accepted backend. Read [telemetry backends](telemetry-backends.md) for compatible routes.
