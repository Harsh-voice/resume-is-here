# 41-second walkthrough

## The film is already made

`30-day-plan.mp4` in this repo. 1920x1080, 30fps, exactly 41.00 seconds,
1.9 MB, silent.

I built it rather than prompting a tool, because that was the only way to use
the **real Matter and Season Mix fonts**. It is rendered from
`film-source.html`, which draws every frame from the same design tokens as
the website, so the type, colour and easing are identical to the page, not
an approximation of it.

It includes the scalloped reveal in lime and periwinkle, the funnel stepper,
the ranked list, the dashboard tiles, the closing line, the end card, and
burned-in subtitles. The subtitles matter: on LinkedIn and in email the video
autoplays muted, so it has to work with no sound at all.

**What is missing is the voice.** See `voice-cues.md` for the exact start
time of each line. Generate the lines with Bulbul, drop each at its cue, and
the voice lands on the captions.

To change anything, edit `film-source.html` and re-render:

```
node render.js            # writes frames/
ffmpeg -framerate 30 -i frames/f%05d.jpg -c:v libx264 -preset slow \
       -crf 18 -pix_fmt yuv420p -movflags +faststart 30-day-plan.mp4 -y
```

The Claude Motion prompt below is kept as a fallback if you ever want a
different cut.

---

# Script and Claude Motion prompt

Reference: `assets.sarvam.ai/Pages/home/india-can.mp4`, Sarvam's own homepage
film. 1920×1080, 30fps, 2:13, continuous music bed, **no narrator**.

---

## The length problem, first

Your script is **257 words**. Spoken at a normal pace that is **1 minute 43
seconds**. There is no delivery speed that fits it into 41 seconds and stays
listenable.

41 seconds, minus about 2 seconds for the end card, gives roughly **100
words**. So this is a 60% cut, not a trim.

**Nothing is lost.** The full 257 words still sit on the page, in the 30-day
plan box. The video is the trailer. The page is the detail. That is the right
split anyway: nobody reads a dense paragraph off a video.

### What I kept

- All three phases. They are the structure of the plan.
- The hesitation line. It shows *how* you work, not just what you'd do.
- The LLM answer line. It is the sharpest strategic point you have, and the
  one a growth lead will react to.
- The closing sentence. Your best line, almost untouched.

### What I cut

- Timing every step from landing page to first call
- The keyword and competitor audit detail
- The three specific deliverables (comparison page, tutorial, schema)
- The five dashboard metrics by name
- "What moved, what didn't, what I'd kill"

All of it stays on the page.

---

## What Sarvam's film does

I pulled their video down and read it frame by frame.

**The scalloped petal shape is everything.** It works three ways: a
horizontal wipe that travels across frame and uncovers the text behind it, a
container holding big type, and a full-bleed colour field with the wordmark
ghosted inside.

**Their signature shot completes a sentence as the shape moves.** "India can"
sits left. The saffron scallop sweeps in from the right and uncovers "train
state-of-the-art models".

**Colour is a journey.** Sepia manuscript, near-white grey, saffron, lime,
periwinkle, magenta, then a black end card with the white wordmark.

**Footage is documentary, never stock.** ISRO launch, a street market, a
farmer on a phone in a mustard field.

**Type is large and given room.** One phrase per frame. Long holds.

**Audio: continuous music, zero silence gaps across all 133 seconds.** No
voiceover anywhere.

---

## The one place not to copy them

Their film has no narrator because it is a brand film. Yours is a
walkthrough. Their look, your voice over the top.

### Whose voice

**Use Sarvam Bulbul v3, their own text-to-speech.** You have API access
through the Startup Program. Docs: docs.sarvam.ai, Text-to-Speech.

Then put one line on the end card: *"Narrated with Sarvam Bulbul v3."*

You would be applying to Sarvam using Sarvam. That single credit proves you
have used the product, which does more for you than the whole tools section
on your page. It also means you never record your own voice.

Set the rate to about 165 words per minute, which puts the film at 38
seconds. Do not go below 155. At 150 the script alone runs 39.6 seconds and
the end card pushes you past the limit. Do not use a generic
American AI voice from anywhere else. That is the one choice that reads as
lazy.

---

## The script — 98 words, 41 seconds

---

**0:00–0:02** · Near-white. Centred, small: `A 30-DAY PLAN`. Below it, large
display type: **Thirty days**. No voice.

---

**0:02–0:11** · Screen recording, real: the Sarvam docs signup. Cursor
moving. Plays at about 1.4×.

> Days one to ten. I sign up for the API as a first-time developer and note
> where I hesitate.

**0:09** The recording freezes. A thin indigo underline draws under the
moment of hesitation.

> Those are the places signups drop.

---

**0:11–0:19** · Cut to a ChatGPT answer card floating on near-white, soft
shadow, a question about Indic speech visible at the top.

> Then I check what ChatGPT says about Indic speech.

**0:16** The card scales up to fill the frame.

> Increasingly, that answer is the top of the funnel.

---

**0:19–0:30** · Lime scallop wipes in from the right. Left: **Days 11–20**.
Revealed right: **ship the cheapest fixes**.

> Days eleven to twenty. The audit becomes a ranked list.

**0:23** A list builds on near-white, one row at a time, three columns
landing separately.

> Every item gets an owner and a number it should move. Then I publish the
> top two or three.

---

**0:30–0:36** · Periwinkle scallop wipe. Then a dashboard assembles tile by
tile, five tiles.

> Days twenty-one to thirty. One dashboard the team opens. Two honest
> experiments. One short readout.

---

**0:36–0:40** · Everything clears to plain near-white. Empty for half a
second. Then one line of display type fades up, centred.

> Not a vanity spike. A setup the team keeps using after I'm gone.

---

**0:40–0:41** · Cut to black. White type, centred:

```
Harsh Bomble
Growth Marketing Intern · Bengaluru
Narrated with Sarvam Bulbul v3
```

---

## Claude Motion prompt

Paste this whole block, then paste the script above after it.

```
Make a 41 second brand film at 1920x1080, 30fps, for a job application to
Sarvam AI. It must look like it came off Sarvam's own homepage. 41 seconds
is a hard limit.

DESIGN SYSTEM, follow exactly:

Type: a geometric humanist sans for labels and body. For every large display
line use a high-contrast display face with slight serif feel. Display lines
are large, weight around 525, letter-spacing -0.022em, and there is never
more than one on screen at a time.

Colours:
  paper      #ffffff     text        #1f1f1f
  hairline   #e6e6e6     muted text  #6b6b6b
  saffron    #f9730c     amber       #ffb053
  indigo     #3333cc     periwinkle  #a5bbfc
  lime       #b7d44a     end card    #000000

THE CORE MOTIF: a scalloped petal shape, a flower with eight rounded lobes,
like a Mughal arch repeated around a circle. Use it two ways in this film:
  1. As a horizontal wipe that travels across frame from the right and
     uncovers the text behind it.
  2. As a soft full-bleed colour field between acts.

THE SIGNATURE SHOT, used twice: a short phrase sits on the left of a
near-white frame. The scalloped shape sweeps in from the right in a solid
colour and, as it travels, uncovers the second half of the sentence. The
sentence completes as the shape moves. Lime the first time, periwinkle the
second.

COLOUR JOURNEY: near-white, lime, periwinkle, then black for the end card.

MOTION: calm, with long holds even at this length. Nothing bounces, nothing
springs. Ease with cubic-bezier(0.2, 0, 0, 1) over about 0.5 seconds.
Elements enter by sliding a short distance while fading, never by scaling
from zero. Hard cuts inside an act, one cross-dissolve between acts.

LAYOUT: large negative space. One idea per frame. UI cards float on
near-white with a very soft shadow and an 18px corner radius.

AUDIO: one continuous calm instrumental bed, warm, no drums in the first ten
seconds, nothing triumphant. A narrator over it, clear and forward in the
mix, reading at about 165 words per minute.

SUBTITLES: burn in the narration as white bold text at bottom centre.

DO NOT: use stock-footage gloss, put drop shadows on text, use more than one
display font, use bright primary blue, use emoji, use elastic or bouncing
easing, or put two headlines on screen at once.

Then follow the scene-by-scene script and voiceover I am providing. Hold the
total to 41 seconds.
```

---

## What you still have to record

Two screen recordings. Nothing can fake these and they are the most
convincing seconds in the film:

1. **Signing up for the Sarvam API.** Record it genuinely, hesitation
   included. That hesitation is the whole point of the first act. You need
   about 9 seconds of usable footage.
2. **A dashboard** with those five metrics on it. Rough is fine. About 6
   seconds.

Everything else can be generated.

---

*A 2 minute 8 second version of this script, using the full 257 words, is in
this repo's git history if the length limit ever changes.*
