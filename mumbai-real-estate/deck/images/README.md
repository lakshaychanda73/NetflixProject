# Photographs

Drop a file here named after its slot and it is cropped, resized and placed on
the next build. Any of `.jpg .jpeg .png .webp .heic .tif`.

| Filename | Lands on | Must show |
|---|---|---|
| `s1_corridor.jpg` | Slide 1, wide band under the stat row | The Eastern & Central corridor at scale — the Powai golden-hour panorama |
| `s5_corridor.jpg` | Slide 5, tall rail beside the priced ladder | Powai lake with the Hiranandani towers — the head of the six-locality spine |
| `s12_founder.jpg` | Slide 12, beside the Sheesham P&L | The founder portrait |
| `s12_jaipur.jpg` | Slide 12, under the portrait (optional) | A Chanda Properties site, scheme or plot — **not** a fort, a palace or a skyline |

```bash
cd ../build
python3 images.py     # shows which slots are filled, and places them
make all              # rebuild the deck PDF
```

An empty slot is not a hole — the slide falls back to its typography-led layout
and still looks deliberate. **Leave a slot empty rather than fill it with a
picture that does not support the argument on that slide.**

## What does not go here

- **Anything watermarked** or credited to a third party — Shutterstock, "© Beautiful
  Jaipur", a photographer's overlay. A deck that ships someone else's watermark
  reads as a deck assembled from search results.
- **South Mumbai landmarks** — the Gateway of India, the Taj, Rajabai Tower.
  Slide 5 argues *against* entering South Mumbai (it scores 4.76, last of six).
  A postcard of Colaba on a deck that recommends Bhandup undercuts its own case.
- **Tourist Jaipur** — Hawa Mahal, Amber, Nahargarh. The Jaipur in this story is
  a market the family has worked for 24 years, not a destination.

Photographs of the corridor we actually work, sites we actually visit and
people who actually run the business are evidence. Everything else is decoration.
