# Film brief — fonts, idea, prompt

Everything needed to build the 41-second film yourself. Nothing else in here.

---

## 1. FONTS

Three files, already in this repo under `fonts/`:

| File | Use it for |
|---|---|
| `SeasonMixVFUprights.woff2` | **Every large line.** Titles, the split lines, the closing line, the name on the end card. This is the face that makes it read as Sarvam. |
| `MatterUprights-VF.woff2` | Body text, card titles, list rows, buttons, anything mid-size. |
| `MatterMono-Regular.woff2` | Small uppercase labels, timers, step numbers, the credit line. |

Both VF files are variable fonts. Season Mix spans weight 300 to 900, Matter
spans 100 to 1000.

### Exact settings

**Season Mix, display:**
```
weight          525
letter-spacing  -0.022em
line-height     1.06  (single line)  /  1.18  (wrapped)
```
Sizes used: title 128px · split lines 76px · punch line 90px · closing line
80px · section heads 48px · end-card name 76px

**Matter, body:**
```
weight          450 normal / 525 emphasis
letter-spacing  0
line-height     1.25 to 1.6
```
Sizes: card titles 31px · list rows 31px · body 22–30px · subtitles 40px

**Matter Mono, labels:**
```
weight          400
letter-spacing  0.12em to 0.20em
transform       uppercase
```
Sizes: 13–24px

### Colours

```
paper        #ffffff        text          #1f1f1f
soft paper   #fafafa        text 2        #4a4a4a
hairline     #e6e6e6        text 3        #6b6b6b
hairline 2   #f0f0f0

saffron      #f9730c        lime          #b7d44a
amber        #ffb053        periwinkle    #a5bbfc
indigo       #3333cc        peri soft     #dbe4fe
indigo 600   #4250d5        end card      #000000
```

One note: Matter and Season Mix are commercial fonts licensed to Sarvam.
You are using them for one application to Sarvam, which is the whole point of
the exercise. Just do not reuse them on other work.

---

## 2. THE IDEA

**One sentence:** a plan told in three acts, in Sarvam's own visual language,
where a scalloped petal field sweeps across the frame and finishes each
sentence as it travels.

**The one device that carries the whole film.** Sarvam's flower motif,
blown up huge, with four rounded lobes on its leading edge. A phrase sits on
the left of a white frame. The coloured field slides in from the right and
the second half of the sentence is written on it, appearing as the field
covers that side. The sentence completes as the shape moves. Then the field
keeps going and clears the frame, handing over to the next act.

Sarvam uses this on their homepage as "India can ⟩ train state-of-the-art
models". You use it twice:

- **₹1L, three weeks** ⟩ *three channels, three pages*, in lime
- **Day 30** ⟩ *one metric, one kill rule*, in periwinkle

**Colour as a journey, not a palette.** White, then lime, then periwinkle,
then black. Each act arrives with its own colour.

**Six beats, 41 seconds:**

| Time | Beat |
|---|---|
| 0:00–0:02 | Title. `A 30-DAY PLAN` in mono, **Default habit** in Season Mix. |
| 0:02–0:12 | Three pills one at a time: ChatGPT, Gemini, Claude. Indigo ring lands on ChatGPT, then **Still opened first.** |
| 0:12–0:20 | A four-row panel: the Startup Program window, SDK written `Once`, rewritten `Rarely`, the real product is `The habit`. |
| 0:20–0:27 | Lime sweep. **₹1L, three weeks** ⟩ *three channels, three pages*. Three channel cards with budget bars. |
| 0:27–0:34 | Periwinkle sweep. **Day 30** ⟩ *one metric, one kill rule*. Four gate tiles. |
| 0:34–0:41 | Empty white, then **Not signups. Developers still calling on day thirty.** Black end card. |

**Burn in the subtitles.** On LinkedIn and in email, video autoplays muted.
Most people watch it with no sound. It has to carry silently.

**Motion rule, the only one that matters:** ease everything with
`cubic-bezier(0.2, 0, 0, 1)` over about 0.5 seconds. Things enter by sliding
a short distance while fading. Nothing bounces, nothing springs, nothing
scales up from zero.

---

## 3. THE PROMPT

Paste this whole block, then paste `voice-script.txt` after it.

```
Make a 41 second film at 1920x1080, 30fps. 41 seconds is a hard limit. It is
a job application to Sarvam AI and must look like it came off Sarvam's own
homepage.

FONTS, use the files I am attaching:
  Season Mix  -> every large display line, weight 525, letter-spacing -0.022em
  Matter      -> body, card titles, list rows, weight 450 to 525
  Matter Mono -> small uppercase labels, timers, numbers, letter-spacing 0.15em

COLOURS:
  paper #ffffff   text #1f1f1f   hairline #e6e6e6   muted text #6b6b6b
  lime #b7d44a    periwinkle #a5bbfc   indigo #3333cc   indigo600 #4250d5
  peri soft #dbe4fe   saffron #f9730c   end card #000000

THE CORE MOTIF: a scalloped petal field. Picture a tall panel whose leading
edge is four large rounded lobes, like a Mughal arch repeated down the side.
It is the only graphic device in the film.

THE SIGNATURE SHOT, used twice. A short phrase sits on the left of a white
frame in Season Mix at 76px. The scalloped field slides in from the right in
a solid colour. The second half of the sentence is written on the field in
white and appears as the field covers that side, so the sentence completes as
the shape travels. The field parks with its lobed edge around x=880, holds
about one second, then continues left and clears the frame.
  First time, lime:        "Rs1L, three weeks"  >  "three channels, three pages"
  Second time, periwinkle: "Day 30"             >  "one metric, one kill rule"

SIX BEATS:
  0:00-0:02  Title. "A 30-DAY PLAN" small in mono above "Default habit" at 128px.
  0:02-0:12  Three pills centred, arriving one at a time: ChatGPT, Gemini, Claude.
             An indigo ring settles on the ChatGPT pill, then the line
             "Still opened first." drops in beneath them at 86px.
  0:12-0:20  A white panel, four rows arriving in order: Startup Program window
             6-12 months, SDK written against Once, Rewritten afterwards Rarely,
             So the real product is The habit. The two Once and The habit values
             are indigo, the rest near-black.
  0:20-0:27  Lime signature shot, then three cards deal out left to right:
             Comparison page (Search), Creator pages (Collab), Founders page
             (Meta). Each has a budget bar that fills from the left.
  0:27-0:34  Periwinkle signature shot, then four tiles land: Rs15k decision
             point, Day 30 measured at, Daily calls sustained, 3 channels judged.
  0:34-0:41  Everything clears to empty white for half a second. Then
             "Not signups. Developers still calling on day thirty." at 80px.
             Cut to a black end card with the name, the role, and
             "NARRATED WITH SARVAM BULBUL V3" small in mono.

LAYOUT: large negative space. One idea per frame, never two headlines at once.
Content sits in the middle of the frame with the bottom fifth kept clear for
subtitles. Cards are white with a 20px radius, a 1px #e6e6e6 border and a very
soft shadow.

MOTION: ease everything with cubic-bezier(0.2, 0, 0, 1) over about 0.5
seconds. Elements enter by sliding a short distance while fading. Long holds.
Hard cuts inside an act, one cross-dissolve between acts.

SUBTITLES: burn the narration in at bottom centre, Matter 40px weight 525, in
#1f1f1f. The film must be readable with the sound off.

AUDIO: one continuous calm instrumental bed, warm, no drums in the first ten
seconds, nothing triumphant. A narrator over it reading at 165 words per
minute, clear and forward in the mix.

DO NOT: use stock-footage gloss, put drop shadows on text, use a second
display font, use bright primary blue, use emoji, use elastic or bouncing
easing, or scale anything up from zero.

Then follow the narration script I am providing. Hold the total to 41 seconds.
```
