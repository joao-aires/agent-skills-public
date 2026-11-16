# Composition: select expertise without losing the outcome

The requested activity owns its outcome, scope and stopping point. Supporting methods deepen the work; they do not replace the activity or become prerequisites.

## Select by capability

Use the client's observed skill inventory or supported discovery. Match the **capability described** to the need; do not maintain a hardcoded list of specialist names, plugin identifiers or filesystem paths. A description is the portable selection surface. Metadata can help where the client exposes it.

| Need encountered during work | Expertise to seek | Fit to establish |
| --- | --- | --- |
| Product outcome, priority or useful slice is unclear | User-problem discovery, prioritization and evidence synthesis | Actual audience, supplied evidence and requested stopping point |
| Service behavior changes | Authority, transactions, stored state, failure and consumer contracts | Accepted implementation and affected boundaries |
| A meaningful interface change | Interaction design, visual hierarchy, accessibility and task language | Actual platform, components, users and affected states |
| An accepted backend needs implementation | Language/framework/persistence expertise | Repository evidence, actual versions and existing commands |
| Delivery infrastructure changes | Artifact identity, trust, compatibility and recovery, then provider implementation | Chosen CI, artifact ecosystem, destination and authorization |
| Documentation or architecture explanation | Writing craft and architecture subject expertise | Actual reader, current evidence and accepted decisions |

Read the matching guidance when available, check its fit and carry useful conclusions into the work. A specialist can also be requested directly; selecting a discipline does not start a full lifecycle.

## Compose domain, interface and technical guidance

A substantive interface task can need three kinds of judgment concurrently:

- **Application/domain or archetype expertise** defines objects, workflows, data meaning and candidate patterns.
- **General interface design** synthesizes information architecture, interactions, visual direction and critique.
- **Technical/platform expertise** contributes existing component contracts, system constraints and implementation feasibility.

These are responsibilities, not an invocation chain. A domain specialist can design without the generic skill; generic design can work without a matching archetype; later verification can send an assumption back for revision. Reconcile conflicts against accepted product outcomes, domain/authority invariants, accessibility/platform obligations and observed evidence.

## Fallback when expertise is absent

| Situation | How work proceeds |
| --- | --- |
| A relevant specialist is available | Read it, confirm applicability and incorporate its guidance within the current scope |
| No specialist, but the project establishes an approach | Use authoritative instructions, code/configuration, accepted decisions and the existing toolchain |
| No specialist or established approach | Use general expertise and current primary sources; verify against the same acceptance criteria |
| A material decision remains unresolved | Investigate technical facts, ask only for the actual unresolved choice and continue independent work |
| A required tool, access or execution target is unavailable | Complete useful independent work and report the precise boundary |

Missing guidance is not missing capability. A Python change can proceed without a Python skill; native operation cannot be claimed without the required runtime/device evidence. Do not install guidance automatically, replace an accepted technology, bypass native controls, start another explicit-only activity or ask again for authority already granted.

## When guidance conflicts with the project or environment

Optional guidance is not authority over the accepted project. Apply these rules:

- **Project constraints win.** An accepted project convention, explicit task constraint or requested outcome overrides an optional method's defaults. A stdlib-only task does not become a framework project because a stack guide prefers one.
- **A task-specified interface is a user decision.** When no user is available and the task names the public interface, seam, file home or command surface, treat that as the agreed decision rather than asking again.
- **Unavailable surfaces do not erase the method.** If a method assumes slash commands, a Git flow, parallel subagents or a tool that is not present, apply its intent inline, record the adaptation and keep the same acceptance standard.
- **Do not treat upstream defaults as authority.** Upstream methods are inputs, not project policy. Preserve their useful reasoning and drop assumptions that conflict with the accepted environment.
- **Record the deviation.** A skipped step, adapted command or unavailable check belongs in the evidence record, not in silent success.

## Keep the activity in charge

- The activity chooses enough expertise to answer the actual question. Reuse accepted solutions for small corrections.
- Descriptions advertise applicability, not absolute precedence. Do not turn an optional specialist into a routing dependency.
- Preserve required internal links and package resources. Optional cross-package guidance is selected by capability, not by a resolver.
- Keep reference atlases, pattern libraries and blueprints separate from execution tasks; do not copy their whole contents into a generic skill.
- Respect native invocation controls and the requested stopping point. Help may name observed activities; it must not fire them.

The [artifact system](../../artifact-system/SKILL.md) owns artifact contracts, homes and quality. This reference owns how supporting expertise composes around the activity.
