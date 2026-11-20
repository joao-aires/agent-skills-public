# Export API

Deploys to the `staging` target from the `main` branch through `.github/workflows/ci.yml`.
A green workflow is build evidence, not proof that staging serves the revision.
`deploy.sh` is the staging action and requires explicit authorization.
