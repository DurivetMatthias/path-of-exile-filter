from app.conditions.base_class import Extension
from app.categories import OPERATOR


class AreaLevel(Extension):
    def __init__(
        self,
        area_level: int,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        super().__init__()
        self.area_level = area_level
        self.operator = operator

    def __str__(self):
        return f"""
            AreaLevel {self.operator.value} {self.area_level}
        """
