from app.conditions.base_class import Extension


class MultiBaseType(Extension):
    def __init__(
        self,
        base_types: list[str],
        fuzzy: bool = False,
    ):
        super().__init__()
        self.fuzzy = fuzzy
        self.base_types = base_types

    def __str__(self):
        if not self.base_types:
            print("MultiBaseType got an empty list")
            exit(1)
        operation = "==" if not self.fuzzy else "="
        class_name_string = " ".join(f'"{name}"' for name in self.base_types)
        return f"""
            BaseType {operation} {class_name_string}
        """
