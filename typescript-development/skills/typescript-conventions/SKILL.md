---
name: typescript-conventions
description: Build, extend or review TypeScript libraries, services and clients using
  the accepted runtime and toolchain. Use for module/compiler configuration, public
  types, runtime boundaries, package compatibility and meaningful verification independently
  of a frontend framework.
license: MIT
metadata:
  scope: stack-specific
  invocation: both
  role: support
  stack: TypeScript
  references: references/sources.md
user-invocable: true
---

# Match TypeScript to its execution and consumer contracts

Read the repository's supported compiler/runtime versions, package manager/lockfile, scripts, module/package boundaries and accepted conventions. Determine whether the result is a library, service, CLI, browser/native client or shared package. Loading language guidance does not select React, a backend framework, Node, Bun, Deno or a bundler. Read [modules and packaging](references/modules-and-packaging.md) when changing resolution, emitted artifacts or consumers, and [sources](references/sources.md) for primary guidance and upstream selection rationale.

## Preserve understandable type contracts

Use types to make valid domain states understandable and invalid combinations difficult to express. Keep related state and behavior together so callers can see what is required for an operation. Prefer inference for local values; use explicit stable public contracts where they help consumers understand and depend on the API.

At JSON/configuration, network, storage and provider boundaries, treat the received value as unknown until the application's validation establishes its shape and meaning. A type assertion changes what the compiler believes; it does not inspect the value. Generated client types and non-null operators likewise cannot establish that runtime input is valid.

Narrow values using validated evidence and retain the distinction between absent, null and optional fields through serialization. Check the actual consumer contract when that distinction changes behavior. Choose the project's existing validation approach rather than adding a schema library solely for this skill.

Use discriminated unions, generics, mapped/conditional types or branded identifiers when they clarify a real contract. Keep common paths readable and account for compiler/editor performance. Avoid introducing an advanced type technique, enum prohibition or complete strictness migration as a prerequisite for a small fix. Preserve an accepted policy; for compatible new work prefer useful strict checking, and stage any migration against the actual codebase.

## Align the compiler with the host

Choose target/lib, module/resolution, import extensions and emission for the actual runtime or bundler.

- Available declarations do not add runtime APIs or polyfills.
- TypeScript paths aliases do not by themselves teach the runtime how to resolve imports.
- Separate server/browser/native globals, public/private configuration and type-only/value imports according to the chosen host and compiler options.

Keep package exports, JavaScript output and declarations consistent. Check supported ESM/CommonJS consumers and module identity only where the package promises them; dual publishing is not compulsory. Assess dependency/peer ranges, public transitive types and runtime imports before release. Preserve existing workspace/package boundaries and avoid creating a monorepo or shared abstraction solely for possible reuse.

## Preserve runtime and failure behavior

Handle asynchronous work, errors, cancellation and resource ownership through the selected runtime/framework. Type-level success does not settle authorization, persistence, retry or recovery behavior. Avoid detached/unhandled work where the contract requires completion, and keep model/user/provider data untrusted at runtime. Seek available service, identity, data or client expertise by capability when relevant; absence of specialists does not remove essential reasoning.

## Verify the distributed result

Use actual project commands for types, lint/format, tests and production build.

- Transpilation or direct execution of TypeScript may omit type checking, so verify that the relevant check runs.
- Test public type contracts when consumers depend on them and runtime behavior separately.
- For libraries, inspect the packed artifact and exercise representative consumers outside source aliases/workspace conveniences; for applications, exercise the supported production entrypoint and environment.

Report the affected contracts, actual checks and version/runtime limits. Package publication, runtime migration and deployment remain separate authorized actions. No blanket coverage target or framework dependency is imposed.
