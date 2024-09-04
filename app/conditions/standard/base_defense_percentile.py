from app.conditions.base_class import Extension
from app.categories import OPERATOR


class BaseDefensePercentile(Extension):
    def __init__(
        self,
        percentile: int,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        super().__init__()
        self.percentile = percentile
        self.operator = operator

    def __str__(self):
        return f"""
            BaseDefencePercentile {self.operator.value} {self.percentile}
        """
