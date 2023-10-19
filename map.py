from rule import Rule
import rarity_options


class MapRule(Rule):
    def __init__(self) -> None:
        super().__init__("", rarity_options.EPIC, False)

    def label(self) -> str:
        """White text on red background"""
        return """
            SetFontSize 45
            SetTextColor 255 255 255
            SetBackgroundColor 150 0 0
            SetBorderColor 150 0 0
        """

    def sound(self) -> str:
        return """
            DisableDropSound
            CustomAlertSound "filter-sounds/lily-aah.mp3"
        """

    def icon(self) -> str:
        return """
            MinimapIcon 0 Red Circle
        """

    def filter(self):
        return """
            Class == "Maps"
        """


rules = [MapRule()]
