from app.extensions.base_class import Extension
from app import categories


class Border(Extension):
    def __init__(self, *, rgb: categories.RGB):
        super().__init__()
        self.rgb = rgb

    def __str__(self):
        return f"""
            SetBorderColor {self.rgb.value}
        """
