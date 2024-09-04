from app.conditions.base_class import Extension
from app.categories import OPERATOR


class SocketGroup(Extension):
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
            SocketGroup {self.operator.value} {self.sockets}
        """
