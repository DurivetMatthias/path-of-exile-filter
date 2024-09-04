from app.conditions.base_class import Extension
from app.categories import OPERATOR


class BaseType(Extension):
    def __init__(
        self,
        base_type: str,
        operator: OPERATOR = OPERATOR.EXACT,
    ):
        super().__init__()
        self.base_type = base_type
        self.operator = operator

    def __str__(self):
        return f"""
            BaseType {self.operator.value} "{self.base_type}"
        """
