from app.extensions.base_class import Extension
from app import categories


class Beam(Extension):
    def __init__(self, *, color: categories.COLOR):
        super().__init__()
        self.color = color

    def __str__(self):
        return f"""
            PlayEffect {self.color.value}
        """
