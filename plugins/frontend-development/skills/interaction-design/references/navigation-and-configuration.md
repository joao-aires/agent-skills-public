# Navigation and configuration design

Use this when defining an application's views, reorganizing navigation or separating ongoing work from configuration. Work from the accepted product capabilities, audience and platform. A familiar pattern is useful when users recognize its purpose; familiarity alone does not establish that the application needs it.

## Find the structure in the work

Read the main journeys and existing routes before drawing a menu. Identify where people start, which objects they compare or change, and where one task leads to another. Group related tasks around those objects and goals. A destination should give someone a reason to go there and a way to understand their current location. Avoid grouping by implementation details that users do not need to operate the product.

Capture the proposed destinations and important transitions in a short route/task map. For each destination, identify its purpose, intended users, current object or workspace, entry points and return path. A small application may need only a workspace and a configuration view. Larger applications may need several levels; add hierarchy when it helps users distinguish meaningful areas without repeatedly passing through unrelated pages.

Check existing content and behavior against the map. Hidden actions, duplicate settings and contradictory labels can indicate an unclear ownership boundary. Move the underlying capability to an appropriate home before adding instructions that explain where it went. Preserve legitimate alternate entry points when they reach the same state and make sense in context.

## Give controls a scope and a home

Classify a control by what changing it does, rather than its appearance:

| Concern | Placement reasoning | Behavior to establish |
| --- | --- | --- |
| Input for the current operation | Keep it near the work or in a related disclosure when users need it to form the result. | Whether it changes the current draft, immediately recomputes a result or requires an explicit action. |
| Default for later operations | Give it a stable settings home. A current-task shortcut may expose it when frequent changes justify that access. | What inherits the default, which overrides remain, and when existing work adopts the new value. |
| Persistent connection or account configuration | Allow enough space for setup, validation and recovery; reuse a recognizable integration or account area when one exists. | Saved values, verified access and actual permissions are separate states. |
| Administration or commercial controls | Add destinations for accepted capabilities and the roles that use them; distinguish planned new views from functionality already available. | Which context is being administered and which authority the application actually checks. Hiding a link does not enforce access. |
| Help and consequential disclosures | Put the relevant explanation or decision beside the action it informs; provide a findable home for detailed help or management. | Which information must be available before acting and how users later inspect, change or revoke the choice. |

A current filter and a saved default filter can refer to the same field while having different effects. Make those effects explicit before exposing both. A shortcut should lead to the same source of truth, not create a second configuration form with different save or validation behavior. Frequency is one consideration: an infrequent destructive or access decision can need more visibility than a frequently edited cosmetic preference.

Group settings by a user-recognizable purpose and scope. Personal appearance, workspace policy and organization administration may need different homes or clear grouping, depending on the product. Keep related validation and save behavior together. A long settings page is not automatically improved by converting every section into another tab; use sections, search or navigation according to the amount of configuration and how users find it.

## Choose a destination or an in-place interaction

| Pattern | Useful when | Tradeoff to resolve |
| --- | --- | --- |
| Page or dedicated view | The task needs space, its own location, substantial configuration or direct entry. | Preserve the relevant object and unfinished work on departure and return. A route change need not imply opening another browser tab. |
| Drawer or adjacent panel | A related task benefits from seeing the underlying work. | Check that both remain readable at actual widths. Define focus and dismissal behavior; a narrow layout may need a full view. |
| Dialog | A short edit or decision warrants a focused interruption. | Provide a bounded completion/cancel path. Complex nested navigation and long setup can outgrow it. |
| Inline controls or disclosure | A small choice or explanation belongs to the current task. | Keep it discoverable without pushing primary content and actions away. Material consequences cannot depend on discovering optional help. |
| Navigation links and sibling views | Users move between stable areas or related views of an object. | Make the active location and return behavior clear. Use hierarchy for parent/child relationships and tabs only where their view-switching behavior fits. |
| Action or overflow menu | Secondary operations belong to the current object or selection. | Make the affected scope understandable. Hiding a frequent primary action increases the work needed to reach it. |

Match semantics and keyboard behavior to what the control does. In web interfaces, ordinary navigation links do not automatically need the ARIA `menu` role merely because the design calls the collection a menu. The [WAI disclosure navigation example](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/examples/disclosure-navigation/) explains that distinction; use supported project primitives and verify their actual behavior. Native interfaces follow their platform's navigation and interaction conventions.

## Specify departure, change and return

Trace a configuration visit from the point where the user is doing other work:

1. Establish what identifies that work: object, account/workspace, selection, draft, scroll position or pending result, as relevant.
2. Describe the route to configuration and how the user knows its scope. Decide whether the task needs an adjacent interaction or a different view.
3. Define immediate versus explicit-save changes, validation failures, cancellation and unfinished edits. Preserve or discard values according to that contract, rather than according to which component happens to unmount.
4. Describe the return path and the effect on the original work. A changed setting may apply later, synchronize now or invalidate a pending result. Make that outcome understandable and enforce it at the operation boundary.

Opening a new tab or window can serve a real platform or continuity need. Establish whether it creates another view of the same session or a different session, and how users return. Keeping everything on one route also has costs if it obscures location, produces nested overlays or prevents direct access to substantial configuration.

Use existing notes or a wireflow where transitions are the uncertainty. An inventory of page names alone does not explain who can do what, where state lives or what a return visit restores.

## Review the complete journey

Assess whether the intended user can find a task, locate the configuration that affects it, understand the effect of a change and return without reconstructing unrelated work. Include relevant narrow layouts, keyboard navigation and role/context variants. If a setting is available from several places, compare their scope, validation, persistence and feedback.

Inspect the rendered experience when it exists. Repeated explanatory copy, inconsistent locations or unexpected navigation may reveal a structural problem that labels alone cannot fix. Verify focus and current-location cues as well as appearance; preserve meaningful explanations on demand when reducing clutter. Readable screenshots and an agent's successful walkthrough do not establish participant findability or comprehension. State which transitions were exercised and which decisions remain unverified.

The [GOV.UK navigation guidance](https://design-system.service.gov.uk/components/service-navigation/) provides a concrete example of recognizable service identity and navigation. Use the relevant reasoning with the product's own design system; its government-service structure is not an application template.
