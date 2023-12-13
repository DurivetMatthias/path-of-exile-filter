from app.extensions.base_class import Extension
from app import categories


class Quality(Extension):
    def __init__(
        self,
        *,
        quality: int,
        operator: categories.OPERATOR,
    ):
        super().__init__()
        self.quality = quality
        self.operator = operator

    def __str__(self):
        return f"""
            Quality {self.operator.value} {self.quality}
        """
