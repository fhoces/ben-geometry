"""Laser-engraving file for building Gauss's 17-gon on wood with a real compass.

Writes 17gon-laser.svg and 17gon-laser.pdf (250 x 250 mm, true size).

    /opt/anaconda3/bin/python3 make_17gon_laser.py

One cut, everything else engraved. Many laser programs cut along stroked lines by
default, so the ONLY stroked line is the cut; everything else is a filled shape:
  - red    (#FF0000, hairline stroke): CUT. The disc outline, CUT_MARGIN mm outside
                      the engraved circle (so the holes on the circle keep their wood).
  - black  (#000000): engrave. The circle, the two axes, the vertex ticks, the letters.
  - blue   (#0000FF): the needle holes, one tiny dot per key point. Give this color
                      a deeper engrave (more power or passes) so the compass needle
                      has a pit to sit in, or set it to "cut" for a pin-hole.
Letters are converted to outlines, so no fonts are needed on the laser computer.

Same exact geometry as ../animation/heptadecagon.py and ../printables/make_17gon_guide.py.
"""
import numpy as np
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties
from matplotlib.path import Path

# ---------------------------------------------------------------- edit me
R_MM = 110.0          # radius of the big circle (mm). Bigger = M and N3 further apart.
SIZE = 250.0          # the SVG/PDF is SIZE x SIZE mm
HOLE_D = 0.4          # needle-hole diameter (mm)
LINE_W = 0.4          # width of the engraved circle and axes (mm)
CUT_MARGIN = 5.0      # the disc is cut this far outside the engraved circle (mm).
                      # 0 cuts right on the circle, but that destroys the holes at A, B, P3, P5.
CUT = "#FF0000"
GAP = 2.0             # unengraved gap (mm) left in a line or the circle around each hole,
                      # so the needle sits in a pit in flat wood, not in a groove it could slide along
LABEL_PT = 5.0        # letter size (font size in mm; capitals come out about 3.6 mm tall)
ENGRAVE, HOLE = "#000000", "#0000FF"
FONT = FontProperties(family="DejaVu Sans", weight="bold")
CX = CY = SIZE / 2

# ---------------------------------------------------------------- exact points (unit circle)
A, B, O, I = np.array([1.0, 0]), np.array([0, 1.0]), np.zeros(2), np.array([0, 0.25])
ang = lambda P, frm: np.arctan2(P[1] - frm[1], P[0] - frm[0])
def hit_axis(theta):
    t = -I[1] / np.sin(theta)
    return np.array([I[0] + t * np.cos(theta), 0])
d_IO, d_IA = ang(O, I), ang(A, I)
d_IE = d_IO + (d_IA - d_IO) / 4
E = hit_axis(d_IE)
F = hit_axis(d_IE - np.pi / 4)
M = (A + F) / 2
K = np.array([0, np.sqrt(np.sum((A - M) ** 2) - M[0] ** 2)])
rE = np.linalg.norm(E - K)
N3, N5 = np.array([E[0] + rE, 0]), np.array([E[0] - rE, 0])
P3 = np.array([N3[0], np.sqrt(1 - N3[0] ** 2)])
P5 = np.array([N5[0], np.sqrt(1 - N5[0] ** 2)])
assert abs(N3[0] - np.cos(6 * np.pi / 17)) < 1e-12 and abs(N5[0] - np.cos(10 * np.pi / 17)) < 1e-12

# point -> (label offset in mm from the hole to the label's centre, page y points down)
POINTS = {
    "O": (O, (-3.8, 4.6)), "A": (A, (-4.0, 4.6)), "B": (B, (-4.2, 4.0)),
    "H": (np.array([0, 0.5]), (-4.4, 0)),                      # middle of OB (first bisection)
    "I": (I, (-4.2, 0)), "K": (K, (4.6, 0)),
    "E": (E, (3.6, 4.6)), "F": (F, (0, 4.6)), "N5": (N5, (0, 4.6)),
    "M": (M, (-2.8, 4.6)), "N3": (N3, (3.6, -4.4)),       # M is the LEFT hole, N3 the RIGHT one
    "P3": (P3, (-3.6, 4.4)), "P5": (P5, (3.8, 4.4)),
}

def page(p):
    return CX + R_MM * p[0], CY - R_MM * p[1]

# ---------------------------------------------------------------- shapes (all filled)
def text_path(s, cx, cy, size):
    """Text as filled outlines, centred on (cx, cy) in page mm."""
    tp = TextPath((0, 0), s, size=size, prop=FONT)
    v = tp.vertices.copy()
    xmin, ymin = v.min(0); xmax, ymax = v.max(0)
    v[:, 0] += cx - (xmin + xmax) / 2
    v[:, 1] = cy - (v[:, 1] - (ymin + ymax) / 2)       # flip y, centre vertically
    d, i, codes = [], 0, tp.codes
    while i < len(codes):
        c = codes[i]
        if c == Path.MOVETO:
            d.append(f"M{v[i,0]:.3f},{v[i,1]:.3f}"); i += 1
        elif c == Path.LINETO:
            d.append(f"L{v[i,0]:.3f},{v[i,1]:.3f}"); i += 1
        elif c == Path.CURVE3:
            d.append(f"Q{v[i,0]:.3f},{v[i,1]:.3f} {v[i+1,0]:.3f},{v[i+1,1]:.3f}"); i += 2
        elif c == Path.CURVE4:
            d.append(f"C{v[i,0]:.3f},{v[i,1]:.3f} {v[i+1,0]:.3f},{v[i+1,1]:.3f} {v[i+2,0]:.3f},{v[i+2,1]:.3f}"); i += 3
        elif c == Path.CLOSEPOLY:
            d.append("Z"); i += 1
        else:
            i += 1
    return f'<path fill="{ENGRAVE}" fill-rule="evenodd" d="{" ".join(d)}"/>'

def ring(cx, cy, r, w):
    a, b = r + w / 2, r - w / 2
    circ = lambda rr: (f"M{cx + rr:.3f},{cy:.3f} A{rr:.3f},{rr:.3f} 0 1 0 {cx - rr:.3f},{cy:.3f} "
                       f"A{rr:.3f},{rr:.3f} 0 1 0 {cx + rr:.3f},{cy:.3f} Z")
    return f'<path fill="{ENGRAVE}" fill-rule="evenodd" d="{circ(a)} {circ(b)}"/>'

def arc_band(cx, cy, r, w, t1, t2):
    """A filled band of width w along the circle from angle t1 to t2 (radians, counter-clockwise)."""
    ro, ri = r + w / 2, r - w / 2
    P = lambda rr, t: (cx + rr * np.cos(t), cy - rr * np.sin(t))
    large = 1 if t2 - t1 > np.pi else 0
    (x1, y1), (x2, y2) = P(ro, t1), P(ro, t2)
    (x3, y3), (x4, y4) = P(ri, t2), P(ri, t1)
    return (f'<path fill="{ENGRAVE}" d="M{x1:.3f},{y1:.3f} A{ro:.3f},{ro:.3f} 0 {large} 0 {x2:.3f},{y2:.3f} '
            f'L{x3:.3f},{y3:.3f} A{ri:.3f},{ri:.3f} 0 {large} 1 {x4:.3f},{y4:.3f} Z"/>')

def bar(x1, y1, x2, y2, w):
    """A straight engraved line of width w, as a filled thin rectangle."""
    p1, p2 = np.array([x1, y1]), np.array([x2, y2])
    n = np.array([-(p2 - p1)[1], (p2 - p1)[0]]); n = n / np.linalg.norm(n) * w / 2
    q = [p1 + n, p2 + n, p2 - n, p1 - n]
    return f'<polygon fill="{ENGRAVE}" points="{" ".join(f"{x:.3f},{y:.3f}" for x, y in q)}"/>'

# ---------------------------------------------------------------- the drawing
out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{SIZE}mm" height="{SIZE}mm" viewBox="0 0 {SIZE} {SIZE}">',
       '<!-- Red hairline = CUT (the disc). Black fills = engrave. Blue dots = needle holes (deeper engrave or pin-hole cut). -->']
W = out.append

W('<g id="engrave-lines">')
def broken(lo, hi, stops):
    """Pieces of the interval [lo, hi] with a GAP-wide break centred on each stop."""
    cuts = sorted((s - GAP / 2, s + GAP / 2) for s in stops)
    pieces, start = [], lo
    for a, b in cuts:
        if a > start:
            pieces.append((start, min(a, hi)))
        start = max(start, b)
    if start < hi:
        pieces.append((start, hi))
    return pieces

on_OA = [R_MM * p[0] for p in (N5, F, O, E, M, N3, A)]       # holes on line OA (mm from O)
for a, b in broken(-R_MM, R_MM, on_OA):                      # line OA, extended through O
    W(bar(CX + a, CY, CX + b, CY, LINE_W))
on_OB = [R_MM * p[1] for p in (O, I, K, np.array([0, 0.5]), B)]   # holes on OB
for a, b in broken(0, R_MM, on_OB):
    W(bar(CX, CY - a, CX, CY - b, LINE_W))
on_circle = [R_MM * np.arctan2(p[1], p[0]) for p in (A, P3, B, P5)]   # arc length (mm) from A
for a, b in broken(-np.pi * R_MM + 1e-6, np.pi * R_MM, on_circle):   # the circle, as arcs between holes
    W(arc_band(CX, CY, R_MM, LINE_W, a / R_MM, b / R_MM))
for k in range(17):                                          # the 17 true vertices, as ticks just outside
    a = 2 * np.pi * k / 17                                   # the circle (inside the cut disc)
    u = np.array([np.cos(a), -np.sin(a)])
    t_out = min(R_MM + 5.0, R_MM + CUT_MARGIN - 2.0)
    if t_out > R_MM + 1.5:
        W(bar(*(np.array([CX, CY]) + (R_MM + 1.5) * u), *(np.array([CX, CY]) + t_out * u), 0.3))
W('</g>')

W('<g id="engrave-text">')
for name, (p, (dx, dy)) in POINTS.items():
    x, y = page(p)
    W(text_path(name, x + dx, y + dy, LABEL_PT))
W('</g>')

W('<g id="needle-holes">')
for name, (p, _) in POINTS.items():
    x, y = page(p)
    W(f'<circle cx="{x:.4f}" cy="{y:.4f}" r="{HOLE_D / 2}" fill="{HOLE}"/>')
W('</g>')
W(f'<circle id="cut" cx="{CX:.4f}" cy="{CY:.4f}" r="{R_MM + CUT_MARGIN:.4f}" fill="none" stroke="{CUT}" stroke-width="0.05"/>')
W('</svg>')

svg = "\n".join(out)
assert svg.count("stroke=") == 1 and 'stroke="#FF0000"' in svg   # the cut is the only stroked line
assert R_MM + CUT_MARGIN < SIZE / 2                                  # the disc fits on the board
open("17gon-laser.svg", "w").write(svg)

import fitz
pdf = fitz.open("pdf", fitz.open("17gon-laser.svg").convert_to_pdf())
pdf.save("17gon-laser.pdf")
print("pdf page (mm):", round(pdf[0].rect.width / 72 * 25.4, 2), "x", round(pdf[0].rect.height / 72 * 25.4, 2))
print("holes:", len(POINTS), " M-N3 centre gap (mm):", round(abs(N3[0] - M[0]) * R_MM, 2),
      " edge gap:", round(abs(N3[0] - M[0]) * R_MM - HOLE_D, 2))


# =====================================================================================
# BACK SIDE: the recipe, engraved on the back of the disc (17gon-laser-back.svg / .pdf)
# =====================================================================================
# Engrave-only text. The one stroked shape is a GREEN ALIGNMENT GUIDE: the same circle as
# the front's cut, for lining the text up on the disc (camera view) and so both files have
# the same outline when imported. SET GREEN TO "IGNORE" / OUTPUT OFF: it must never fire,
# or it re-cuts the disc's edge. Same 250 mm page and centre as the front, so the disc can
# also be flipped over inside the hole it came out of and run in place. Lines flow inside the disc, centred, each one as wide as
# the circle allows at its height, at least BACK_MARGIN mm from the cut edge.
BACK_MARGIN = 9.0
BODY_FONT = FontProperties(family="DejaVu Sans")
RECIPE = [   # (style, text). Styles: title, subtitle, sub, head, body, foot
    ("title", "Heptadecagon"),
    ("subtitle", "Gauss's 17-gon"),
    ("sub", "Only a compass and a straightedge. Every point is marked on the front."),
    ("head", "1. Quarter an angle"),
    ("body", "Bisect OB to find its middle, H. Bisect OH to find I, a quarter of the way up. "
             "Bisect the angle at I between IO and IA, then bisect that half again. "
             "Where the line meets line OA: E."),
    ("head", "2. 45 degrees, then a circle"),
    ("body", "At I, make a right angle to IE. Mark two points on line IE, one on each side of I, "
             "the same distance away. From each, draw a wider arc. Join I to where the arcs cross."),
    ("body", "Bisect that right angle to get 45 degrees. Where it meets line OA, past O: F."),
    ("body", "Find the middle of AF: equal arcs from A and from F, then join their crossings. "
             "The middle is M. Compass on M, opened to A: draw the circle. It meets OB at K."),
    ("head", "3. One more circle"),
    ("body", "Compass on E, opened to K: draw the circle. It meets line OA at N3 and N5. "
             "Raise a perpendicular at each, up to the big circle: P3 and P5."),
    ("body", "P3 is exactly 3/17 of the way round from A. P5 is exactly 5/17."),
    ("head", "4. Walk it round"),
    ("body", "Open the compass from P3 to P5 and step it from A: you land 2/17 of the way round. "
             "From there to P3 is one side, exactly 1/17. Walk that width round the circle 17 times "
             "and join the marks. Every corner should land on a tick."),
    ("foot", "Inspired by: Numberphile - Heptadecagon (17-gon)"),
]
STYLE = {  # font size (mm), font, line height factor, space before (mm)
    "title": (12.0, FONT, 1.2, 0.0), "subtitle": (7.0, BODY_FONT, 1.3, 0.0), "sub": (4.32, BODY_FONT, 1.4, 1.0),
    "head": (5.66, FONT, 1.35, 3.4), "body": (4.8, BODY_FONT, 1.42, 0.7), "foot": (3.5, BODY_FONT, 1.4, 3.2),
}


def line_path(s, cx, baseline, size, prop):
    """One line of text as filled outlines, centred horizontally on cx, sitting on `baseline`."""
    tp = TextPath((0, 0), s, size=size, prop=prop)
    v = tp.vertices.copy()
    if len(v) == 0:
        return "", 0.0
    xmin, xmax = v[:, 0].min(), v[:, 0].max()
    v[:, 0] += cx - (xmin + xmax) / 2
    v[:, 1] = baseline - v[:, 1]
    d, i, codes = [], 0, tp.codes
    while i < len(codes):
        c = codes[i]
        if c == Path.MOVETO:
            d.append(f"M{v[i,0]:.3f},{v[i,1]:.3f}"); i += 1
        elif c == Path.LINETO:
            d.append(f"L{v[i,0]:.3f},{v[i,1]:.3f}"); i += 1
        elif c == Path.CURVE3:
            d.append(f"Q{v[i,0]:.3f},{v[i,1]:.3f} {v[i+1,0]:.3f},{v[i+1,1]:.3f}"); i += 2
        elif c == Path.CURVE4:
            d.append(f"C{v[i,0]:.3f},{v[i,1]:.3f} {v[i+1,0]:.3f},{v[i+1,1]:.3f} {v[i+2,0]:.3f},{v[i+2,1]:.3f}"); i += 3
        elif c == Path.CLOSEPOLY:
            d.append("Z"); i += 1
        else:
            i += 1
    return f'<path fill="{ENGRAVE}" fill-rule="evenodd" d="{" ".join(d)}"/>', xmax - xmin


def width_of(s, size, prop):
    v = TextPath((0, 0), s, size=size, prop=prop).vertices
    return 0.0 if len(v) == 0 else v[:, 0].max() - v[:, 0].min()


def layout(top):
    """Flow RECIPE into the safe circle starting at y=top. Returns (lines, bottom, overflow)."""
    r_safe = R_MM + CUT_MARGIN - BACK_MARGIN
    y, lines = top, []
    for k, (style, text) in enumerate(RECIPE):
        size, prop, lh_f, before = STYLE[style]
        lh = size * lh_f
        if k:
            y += before
        words = text.split()
        while words:
            far = max(abs(y - CY), abs(y + lh - CY))          # the line's edge farthest from centre
            if far >= r_safe:
                return lines, y, True
            avail = 2 * np.sqrt(r_safe**2 - far**2)
            line = words[0]
            j = 1
            while j < len(words) and width_of(line + " " + words[j], size, prop) <= avail:
                line += " " + words[j]; j += 1
            if width_of(line, size, prop) > avail:            # a single word too wide here: move down
                y += lh; continue
            lines.append((line, y + 0.8 * lh, size, prop))
            words = words[j:]
            y += lh
    return lines, y, False


# try every starting height; keep the layout that fits with the block closest to centred
best = None
for top in np.arange(CY - 105, CY - 30, 0.5):
    lines, bottom, overflow = layout(top)
    if not overflow:
        off = abs((top + bottom) / 2 - CY)
        if best is None or off < best[0]:
            best = (off, lines)
assert best is not None, "recipe does not fit on the back: shorten it or shrink STYLE sizes"
lines = best[1]

back = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{SIZE}mm" height="{SIZE}mm" viewBox="0 0 {SIZE} {SIZE}">',
        '<!-- BACK SIDE. Black fills = engrave. GREEN circle = ALIGNMENT GUIDE ONLY: set green to IGNORE / output off (never cut it). -->',
        '<g id="engrave-text">']
r_safe = R_MM + CUT_MARGIN - BACK_MARGIN
worst = 0.0
for s, baseline, size, prop in lines:
    p, w = line_path(s, CX, baseline, size, prop)
    back.append(p)
    for yy in (baseline - 0.75 * size, baseline + 0.25 * size):   # glyph top and descender bottom
        worst = max(worst, np.hypot(w / 2, yy - CY))
back.append('</g>')
back.append(f'<circle id="align-guide-do-not-cut" cx="{CX:.4f}" cy="{CY:.4f}" r="{R_MM + CUT_MARGIN:.4f}" '
            f'fill="none" stroke="#00A000" stroke-width="0.05"/>')
back.append('</svg>')
back_svg = "\n".join(back)
assert back_svg.count("stroke=") == 1 and 'stroke="#00A000"' in back_svg   # only the green guide
assert worst < r_safe + 0.5, worst
open("17gon-laser-back.svg", "w").write(back_svg)
fitz.open("pdf", fitz.open("17gon-laser-back.svg").convert_to_pdf()).save("17gon-laser-back.pdf")
print(f"back: {len(lines)} lines, text reaches {worst:.1f} mm from centre (cut at {R_MM + CUT_MARGIN:.0f} mm)")
