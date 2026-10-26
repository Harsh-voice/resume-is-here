# Image slots

Three slots in the "Selected work" section of `index.html`.
Portrait **4:5**, about **1000 x 1250 px**. JPG or PNG.

To use one, find the slot in `index.html` and replace

    <div class="sample-ph"> ... </div>

with

    <img src="samples/01-campaign.jpg" alt="Marathi campaign creative">

The caption under each slot is a separate `<p class="sample-cap">` — edit the text there.

| slot | file | what it should show |
|---|---|---|
| 01 | `01-campaign.jpg` | Real Marathi ad creative from the MLA campaign |
| 02 | `02-adsmanager.jpg` | Ads Manager results screen behind the 10x |
| 03 | `03-dialvola.jpg`  | Dialvola as customers saw it |

Real screenshots beat generated images here. If you use Ads Manager
screenshots, blur or crop any client name, account ID or phone number
you do not have permission to publish.

---

## Which of these to generate, and which not to

**01 — Campaign creative: use your real asset.**
Do not generate a Marathi political ad for the NCP. A synthetic ad for a real
party, even as portfolio filler, is the kind of image that causes problems if
it travels. You made real creative; use it.

**02 — Ads Manager: must be a real screenshot.**
A generated dashboard showing ₹7.6L spend and ₹75.2L sales would be invented
evidence of a real result. Screenshot the actual account and blur the client
name, account ID and any phone number.

**03 — Dialvola: fine to generate.**
It is your own product and nothing is being claimed about results. Prompt:

> A clean product interface mockup for an AI voice calling service for small
> businesses in India. Portrait 4:5. Single screen on a plain near-white
> background (#f9f9f9). Shows a call-in-progress view: a live transcript in
> Devanagari and Latin script, a waveform, call duration, and a short list of
> recent calls. Minimal flat UI, thin 1px light-grey borders, 16px rounded
> corners, generous whitespace, one indigo accent (#3333cc), everything else
> greyscale. Soft even lighting, no 3D, no gradients, no stock-photo people,
> no logos, no lens flare. Editorial product-shot feel.

Add `?v=2` to the `src` if you replace an image and the old one is cached.
