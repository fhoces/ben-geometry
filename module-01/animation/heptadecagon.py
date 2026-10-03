"""Module 01 bonus: Gauss's 17-gon, built with Richmond's 1893 recipe.

Follows the deck's "Bonus: Gauss's 17-gon" slides step by step (Step 1 to Step 4).

Render (from this folder):
    /opt/anaconda3/envs/manim/bin/manim -qm --progress_bar none heptadecagon.py Heptadecagon
    cp media/videos/heptadecagon/720p30/Heptadecagon.mp4 heptadecagon.mp4
Fast draft while editing: use -ql instead of -qm (480p, renders ~4x faster).

EDITING GUIDE
- Words on screen: change them in CAPTIONS below (one entry per step, a list of lines).
- Speed: PACE stretches or shrinks every pause and animation (1.0 = normal, 1.5 = slower).
- Colors and size: the block right under CAPTIONS.
- The order of the video: construct() at the bottom calls one function per step;
  comment out a line there to skip a step while you work on another.
"""
from manim import *
import numpy as np

# ---------------------------------------------------------------- edit me: words
CAPTIONS = {
    "intro":    ["The hexagon was easy. Can we build a perfect 17-gon",
                 "with only a compass and a straight edge?"],
    "axes":     ["Draw a circle, and two radii OA and OB", "that meet at a right angle."],
    "mark_I":   ["Mark I, a quarter of the way up from O to B."],
    "angle":    ["Look at the angle at I, between IO and IA."],
    "bisect1":  ["Bisect it: cut it exactly in half."],
    "bisect2":  ["Bisect that half again: now we have a quarter.", "Where it hits the line OA, call it E."],
    "turn45":   ["Turn 45 degrees further round from IE.", "Where that hits the line, call it F."],
    "circleAF": ["Draw the circle with AF as its diameter.", "It crosses OB at K."],
    "circleE":  ["Draw the circle centered at E, through K.", "It crosses the line at N3 and N5."],
    "raise":    ["Raise a perpendicular at N3 and at N5,", "up to the big circle: P3 and P5."],
    "check":    ["Check: cut the circle into 17 equal slices.", "P3 sits on slice 3, P5 on slice 5. Exactly."],
    "copy":     ["Copy the chord P3 to P5 starting from A.", "That lands on slice 2."],
    "side":     ["The gap from slice 2 to P3 is one slice:", "the side of the 17-gon."],
    "walk":     ["Walk that width around the circle,", "just like the hexagon."],
    "done":     ["Seventeen equal sides. No measuring,", "just circles and straight lines."],
}

# ---------------------------------------------------------------- edit me: look
PACE = 1.0                  # 1.5 = everything 50% slower
R = 3.3                     # radius of the big circle during the construction
O = np.array([0, -2.0, 0])  # where the center sits during the construction
FONT = 30                   # caption size
LABEL = 26                  # point-label size

BLUE_D, ORANGE_D, RED_D = "#1769aa", "#c2410c", "#c0392b"   # same as the deck
GREEN_D, PURPLE_D, GREY_D = "#1b7a3d", "#7b3fa0", "#4d4d4d"
config.background_color = WHITE

# ---------------------------------------------------------------- the geometry
# Exact points on a unit circle (same math as richmond17_pts() in ../slides.Rmd).
def unit_points():
    A, I = np.array([1.0, 0]), np.array([0, 0.25])
    to = lambda P, frm: np.arctan2(P[1] - frm[1], P[0] - frm[0])
    def hit_axis(theta):            # where a ray from I at angle theta meets the line OA
        t = -I[1] / np.sin(theta)
        return np.array([I[0] + t * np.cos(theta), 0])
    d_IO, d_IA = to(np.zeros(2), I), to(A, I)
    angle_OIA = d_IA - d_IO
    d_IE = d_IO + angle_OIA / 4
    E = hit_axis(d_IE)
    F = hit_axis(d_IE - PI / 4)
    c, r = (A + F) / 2, np.linalg.norm(A - F) / 2
    K = np.array([0, c[1] + np.sqrt(r**2 - c[0]**2)])
    rE = np.linalg.norm(E - K)
    N3, N5 = np.array([E[0] + rE, 0]), np.array([E[0] - rE, 0])
    P3, P5 = np.array([N3[0], np.sqrt(1 - N3[0]**2)]), np.array([N5[0], np.sqrt(1 - N5[0]**2)])
    return dict(A=A, B=np.array([0, 1.0]), I=I, E=E, F=F, K=K, N3=N3, N5=N5, P3=P3, P5=P5,
                d_IO=d_IO, d_IA=d_IA, d_IE=d_IE)


U = unit_points()
def pt(name):               # a unit-circle point -> screen coordinates
    return O + R * np.array([*U[name], 0])
def on_circle(k):           # slice k of 17 -> screen coordinates
    a = 2 * PI * k / 17
    return O + R * np.array([np.cos(a), np.sin(a), 0])
def direction(theta):
    return np.array([np.cos(theta), np.sin(theta), 0])


class Heptadecagon(MovingCameraScene):
    # ------------------------------------------------------------ helpers
    def say(self, key, wait=1.5):
        new = VGroup(*[Text(s, font_size=FONT, color=BLACK) for s in CAPTIONS[key]])
        frame = self.camera.frame                      # captions follow the camera zoom
        s = frame.width / config.frame_width
        new.arrange(DOWN, buff=0.15).scale(s)
        new.move_to(frame.get_top() + DOWN * (new.height / 2 + 0.3 * s))
        new = VGroup(SurroundingRectangle(new, color=WHITE, fill_color=WHITE, fill_opacity=0.92,
                                          stroke_width=0, buff=0.15 * s), new)
        if self.caption is None:
            self.play(FadeIn(new), run_time=0.6 * PACE)
        else:
            self.play(FadeOut(self.caption), FadeIn(new), run_time=0.6 * PACE)
        self.caption = new
        self.wait(wait * PACE)

    def dot(self, name, color, direction_, text=None):
        d = Dot(pt(name), color=color, radius=0.07)
        l = Text(text or name, font_size=LABEL, color=color).next_to(d, direction_, buff=0.1)
        l.set_stroke(WHITE, width=5, background=True)   # white halo so lines don't cross the letters
        self.play(FadeIn(d, scale=2), FadeIn(l), run_time=0.6 * PACE)
        return VGroup(d, l)

    def go(self, *anims, t=1.2):
        self.play(*anims, run_time=t * PACE)

    def zoom(self, center, width):
        """Move the camera: width 14.2 is the full picture, smaller is closer in."""
        if self.caption is not None:
            self.play(FadeOut(self.caption), run_time=0.4 * PACE)
            self.caption = None
        self.go(self.camera.frame.animate.set(width=width).move_to(center), t=1.5)

    # ------------------------------------------------------------ the steps
    def step_axes(self):
        self.say("intro", wait=2.5)
        self.big = Arc(radius=R, start_angle=-0.25, angle=PI + 0.5, arc_center=O, color=GREY_D)
        self.say("axes", wait=0.3)
        self.go(Create(self.big))
        self.OA = Line(O + 0.6 * R * LEFT, pt("A"), color=GREY_D)   # extended past O for F
        self.OB = Line(O, pt("B"), color=GREY_D)
        self.go(Create(self.OA), Create(self.OB))
        self.labels = VGroup(
            Dot(O, color=BLACK, radius=0.06), Text("O", font_size=LABEL, color=BLACK).next_to(O, DOWN, buff=0.45),
            Dot(pt("A"), color=BLACK, radius=0.06), Text("A", font_size=LABEL, color=BLACK).next_to(pt("A"), DR, buff=0.08),
            Dot(pt("B"), color=BLACK, radius=0.06), Text("B", font_size=LABEL, color=BLACK).next_to(pt("B"), UR, buff=0.08),
        )
        self.go(FadeIn(self.labels), t=0.6)

    def step_quarter_angle(self):
        self.say("mark_I", wait=0.3)
        self.I = self.dot("I", BLUE_D, LEFT)
        self.say("angle", wait=0.3)
        IA = DashedLine(pt("I"), pt("A"), color=BLUE_D)
        full = Angle(Line(pt("I"), O), Line(pt("I"), pt("A")), radius=0.7, color=BLUE_D)
        self.go(Create(IA), Create(full))
        self.wait(PACE)
        self.say("bisect1", wait=0.3)
        half_dir = direction(U["d_IO"] + (U["d_IA"] - U["d_IO"]) / 2)
        half = Line(pt("I"), pt("I") + 1.1 * half_dir, color=ORANGE_D, stroke_opacity=0.6)
        self.go(Create(half))
        self.say("bisect2", wait=0.3)
        quarter = Line(pt("I"), pt("E"), color=ORANGE_D, stroke_width=5)
        q_angle = Angle(Line(pt("I"), O), Line(pt("I"), pt("E")), radius=1.0, color=ORANGE_D)
        self.go(Create(quarter), Create(q_angle))
        self.E = self.dot("E", ORANGE_D, DOWN)
        self.go(FadeOut(half, full, IA), t=0.6)
        self.IE, self.q_angle = quarter, q_angle

    def step_45_and_circle_AF(self):
        self.say("turn45", wait=0.3)
        IF = Line(pt("I"), pt("F"), color=RED_D, stroke_width=5)
        a45 = Angle(Line(pt("I"), pt("F")), Line(pt("I"), pt("E")), radius=0.35, color=RED_D)
        t45 = Text("45°", font_size=14, color=RED_D).move_to(
            pt("I") + 0.55 * direction(U["d_IE"] - PI / 8))
        self.go(Create(IF), Create(a45), FadeIn(t45))
        self.IF = IF
        self.F = self.dot("F", RED_D, DOWN)
        self.wait(PACE)
        self.go(FadeOut(a45, t45, self.q_angle), t=0.6)
        self.say("circleAF", wait=0.3)
        c = (pt("A") + pt("F")) / 2
        self.cAF = DashedVMobject(Circle(radius=np.linalg.norm(pt("A") - c), color=GREEN_D).move_to(c), num_dashes=60)
        self.go(Create(self.cAF), t=2)
        self.K = self.dot("K", GREEN_D, RIGHT)

    def step_circle_E_and_raise(self):
        self.say("circleE", wait=0.3)
        rE = np.linalg.norm(pt("E") - pt("K"))
        self.cE = DashedVMobject(Circle(radius=rE, color=PURPLE_D).move_to(pt("E")), num_dashes=50)
        self.go(Create(self.cE), t=2)
        self.N3 = self.dot("N3", PURPLE_D, DOWN)
        self.N5 = self.dot("N5", PURPLE_D, DOWN)
        self.wait(PACE)
        self.zoom(ORIGIN, config.frame_width)          # back to the whole picture
        self.say("raise", wait=0.3)
        up3 = DashedLine(pt("N3"), pt("P3"), color=PURPLE_D)
        up5 = DashedLine(pt("N5"), pt("P5"), color=PURPLE_D)
        self.go(Create(up3), Create(up5))
        self.P3 = self.dot("P3", BLACK, UR)
        self.P5 = self.dot("P5", BLACK, UL)
        self.raise_lines = VGroup(up3, up5)

    def step_check(self):
        # clear the scaffolding, then show the 17 equal slices
        scaffold = VGroup(self.IE, self.IF, self.cAF, self.cE, self.raise_lines, self.I, self.E, self.F, self.K,
                          self.N3, self.N5, self.OB)
        self.go(FadeOut(scaffold), t=0.8)
        self.say("check", wait=0.3)
        ticks = VGroup(*[Line(O, on_circle(k), color=GREY_C, stroke_width=2) for k in range(9)])
        nums = VGroup(*[Text(str(k), font_size=24, color=BLACK).move_to(O + (R - 0.35) * (on_circle(k) - O) / R)
                        for k in range(1, 9)])
        self.go(LaggedStart(*[Create(t) for t in ticks], lag_ratio=0.15), FadeIn(nums), t=2)
        self.go(Indicate(self.P3[0], color=PURPLE_D, scale_factor=2), Indicate(self.P5[0], color=PURPLE_D, scale_factor=2))
        self.wait(1.5 * PACE)
        self.go(FadeOut(ticks, nums), t=0.6)

    def step_finish(self):
        self.say("copy", wait=0.3)
        chord = Line(pt("P3"), pt("P5"), color=PURPLE_D, stroke_width=5)
        self.go(Create(chord))
        width = np.linalg.norm(pt("P3") - pt("P5"))
        compass = Arc(radius=width, start_angle=PI / 2 + 0.05, angle=0.6, arc_center=pt("A"), color=PURPLE_D)
        copy = chord.copy()
        self.go(copy.animate.put_start_and_end_on(pt("A"), on_circle(2)), Create(compass), t=1.8)
        P2 = Dot(on_circle(2), color=PURPLE_D, radius=0.07)
        self.play(FadeIn(P2, scale=2), run_time=0.5 * PACE)
        self.say("side", wait=0.3)
        side = Line(on_circle(2), pt("P3"), color=BLUE_D, stroke_width=7)
        self.go(Create(side))
        self.wait(PACE)

        # zoom out to the whole circle for the walk
        self.say("walk", wait=0.3)
        board = Group(*[m for m in self.mobjects if m is not self.caption])
        full = Circle(radius=R, color=GREY_D).move_to(O)
        self.go(FadeOut(board), FadeIn(full), t=0.8)
        self.go(full.animate.scale(0.78).move_to(0.55 * DOWN), t=1.2)
        r2, c2 = full.width / 2, full.get_center()
        corner = lambda k: c2 + r2 * direction(2 * PI * k / 17)
        dots = [Dot(corner(0), color=BLUE_D, radius=0.06)]
        self.add(dots[0])
        edges = []
        for k in range(1, 18):
            e = Line(corner(k - 1), corner(k), color=BLUE_D, stroke_width=5)
            d = Dot(corner(k % 17), color=BLUE_D, radius=0.06)
            self.play(Create(e), FadeIn(d), run_time=0.35 * PACE)
            edges.append(e); dots.append(d)
        self.say("done", wait=3)


    # ------------------------------------------------------------ the order
    def construct(self):
        self.caption = None
        self.step_axes()                # slide "Step 1", setup
        self.zoom(O + np.array([0.9, 0.3, 0]), 8)   # zoom in: the action is near O
        self.step_quarter_angle()       # slide "Step 1: quarter an angle"
        self.step_45_and_circle_AF()    # slide "Step 2: 45 degrees, then a circle"
        self.step_circle_E_and_raise()  # slide "Step 3: one more circle finds the answer"
        self.step_check()               # the P3 = 3/17, P5 = 5/17 claim, shown on the circle
        self.step_finish()              # slide "Step 4: finish it like Move 3"
