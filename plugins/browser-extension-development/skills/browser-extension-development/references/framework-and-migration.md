# Framework configuration and migration

## Read the build before editing it

Find installed package versions and scripts first. File names are clues, not proof of a framework or a command. Confirm the plugin import and its actual configuration, then inspect the generated production directory. Preserve an existing Vite/plain/WXT/CRXJS project unless migration is part of the objective.

| Approach | Source of entrypoints and manifest | What to inspect |
| --- | --- | --- |
| Plain bundled extension | Authored manifest plus the project's bundler inputs | Emitted paths, bundled scripts/assets, module format and copied resources |
| WXT | Config plus file-based entrypoints and entrypoint options | Actual source directory/configuration, generated manifest and target-specific output |
| CRXJS | Vite `crx({ manifest })`, using an explicit JSON manifest or `defineManifest` | Vite plugin registration, manifest object/file and referenced source inputs |

CRXJS does not imply a `crxjs.config.ts`, automatic entrypoints from `package.json`, or a built-in publishing command. Follow [its manifest contract](https://crxjs.dev/concepts/manifest/) and [Vite setup](https://crxjs.dev/guide/installation/from-scratch/). WXT discovers entrypoints according to [its configured conventions](https://wxt.dev/guide/essentials/entrypoints.html); do not apply those file names to another bundler.

For new projects, confirm a current compatible scaffolder command from the chosen framework. Check generated dependencies and scripts before running follow-up commands; do not add a second lockfile or assume a `zip`/`package` script exists. Establish lint/type checks, behavior tests, production build and applicable CI/documentation using the project's foundation conventions. A scaffold is a starting point, not completed application setup.

The generated manifest should reference files actually present in the distribution. Check its background type, popup/options/side-panel paths, content-script matches, permissions, web-accessible resources and production CSP. Development servers and HMR can introduce behavior or access that must not leak into the release build. Bundle executable code locally for the applicable MV3/store requirements and verify any necessary WebAssembly or sandbox arrangement against current policy.

## Migrate behavior, not only manifest keys

Inventory the existing actions, page access, persisted data and supported user environments before changing MV2. Record which outcomes must survive. Avoid combining the browser migration with a framework or visual redesign unless that is accepted scope.

1. Separate background DOM work from coordination. Use a suitable extension page or the supported offscreen-document mechanism only when required; verify its reasons, permissions and lifecycle. An MV3 service worker has no `window` or `localStorage`.
2. Replace persistent process assumptions with event handlers and stored state. Audit timers, globals, queue progress and initialization after restart. Convert storage with a versioned, repeatable migration that preserves existing user data.
3. Map deprecated APIs to supported capabilities. Blocking network interception needs a functional comparison with declarative rules, including rule limits and any enterprise-specific exception; it is not a mechanical method rename.
4. Revisit host access, content-script injection, web-accessible resources and CSP under the new model. Keep grants limited to the intended operation and sites.
5. Test existing-user update, clean installation, worker restart, navigation and denied/revoked access using the production build. Verify data and resulting user behavior independently of startup success.

Use the [Chrome migration guide](https://developer.chrome.com/docs/extensions/develop/migrate), [worker lifecycle](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers/lifecycle) and version-matched API documentation. State any incompatible behavior and the actual affected audience; do not promise Firefox/Edge/Safari parity from a Chrome test.
