from app.conditions.base_class import Extension
from app.operators import *


class ClassName(Extension):
    def __init__(
        self,
        class_name: str,
        operator: str = EXACT,
    ):
        super().__init__()
        self.class_name = class_name
        self.operator = operator

    def __str__(self):
        return f"""
            Class {self.operator} "{self.class_name}"
        """
