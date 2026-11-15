# My Baby — Romantic Purple & Tulip Website 🌷💜

A personalized, romantic website created as a dedicated gift for your girlfriend. Designed entirely around her favorite color **PURPLE** and featuring delicate, blossoming **TULIP** motifs throughout.

---

## 🎨 Theme & Color Palette

The site uses a romantic color scheme with smooth gradients and glassmorphism:

- **Primary Lavender:** `#B57EDC`
- **Soft Lilac:** `#D8B4F8`
- **Accent Deep Purple:** `#7B2CBF`
- **Light Background:** `#FAF7FF` (Lavender White)
- **Soft Pink:** `#F5D9F2`
- **White:** `#FFFFFF`
- **Royal / Midnight Purple:** `#3C096C` / `#240046`

---

## 🌷 Decorative Tulip Assets

All requested decorative assets are included in `images/decorations/`:
- `images/decorations/purple-tulip.png` & `.svg` — Blooming purple tulip vector illustration with gradient petals and soft dewdrops.
- `images/decorations/tulip-bouquet.png` & `.svg` — Romantic purple tulip bouquet tied with a lilac ribbon bow.
- `images/decorations/tulip-corner.svg` — Corner flourish used on profile frames and romantic letterhead.
- `images/decorations/tulip-pattern.svg` — Seamless subtle tulip pattern used for section backgrounds.
- `images/decorations/tulip-seal.svg` — Embossed purple wax seal with a tulip emblem for the love letter envelope.

---

## ✨ Features & Sections

1. **Floating Falling Petals Canvas:**
   - Soft purple and pink petals and miniature tulips gracefully drift across the screen.
   - Responds to mouse breeze with interactive toggle in navigation bar (`Petals: On/Off`).

2. **Romantic Ambient Music Box (Web Audio API):**
   - Synthesizes a gentle, soothing romantic lullaby using native Web Audio oscillators (zero external dependencies required!).
   - Can be toggled on/off at any time via the `Play Melody` button in the navigation bar.

3. **Hero Section:**
   - Multi-stop purple gradient with glowing ambient orbs.
   - Romantic headline: *"In a Field of Roses, You'll Always Be My Purple Tulip"*.
   - Live Days Together Counter (updating every second with days, hours, minutes, seconds).
   - "Open My Love Letter" and "Explore Our Garden" call-to-actions.

4. **About Her Section:**
   - Profile card with 4 ornate tulip corner flourishes.
   - Nickname tags (*"My Purple Tulip"*, *"Sweet Babygirl"*, *"My Safe Place"*, etc.).
   - Her Favorite Things grid (Purple shades, Tulips, Cozy blankets, Sweet habits).

5. **Photo Carousel Section:**
   - White and soft lilac glass cards with glowing purple prev/next controls and pill dots.
   - Touch swipe support for phones/tablets, keyboard arrows, and pause on hover.
   - Click any photo to open it in full view within the romantic Lightbox modal.

6. **Video Section:**
   - Soft purple gradient container with tulip borders.
   - Custom romantic video wrapper, play button, and romantic quote banner.
   - Easy file picker button to select and play your personal `video.mp4` clip.

7. **Things I Love About Her Section:**
   - 6 lavender cards with heart and tulip icons, hover lift animations, and personal sweet messages.

8. **Our Memories (Scrapbook Gallery):**
   - Polaroid-style cards naturally tilted with washi tape details and tulip stickers.
   - Interactive category filter buttons: *All Keepsakes*, *Sweet Dates*, *Adventures*, *Milestones*.

9. **Timeline Section:**
   - Purple gradient central timeline with glowing heart-shaped markers.
   - Chronological story chapters celebrating how your love bloomed from day one to eternity.

10. **Interactive Love Letter Section:**
    - Lavender envelope design sealed with an authentic purple tulip wax emblem.
    - Clicking the seal smoothly breaks the seal and unfolds the stationery letter.
    - Elegant handwritten script typography, sincere romantic vows, and a *"Seal Letter Back"* button.

11. **Footer:**
    - Deep royal purple gradient with tulip bouquet emblem, romantic quote, and smooth *"Back to Garden Top"* button.

---

## 🚀 How to View the Website

### Option 1: Direct Double Click
Simply double-click `index.html` in your file explorer to open it directly in Chrome, Edge, Safari, or Firefox.

### Option 2: Local Python Server
Run the following command in PowerShell:
```powershell
python -m http.server 8000
```
Then open your browser to `http://localhost:8000`.

---

## 🛠 How to Customize

- **Change Anniversary Date:** In `js/main.js`, update `defaultStartDate` or set `localStorage.setItem('anniversary_date', 'YYYY-MM-DD')`.
- **Change Photos:** Replace files in `images/photos/` or link your own images in `index.html`.
- **Change Video:** Drop your personal video named `video.mp4` into the project root directory or click *"Choose Video Clip"*.
