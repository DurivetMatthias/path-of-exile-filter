from app.extensions.base_class import Extension
from app import categories


class BaseDefencePercentile(Extension):
    def __init__(
        self,
        *,
        percentile: int,
        operator: categories.OPERATOR,
    ):
        super().__init__()
        self.percentile = percentile
        self.operator = operator

    def __str__(self):
        return f"""
            BaseDefencePercentile {self.operator.value} {self.percentile}
        """
