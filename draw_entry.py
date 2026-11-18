#!/usr/bin/env python3
"""Draw the 18 November 2026 world-news front page (1024x1024 PNG).

Deterministic: fixed text, fixed geometry, no randomness, no network.
Run: python3 draw_entry.py  -> writes entry.png beside this file.
Fonts: DejaVu (present on the build machine and in most Linux images).
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 238)
NAVY = (20, 33, 61)
NAVY2 = (27, 45, 84)
GOLD = (201, 162, 39)
RED = (180, 35, 24)
INK = (24, 24, 24)
GREY = (90, 90, 90)
CARD = (255, 255, 255)
BORDER = (210, 205, 192)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to pixel width; returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------------- masthead ----------------
d.rectangle([0, 0, W, 122], fill=NAVY)
d.text((W // 2, 14), "THE WORLD TODAY", font=font(SERIF, 58),
       fill=(255, 255, 255), anchor="ma")
d.rectangle([W // 2 - 300, 86, W // 2 + 300, 89], fill=GOLD)
d.text((W // 2, 96), "WEDNESDAY  ·  18 NOVEMBER 2026",
       font=font(SANS_B, 24), fill=(232, 196, 90), anchor="ma")

# ---------------- lead story ----------------
LX, LY, LW, LH = 28, 138, 968, 300
d.rectangle([LX, LY, LX + LW, LY + LH], fill=CARD, outline=BORDER, width=2)
d.rectangle([LX, LY, LX + LW, LY + 6], fill=RED)
tx = LX + 22
d.text((tx, LY + 20), "LEAD  —  ASIA  ·  DIPLOMACY",
       font=font(SANS_B, 19), fill=RED)
headline = "Trump lands in Manila for Quad talks ahead of China visit"
y = draw_lines(d, tx, LY + 50,
               wrap(d, headline, font(SANS_B, 38), 560),
               font(SANS_B, 38), INK, 46)
summary = ("The US president arrived in the Philippines as ASEAN leaders "
           "wrapped up their summit in Manila. Quad leaders — the US, "
           "India, Japan and Australia — meet on maritime security, AI and "
           "critical minerals.")
draw_lines(d, tx, y + 8,
           wrap(d, summary, font(SANS, 18), 560),
           font(SANS, 18), (60, 60, 60), 25)

# lead illustration: sky panel with globe + four Quad flag chips
PX, PY, PW, PH = 648, LY + 20, 326, 238
d.rectangle([PX, PY, PX + PW, PY + PH], fill=(214, 232, 245),
            outline=BORDER, width=1)
# globe
cx, cy, r = PX + 163, PY + 78, 52
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(46, 111, 173),
          outline=(255, 255, 255), width=3)
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255), width=2)
d.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=(255, 255, 255), width=3)
d.arc([cx - r // 2, cy - r, cx + r // 2, cy + r], 90, 270,
      fill=(255, 255, 255), width=3)
d.line([cx - r, cy, cx + r, cy], fill=(255, 255, 255), width=3)
# four flag chips: USA, Philippines, Japan, Australia (simplified)
flags = [
    ("USA", (178, 34, 52), (255, 255, 255)),
    ("PHL", (0, 56, 168), (255, 255, 255)),
    ("JPN", (188, 0, 45), (255, 255, 255)),
    ("AUS", (0, 0, 139), (255, 255, 255)),
]
fx, fy, fw, fh, gap = PX + 14, PY + 158, 68, 46, 10
for i, (code, col, _) in enumerate(flags):
    x0 = fx + i * (fw + gap)
    d.rectangle([x0, fy, x0 + fw, fy + fh], fill=col,
                outline=(255, 255, 255), width=2)
    if code == "USA":
        for s in range(4):
            d.rectangle([x0, fy + 6 + s * 11, x0 + fw, fy + 9 + s * 11],
                        fill=(255, 255, 255))
        d.rectangle([x0, fy, x0 + 28, fy + 22], fill=(20, 33, 61))
    elif code == "PHL":
        d.polygon([(x0 + 8, fy + 6), (x0 + 8, fy + fh - 6),
                   (x0 + 30, fy + fh // 2)], fill=(255, 255, 255))
        d.ellipse([x0 + 40, fy + 13, x0 + 58, fy + 31], fill=(255, 209, 0))
    elif code == "JPN":
        d.rectangle([x0, fy, x0 + fw, fy + fh], fill=(255, 255, 255),
                    outline=(255, 255, 255), width=2)
        d.ellipse([x0 + 24, fy + 11, x0 + 44, fy + 31], fill=(188, 0, 45))
    else:
        d.ellipse([x0 + 14, fy + 10, x0 + 22, fy + 18], fill=(255, 255, 255))
        d.ellipse([x0 + 44, fy + 26, x0 + 52, fy + 34], fill=(255, 255, 255))
        d.ellipse([x0 + 30, fy + 28, x0 + 36, fy + 34], fill=(255, 255, 255))
    d.text((x0 + fw // 2, fy + fh + 4), code, font=font(SANS_B, 13),
           fill=NAVY, anchor="ma")
d.text((PX + PW // 2, PY + PH - 2), "", font=font(SANS, 10), fill=NAVY)

# ---------------- story cards: 2 cols x 3 rows ----------------
cards = [
    ("UKRAINE", (180, 35, 24), "bridge",
     "Ukraine hits Crimean Bridge again",
     "Second straight day of strikes on the link to Crimea, as Russian "
     "missiles hit bridges in Kyiv, cutting power and water."),
    ("GULF", (13, 92, 96), "drone",
     "Iran drones target US radar in Bahrain",
     "Bahrain sounds the all-clear after a threat warning; Kuwait says its "
     "army intercepted drones overnight."),
    ("TRADE", (27, 108, 66), "trade",
     "Canada and China extend trade deals",
     "Xi meets PM Carney ahead of the APEC summit as both sides widen "
     "cooperation on trade."),
    ("BRITAIN", (20, 33, 61), "gavel",
     "UK sanctions Israeli settlement firms",
     "London acts against West Bank settlement companies in a push to "
     "protect the two-state solution."),
    ("WEATHER", (18, 90, 160), "storm",
     "Cyclone Akvan strengthens",
     "The Bay of Bengal storm heads for India's east coast; Andhra Pradesh "
     "and Odisha are on high alert."),
    ("SPORT", (176, 92, 8), "sport",
     "Dhoni retires from the IPL",
     "MS Dhoni ends his playing career and becomes Chennai Super Kings "
     "mentor; India beat Pakistan 2-1 for a 10th SAFF title."),
]

GX, GY = 28, 454
CW, CH, CGAP, RGAP = 476, 152, 16, 12


def icon(draw, kind, x, y, col):
    """Simple 46x46 pictogram in the card's accent colour."""
    if kind == "bridge":
        draw.line([x, y + 36, x + 46, y + 36], fill=col, width=4)
        draw.line([x + 6, y + 36, x + 6, y + 10], fill=col, width=4)
        draw.line([x + 40, y + 36, x + 40, y + 10], fill=col, width=4)
        draw.arc([x + 6, y + 14, x + 40, y + 40], 180, 360, fill=col, width=3)
        draw.line([x + 6, y + 10, x + 40, y + 10], fill=col, width=3)
    elif kind == "drone":
        draw.ellipse([x + 16, y + 16, x + 30, y + 30], fill=col)
        for cx0, cy0 in [(x + 4, y + 4), (x + 34, y + 4),
                         (x + 4, y + 34), (x + 34, y + 34)]:
            draw.ellipse([cx0, cy0, cx0 + 8, cy0 + 8], outline=col, width=2)
        draw.line([x + 8, y + 8, x + 18, y + 18], fill=col, width=2)
        draw.line([x + 38, y + 8, x + 28, y + 18], fill=col, width=2)
        draw.line([x + 8, y + 38, x + 18, y + 28], fill=col, width=2)
        draw.line([x + 38, y + 38, x + 28, y + 28], fill=col, width=2)
    elif kind == "trade":
        draw.line([x + 4, y + 14, x + 34, y + 14], fill=col, width=4)
        draw.polygon([(x + 34, y + 6), (x + 44, y + 14), (x + 34, y + 22)],
                     fill=col)
        draw.line([x + 42, y + 32, x + 12, y + 32], fill=col, width=4)
        draw.polygon([(x + 12, y + 24), (x + 2, y + 32), (x + 12, y + 40)],
                     fill=col)
    elif kind == "gavel":
        draw.line([x + 8, y + 38, x + 38, y + 8], fill=col, width=5)
        draw.rectangle([x + 2, y + 26, x + 20, y + 38], fill=col)
        draw.rectangle([x + 26, y + 8, x + 44, y + 20], fill=col)
        draw.line([x + 4, y + 42, x + 42, y + 42], fill=col, width=3)
    elif kind == "storm":
        for rr in (20, 14, 8):
            draw.arc([x + 23 - rr, y + 23 - rr, x + 23 + rr, y + 23 + rr],
                     40, 300, fill=col, width=3)
        draw.line([x + 23, y + 23, x + 40, y + 12], fill=col, width=3)
    elif kind == "sport":
        draw.line([x + 10, y + 40, x + 34, y + 10], fill=col, width=7)
        draw.ellipse([x + 34, y + 30, x + 44, y + 40], fill=(178, 34, 52))


for i, (tag, col, kind, head, body) in enumerate(cards):
    cx0 = GX + (i % 2) * (CW + CGAP)
    cy0 = GY + (i // 2) * (CH + RGAP)
    d.rectangle([cx0, cy0, cx0 + CW, cy0 + CH], fill=CARD,
                outline=BORDER, width=2)
    d.rectangle([cx0, cy0, cx0 + 8, cy0 + CH], fill=col)
    icon(d, kind, cx0 + CW - 62, cy0 + 14, col)
    d.text((cx0 + 22, cy0 + 12), tag, font=font(SANS_B, 15), fill=col)
    y = draw_lines(d, cx0 + 22, cy0 + 34,
                   wrap(d, head, font(SANS_B, 20), CW - 100),
                   font(SANS_B, 20), INK, 24)
    draw_lines(d, cx0 + 22, y + 4,
               wrap(d, body, font(SANS, 14), CW - 44),
               font(SANS, 14), (70, 70, 70), 19)

# ---------------- ticker footer ----------------
FY = 948
d.rectangle([0, FY, W, H], fill=NAVY)
ticker = ("ALSO:  Amazon pledges $7bn for renewables in India  ·  Baidu chief warns of an AI bubble  ·  "
          "UN: 372 civilians killed in Ukraine in October")
tfs = 16
while d.textlength(ticker, font=font(SANS_B, tfs)) > W - 40 and tfs > 10:
    tfs -= 1
d.text((W // 2, FY + 10), ticker, font=font(SANS_B, tfs),
       fill=(255, 255, 255), anchor="ma")
d.text((W // 2, FY + 38), "Wednesday 18 November 2026  ·  The world in one image",
       font=font(SANS, 14), fill=(200, 205, 220), anchor="ma")

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
