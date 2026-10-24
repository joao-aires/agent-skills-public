# Inspect component and token drift

Resolve the requested page, flow, component library or changed callers. Inventory only the relevant component definitions/instances, variants, semantic tokens and binding relationships. Trace to implementation as well as design artifacts when both are available. Visually similar controls may intentionally have different behavior or platform constraints; matching names alone cannot establish equivalence.

Identify confirmed duplicates, orphaned instances, inconsistent names, unbound values, missing meaningful states and caller overrides. Separate missing access to a remote library from a genuinely orphaned component. Record the exact instance/definition, expected relationship, evidence and user or maintenance impact. Group repeated root causes; an inventory count is not proof of a defect.

Review is read-only. When repair is authorized, inspect references/consumers first, use existing variants and semantic tokens, and preserve live bindings, instance overrides, accessible behavior and required platform differences. Renaming, cloning, detaching or mass-swapping instances can break consumers; do not apply those changes merely because an audit script suggests them. An intentional alternative spacing scale or optical offset is not drift by definition.

Verify relevant variants and actual callers after a shared change. Recheck binding/instance identity, realistic content, errors and narrow layouts. Compare screenshots where useful and run applicable interaction/regression checks; static token parity does not prove focus behavior. Report what changed, what was inspected and what remains unverified. Annotation or audit-document writes also need to be within the requested scope.
