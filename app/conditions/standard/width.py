from app.conditions.base_class import Extension
from app.categories import OPERATOR


class Width(Extension):
    def __init__(
        self,
        width,
        operator: OPERATOR = OPERATOR.EXACT,
    ):
        super().__init__()
        self.width = width
        self.operator = operator

    def __str__(self):
        return f"""
            Width {self.operator.value} {self.width}
        """
