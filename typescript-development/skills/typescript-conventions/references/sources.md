# TypeScript sources and upstream selection

This is original focused guidance for a gap across runtimes and package types. No TypeScript upstream skill is acquired. React/native implementation guidance retains enough language reasoning to work independently; this package deepens module, validation and distributed-artifact decisions.

| Reviewed candidate | Revision | Decision |
| --- | --- | --- |
| [Jeffallan typescript-pro](https://github.com/Jeffallan/claude-skills/tree/36f3fe8052da7c57083783268c6ea3265d075265/skills/typescript-pro) | `36f3fe8052da7c57083783268c6ea3265d075265` | Reference only. Useful type/configuration topics, but compulsory branded types, declaration generation and fixed configuration do not fit every application/runtime. Repository declares MIT. |
| [Wshobson typescript-advanced-types](https://github.com/wshobson/agents/tree/0874a27b17a22e2b7c2e2bcd725768e0803cad06/plugins/javascript-typescript/skills/typescript-advanced-types) | `0874a27b17a22e2b7c2e2bcd725768e0803cad06` | Reference only. Focused tutorial examples do not replace the runtime/module/package foundation; substantial overlap with the official handbook does not currently justify adding another entrypoint. Repository declares MIT. |
| [Microsoft TypeScript repository](https://github.com/microsoft/TypeScript/tree/28534d7609062699a68b1b66e2367f8d95dbf290/.github/skills) | `28534d7609062699a68b1b66e2367f8d95dbf290` | Its inspected skill inventory concerns compiler-repository/API/test work rather than general TypeScript application development. No compiler-maintenance workflow is imported. |

## First-party implementation references

- [TypeScript module theory](https://www.typescriptlang.org/docs/handbook/modules/theory.html) and [compiler option selection](https://www.typescriptlang.org/docs/handbook/modules/guides/choosing-compiler-options.html) explain why the host determines valid module behavior.
- [Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html), [generics](https://www.typescriptlang.org/docs/handbook/2/generics.html) and [configuration](https://www.typescriptlang.org/tsconfig/) inform types and compiler decisions; do not copy every advanced technique into routine work.
- [Publishing declarations](https://www.typescriptlang.org/docs/handbook/declaration-files/publishing.html) and the chosen runtime/package manager's official guidance own actual package behavior.
- [Node TypeScript](https://nodejs.org/api/typescript.html) distinguishes supported direct-execution syntax and limitations. Node is an example host, not this package's required runtime.

Choose actual installed/supported versions when implementing. Frontmatter source metadata is attribution and reading context; it does not install a tool or implement optional dependency routing.
