from app.extensions.base_class import Extension


class ClassName(Extension):
    def __init__(self, *, class_name: str, fuzzy: bool = False):
        super().__init__()
        self.fuzzy = fuzzy
        self.class_name = class_name

    def __str__(self):
        operation = "==" if not self.fuzzy else "="
        return f"""
            Class {operation} "{self.class_name}"
        """
