from app.extensions.base_class import Extension
from app import categories


class GemLevel(Extension):
    def __init__(
        self,
        *,
        gem_level: int,
        operator: categories.OPERATOR,
    ):
        super().__init__()
        self.gem_level = gem_level
        self.operator = operator

    def __str__(self):
        return f"""
            GemLevel {self.operator.value} {self.gem_level}
        """
