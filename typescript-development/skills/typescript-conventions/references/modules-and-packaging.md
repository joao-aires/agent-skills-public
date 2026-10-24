# Modules and packaging decisions

Consult when changing compiler options, imports, package exports or build output. Select documentation for the installed compiler/runtime rather than copying a universal tsconfig.

| Consumer/host | Establish | Verify |
| --- | --- | --- |
| Runtime executes emitted JavaScript | Runtime version, package type, extensions and ESM/CommonJS interoperability | Actual emitted imports and supported entrypoints load outside the development runner |
| Bundler consumes TypeScript | Bundler resolution/transforms, target and runtime globals | Production bundle, split chunks/assets and actual target execution |
| Runtime executes TypeScript directly | Supported syntax/transforms, resolution and whether checking occurs | Separate type check plus direct execution on the promised runtime version |
| Published library | Public entrypoints, module formats, declarations, supported compiler/runtime and peer dependencies | Packed contents and representative external consumer type/runtime checks |
| Workspace/shared package | Ownership, build order, public imports and dependency graph | Consumer works through intended exports rather than accidental source aliases |

## Follow an import to its consumer

Check the path from source import to distributed code. The compiler may use declarations or aliases that are available only in the workspace, while the runtime loads the emitted JavaScript through package metadata and actual files. A declaration file describes a consumer contract; it does not establish that an exported value exists or that its imports resolve.

Inspect the package contents and public exports, then exercise a representative consumer through those exports outside the source workspace. Keep that consumer from resolving unpublished source paths or relying on the repository's development aliases. Check both its type use and runtime loading for the formats the package promises. An application needs the corresponding check through its production build and supported entrypoint.

Separate declaration generation, transpilation, bundling and type checking in the actual toolchain. A successful transform can leave a type error unchecked, while a successful type check can accept an import that the bundler or runtime cannot load. Verify the steps that the chosen host and consumer actually depend on.

For large type/build cost, inspect diagnostics and dependency boundaries before adding elaborate project references or disabling checks. A valid type assertion can still misrepresent untrusted data; runtime validation and semantic tests remain necessary.

Primary references: [module theory](https://www.typescriptlang.org/docs/handbook/modules/theory.html), [compiler-option selection](https://www.typescriptlang.org/docs/handbook/modules/guides/choosing-compiler-options.html), [publishing declarations](https://www.typescriptlang.org/docs/handbook/declaration-files/publishing.html), [Node TypeScript execution](https://nodejs.org/api/typescript.html). Other accepted hosts require their own version-matched documentation.
