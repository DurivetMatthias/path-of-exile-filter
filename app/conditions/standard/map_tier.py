from app.conditions.base_class import Extension
from app.categories import OPERATOR


class MapTier(Extension):
    def __init__(
        self,
        tier: int,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.tier = tier
        self.operator = operator

    def __str__(self):
        return f"""
            MapTier {self.operator.value} {self.tier}
        """
