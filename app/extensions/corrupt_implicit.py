from app.extensions.base_class import Extension


class CorruptedImplicit(Extension):
    def __str__(self):
        return """
            CorruptedMods > 0
        """
