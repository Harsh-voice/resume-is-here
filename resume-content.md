# Resume — content, ready to set as a PDF

One page. Plain. The site does the arguing; this gets filed and parsed.

Two things still needed from you, marked `[?]` below: your phone number, and
the ElevenLabs / Sarvam question. The link assumes the Vercel project is
renamed to `portfolio-is-here`.

---

## HEADER

```
Harsh Bomble
Growth Marketing Intern · Mumbai, open to relocate to Bengaluru

[?] phone   ·   harshbomble.work@gmail.com
linkedin.com/in/harsh-bomble   ·   portfolio-is-here.vercel.app
```

The portfolio link goes **in the header, not at the bottom**. It is the most
valuable line on the page and it should be visible in the first two seconds.

---

## ONE LINE, UNDER THE HEADER

> Growth and performance marketer who already builds on Sarvam. **41+ political
> campaigns** across Maharashtra on **₹7.6L of Meta spend**, **₹75.2L in sales at
> roughly 10x** for PK Films India, **50+ sites** shipped for Chakan MIDC
> companies, and a voice AI product running on **Sarvam's APIs** under the Sarvam
> AI Startup Program.

No "objective". No "seeking a challenging role". One sentence of facts.

---

## EXPERIENCE

### DialVola — Founder
*AI voice call centre · Mar 2026 – Oct 2026*

- Built and sold an AI voice call centre to **22+ astrologers in Pune**. Found
  the segment, wrote the pitch, closed every client personally.
- Built on **Sarvam's APIs** under the **Sarvam AI Startup Program**. `[?]`
- Wrote an **OpenAI-compatible shim** to remove the switching cost from OpenAI,
  the same friction that keeps developers on their first provider.
- The product worked and distribution did not. That gap is why I am applying
  for this role rather than starting another company.

### Nexussv — Co-Founder
*Full-time · Aug 2023 – Feb 2026*

- Ran **41+ political campaigns** across Maharashtra, including **MLA and MP
  election campaigns for the NCP**.
- Managed **₹7.6 lakh of Meta ad spend** delivering **16.7M impressions**. Audience targeting, vernacular creative, daily
  optimisation against a fixed polling date.
- Grew the agency to **23+ clients** over two and a half years, including **50+
  sites** for companies across Chakan MIDC.
- Client and campaign specifics withheld under agency confidentiality.

### PK Films — Growth & Performance Marketing
*Part-time · May 2025 – Dec 2025*

- Drove **₹75.2L in sales on ₹7.6 lakh of ad spend** across WhatsApp Ads and
  Google Ads, roughly a **10x return**.
- Owned the full paid funnel: targeting, creative, WhatsApp conversation flow,
  conversion tracking.

### India Post — Campaign Design & Creative
*Project engagement · Sep 2024*

- Produced design and creative for a campaign serving offline offices across
  rural Pune, marketing to audiences reached in person rather than online.

---

## EDUCATION

**B.Tech, Data Science** — Department of Technology, Savitribai Phule Pune
University · Third year

---

## SKILLS

Keep them grouped. A flat list of nineteen tools reads as noise.

- **Performance** — Meta Ads, Google Ads, WhatsApp Business, Meta Ads Manager
- **AI stack** — Sarvam, OpenAI, Claude, Gemini, ElevenLabs, Hugging Face
- **Analytics** — Google Search Console, conversion tracking, attribution design
- **Build** — Webflow, Figma, vibe-coded landing pages
- **Creative** — Canva, Photoshop, Premiere Pro, Jitter

## LANGUAGES

Marathi (native) · Hindi (fluent) · English (working)

Worth keeping for this application specifically. Sarvam builds for Indian
languages, and you have run paid campaigns in Marathi.

---

# Rules this follows

**Leave out**, even though Indian templates ask for them: photo, date of birth,
father's name, full address, marital status, hobbies, "references available on
request", and the signed declaration. Each one costs a line and buys nothing.

**One page.** You have four roles and a degree in progress. Two pages reads as
padding at this stage.

**Real text, not an image.** Export as text-based PDF. Tracking systems cannot
read a screenshot of a resume, and some reject what they cannot parse.

**No columns, no text boxes, no tables** for the main content. They parse out of
order. One column, top to bottom.

**Standard headings.** `Experience`, `Education`, `Skills`. Parsers look for
exactly these words. Clever headings get skipped.

**File name:** `Harsh-Bomble-Growth-Marketing-Intern.pdf`. Recruiters have a
hundred files called `resume.pdf`.

---

# The numbers decision

I have used the **proven** figures above, not the page's headline ones:

| | Page says | Receipts prove | Used here |
|---|---|---|---|
| Nexussv Meta spend | ₹14 lakh | ₹7.63 lakh | **₹7.6 lakh** |
| Reach claim | 14M+ views | 16.7M impressions | **16.7M impressions** |

A PDF gets forwarded, saved and read closely by people who do arithmetic. Put
the defensible number here. If the larger figures are real and you have the
accounts to show, send those screenshots and I will raise it.

One thing to check: ₹7.6 lakh now appears for both Nexussv Meta spend and PK
Films spend. If those are genuinely two different ₹7.6L figures, fine, but it
reads like a copy-paste error. Worth separating with exact amounts.

---

# Built

`resume.html` sets this in the site's own theme and prints to
`Harsh-Bomble-Growth-Marketing-Intern.pdf`, one A4 page.

```
node -e "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
const p=await b.newPage();await p.goto('file://'+process.cwd()+'/resume.html',{waitUntil:'networkidle'});
await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.pdf({path:'Harsh-Bomble-Growth-Marketing-Intern.pdf',format:'A4',printBackground:true,
margin:{top:'0',right:'0',bottom:'0',left:'0'}});await b.close();})()"
```

Search and replace `portfolio-is-here.vercel.app` in `resume.html` once the site is on Vercel,
then re-run that command.
