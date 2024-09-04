from app.conditions.base_class import Extension
from app.categories import OPERATOR


class Quality(Extension):
    def __init__(
        self,
        quality: int,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        super().__init__()
        self.quality = quality
        self.operator = operator

    def __str__(self):
        return f"""
            Quality {self.operator.value} {self.quality}
        """
