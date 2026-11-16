# Contract template

Use this shape for every artifact contract: a reader test, a normative content block, the handoff to the next phase, and the maturity/evidence rules. Keep detailed writing advice in the paired guide.

```markdown
# <Artifact> contract: <one-line purpose>

<What the artifact is, what it is not, and which authority or home it uses.>

Read [guide-<artifact>](../../../guide-<artifact>/SKILL.md) for writing conventions, examples and review checks.

## Reader questions

A <reader> must be able to answer:

1. <decision or action question>
2. <scope and authority question>
3. <content question>
4. <evidence or status question>
5. <handoff question>

## Contract

```markdown
# <Artifact title>

## <Required section>
<What it must answer.>

## <Required section>
<What it must answer.>
```

## Handoff

<What the next phase needs and which linked artifacts may supply it. See [handoff](../handoff.md).>

## Maturity

<Allowed states and what each may claim.>

## Review

<The reader test for this artifact, not a generic checklist.>
```

Rules:

- The reader questions and `## Contract` block are normative.
- The handoff is normative; it is content, not a document.
- Maturity and evidence are normative.
- `## Review` is guidance; detailed examples and anti-patterns belong in the guide.
- One contract per artifact type. Do not create a contract per software type or per tool.
