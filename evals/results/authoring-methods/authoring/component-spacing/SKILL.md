---
name: component-spacing
description: Adjust spacing within an existing component while preserving the accepted design system.
user-invocable: true
---

# Adjust spacing in context

Inspect the component with its actual content and the adjacent elements it must align with. Identify which elements form a group and which gaps separate groups. Use the existing spacing roles and comparable components to choose those gaps: related elements should read as a unit, while separate groups should remain distinguishable. Keep shared edges aligned with the surrounding layout.

Adjust the relevant padding or gaps using the accepted spacing system. Preserve accepted type, color and interaction behavior. A spacing request does not authorize a component-library migration.

Render the affected component in context and at its relevant narrow layout. Check whether grouping and alignment remain clear with long labels and content growth, and whether keyboard focus remains visible without clipping or overlap. If a gap works only for the current short content, revisit the spacing in that context before reporting success.

Report the spacing adjusted, why it fits the component's grouping and alignment, and the layouts and content states actually checked. If rendering is unavailable, describe the proposed change and explicitly leave visual verification outstanding. Distinguish any applied edit from a proposal and any unchecked state from a verified result.
