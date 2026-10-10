# Design System Reference

This document defines the full CSS variable palette, typography scale, and theming conventions for architecture-mapper diagrams.

## Table of Contents

- [CSS Variable Palette](#css-variable-palette)
- [Light Mode Overrides](#light-mode-overrides)
- [Typography Scale](#typography-scale)
- [Theme Toggle](#theme-toggle)
- [Light Mode Override Patterns](#light-mode-override-patterns)

## CSS Variable Palette

```css
:root {
  /* ── Surfaces ── */
  --bg-body: #0d0d0d;
  --bg-panel: #141414;
  --bg-card: #181818;
  --bg-chip: #222;
  --bg-main: #111;
  --bg-service: #161616;

  /* ── Borders ── */
  --border-subtle: #1e1e1e;
  --border-card: #252525;
  --border-panel: #2a2a2a;
  --border-chip: #333;

  /* ── Text hierarchy ── */
  --text-primary: #e8e8e8;
  --text-secondary: #bbb;
  --text-muted: #777;
  --text-dim: #555;
  --text-faint: #3a3a3a;
  --text-label: #6b6b6b;

  /* ── Semantic accent colours ── */
  --accent-pink: #ff3cac;    /* Primary accent / titles */
  --accent-purple: #c084fc;  /* Secondary systems */
  --accent-blue: #60a5fa;    /* Networking / runtime A */
  --accent-green: #4ade80;   /* Healthy / isolated / secure */
  --accent-teal: #34d399;    /* External services */
  --accent-indigo: #818cf8;  /* Integrations / tooling */
  --accent-amber: #f59e0b;   /* Warnings / config */
  --accent-sky: #38bdf8;     /* Events / ingestion */

  /* ── Separator label ── */
  --separator-label-bg: #0d0d0d;

  font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
}
```

## Light Mode Overrides

```css
html.light-mode {
  --bg-body: #f5f5f7;
  --bg-panel: #ffffff;
  --bg-card: #f8f8fa;
  --bg-chip: #eee;
  --bg-main: #ffffff;
  --bg-service: #f0f0f2;
  --border-subtle: #e0e0e0;
  --border-card: #d8d8d8;
  --border-panel: #d0d0d0;
  --border-chip: #ccc;
  --text-primary: #1a1a1a;
  --text-secondary: #444;
  --text-muted: #666;
  --text-dim: #888;
  --text-faint: #bbb;
  --text-label: #777;
  --accent-pink: #d6006c;
  --accent-purple: #7c3aed;
  --accent-blue: #2563eb;
  --accent-green: #16a34a;
  --accent-teal: #0d9488;
  --accent-indigo: #4f46e5;
  --accent-amber: #d97706;
  --accent-sky: #0284c7;
  --separator-label-bg: #f5f5f7;
}
```

## Typography Scale

| Element | Size | Weight | Extra Styles |
|---------|------|--------|-------------|
| Diagram title (`h1`) | `1.05rem` | 600 | `text-transform: uppercase; letter-spacing: 0.18em; color: var(--accent-pink)` |
| System boundary title | `1.25rem` | 800 | `text-transform: uppercase; letter-spacing: 0.2em; background: linear-gradient(90deg, var(--accent-pink), var(--accent-purple)); -webkit-background-clip: text; -webkit-text-fill-color: transparent` |
| Group/section label | `0.5–0.58rem` | 700 | `text-transform: uppercase; letter-spacing: 0.12–0.18em; color at ~44% opacity` |
| Node title | `0.75rem` | 700 | `color: var(--text-primary); letter-spacing: 0.06em` |
| Node description | `0.62rem` | 400 | `color: var(--text-label)` |
| Badge/chip text | `0.55–0.58rem` | 600 | Pill shape with `var(--bg-chip)` background |
| Connector label | `0.48–0.58rem` | 400 | Accent colour, `letter-spacing: 0.06–0.1em` |
| Detail panel title | `0.6rem` | 700 | `text-transform: uppercase; letter-spacing: 0.14em` |
| Detail item text | `0.62rem` | 400 | `color: var(--text-muted); line-height: 1.45` |
| Footer note | `0.62rem` | 400 | `color: var(--text-faint); text-align: center` |

## Theme Toggle

Every diagram includes a fixed-position toggle button for dark/light switching:

```css
.theme-toggle {
  position: fixed; top: 16px; right: 16px; z-index: 1000;
  background: var(--bg-panel);
  border: 1px solid var(--border-panel);
  border-radius: 24px; padding: 6px 14px; cursor: pointer;
  font-size: 0.72rem; font-weight: 600; letter-spacing: 0.06em;
  color: var(--text-secondary);
  display: flex; align-items: center; gap: 6px;
  transition: background 0.3s, border-color 0.3s, color 0.3s;
  box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}
.theme-toggle:hover {
  border-color: var(--accent-pink); color: var(--accent-pink);
}
```

```html
<button class="theme-toggle" onclick="toggleTheme()">
  <span id="theme-icon">☾</span>
  <span id="theme-label">Light</span>
</button>
```

```javascript
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
```

## Light Mode Override Patterns

For every element styled with a dark-mode-specific inline gradient or opacity, provide a `html.light-mode` counterpart. Common patterns:

```css
/* Gradient connector lines */
html.light-mode .connector-line {
  background: linear-gradient(90deg, #ccc, color-mix(in srgb, var(--accent-pink) 27%, transparent)) !important;
}

/* CSS triangle arrows */
html.light-mode .arrow-right {
  border-left-color: color-mix(in srgb, var(--accent-pink) 53%, transparent) !important;
}
html.light-mode .arrow-left {
  border-right-color: color-mix(in srgb, var(--accent-purple) 53%, transparent) !important;
}

/* Spawn/dependency boxes */
html.light-mode .spawn-target {
  background: color-mix(in srgb, var(--accent-green) 5%, white);
  border-color: color-mix(in srgb, var(--accent-green) 20%, transparent);
}

/* Group labels */
html.light-mode .node-group-label {
  color: color-mix(in srgb, var(--accent-pink) 40%, transparent);
}

/* System boundary */
html.light-mode .system-boundary {
  border-color: color-mix(in srgb, var(--accent-pink) 33%, transparent);
}
```

The general rule: if an element uses `#rrggbbNN` hex-with-alpha or a specific dark-background gradient, it needs a light-mode override. Elements that only use `var()` references are automatically handled by the variable swap.
