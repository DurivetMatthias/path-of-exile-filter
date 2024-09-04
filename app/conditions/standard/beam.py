from app.conditions.base_class import Extension
from app.categories import COLOR


class Beam(Extension):
    def __init__(
        self,
        color: COLOR,
    ):
        super().__init__()
        self.color = color

    def __str__(self):
        return f"""
            PlayEffect {self.color.value}
        """
