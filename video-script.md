# Two-minute walkthrough — script and Claude Motion prompt

Reference: `assets.sarvam.ai/Pages/home/india-can.mp4` — Sarvam's own homepage
film. 1920×1080, 30fps, 2:13, continuous music bed, **no narrator**.

---

## What Sarvam's film actually does

I pulled their video down and read it frame by frame. The grammar:

**The scalloped shape is everything.** Their petal/flower mark is used three
ways: as a horizontal wipe that slides across frame and reveals the second
half of a sentence, as a container holding big type, and as a full-bleed
colour field with the wordmark ghosted inside it.

**The signature move is a split line.** "India can" sits left. The saffron
scallop sweeps in from the right and uncovers "train state-of-the-art
models". Sentence completes as the shape travels.

**Colour runs as a journey, not a palette.** Sepia manuscript → near-white
grey → saffron → lime → periwinkle → magenta → black endcard with the white
wordmark.

**Footage is documentary, never stock.** ISRO launch, a street market, a
farmer on a phone in a mustard field, a hand slipping a phone into a shirt
pocket. Real, slightly imperfect, warm.

**Type is Season Mix, large, and given room.** Often one phrase per frame
with enormous margins. Holds are long. Nothing rushes.

**Burned-in subtitles** in white bold at the bottom when anyone speaks.

**Audio: continuous music, zero silence gaps across all 133 seconds.** No
voiceover anywhere. Speech in the film comes from the people on camera and
gets subtitled.

---

## The one place you should NOT copy them

Sarvam's film has no narrator because it is a brand film. Yours is a
walkthrough of a plan. Your page promises "a two-minute walkthrough", and
290 words of plan will not survive as silent title cards.

**So: their visual grammar, your voice over the top.**

### Whose voice

Two options, and the second is better.

1. **Your own voice.** They are hiring a person. An Indian accent applying to
   an Indian-languages AI company is not a liability.

2. **Sarvam's own TTS (Bulbul v3).** You have API access through the Startup
   Program. Narrating a Sarvam application with Sarvam's speech model is a
   demonstration, not a shortcut. Put one line in the end card: *"Narrated
   with Sarvam Bulbul v3."* That single credit does more work than the whole
   tools section on your page. Docs: docs.sarvam.ai, Text-to-Speech.

Either way, do not use a generic American AI voice. That is the one choice
that reads as lazy.

---

## The script

Target 2:05. Written for the ear, so sentences are shorter than the page.
Timings are cumulative.

---

### ACT 1 — Days 1–10 · 0:00–0:40

**0:00** Black. White `sarvam`-weight wordmark reading **Harsh Bomble** fades
up, holds 1s, cuts.

> **VO:** Thirty days. Here is what I would actually do.

**0:06** Near-white frame. Left: **Days 1–10**. The saffron scallop sweeps in
from the right and uncovers **learn the funnel by using it**.

> **VO:** Days one to ten. Learn the funnel by using it.

**0:12** Screen recording, real: the Sarvam docs signup, cursor moving, a
timer counting in the corner. Slightly sped up.

> **VO:** I sign up for the API the way a first-time developer would. I time
> every step, from landing page to first successful call. And I write down
> every place I hesitate.

**0:24** Hold on one frozen frame of that recording. A thin indigo underline
draws under the moment of hesitation.

> **VO:** Those are the same places signups drop off.

**0:29** Cut to three small UI cards floating on near-white, soft shadows,
drifting up in sequence: a Search Console graph, a keyword table, a ChatGPT
answer about Indic speech.

> **VO:** At the same time I audit what already exists. Which docs pages pull
> organic traffic. Which keywords Sarvam ranks for. And how Sarvam gets
> described when you ask ChatGPT, Perplexity or Gemini about Indian-language
> speech.

**0:38** The ChatGPT card scales up to fill frame.

> **VO:** Increasingly, that answer is the top of the funnel.

---

### ACT 2 — Days 11–20 · 0:40–1:17

**0:42** Lime-green scallop wipe. Left: **Days 11–20**, revealed right:
**ship the cheapest fixes**.

> **VO:** Days eleven to twenty. Ship the cheapest fixes.

**0:48** A ranked list builds on near-white, one row at a time. Each row has
three columns that land separately: owner, effort, the number it should move.

> **VO:** The audit becomes a ranked list. Every item has an owner, an effort
> estimate, and a number it should move.

**0:58** Three cards deal out like playing cards and settle in a row.

> **VO:** Then I publish the two or three that matter most myself. A
> comparison page that captures search demand that already exists. A
> developer tutorial that ends in a working call. And the metadata and schema
> changes that make both easier for search engines and LLMs to quote.

---

### ACT 3 — Days 21–30 · 1:17–1:55

**1:19** Periwinkle scallop wipe. Left: **Days 21–30**, revealed right:
**prove it with numbers**.

> **VO:** Days twenty-one to thirty. Prove it with numbers.

**1:25** A dashboard assembles tile by tile. Five tiles, each labelled as the
VO names it.

> **VO:** One dashboard the team actually opens. Signups, activation rate,
> time to first call, organic sessions, assisted conversions. One view.

**1:36** Two A/B panels slide in side by side. One wins. A small indigo tick
lands on it.

> **VO:** At least two honest experiments against it.

**1:41** A document page scrolls past, four headings highlighting in turn.

> **VO:** And a short written readout at the end of the month. What moved.
> What did not. What I would kill. And the three bets worth a bigger budget
> in month two.

---

### CLOSE · 1:55–2:08

**1:55** Everything clears to plain near-white. Nothing on screen.

> **VO:** The goal for thirty days is not a vanity spike.

**2:00** A single line of Season Mix type fades up, centred.

> **VO:** It is leaving behind a measurement setup and a backlog the team
> keeps using after the internship ends.

**2:06** Cut to black. White type, centred, three lines, 1.5s hold:

```
Harsh Bomble
Growth Marketing Intern · Bengaluru
Narrated with Sarvam Bulbul v3
```

---

## Claude Motion prompt

Paste this whole block.

```
Make a 2 minute 8 second brand film at 1920x1080, 30fps, for a job
application to Sarvam AI. It must look like it came off Sarvam's own
homepage.

DESIGN SYSTEM — follow exactly:

Typeface: a geometric humanist sans for body and labels. For every large
display line use a high-contrast serif-adjacent display face. Display lines
are set large, weight around 525, letter-spacing -0.022em.

Colours:
  paper      #ffffff      text        #1f1f1f
  hairline   #e6e6e6      muted text  #6b6b6b
  saffron    #f9730c      amber       #ffb053
  indigo     #3333cc      periwinkle  #a5bbfc
  lime       #b7d44a
  black endcard #000000

THE CORE MOTIF: a scalloped petal shape, like a flower with eight rounded
lobes, or a Mughal arch repeated around a circle. Use it three ways:
  1. As a horizontal wipe that travels across frame left to right and
     uncovers the text behind it.
  2. As a container holding a line of display type, filled with a soft
     two-stop gradient.
  3. As a full-bleed colour field with a wordmark ghosted inside at low
     opacity.

THE SIGNATURE SHOT, used three times: a short phrase sits on the left of a
near-white frame. The scalloped shape sweeps in from the right in a solid
colour and, as it travels, uncovers the second half of the sentence. The
sentence completes as the shape moves. Saffron the first time, lime the
second, periwinkle the third.

COLOUR JOURNEY across the film: near-white, then saffron, then lime, then
periwinkle, then black for the end card.

MOTION: calm and generous. Long holds. Nothing bounces, nothing is springy.
Ease everything with cubic-bezier(0.2, 0, 0, 1) over roughly 0.5 seconds.
Elements enter by sliding a short distance and fading, never by scaling from
zero. Cross-dissolves between acts, hard cuts inside an act.

LAYOUT: enormous negative space. One idea per frame. Never more than one
display line on screen at a time. UI cards float on near-white with a very
soft shadow and an 18px corner radius.

AUDIO: a continuous instrumental bed, calm, warm, no drums until the second
act, nothing triumphant. Under a narrator reading the attached script. Leave
the narration clear and forward in the mix.

SUBTITLES: burn in the narration as white bold text at the bottom centre.

DO NOT: use stock-footage gloss, use drop shadows on text, use more than one
font family for display, use bright primary blue, use any emoji, use any
bouncing or elastic easing, put more than one headline on screen at once.

Then follow the scene-by-scene script and voiceover I am providing.
```

Paste the three acts above after it.

---

## What you still have to make yourself

Two screen recordings. Nothing can fake these and they are the most
convincing seconds in the film:

1. **Signing up for the Sarvam API**, timer running in the corner, from
   landing page to first successful call. Record it genuinely, hesitation
   included. That hesitation is the whole point of Act 1.
2. **The dashboard**, even a rough one, with those five metrics on it.

Everything else in the film can be generated.
