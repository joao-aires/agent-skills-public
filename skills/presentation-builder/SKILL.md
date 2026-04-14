---
name: presentation-builder
description: "Build single-file HTML presentations with a dark theme, scroll-driven slides, responsive card grids, and reveal animations. Optional addons extend the base with features like a vertical timeline navigation. Use when the user asks to: create a presentation, build a slide deck, add or edit slides, fix slide layout or overflow issues, add timeline events, create card grids, add reveal animations, embed images or tweets, fix fullscreen rendering, or any task involving HTML presentation creation and refinement."
metadata:
  version: "1.0"
---

# Presentation Builder

Create polished, single-file HTML slide presentations optimised for widescreen and fullscreen delivery.

## When to Use

Use this skill when asked to:

- create a new presentation from scratch
- add, edit, reorder, or remove slides
- fix layout, overflow, or fullscreen rendering issues
- add or modify optional addons (e.g. the vertical timeline navigation)
- create card grids, comparison layouts, or diagrams
- embed images, tweets, or interactive elements
- refine typography, spacing, or visual consistency across slides

## Architecture Overview

Each presentation is a **single `index.html` file** containing all markup, CSS, and JavaScript inline. No build step is required. Assets (images) live in an `attachments/` directory alongside the HTML file.

```text
presentation/
  index.html          # The entire presentation
  attachments/         # Images referenced by slides
    3.png
    ...
```

Self-contained addon reference files live under `references/addons/`. Each addon bundles the CSS, HTML, and JS required to extend the base skeleton.

### Key Technical Decisions

- **Single file** — everything in one HTML file for portability
- **No frameworks** — vanilla HTML, CSS, and JS only
- **Dark theme** — dark background with light text, always
- **Vertical scroll** — slides are full-viewport `<section>` elements stacked vertically
- **Addon-based extensions** — optional features (e.g. timeline navigation) are self-contained addon files that merge into the base skeleton
- **Responsive by default** — `clamp()` throughout; slides work on most screens, optimised for widescreen (16:9 to ultrawide)
- **Fullscreen support** — press `F` to toggle; dense slides use `fit-wide` auto-scaling

## Design System

### Colour Palette

```css
:root {
  --bg: #0a0a12;
  --surface: #12121e;
  --surface-alt: #181828;
  --border: #1e1e30;
  --text: #e8e8f0;
  --text-muted: #8888a0;
  --accent: #4ecdc4; /* Teal — primary accent */
  --accent-dim: rgba(78, 205, 196, 0.15);
  --red: #ff6b6b;
  --yellow: #ffd93d;
  --purple: #a78bfa;
  --blue: #60a5fa;
  --font-sans: "Inter", system-ui, sans-serif;
  --font-mono: "JetBrains Mono", monospace;
}
```

Use named CSS variables everywhere. Never use raw hex colours in slide markup.

### Typography

- **Font**: Inter (sans-serif) for all text, JetBrains Mono for code and monospace elements
- **Headings**: Use `clamp()` for all font sizes — specify `(min, preferred, max)`
- **h1**: Title slides only. `clamp(2.4rem, 4.5vw, 5rem)`, weight 700
- **h2**: Slide titles. `clamp(1.5rem, 2.8vw, 3.2rem)`, weight 600
- **h3**: Eyebrow/section labels above `h2`. Uppercase, letter-spacing `.08em`, accent colour
- **Body text**: `clamp(.88rem, 1.3vw, 1.4rem)` for bullet lists
- **Strong text inside bullets**: Use `color: var(--accent)` for emphasis

### Spacing

- Use `clamp()` for all padding, margins, and gaps
- Pattern: `clamp(min, preferred-vw-or-vh, max)`
- Never use fixed pixel values for layout spacing

### Customisation

The design system above defines **defaults**, not constraints. When the user requests a different visual style or new components, adapt accordingly:

**Colour changes**: If the user wants a different accent colour, light theme, or custom palette — update the `:root` CSS variables. All components use variables, so a single change propagates everywhere. Keep the variable naming convention (`--accent`, `--surface`, etc.) and update the values.

**Typography changes**: If the user wants a different font, weight scheme, or sizing — update the `--font-sans` / `--font-mono` variables, adjust the `clamp()` values, and update the Google Fonts `<link>`. The `clamp(min, preferred, max)` pattern should always be used regardless of the specific font.

**New components**: When the user asks for a component that doesn't exist in the catalog (e.g. a comparison table, a code block, a quote callout, a stat counter) — create it inline following these rules:
1. Use CSS variables for colours — never hardcode hex values
2. Use `clamp()` for all sizing and spacing
3. Use the existing border-radius (`8px`–`12px`), background (`var(--surface)`), and border (`var(--border)`) patterns for visual consistency
4. Apply `.reveal` or `.reveal-stagger` for scroll animation
5. Add the component's CSS in the slide-specific CSS section or, if reused across slides, in the main `<style>` block

**Layout modifications**: If the user wants multi-column layouts, split views, or non-standard arrangements — build them with CSS grid or flexbox inline. Keep the `.scene` / `.scene-inner` wrapper structure and add layout rules either as inline styles or slide-specific CSS.

**Slide transitions or effects**: The default is scroll-driven reveal. If the user wants different animations (e.g. fade-in from left, scale-up, typewriter) — create new CSS classes following the `.reveal` pattern: hidden by default, `.visible` state applied by the existing `IntersectionObserver`.

The principle: **match the user's vision while maintaining the technical conventions** (single file, CSS variables, `clamp()`, responsive behaviour, no frameworks).

## Slide Structure

### Basic Slide

Every slide is a `<section class="scene">` containing a `<div class="scene-inner">`:

```html
<!-- ================================================================
 N · SLIDE TITLE (for reference)
 ================================================================ -->
<section class="scene" id="s-unique-id">
  <div class="scene-inner">
    <h3>Section Label</h3>
    <h2 class="reveal">Slide Title</h2>
    <!-- content -->
  </div>
</section>
```

Rules:

- Every slide gets a unique `id` prefixed with `s-`
- When using the timeline addon, add `data-tl` to link the slide to its timeline event
- Always include a numbered HTML comment block above each slide for navigation
- `h3` is the section eyebrow (e.g., "The impact", "Tips & tricks"), `h2` is the slide title

### Slide Types and Classes

| Class                        | Purpose                                                   |
| ---------------------------- | --------------------------------------------------------- |
| `.scene`                     | Base slide — vertically centred content                   |
| `.scene.fit-wide`            | Dense slides — enables JS auto-scaling for fullscreen     |
| `.scene.fullscreen-balanced` | Card-heavy slides — uses flexbox layout in wide viewports |

**`.fit-wide`** enables `fitWideSlides()` JS that scales `.scene-inner` down (min 0.82×) when content overflows the viewport. Use for slides with lots of content that must be visible without scrolling.

**`.fullscreen-balanced`** adds CSS media queries that make `.scene-inner` flex-column and expand card grids. Use for slides with 2–4 cards that should fill the viewport evenly.

### Component Catalog

All components below are available in the base skeleton. Choose the component that best fits your content type.

#### Title Slide — `.title-slide`

**When to use**: First slide of every presentation. Sets the topic, author, and context.

```html
<section class="scene" id="s-title">
    <div class="scene-inner title-slide reveal">
        <span class="tag">EVENT_TAG · DATE</span>
        <h1>Presentation Title</h1>
        <p class="subtitle">A supporting one-liner that frames the talk</p>
        <div class="meta">Author Name · Role</div>
    </div>
</section>
```

Sub-elements:

- **`.tag`** — monospace label above the title (event name, date, category). Use for situational context the audience needs before reading the title.
- **`.subtitle`** — lighter, thinner text below `h1`. One sentence max. Use to qualify or narrow the title's scope.
- **`.meta`** — small muted text for author, role, team, or date. Appears below the subtitle.

#### Closing / Q&A Slide — `.qa-slide`

**When to use**: Last slide. Signals the end and opens the floor.

```html
<section class="scene" id="s-closing">
    <div class="scene-inner qa-slide reveal">
        <h2>Q&A</h2>
        <p>Thank you!</p>
    </div>
</section>
```

Centre-aligned, large heading. Keep it minimal — no bullets or cards.

#### Bullet Lists — `.bullet-list`

**When to use**: Presenting 3–5 key points, arguments, or takeaways in sequence. The default choice when content is narrative or explanatory.

```html
<ul class="bullet-list reveal">
  <li><strong>Bold lead phrase</strong> — supporting detail</li>
  <li>
    Regular bullet point
    <ul class="sub">
      <li>Sub-bullet with <strong>emphasis</strong></li>
      <li>Another sub-point — use <code>–</code> marker</li>
    </ul>
  </li>
</ul>
```

Conventions:
- Bullets use `›` markers (via CSS `::before`), sub-bullets use `–`
- Keep main bullets to 3–5 per slide
- `<strong>` inside bullets renders in `var(--accent)` colour

#### Card Grids — `.card-grid` + `.card`

**When to use**: Comparing features, tools, options, or categories side by side. Best for 2–6 items of roughly equal weight that the audience should scan in parallel rather than read in order.

```html
<div class="card-grid reveal-stagger">
  <div class="card" style="border-top:3px solid var(--accent)">
    <h4>Card Title</h4>
    <p>Card description text.</p>
  </div>
  <div class="card" style="border-top:3px solid var(--purple)">
    <h4>Another Card</h4>
    <ul>
      <li><strong>Bold item</strong> — detail</li>
      <li>Another item</li>
    </ul>
  </div>
</div>
```

Conventions:
- Use `border-top: 3px solid var(--colour)` for visual distinction between cards
- Card bullets use `›` markers (same as pillar cards)
- Keep card content concise — 3–5 bullet points max
- Cards auto-fit: `grid-template-columns: repeat(auto-fit, minmax(clamp(200px, 18vw, 300px), 1fr))`
- For 5+ cards or dense content, add `fit-wide` to the slide and use `fullscreen-balanced` for 2–4 cards

#### Pillar Cards — `.pillar-grid` + `.pillar-card`

**When to use**: Presenting strategic pillars, principles, or structured categories that each have a title, optional tagline, and bullet details. Prefer over plain cards when each item needs a clear header + subtitle hierarchy.

```html
<div class="pillar-grid reveal-stagger">
  <div class="pillar-card" style="border-top:3px solid var(--accent)">
    <div class="pillar-card-header">
      <h4 style="color:var(--accent)">Pillar Name</h4>
    </div>
    <div class="pillar-subtitle">Tagline or subtitle</div>
    <ul class="pillar-items">
      <li>Bullet with <strong>emphasis</strong></li>
      <li>Another point</li>
    </ul>
  </div>
</div>
```

Pillar cards are the **preferred visual reference** for informational card styling. When normalising card styles across a deck, use pillar cards as the benchmark:
- Lighter background: `rgba(255, 255, 255, .02)`
- Softer borders: `rgba(255, 255, 255, .08)`
- 12px border-radius
- `›` bullet markers in accent colour
- Fixed 3-column grid (`repeat(3, 1fr)`) — adjust count if needed

#### Timeline Event Slides — `.event-slide`

**When to use**: A slide anchored to a specific date or milestone. Typically used with the timeline addon but works standalone for any chronological narrative. Pair with the event marker (coloured dot + vertical line) to visually anchor the date.

```html
<section class="scene" id="s-event-name" data-tl="s-event-name">
  <div class="scene-inner">
    <div class="event-slide reveal">
      <div class="event-marker">
        <div class="edot" style="background:var(--accent)"></div>
        <div class="eline" style="background:var(--accent)"></div>
      </div>
      <div class="event-body">
        <span class="year">Month Year</span>
        <h2>Event Title</h2>
        <ul class="bullet-list">
          <li>Key point about this event</li>
        </ul>
        <img class="event-img" src="attachments/image.png" alt="Description" />
      </div>
    </div>
  </div>
</section>
```

Conventions:
- Colour the `.edot` and `.eline` with the appropriate theme colour for the event
- `<span class="year">` is monospace, muted — shows "Month Year" above the title
- `<img class="event-img">` is optional — for screenshots or diagrams related to the event

#### Image Cards with Hover Preview — `.card.has-preview`

**When to use**: Cards that reference a tool, page, or visual artefact the audience may want to see. The preview image appears on hover/focus, useful for demo screenshots or UI references without cluttering the slide.

```html
<div class="card has-preview" tabindex="0">
  <h4>Card Title</h4>
  <p>Description</p>
  <div class="card-preview">
    <img src="attachments/preview.png" alt="Preview" />
    <div class="card-preview-caption">Caption text</div>
  </div>
</div>
```

Conventions:
- Add `tabindex="0"` so keyboard users can trigger the preview
- For wide/fullscreen, position previews to the right side with slide-specific CSS media queries

#### Tweet Embeds

**When to use**: Quoting a public statement, announcement, or reaction from social media. Adds credibility and a visual break from bullets/cards.

```html
<blockquote class="twitter-tweet" data-theme="dark">
  <p lang="en" dir="ltr">Tweet text...</p>
  &mdash; Author (@handle)
  <a href="https://twitter.com/...">Date</a>
</blockquote>
```

Conventions:
- The Twitter widgets script is loaded **once globally** at the end of the file — never duplicate it inside individual slides
- Always use `data-theme="dark"` to match the presentation theme

#### Eyebrow + Title Pattern — `h3` + `h2`

**When to use**: Every content slide. The `h3` eyebrow provides section continuity across slides (e.g. "The problem", "Our approach", "Results") while `h2` is the unique slide title.

```html
<h3>Section Label</h3>
<h2 class="reveal">Slide Title</h2>
```

Conventions:
- `h3` is uppercase, accent-coloured, letter-spaced — acts as a section grouping label
- `h2` is the main title — apply `.reveal` for scroll animation
- Keep the same `h3` across slides that belong to the same narrative section

#### Diagrams — inline SVG or HTML/CSS

**When to use**: Showing architecture, flows, relationships, or processes that are clearer as a visual than as bullets or cards. Use when the audience needs to see how things connect rather than just what they are.

Diagrams are built inline using either **HTML/CSS boxes with flexbox/grid** or **inline SVG**. Never use external diagram tools or images for diagrams that could be drawn with code — keeps them resolution-independent and theme-consistent.

**HTML/CSS approach** (preferred for box-and-arrow layouts):

```html
<div class="diagram reveal" style="display:flex; gap:clamp(.5rem,1vw,1.2rem); align-items:center; justify-content:center; flex-wrap:wrap;">
    <div style="background:var(--surface); border:1px solid var(--border); border-radius:8px; padding:clamp(.5rem,.8vw,1rem); text-align:center; min-width:clamp(100px,12vw,180px);">
        <div style="font-size:clamp(.7rem,.9vw,1rem); font-weight:600; color:var(--accent);">Box A</div>
        <div style="font-size:clamp(.6rem,.75vw,.85rem); color:var(--text-muted);">Description</div>
    </div>
    <div style="color:var(--text-muted); font-size:clamp(.8rem,1vw,1.2rem);">→</div>
    <div style="background:var(--surface); border:1px solid var(--border); border-radius:8px; padding:clamp(.5rem,.8vw,1rem); text-align:center; min-width:clamp(100px,12vw,180px);">
        <div style="font-size:clamp(.7rem,.9vw,1rem); font-weight:600; color:var(--purple);">Box B</div>
        <div style="font-size:clamp(.6rem,.75vw,.85rem); color:var(--text-muted);">Description</div>
    </div>
</div>
```

**Inline SVG approach** (for complex paths, arrows, or non-linear layouts):

```html
<svg class="reveal" viewBox="0 0 600 200" style="width:100%; max-width:clamp(500px,50vw,800px); height:auto;">
    <rect x="10" y="60" width="150" height="80" rx="8"
          fill="var(--surface)" stroke="var(--border)" stroke-width="1"/>
    <text x="85" y="105" text-anchor="middle"
          fill="var(--accent)" font-family="var(--font-sans)" font-size="14" font-weight="600">Service A</text>
    <line x1="160" y1="100" x2="250" y2="100"
          stroke="var(--text-muted)" stroke-width="1.5" marker-end="url(#arrow)"/>
    <rect x="250" y="60" width="150" height="80" rx="8"
          fill="var(--surface)" stroke="var(--border)" stroke-width="1"/>
    <text x="325" y="105" text-anchor="middle"
          fill="var(--purple)" font-family="var(--font-sans)" font-size="14" font-weight="600">Service B</text>
    <defs>
        <marker id="arrow" viewBox="0 0 10 10" refX="10" refY="5"
                markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="var(--text-muted)"/>
        </marker>
    </defs>
</svg>
```

Conventions:
- Use CSS variables for all colours — `var(--surface)`, `var(--border)`, `var(--accent)`, etc.
- Use `clamp()` for sizing and spacing in the HTML/CSS approach
- Use `viewBox` for SVGs so they scale responsively
- Arrows: use `→` character for simple flows, SVG `<marker>` for complex connectors
- Keep diagrams to 3–6 nodes — more than that needs a dedicated slide or simplification
- Apply `.reveal` to the diagram container for scroll animation
- Colour-code nodes by role using the theme palette (accent for primary, purple for secondary, blue for tertiary, etc.)

## Reveal Animations

Two animation systems:

1. **`.reveal`** — single element fade-up on scroll
2. **`.reveal-stagger`** — container whose children animate in sequence

```html
<h2 class="reveal">Title fades in</h2>
<div class="card-grid reveal-stagger">
  <!-- Each .card child animates in with staggered delay -->
</div>
```

**Critical**: The stagger system defines explicit `nth-child` delays for children 1–6. A catch-all rule ensures children 7+ are also visible (just without stagger delay). If a grid has more than 6 children, verify they all appear.

The reveal system uses `IntersectionObserver` with a 12% threshold to add the `.visible` class.

## Addons

Addons are **optional, self-contained feature packages** that extend the base presentation skeleton. Each addon lives as a single reference file under `references/addons/<name>.html` containing all the CSS, HTML, and JS needed.

### When to Include an Addon

Include an addon when:

- The user explicitly requests the feature
- The content naturally calls for it (e.g. chronological data → timeline)

Omit when:

- The presentation is short or non-chronological (timeline)
- The user wants a minimal deck

### Addon File Convention

Each addon file contains:

1. **Header comment** — name, purpose, and integration points
2. **CSS section** — styles to merge into `<style>`, plus any `:root` variable additions
3. **HTML section** — markup to insert at the specified location
4. **JS section** — code to merge into the main `<script>` IIFE

Integration points are documented per-addon in the header comment. When applying an addon, merge each section into the corresponding location in the skeleton rather than pasting the addon file verbatim.

### Available Addons

#### Timeline Navigation

**Reference**: [references/addons/timeline.html](references/addons/timeline.html)

A fixed right-side vertical rail with chronological event labels, year markers, SVG leader-line connectors, and progressive disclosure tied to scroll position.

**When to use**: The content is chronological, has 5+ events spanning multiple dates, or the user requests a timeline.

**Integration points** (documented in the file header):

- **`:root` variables** — add `--nav-w` and `--rail-x`
- **`.scene` padding** — add `padding-right: calc(var(--nav-w) + clamp(...))`
- **Slide counter** — shift right by `--nav-w`
- **`<nav>` HTML** — insert before the slide counter
- **`data-tl` attribute** — add to each `<section>` to link slides to events
- **JS** — merge `positionTimeline()`, progressive disclosure, and `updateTimeline()` into the main IIFE; call `updateTimeline(idx)` from the existing scroll handler

**Structure**:

- **Year markers** (centred on rail) — positioned by `data-date`
- **Right-side events** — clickable, linked to slides via `data-target`
- **Left-side events** (`tl-left`) — secondary track, purple-tinted; clickable by default
- **Annotations** (`tl-left tl-secondary`) — non-interactive left-side labels with smaller font, optional `.badge` span
- **"Now" marker** — pulsing accent dot at the current date
- **SVG leader-lines** — curved paths from anchor dots to labels

**Adding a right-side event**:

```html
<div class="tl-event" data-date="YYYY-MM" data-target="s-slide-id">
    <div class="label">Event Name</div>
</div>
```

Optional tint classes: `tl-yellow` (notable), `tl-red` (critical).

**Adding a left-side event**:

```html
<div class="tl-event tl-left" data-date="YYYY-MM" data-target="s-slide-id">
    <div class="label">Left Event</div>
</div>
```

**Adding a non-interactive annotation** (left side, smaller, no click):

```html
<div class="tl-event tl-left tl-secondary" data-date="YYYY-MM">
    <div class="label">Annotation</div><span class="badge">detail</span>
</div>
```

Annotations are revealed progressively based on the nearest preceding event by date. Those dated after all events reveal with the "Now" section.

**Progressive disclosure**: Events are hidden until the viewer scrolls to the linked slide. Prior events stay visible but dimmed; the current event is bright.

**Collision avoidance**: The JS automatically spaces labels to prevent overlap with independent collision resolution for right-side and left-side groups.

## Handling Dense Slides

Dense slides that overflow in fullscreen need **targeted, slide-specific CSS** — never blunt global scaling.

### Strategy

1. Mark the slide with `class="scene fit-wide"` to enable JS auto-scaling
2. Add slide-specific `@media` rules to tighten spacing, font sizes, and grid columns
3. Use two tiers of compaction:
   - Broad tier: `@media (min-width: 1000px) and (min-aspect-ratio: 4/3)` — most desktop/fullscreen sizes
   - Strict tier: `@media (min-width: 1400px) and (min-aspect-ratio: 3/2)` — ultrawide

### Example: Compacting a Card Grid Slide

```css
@media (min-width: 1000px) and (min-aspect-ratio: 4/3) {
  #s-slide-id .scene-inner {
    display: flex;
    flex-direction: column;
    gap: clamp(0.22rem, 0.38vw, 0.38rem);
    overflow: visible;
  }
  #s-slide-id h2 {
    font-size: clamp(1.78rem, 2.2vw, 2.55rem);
    margin-bottom: clamp(0.35rem, 0.7vh, 0.6rem);
  }
  #s-slide-id .card-grid {
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: clamp(0.45rem, 0.7vw, 0.75rem);
    flex: 1;
    min-height: 0;
  }
  #s-slide-id .card {
    padding: clamp(0.68rem, 0.82vw, 0.88rem);
  }
  #s-slide-id .card h4 {
    font-size: clamp(0.76rem, 0.82vw, 0.92rem);
  }
}
```

### Common Overflow Fixes

- Check the stagger animation first — children beyond nth-child(6) may be hidden (opacity: 0)
- Verify elements exist in the DOM before assuming they were deleted
- Add padding-top to `.scene-inner` if eyebrow labels get clipped at the top
- Use `grid-auto-rows: 1fr` and `align-content: stretch` to force uniform card heights

## Keyboard Navigation

Built into every deck:

- **Arrow Down / Right** — next slide
- **Arrow Up / Left** — previous slide
- **F** — toggle fullscreen

## Responsive Behaviour

- **Mobile (< 700px)**: Timeline (if present) hidden, single-column cards, no preview popups
- **Desktop**: Full timeline (if present), multi-column cards, hover previews
- **Fullscreen**: `fitWideSlides()` auto-scales dense slides, fullscreen-balanced slides expand

## Creating a New Presentation

### 1. Scaffold the File

Start with the full HTML skeleton: `<!DOCTYPE html>`, fonts, CSS variables, slide counter, scripts. Load [references/presentation-skeleton.html](references/presentation-skeleton.html) if available, or use an existing presentation as a template.

### 2. Choose Addons

Decide which addons to include based on content. For chronological presentations, integrate the **Timeline Navigation** addon (see [Addons](#addons)). For non-chronological decks, skip this step — the base skeleton is complete on its own.

When integrating an addon, read the addon reference file and merge its CSS, HTML, and JS into the skeleton at the documented integration points.

### 3. Build Slides

Create each slide as a `<section class="scene">` with appropriate `id`, `data-tl`, and content. Use the slide type that best fits the content density.

### 4. Test in Fullscreen

After building, test every slide in fullscreen (`F` key). Fix any overflow with slide-specific media queries. Verify all stagger-animated children are visible.

### 5. Refine

- Ensure card styles are visually consistent (use pillar card style as the reference)
- If using the timeline addon, verify progressive disclosure works correctly
- Check that the slide counter shows the correct total
- Test keyboard navigation end-to-end

## Common Pitfalls and Lessons Learned

1. **Stagger animations hide children > 6**: The `.reveal-stagger` CSS only had explicit `nth-child` rules for items 1–6. Always include a catch-all `.reveal-stagger.visible > * { opacity: 1; transform: translateY(0); }` rule.

2. **Timeline secondary annotations after the last event stay hidden** (timeline addon): If an annotation's `data-date` is later than all events, the fallback reveal index must use `nowRevealIdx` instead of `Infinity`.

3. **Don't duplicate the Twitter widgets script**: It's loaded once globally at the end of `<body>`.

4. **Dense slides need targeted CSS, not blunt global scaling**: Create slide-specific `@media` rules with the slide's `#id` selector. Never shrink everything globally.

5. **Verify DOM presence before assuming things are "missing"**: When elements appear hidden, check if they exist in markup first — the issue is usually CSS (opacity, overflow, layout) not deletion.

6. **Eyebrow labels clip at the top**: Add explicit `padding-top` to `.scene-inner` for slides where the `h3` eyebrow is cut off by the scene's top edge.

7. **Card content should be concise**: Keep cards to 3–5 bullet points. Dense multi-paragraph cards break layout on smaller screens and in fullscreen.

8. **Use `clamp()` for everything**: Every font size, padding, margin, and gap should use `clamp(min, preferred, max)` for fluid scaling.

9. **Strong text in bullet lists**: Use `color: var(--accent)` for `strong` elements inside bullets. This is the established emphasis pattern.

10. **Slide numbering**: The slide counter calculates `total` from `document.querySelectorAll('.scene').length`. When adding/removing slides, the counter auto-updates. Commented-out slides still exist in the DOM and may be counted — use deletion, not comments, to remove slides.
