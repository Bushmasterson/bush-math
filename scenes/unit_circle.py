# pyright: reportWildcardImportFromLibrary=false

from manim import *
import numpy as np

from _style import StyledScene, MAIN_YELLOW, MAIN_BLUE


class UnitCircleSine(StyledScene):

    CIRCLE_RADIUS = 1.5
    CIRCLE_CENTER = LEFT * 4
    THETA_MAX = 4 * PI
    RUN_TIME = 8

    def construct(self) -> None:
        circle = Circle(radius=self.CIRCLE_RADIUS, color=MAIN_BLUE).move_to(self.CIRCLE_CENTER)
        axes = Axes(
            x_range=[0, self.THETA_MAX, PI],
            y_range=[-1.5, 1.5, 1],
            x_length=8,
            y_length=3,
            axis_config={"include_tip": False},
        ).move_to(RIGHT * 1.5)

        theta = ValueTracker(0.0)

        def circle_point() -> np.ndarray:
            angle = theta.get_value()
            return self.CIRCLE_CENTER + self.CIRCLE_RADIUS * np.array(
                [np.cos(angle), np.sin(angle), 0.0]
            )

        dot = always_redraw(lambda: Dot(circle_point(), color=MAIN_YELLOW))
        radius = always_redraw(lambda: Line(self.CIRCLE_CENTER, circle_point(), color=MAIN_YELLOW))
        sine_dot = always_redraw(
            lambda: Dot(axes.c2p(theta.get_value(), np.sin(theta.get_value())), color=MAIN_YELLOW)
        )
        sine_curve = always_redraw(
            lambda: axes.plot(np.sin, x_range=[0, max(theta.get_value(), 1e-3)], color=MAIN_YELLOW)
        )

        self.play(Create(circle), Create(axes), run_time=1.5, rate_func=smooth)
        self.add(dot, radius, sine_dot, sine_curve)
        self.play(
            theta.animate.set_value(self.THETA_MAX),
            run_time=self.RUN_TIME,
            rate_func=linear,
        )
        self.wait()