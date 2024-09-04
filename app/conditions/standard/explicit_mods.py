from app.conditions.base_class import Extension
from app.categories import OPERATOR


class ExplicitMods(Extension):
    def __init__(
        self,
        amount: int = 1,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.amount = amount
        self.operator = operator

    def __str__(self):
        return f"""
            HasExplicitMod {self.operator.value} {self.amount}
        """
