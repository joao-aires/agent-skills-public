# Building Blocks Reference

Complete HTML/CSS code snippets for every building block in the architecture-mapper skill. Organized by category.

## Table of Contents

- [Page Skeleton](#page-skeleton)
- [Diagram Layouts](#diagram-layouts)
- [Structural Elements](#structural-elements)
- [Component Elements](#component-elements)
- [Connection Elements](#connection-elements)
- [Information Display Elements](#information-display-elements)
- [Sequence Diagram Elements](#sequence-diagram-elements)
- [State Diagram Elements](#state-diagram-elements)
- [Pipeline Elements](#pipeline-elements)

---

## Page Skeleton

Every diagram starts with a full HTML page. The structure is always the same: inline styles, a theme toggle button, the diagram content, a footer, and an inline script for theme persistence.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Diagram Title</title>
  <style>
    /* :root variables — see design-system.md */
    /* html.light-mode overrides — see design-system.md */

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background: var(--bg-body);
      font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
      color: var(--text-primary);
      min-height: 100vh;
      display: flex; flex-direction: column; align-items: center;
      padding: 40px 20px 60px;
      transition: background 0.3s, color 0.3s;
    }

    h1 {
      font-size: 1.05rem; font-weight: 600;
      letter-spacing: 0.18em; text-transform: uppercase;
      color: var(--accent-pink);
      margin-bottom: 36px; text-align: center;
    }

    .footer-note {
      margin-top: 42px; font-size: 0.62rem;
      color: var(--text-faint); text-align: center;
      letter-spacing: 0.04em;
    }

    /* ... component styles ... */
    /* ... responsive rules ... */
  </style>
</head>
<body>
  <!-- Theme toggle — see design-system.md for styling -->
  <button class="theme-toggle" onclick="toggleTheme()">
    <span id="theme-icon">☾</span>
    <span id="theme-label">Light</span>
  </button>

  <h1>Diagram Title</h1>
  <div class="diagram">
    <!-- diagram content -->
  </div>
  <p class="footer-note">Subtitle &nbsp;·&nbsp; Context</p>

  <script>
    function toggleTheme() {
      const isLight = document.documentElement.classList.toggle('light-mode');
      document.getElementById('theme-icon').textContent = isLight ? '☽' : '☾';
      document.getElementById('theme-label').textContent = isLight ? 'Dark' : 'Light';
      localStorage.setItem('diagram-theme', isLight ? 'light' : 'dark');
    }
    (function() {
      if (localStorage.getItem('diagram-theme') === 'light') {
        document.documentElement.classList.add('light-mode');
        document.getElementById('theme-icon').textContent = '☽';
        document.getElementById('theme-label').textContent = 'Dark';
      }
    })();
  </script>
</body>
</html>
```

---

## Diagram Layouts

### Three-Column Grid (Sources → System → Details)

Best for: system architecture, integration diagrams, cloud architecture.

```css
.diagram {
  display: grid;
  grid-template-columns: 185px 1fr 310px;
  gap: 0;
  width: 100%; max-width: 1140px;
  position: relative;
}
```

### Two-Column Grid (System + Sidebar)

Best for: application architecture with detail panels, deployment diagrams.

```css
.diagram {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 20px;
  width: 100%; max-width: 960px;
}
```

### Single-Column Vertical Flow

Best for: pipeline/DevOps diagrams, vertical sequence flows.

```css
.diagram {
  display: flex;
  flex-direction: column;
  gap: 16px;
  width: 100%; max-width: 700px;
}
```

### Responsive Collapse

Always include this so diagrams work on narrow viewports:

```css
@media (max-width: 900px) {
  .diagram { grid-template-columns: 1fr; }
  .col-right { border-left: none; padding-left: 0; padding-top: 20px; }
  .connector { display: none; }
  .internal-row, .bottom-row { grid-template-columns: 1fr; }
}
```

---

## Structural Elements

### System Boundary

The primary wrapper for the main system. Uses an accented border and gradient text title.

```css
.system-boundary {
  border: 1.5px solid color-mix(in srgb, var(--accent-pink) 33%, transparent);
  border-radius: 18px;
  background: var(--bg-main);
  padding: 24px;
  position: relative;
}

.system-boundary-title {
  text-align: center;
  font-size: 1.25rem; font-weight: 800;
  letter-spacing: 0.2em; text-transform: uppercase;
  background: linear-gradient(90deg, var(--accent-pink), var(--accent-purple));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 22px;
}
```

### Nested Boundary

For logical groupings inside a system (VPCs, clusters, namespaces). The label floats on the border.

```css
.nested-boundary {
  border: 2px dashed var(--border-panel);
  border-radius: 12px;
  padding: clamp(1.5rem, 2vw, 2rem);
  position: relative; margin: 1rem 0;
}

.nested-boundary-label {
  position: absolute; top: -0.8rem; left: clamp(1rem, 2vw, 1.5rem);
  background: var(--bg-main); padding: 0 0.5rem;
  font-size: 0.5rem; font-weight: 700;
  letter-spacing: 0.16em; text-transform: uppercase;
  color: color-mix(in srgb, var(--accent-pink) 27%, transparent);
}
```

```html
<div class="nested-boundary">
  <span class="nested-boundary-label">Production VPC</span>
  <!-- nodes inside -->
</div>
```

### Layer Band

Full-width horizontal band for application layers (presentation → business logic → data). Stacked vertically.

```css
.layer-band {
  border: 1px solid var(--border-card);
  border-left: 3px solid var(--accent-blue); /* colour per layer */
  border-radius: 10px;
  background: var(--bg-card);
  padding: 14px 18px;
  margin-bottom: 8px;
}

.layer-band-title {
  font-size: 0.6rem; font-weight: 700;
  letter-spacing: 0.12em; text-transform: uppercase;
  margin-bottom: 8px;
  /* colour set per layer */
}

.layer-band-content {
  display: flex; flex-wrap: wrap; gap: 8px;
}
```

```html
<div class="layer-band" style="border-left-color: var(--accent-sky);">
  <div class="layer-band-title" style="color: var(--accent-sky);">Presentation Layer</div>
  <div class="layer-band-content">
    <!-- nodes or chips inside -->
  </div>
</div>
```

### Host Container

For deployment diagrams — represents a server, VM, or container that hosts deployed artifacts.

```css
.host-container {
  border: 1px solid var(--border-panel);
  border-radius: 12px;
  background: var(--bg-panel);
  padding: 14px;
  position: relative;
}

.host-container-label {
  position: absolute; top: -0.7rem; right: 12px;
  background: var(--bg-body); padding: 0 6px;
  font-size: 0.48rem; font-weight: 700;
  letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--text-dim);
}
```

### Internal Sub-Row Grids

Within a system boundary, arrange internal components side by side:

```css
/* Two-column */
.internal-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  padding: 10px 0 0;
}

/* Three-column */
.bottom-row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 14px;
}
```

---

## Component Elements

### Node

The standard component shape. Colour-coded top border denotes category.

```css
.node {
  border: 1px solid var(--border-card);
  border-radius: 10px;
  background: var(--bg-card);
  padding: 12px 14px;
}

.node-title {
  font-size: 0.75rem; font-weight: 700;
  color: var(--text-primary); letter-spacing: 0.06em;
  margin-bottom: 3px;
}

.node-desc {
  font-size: 0.62rem; color: var(--text-label);
  letter-spacing: 0.02em;
}
```

### Grouped Node Block

Groups related nodes with a faint category label.

```css
.node-group {
  border: 1px solid var(--border-card);
  border-radius: 12px;
  background: var(--bg-panel);
  padding: 10px 10px 6px;
  display: flex; flex-direction: column; gap: 8px;
}

.node-group-label {
  font-size: 0.5rem; font-weight: 700;
  letter-spacing: 0.16em; text-transform: uppercase;
  color: color-mix(in srgb, var(--accent-pink) 27%, transparent);
  text-align: center; margin-bottom: 2px;
}
```

### Extensibility Placeholder

Signals "more can be added here" with a dashed border and reduced opacity.

```html
<div class="node" style="border-style: dashed; opacity: 0.45;">
  <div class="node-title" style="color: var(--text-dim);">...</div>
  <div class="node-desc">Future / pluggable</div>
</div>
```

### Chip / Tag

Small pill for inline listing.

```css
.chip {
  font-size: 0.58rem;
  background: var(--bg-chip);
  border: 1px solid var(--border-chip);
  border-radius: 20px;
  padding: 3px 9px;
  color: var(--text-secondary);
  letter-spacing: 0.04em;
}

/* Accent-coloured variant */
.chip.accent {
  border-color: color-mix(in srgb, var(--accent-purple) 33%, transparent);
  color: var(--accent-purple);
}

/* Extensibility placeholder variant */
.chip.extensible {
  border-style: dashed; opacity: 0.45;
}
```

### Badge

Compact technology or status label.

```css
.badge {
  font-size: 0.55rem; font-weight: 600;
  letter-spacing: 0.08em; border-radius: 4px;
  padding: 2px 7px; display: inline-block;
}
```

Set colours per instance: `background: color-mix(in srgb, var(--accent-blue) 15%, transparent); color: var(--accent-blue); border: 1px solid color-mix(in srgb, var(--accent-blue) 30%, transparent);`

### Status Indicator

Coloured dot for health/state on nodes.

```css
.status-dot {
  width: 6px; height: 6px; border-radius: 50%;
  display: inline-block; margin-right: 4px;
}
.status-dot.healthy { background: var(--accent-green); }
.status-dot.warning { background: var(--accent-amber); }
.status-dot.critical { background: var(--accent-pink); }
```

### Replica Indicator

Shows horizontal scaling on a node.

```html
<span class="badge" style="background: color-mix(in srgb, var(--accent-green) 15%, transparent); color: var(--accent-green); border: 1px solid color-mix(in srgb, var(--accent-green) 30%, transparent);">×3</span>
```

### Icon-Enhanced Node

**Inline icon** (most common):
```html
<div class="node-title">📥 &nbsp;Event Ingestion</div>
```

**Emphasis icon** (for central/important components):
```css
.icon-circle {
  width: 52px; height: 52px; border-radius: 50%;
  background: radial-gradient(circle at 40% 40%,
    color-mix(in srgb, var(--accent-pink) 20%, transparent),
    var(--bg-body));
  border: 1.5px solid color-mix(in srgb, var(--accent-pink) 33%, transparent);
  display: flex; align-items: center; justify-content: center;
  font-size: 1.5rem; flex-shrink: 0;
}
```

### Service Strip

Compact horizontal bar for API endpoints, queues, or layers within a boundary.

```css
.service-strip {
  display: flex; gap: 10px; margin-bottom: 16px;
}

.service-strip-item {
  flex: 1;
  background: var(--bg-service);
  border: 1px solid var(--border-card);
  border-radius: 8px; padding: 9px 12px;
}

.service-strip-title {
  font-size: 0.6rem; font-weight: 700;
  letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--accent-pink); opacity: 0.55;
  margin-bottom: 4px;
}

.service-strip-desc {
  font-size: 0.6rem; color: var(--text-dim); line-height: 1.5;
}
```

---

## Connection Elements

### Gradient Line Connector

Horizontal connection between source/target columns and the main system.

```css
.connector {
  display: flex; align-items: center; gap: 6px;
  margin: 2px 0 2px 12px;
}

.connector-line {
  flex: 1; height: 1px;
  background: linear-gradient(90deg, var(--border-chip),
    color-mix(in srgb, var(--accent-pink) 27%, transparent));
}

.connector-label {
  font-size: 0.58rem; letter-spacing: 0.06em;
  color: var(--accent-pink); white-space: nowrap;
}

.arrow-right {
  width: 0; height: 0;
  border-top: 4px solid transparent;
  border-bottom: 4px solid transparent;
  border-left: 6px solid color-mix(in srgb, var(--accent-pink) 53%, transparent);
  flex-shrink: 0;
}

.arrow-left {
  width: 0; height: 0;
  border-top: 4px solid transparent;
  border-bottom: 4px solid transparent;
  border-right: 6px solid color-mix(in srgb, var(--accent-purple) 53%, transparent);
  flex-shrink: 0;
}
```

```html
<div class="connector">
  <div class="connector-line"></div>
  <div class="connector-label">REST</div>
  <div class="arrow-right"></div>
</div>
```

### Bidirectional Connector

For peer-to-peer, request/response, or two-way data flow.

```css
.connector-bidi {
  display: flex; align-items: center; gap: 6px;
  margin: 4px 12px;
}

.connector-bidi-line {
  flex: 1; height: 1px;
  background: var(--border-panel);
}

.connector-bidi-label {
  font-size: 0.52rem; letter-spacing: 0.08em;
  color: var(--text-muted); white-space: nowrap;
  text-transform: uppercase;
}
```

```html
<div class="connector-bidi">
  <div class="arrow-left"></div>
  <div class="connector-bidi-line"></div>
  <div class="connector-bidi-label">gRPC</div>
  <div class="connector-bidi-line"></div>
  <div class="arrow-right"></div>
</div>
```

### Down Arrow / Flow Indicator

Vertical flow cue between stacked sections.

```css
.down-arrow {
  text-align: center;
  font-size: 0.65rem;
  color: color-mix(in srgb, var(--accent-pink) 40%, transparent);
  margin: -6px 0;
  letter-spacing: 0.06em;
}
```

```html
<div class="down-arrow">▾ &nbsp;routes to runtime &nbsp;▾</div>
```

### Connector Strip

Labeled horizontal strip that clarifies what connects to what.

```css
.connector-strip {
  display: flex; align-items: center; gap: 8px;
  padding: 8px 2px 6px;
}

.connector-strip-line {
  flex: 1; height: 1px;
}

.connector-strip-label {
  font-size: 0.48rem; letter-spacing: 0.1em;
  text-transform: uppercase; color: var(--text-faint);
  white-space: nowrap; display: flex; align-items: center; gap: 5px;
}
```

### Spawn / Dependency Relationship

One component creating or spawning another (ephemeral sandbox, triggered deployment).

```css
.spawn-box {
  margin-top: 10px;
  border-top: 1px dashed color-mix(in srgb, var(--accent-green) 13%, transparent);
  padding-top: 8px;
}

.spawn-arrow {
  font-size: 0.5rem; text-align: center;
  color: color-mix(in srgb, var(--accent-green) 33%, transparent);
  letter-spacing: 0.06em; margin-bottom: 4px;
}

.spawn-target {
  display: flex; align-items: center; gap: 8px;
  background: color-mix(in srgb, var(--accent-green) 5%, var(--bg-body));
  border: 1px dashed color-mix(in srgb, var(--accent-green) 20%, transparent);
  border-radius: 6px; padding: 6px 9px;
}

.spawn-target-icon { font-size: 1.1rem; opacity: 0.6; flex-shrink: 0; }

.spawn-target-title {
  font-size: 0.55rem; font-weight: 700;
  color: color-mix(in srgb, var(--accent-green) 53%, transparent);
  letter-spacing: 0.08em; text-transform: uppercase;
}

.spawn-target-desc {
  font-size: 0.5rem; color: var(--text-faint); margin-top: 1px;
}
```

### Failover Connector

Dashed line showing a backup/failover path in resilience diagrams.

```css
.connector-failover {
  display: flex; align-items: center; gap: 6px;
  margin: 4px 12px;
}

.connector-failover-line {
  flex: 1; height: 1px;
  border-top: 1px dashed color-mix(in srgb, var(--accent-amber) 40%, transparent);
}

.connector-failover-label {
  font-size: 0.5rem; letter-spacing: 0.08em;
  color: var(--accent-amber); white-space: nowrap;
  text-transform: uppercase; font-style: italic;
}
```

### Section Divider with Label

Labeled break between alternative paths or logical sections.

```css
.section-divider {
  display: flex; align-items: center; gap: 6px;
  margin: 4px 0;
}

.section-divider-line {
  flex: 1; height: 1px; background: var(--border-subtle);
}

.section-divider-label {
  font-size: 0.48rem; color: var(--text-faint);
  letter-spacing: 0.1em; text-transform: uppercase;
  white-space: nowrap;
}
```

```html
<div class="section-divider">
  <div class="section-divider-line"></div>
  <div class="section-divider-label">or</div>
  <div class="section-divider-line"></div>
</div>
```

---

## Information Display Elements

### Detail Panel

Rich sidebar panel with coloured title and dot-prefixed items.

```css
.detail-panel {
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  background: var(--bg-main);
  padding: 16px 18px;
  margin-bottom: 8px;
}

.detail-panel-title {
  font-size: 0.6rem; font-weight: 700;
  letter-spacing: 0.14em; text-transform: uppercase;
  margin-bottom: 10px;
}

.detail-items {
  display: flex; flex-direction: column; gap: 7px;
}

.detail-item {
  display: flex; align-items: flex-start; gap: 8px;
  font-size: 0.62rem; color: var(--text-muted); line-height: 1.45;
}

.detail-item-dot {
  width: 5px; height: 5px; border-radius: 50%;
  margin-top: 5px; flex-shrink: 0;
}

.detail-item strong {
  color: var(--text-secondary); font-weight: 600;
}
```

### Detail Sub-Section Header

Small uppercase label within a detail panel to divide content.

```html
<div style="font-size:0.5rem; font-weight:700; letter-spacing:0.14em; text-transform:uppercase; color:var(--accent-amber); opacity:0.35; margin-bottom:2px;">
  Sub-Section Title
</div>
```

### Column Separator Label

Label floating on the vertical border between columns.

```css
.separator-label {
  position: absolute; top: 0; left: -1px;
  transform: translateX(-50%);
  background: var(--separator-label-bg); padding: 3px 0;
  display: flex; flex-direction: column; align-items: center; gap: 4px;
}

.separator-label span {
  font-size: 0.46rem; font-weight: 700;
  letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--border-panel);
  background: var(--separator-label-bg); padding: 2px 5px;
  border: 1px solid var(--border-subtle); border-radius: 4px;
}
```

### Legend / Key

Colour-coded reference for diagrams with multiple node categories.

```css
.legend {
  display: flex; flex-wrap: wrap; gap: 12px;
  padding: 10px 14px;
  border: 1px solid var(--border-subtle);
  border-radius: 8px;
  background: var(--bg-panel);
  margin-top: 16px;
}

.legend-title {
  font-size: 0.5rem; font-weight: 700;
  letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--text-dim);
  width: 100%; margin-bottom: 4px;
}

.legend-item {
  display: flex; align-items: center; gap: 6px;
  font-size: 0.55rem; color: var(--text-muted);
}

.legend-swatch {
  width: 12px; height: 3px; border-radius: 2px;
  flex-shrink: 0;
}
```

```html
<div class="legend">
  <div class="legend-title">Legend</div>
  <div class="legend-item">
    <div class="legend-swatch" style="background: var(--accent-blue);"></div>
    Core Services
  </div>
  <div class="legend-item">
    <div class="legend-swatch" style="background: var(--accent-purple);"></div>
    External Systems
  </div>
</div>
```

### Annotation / Callout

A bordered note that calls attention to a specific part of the diagram.

```css
.callout {
  border: 1px solid color-mix(in srgb, var(--accent-amber) 30%, transparent);
  border-left: 3px solid var(--accent-amber);
  border-radius: 6px;
  background: color-mix(in srgb, var(--accent-amber) 5%, var(--bg-body));
  padding: 8px 12px;
  font-size: 0.58rem; color: var(--text-muted);
  line-height: 1.5; margin: 8px 0;
}

.callout strong { color: var(--accent-amber); }
```

---

## Sequence Diagram Elements

Sequence diagrams use a fundamentally different layout: vertical lifelines with horizontal message arrows between them.

### Layout

```css
.sequence-diagram {
  display: flex; gap: 0;
  position: relative;
  padding-top: 60px; /* space for participant headers */
}

.participant-column {
  flex: 1;
  display: flex; flex-direction: column;
  align-items: center;
  position: relative;
  min-width: clamp(100px, 15vw, 180px);
}
```

### Participant Header

```css
.participant-header {
  background: var(--bg-card);
  border: 1px solid var(--border-card);
  border-top: 3px solid var(--accent-blue); /* colour per participant */
  border-radius: 8px;
  padding: 8px 14px;
  font-size: 0.7rem; font-weight: 700;
  color: var(--text-primary);
  letter-spacing: 0.06em;
  text-align: center;
  z-index: 2; position: relative;
}
```

### Lifeline

```css
.lifeline {
  width: 1px;
  background: repeating-linear-gradient(
    to bottom,
    var(--border-panel) 0px,
    var(--border-panel) 6px,
    transparent 6px,
    transparent 12px
  );
  flex: 1;
  min-height: 40px;
}
```

### Activation Bar

A narrow coloured rectangle on a lifeline showing active processing.

```css
.activation-bar {
  width: 10px;
  background: color-mix(in srgb, var(--accent-blue) 25%, transparent);
  border: 1px solid color-mix(in srgb, var(--accent-blue) 40%, transparent);
  border-radius: 3px;
  position: absolute;
  left: 50%; transform: translateX(-50%);
  z-index: 1;
  /* top and height set per instance */
}
```

### Message Arrow

Horizontal arrow between lifelines. Positioned absolutely over the sequence diagram.

```css
.message {
  position: absolute;
  display: flex; align-items: center;
  z-index: 3;
  /* left, width, top set per instance */
}

.message-line {
  flex: 1; height: 1px;
  background: var(--text-muted);
}

.message-line.dashed {
  border-top: 1px dashed var(--text-dim);
  background: none; height: 0;
}

.message-label {
  position: absolute; top: -16px;
  font-size: 0.55rem; color: var(--text-secondary);
  white-space: nowrap;
  left: 50%; transform: translateX(-50%);
}

.message-arrow-right {
  width: 0; height: 0;
  border-top: 4px solid transparent;
  border-bottom: 4px solid transparent;
  border-left: 6px solid var(--text-muted);
}

.message-arrow-left {
  width: 0; height: 0;
  border-top: 4px solid transparent;
  border-bottom: 4px solid transparent;
  border-right: 6px solid var(--text-dim);
}
```

### Step Number

Circled number on a message for ordering interactions.

```css
.step-number {
  width: 18px; height: 18px;
  border-radius: 50%;
  background: var(--accent-pink);
  color: var(--bg-body);
  font-size: 0.5rem; font-weight: 700;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
  position: absolute; left: -24px; top: -9px;
}
```

### Self-Call Loop

Arrow that curves back to the same lifeline.

```css
.self-call {
  position: absolute;
  border: 1px solid var(--text-muted);
  border-left: none;
  border-radius: 0 6px 6px 0;
  width: 30px;
  z-index: 3;
  /* top and height set per instance */
}

.self-call-label {
  position: absolute; right: -4px; top: 50%;
  transform: translateX(100%) translateY(-50%);
  font-size: 0.5rem; color: var(--text-muted);
  white-space: nowrap;
}
```

---

## State Diagram Elements

### State Node

Rounded rectangle representing a state, with optional internal action labels.

```css
.state-node {
  border: 1px solid var(--border-panel);
  border-radius: 20px;
  background: var(--bg-card);
  padding: 12px 18px;
  text-align: center;
  min-width: clamp(120px, 14vw, 200px);
}

.state-node-title {
  font-size: 0.75rem; font-weight: 700;
  color: var(--text-primary); letter-spacing: 0.06em;
  margin-bottom: 4px;
}

.state-node-actions {
  font-size: 0.55rem; color: var(--text-dim);
  border-top: 1px solid var(--border-subtle);
  padding-top: 6px; margin-top: 6px;
  text-align: left; line-height: 1.5;
}
```

### Initial State Marker

Filled circle indicating the entry point.

```css
.state-initial {
  width: 16px; height: 16px;
  border-radius: 50%;
  background: var(--text-primary);
}
```

### Final State Marker

Bullseye (circle within circle) indicating the terminal state.

```css
.state-final {
  width: 20px; height: 20px;
  border-radius: 50%;
  border: 2px solid var(--text-primary);
  display: flex; align-items: center; justify-content: center;
}

.state-final-inner {
  width: 10px; height: 10px;
  border-radius: 50%;
  background: var(--text-primary);
}
```

### Transition Arrow

Labeled connection between states. Use CSS-only for horizontal/vertical, SVG for diagonal.

```css
.transition {
  display: flex; align-items: center; gap: 4px;
}

.transition-line {
  flex: 1; height: 1px;
  background: var(--text-muted);
}

.transition-label {
  font-size: 0.5rem; color: var(--accent-purple);
  white-space: nowrap; letter-spacing: 0.04em;
  padding: 0 4px;
  background: var(--bg-body);
}
```

---

## Pipeline Elements

### Stage Container

Box representing a pipeline stage with a coloured top accent.

```css
.stage {
  border: 1px solid var(--border-card);
  border-top: 3px solid var(--accent-blue); /* colour per stage */
  border-radius: 10px;
  background: var(--bg-card);
  padding: 14px;
  text-align: center;
  flex: 1;
}

.stage-title {
  font-size: 0.65rem; font-weight: 700;
  letter-spacing: 0.1em; text-transform: uppercase;
  margin-bottom: 8px;
}

.stage-items {
  display: flex; flex-direction: column; gap: 4px;
}

.stage-item {
  font-size: 0.58rem; color: var(--text-muted);
  padding: 3px 0;
  border-bottom: 1px solid var(--border-subtle);
}
.stage-item:last-child { border-bottom: none; }
```

### Pipeline Layout

Stages connected by arrows in a horizontal flow.

```css
.pipeline {
  display: flex; align-items: stretch; gap: 0;
}

.pipeline-arrow {
  display: flex; align-items: center;
  padding: 0 8px;
  color: var(--text-faint);
  font-size: 1.2rem;
}
```

```html
<div class="pipeline">
  <div class="stage" style="border-top-color: var(--accent-sky);">
    <div class="stage-title" style="color: var(--accent-sky);">Build</div>
    <div class="stage-items">
      <div class="stage-item">Compile</div>
      <div class="stage-item">Lint</div>
    </div>
  </div>
  <div class="pipeline-arrow">→</div>
  <div class="stage" style="border-top-color: var(--accent-indigo);">
    <div class="stage-title" style="color: var(--accent-indigo);">Test</div>
    <div class="stage-items">
      <div class="stage-item">Unit</div>
      <div class="stage-item">Integration</div>
    </div>
  </div>
  <div class="pipeline-arrow">→</div>
  <div class="stage" style="border-top-color: var(--accent-green);">
    <div class="stage-title" style="color: var(--accent-green);">Deploy</div>
    <div class="stage-items">
      <div class="stage-item">Staging</div>
      <div class="stage-item">Production</div>
    </div>
  </div>
</div>
```

### Step Indicator

Numbered circle connecting pipeline stages.

```css
.step-indicator {
  width: 22px; height: 22px;
  border-radius: 50%;
  background: var(--bg-panel);
  border: 1.5px solid var(--border-panel);
  color: var(--text-muted);
  font-size: 0.55rem; font-weight: 700;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}

.step-indicator.active {
  border-color: var(--accent-pink);
  color: var(--accent-pink);
}

.step-indicator.complete {
  background: var(--accent-green);
  border-color: var(--accent-green);
  color: var(--bg-body);
}
```

### Status Badge

Pass/fail/pending indicator for pipeline steps.

```css
.status-badge {
  font-size: 0.48rem; font-weight: 700;
  letter-spacing: 0.08em; text-transform: uppercase;
  padding: 2px 8px; border-radius: 4px;
  display: inline-block;
}

.status-badge.pass {
  background: color-mix(in srgb, var(--accent-green) 15%, transparent);
  color: var(--accent-green);
  border: 1px solid color-mix(in srgb, var(--accent-green) 30%, transparent);
}

.status-badge.fail {
  background: color-mix(in srgb, var(--accent-pink) 15%, transparent);
  color: var(--accent-pink);
  border: 1px solid color-mix(in srgb, var(--accent-pink) 30%, transparent);
}

.status-badge.pending {
  background: color-mix(in srgb, var(--accent-amber) 15%, transparent);
  color: var(--accent-amber);
  border: 1px solid color-mix(in srgb, var(--accent-amber) 30%, transparent);
}
```
