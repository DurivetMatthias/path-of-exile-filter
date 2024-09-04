from app.conditions.base_class import Extension
from app.categories import OPERATOR


class StackSize(Extension):
    def __init__(
        self,
        stack_size: int,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        super().__init__()
        self.stack_size = stack_size
        self.operator = operator

    def __str__(self):
        return f"""
            StackSize {self.operator.value} {self.stack_size}
        """
