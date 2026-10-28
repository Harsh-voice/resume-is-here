# Design spec — top to bottom

Colours, palette, fonts, data, design. Nothing else.

---

## PALETTE

27 tokens, all declared on `:root` in `styles.css`.

### Ink

| Token | Hex | Used for |
|---|---|---|
| `--tx` | `#1f1f1f` | All headings, bold text, the near-black everything sits on |
| `--tx-secondary` | `#3d3d3d` | Body copy inside cards and accordions |
| `--tx-tertiary` | `#666` | Ledes, captions, tags, the quiet layer |

### Paper and lines

| Token | Hex | Used for |
|---|---|---|
| `--paper` | `#ffffff` | Page background, card fills |
| `--paper-soft` | `#fcfcfc` | Footer, alternating section wash |
| `--st` | `#e6e6e6` | Every 1px border and hairline |
| `--st-secondary` | `#f0f0f0` | The lighter second-level rule |

### Greys

`--grey-50 #f9f9f9` · `--grey-100 #f5f5f5` · `--grey-200 #f0f0f0`
`--grey-300 #e6e6e6` · `--grey-400 #cccccc` · `--grey-600 #999999`

Used for placeholder fills, disabled states and the proof-shot backgrounds.

### Indigo — the one accent colour

| Token | Hex | Used for |
|---|---|---|
| `--indigo-100` | `#e8effc` | Wash behind highlighted rows |
| `--indigo-300` | `#a7c0f1` | Hover borders |
| `--indigo-500` | `#6a88e2` | Secondary marks |
| `--indigo-600` | `#556adc` | **The verification badges.** 23 of them |
| `--indigo-700` | `#4250d5` | Links, numbers, the stepper's active state |
| `--indigo-800` | `#3333cc` | **Sarvam's primary blue.** Link hover, favicon |
| `--indigo-900` | `#212191` | Deepest, used sparingly |

### Ink button gradient

`--ink-btn-a #3a3f5c` → `--ink-btn-b #1e2033`

The dark pill buttons. Not flat black, a blue-leaning charcoal gradient. Taken
off Sarvam's own buttons.

### Glyph field — the only place warm colour appears

| Token | Hex |
|---|---|
| `--glyph-dim` | `#d8d8d8` |
| `--glyph-saffron` | `#f9730c` |
| `--glyph-amber` | `#ffb053` |
| `--glyph-indigo` | `#556adc` |
| `--glyph-peri` | `#a5bbfc` |

Saffron through to indigo, the flag running left to right across the Indic
glyphs in the closing section.

### Rules this palette follows

1. **One accent.** Indigo. Everything else is ink, paper or a hairline.
2. **Warm colour appears exactly once**, in the glyph field at the end.
3. **No pure black and no pure grey text.** `#1f1f1f`, never `#000`.
4. **Borders are always `#e6e6e6`.** One weight, one colour, everywhere.

---

## FONTS

Three faces. All variable except the mono.

| Face | Weight range | Used for |
|---|---|---|
| **Season Mix** | 300–900 | Every large heading. The face that makes it read as Sarvam |
| **Matter** | 100–1000 | All body, labels, buttons, list rows |
| **Matter Mono** | 400 | Small uppercase labels, dates, numbers, the footer line |

### Display setting

```
font-family     "Season Mix", Matter, serif
font-weight     525
letter-spacing  -0.022em
line-height     1.06 to 1.18
```

That weight and that letter-spacing are the two values that matter. Miss them
and it stops looking like Sarvam whatever else is right.

### Type scale

| Role | Size | Face |
|---|---|---|
| Hero h1 | `clamp(38px, 5.2vw, 64px)` | Season Mix 425 |
| Closing h2 | `clamp(36px, 4.8vw, 52px)` | Season Mix 525 |
| Section h2 | `clamp(30px, 3.9vw, 42px)` | Season Mix 525 |
| Phase card h3 | `clamp(26px, 3.2vw, 38px)` | Season Mix 525 |
| Experience role | `clamp(21px, 2.4vw, 27px)` | Matter 525 |
| Section lede | 18px | Matter 450 |
| Body, list rows | 17px | Matter 450 |
| Card body | 16px | Matter 450 |
| Tags, captions | 13px | Matter 450 |
| Kicker labels | 12px, `letter-spacing: 2px`, uppercase | Matter Mono |

---

## THE PAGE, TOP TO BOTTOM

### Header — fixed

```
sarvam     Walkthrough  30-Day Plan  Experience    [Growth Marketing Intern] [Harsh Bomble]
```

**Design.** Fixed to the top. Transparent over the hero, then a white panel
fades in past 40px of scroll. The wordmark links to sarvam.ai.

**Colours.** White panel, `#e6e6e6` bottom hairline. Left pill is white with a
hairline border, right pill is the ink gradient.

**Type.** Nav links Matter 450. Pills Matter 525 at 15px.

---

### 1 · Hero

**Data.** Kicker: *Application · Growth Marketing Intern.* Headline: **What
I'd ship in my first month.** Two buttons: *Watch the walkthrough* and *Read
the plan*.

**Design.** Centred, 206px of air above the headline. Sarvam's real gradient
SVG behind it, a saffron-to-periwinkle wash, plus the flower motif and a grain
overlay at 0.22 opacity.

---

### 2 · Walkthrough — `#walkthrough`

**Data.** Four steps: **Bet · Build · Spend · Cut.** Heading: *The
two-minute version.* The video frame sits beside it.

**Design.** Split layout. Stepper on the left with a connecting rule, media
frame on the right with a translucent border, copied from Sarvam's own media
pattern.

---

### 3 · The 30-day plan — `#plan`

**Data.** One 231-word paragraph. Harsh's own plan, almost verbatim: aim at
startup founders and developers, because the category is won on default habit.
The Startup Program is really a habit-formation product. ₹1L across three
weeks, three channels, each on its own page. The metric is developers at
sustained daily API calls by day 30, not signups. Kill a channel over target
at ₹15k.

**Design.** A single bordered card, 24px radius, with a flower motif bleeding
off one corner.

### 4 · Three phases — `#phases`

**Data.**

| Card | Heading | Panel |
|---|---|---|
| The bet | This category is won on default habit | Program window `6–12 mo` · SDK written `Once` · Rewritten `Rarely` · Real product `The habit` |
| Weeks 1–3 · ₹1L | Three channels, three pages | Comparison page `Search` · Creator pages `Collab` · Founders page `Meta` · Clean attribution `Per page` |
| Day 30 | One metric, one kill rule | `₹15k` decision point · `Day 30` measured at · `Daily` calls sustained · `3` channels judged |

**Design.** The three cards are `position: sticky` at stepped offsets of
100px, 122px and 144px. Card one pins, card two slides over it, card three
over that. On screens under 1000px, and with reduced motion on, they stack
normally.

---

### 5 · What I'd measure

**Data.** Four numbered items: **Developers at sustained daily calls · Cost per
activated developer · Attribution by landing page · The ₹15k gate.**

**Design.** No boxes. A numbered list with hairlines between, so it reads
differently from the card grids above and below it.

---

### 6 · Experience — `#experience`

**Stat strip.** `14M+` Views generated · `₹75.2L` Revenue driven · `10x`
Return on ad spend · `₹21.6L` Ad spend managed. Each counts up when it enters
the viewport. Beneath: *Client and campaign specifics withheld under agency
confidentiality.*

**Data.** Five panels, multi-expand, first one open.

| | Role | Org | Dates |
|---|---|---|---|
| 01 | Co-Founder | Nexussv · Full-time | Aug 2023 – Feb 2026 |
| 02 | Founder | Dialvola · AI voice call centre | Mar 2026 – Oct 2026 |
| 03 | Growth & Performance Marketing | PK Films · Part-time | May 2025 – Dec 2025 |
| 04 | Campaign Design & Creative | India Post · Project engagement | Sep 2024 |
| – | B.Tech, Data Science | Department of Technology, SPPU | Third year |

**Design.** Every bullet carries Sarvam's real scalloped verification badge in
`--indigo-600`, drawn once as an SVG `<symbol>` and referenced 23 times. The
panels animate open with `grid-template-rows: 0fr → 1fr`, so the height
animates with no JavaScript measurement.

**Languages.** Hindi **Fluent** · Marathi **Native** · English **Working**.
Each in a pill with its script shown: हिन्दी, मराठी, Aa.

---

### 7 · Receipts — `#proof`

**Data.** One card: *Every number on this page comes off Meta Ads Manager or
the Instagram professional dashboard.* Links to `proof.html`, which holds nine
screenshots.

**Design.** A single bordered card with an arrow that slides 4px on hover.

---

### 8 · FAQ — `#faq`

**Data.** Ten questions, multi-expand, all closed by default.

**Design.** The same accordion component as Experience, driven by the same
`[data-accordion]` handler but independent of it.

---

### 9 · Pull quote

**Data.** *"I built the voice layer on ElevenLabs. Not after a benchmark
comparison. It was the name I already knew. That default is exactly the gap I
want to work on at Sarvam."*

**Design.** Large Season Mix, centred, no quotation marks drawn as ornament.

---

### 10 · What I work with — `#stack`

**Data.** 19 tools, staggered **6 / 7 / 6**:

> Meta Ads · Google Ads · Sarvam · Claude · ElevenLabs · Hugging Face ·
> WhatsApp Business · Gemini · OpenAI · Google Flow · Canva · Photoshop ·
> Premiere Pro · Jitter · Webflow · Discord · Emergent · Search Console · Figma

**Design.** Each tool is its real SVG logo plus a label in a hairline pill.
Three rows, the middle one wider, offset so it reads as a composition rather
than a grid.

---

### 11 · And I built this page — `#design`

**Data.** The live design tokens of the page itself: the colour ramp, the type
scale, the motion curve. *Vibe-coded end to end, the same way I shipped 50+
sites for Chakan MIDC companies.*

**Design.** A spec panel that reads its values from the page it is on, so it
cannot go out of date.

---

### 12 · Why Sarvam — `#why`

**Data.** Currently `REPLACE ME`.

**Design.** A bordered card with a motif bleeding off the corner.

---

### 13 · Closing statement

**Data.** Kicker: *Growth Marketing Intern · Bengaluru.* Headline: **Build the
Future of India's AI** / *with Sarvam*, the second line in the saffron-to-indigo
gradient. Below: *The plan above is a starting position, not a pitch.*

**Design.** Behind it, a field of Indic glyphs rendered as **live text**, not
an image, which is how Sarvam does it on their careers page. Saffron through
amber through indigo through periwinkle, left to right.

---

### Footer

```
Harsh Bomble
Applying for Growth Marketing Intern · Bengaluru
harshbomble.work@gmail.com   LinkedIn   Experience   30-Day Plan
────────────────────────────────────────────────────────────────
VIBE-CODED BY HARSH BOMBLE · NOT AFFILIATED WITH SARVAM AI    2026
```

**Design.** `--paper-soft` background, `#e6e6e6` top rule. Name in Season Mix
425. The base line in Matter Mono 11px, `letter-spacing: 0.08em`, uppercase,
in `--grey-400`.

---

## MOTION

One curve for everything: `cubic-bezier(0.2, 0, 0, 1)`.

| Thing | Timing |
|---|---|
| Reveal on scroll | `opacity .36s ease-out, translate .52s` |
| Hover | `.35s` |
| Accordion | `.45s` |
| Header panel | `.4s` |
| Preloader lift | `.5s` |

Measured off Sarvam's live site, not guessed. Nothing bounces, nothing
springs, nothing scales from zero.
