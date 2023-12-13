from app.extensions.base_class import Extension


class BaseType(Extension):
    def __init__(self, *, base_type: str, fuzzy: bool = False):
        super().__init__()
        self.fuzzy = fuzzy
        self.base_type = base_type

    def __str__(self):
        operation = "==" if not self.fuzzy else "="
        return f"""
            BaseType {operation} "{self.base_type}"
        """
