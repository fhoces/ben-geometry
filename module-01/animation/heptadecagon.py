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
    "axes":     ["Draw a circle around O, and a line through O.",
                 "It meets the circle at A, and at A' on the other side."],
    "right1":   ["Now a right angle at O. Open the compass wider and",
                 "draw equal arcs from A and from A'. They cross above O."],
    "right2":   ["O and that crossing are each the same distance from A and A',",
                 "so the line through them is square to OA. It meets the circle at B."],
    "mark_I":   ["Next, find I: a quarter of the way from O to B.",
                 "A quarter is half of a half, so we bisect twice."],
    "half1":    ["Move 2 on OB: equal arcs from O and from B.",
                 "Join where they cross: that line cuts OB in half."],
    "half2":    ["Now cut the lower half in half the same way.",
                 "That point is a quarter of the way up: call it I."],
    "angle":    ["Look at the angle at I, between IO and IA."],
    "bisect1":  ["Bisect it (Move 4): one arc from I across both sides,",
                 "then equal arcs from those two marks. Join I to the crossing."],
    "bisect2":  ["Bisect that half again, the same way: now we have a quarter.",
                 "Where it hits the line OA, call it E."],
    "turn45":   ["Next we need a 45-degree angle at I, turned from IE.",
                 "Recipe: build a right angle, then cut it in half."],
    "perp":     ["Right angle first. Compass on I: mark two points on",
                 "line IE, the same distance from I on each side."],
    "perp2":    ["Wider compass, from each mark: the arcs cross.",
                 "The line from I to that crossing is square to IE."],
    "bisect45": ["Now bisect that right angle (Move 4): one arc from I,",
                 "then two equal arcs from where it cuts each side."],
    "hitF":     ["Half of 90 is 45 degrees.", "Where this line hits line OA, call it F."],
    "midAF":    ["We need the circle with AF as its diameter,",
                 "so first find the exact middle of AF."],
    "midAF2":   ["Move 2: arcs from A and from F, same width.",
                 "Join the crossings: that line cuts AF in half at M."],
    "circleAF": ["Compass on M, opened to A: draw the circle.",
                 "It passes through F too, and crosses OB at K."],
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

    def dot_at(self, point, text, color, direction_):
        d = Dot(point, color=color, radius=0.07)
        l = Text(text, font_size=LABEL, color=color).next_to(d, direction_, buff=0.1)
        l.set_stroke(WHITE, width=5, background=True)
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
        A2 = O + R * LEFT                                            # the other end of the diameter
        self.OA = Line(A2, pt("A"), color=GREY_D)                    # line OA, right through O
        self.go(Create(self.OA))
        lab = lambda s, p, d: Text(s, font_size=LABEL, color=BLACK).next_to(p, d, buff=0.08)
        self.labels = VGroup(
            Dot(O, color=BLACK, radius=0.06), Text("O", font_size=LABEL, color=BLACK).next_to(O, DOWN, buff=0.45),
            Dot(pt("A"), color=BLACK, radius=0.06), lab("A", pt("A"), DR),
        )
        a2 = VGroup(Dot(A2, color=BLACK, radius=0.06), lab("A'", A2, DL))
        self.go(FadeIn(self.labels), FadeIn(a2), t=0.6)

        # the right angle at O: Move 2 on the two ends of the diameter
        self.say("right1", wait=0.3)
        r = 1.27 * R                                                 # wider than OA
        X = O + np.sqrt(r**2 - R**2) * UP                            # where the arcs from A and A' cross
        arcs = VGroup(self.compass(pt("A"), X, 0.18), self.compass(A2, X, 0.18))
        self.go(Create(arcs[0]), t=0.9)
        self.go(Create(arcs[1]), t=0.9)
        cross = Dot(X, color=BLACK, radius=0.05)
        self.go(FadeIn(cross, scale=2), t=0.4)
        self.say("right2", wait=0.3)
        self.OB = Line(O, pt("B"), color=GREY_D)
        square = RightAngle(Line(O, pt("A")), Line(O, pt("B")), length=0.3, color=BLUE_D)
        self.go(Create(self.OB), t=1.0)
        b = VGroup(Dot(pt("B"), color=BLACK, radius=0.06), lab("B", pt("B"), UR))
        self.go(Create(square), FadeIn(b), t=0.6)
        self.labels.add(*b)
        self.wait(1.5 * PACE)
        self.go(FadeOut(arcs, cross, square, a2), t=0.6)

    def bisect_segment(self, P, Q, key, color=GREY_B):
        """Move 2 on segment PQ: equal arcs from P and Q, join the crossings. Returns the midpoint."""
        mid, half = (P + Q) / 2, np.linalg.norm(Q - P) / 2
        u = (Q - P) / (2 * half)
        n = np.array([-u[1], u[0], 0])
        r = 1.4 * half                                                # wider than half of PQ
        h = np.sqrt(r**2 - half**2)
        X1, X2 = mid + h * n, mid - h * n                             # where the arcs cross
        self.say(key, wait=0.3)
        arcsP = VGroup(self.compass(P, X1, 0.2), self.compass(P, X2, 0.2))
        arcsQ = VGroup(self.compass(Q, X1, 0.2), self.compass(Q, X2, 0.2))
        self.go(Create(arcsP), t=0.8)
        self.go(Create(arcsQ), t=0.8)
        cut = DashedLine(X1, X2, color=color)
        self.go(Create(cut), t=0.7)
        return mid, VGroup(arcsP, arcsQ, cut)

    def step_find_I(self):
        self.say("mark_I", wait=1.5)
        Hm, g1 = self.bisect_segment(O, pt("B"), "half1")              # middle of OB
        h_dot = Dot(Hm, color=BLACK, radius=0.05)
        self.go(FadeIn(h_dot, scale=2), t=0.4)
        self.wait(0.5 * PACE)
        self.go(FadeOut(g1), t=0.5)
        Im, g2 = self.bisect_segment(O, Hm, "half2")                   # middle of the lower half
        assert np.allclose(Im, pt("I"))                               # it IS a quarter of OB
        self.I = self.dot("I", BLUE_D, LEFT)
        self.wait(PACE)
        self.go(FadeOut(g2, h_dot), t=0.5)

    def bisect_angle(self, apex, d1, d2, r_arc, r_cross):
        """Move 4: bisect the angle at `apex` between directions d1 and d2 (unit vectors).
        Returns the bisector direction and the scaffolding drawn."""
        U1, V1 = apex + r_arc * d1, apex + r_arc * d2
        bis = (d1 + d2) / np.linalg.norm(d1 + d2)
        half = np.linalg.norm(U1 - V1) / 2
        W = (U1 + V1) / 2 + np.sqrt(r_cross**2 - half**2) * bis       # equal arcs from U1, V1 cross here
        a1, a2 = np.arctan2(d1[1], d1[0]), np.arctan2(d2[1], d2[0])
        sweep = Arc(radius=r_arc, start_angle=min(a1, a2) - 0.12, angle=abs(a2 - a1) + 0.24,
                    arc_center=apex, color=GREY_B, stroke_width=3)
        self.go(Create(sweep), t=0.8)
        marks = VGroup(Dot(U1, radius=0.04, color=BLACK), Dot(V1, radius=0.04, color=BLACK))
        self.go(FadeIn(marks), t=0.3)
        cross = VGroup(self.compass(U1, W, 0.35), self.compass(V1, W, 0.35))
        self.go(Create(cross), t=0.9)
        return bis, VGroup(sweep, marks, cross)

    def step_quarter_angle(self):
        I = pt("I")
        dO, dA = direction(U["d_IO"]), direction(U["d_IA"])
        self.say("angle", wait=0.3)
        IA = DashedLine(I, pt("A"), color=BLUE_D)
        full = Angle(Line(I, O), Line(I, pt("A")), radius=0.25, color=BLUE_D)
        self.go(Create(IA), Create(full))
        self.wait(PACE)
        # first bisection: the angle OIA
        self.say("bisect1", wait=0.3)
        d_half, g1 = self.bisect_angle(I, dO, dA, 0.6, 0.5)
        half = Line(I, I + 1.0 * d_half, color=ORANGE_D, stroke_opacity=0.6)
        self.go(Create(half), t=0.8)
        self.wait(0.5 * PACE)
        self.go(FadeOut(g1), t=0.4)
        # second bisection: between IO and the half
        self.say("bisect2", wait=0.3)
        d_q, g2 = self.bisect_angle(I, dO, d_half, 0.6, 0.35)
        assert np.allclose(d_q, direction(U["d_IE"]))                 # it IS the quarter, so it lands on E
        quarter = Line(I, pt("E"), color=ORANGE_D, stroke_width=5)
        q_angle = Angle(Line(I, O), Line(I, pt("E")), radius=1.0, color=ORANGE_D)
        self.go(Create(quarter), Create(q_angle))
        self.E = self.dot("E", ORANGE_D, DOWN)
        self.go(FadeOut(half, full, IA, g2), t=0.6)
        self.IE, self.q_angle = quarter, q_angle

    def compass(self, center, target, spread=0.3, color=GREY_B):
        """A short compass arc: centered at `center`, passing through `target`."""
        v = target - center
        a = np.arctan2(v[1], v[0])
        return Arc(radius=np.linalg.norm(v), start_angle=a - spread, angle=2 * spread,
                   arc_center=center, color=color, stroke_width=3)

    def step_45(self):
        self.go(FadeOut(self.q_angle), t=0.4)
        self.say("turn45", wait=1.5)
        I = pt("I")
        dE = direction(U["d_IE"])                 # along IE
        dP = direction(U["d_IE"] - PI / 2)        # square to IE, on the side away from A
        bis = (dE + dP) / np.linalg.norm(dE + dP)  # halfway between them: 45 degrees from IE

        # 1. a right angle at I (Move 2's trick on two marks either side of I)
        self.say("perp", wait=0.3)
        r1, r2 = 0.6, 1.0
        X1, X2 = I + r1 * dE, I - r1 * dE
        back = DashedLine(I, I - 0.8 * dE, color=ORANGE_D)          # IE extended past I
        self.go(Create(back), t=0.6)
        arcs1 = VGroup(self.compass(I, X1), self.compass(I, X2))
        self.go(Create(arcs1), t=0.9)
        marks = VGroup(Dot(X1, radius=0.05, color=BLACK), Dot(X2, radius=0.05, color=BLACK))
        self.go(FadeIn(marks), t=0.4)
        self.say("perp2", wait=0.3)
        Y = I + np.sqrt(r2**2 - r1**2) * dP                            # where the two arcs cross
        arcs2 = VGroup(self.compass(X1, Y, 0.25), self.compass(X2, Y, 0.25))
        self.go(Create(arcs2), t=1.0)
        perp = Line(I, I + 1.3 * dP, color=BLUE_D, stroke_width=4)
        square = RightAngle(Line(I, I + dE), Line(I, I + dP), length=0.18, color=BLUE_D)
        self.go(Create(perp), Create(square), t=0.9)
        self.wait(PACE)
        scaffold1 = VGroup(arcs1, arcs2, marks, back)

        # 2. bisect the right angle (Move 4)
        self.say("bisect45", wait=0.3)
        r3 = 0.75
        Uc, Vc = I + r3 * dE, I + r3 * dP
        sweep = Arc(radius=r3, start_angle=U["d_IE"] - PI / 2 - 0.15, angle=PI / 2 + 0.3,
                    arc_center=I, color=GREY_B, stroke_width=3)
        self.go(FadeOut(scaffold1), Create(sweep), t=1.0)
        UV = VGroup(Dot(Uc, radius=0.05, color=BLACK), Dot(Vc, radius=0.05, color=BLACK))
        self.go(FadeIn(UV), t=0.4)
        half = np.linalg.norm(Uc - Vc) / 2
        W = (Uc + Vc) / 2 + np.sqrt(r3**2 - half**2) * bis                # equal arcs from U and V cross here
        arcs4 = VGroup(self.compass(Uc, W, 0.3), self.compass(Vc, W, 0.3))
        self.go(Create(arcs4), t=1.0)

        # 3. the 45-degree line, out to line OA
        self.say("hitF", wait=0.3)
        IF = Line(I, pt("F"), color=RED_D, stroke_width=5)
        beyond = DashedLine(pt("F"), W, color=RED_D)       # the line runs on past F to the arc crossing
        a45 = Angle(Line(I, pt("F")), Line(I, pt("E")), radius=0.35, color=RED_D)
        t45 = Text("45°", font_size=14, color=RED_D).move_to(I + 0.55 * direction(U["d_IE"] - PI / 8))
        self.go(Create(IF), Create(beyond), Create(a45), FadeIn(t45), t=1.2)
        self.IF = IF
        self.F = self.dot("F", RED_D, DOWN)
        self.wait(1.5 * PACE)
        self.go(FadeOut(a45, t45, perp, square, sweep, UV, arcs4, beyond), t=0.6)

    def step_circle_AF(self):
        self.say("midAF", wait=1.2)
        A, F = pt("A"), pt("F")
        Mid = (A + F) / 2
        r = 0.57 * np.linalg.norm(A - F)                                # a bit more than half of AF
        h = np.sqrt(r**2 - (np.linalg.norm(A - F) / 2) ** 2)
        top, bottom = Mid + h * UP, Mid + h * DOWN                      # where the arcs from A and F cross
        self.say("midAF2", wait=0.3)
        arcsA = VGroup(self.compass(A, top, 0.22), self.compass(A, bottom, 0.22))
        arcsF = VGroup(self.compass(F, top, 0.22), self.compass(F, bottom, 0.22))
        self.go(Create(arcsA), t=1.0)
        self.go(Create(arcsF), t=1.0)
        cut = DashedLine(top, bottom, color=GREEN_D)
        self.go(Create(cut), t=0.8)
        self.M = self.dot_at(Mid, "M", GREEN_D, DR)
        self.wait(PACE)
        self.say("circleAF", wait=0.3)
        self.go(FadeOut(arcsA, arcsF, cut), t=0.5)
        radius_line = Line(Mid, A, color=GREEN_D)
        self.go(Create(radius_line), t=0.6)
        self.cAF = DashedVMobject(Circle(radius=np.linalg.norm(A - Mid), color=GREEN_D).move_to(Mid), num_dashes=60)
        self.go(Create(self.cAF), FadeOut(radius_line), t=2)
        self.K = self.dot("K", GREEN_D, RIGHT)
        self.go(FadeOut(self.M), t=0.4)

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
        self.step_find_I()              # I = a quarter of OB, by bisecting twice
        self.zoom(O + np.array([0.9, 0.3, 0]), 8)   # zoom in: the action is near O
        self.step_quarter_angle()       # slide "Step 1: quarter an angle"
        self.step_45()                  # slide "Step 2": building the 45-degree angle
        self.step_circle_AF()           # slide "Step 2": the circle on AF (midpoint first)
        self.step_circle_E_and_raise()  # slide "Step 3: one more circle finds the answer"
        self.step_check()               # the P3 = 3/17, P5 = 5/17 claim, shown on the circle
        self.step_finish()              # slide "Step 4: finish it like Move 3"
