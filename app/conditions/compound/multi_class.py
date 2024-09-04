from app.conditions.base_class import Extension
from app.categories import OPERATOR


class MultiClass(Extension):
    def __init__(
        self,
        class_names: list[str],
        operator: OPERATOR = OPERATOR.EXACT,
    ):
        super().__init__()
        self.class_names = class_names
        self.operator = operator

    def __str__(self):
        if not self.class_names:
            print("MultiClass got an empty list")
            exit(1)
        class_name_string = " ".join(f'"{name}"' for name in self.class_names)
        return f"""
            Class {self.operator.value} {class_name_string}
        """
