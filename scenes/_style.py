# pyright: reportWildcardImportFromLibrary=false

from manim import *
from manim.utils.color import ManimColor

# ── Палитра bush-math ──────────────────────────────────
# Фон: чёрный (задаётся в manim.cfg). Акценты: жёлтый и синий.

BG_COLOR = ManimColor("#000000")
MAIN_YELLOW = ManimColor("#F7D96F")
MAIN_BLUE = ManimColor("#58C4DD")


class StyledScene(Scene):
    """Базовая сцена с палитрой bush-math. Фон берётся из manim.cfg."""
    pass