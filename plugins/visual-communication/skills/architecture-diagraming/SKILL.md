---
name: architecture-diagraming
description: "Build responsive, theme-aware HTML architecture diagrams using CSS grid/flexbox and CSS variables. Use when the user asks to: create a system architecture diagram, map out microservices, visualize cloud infrastructure, draw a sequence diagram, model data flows, build a deployment diagram, create a state machine visualization, design a pipeline or DevOps flow, map network topology, show integration between systems, create any kind of technical diagram or visual system map. This skill should be used any time the user wants to visualize how software components, services, infrastructure, or data relate to each other — even if they don't explicitly say 'architecture diagram'. Covers structural diagrams (system, application, cloud, network, deployment), behavioral diagrams (sequence, data flow, state, pipeline), and operational diagrams (resilience, availability)."
metadata:
  version: "2.0"
---

# Architecture Mapper

Create beautiful, responsive, single-file HTML architecture diagrams with dark/light theme support.

## When to Use

Use this skill any time the user needs a visual representation of how things connect, flow, or are structured in a software system. This includes but is not limited to:

- System or application architecture overviews
- Cloud infrastructure layouts (AWS, Azure, GCP)
- Microservice interaction maps
- Data flow and pipeline diagrams
- Sequence diagrams (component interactions over time)
- State machine visualizations
- Network topology and deployment maps
- Integration diagrams between systems
- DevOps / CI-CD pipeline flows
- Availability and resilience diagrams

## Why HTML Over Mermaid or Static Images

HTML-based diagrams are the right choice when flexibility matters more than speed-of-creation:

- **Text wraps naturally** — no truncation or overflow issues
- **CSS variables enable instant theme switching** — one palette change recolours everything
- **Rich content inside nodes** — embed lists, badges, links, status indicators
- **Responsive by default** — diagrams adapt to any viewport with `clamp()` and grid
- **Version-controllable** — diffs are meaningful, unlike binary images
- **Interactive** — hover effects, theme toggles, clickable elements are trivial to add

## Architecture

Each diagram is a **single self-contained HTML file** with all CSS and JS inline. No build step, no dependencies. Open it directly in a browser.

### Key Principles

- **Single file** — everything in one HTML file for portability
- **No frameworks** — vanilla HTML, CSS, and minimal JS only
- **Dark theme default with light toggle** — dual-theme via CSS variables and `html.light-mode` class
- **CSS variables everywhere** — never use raw hex in component markup; always `var(--name)` or `color-mix()`
- **`clamp()` for all sizing** — every font-size, padding, margin, and gap uses `clamp(min, preferred, max)`
- **HTML nodes, CSS connectors** — nodes are `<div>` elements; connectors use CSS gradients and borders; SVG only when unavoidable

## Diagram Type Selection

Choose the layout and building blocks based on what the user is trying to communicate:

| Diagram Type | Layout | Key Building Blocks |
|---|---|---|
| System Architecture | Multi-column grid (3-col) | System boundary, nodes, connectors, detail panels |
| Application Architecture | Vertical stack | Layer bands, nested boundaries, internal grids |
| Cloud Architecture | Multi-column with nested boundaries | Grouped nodes, boundary labels, spawn relationships |
| Integration Diagram | Source → System → Target (3-col) | Connector lines with arrows, grouped source/target blocks |
| Deployment Diagram | Grid with nested containers | Host containers, spawn relationships, status indicators |
| Network Diagram | Grid with connector lines | Bidirectional connectors, zone boundaries, protocol labels |
| Data Flow Diagram | Left-to-right linear flow | Process nodes, data stores, labeled connectors |
| Sequence Diagram | Vertical with participant columns | Lifeline columns, message arrows, activation bars, step numbers |
| State Diagram | Grid or free-form | State nodes, transition arrows (bidirectional), initial/final markers |
| DevOps / Pipeline | Horizontal linear stages | Stage containers, step indicators, status badges |
| Availability / Resilience | Grid with redundancy | Replica indicators, failover connectors, health dots |

## Design System

Read [references/design-system.md](references/design-system.md) for the full CSS variable palette (dark + light themes), typography scale, and component styling details.

The essentials:

- **Surfaces**: `--bg-body`, `--bg-panel`, `--bg-card`, `--bg-main` — layered depth
- **Borders**: `--border-subtle`, `--border-card`, `--border-panel` — three intensity levels
- **Text**: `--text-primary` → `--text-faint` — five-level hierarchy
- **Accents**: `--accent-pink` (primary), `--accent-purple`, `--accent-blue`, `--accent-green`, `--accent-teal`, `--accent-indigo`, `--accent-amber`, `--accent-sky` — semantic role colours
- **Light mode**: Every accent has a darker variant for legibility on white; defined in `html.light-mode`

## Building Blocks Catalog

The full catalog with HTML/CSS code snippets is in [references/building-blocks.md](references/building-blocks.md). Below is a summary of what each block does and when to use it.

### Structural Elements

| Block | Purpose | When to Use |
|---|---|---|
| **Page Skeleton** | Full HTML page with inline CSS/JS, theme toggle, footer | Every diagram — always start here |
| **Diagram Layout** | Top-level CSS grid (1/2/3-column variants) | Every diagram — choose columns based on type |
| **System Boundary** | Accented-border wrapper with gradient title | Wrapping the primary system being diagrammed |
| **Nested Boundary** | Dashed-border wrapper with floating label | VPCs, clusters, zones, namespaces — any logical grouping inside a system |
| **Layer Band** | Full-width horizontal band with label | Application layers (presentation → logic → data) |
| **Host Container** | Box containing deployed artifacts | Deployment diagrams — servers, VMs, containers |

### Component Elements

| Block | Purpose | When to Use |
|---|---|---|
| **Node** | Standard component card (title + description) | Services, APIs, databases, any named component |
| **Grouped Node Block** | Visually groups related nodes with a category label | "Event Sources", "External APIs", clusters of similar things |
| **Extensibility Placeholder** | Dashed-border, faded node for future items | Signalling "more can be added here" |
| **Chip / Tag** | Small pill-shaped inline labels | Listing features, endpoints, names inside a node |
| **Badge** | Compact technology or status label | Labeling tech stack, runtime info, versions |
| **Status Indicator** | Coloured dot (green/amber/red) on a node | Health status, deploy state, availability |
| **Icon-Enhanced Node** | Emoji icon inline or in a gradient circle | Visually categorizing important components at a glance |
| **Service Strip** | Compact horizontal bar for endpoints/layers | API routes, queue names, internal layers within a boundary |

### Connection Elements

| Block | Purpose | When to Use |
|---|---|---|
| **Gradient Line Connector** | Horizontal line with label + CSS triangle arrow | Connecting source/target columns to the main system |
| **Bidirectional Connector** | Arrows on both ends with a centered label | Peer-to-peer, request/response, two-way data flow |
| **Down Arrow / Flow Indicator** | `▾ label ▾` vertical cue | Showing flow direction between stacked sections |
| **Connector Strip** | Labeled horizontal strip between vertical sections | Clarifying what connects to what (e.g., "both runtimes connect to ↓") |
| **Spawn / Dependency** | Dashed border + downward arrow | One component spawning/creating another |
| **Failover Connector** | Dashed line with "failover" label | Resilience diagrams — secondary/backup paths |

### Information Display Elements

| Block | Purpose | When to Use |
|---|---|---|
| **Detail Panel** | Rich sidebar panel with coloured title + dot-prefixed items | Deep-dive information that doesn't fit in a node |
| **Detail Sub-Section** | Small uppercase header within a detail panel | Splitting a panel into logical groups |
| **Section Divider with Label** | `— or —` or `— then —` separator | Between alternative paths or logical breaks |
| **Column Separator Label** | Label floating on a column border | Explaining the relationship between columns |
| **Legend / Key** | Colour-coded reference table | Any diagram with 4+ node types or colour categories |
| **Annotation / Callout** | Bordered note pointing to a diagram area | Calling attention to a specific design decision |
| **Replica Indicator** | ×N badge on a node | Showing horizontal scaling or redundancy |
| **Footer Note** | Centered text below diagram | Attribution, version, or context |

### Sequence Diagram Elements

| Block | Purpose | When to Use |
|---|---|---|
| **Participant Header** | Column header with service name | Top of each lifeline in a sequence diagram |
| **Lifeline** | Vertical dashed line under a participant | The timeline of each participant |
| **Message Arrow** | Horizontal arrow between lifelines with label | Request, response, or event between participants |
| **Return Arrow** | Dashed horizontal arrow (reverse direction) | Return values or async responses |
| **Activation Bar** | Narrow coloured rectangle on a lifeline | Period when a participant is actively processing |
| **Step Number** | Circled number on a message arrow | Ordering interactions |
| **Self-Call Loop** | Arrow that curves back to the same lifeline | Internal processing or recursive calls |

### State Diagram Elements

| Block | Purpose | When to Use |
|---|---|---|
| **State Node** | Rounded box with internal description/actions | Each state in a state machine |
| **Initial State Marker** | Filled circle | Entry point of a state machine |
| **Final State Marker** | Bullseye (circle within circle) | Terminal/accepting state |
| **Transition Arrow** | Labeled arrow between states | State transitions with trigger/condition labels |

### Pipeline Elements

| Block | Purpose | When to Use |
|---|---|---|
| **Stage Container** | Box representing a pipeline stage | CI/CD stages, data processing steps |
| **Step Indicator** | Numbered circle connecting stages | Ordering pipeline stages |
| **Status Badge** | Pass/fail/pending coloured badge | Build status, test results, deployment state |

## Responsive Behaviour

All diagrams must collapse to single-column on narrow viewports:

```css
@media (max-width: 900px) {
  .diagram { grid-template-columns: 1fr; }
  .connector { display: none; }
  .internal-row, .bottom-row { grid-template-columns: 1fr; }
}
```

## Light Mode

The dual-theme system requires overrides for any element using inline accent colours or gradient lines. For every dark-mode-specific gradient or opacity, provide a corresponding `html.light-mode` selector. See the design system reference for the full override pattern.

## Common Pitfalls

1. **Raw hex in component markup** — always use `var()` or `color-mix()`. Raw hex breaks theming.
2. **Fixed pixel values** — use `clamp()` for everything. Fixed sizes break at different viewports.
3. **Missing light-mode overrides** — if you style an element with an inline gradient or accent opacity, add the `html.light-mode` counterpart or it will be invisible/ugly in light mode.
4. **Overly complex SVG** — prefer CSS grid + HTML nodes. Only reach for SVG when connections truly cannot be expressed with flexbox alignment.
5. **Cramming too much into nodes** — use detail panels in a sidebar column to offload dense information. Keep the main diagram scannable.
6. **No legend** — once a diagram has 4+ colour-coded categories, add a legend. Viewers shouldn't have to guess what colours mean.
