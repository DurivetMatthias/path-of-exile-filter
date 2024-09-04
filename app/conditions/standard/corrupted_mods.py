from app.conditions.base_class import Extension
from app.categories import OPERATOR


class CorruptedMods(Extension):
    def __init__(
        self,
        amount: int = 1,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.amount = amount
        self.operator = operator

    def __str__(self):
        return f"""
            CorruptedMods {self.operator.value} {self.amount}
        """
