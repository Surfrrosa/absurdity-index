# Absurdity Index Design System

*Established: January 2026*
*Maintainer: Shaina Pauley (with Claude Code)*

---

## Philosophy

The Absurdity Index uses **brutalist design** to match its unflinching examination of modern absurdity. The aesthetic is intentionally stark, bold, and uncompromising—like the data it presents.

**Core Principles:**
1. **Clarity over decoration** — Data speaks for itself
2. **High contrast** — No ambiguity, no soft edges
3. **Meaningful color** — Red means crisis, not decoration
4. **Consistent thresholds** — 50% is the line between "concerning" and "crisis"

---

## Typography

### Font Stack

| Font | Weight | Usage | CSS Class |
|------|--------|-------|-----------|
| **Archivo Black** | 400 (appears black) | Headlines (h1-h6), titles, metric names | Applied automatically to `h1`-`h6` |
| **Space Grotesk** | 700 (bold) | Body text, labels, UI elements | Default `font-family` on `body` |
| **Roboto Mono** | 700 (bold) | Numbers, data, scores, dates | `.mono` class |

### Font Import (globals.css)
```css
@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Space+Grotesk:wght@700&family=Roboto+Mono:wght@700&display=swap');
```

### Automatic Styling
Headlines (`h1`-`h6`) automatically receive:
- `font-family: 'Archivo Black', sans-serif`
- `text-transform: uppercase`
- `letter-spacing: -0.02em`

### Text Transform Rules
| Element | Transform |
|---------|-----------|
| Headlines | `uppercase` (automatic) |
| Metric titles | `uppercase` |
| Labels | `uppercase` |
| Data/Numbers | None (use `.mono`) |
| Body paragraphs | Sentence case |

### Sizing Scale

| Element | Mobile | Desktop |
|---------|--------|---------|
| Page title (h1) | `text-3xl` | `text-5xl`–`text-6xl` |
| Main score display | `text-6xl` | `text-8xl`–`text-9xl` |
| Card title | `text-lg` | `text-xl` |
| Card score | `text-5xl` | `text-6xl` |
| Labels/Status | `text-xs` | `text-xs` |
| Body text | `text-sm` | `text-base` |

### Font Weight Rules
- **Only use:** `font-bold` (700) and `font-black` (900)
- **Never use:** Light, regular, or medium weights
- Headlines: `font-black`
- Body/Labels: `font-bold`

---

## Color Palette

### Primary Colors

| Color | Hex | Tailwind | Usage |
|-------|-----|----------|-------|
| Pure Black | `#000000` | `black` | Page background, borders, text on light backgrounds |
| Pure White | `#FFFFFF` | `white` | Card backgrounds (< 50%), text on dark backgrounds |
| Crisis Red | `#DC2626` | `red-600` | Crisis state backgrounds, progress bar fills, alerts |

### Accent Colors (Banner Only)

| Color | Hex | Usage |
|-------|-----|-------|
| Dark Burgundy | `#5f0f0f` | Bosch banner background only |

### Data Visualization Colors

| Color | Tailwind | Usage |
|-------|----------|-------|
| Red | `red-600` | Level 3 (Crisis) badges |
| Orange | `orange-500` | Level 2 (Frustrated) badges |
| Yellow | `yellow-500` | Level 1 (Mild) badges |
| Green | `green-600` | Completion indicators, improving trends |

### Color Rules

1. **Red indicates crisis** — Never use red decoratively
2. **Black and white are structural** — They define space and hierarchy
3. **Visualization colors stay in data viz** — Orange/Yellow/Green only in charts and badges
4. **No grays** — Use pure black or pure white (exception: `border-black/20` for subtle dividers)

---

## The 50% Threshold Rule

The 50% mark is the **critical threshold** where a metric crosses from "concerning" to "crisis mode." This is the core visual mechanic of the dashboard.

### Below 50% (Non-Crisis State)
| Element | Value |
|---------|-------|
| Card Background | White (`bg-white`) |
| Text/Numbers | Black (`text-black`) |
| Progress Bar Track | Black (`bg-black`) |
| Progress Bar Fill | Red (`bg-red-600`) |
| Border Divider | Light (`border-gray-300`) |

### At or Above 50% (Crisis State)
| Element | Value |
|---------|-------|
| Card Background | Red (`bg-red-600`) |
| Text/Numbers | White (`text-white`) |
| Progress Bar Track | Black (`bg-black`) |
| Progress Bar Fill | White (`bg-white`) |
| Border Divider | Dark (`border-gray-600`) |

**Visual meaning:** When a card "flips" to red, it signals the metric has crossed into crisis territory.

### Threshold Rule Exceptions

Some components are **exempt** from the 50% threshold rule:

#### 1. AbsurdityScore (Main Score Display)
The overall score at the top of the dashboard uses a **fixed design**:
- Background: Black (`bg-black`)
- Score color: Red (`text-red-600`)
- Progress bar: White track (`bg-white`), Red fill (`bg-red-600`)

**Rationale:** The main score is an aggregate of all metrics. It uses an inverted color scheme (dark background) to visually separate it from individual metric cards. The red score number provides emphasis without implying the same "crisis flip" mechanic.

#### 2. MetricDetail Modal (Accent Sections)
The modal's "Score Breakdown" and "Methodology & Sources" sections are **always red** regardless of the metric's score:
- These sections use `bg-red-600` as **visual hierarchy accents**
- They are not data-reactive elements

**Rationale:** The modal is informational—users already know which metric they're viewing from the card they clicked. The red accent sections provide visual rhythm and break up large amounts of information. Making them threshold-reactive would create visual chaos and lose the hierarchy.

#### 3. Data Visualization Sections
Level distribution bars and collection progress bars use **fixed color schemes**:
- Level 3: Red (`bg-red-600`)
- Level 2: Orange (`bg-orange-500`)
- Level 1: Yellow (`bg-yellow-500`)
- Complete: Green (`bg-green-600`)

**Rationale:** These represent categorical data, not score thresholds.

---

## Imagery

### Banner Image
- **Source:** Hieronymus Bosch, "The Garden of Earthly Delights" (middle panel)
- **URL:** Wikimedia Commons (public domain)
- **Treatment:**
  - `backgroundSize: '280%'`
  - `backgroundPosition: '50% 30%'`
  - `opacity: 0.45`
  - `filter: grayscale(5%) contrast(140%) brightness(65%)`
  - `mixBlendMode: 'overlay'`

### Image Rules
1. **Classical absurdist art only** — Bosch, Bruegel, Goya style
2. **Always desaturated/filtered** — Never full-color imagery
3. **Overlay blend mode** — Images support, not dominate
4. **No stock photos** — No modern photography

---

## Borders

Borders are **structural elements** in brutalist design—thick, black, and uncompromising.

### Border Widths

| Context | Width | Example |
|---------|-------|---------|
| Main score container | `border-8` | Outer wrapper of overall score |
| Modal/Detail views | `border-8` | MetricDetail sections |
| Standard cards | `border-4` | MetricCard |
| Buttons | `border-4` | Navigation buttons |
| Progress bars | `border-2` | All progress bar tracks |
| Section dividers | `border-b-4` | Header bottom borders |
| Internal dividers | `border-t-2` | Within-card separators |

### Border Rules
1. **Always black** — `border-black` (exception: hover state uses `border-red-600`)
2. **Always sharp** — No `rounded-*` classes, ever
3. **Consistent per component type** — Don't mix widths within a component
4. **White borders on dark backgrounds** — Use `border-white` when on black/red backgrounds

---

## Progress Bars

### Anatomy
```
┌──────────────────────────────────────┐
│ Track (unfilled)  │ Fill (score %)   │
└──────────────────────────────────────┘
```

### Specifications

| Property | Value |
|----------|-------|
| Height (cards) | `h-6` |
| Height (main score) | `h-8` |
| Border | `border-2 border-black` |
| Fill transition | `transition-all duration-1000` |

### Colors by Threshold

| Score | Track | Fill |
|-------|-------|------|
| < 50% | Black (`bg-black`) | Red (`bg-red-600`) |
| >= 50% | Black (`bg-black`) | White (`bg-white`) |

**Note:** Track is always black. Only the fill color changes at the threshold.

---

## Cards (MetricCard)

### Visual Anatomy
```
┌─────────────────────────────────────┐
│ METRIC TITLE                     ↑  │  ← Archivo Black, uppercase
│                                     │
│ 49.97                               │  ← Roboto Mono, large
│                                     │
│ "STATUS LABEL IN QUOTES"            │  ← Space Grotesk, uppercase, small
│                                     │
│ ████████████░░░░░░░░░░░░░░░░░░░░░░  │  ← Progress bar
│                                     │
│ Data source line 1...               │  ← Roboto Mono, truncated
│ Data source line 2...               │
│ Data source line 3...               │
│─────────────────────────────────────│  ← border-t-2 divider
│ 427 entries                         │  ← Roboto Mono
│ January 18, 2026                    │  ← Roboto Mono, slightly dimmed
└─────────────────────────────────────┘
```

### State Styling

| Score | Background | Text | Progress Fill | Divider |
|-------|------------|------|---------------|---------|
| < 50 | `bg-white` | `text-black` | `bg-red-600` | `border-gray-300` |
| >= 50 | `bg-red-600` | `text-white` | `bg-white` | `border-gray-600` |

### Interactions
| State | Effect |
|-------|--------|
| Default | No shadow |
| Hover | `border-red-600`, `shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]`, `-translate-y-1` |
| Active | `shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]`, position returns |
| Focus | Same as hover (keyboard accessibility) |

---

## Buttons

### Primary Button (Light)
```
bg-white text-black border-4 border-black
hover:bg-red-600 hover:text-white hover:border-white
```

### Primary Button (Dark/On Red)
```
bg-red-600 text-white border-4 border-white
hover:bg-white hover:text-black
```

### Button Text
- `font-black`
- `uppercase`
- `tracking-wide`
- Size: `text-xs` (mobile) to `text-sm` (desktop)

---

## Spacing

### Container Padding
| Context | Mobile | Desktop |
|---------|--------|---------|
| Cards | `p-4` | `p-6` |
| Main sections | `p-6` | `p-10` |
| Page margins | `px-4` | `px-6` |

### Grid & Gaps
| Context | Mobile | Desktop |
|---------|--------|---------|
| Card grid | `gap-4` | `gap-6` |
| Grid columns | 1 | 2 (md) → 4 (lg) |

### Vertical Rhythm
| Context | Value |
|---------|-------|
| Between major sections | `mt-12` |
| Between cards and sections | `mt-8` |
| Within cards | `mb-3`–`mb-4` |

---

## Shadows

Shadows are **interaction feedback only**—never decorative.

| State | Shadow |
|-------|--------|
| Default | None |
| Hover | `shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]` |
| Active | `shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]` |

**Rules:**
- Hard-edge shadows only (no blur)
- Black only
- Offset shadows (brutalist style)

---

## Animations

### Entrance Animation
```css
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fadeInUp {
  animation: fadeInUp 0.6s ease-out forwards;
}
```

### Staggered Loading
Cards animate in with staggered delays: `(index + 1) * 100ms`

### Progress Bar Animation
- Main score: `duration-2000` (2 seconds)
- Cards: `duration-1000` (1 second)

### Rules
1. **Subtle and purposeful** — Animations serve UX, not decoration
2. **Ease-out timing** — Fast start, gentle landing
3. **Respect reduced motion** — Should disable for `prefers-reduced-motion`

---

## Level Indicators (Data Visualization)

### Severity Levels

| Level | Color | Tailwind | Label |
|-------|-------|----------|-------|
| Level 3 | Red | `bg-red-600` | CRISIS |
| Level 2 | Orange | `bg-orange-500` | FRUSTRATED |
| Level 1 | Yellow | `bg-yellow-500` | MILD |

### Usage
- Level badges in sample data
- Distribution bar charts in MetricDetail
- **Never** in primary card UI

---

## Component Hierarchy

### Z-Index Layers
| Layer | Z-Index | Usage |
|-------|---------|-------|
| Base content | 0 | Cards, main content |
| Banner overlay | 10 | Bosch image overlay |
| Modal backdrop | 50 | MetricDetail overlay |
| Modal close button | 50 | Fixed position close X |

---

## Accessibility

### Contrast Requirements
All combinations must meet WCAG AA (4.5:1 for text):
- ✓ Black on white
- ✓ White on black
- ✓ White on red-600
- ✓ Black on red-600

### Interactive Requirements
- All clickable elements have visible focus states
- Keyboard navigation works (Enter/Space to activate)
- Touch targets minimum 44x44px
- Skip links for screen readers (if needed)

### Motion Considerations
- Animations should respect `prefers-reduced-motion`
- Critical information never depends on animation

---

## Don'ts

| Don't | Why |
|-------|-----|
| Use gradients | Flat colors are brutalist |
| Use rounded corners | Sharp edges define the aesthetic |
| Use colored borders | Black only (red on hover is exception) |
| Use decorative red | Red = crisis, always meaningful |
| Use light/medium font weights | Bold and black only |
| Use gray backgrounds | Black or white only |
| Use blur shadows | Hard-edge shadows only |
| Use stock photography | Classical art or nothing |
| Mix border widths in a component | Consistency within components |

---

## Resolved Design Decisions

The following items were identified during the January 2026 audit and have been resolved:

| Item | Resolution |
|------|------------|
| MetricDetail red sections | **Documented as intentional** — See "Threshold Rule Exceptions" |
| AbsurdityScore progress bar | **Documented as intentional** — See "Threshold Rule Exceptions" |
| MetricCard threshold | **Fixed** — Now correctly flips at 50% |
| Unused Geist font imports | **Removed** — Cleaned from layout.tsx |

### Remaining Data Issues (Not Design)

1. **Methodology page hardcoded** — Data counts don't auto-update (requires automation work, not design fix)

---

## Component Checklist

When creating or modifying components, verify:

- [ ] Fonts: Archivo Black for headlines, Space Grotesk for body, Roboto Mono for data
- [ ] Colors follow the 50% threshold rule
- [ ] Borders are black, sharp, and consistent width
- [ ] Text is uppercase where appropriate
- [ ] Numbers use `.mono` class
- [ ] Interactive states defined (hover, active, focus)
- [ ] Animations use ease-out timing
- [ ] Accessibility requirements met

---

*This document is the source of truth for Absurdity Index design decisions.*
*Last updated: January 18, 2026*
