from app.extensions.base_class import Extension
from app import categories


class Icon(Extension):
    def __init__(
        self,
        *,
        color: categories.COLOR,
        shape: categories.SHAPE,
        size: categories.SIZE,
    ):
        super().__init__()
        self.color = color
        self.shape = shape
        self.size = size

    def __str__(self):
        return f"""
            MinimapIcon {self.size.value} {self.color.value} {self.shape.value}
        """
