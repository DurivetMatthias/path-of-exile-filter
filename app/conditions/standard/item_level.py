from app.conditions.base_class import Extension
from app.categories import OPERATOR


class ItemLevel(Extension):
    def __init__(
        self,
        item_level: int,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        super().__init__()
        self.item_level = item_level
        self.operator = operator

    def __str__(self):
        return f"""
            ItemLevel {self.operator.value} {self.item_level}
        """
