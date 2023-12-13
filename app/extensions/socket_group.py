from app.extensions.base_class import Extension
from app import categories


class SocketGroup(Extension):
    def __init__(
        self,
        *,
        sockets: str,
        operator: categories.OPERATOR,
    ):
        super().__init__()
        self.sockets = sockets
        self.operator = operator

    def __str__(self):
        return f"""
            SocketGroup {self.operator.value} {self.sockets}
        """
