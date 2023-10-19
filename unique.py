from rule import Rule
import rarity_options


class Unique(Rule):
    def label(self) -> str:
        return """
            SetFontSize 45
            SetTextColor 175 96 37
            SetBackgroundColor 0 0 0
            SetBorderColor 175 96 37
        """

    def sound(self) -> str:
        return """
            DisableDropSound
            CustomAlertSound "filter-sounds/lily-pekabo.mp3"
        """

    def icon(self) -> str:
        return "MinimapIcon 0 Orange Star"

    def filter(self):
        return f"""
            BaseType == "{self.name}"
            Rarity Unique
        """


class UniqueClass(Unique):
    def filter(self):
        return f"""
            Class == "{self.name}"
            Rarity Unique
        """


rules = [
    Unique(
        name="Leather Belt",
        rarity=rarity_options.LEGENDARY,
    ),
    Unique(
        name="Wyrmscale Boots",
        rarity=rarity_options.LEGENDARY,
    ),
    Unique(
        name="Onyx Amulet",
        rarity=rarity_options.LEGENDARY,
    ),
    UniqueClass(
        name="Jewel",
        rarity=rarity_options.LEGENDARY,
    ),
    UniqueClass(
        name="Map",
        rarity=rarity_options.LEGENDARY,
    ),
]
