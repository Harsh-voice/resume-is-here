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

# Script and shot list

## The six beats

| Time | Beat |
|---|---|
| 0:00–0:02 | Title. `A 30-DAY PLAN` in mono above **Default habit** at 128px. |
| 0:02–0:12 | Three pills arrive one at a time: ChatGPT, Gemini, Claude. An indigo ring lands on ChatGPT, then **Still opened first.** drops beneath them. |
| 0:12–0:20 | A panel builds row by row: Startup Program window `6–12 months` · SDK written against `Once` · Rewritten afterwards `Rarely` · So the real product is `The habit`. |
| 0:20–0:27 | Lime scallop sweeps in. **₹1L, three weeks** ⟩ *three channels, three pages*. Then three channel cards deal out with their budget bars filling. |
| 0:27–0:34 | Periwinkle scallop. **Day 30** ⟩ *one metric, one kill rule*. Four gate tiles land: ₹15k, Day 30, Daily, 3. |
| 0:34–0:41 | Clears to white. **Not signups. Developers still calling on day thirty.** Black end card. |

## The narration

99 words, 165 words per minute. In `voice-script.txt` on its own, and in
`voice-cues.md` with the start time of each line.

See `film-brief.md` for the palette, the type settings and a prompt block if
you ever want to rebuild this in another tool.
