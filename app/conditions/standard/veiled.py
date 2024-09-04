from app.conditions.base_class import Extension


class VeiledPrefix(Extension):
    def __str__(self):
        return """
            HasExplicitMod "Veiled"
        """


class VeiledSuffix(Extension):
    def __str__(self):
        return """
            HasExplicitMod "of the Veil"
        """
