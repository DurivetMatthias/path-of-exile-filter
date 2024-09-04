from app.conditions.base_class import Extension
from app.categories import OPERATOR


class Sockets(Extension):
    def __init__(
        self,
        sockets: str,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        super().__init__()
        self.sockets = sockets
        self.operator = operator

    def __str__(self):
        return f"""
            Sockets {self.operator.value} {self.sockets}
        """
