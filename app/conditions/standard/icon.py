from app.conditions.base_class import Extension
from app.categories import COLOR, SHAPE, SIZE


class Icon(Extension):
    def __init__(
        self,
        size: SIZE,
        color: COLOR,
        shape: SHAPE,
    ):
        super().__init__()
        self.size = size
        self.color = color
        self.shape = shape

    def __str__(self):
        return f"""
            MinimapIcon {self.size.value} {self.color.value} {self.shape.value}
        """
