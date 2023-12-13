from app.extensions.base_class import Extension
from app import categories


class AreaLevel(Extension):
    def __init__(
        self,
        *,
        area_level: int,
        operator: categories.OPERATOR,
    ):
        super().__init__()
        self.area_level = area_level
        self.operator = operator

    def __str__(self):
        return f"""
            AreaLevel {self.operator.value} {self.area_level}
        """
