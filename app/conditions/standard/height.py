from app.conditions.base_class import Extension
from app.categories import OPERATOR


class Height(Extension):
    def __init__(
        self,
        height,
        operator: OPERATOR = OPERATOR.EXACT,
    ):
        super().__init__()
        self.height = height
        self.operator = operator

    def __str__(self):
        return f"""
            Height {self.operator.value} {self.height}
        """
