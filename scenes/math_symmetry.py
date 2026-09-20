# pyright: reportWildcardImportFromLibrary=false

import os
from manim import *
import numpy as np

from _style import StyledScene, MAIN_YELLOW, MAIN_BLUE


class MathSymmetry(StyledScene):
    """
    88-second fast-paced journey through mathematics:
    geometry → trigonometry → algebra → analysis → series → symmetry.
    All labels use Unicode — no LaTeX required.
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
        # ACT 1 · 0.0–3.0s · MATHEMATICAL SYMMETRY
        # ═════════════════════════════════════════════════
        title = Text("MATHEMATICAL", color=YELLOW, font_size=72)
        title2 = Text("SYMMETRY", color=BLUE, font_size=72).next_to(title, DOWN, buff=0.2)
        group = VGroup(title, title2).move_to(ORIGIN)

        self.play(FadeIn(group, shift=UP * 0.3, scale=0.9), run_time=0.8)
        self.play(group.animate.scale(1.05), run_time=0.3)
        self.play(group.animate.scale(1 / 1.05), run_time=0.3)
        self.play(FadeOut(group), run_time=0.5)
        self.wait(1.1)
        # 3.0s

        # ═════════════════════════════════════════════════
        # ACT 2 · 3.0–14.0s · Geometry · Pythagoras
        # ═════════════════════════════════════════════════
        a_line = Line(ORIGIN, RIGHT * 3, color=YELLOW, stroke_width=5)
        b_line = Line(RIGHT * 3, RIGHT * 3 + UP * 4, color=BLUE, stroke_width=5)
        c_line = Line(ORIGIN, RIGHT * 3 + UP * 4, color=YELLOW, stroke_width=5)

        right_angle = RightAngle(
            Line(RIGHT * 3, ORIGIN), Line(RIGHT * 3, RIGHT * 3 + UP * 4),
            length=0.4, color=BLUE,
        )

        a_lbl = Text("a", color=YELLOW, font_size=40).next_to(a_line, DOWN, buff=0.15)
        b_lbl = Text("b", color=BLUE, font_size=40).next_to(b_line, RIGHT, buff=0.15)
        c_lbl = Text("c", color=YELLOW, font_size=40).next_to(c_line.get_center(), LEFT, buff=0.2)

        self.play(
            Create(a_line), Create(b_line),
            FadeIn(right_angle),
            run_time=0.8,
        )
        self.play(
            Create(c_line),
            LaggedStart(
                FadeIn(a_lbl), FadeIn(b_lbl), FadeIn(c_lbl),
                lag_ratio=0.3,
            ),
            run_time=0.6,
        )
        # 4.4s

        pyth = Text("a² + b² = c²", color=YELLOW, font_size=64).move_to(ORIGIN)
        self.play(
            FadeOut(a_line, b_line, c_line, a_lbl, b_lbl, c_lbl, right_angle),
            FadeIn(pyth, scale=1.3),
            run_time=0.7,
        )
        # 5.1s

        for _ in range(3):
            self.play(pyth.animate.set_color(BLUE), run_time=0.15)
            self.play(pyth.animate.set_color(YELLOW), run_time=0.15)
        # 6.0s

        # Square-on-hypotenuse diagram
        squares = VGroup(
            Square(side_length=3, color=YELLOW, fill_opacity=0.1).move_to(
                np.array([1.5, -1.5, 0.0])
            ),
            Square(side_length=4, color=BLUE, fill_opacity=0.1).move_to(
                np.array([5.0, 2.0, 0.0])
            ),
        )
        self.play(
            FadeOut(pyth),
            LaggedStart(
                Create(squares[0]),
                Create(squares[1]),
                lag_ratio=0.4,
            ),
            run_time=0.8,
        )
        self.wait(0.3)
        self.play(FadeOut(squares), run_time=0.5)
        # 7.6s

        # Circle + pi
        circ_geo = Circle(radius=1.5, color=BLUE, stroke_width=4)
        r_line = Line(ORIGIN, RIGHT * 1.5, color=YELLOW, stroke_width=4)
        r_lbl = Text("r", color=YELLOW, font_size=40).next_to(r_line, UP, buff=0.1)
        self.play(
            LaggedStart(
                Create(circ_geo), Create(r_line), FadeIn(r_lbl),
                lag_ratio=0.3,
            ),
            run_time=0.8,
        )
        # 8.4s

        circ_formula = Text("C = 2πr    A = πr²", color=YELLOW, font_size=48)
        circ_formula.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(circ_formula, shift=UP * 0.3), run_time=0.6)
        self.wait(0.4)
        # 9.4s

        self.play(
            FadeOut(circ_geo, r_line, r_lbl, circ_formula),
            run_time=0.5,
        )
        # 9.9s

        # Angles — triangle sum
        tri_pts = [
            np.array([-2.0, -1.5, 0.0]),
            np.array([2.0, -1.5, 0.0]),
            np.array([0.5, 1.5, 0.0]),
        ]
        tri = Polygon(*tri_pts, color=BLUE, stroke_width=4)
        self.play(Create(tri), run_time=0.6)
        # 10.5s

        ang_labels = VGroup(
            Text("α", color=YELLOW, font_size=36).move_to(np.array([-1.4, -1.1, 0.0])),
            Text("β", color=YELLOW, font_size=36).move_to(np.array([1.5, -1.1, 0.0])),
            Text("γ", color=YELLOW, font_size=36).move_to(np.array([0.35, 0.9, 0.0])),
        )
        self.play(
            LaggedStart(*[FadeIn(a, scale=1.3) for a in ang_labels], lag_ratio=0.25),
            run_time=0.6,
        )
        # 11.1s

        angle_sum = Text("α + β + γ = 180°", color=YELLOW, font_size=48)
        angle_sum.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(angle_sum, shift=UP * 0.3), run_time=0.5)
        self.wait(0.4)
        self.play(FadeOut(tri, ang_labels, angle_sum), run_time=0.5)
        # 12.5s
        self.wait(1.5)
        # 14.0s

        # ═════════════════════════════════════════════════
        # ACT 3 · 14.0–27.0s · Trigonometry · unit circle
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

        self.play(
            LaggedStart(Create(circle), Create(axes), lag_ratio=0.3),
            run_time=0.7,
        )
        # 14.7s

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
        self.play(theta.animate.set_value(4 * PI), run_time=5.5, rate_func=linear)
        self.wait(0.3)
        # 20.5s

        # Cos appears
        cos_curve = axes.plot(np.cos, x_range=[0, 4 * PI], color=BLUE, stroke_width=4)
        sin_lbl = Text("sin", color=YELLOW, font_size=36).to_corner(UL, buff=0.5)
        cos_lbl = Text("cos", color=BLUE, font_size=36).next_to(sin_lbl, DOWN, buff=0.2)

        self.play(
            FadeOut(radius, dot_c, dot_s, connector),
            Create(cos_curve),
            run_time=0.7,
        )
        # 21.2s

        self.play(
            LaggedStart(
                FadeIn(sin_lbl, shift=RIGHT * 0.2),
                FadeIn(cos_lbl, shift=RIGHT * 0.2),
                lag_ratio=0.4,
            ),
            run_time=0.5,
        )
        # 21.7s

        for _ in range(2):
            self.play(sin_lbl.animate.scale(1.15), cos_lbl.animate.scale(0.9), run_time=0.18)
            self.play(cos_lbl.animate.scale(1.15 / 0.9), sin_lbl.animate.scale(1 / 1.15), run_time=0.18)
        # 22.4s

        shifted = axes.plot(np.cos, x_range=[0, 4 * PI], color=YELLOW, stroke_width=4)
        self.play(Transform(curve, shifted), run_time=0.7)
        # 23.1s

        self.play(FadeOut(curve, cos_curve, sin_lbl, cos_lbl), run_time=0.4)
        # 23.5s

        # Identity
        identity = Text("sin²(θ) + cos²(θ) = 1", color=YELLOW, font_size=64)
        self.play(FadeIn(identity, scale=1.3), run_time=0.6)
        for _ in range(3):
            self.play(identity.animate.set_color(BLUE), run_time=0.18)
            self.play(identity.animate.set_color(YELLOW), run_time=0.18)
        # 25.4s
        self.play(FadeOut(identity), run_time=0.4)
        # 25.8s
        self.wait(1.2)
        # 27.0s

        # ═════════════════════════════════════════════════
        # ACT 4 · 27.0–38.0s · Algebra · identities
        # ═════════════════════════════════════════════════
        formulas = [
            Text("(a + b)² = a² + 2ab + b²", color=YELLOW, font_size=52),
            Text("(a − b)² = a² − 2ab + b²", color=BLUE, font_size=52),
            Text("a² − b² = (a − b)(a + b)", color=YELLOW, font_size=52),
            Text("(a + b)³ = a³ + 3a²b + 3ab² + b³", color=BLUE, font_size=48),
            Text("e^(iπ) + 1 = 0", color=YELLOW, font_size=64),
        ]

        for f in formulas:
            f.move_to(ORIGIN)
            self.play(FadeIn(f, shift=UP * 0.3, scale=1.2), run_time=0.5)
            self.wait(0.4)
            self.play(FadeOut(f, shift=DOWN * 0.3), run_time=0.4)
            # ~1.3s per formula × 5 = 6.5s
        # 33.5s

        # Polynomial graph — quadratic
        poly_axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 6, 1],
            x_length=6,
            y_length=4,
            axis_config={
                "include_tip": False,
                "stroke_color": BLUE,
                "stroke_width": 3,
                "include_numbers": False,
            },
        )
        parabola = poly_axes.plot(
            lambda x: x * x, color=YELLOW, stroke_width=4,
        )
        quad_lbl = Text("y = x²", color=YELLOW, font_size=40)
        quad_lbl.to_corner(UL, buff=0.5)

        self.play(Create(poly_axes), run_time=0.5)
        self.play(
            Create(parabola),
            FadeIn(quad_lbl),
            run_time=0.6,
        )
        # 34.6s

        cubic = poly_axes.plot(
            lambda x: 0.3 * x * x * x, color=BLUE, stroke_width=4,
        )
        cubic_lbl = Text("y = x³", color=BLUE, font_size=40)
        cubic_lbl.next_to(quad_lbl, DOWN, buff=0.2)

        self.play(
            Transform(parabola, cubic),
            FadeIn(cubic_lbl),
            run_time=0.6,
        )
        # 35.2s

        sine_poly = poly_axes.plot(
            lambda x: np.sin(x), color=YELLOW, stroke_width=4,
        )
        sine_lbl = Text("y = sin(x)", color=YELLOW, font_size=40)
        sine_lbl.next_to(cubic_lbl, DOWN, buff=0.2)

        self.play(
            Transform(parabola, sine_poly),
            FadeIn(sine_lbl),
            run_time=0.6,
        )
        # 35.8s

        # Flash each
        for _ in range(2):
            self.play(
                quad_lbl.animate.set_opacity(1.0).scale(1.15),
                cubic_lbl.animate.set_opacity(0.3),
                sine_lbl.animate.set_opacity(0.3),
                run_time=0.2,
            )
            self.play(
                quad_lbl.animate.scale(1 / 1.15).set_opacity(0.3),
                cubic_lbl.animate.set_opacity(1.0).scale(1.15),
                run_time=0.2,
            )
            self.play(
                cubic_lbl.animate.scale(1 / 1.15).set_opacity(0.3),
                sine_lbl.animate.set_opacity(1.0).scale(1.15),
                run_time=0.2,
            )
            self.play(
                sine_lbl.animate.scale(1 / 1.15).set_opacity(0.3),
                run_time=0.2,
            )
        # 37.4s

        self.play(
            FadeOut(poly_axes, parabola, quad_lbl, cubic_lbl, sine_lbl),
            run_time=0.6,
        )
        # 38.0s

        # ═════════════════════════════════════════════════
        # ACT 5 · 38.0–49.0s · Euler + complex plane
        # ═════════════════════════════════════════════════
        euler = Text("e^(iθ) = cos(θ) + i·sin(θ)", color=BLUE, font_size=44)
        euler.to_edge(UP, buff=0.6)
        self.play(FadeIn(euler, shift=DOWN * 0.3), run_time=0.6)
        # 38.6s

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
            run_time=0.5,
        )
        # 39.1s

        t = ValueTracker(0.0)

        def rot_pt() -> np.ndarray:
            a = t.get_value()
            return np.array([np.cos(a), np.sin(a), 0.0])

        rot_vec = always_redraw(
            lambda: Line(ORIGIN, rot_pt(), color=YELLOW, stroke_width=5)
        )
        rot_dot = always_redraw(lambda: Dot(rot_pt(), color=YELLOW, radius=0.1))
        spiral = always_redraw(
            lambda: ParametricFunction(
                lambda a: np.array([np.cos(a), np.sin(a), 0.0]),
                t_range=(0.0, max(t.get_value(), 1e-3), 0.05),
                color=YELLOW, stroke_width=2,
            )
        )

        self.add(spiral, rot_vec, rot_dot)
        self.play(t.animate.set_value(6 * PI), run_time=5.5, rate_func=linear)
        self.wait(0.3)
        # 44.9s

        self.play(
            FadeOut(spiral, rot_vec, rot_dot, small_axes, unit_circle, euler),
            run_time=0.5,
        )
        # 45.4s

        # Complex roots flash
        roots = [
            ("i⁰ = 1", YELLOW),
            ("i¹ = i", BLUE),
            ("i² = −1", YELLOW),
            ("i³ = −i", BLUE),
            ("i⁴ = 1", YELLOW),
        ]
        for text, color in roots:
            r = Text(text, color=color, font_size=72).move_to(ORIGIN)
            self.play(FadeIn(r, scale=1.4), run_time=0.35)
            self.play(FadeOut(r, scale=0.9), run_time=0.35)
            # 0.7s each × 5 = 3.5s
        # 48.9s
        self.wait(0.1)
        # 49.0s

        # ═════════════════════════════════════════════════
        # ACT 6 · 49.0–61.0s · Derivative · tangent
        # ═════════════════════════════════════════════════
        d_axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 4, 1],
            x_length=7,
            y_length=5,
            axis_config={
                "include_tip": False,
                "stroke_color": BLUE,
                "stroke_width": 3,
                "include_numbers": False,
            },
        )

        f_curve = d_axes.plot(lambda x: 0.5 * x * x, color=YELLOW, stroke_width=4)
        f_lbl = Text("f(x) = ½x²", color=YELLOW, font_size=40)
        f_lbl.to_corner(UL, buff=0.5)

        self.play(Create(d_axes), run_time=0.5)
        self.play(Create(f_curve), FadeIn(f_lbl), run_time=0.6)
        # 50.1s

        x0 = ValueTracker(1.0)

        def tangent_line() -> Line:
            xv = x0.get_value()
            slope = xv
            yv = 0.5 * xv * xv
            p1 = d_axes.c2p(xv - 0.7, yv - slope * 0.7)
            p2 = d_axes.c2p(xv + 0.7, yv + slope * 0.7)
            return Line(p1, p2, color=BLUE, stroke_width=4)

        tangent = always_redraw(tangent_line)
        point = always_redraw(
            lambda: Dot(
                d_axes.c2p(x0.get_value(), 0.5 * x0.get_value() ** 2),
                color=YELLOW, radius=0.1,
            )
        )

        self.add(tangent, point)

        deriv_lbl = Text("f'(x) = x", color=BLUE, font_size=40)
        deriv_lbl.to_corner(UR, buff=0.5)
        self.play(FadeIn(deriv_lbl), run_time=0.4)
        # 50.5s

        self.play(x0.animate.set_value(3.0), run_time=3.0, rate_func=smooth)
        self.play(x0.animate.set_value(0.5), run_time=2.0, rate_func=smooth)
        self.play(x0.animate.set_value(2.5), run_time=2.0, rate_func=smooth)
        # 57.5s

        self.play(
            FadeOut(d_axes, f_curve, tangent, point, f_lbl, deriv_lbl),
            run_time=0.5,
        )
        # 58.0s

        limit_lbl = Text("f'(x) = lim  (f(x+h) − f(x)) / h", color=YELLOW, font_size=44)
        limit_lbl.move_to(ORIGIN)
        self.play(FadeIn(limit_lbl, scale=1.3), run_time=0.6)
        for _ in range(2):
            self.play(limit_lbl.animate.set_color(BLUE), run_time=0.2)
            self.play(limit_lbl.animate.set_color(YELLOW), run_time=0.2)
        # 59.4s
        self.play(FadeOut(limit_lbl), run_time=0.4)
        # 59.8s
        self.wait(1.2)
        # 61.0s

        # ═════════════════════════════════════════════════
        # ACT 7 · 61.0–72.0s · Integral · area
        # ═════════════════════════════════════════════════
        i_axes = Axes(
            x_range=[-0.5, 4, 1],
            y_range=[-0.5, 4, 1],
            x_length=7,
            y_length=5,
            axis_config={
                "include_tip": False,
                "stroke_color": BLUE,
                "stroke_width": 3,
                "include_numbers": False,
            },
        )
        g_curve = i_axes.plot(
            lambda x: 0.7 * np.sin(x) + 1.5,
            x_range=[0, 3.5],
            color=YELLOW, stroke_width=4,
        )
        i_lbl = Text("∫ f(x) dx", color=YELLOW, font_size=48)
        i_lbl.to_corner(UL, buff=0.5)

        self.play(Create(i_axes), run_time=0.5)
        self.play(Create(g_curve), FadeIn(i_lbl), run_time=0.6)
        # 62.1s

        # Growing area under curve — Riemann
        x_riemann = ValueTracker(0.0)

        def riemann_rects() -> VGroup:
            xv = x_riemann.get_value()
            n = max(int(xv * 8), 0)
            if n == 0:
                return VGroup()
            dx = xv / n
            rects = VGroup()
            for i in range(n):
                x_left = i * dx
                h = 0.7 * np.sin(x_left) + 1.5
                rect = Rectangle(
                    width=i_axes.c2p(dx, 0)[0] - i_axes.c2p(0, 0)[0],
                    height=i_axes.c2p(0, h)[1] - i_axes.c2p(0, 0)[1],
                    color=BLUE,
                    fill_opacity=0.4,
                    stroke_width=1,
                )
                rect.move_to(i_axes.c2p(x_left + dx / 2, h / 2))
                rects.add(rect)
            return rects

        riemann = always_redraw(riemann_rects)
        self.add(riemann)
        self.play(x_riemann.animate.set_value(3.5), run_time=5.5, rate_func=linear)
        # 67.6s

        area_lbl = Text("Area = ∫₀³·⁵ f(x) dx", color=BLUE, font_size=40)
        area_lbl.to_corner(UR, buff=0.5)
        self.play(FadeIn(area_lbl), run_time=0.4)
        self.wait(0.5)
        # 68.5s

        self.play(
            FadeOut(i_axes, g_curve, riemann, i_lbl, area_lbl),
            run_time=0.5,
        )
        # 69.0s

        ftc = Text("∫ₐᵇ f'(x) dx = f(b) − f(a)", color=YELLOW, font_size=44)
        ftc.move_to(ORIGIN)
        self.play(FadeIn(ftc, scale=1.3), run_time=0.6)
        self.wait(1.4)
        # 71.0s
        self.play(FadeOut(ftc), run_time=0.5)
        # 71.5s
        self.wait(0.5)
        # 72.0s

        # ═════════════════════════════════════════════════
        # ACT 8 · 72.0–83.0s · Taylor + Fourier flash
        # ═════════════════════════════════════════════════
        taylor = Text("sin(x) = x − x³/3! + x⁵/5! − …", color=YELLOW, font_size=44)
        taylor.move_to(ORIGIN)
        self.play(FadeIn(taylor, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(taylor), run_time=0.3)
        # 73.3s

        fourier = Text("f(x) = Σ (aₙ cos(nx) + bₙ sin(nx))", color=BLUE, font_size=40)
        fourier.move_to(ORIGIN)
        self.play(FadeIn(fourier, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(fourier), run_time=0.3)
        # 74.6s

        # Fourier sum visualization
        f_axes = Axes(
            x_range=[-PI, PI, PI / 2],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=3,
            axis_config={
                "include_tip": False,
                "stroke_color": BLUE,
                "stroke_width": 3,
                "include_numbers": False,
            },
        )
        self.play(Create(f_axes), run_time=0.4)
        # 75.0s

        def fourier_partial(n_terms: int):
            def f(x):
                result = 0.0
                for k in range(1, n_terms + 1):
                    result += (4 / PI) * np.sin((2 * k - 1) * x) / (2 * k - 1)
                return result
            return f

        # Animate partial sums
        first_wave = None
        for n in [1, 3, 7, 15]:
            wave = f_axes.plot(
                fourier_partial(n), x_range=[-PI, PI, 0.01],
                color=YELLOW, stroke_width=3,
            )
            if first_wave is None:
                first_wave = wave
                self.play(Create(wave), run_time=0.6)
            else:
                self.play(Transform(first_wave, wave), run_time=0.6)
            # 0.6s × 4 = 2.4s
        # 77.4s

        self.play(FadeOut(f_axes, first_wave), run_time=0.4)
        # 77.8s

        # Series convergence — Σ
        sigma = Text("Σ 1/n² = π²/6", color=YELLOW, font_size=64)
        sigma.move_to(ORIGIN)
        self.play(FadeIn(sigma, scale=1.4), run_time=0.6)
        for _ in range(3):
            self.play(sigma.animate.set_color(BLUE), run_time=0.2)
            self.play(sigma.animate.set_color(YELLOW), run_time=0.2)
        # 79.6s
        self.play(FadeOut(sigma), run_time=0.4)
        # 80.0s

        # Golden ratio flash
        phi = Text("φ = (1 + √5) / 2 ≈ 1.618…", color=BLUE, font_size=52)
        phi.move_to(ORIGIN)
        self.play(FadeIn(phi, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(phi), run_time=0.4)
        # 81.7s

        # Fibonacci spiral — quick
        fib_circles = VGroup()
        a, b = 1.0, 1.0
        x, y = 0.0, 0.0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(7):
            dx, dy = directions[i % 4]
            circ = Circle(
                radius=b / 2,
                color=YELLOW if i % 2 == 0 else BLUE,
                stroke_width=2,
            )
            circ.move_to(np.array([x + dx * b / 2, y + dy * b / 2, 0.0]))
            fib_circles.add(circ)
            x += dx * b
            y += dy * b
            a, b = b, a + b

        fib_circles.scale(0.6).move_to(ORIGIN)
        self.play(
            LaggedStart(*[Create(c) for c in fib_circles], lag_ratio=0.1),
            run_time=1.0,
        )
        # 82.7s
        self.play(FadeOut(fib_circles), run_time=0.3)
        # 83.0s

        # ═════════════════════════════════════════════════
        # ACT 9 · 83.0–88.0s · SYMMETRY finale
        # ═════════════════════════════════════════════════
        final = Text("SYMMETRY", color=YELLOW, font_size=140)
        final.move_to(ORIGIN)

        self.play(FadeIn(final, scale=1.6), run_time=0.8)
        # 83.8s

        for _ in range(4):
            self.play(final.animate.set_color(BLUE).scale(1.06), run_time=0.2)
            self.play(final.animate.set_color(YELLOW).scale(1 / 1.06), run_time=0.2)
        # 85.4s

        self.wait(2.0)
        # 88.0s