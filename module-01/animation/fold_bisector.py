"""Module 01, Move 2: why the perpendicular bisector is exact, shown as a fold.

Render (from this folder; manim lives in the `manim` conda env):

    conda run -n manim manim -qm --progress_bar none fold_bisector.py FoldBisector
    cp media/videos/fold_bisector/720p30/FoldBisector.mp4 fold_bisector.mp4

`media/` is a build folder and is gitignored. Colors match the deck's
`draw_bisect()` figure in ../slides.Rmd.
"""
from manim import *
import numpy as np

config.background_color = WHITE

BLUE_D = "#1769aa"    # the fold line PQ (deck `blue`)
RED_D = "#c0392b"     # the four radii (deck `red_c`)
GREEN_D = "#1b7a3d"   # the half that folds over (deck `grn_c`)
GREY_D = "#4d4d4d"
INK = BLACK

R = 2.8                     # the compass radius
DOWN_SHIFT = 0.6 * DOWN     # leave room for captions at the top
A = np.array([-2, 0, 0]) + DOWN_SHIFT
B = np.array([2, 0, 0]) + DOWN_SHIFT
h = np.sqrt(R**2 - 4)
P = np.array([0, h, 0]) + DOWN_SHIFT
Q = np.array([0, -h, 0]) + DOWN_SHIFT
M = (A + B) / 2


def caption(*lines):
    t = VGroup(*[Text(s, font_size=30, color=INK) for s in lines]).arrange(DOWN, buff=0.15)
    return t.to_edge(UP, buff=0.35)


def label(s, point, direction, color=INK):
    return Text(s, font_size=30, color=color).next_to(point, direction, buff=0.15)


class FoldBisector(Scene):
    def say(self, cap, *lines, wait=1.5):
        new = caption(*lines)
        if cap is None:
            self.play(FadeIn(new))
        else:
            self.play(FadeOut(cap), FadeIn(new))
        self.wait(wait)
        return new

    def construct(self):
        # 1. the construction
        cap = self.say(None, "Cut a segment exactly in half,", "with no measuring.")
        ab = Line(A, B, color=GREY_D, stroke_width=5)
        dA, dB = Dot(A, color=INK), Dot(B, color=INK)
        lA, lB = label("A", A, LEFT), label("B", B, RIGHT)
        self.play(Create(ab), FadeIn(dA, dB, lA, lB))

        cap = self.say(cap, "Compass on A, opened past halfway:", "arcs above and below.", wait=0.5)
        ang = np.arctan2(h, 2)
        arcs_A = VGroup(
            Arc(R, ang - 0.35, 0.7, arc_center=A, color=GREY_B),
            Arc(R, -ang - 0.35, 0.7, arc_center=A, color=GREY_B),
        )
        radius_A = Line(A, A + R * np.array([np.cos(ang - 0.35), np.sin(ang - 0.35), 0]), color=GREY_B)
        self.play(Create(radius_A))
        self.play(Create(arcs_A), FadeOut(radius_A))

        cap = self.say(cap, "Same width, compass on B.", wait=0.5)
        arcs_B = VGroup(
            Arc(R, PI - ang - 0.35, 0.7, arc_center=B, color=GREY_B),
            Arc(R, PI + ang - 0.35, 0.7, arc_center=B, color=GREY_B),
        )
        self.play(Create(arcs_B))

        dP, dQ = Dot(P, color=GREY_D), Dot(Q, color=GREY_D)
        lP, lQ = label("P", P, UL, GREY_D), label("Q", Q, DL, GREY_D)
        pq = Line(P + 0.6 * UP, Q + 0.6 * DOWN, color=BLUE_D, stroke_width=6)
        dM, lM = Dot(M, color=BLUE_D), label("M", M, DR, BLUE_D)
        self.play(FadeIn(dP, dQ, lP, lQ))
        self.play(Create(pq), FadeIn(dM, lM))

        # 2. the question first
        cap = self.say(cap, "Why is M exactly in the middle?", "And why is the corner square?", wait=2)

        # 3. the four equal lengths
        PA, PB = Line(P, A, color=RED_D), Line(P, B, color=RED_D)
        QA, QB = Line(Q, A, color=RED_D), Line(Q, B, color=RED_D)
        cap = self.say(cap, "The four red lines are each", "exactly one radius long.", wait=0.3)
        self.play(FadeOut(arcs_A, arcs_B), Create(PA), Create(QA), Create(PB), Create(QB))
        self.wait(1.5)

        # 4. the fold
        cap = self.say(cap, "Fold the page along the blue line PQ.", wait=0.3)
        ang_left = Angle(Line(M, P), Line(M, A), radius=0.45, color=ORANGE)
        ang_right = Angle(Line(M, B), Line(M, P), radius=0.45, color=ORANGE)
        self.play(Create(ang_left), Create(ang_right))
        left_half = VGroup(
            Line(P, A), Line(Q, A), Line(M, A), ang_left.copy(), Dot(A)
        ).set_color(GREEN_D)
        self.play(FadeIn(left_half))
        self.play(Rotate(left_half, angle=PI, axis=UP, about_point=M), run_time=3)
        self.play(Flash(B, color=GREEN_D))

        cap = self.say(
            cap,
            "A lands exactly on B. It must stay one radius from P",
            "and one radius from Q, and on that side only B does.",
            wait=2.5,
        )

        # 5. the payoff
        cap = self.say(cap, "M is on the fold, so it stays put.", "So MA folds onto MB: they are equal.", wait=2)
        self.play(FadeOut(left_half))

        deg_r = Text("90°", font_size=24, color=ORANGE).move_to(M + 0.8 * np.array([0.7, 0.7, 0]))
        deg_l = Text("90°", font_size=24, color=ORANGE).move_to(M + 0.8 * np.array([-0.7, 0.7, 0]))
        cap = self.say(
            cap,
            "The two angles at M fold onto each other, so they match.",
            "Together they make a straight line: 180 / 2 = 90.",
            wait=0.3,
        )
        self.play(FadeIn(deg_l, deg_r))
        self.wait(2.5)
