from app.conditions.base_class import Extension
from app.categories import RGB


class Border(Extension):
    def __init__(
        self,
        rgb: RGB,
    ):
        super().__init__()
        self.rgb = rgb

    def __str__(self):
        return f"""
            SetBorderColor {self.rgb.value}
        """
