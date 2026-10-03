"""Printable guide for building Gauss's 17-gon with a real compass (Richmond's recipe).

Writes 17gon-guide.svg (US Letter, true size in millimetres) and 17gon-guide.pdf.
Print at 100% / "Actual size" (not "Fit to page"), then check the 100 mm bar.

    /opt/anaconda3/envs/manim/bin/python make_17gon_guide.py

Every point is computed exactly (same math as ../animation/heptadecagon.py and the
deck's richmond17_pts()), and the script asserts that N3 and N5 match
cos(3*2pi/17) and cos(5*2pi/17) before writing anything.
"""
import numpy as np

R_MM = 85.0                          # radius of the big circle, in millimetres
PAGE_W, PAGE_H = 215.9, 279.4        # US Letter in mm (A4 would be 210 x 297)
CX, CY = PAGE_W / 2, 112.0           # where O sits on the page
COLORS = {"H": "#555555", "I": "#1769aa", "E": "#c2410c", "F": "#c0392b", "M": "#1b7a3d", "K": "#1b7a3d",
          "N3": "#7b3fa0", "N5": "#7b3fa0", "P3": "#000000", "P5": "#000000"}

# ---------------------------------------------------------------- exact points (unit circle)
A, I = np.array([1.0, 0]), np.array([0, 0.25])
ang = lambda P, frm: np.arctan2(P[1] - frm[1], P[0] - frm[0])
def hit_axis(theta):
    t = -I[1] / np.sin(theta)
    return np.array([I[0] + t * np.cos(theta), 0])
d_IO, d_IA = ang(np.zeros(2), I), ang(A, I)
d_IE = d_IO + (d_IA - d_IO) / 4                 # angle OIA bisected twice
E = hit_axis(d_IE)
F = hit_axis(d_IE - np.pi / 4)                  # 45 degrees further round
M = (A + F) / 2                                 # midpoint of AF
K = np.array([0, M[1] + np.sqrt(np.sum((A - M) ** 2) - M[0] ** 2)])
rE = np.linalg.norm(E - K)
N3, N5 = np.array([E[0] + rE, 0]), np.array([E[0] - rE, 0])
P3 = np.array([N3[0], np.sqrt(1 - N3[0] ** 2)])
P5 = np.array([N5[0], np.sqrt(1 - N5[0] ** 2)])
assert abs(N3[0] - np.cos(3 * 2 * np.pi / 17)) < 1e-12 and abs(N5[0] - np.cos(5 * 2 * np.pi / 17)) < 1e-12

POINTS = {"H": np.array([0, 0.5]), "I": I, "E": E, "F": F, "M": M, "K": K, "N3": N3, "N5": N5, "P3": P3, "P5": P5}
# label offsets in mm (dx, dy on the page, y down), chosen so neighbours don't collide
LABEL_AT = {"H": (-6, 1), "I": (-6, 1), "E": (1.5, 6), "F": (-4, 6), "M": (-1.5, 6.5), "K": (2.5, -2),
            "N3": (1.5, -3), "N5": (-4, 6), "P3": (2.5, -2.5), "P5": (-8, -2.5)}

def page(p):                                    # unit-circle point -> page mm (SVG y points down)
    return CX + R_MM * p[0], CY - R_MM * p[1]

# ---------------------------------------------------------------- SVG
out = []
W = out.append
W(f'<svg xmlns="http://www.w3.org/2000/svg" width="{PAGE_W}mm" height="{PAGE_H}mm" '
  f'viewBox="0 0 {PAGE_W} {PAGE_H}" font-family="Helvetica, Arial, sans-serif">')
W(f'<rect width="{PAGE_W}" height="{PAGE_H}" fill="white"/>')
W('<text x="12" y="12" font-size="5" font-weight="bold">Gauss\'s 17-gon: Richmond\'s recipe, with the exact points</text>')
W('<text x="12" y="17.5" font-size="3.2" fill="#555">Print at 100% ("Actual size"). The bar below must measure exactly 100 mm.</text>')

# the circle, line OA extended through O, and OB
W('<g id="circle-and-axes" fill="none" stroke="#000" stroke-width="0.35">')
W(f'<circle cx="{CX:.3f}" cy="{CY:.3f}" r="{R_MM}"/>')
W(f'<line x1="{CX - R_MM:.3f}" y1="{CY:.3f}" x2="{CX + R_MM:.3f}" y2="{CY:.3f}"/>')
W(f'<line x1="{CX:.3f}" y1="{CY:.3f}" x2="{CX:.3f}" y2="{CY - R_MM:.3f}"/>')
W('</g>')
for name, p, dx, dy in [("O", np.zeros(2), -5, 5.5), ("A", A, 2, 5.5), ("B", np.array([0, 1.0]), 1.5, -2)]:
    x, y = page(p)
    W(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="0.6" fill="#000"/>')
    W(f'<text x="{x + dx:.3f}" y="{y + dy:.3f}" font-size="4">{name}</text>')

# crosshair at each key point: put the compass point exactly where the two hairlines cross
W('<g id="key-points">')
for name, p in POINTS.items():
    x, y = page(p)
    c = COLORS[name]
    W(f'<g stroke="{c}" stroke-width="0.15" fill="none">'
      f'<line x1="{x - 2.2:.3f}" y1="{y:.3f}" x2="{x + 2.2:.3f}" y2="{y:.3f}"/>'
      f'<line x1="{x:.3f}" y1="{y - 2.2:.3f}" x2="{x:.3f}" y2="{y + 2.2:.3f}"/>'
      f'<circle cx="{x:.3f}" cy="{y:.3f}" r="1.1"/></g>')
    dx, dy = LABEL_AT[name]
    W(f'<text x="{x + dx:.3f}" y="{y + dy:.3f}" font-size="3.4" fill="{c}" font-weight="bold">{name}</text>')
W('</g>')

# the 17 true vertices, as ticks just outside the circle, to check your finished polygon
W('<g id="vertex-check-ticks" stroke="#888" stroke-width="0.25">')
for k in range(17):
    a = 2 * np.pi * k / 17
    u = np.array([np.cos(a), -np.sin(a)])
    x1, y1 = CX + (R_MM + 1.5) * u[0], CY + (R_MM + 1.5) * u[1]
    x2, y2 = CX + (R_MM + 5.0) * u[0], CY + (R_MM + 5.0) * u[1]
    xt, yt = CX + (R_MM + 8.5) * u[0], CY + (R_MM + 8.5) * u[1] + 1.1
    W(f'<line x1="{x1:.3f}" y1="{y1:.3f}" x2="{x2:.3f}" y2="{y2:.3f}"/>')
    W(f'<text x="{xt:.3f}" y="{yt:.3f}" font-size="2.6" fill="#888" stroke="none" text-anchor="middle">{k}</text>')
W('</g>')

# scale bar
by = 213.0
W(f'<g stroke="#000" stroke-width="0.3"><line x1="12" y1="{by}" x2="112" y2="{by}"/>'
  f'<line x1="12" y1="{by - 2}" x2="12" y2="{by + 2}"/><line x1="112" y1="{by - 2}" x2="112" y2="{by + 2}"/></g>')
W(f'<text x="114" y="{by + 1.2}" font-size="3.2">100 mm</text>')

# the recipe
steps = [
    "1. Bisect OB to find its middle H, then bisect OH to find I. Bisect angle OIA twice; it hits line OA at E.",
    "2. At I, build a right angle to IE and bisect it: 45 degrees. That line hits line OA (past O) at F.",
    "3. Arcs from A and from F (same width) give the middle of AF: M. Circle centered M through A meets OB at K.",
    "4. Circle centered E through K meets line OA at N3 and N5. Raise perpendiculars there to the circle: P3, P5.",
    "5. P3 is 3/17 of the way round from A, P5 is 5/17. Copy chord P3P5 from A to reach vertex 2; then vertex 2",
    "    to P3 is one side. Walk that width round the circle. The grey ticks show where all 17 vertices belong.",
    "Note: M and N3 really are only about 0.6 mm apart. That is not a printing error.",
    "Inspired by Numberphile: The Amazing Heptadecagon (17-gon), youtube.com/watch?v=87uo2TPrsl8",
]
CREDIT_URL = "https://www.youtube.com/watch?v=87uo2TPrsl8"
for i, s in enumerate(steps):
    W(f'<text x="12" y="{226 + 6.2 * i:.1f}" font-size="3.1" fill="{"#555" if s.startswith(("Note", "Inspired")) else "#000"}">'
      f'{s.replace("&", "&amp;")}</text>')
W('</svg>')

svg = "\n".join(out)
open("17gon-guide.svg", "w").write(svg)

import fitz                                      # PyMuPDF: SVG -> PDF at the same physical size
doc = fitz.open("17gon-guide.svg")
pdf = fitz.open("pdf", doc.convert_to_pdf())
# make the credit line a clickable link (SVG links do not survive the PDF conversion)
hit = pdf[0].search_for("Inspired by Numberphile")
line = pdf[0].search_for("youtube.com/watch?v=87uo2TPrsl8")
assert hit and line
pdf[0].insert_link({"kind": fitz.LINK_URI, "from": hit[0] | line[0], "uri": CREDIT_URL})
pdf.save("17gon-guide.pdf")
print("page (pt):", pdf[0].rect, " expected", PAGE_W / 25.4 * 72, "x", PAGE_H / 25.4 * 72)
print("M to N3 on paper (mm):", round(abs(N3[0] - M[0]) * R_MM, 2))
