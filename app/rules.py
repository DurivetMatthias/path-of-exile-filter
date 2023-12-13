from typing import Sequence

from app.extensions import Extension


class Rule:
    def __init__(
        self,
        *,
        instruction: Extension,
        extensions: Sequence[Extension],
    ):
        self.instruction = instruction
        self.extensions = extensions
