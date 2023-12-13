from app import categories
from app.extensions.base_class import Extension


class FontSize(Extension):
    def __init__(
        self,
        *,
        size: categories.FONT_SIZE,
    ):
        self.size = size

    def __str__(self):
        return f"""
            SetFontSize {self.size.value}
        """
