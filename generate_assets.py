import os
import math
from PIL import Image, ImageDraw, ImageFilter

os.makedirs('images/decorations', exist_ok=True)
os.makedirs('images/photos', exist_ok=True)

# 1. purple-tulip.svg
purple_tulip_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 500" width="100%" height="100%">
  <defs>
    <linearGradient id="stemGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4A6B48"/>
      <stop offset="50%" stop-color="#688F66"/>
      <stop offset="100%" stop-color="#8DB58A"/>
    </linearGradient>
    <linearGradient id="leafGradL" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#385437"/>
      <stop offset="60%" stop-color="#638C61"/>
      <stop offset="100%" stop-color="#8CB48A"/>
    </linearGradient>
    <linearGradient id="leafGradR" x1="100%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#385437"/>
      <stop offset="60%" stop-color="#638C61"/>
      <stop offset="100%" stop-color="#9BC499"/>
    </linearGradient>
    <linearGradient id="petalBack" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#3C096C"/>
      <stop offset="50%" stop-color="#5A189A"/>
      <stop offset="100%" stop-color="#7B2CBF"/>
    </linearGradient>
    <linearGradient id="petalLeft" x1="0%" y1="100%" x2="80%" y2="0%">
      <stop offset="0%" stop-color="#5A189A"/>
      <stop offset="40%" stop-color="#7B2CBF"/>
      <stop offset="80%" stop-color="#B57EDC"/>
      <stop offset="100%" stop-color="#D8B4F8"/>
    </linearGradient>
    <linearGradient id="petalRight" x1="100%" y1="100%" x2="20%" y2="0%">
      <stop offset="0%" stop-color="#481173"/>
      <stop offset="45%" stop-color="#7B2CBF"/>
      <stop offset="85%" stop-color="#B57EDC"/>
      <stop offset="100%" stop-color="#F5D9F2"/>
    </linearGradient>
    <linearGradient id="petalCenter" x1="50%" y1="100%" x2="50%" y2="0%">
      <stop offset="0%" stop-color="#6E25A8"/>
      <stop offset="30%" stop-color="#9D4EDD"/>
      <stop offset="70%" stop-color="#B57EDC"/>
      <stop offset="95%" stop-color="#E9D5FF"/>
      <stop offset="100%" stop-color="#FAF7FF"/>
    </linearGradient>
    <radialGradient id="tulipGlow" cx="50%" cy="40%" r="50%">
      <stop offset="0%" stop-color="#D8B4F8" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#B57EDC" stop-opacity="0"/>
    </radialGradient>
    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <circle cx="200" cy="180" r="95" fill="url(#tulipGlow)" />

  <!-- Stem -->
  <path d="M200,230 Q206,340 196,470" fill="none" stroke="url(#stemGrad)" stroke-width="12" stroke-linecap="round"/>

  <!-- Left Leaf -->
  <path d="M196,410 C145,375 105,310 110,230 C135,280 170,340 197,365 Z" fill="url(#leafGradL)" opacity="0.95"/>
  <!-- Right Leaf -->
  <path d="M197,430 C242,395 290,335 285,200 C262,275 230,345 197,385 Z" fill="url(#leafGradR)" opacity="0.95"/>

  <!-- Back Petals -->
  <path d="M175,170 C160,110 185,70 200,60 C215,70 240,110 225,170 Z" fill="url(#petalBack)"/>
  <path d="M152,185 C132,130 148,80 170,72 C185,120 180,170 168,198 Z" fill="url(#petalBack)" opacity="0.85"/>
  <path d="M248,185 C268,130 252,80 230,72 C215,120 220,170 232,198 Z" fill="url(#petalBack)" opacity="0.85"/>

  <!-- Left Main Petal -->
  <path d="M195,240 C145,235 120,175 132,118 C148,88 175,85 186,102 C164,148 174,198 195,240 Z" fill="url(#petalLeft)"/>

  <!-- Right Main Petal -->
  <path d="M205,240 C255,235 280,175 268,118 C252,88 225,85 214,102 C236,148 226,198 205,240 Z" fill="url(#petalRight)"/>

  <!-- Center Front Petal -->
  <path d="M200,248 C162,238 152,160 174,102 C186,76 214,76 226,102 C248,160 238,238 200,248 Z" fill="url(#petalCenter)" filter="url(#softGlow)"/>

  <!-- Center Highlight Rib -->
  <path d="M200,238 C188,180 190,125 200,90 C210,125 212,180 200,238 Z" fill="#FFFFFF" opacity="0.25"/>

  <!-- Dew drops -->
  <circle cx="186" cy="140" r="3.5" fill="#FFFFFF" opacity="0.8"/>
  <circle cx="190" cy="137" r="1.5" fill="#FFFFFF" opacity="0.95"/>
  <circle cx="218" cy="170" r="2.8" fill="#FAF7FF" opacity="0.7"/>
</svg>'''

with open('images/decorations/purple-tulip.svg', 'w', encoding='utf-8') as f:
    f.write(purple_tulip_svg)

# 2. tulip-bouquet.svg
tulip_bouquet_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 650" width="100%" height="100%">
  <defs>
    <linearGradient id="bqStem" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4B6B48"/>
      <stop offset="100%" stop-color="#8BB588"/>
    </linearGradient>
    <linearGradient id="bqLeaf" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#385437"/>
      <stop offset="70%" stop-color="#648E62"/>
      <stop offset="100%" stop-color="#9BC499"/>
    </linearGradient>
    <linearGradient id="bqDark" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#3C096C"/>
      <stop offset="100%" stop-color="#7B2CBF"/>
    </linearGradient>
    <linearGradient id="bqMed" x1="0%" y1="100%" x2="50%" y2="0%">
      <stop offset="0%" stop-color="#5A189A"/>
      <stop offset="50%" stop-color="#7B2CBF"/>
      <stop offset="100%" stop-color="#B57EDC"/>
    </linearGradient>
    <linearGradient id="bqLight" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7B2CBF"/>
      <stop offset="50%" stop-color="#B57EDC"/>
      <stop offset="90%" stop-color="#D8B4F8"/>
      <stop offset="100%" stop-color="#FAF7FF"/>
    </linearGradient>
    <linearGradient id="bqSoftPink" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7B2CBF"/>
      <stop offset="60%" stop-color="#D8B4F8"/>
      <stop offset="100%" stop-color="#F5D9F2"/>
    </linearGradient>
    <linearGradient id="ribbonGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#9D4EDD"/>
      <stop offset="40%" stop-color="#D8B4F8"/>
      <stop offset="80%" stop-color="#B57EDC"/>
      <stop offset="100%" stop-color="#7B2CBF"/>
    </linearGradient>
    <radialGradient id="bouquetGlow" cx="50%" cy="35%" r="50%">
      <stop offset="0%" stop-color="#D8B4F8" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#FAF7FF" stop-opacity="0"/>
    </radialGradient>
    <filter id="bqGlow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <ellipse cx="300" cy="220" rx="220" ry="180" fill="url(#bouquetGlow)"/>

  <!-- Stems gathered -->
  <g stroke="url(#bqStem)" stroke-width="9" stroke-linecap="round">
    <path d="M190,260 C240,360 270,440 280,590"/>
    <path d="M240,240 C260,350 285,440 295,590"/>
    <path d="M300,210 C300,340 300,440 300,600"/>
    <path d="M360,240 C340,350 315,440 305,590"/>
    <path d="M410,260 C360,360 330,440 320,590"/>
    <path d="M220,300 C250,380 275,450 288,580"/>
    <path d="M380,300 C350,380 325,450 312,580"/>
  </g>

  <!-- Large lush leaves -->
  <path d="M280,480 C190,440 100,350 90,220 C130,290 200,380 285,440 Z" fill="url(#bqLeaf)" opacity="0.95"/>
  <path d="M320,480 C410,440 500,350 510,220 C470,290 400,380 315,440 Z" fill="url(#bqLeaf)" opacity="0.95"/>
  <path d="M290,470 C240,410 180,310 200,180 C230,270 270,360 295,440 Z" fill="url(#bqLeaf)" opacity="0.85"/>
  <path d="M310,470 C360,410 420,310 400,180 C370,270 330,360 305,440 Z" fill="url(#bqLeaf)" opacity="0.85"/>

  <!-- TULIP 1 (Far Left - Deep Violet) -->
  <g transform="translate(140, 200) rotate(-22) scale(0.68)">
    <path d="M50,150 C10,90 25,40 50,30 C75,40 90,90 50,150 Z" fill="url(#bqDark)"/>
    <path d="M50,150 C0,140 -15,80 5,45 C25,18 45,30 50,150 Z" fill="url(#bqMed)"/>
    <path d="M50,150 C100,140 115,80 95,45 C75,18 55,30 50,150 Z" fill="url(#bqMed)"/>
    <path d="M50,155 C20,145 15,85 35,45 C45,25 65,25 75,55 C90,105 75,150 50,155 Z" fill="url(#bqLight)"/>
  </g>

  <!-- TULIP 2 (Far Right - Deep Violet) -->
  <g transform="translate(410, 200) rotate(22) scale(0.68)">
    <path d="M50,150 C10,90 25,40 50,30 C75,40 90,90 50,150 Z" fill="url(#bqDark)"/>
    <path d="M50,150 C0,140 -15,80 5,45 C25,18 45,30 50,150 Z" fill="url(#bqMed)"/>
    <path d="M50,150 C100,140 115,80 95,45 C75,18 55,30 50,150 Z" fill="url(#bqMed)"/>
    <path d="M50,155 C20,145 15,85 35,45 C45,25 65,25 75,55 C90,105 75,150 50,155 Z" fill="url(#bqSoftPink)"/>
  </g>

  <!-- TULIP 3 (Mid Left - Soft Lilac) -->
  <g transform="translate(200, 130) rotate(-11) scale(0.8)">
    <path d="M50,150 C10,90 25,40 50,30 C75,40 90,90 50,150 Z" fill="url(#bqDark)"/>
    <path d="M50,150 C-5,140 -15,75 8,40 C28,15 48,25 50,150 Z" fill="url(#bqMed)"/>
    <path d="M50,150 C105,140 115,75 92,40 C72,15 52,25 50,150 Z" fill="url(#bqMed)"/>
    <path d="M50,155 C20,145 15,80 35,40 C45,20 65,20 75,50 C92,100 78,150 50,155 Z" fill="url(#bqLight)"/>
  </g>

  <!-- TULIP 4 (Mid Right - Soft Pinkish Lavender) -->
  <g transform="translate(350, 130) rotate(11) scale(0.8)">
    <path d="M50,150 C10,90 25,40 50,30 C75,40 90,90 50,150 Z" fill="url(#bqDark)"/>
    <path d="M50,150 C-5,140 -15,75 8,40 C28,15 48,25 50,150 Z" fill="url(#bqMed)"/>
    <path d="M50,150 C105,140 115,75 92,40 C72,15 52,25 50,150 Z" fill="url(#bqMed)"/>
    <path d="M50,155 C20,145 15,80 35,40 C45,20 65,20 75,50 C92,100 78,150 50,155 Z" fill="url(#bqSoftPink)"/>
  </g>

  <!-- TULIP 5 (Top Center Crown - Glorious Radiant Lavender) -->
  <g transform="translate(265, 75) scale(0.85)">
    <path d="M50,150 C10,90 25,35 50,25 C75,35 90,90 50,150 Z" fill="url(#bqDark)"/>
    <path d="M50,150 C-10,140 -20,70 8,35 C30,10 50,20 50,150 Z" fill="url(#bqMed)"/>
    <path d="M50,150 C110,140 120,70 92,35 C70,10 50,20 50,150 Z" fill="url(#bqMed)"/>
    <path d="M50,155 C18,145 12,75 35,35 C46,15 66,15 78,45 C95,95 80,150 50,155 Z" fill="url(#bqLight)"/>
    <circle cx="48" cy="70" r="3" fill="#FFFFFF" opacity="0.8"/>
  </g>

  <!-- TULIP 6 (Front Center Hero Bloom) -->
  <g transform="translate(255, 180) scale(1.05)" filter="url(#bqGlow)">
    <path d="M50,150 C10,90 25,35 50,25 C75,35 90,90 50,150 Z" fill="url(#bqDark)"/>
    <path d="M50,150 C-15,138 -20,68 8,32 C30,8 50,18 50,150 Z" fill="url(#bqMed)"/>
    <path d="M50,150 C115,138 120,68 92,32 C70,8 50,18 50,150 Z" fill="url(#bqMed)"/>
    <path d="M50,155 C16,144 10,70 34,30 C46,10 66,10 78,40 C96,92 82,150 50,155 Z" fill="url(#bqLight)"/>
    <path d="M50,150 C44,110 46,70 50,45 C54,70 56,110 50,150 Z" fill="#FFFFFF" opacity="0.3"/>
    <circle cx="46" cy="65" r="3.5" fill="#FFFFFF" opacity="0.85"/>
    <circle cx="58" cy="85" r="2" fill="#FAF7FF" opacity="0.7"/>
  </g>

  <!-- Ribbon Tie & Bow -->
  <!-- Back Ribbon tails -->
  <path d="M260,490 C230,530 190,570 200,630 C220,635 240,580 280,510 Z" fill="url(#ribbonGrad)" opacity="0.9"/>
  <path d="M340,490 C370,530 410,570 400,630 C380,635 360,580 320,510 Z" fill="url(#ribbonGrad)" opacity="0.9"/>
  <!-- Wrap Band -->
  <ellipse cx="300" cy="485" rx="42" ry="16" fill="url(#ribbonGrad)"/>
  <!-- Bow loops -->
  <path d="M300,485 C270,440 210,450 230,490 C245,510 285,495 300,485 Z" fill="url(#ribbonGrad)"/>
  <path d="M300,485 C330,440 390,450 370,490 C355,510 315,495 300,485 Z" fill="url(#ribbonGrad)"/>
  <!-- Knot -->
  <circle cx="300" cy="485" r="14" fill="#5A189A"/>
  <circle cx="300" cy="485" r="10" fill="url(#ribbonGrad)"/>

  <!-- Sparkle Stars -->
  <path d="M160,110 Q160,125 145,125 Q160,125 160,140 Q160,125 175,125 Q160,125 160,110 Z" fill="#F5D9F2" opacity="0.8"/>
  <path d="M430,90 Q430,105 415,105 Q430,105 430,120 Q430,105 445,105 Q430,105 430,90 Z" fill="#D8B4F8" opacity="0.85"/>
  <path d="M220,40 Q220,55 205,55 Q220,55 220,70 Q220,55 235,55 Q220,55 220,40 Z" fill="#FAF7FF" opacity="0.9"/>
  <path d="M375,50 Q375,63 362,63 Q375,63 375,76 Q375,63 388,63 Q375,63 375,50 Z" fill="#FFFFFF" opacity="0.85"/>
</svg>'''

with open('images/decorations/tulip-bouquet.svg', 'w', encoding='utf-8') as f:
    f.write(tulip_bouquet_svg)

# 3. tulip-corner.svg
tulip_corner_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <defs>
    <linearGradient id="crnGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7B2CBF"/>
      <stop offset="60%" stop-color="#B57EDC"/>
      <stop offset="100%" stop-color="#D8B4F8"/>
    </linearGradient>
    <linearGradient id="crnGrad2" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#5A189A"/>
      <stop offset="100%" stop-color="#F5D9F2"/>
    </linearGradient>
    <linearGradient id="crnStem" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#588157"/>
      <stop offset="100%" stop-color="#8DB58A"/>
    </linearGradient>
  </defs>

  <!-- Corner Flourish Vines -->
  <path d="M8,180 C8,80 80,8 180,8" fill="none" stroke="url(#crnGrad1)" stroke-width="2.5" stroke-dasharray="4 3" opacity="0.6"/>
  <path d="M12,150 C12,65 65,12 150,12" fill="none" stroke="url(#crnStem)" stroke-width="2.5" stroke-linecap="round"/>

  <!-- Swirls -->
  <path d="M12,150 C12,175 30,175 30,160 C30,145 18,148 18,155" fill="none" stroke="url(#crnStem)" stroke-width="2" stroke-linecap="round"/>
  <path d="M150,12 C175,12 175,30 160,30 C145,30 148,18 155,18" fill="none" stroke="url(#crnStem)" stroke-width="2" stroke-linecap="round"/>

  <!-- Corner Leaves -->
  <path d="M35,115 C20,95 25,75 42,70 C48,90 42,105 35,115 Z" fill="#648E62" opacity="0.8"/>
  <path d="M115,35 C95,20 75,25 70,42 C90,48 105,42 115,35 Z" fill="#648E62" opacity="0.8"/>

  <!-- Main Corner Tulip (Center diagonal) -->
  <g transform="translate(38, 38) rotate(45) scale(0.38)">
    <path d="M50,130 C20,80 30,40 50,30 C70,40 80,80 50,130 Z" fill="#5A189A"/>
    <path d="M50,130 C5,120 -10,70 10,40 C30,15 45,25 50,130 Z" fill="url(#crnGrad2)"/>
    <path d="M50,130 C95,120 110,70 90,40 C70,15 55,25 50,130 Z" fill="url(#crnGrad2)"/>
    <path d="M50,135 C22,125 18,75 35,38 C45,18 65,18 75,45 C90,85 78,130 50,135 Z" fill="url(#crnGrad1)"/>
  </g>

  <!-- Little Bud on Left -->
  <g transform="translate(16, 95) rotate(-15) scale(0.22)">
    <path d="M50,130 C20,80 30,40 50,30 C70,40 80,80 50,130 Z" fill="#7B2CBF"/>
    <path d="M50,135 C25,125 20,75 35,40 C45,20 65,20 75,45 C85,85 75,130 50,135 Z" fill="url(#crnGrad1)"/>
  </g>

  <!-- Little Bud on Top -->
  <g transform="translate(95, 16) rotate(75) scale(0.22)">
    <path d="M50,130 C20,80 30,40 50,30 C70,40 80,80 50,130 Z" fill="#7B2CBF"/>
    <path d="M50,135 C25,125 20,75 35,40 C45,20 65,20 75,45 C85,85 75,130 50,135 Z" fill="url(#crnGrad1)"/>
  </g>

  <!-- Shimmering Dots -->
  <circle cx="82" cy="72" r="2.5" fill="#B57EDC" opacity="0.7"/>
  <circle cx="72" cy="82" r="2" fill="#D8B4F8" opacity="0.8"/>
  <circle cx="100" cy="55" r="1.5" fill="#7B2CBF" opacity="0.6"/>
  <circle cx="55" cy="100" r="1.5" fill="#7B2CBF" opacity="0.6"/>
</svg>'''

with open('images/decorations/tulip-corner.svg', 'w', encoding='utf-8') as f:
    f.write(tulip_corner_svg)

# 4. tulip-pattern.svg
tulip_pattern_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="120" height="120" viewBox="0 0 120 120">
  <defs>
    <linearGradient id="patGrad" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7B2CBF" stop-opacity="0.14"/>
      <stop offset="60%" stop-color="#B57EDC" stop-opacity="0.11"/>
      <stop offset="100%" stop-color="#D8B4F8" stop-opacity="0.08"/>
    </linearGradient>
    <linearGradient id="patStem" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#648E62" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#8DB58A" stop-opacity="0.08"/>
    </linearGradient>
  </defs>

  <!-- Subtle grid pattern -->
  <!-- Center tulip -->
  <g transform="translate(60, 48) scale(0.24)">
    <path d="M0,0 Q2,35 -2,70" fill="none" stroke="url(#patStem)" stroke-width="4"/>
    <path d="M-2,50 C-18,40 -25,25 -20,10 C-10,20 -2,35 -1,45 Z" fill="url(#patStem)"/>
    <path d="M0,0 C-25,-5 -22,-45 0,-60 C22,-45 25,-5 0,0 Z" fill="url(#patGrad)"/>
    <path d="M0,0 C-12,-8 -18,-35 0,-50 C18,-35 12,-8 0,0 Z" fill="url(#patGrad)"/>
  </g>

  <!-- Corner tulips (tileable) -->
  <g transform="translate(0, 0) scale(0.18)">
    <path d="M0,0 C-25,-5 -22,-45 0,-60 C22,-45 25,-5 0,0 Z" fill="url(#patGrad)"/>
  </g>
  <g transform="translate(120, 0) scale(0.18)">
    <path d="M0,0 C-25,-5 -22,-45 0,-60 C22,-45 25,-5 0,0 Z" fill="url(#patGrad)"/>
  </g>
  <g transform="translate(0, 120) scale(0.18)">
    <path d="M0,0 C-25,-5 -22,-45 0,-60 C22,-45 25,-5 0,0 Z" fill="url(#patGrad)"/>
  </g>
  <g transform="translate(120, 120) scale(0.18)">
    <path d="M0,0 C-25,-5 -22,-45 0,-60 C22,-45 25,-5 0,0 Z" fill="url(#patGrad)"/>
  </g>

  <!-- Subtle petal sprinkles -->
  <path d="M25,85 C20,80 25,72 32,76 C35,82 30,88 25,85 Z" fill="url(#patGrad)"/>
  <path d="M95,25 C90,20 95,12 102,16 C105,22 100,28 95,25 Z" fill="url(#patGrad)"/>
  <circle cx="85" cy="88" r="1.5" fill="#B57EDC" opacity="0.12"/>
  <circle cx="35" cy="28" r="1.5" fill="#7B2CBF" opacity="0.12"/>
</svg>'''

with open('images/decorations/tulip-pattern.svg', 'w', encoding='utf-8') as f:
    f.write(tulip_pattern_svg)

# 5. tulip-seal.svg (For Love Letter Envelope Wax Seal)
tulip_seal_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <radialGradient id="waxGrad" cx="40%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#9D4EDD"/>
      <stop offset="45%" stop-color="#7B2CBF"/>
      <stop offset="85%" stop-color="#5A189A"/>
      <stop offset="100%" stop-color="#3C096C"/>
    </radialGradient>
    <filter id="waxShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#240046" flood-opacity="0.4"/>
    </filter>
    <linearGradient id="emboss" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E9D5FF"/>
      <stop offset="60%" stop-color="#D8B4F8"/>
      <stop offset="100%" stop-color="#7B2CBF"/>
    </linearGradient>
  </defs>

  <!-- Organic Wax Seal Outer Rim -->
  <path d="M50,8 C65,7 72,12 82,20 C92,28 94,38 93,50 C92,63 88,74 78,83 C68,92 56,93 47,92 C32,91 22,87 14,76 C6,65 7,52 8,42 C9,30 16,18 26,12 C36,6 42,9 50,8 Z" fill="url(#waxGrad)" filter="url(#waxShadow)"/>

  <!-- Inner Rim Ridge -->
  <circle cx="50" cy="50" r="32" fill="none" stroke="#5A189A" stroke-width="2.5" opacity="0.6"/>
  <circle cx="50" cy="50" r="30" fill="none" stroke="#D8B4F8" stroke-width="1" opacity="0.5"/>

  <!-- Embossed Tulip Emblem -->
  <g transform="translate(50, 48) scale(0.38)">
    <path d="M0,20 Q2,45 0,65" fill="none" stroke="url(#emboss)" stroke-width="5" stroke-linecap="round"/>
    <path d="M0,50 C-15,40 -25,25 -20,8 C-10,18 0,32 0,42 Z" fill="url(#emboss)" opacity="0.8"/>
    <path d="M0,50 C15,40 25,25 20,8 C10,18 0,32 0,42 Z" fill="url(#emboss)" opacity="0.8"/>
    <!-- Petals -->
    <path d="M0,18 C-30,10 -35,-30 -8,-50 C0,-35 0,-10 0,18 Z" fill="url(#emboss)" opacity="0.85"/>
    <path d="M0,18 C30,10 35,-30 8,-50 C0,-35 0,-10 0,18 Z" fill="url(#emboss)" opacity="0.85"/>
    <path d="M0,22 C-18,15 -18,-35 0,-48 C18,-35 18,15 0,22 Z" fill="url(#emboss)"/>
  </g>

  <!-- Wax Highlight -->
  <ellipse cx="40" cy="24" rx="14" ry="7" fill="#FFFFFF" opacity="0.22" transform="rotate(-15, 40, 24)"/>
</svg>'''

with open('images/decorations/tulip-seal.svg', 'w', encoding='utf-8') as f:
    f.write(tulip_seal_svg)

print("SVGs created successfully.")

# Now let's create high-resolution transparent PNGs for purple-tulip.png and tulip-bouquet.png using Pillow
# We'll render them with supersampling (e.g. 1024x1024 downsampled to 512x512) for smooth edges

def create_purple_tulip_png():
    scale = 2
    w, h = 400 * scale, 500 * scale
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Stem
    points = []
    for t in range(101):
        progress = t / 100.0
        # quadratic bezier (200,230) -> (206,340) -> (196,470)
        p0 = (200 * scale, 230 * scale)
        p1 = (206 * scale, 340 * scale)
        p2 = (196 * scale, 470 * scale)
        x = (1 - progress)**2 * p0[0] + 2 * (1 - progress) * progress * p1[0] + progress**2 * p2[0]
        y = (1 - progress)**2 * p0[1] + 2 * (1 - progress) * progress * p1[1] + progress**2 * p2[1]
        points.append((x, y))

    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=(104, 143, 102, 255), width=int(12 * scale))

    # Leaves
    # Left leaf polygon
    left_leaf = [
        (196*scale, 410*scale), (170*scale, 390*scale), (135*scale, 350*scale),
        (110*scale, 280*scale), (110*scale, 230*scale), (135*scale, 275*scale),
        (165*scale, 335*scale), (197*scale, 365*scale)
    ]
    draw.polygon(left_leaf, fill=(99, 140, 97, 240))

    # Right leaf polygon
    right_leaf = [
        (197*scale, 430*scale), (230*scale, 410*scale), (270*scale, 360*scale),
        (285*scale, 260*scale), (285*scale, 200*scale), (265*scale, 270*scale),
        (235*scale, 340*scale), (197*scale, 385*scale)
    ]
    draw.polygon(right_leaf, fill=(108, 150, 106, 240))

    # Back petals (deep purple)
    draw.ellipse([160*scale, 65*scale, 240*scale, 200*scale], fill=(90, 24, 154, 255))
    draw.ellipse([135*scale, 80*scale, 205*scale, 220*scale], fill=(80, 20, 140, 240))
    draw.ellipse([195*scale, 80*scale, 265*scale, 220*scale], fill=(80, 20, 140, 240))

    # Left main petal
    draw.polygon([
        (195*scale, 240*scale), (145*scale, 230*scale), (122*scale, 160*scale),
        (135*scale, 110*scale), (175*scale, 95*scale), (185*scale, 120*scale),
        (170*scale, 170*scale), (195*scale, 240*scale)
    ], fill=(123, 44, 191, 250))

    # Right main petal
    draw.polygon([
        (205*scale, 240*scale), (255*scale, 230*scale), (278*scale, 160*scale),
        (265*scale, 110*scale), (225*scale, 95*scale), (215*scale, 120*scale),
        (230*scale, 170*scale), (205*scale, 240*scale)
    ], fill=(157, 78, 221, 250))

    # Center front petal
    draw.polygon([
        (200*scale, 248*scale), (160*scale, 230*scale), (150*scale, 160*scale),
        (175*scale, 100*scale), (200*scale, 82*scale), (225*scale, 100*scale),
        (250*scale, 160*scale), (240*scale, 230*scale), (200*scale, 248*scale)
    ], fill=(181, 126, 220, 255))

    # Highlight petal rib & shine
    draw.polygon([
        (200*scale, 238*scale), (188*scale, 160*scale), (195*scale, 95*scale),
        (200*scale, 90*scale), (205*scale, 95*scale), (212*scale, 160*scale),
        (200*scale, 238*scale)
    ], fill=(233, 213, 255, 180))

    # Dew drops
    draw.ellipse([184*scale, 137*scale, 191*scale, 144*scale], fill=(255, 255, 255, 220))
    draw.ellipse([216*scale, 167*scale, 222*scale, 173*scale], fill=(250, 247, 255, 190))

    # Downsample
    img_final = img.resize((400, 500), Image.Resampling.LANCZOS)
    img_final.save('images/decorations/purple-tulip.png', 'PNG')
    print("purple-tulip.png created successfully.")

def create_tulip_bouquet_png():
    scale = 2
    w, h = 600 * scale, 650 * scale
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Glow in center
    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse([120*scale, 60*scale, 480*scale, 400*scale], fill=(216, 180, 248, 60))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=25*scale))
    img = Image.alpha_composite(img, glow)
    draw = ImageDraw.Draw(img)

    # Stems
    stems = [
        [(190, 260), (240, 360), (270, 440), (280, 590)],
        [(240, 240), (260, 350), (285, 440), (295, 590)],
        [(300, 210), (300, 340), (300, 440), (300, 600)],
        [(360, 240), (340, 350), (315, 440), (305, 590)],
        [(410, 260), (360, 360), (330, 440), (320, 590)]
    ]
    for stem in stems:
        pts = [(pt[0]*scale, pt[1]*scale) for pt in stem]
        draw.line(pts, fill=(99, 142, 98, 255), width=int(8*scale), joint="curve")

    # Bouquet leaves
    draw.polygon([(280*scale, 480*scale), (190*scale, 440*scale), (95*scale, 280*scale),
                  (135*scale, 270*scale), (210*scale, 380*scale), (285*scale, 440*scale)],
                 fill=(88, 129, 87, 240))
    draw.polygon([(320*scale, 480*scale), (410*scale, 440*scale), (505*scale, 280*scale),
                  (465*scale, 270*scale), (390*scale, 380*scale), (315*scale, 440*scale)],
                 fill=(88, 129, 87, 240))

    # Tulips in bouquet
    tulip_positions = [
        (170, 210, 0.72, (90, 24, 154), (123, 44, 191), (181, 126, 220)),
        (430, 210, 0.72, (90, 24, 154), (123, 44, 191), (245, 217, 242)),
        (220, 140, 0.85, (90, 24, 154), (157, 78, 221), (216, 180, 248)),
        (380, 140, 0.85, (90, 24, 154), (157, 78, 221), (245, 217, 242)),
        (300, 95, 0.9, (90, 24, 154), (157, 78, 221), (216, 180, 248)),
        (300, 210, 1.15, (60, 9, 108), (123, 44, 191), (216, 180, 248))
    ]

    for cx, cy, s, c_dark, c_med, c_light in tulip_positions:
        r = int(45 * s * scale)
        # Back
        draw.ellipse([int((cx-30*s)*scale), int((cy-55*s)*scale), int((cx+30*s)*scale), int((cy+20*s)*scale)], fill=c_dark)
        # Left
        draw.ellipse([int((cx-42*s)*scale), int((cy-45*s)*scale), int((cx+5*s)*scale), int((cy+30*s)*scale)], fill=c_med)
        # Right
        draw.ellipse([int((cx-5*s)*scale), int((cy-45*s)*scale), int((cx+42*s)*scale), int((cy+30*s)*scale)], fill=c_med)
        # Center
        draw.ellipse([int((cx-28*s)*scale), int((cy-40*s)*scale), int((cx+28*s)*scale), int((cy+35*s)*scale)], fill=c_light)

    # Ribbon bow
    ribbon_color = (181, 126, 220, 255)
    dark_ribbon = (123, 44, 191, 255)
    # tails
    draw.polygon([(260*scale, 490*scale), (200*scale, 620*scale), (230*scale, 625*scale), (280*scale, 510*scale)], fill=dark_ribbon)
    draw.polygon([(340*scale, 490*scale), (400*scale, 620*scale), (370*scale, 625*scale), (320*scale, 510*scale)], fill=dark_ribbon)
    # loops
    draw.ellipse([215*scale, 450*scale, 305*scale, 510*scale], fill=ribbon_color)
    draw.ellipse([295*scale, 450*scale, 385*scale, 510*scale], fill=ribbon_color)
    # band & knot
    draw.ellipse([285*scale, 470*scale, 315*scale, 500*scale], fill=dark_ribbon)
    draw.ellipse([290*scale, 475*scale, 310*scale, 495*scale], fill=(216, 180, 248, 255))

    img_final = img.resize((600, 650), Image.Resampling.LANCZOS)
    img_final.save('images/decorations/tulip-bouquet.png', 'PNG')
    print("tulip-bouquet.png created successfully.")

create_purple_tulip_png()
create_tulip_bouquet_png()

# 6. Generate Romantic Photo Placeholders
photo_metadata = [
    ("profile.svg", "Merry Rose Ann Estrella", "", "#B57EDC", "#7B2CBF"),
    ("moment1.svg", "First Day We Laughed", "The moment I knew you were the one", "#D8B4F8", "#9D4EDD"),
    ("moment2.svg", "Stargazing Nights", "Wrapped in blankets, talking forever", "#7B2CBF", "#3C096C"),
    ("moment3.svg", "Our Favorite Coffee Date", "Sweet smiles and shared lattes", "#B57EDC", "#D8B4F8"),
    ("moment4.svg", "Walking In The Garden", "Surrounded by purple tulips, holding hands", "#F5D9F2", "#B57EDC"),
    ("moment5.svg", "Road Trip & Sunset", "Golden hour glow on your gorgeous smile", "#D8B4F8", "#7B2CBF"),
    ("moment6.svg", "Forever & Always", "Every tomorrow is brighter with you", "#9D4EDD", "#3C096C"),
]

for filename, title, subtitle, col1, col2 in photo_metadata:
    title_y = 500 if filename == "profile.svg" else 482
    title_size = 26 if filename == "profile.svg" else 28
    title_markup = f'''<text x="400" y="{title_y}" text-anchor="middle" font-family="'Playfair Display', Georgia, serif" font-weight="700" font-size="{title_size}" fill="#3C096C">{title}</text>'''
    subtitle_markup = "" if filename == "profile.svg" else f'''<text x="400" y="515" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-weight="500" font-size="16" fill="#7B2CBF">{subtitle}</text>'''

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{col1}"/>
      <stop offset="50%" stop-color="#FAF7FF"/>
      <stop offset="100%" stop-color="{col2}"/>
    </linearGradient>
    <radialGradient id="heartGlow" cx="50%" cy="45%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </radialGradient>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#3C096C" flood-opacity="0.25"/>
    </filter>
  </defs>

  <rect width="800" height="600" rx="24" fill="url(#bgGrad)"/>
  <circle cx="400" cy="270" r="180" fill="url(#heartGlow)"/>

  <!-- Romantic Frame Outline -->
  <rect x="25" y="25" width="750" height="550" rx="18" fill="none" stroke="#FFFFFF" stroke-width="2.5" opacity="0.6"/>
  <rect x="35" y="35" width="730" height="530" rx="14" fill="none" stroke="{col2}" stroke-width="1" stroke-dasharray="8 6" opacity="0.4"/>

  <!-- Decorative Tulip Emblem Center -->
  <g transform="translate(400, 240) scale(1.1)" filter="url(#soft)">
    <!-- Heart backdrop -->
    <path d="M0,45 C-55,0 -95,-45 -95,-85 C-95,-125 -60,-155 -15,-155 C15,-155 35,-140 0,-105 C-35,-140 -15,-155 15,-155 C60,-155 95,-125 95,-85 C95,-45 55,0 0,45 Z" fill="#FFFFFF" opacity="0.55" transform="translate(0, 30) scale(1.15)"/>
    
    <!-- Stylized Tulip -->
    <path d="M0,80 Q5,140 0,200" stroke="#588157" stroke-width="7" stroke-linecap="round" fill="none"/>
    <path d="M0,150 C-35,130 -60,95 -50,60 C-30,85 0,120 0,140 Z" fill="#648E62" opacity="0.9"/>
    <path d="M0,165 C35,145 60,110 50,75 C30,100 0,135 0,155 Z" fill="#74A57F" opacity="0.9"/>
    <!-- Petals -->
    <path d="M0,75 C-45,65 -50,-10 -20,-35 C-5,-10 0,20 0,75 Z" fill="{col2}"/>
    <path d="M0,75 C45,65 50,-10 20,-35 C5,-10 0,20 0,75 Z" fill="{col1}"/>
    <path d="M0,80 C-25,65 -25,-25 0,-42 C25,-25 25,65 0,80 Z" fill="#FAF7FF"/>
  </g>

  <!-- Typography Card Overlay -->
  <rect x="80" y="440" width="640" height="100" rx="20" fill="#FFFFFF" opacity="0.88" filter="url(#soft)"/>
  {title_markup}
  {subtitle_markup}

  <!-- Sweet Sparkles -->
  <circle cx="120" cy="110" r="4" fill="#FFFFFF" opacity="0.8"/>
  <circle cx="680" cy="130" r="5" fill="#FAF7FF" opacity="0.85"/>
  <circle cx="710" cy="160" r="3" fill="#D8B4F8" opacity="0.9"/>
  <circle cx="90" cy="140" r="2.5" fill="#B57EDC" opacity="0.9"/>
</svg>'''
    with open(f'images/photos/{filename}', 'w', encoding='utf-8') as f:
        f.write(svg_content)

print("All photo placeholders generated successfully.")
