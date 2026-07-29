from app.conditions import Condition


class Block:
    __slots__ = ["conditions", "instruction"]


class Show(Block):
    def __init__(
        self,
        conditions: list[Condition],
    ):
        self.instruction = "Show"
        self.conditions = conditions


class Hide(Block):
    def __init__(
        self,
        conditions: list[Condition],
    ):
        self.instruction = "Hide"
        self.conditions = conditions
