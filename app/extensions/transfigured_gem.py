from app.extensions.base_class import Extension


class TransfiguredGem(Extension):
    def __init__(
        self,
        *,
        transfigured: bool = True,
    ):
        super().__init__()
        self.transfigured = transfigured

    def __str__(self):
        return f"""
            TransfiguredGem {self.transfigured}
        """
