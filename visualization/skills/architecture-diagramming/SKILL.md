---
name: architecture-diagramming
description: Create or refine responsive, theme-aware HTML architecture diagrams for structural, runtime, data and deployment explanations. Use when a portable HTML diagram is requested or chosen; preserve existing notation and accepted visual direction.
metadata:
  version: '2.0'
  scope: generic
  invocation: user
  role: task
---

# Explain architecture in portable HTML

Create a responsive, self-contained HTML diagram when that is the requested artifact. Choose a view that answers the reader's structural, runtime, data or deployment question. For an existing project, preserve its accepted notation and visual direction; a diagramming request alone does not authorize application changes.

## Establish meaning before layout

Identify the audience, question, scope and source evidence. Distinguish implemented architecture, observed deployment, proposed design and unknowns. Trace important relationships to supplied context or source; use current-system mapping expertise or evidence-backed architecture explanation expertise when available for deeper discovery and semantic coverage. Keep technology lists and invented components from standing in for an explanation.

Choose the smallest view that answers the question. Decide what each element and connection means before arranging it:

| Reader's question | Suitable view | Meaning to preserve |
| --- | --- | --- |
| What is the structure? | Context/container/component | Responsibilities and directed dependencies |
| What happens in what order? | Sequence | Participants, ordering and consequential branches |
| How does state change? | State/lifecycle | Valid states and transitions |
| Where does information move? | Data flow | Information sources, destinations and movement |

Mixing those meanings in one unlabeled connector makes an attractive diagram difficult to interpret.

Keep labels, directed relationships and boundaries consistent. Give a relationship a verb or message that explains what crosses it. Use grouping to express an actual boundary or ownership, and provide text for important meaning. Add another view when it answers a different useful question rather than overloading one picture with every detail.

## Use the HTML guide selectively

Read [HTML patterns and design system](references/html-guide.md) when constructing or repairing this artifact. It retains the original layout catalogue, theming conventions, connectors and responsive techniques. Treat its dark/light palette and example layouts as a coherent starting profile; adapt visual choices to the brief and content while keeping portability and semantic clarity.

Use reusable CSS variables, fluid layouts and detail disclosure to keep realistic labels readable. Show connections and ordering clearly at the target widths; hiding connectors must not remove the only explanation of a relationship. Select blocks for the information they communicate rather than filling a fixed card arrangement.

## Verify the delivered explanation

Render the actual file and inspect representative dense/long-content views, supported themes and narrow layouts. Check readable labels, complete relationships, navigation/links and any interaction. Reconcile architectural claims with evidence separately from HTML rendering. Deliver the artifact path, evidence scope, unresolved assumptions and checks actually performed; a valid file cannot establish that a proposed system is implemented.
