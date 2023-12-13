from app.extensions.base_class import Extension
from app import categories


class Rarity(Extension):
    def __init__(
        self,
        *,
        rarity: categories.RARITY,
        operator: categories.OPERATOR,
    ):
        super().__init__()
        self.rarity = rarity
        self.operator = operator

    def __str__(self):
        return f"""
           Rarity {self.operator.value} {self.rarity.value}
        """
