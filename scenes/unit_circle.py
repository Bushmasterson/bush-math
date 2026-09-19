# pyright: reportWildcardImportFromLibrary=false

from manim import *
import numpy as np

from _style import StyledScene, MAIN_YELLOW, MAIN_BLUE


class UnitCircleSine(StyledScene):
    """
    A point moves along the unit circle; on the right, the sine wave is drawn
    in real time. Key angles (pi/2, pi, 3pi/2) are marked with short pauses.
    No LaTeX required — all labels use Text + Unicode.
    """

    CIRCLE_RADIUS = 1.5
    CIRCLE_CENTER = LEFT * 4
    THETA_MAX = 4 * PI
    RUN_TIME = 12

    def construct(self) -> None:
        YELLOW = MAIN_YELLOW
        BLUE = MAIN_BLUE
        GREY = ManimColor("#555555")
        FAINT = ManimColor("#2A2A2A")

        # ── 1. Title ───────────────────────────────────────
        title = Text("sin(θ)", color=YELLOW, font_size=56)
        title.to_corner(UL, buff=0.5)
        self.play(Write(title), run_time=0.8)
        self.wait(0.2)

        # ── 2. Circle ──────────────────────────────────────
        circle = Circle(radius=self.CIRCLE_RADIUS, color=BLUE, stroke_width=3)
        circle.move_to(self.CIRCLE_CENTER)
        self.play(Create(circle), run_time=1.0)

        # ── 3. Axes (no auto-numbers — labels added manually) ──
        axes = Axes(
            x_range=[0, self.THETA_MAX, PI / 2],
            y_range=[-1.5, 1.5, 1],
            x_length=8,
            y_length=3,
            axis_config={
                "include_tip": False,
                "stroke_color": BLUE,
                "stroke_width": 3,
                "include_numbers": False,
            },
        ).move_to(RIGHT * 1.5)

        # Manual x-labels: π, 2π, 3π, 4π
        x_labels = VGroup()
        for value, label in [
            (PI, "π"),
            (2 * PI, "2π"),
            (3 * PI, "3π"),
            (4 * PI, "4π"),
        ]:
            t = Text(label, font_size=28, color=BLUE)
            t.next_to(axes.c2p(value, 0), DOWN, buff=0.15)
            x_labels.add(t)

        # Manual y-labels: −1, 1
        y_labels = VGroup()
        for value, label in [(-1, "−1"), (1, "1")]:
            t = Text(label, font_size=28, color=BLUE)
            t.next_to(axes.c2p(0, value), LEFT, buff=0.15)
            y_labels.add(t)

        x_label = Text("θ", font_size=36, color=BLUE)
        x_label.next_to(axes.c2p(self.THETA_MAX, 0), RIGHT, buff=0.15)

        y_label = Text("sin(θ)", font_size=30, color=BLUE)
        y_label.next_to(axes.c2p(0, 1.5), UP, buff=0.1)

        self.play(Create(axes), run_time=1.0)
        self.play(
            FadeIn(x_labels),
            FadeIn(y_labels),
            FadeIn(x_label),
            FadeIn(y_label),
            run_time=0.5,
        )
        self.wait(0.2)

        # ── 4. ValueTracker ────────────────────────────────
        theta = ValueTracker(0.0)

        # ── 5. Dynamic elements ────────────────────────────
        def circle_point() -> np.ndarray:
            a = theta.get_value()
            return self.CIRCLE_CENTER + self.CIRCLE_RADIUS * np.array(
                [np.cos(a), np.sin(a), 0.0]
            )

        def sine_point() -> np.ndarray:
            return axes.c2p(theta.get_value(), np.sin(theta.get_value()))

        def make_radius() -> Line:
            return Line(self.CIRCLE_CENTER, circle_point(), color=YELLOW, stroke_width=4)

        def make_arc() -> Arc:
            angle = min(theta.get_value(), 2 * PI)
            return Arc(
                radius=0.55,
                start_angle=0,
                angle=angle,
                arc_center=self.CIRCLE_CENTER,
                color=YELLOW,
                stroke_width=3,
            )

        def make_theta_label() -> Text:
            angle = theta.get_value()
            offset = 0.85
            pos = self.CIRCLE_CENTER + offset * np.array(
                [np.cos(angle / 2), np.sin(angle / 2), 0.0]
            )
            return Text("θ", font_size=32, color=YELLOW).move_to(pos)

        def make_v_line() -> DashedLine:
            p = circle_point()
            return DashedLine(
                start=p,
                end=[p[0], self.CIRCLE_CENTER[1], 0],
                color=GREY,
                stroke_width=2,
                dash_length=0.06,
            )

        def make_h_line() -> DashedLine:
            p = circle_point()
            return DashedLine(
                start=p,
                end=[self.CIRCLE_CENTER[0], p[1], 0],
                color=GREY,
                stroke_width=2,
                dash_length=0.06,
            )

        def make_connector() -> DashedLine:
            return DashedLine(
                start=circle_point(),
                end=sine_point(),
                color=FAINT,
                stroke_width=1.5,
                dash_length=0.1,
            )

        def make_curve() -> ParametricFunction:
            return axes.plot(
                np.sin,
                x_range=[0, max(theta.get_value(), 1e-3)],
                color=YELLOW,
                stroke_width=4,
            )

        def make_glow(point: np.ndarray, radius: float) -> Dot:
            return Dot(point, color=YELLOW, radius=radius, fill_opacity=0.2)

        # ── 6. always_redraw ──────────────────────────────
        curve = always_redraw(make_curve)
        connector = always_redraw(make_connector)
        v_line = always_redraw(make_v_line)
        h_line = always_redraw(make_h_line)
        arc = always_redraw(make_arc)
        theta_label = always_redraw(make_theta_label)
        radius = always_redraw(make_radius)

        dot_glow = always_redraw(lambda: make_glow(circle_point(), 0.22))
        dot = always_redraw(lambda: Dot(circle_point(), color=YELLOW, radius=0.09))

        sine_dot_glow = always_redraw(lambda: make_glow(sine_point(), 0.22))
        sine_dot = always_redraw(lambda: Dot(sine_point(), color=YELLOW, radius=0.09))

        # ── 7. Initial appearance ─────────────────────────
        self.play(FadeIn(arc), FadeIn(theta_label), FadeIn(radius), run_time=0.6)
        self.add(v_line, h_line, connector, curve)
        self.add(dot_glow, dot, sine_dot_glow, sine_dot)

        # ── 8. Movement in quarters with pauses ───────────
        quarter = PI / 2
        segment_time = self.RUN_TIME / 4

        for i, target in enumerate([quarter, 2 * quarter, 3 * quarter, 4 * quarter]):
            self.play(
                theta.animate.set_value(target),
                run_time=segment_time,
                rate_func=smooth,
            )
            if i < 3:
                self.wait(0.4)

        self.wait(2)