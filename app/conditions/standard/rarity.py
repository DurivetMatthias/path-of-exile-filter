from app.conditions.base_class import Extension
from app.categories import OPERATOR, RARITY


class Rarity(Extension):
    def __init__(
        self,
        rarity: RARITY,
        operator: OPERATOR = OPERATOR.EXACT,
    ):
        super().__init__()
        self.rarity = rarity
        self.operator = operator

    def __str__(self):
        return f"""
           Rarity {self.operator.value} {self.rarity.value}
        """
