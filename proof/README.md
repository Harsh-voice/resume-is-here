# Receipts — screenshot slots

Three slots on the page, in `#proof`. Layout is one full-width lead plus two
side by side.

| File | Slot | Rendered | Caption |
|---|---|---|---|
| `01-meta-pivot.webp` | lead, full width | 1198 × 673 | 779 campaigns · 9.75M impressions · 2.99M reach · ₹3.46L spent |
| `02-meta-campaigns.webp` | bottom left | 587 × 329 | 40 campaigns · 699K reach · ₹1.72L spent · ₹92 CPM |
| `03-meta-leads.webp` | bottom right | 587 × 329 | 34 campaigns · 1.94M reach · 6.99M impressions · ₹2.45L spent |

## Swapping one out

Export at **16:9** — 1920 × 1080 is ideal. The slot is `aspect-ratio: 16/9`
with `object-fit: contain`, so nothing gets cropped; an image at another ratio
will letterbox against white rather than lose its totals row.

Drop the file in here under the same name and rebuild. Each slot links to the
full-size file, so the two smaller ones stay readable on click.

## Before you export

- Blur or crop campaign names and the ad account name.
- Check the top-left account switcher and any avatars.
- Leave the **totals row** alone — it is the thing being shown.
- Set the date range deliberately; "Maximum" defaults back to the account's
  first ever campaign, which may predate the role you are claiming.
