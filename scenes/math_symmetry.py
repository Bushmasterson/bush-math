# pyright: reportWildcardImportFromLibrary=false

import os
from manim import *
import numpy as np

from _style import StyledScene, MAIN_YELLOW, MAIN_BLUE


class MathSymmetry(StyledScene):
    """
    Fast-paced 44-second piece: sin, cos, Euler, mirror symmetry.
    Rhythm: ~2-second beats, heavy use of Transform.
    """

    SOUNDTRACK = "assets/soundtrack.mp3"

    def construct(self) -> None:
        YELLOW = MAIN_YELLOW
        BLUE = MAIN_BLUE
        GREY = ManimColor("#666666")
        FAINT = ManimColor("#2A2A2A")

        if os.path.exists(self.SOUNDTRACK):
            self.add_sound(self.SOUNDTRACK, gain=-6)

        # ═════════════════════════════════════════════════
        # ACT 1 · 0.0–2.5s · title flash
        # ═════════════════════════════════════════════════
        title = Text("MATHEMATICAL", color=YELLOW, font_size=72)
        title2 = Text("SYMMETRY", color=BLUE, font_size=72).next_to(title, DOWN, buff=0.2)
        group = VGroup(title, title2).move_to(ORIGIN)

        self.play(FadeIn(group, shift=UP * 0.3, scale=0.9), run_time=0.8)
        self.play(group.animate.scale(1.05), run_time=0.3)
        self.play(group.animate.scale(1 / 1.05), run_time=0.3)
        self.play(FadeOut(group), run_time=0.4)
        # 1.8s → pad 0.7s with wait

        # ═════════════════════════════════════════════════
        # ACT 2 · 2.5–10.5s · unit circle → sine
        # ═════════════════════════════════════════════════
        circle_center = LEFT * 3.5
        circle = Circle(radius=1.6, color=BLUE, stroke_width=4).move_to(circle_center)

        axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-1.5, 1.5, 1],
            x_length=8,
            y_length=3,
            axis_config={
                "include_tip": False,
                "stroke_color": BLUE,
                "stroke_width": 3,
                "include_numbers": False,
            },
        ).shift(RIGHT * 2.5)

        # Fast entrance — simultaneous
        self.play(
            LaggedStart(
                Create(circle),
                Create(axes),
                lag_ratio=0.3,
            ),
            run_time=0.7,
        )

        theta = ValueTracker(0.0)

        def circle_pt() -> np.ndarray:
            a = theta.get_value()
            return circle_center + 1.6 * np.array([np.cos(a), np.sin(a), 0.0])

        def sine_pt() -> np.ndarray:
            return axes.c2p(theta.get_value(), np.sin(theta.get_value()))

        radius = always_redraw(
            lambda: Line(circle_center, circle_pt(), color=YELLOW, stroke_width=4)
        )
        dot_c = always_redraw(lambda: Dot(circle_pt(), color=YELLOW, radius=0.1))
        dot_s = always_redraw(lambda: Dot(sine_pt(), color=YELLOW, radius=0.1))
        connector = always_redraw(
            lambda: DashedLine(
                circle_pt(), sine_pt(),
                color=FAINT, stroke_width=1.5, dash_length=0.1,
            )
        )
        curve = always_redraw(
            lambda: axes.plot(
                np.sin,
                x_range=[0, max(theta.get_value(), 1e-3)],
                color=YELLOW, stroke_width=4,
            )
        )

        self.add(radius, dot_c, dot_s, connector, curve)
        self.play(theta.animate.set_value(4 * PI), run_time=6.0, rate_func=linear)
        self.wait(0.3)
        # 10.5s

        # ═════════════════════════════════════════════════
        # ACT 3 · 10.5–15.5s · cos appears (symmetry)
        # ═════════════════════════════════════════════════
        cosine_curve = axes.plot(np.cos, x_range=[0, 4 * PI], color=BLUE, stroke_width=4)
        sin_label = Text("sin", color=YELLOW, font_size=36).to_corner(UL, buff=0.5)
        cos_label = Text("cos", color=BLUE, font_size=36).next_to(sin_label, DOWN, buff=0.2)

        self.play(
            FadeOut(radius, dot_c, dot_s, connector),
            Create(cosine_curve),
            run_time=0.8,
        )
        self.play(
            LaggedStart(
                FadeIn(sin_label, shift=RIGHT * 0.2),
                FadeIn(cos_label, shift=RIGHT * 0.2),
                lag_ratio=0.4,
            ),
            run_time=0.6,
        )
        self.wait(0.5)
        # ~12.4s

        # Flash focus between sin and cos
        for _ in range(2):
            self.play(sin_label.animate.scale(1.15), cos_label.animate.scale(0.9), run_time=0.2)
            self.play(cos_label.animate.scale(1.15 / 0.9), sin_label.animate.scale(1 / 1.15), run_time=0.2)
        # ~13.2s

        # Sin curve transforms to cos (visible shift)
        shifted_curve = axes.plot(np.cos, x_range=[0, 4 * PI], color=YELLOW, stroke_width=4)
        self.play(
            Transform(curve, shifted_curve),
            run_time=0.7,
        )
        self.wait(0.3)
        # ~14.2s → pad to 15.5

        # ═════════════════════════════════════════════════
        # ACT 4 · 15.5–19.5s · identity flash
        # ═════════════════════════════════════════════════
        self.play(
            FadeOut(curve, cosine_curve, sin_label, cos_label),
            run_time=0.4,
        )
        # 15.9s

        identity = Text("sin²(θ) + cos²(θ) = 1", color=YELLOW, font_size=64)
        self.play(FadeIn(identity, scale=1.3), run_time=0.6)
        # 16.5s

        # Color pulse × 3
        for _ in range(3):
            self.play(identity.animate.set_color(BLUE), run_time=0.2)
            self.play(identity.animate.set_color(YELLOW), run_time=0.2)
        # 17.7s

        self.play(FadeOut(identity), run_time=0.4)
        # 18.1s → pad to 19.5

        # ═════════════════════════════════════════════════
        # ACT 5 · 19.5–28.0s · Euler spiral
        # ═════════════════════════════════════════════════
        euler = Text("e^(iθ) = cos(θ) + i·sin(θ)", color=BLUE, font_size=44)
        euler.to_edge(UP, buff=0.6)
        self.play(FadeIn(euler, shift=DOWN * 0.3), run_time=0.7)
        # 20.2s

        # Static axes (no complex plane to keep it light)
        small_axes = Axes(
            x_range=[-1.5, 1.5, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=3.2,
            y_length=3.2,
            axis_config={
                "include_tip": False,
                "stroke_color": BLUE,
                "stroke_width": 2,
                "include_numbers": False,
            },
        )
        unit_circle = Circle(radius=1.0, color=BLUE, stroke_width=2)
        self.play(
            Create(small_axes),
            Create(unit_circle),
            run_time=0.6,
        )
        # 20.8s

        t = ValueTracker(0.0)

        def rot_pt() -> np.ndarray:
            a = t.get_value()
            return np.array([np.cos(a), np.sin(a), 0.0])

        rot_vec = always_redraw(
            lambda: Line(ORIGIN, rot_pt(), color=YELLOW, stroke_width=5)
        )
        rot_dot = always_redraw(lambda: Dot(rot_pt(), color=YELLOW, radius=0.1))
        spiral_curve = always_redraw(
            lambda: ParametricFunction(
                lambda a: np.array([np.cos(a), np.sin(a), 0.0]),
                t_range=(0.0, max(t.get_value(), 1e-3), 0.05),
                color=YELLOW,
                stroke_width=2,
            )
        )

        self.add(spiral_curve, rot_vec, rot_dot)
        self.play(t.animate.set_value(6 * PI), run_time=6.5, rate_func=linear)
        self.wait(0.2)
        # 27.5s

        self.play(
            FadeOut(spiral_curve, rot_vec, rot_dot, small_axes, unit_circle, euler),
            run_time=0.5,
        )
        # 28.0s

        # ═════════════════════════════════════════════════
        # ACT 6 · 28.0–34.0s · mirror symmetry
        # ═════════════════════════════════════════════════
        axes2 = Axes(
            x_range=[-4 * PI, 4 * PI, PI],
            y_range=[-1.5, 1.5, 1],
            x_length=12,
            y_length=3,
            axis_config={
                "include_tip": False,
                "stroke_color": BLUE,
                "stroke_width": 3,
                "include_numbers": False,
            },
        )

        sin_wave = axes2.plot(np.sin, x_range=[0, 4 * PI], color=YELLOW, stroke_width=3)
        cos_wave = axes2.plot(np.cos, x_range=[0, 4 * PI], color=BLUE, stroke_width=3)
        sin_mirror = axes2.plot(
            lambda x: np.sin(-x), x_range=[-4 * PI, 0], color=YELLOW, stroke_width=3
        )
        cos_mirror = axes2.plot(
            lambda x: np.cos(-x), x_range=[-4 * PI, 0], color=BLUE, stroke_width=3
        )

        self.play(Create(axes2), run_time=0.4)
        self.play(
            LaggedStart(
                Create(sin_wave),
                Create(cos_wave),
                Create(sin_mirror),
                Create(cos_mirror),
                lag_ratio=0.15,
            ),
            run_time=2.0,
        )
        # 30.4s

        sym_line = DashedLine(
            axes2.c2p(0, -1.5), axes2.c2p(0, 1.5),
            color=GREY, stroke_width=2,
        )
        self.play(Create(sym_line), run_time=0.3)
        self.wait(0.3)
        # 31.0s

        # Mirror flash — quick swaps
        for _ in range(3):
            self.play(
                sin_mirror.animate.set_opacity(0.2),
                cos_mirror.animate.set_opacity(0.2),
                run_time=0.2,
            )
            self.play(
                sin_mirror.animate.set_opacity(1.0),
                cos_mirror.animate.set_opacity(1.0),
                run_time=0.2,
            )
        # 32.2s

        self.play(
            FadeOut(sym_line, cos_mirror, sin_mirror),
            run_time=0.4,
        )
        # 32.6s

        # ═════════════════════════════════════════════════
        # ACT 7 · 32.6–44.0s · convergence + finale
        # ═════════════════════════════════════════════════

        # Random dots along sine
        rng = np.random.default_rng(42)
        dots = VGroup(*[
            Dot(
                axes2.c2p(
                    float(rng.uniform(0, 4 * PI)),
                    float(np.sin(rng.uniform(0, 4 * PI))),
                ),
                color=YELLOW,
                radius=0.05,
            )
            for _ in range(40)
        ])

        self.play(
            LaggedStart(
                *[FadeIn(d, scale=0.2) for d in dots],
                lag_ratio=0.02,
            ),
            run_time=1.5,
        )
        # 34.1s

        final_text = Text("SYMMETRY", color=YELLOW, font_size=140)
        final_text.move_to(ORIGIN)

        self.play(
            FadeOut(axes2, sin_wave, cos_wave, dots),
            FadeIn(final_text, scale=1.5),
            run_time=1.0,
        )
        # 35.1s

        # Pulse
        for _ in range(4):
            self.play(final_text.animate.set_color(BLUE).scale(1.06), run_time=0.2)
            self.play(final_text.animate.set_color(YELLOW).scale(1 / 1.06), run_time=0.2)
        # 36.7s

        self.wait(6.7)
        # 44.0s