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
on_OB = [R_MM * p[1] for p in (O, I, K, B)]                  # holes on OB
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
