from abc import ABC
from app.extention import Extension


class Rule(ABC):
    __slots__ = ["instruction", "extensions"]


class Show(Rule):
    def __init__(
        self,
        extensions: list[Extension],
    ):
        self.instruction = "Show"
        self.extensions = extensions


class Hide(Rule):
    def __init__(
        self,
        extensions: list[Extension],
    ):
        self.instruction = "Hide"
        self.extensions = extensions
