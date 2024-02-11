from typing import List

from app.extensions import Extension


class Rule:

    def __init__(
        self,
        *,
        instruction: Extension,
        extensions: List[Extension],
    ):
        self.instruction = instruction
        self.extensions = extensions
