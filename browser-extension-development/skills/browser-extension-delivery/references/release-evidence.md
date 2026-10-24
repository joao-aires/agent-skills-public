# Release evidence and automation

## Package the verified production tree

Use the actual build output selected by the framework/target. Inspect the manifest version, entrypoint paths, resources, production endpoints, permissions and CSP. Check that all referenced files are present and no development server, confidential key, test credential or private data is bundled. Decide source-map treatment deliberately: maps may expose source but are not inherently a store violation.

Create the ZIP from inside the production extension root so `manifest.json` is at the archive root. Inspect its entries after creation. Record source revision, lockfile/configuration identity, relevant checks and ZIP digest. The archive is the candidate to promote; rerunning a build under a different environment requires evidence for that new artifact.

Use [Chrome's version field rules](https://developer.chrome.com/docs/extensions/reference/manifest/version) rather than assuming every SemVer prerelease string is valid. Reconcile framework-generated versions and any package metadata. Test clean install and the relevant previous-version update/data path; additional grant warnings or disabled features can change the user's upgrade experience.

## Integrate into the existing CI

Keep untrusted PR verification separate from privileged release credentials. Use the repository's established action pinning, supported runtime, least-privilege permissions and environment protections. The technical stages are:

| Stage | Observable output |
| --- | --- |
| Verify/build/package | Candidate ZIP and digest, generated manifest, test results and scoped gaps |
| Upload | Publisher/item and uploaded candidate identity or an explicit ambiguous result |
| Submit | Review state for that item/version, with the authorized visibility/publication policy |
| Publish/observe | Current store state and separately verified installed version where available |

Implement only stages authorized by the release policy. A readiness-only task can describe an upload job without executing it; a candidate workflow should not silently publish on every push/tag. Preserve existing workflows and credential handling rather than installing a global uploader or assuming the application uses GitHub Actions.

Consult the current [Chrome Web Store API](https://developer.chrome.com/docs/webstore/api) and selected uploader's actual version/support. The current API includes V2 and service-account support; older OAuth/CLI examples are not a universal setup contract. Keep credentials in approved secret mechanisms and avoid command/log/report exposure. Distinguish authentication setup from permission to promote an item.

After timeouts or partial failures, query supported item/upload/review status and compare the candidate version before retrying. Define what evidence permits continuation or requires publisher intervention. Store review and browser adoption can lag publication, and a corrective higher version may be the workable recovery path. Check [publishing documentation](https://developer.chrome.com/docs/webstore/publish) and actual item status before promising rollout percentages, staging channels or rollback capabilities.
