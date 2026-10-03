"""Module 01 bonus: fold a trihexaflexagon from a strip of 10 triangles, then flex it.

Follows the deck's hexaflexagon slides (Steps 1 to 3 and "A new face!").

Render (from this folder):
    /opt/anaconda3/envs/manim/bin/manim -qm --progress_bar none hexaflexagon.py Hexaflexagon
    cp media/videos/hexaflexagon/720p30/Hexaflexagon.mp4 hexaflexagon.mp4
Fast draft while editing: use -ql instead of -qm.

The folds are real: each one flips the rest of the strip over a crease, and the
points come from reflecting the strip across that crease. Folding back after
triangles 2, 5 and 8 is the choice that leaves triangle 10 directly behind
triangle 1 (checked by simulation), so the two can be glued.

EDITING GUIDE
- Words on screen: CAPTIONS below.  Speed: PACE (1.5 = slower).
- Face colors: FACE_COLORS.  Paper colors: PAPER_FRONT / PAPER_BACK.
- Order of the video: construct() at the bottom, one line per step.
"""
from manim import *
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import stops   # pause points for the slide player (writes <name>_stops.js)
import numpy as np

# ---------------------------------------------------------------- edit me: words
CAPTIONS = {
    "strip":   ["A strip of paper, creased into 10 equal triangles.",
                "(The deck's Step 1 shows how to fold the creases.)"],
    "fold1":   ["Fold the strip back, behind itself,", "along the crease after triangle 2."],
    "fold2":   ["Again: fold back along the crease after triangle 5."],
    "fold3":   ["And once more, after triangle 8."],
    "glue":    ["Triangle 10 is now right behind triangle 1.", "Glue them together."],
    "hexagon": ["A hexagon, made only by folding!"],
    "color1":  ["Color the face you can see: blue."],
    "flip":    ["Turn it over and color the back: orange."],
    "flipback": ["Turn it back to blue."],
    "pinch":   ["Pinch three corners that skip one another", "up to meet in the middle..."],
    "open":    ["...then push the middle open."],
    "newface": ["A face you have never seen! Color it green."],
    "again":   ["Flex again: pinch, then open."],
    "orange":  ["Orange is back on top."],
    "again2":  ["One more flex..."],
    "blue":    ["And again: blue. Three faces take turns,", "all hiding in one loop of paper."],
}

# ---------------------------------------------------------------- edit me: look
PACE = 1.0
S = 1.15                      # side of one triangle while folding (small, so every fold fits)
HEX_R = 1.9                   # side of the finished hexagon's triangles when coloring and flexing
FONT, NUM = 30, 22
PAPER_FRONT = "#f4ecd8"       # the printed side of the paper
PAPER_BACK = "#e2d6b8"        # the other side (a shade darker, so flips show)
FACE_COLORS = {"blue": "#1769aa", "orange": "#c2410c", "green": "#1b7a3d"}
EDGE = "#4d4d4d"
GLUE = "#c0392b"
config.background_color = WHITE

FOLDS = [2, 5, 8]             # fold back along the crease after these triangles

# ---------------------------------------------------------------- the geometry
H = np.sqrt(3) / 2
STRIP_LEFT = np.array([-2.25 * S, -3.7 + 0.87 * S, 0])   # bottom-left corner of the strip (fits all folds)


def flat_triangle(i):
    """Triangle i (1..10) of the flat strip, as three 3D points."""
    if i % 2 == 1:
        pts = [((i - 1) / 2, 0), ((i + 1) / 2, 0), (i / 2, H)]
    else:
        pts = [((i - 1) / 2, H), ((i + 1) / 2, H), (i / 2, 0)]
    return [STRIP_LEFT + S * np.array([x, y, 0]) for x, y in pts]


def reflect(p, a, b):
    d = (b - a) / np.linalg.norm(b - a)
    v = p - a
    return a + 2 * np.dot(v, d) * d - v


def simulate():
    """Positions of every triangle after each fold, plus the crease used for each fold."""
    T = {i: flat_triangle(i) for i in range(1, 11)}
    creases = []
    for c in FOLDS:
        a, b = [p for p in T[c] if min(np.linalg.norm(p - q) for q in T[c + 1]) < 1e-9]
        creases.append((a, b))
        for j in range(c + 1, 11):
            T[j] = [reflect(p, a, b) for p in T[j]]
    return T, creases


FINAL, CREASES = simulate()
# which triangles have been flipped an odd number of times (show their back side)
FLIPS = {i: sum(1 for c in FOLDS if i > c) for i in range(1, 11)}


class Hexaflexagon(Scene):
    # ------------------------------------------------------------ helpers
    def say(self, key, wait=1.5):
        stops.mark(self)                              # a new concept starts here
        new = VGroup(*[Text(s, font_size=FONT, color=BLACK) for s in CAPTIONS[key]])
        new.arrange(DOWN, buff=0.15).to_edge(UP, buff=0.3)
        if self.caption is None:
            self.play(FadeIn(new), run_time=0.6 * PACE)
        else:
            self.play(FadeOut(self.caption), FadeIn(new), run_time=0.6 * PACE)
        self.caption = new
        self.wait(wait * PACE)

    def go(self, *anims, t=1.2):
        self.play(*anims, run_time=t * PACE)

    def hexagon(self, color, center, radius, start):
        """Six triangles around a center, filled with one face color."""
        corners = [center + radius * np.array([np.cos(start + k * PI / 3), np.sin(start + k * PI / 3), 0])
                   for k in range(6)]
        hexa = VGroup(*[Polygon(center, corners[k], corners[(k + 1) % 6], color=EDGE, stroke_width=2,
                                fill_color=color, fill_opacity=1) for k in range(6)])
        return hexa.set_z_index(2), corners

    # ------------------------------------------------------------ the steps
    def step_strip(self):
        self.say("strip", wait=0.3)
        self.tris, self.nums = {}, {}
        for i in range(1, 11):
            t = Polygon(*flat_triangle(i), color=EDGE, stroke_width=2, fill_color=PAPER_FRONT, fill_opacity=1)
            n = Text(str(i), font_size=NUM, color=EDGE).move_to(t.get_center_of_mass())
            t.set_z_index(0); n.set_z_index(0.5)
            self.tris[i], self.nums[i] = t, n
        self.go(LaggedStart(*[FadeIn(self.tris[i], self.nums[i]) for i in range(1, 11)], lag_ratio=0.1), t=1.8)
        self.wait(PACE)

    def fold(self, k):
        c = FOLDS[k]
        self.say(f"fold{k + 1}", wait=0.3)
        a, b = CREASES[k]
        crease = DashedLine(a, b, color=GLUE, stroke_width=5).set_z_index(5)
        self.go(Create(crease), t=0.6)
        moving = [i for i in range(c + 1, 11)]
        group = VGroup(*[self.tris[i] for i in moving], *[self.nums[i] for i in moving])
        for i in moving:                       # folded part goes behind: lower layer
            self.tris[i].set_z_index(-10 * (k + 1))
            self.nums[i].set_z_index(-10 * (k + 1) + 0.5)
        self.go(Rotate(group, angle=PI, axis=b - a, about_point=a), t=2)
        # snap to the exact reflected positions, show the paper's back side, and keep numbers readable
        anims = []
        for i in moving:
            back = FLIPS[i] % 2 == 1 if k == len(FOLDS) - 1 else sum(1 for c2 in FOLDS[:k + 1] if i > c2) % 2 == 1
            target = Polygon(*[FINAL_AT[k][i][j] for j in range(3)], color=EDGE, stroke_width=2,
                             fill_color=PAPER_BACK if back else PAPER_FRONT, fill_opacity=1)
            target.set_z_index(self.tris[i].z_index)
            anims.append(Transform(self.tris[i], target))
            n = Text(str(i), font_size=NUM, color=EDGE).move_to(target.get_center_of_mass())
            n.set_z_index(self.nums[i].z_index)
            anims.append(Transform(self.nums[i], n))
        self.go(*anims, FadeOut(crease), t=0.5)

    def step_glue(self):
        self.say("glue", wait=0.3)
        self.go(self.tris[1].animate.set_fill(opacity=0.25), self.nums[1].animate.set_opacity(0.25), t=0.8)
        self.go(Indicate(self.tris[10], color=GLUE, scale_factor=1.1), t=1.2)
        self.go(self.tris[1].animate.set_fill(opacity=1), self.nums[1].animate.set_opacity(1), t=0.8)

    def step_hexagon(self):
        everything = VGroup(*self.tris.values(), *self.nums.values())
        pts = np.array([p for i in range(1, 10) for p in FINAL[i]])
        center = pts.mean(axis=0)
        self.center = 0.6 * DOWN
        self.go(everything.animate.shift(-center + self.center).scale(HEX_R / S, about_point=self.center), t=1.2)
        # the hexagon's corners: the far vertices of the six visible triangles
        far = [p - center + self.center for p in pts if np.linalg.norm(p - center) > 0.9 * S]
        a0 = min(np.arctan2(*(q - self.center)[1::-1]) % (PI / 3) for q in far)
        self.start = a0
        self.say("hexagon", wait=1.5)
        self.paper = everything

    def step_color_and_flip(self):
        self.say("color1", wait=0.3)
        blue, self.corners = self.hexagon(FACE_COLORS["blue"], self.center, HEX_R, self.start)
        self.go(LaggedStart(*[FadeIn(t) for t in blue], lag_ratio=0.2), t=1.5)
        self.remove(self.paper)
        self.face = blue
        self.say("flip", wait=0.3)
        self.go(self.face.animate.stretch(0.02, 0), t=0.7)
        back, _ = self.hexagon(PAPER_BACK, self.center, HEX_R, self.start)
        back.stretch(0.02, 0)
        self.remove(self.face); self.add(back)
        self.go(back.animate.stretch(50, 0), t=0.7)
        orange, _ = self.hexagon(FACE_COLORS["orange"], self.center, HEX_R, self.start)
        self.go(LaggedStart(*[FadeIn(t) for t in orange], lag_ratio=0.2), t=1.5)
        self.remove(back)
        self.say("flipback", wait=0.3)
        self.go(orange.animate.stretch(0.02, 0), t=0.7)
        self.remove(orange)
        blue2, _ = self.hexagon(FACE_COLORS["blue"], self.center, HEX_R, self.start)
        blue2.stretch(0.02, 0); self.add(blue2)
        self.go(blue2.animate.stretch(50, 0), t=0.7)
        self.face = blue2

    def flex(self, new_color, pinch_key, open_key, show_arrows):
        if pinch_key:
            self.say(pinch_key, wait=0.3)
        c, corners = self.center, self.corners
        arrows = VGroup(*[Arrow(corners[k], c + 0.35 * (corners[k] - c), color=GLUE, buff=0.1, stroke_width=6)
                          for k in (1, 3, 5)])
        if show_arrows:
            self.go(GrowArrow(arrows[0]), GrowArrow(arrows[1]), GrowArrow(arrows[2]), t=0.8)
        # pinch: corners 1, 3, 5 slide in to the middle, the hexagon becomes a three-pointed star
        pinched = [corners[k] if k % 2 == 0 else c + 0.12 * (corners[k] - c) for k in range(6)]
        old = self.face
        star = VGroup(*[Polygon(c, pinched[k], pinched[(k + 1) % 6], color=EDGE, stroke_width=2,
                                fill_color=old[0].get_fill_color(), fill_opacity=1) for k in range(6)])
        anims = [Transform(old, star)]
        if show_arrows:
            anims.append(FadeOut(arrows))
        self.go(*anims, t=1.5)
        if open_key:
            self.say(open_key, wait=0.2)
        # open: the hidden face unfolds from the middle and flattens out
        new, _ = self.hexagon(new_color, c, HEX_R, self.start)
        new.set_z_index(1).scale(0.05).rotate(PI / 3)
        self.go(new.animate.scale(20).rotate(-PI / 3), old.animate.scale(0.6).set_opacity(0), t=1.8)
        self.remove(old)
        self.face = new

    def step_flexes(self):
        self.flex(PAPER_FRONT, "pinch", "open", show_arrows=True)       # the hidden face is still blank
        self.say("newface", wait=0.3)
        green, _ = self.hexagon(FACE_COLORS["green"], self.center, HEX_R, self.start)
        self.go(LaggedStart(*[FadeIn(t) for t in green], lag_ratio=0.2), t=1.5)
        self.remove(self.face); self.face = green
        self.say("again", wait=0.3)
        self.flex(FACE_COLORS["orange"], None, None, show_arrows=True)
        self.say("orange", wait=1.5)
        self.say("again2", wait=0.3)
        self.flex(FACE_COLORS["blue"], None, None, show_arrows=True)
        self.say("blue", wait=3)

    # ------------------------------------------------------------ the order
    def construct(self):
        self.caption = None
        self.step_strip()          # slide "Step 1: fold a chain of triangles"
        for k in range(len(FOLDS)):
            self.fold(k)           # slide "Step 2: curl it into a ring"
        self.step_glue()
        self.step_hexagon()
        self.step_color_and_flip()
        self.step_flexes()         # slides "Step 3: flex it open" and "A new face!"
        stops.write(self, "hexaflexagon")      # pause points for the slide player


# positions of every triangle right after fold k (used to snap each fold exactly)
def _after_each_fold():
    T = {i: flat_triangle(i) for i in range(1, 11)}
    out = []
    for c in FOLDS:
        a, b = [p for p in T[c] if min(np.linalg.norm(p - q) for q in T[c + 1]) < 1e-9]
        for j in range(c + 1, 11):
            T[j] = [reflect(p, a, b) for p in T[j]]
        out.append({i: list(T[i]) for i in T})
    return out


FINAL_AT = _after_each_fold()
