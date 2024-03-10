from app.extensions.base_class import Extension


class MultiClass(Extension):
    def __init__(self, *, class_names: list[str], fuzzy: bool = False):
        super().__init__()
        self.fuzzy = fuzzy
        self.class_names = class_names

    def __str__(self):
        operation = "==" if not self.fuzzy else "="
        class_name_string = " ".join(f'"{name}"' for name in self.class_names)
        return f"""
            Class {operation} {class_name_string}
        """
