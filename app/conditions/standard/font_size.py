from app.conditions.base_class import Extension
from app.categories import FONT_SIZE


class FontSize(Extension):
    def __init__(
        self,
        size: FONT_SIZE,
    ):
        self.size = size

    def __str__(self):
        return f"""
            SetFontSize {self.size.value}
        """
