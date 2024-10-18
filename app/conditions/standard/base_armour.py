from app.conditions.base_class import Extension
from app.categories import OPERATOR


class BaseArmour(Extension):
    def __init__(
        self,
        value: int,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        super().__init__()
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            BaseArmour {self.operator.value} {self.value}
        """