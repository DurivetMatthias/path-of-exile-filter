from rule import Rule
import rarity_options


class GemStyle(Rule):
    def label(self) -> str:
        return """
            SetFontSize 45
            SetTextColor 0 0 0
            SetBackgroundColor 0 150 0
            SetBorderColor 0 150 0
        """

    def sound(self) -> str:
        return """
            DisableDropSound
            CustomAlertSound "filter-sounds/lily-aah.mp3"
        """

    def filter(self):
        return f"""
            BaseType "{self.name}"
        """


class QualityGem(GemStyle):
    def __init__(self, rarity: str) -> None:
        super().__init__("", rarity, False)

    def filter(self):
        return """
            GemQualityType "Superior" "Divergent" "Anomalous" "Phantasmal"
            Quality > 0
            Class "Gems"
        """

    def sound(self) -> str:
        return """
            DisableDropSound
        """


class LeveledGem(QualityGem):
    def filter(self):
        return """
            GemLevel >= 20
            Class "Gems"
        """


class HideGems(Rule):
    def __init__(self) -> None:
        super().__init__("", rarity_options.COMMON, True)

    def filter(self):
        return """
            Class "Gems"
        """


rules = [
    GemStyle(
        name="Empower",
        rarity=rarity_options.LEGENDARY,
    ),
    GemStyle(
        name="Enhance",
        rarity=rarity_options.LEGENDARY,
    ),
    GemStyle(
        name="Enlighten",
        rarity=rarity_options.LEGENDARY,
    ),
    GemStyle(
        name="Awakened",
        rarity=rarity_options.LEGENDARY,
    ),
    GemStyle(
        name="Prime Regrading Lens",
        rarity=rarity_options.LEGENDARY,
    ),
    GemStyle(
        name="Secondary Regrading Lens",
        rarity=rarity_options.LEGENDARY,
    ),
    LeveledGem(rarity=rarity_options.COMMON),
    QualityGem(rarity=rarity_options.COMMON),
    HideGems(),
]
