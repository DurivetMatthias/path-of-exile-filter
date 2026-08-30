class Markup(str):
    def __str__(self):
        raise NotImplementedError


class Bold(Markup):
    def __init__(
        self,
        text: str,
    ):
        self.text = text

    def __str__(self):
        return f"""
            <bold>{{ {self.text} }}
        """
