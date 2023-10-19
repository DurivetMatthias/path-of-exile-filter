from rule import Rule
import rarity_options


class HeistItem(Rule):
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
            CustomAlertSound "filter-sounds/lily-bam.mp3"
        """

    def icon(self) -> str:
        return "MinimapIcon 0 Red UpsideDownHouse"


class HeistClass(HeistItem):
    def filter(self):
        return f"""
            Class "{self.name}"
        """


rules = [
    HeistItem(
        name="Rogue's Marker",
        rarity=rarity_options.COMMON,
    ),
    HeistItem(
        name="Tempering Orb",
        rarity=rarity_options.LEGENDARY,
    ),
    HeistItem(
        name="Tailoring Orb",
        rarity=rarity_options.LEGENDARY,
    ),
    HeistClass(
        name="Blueprint",
        rarity=rarity_options.LEGENDARY,
    ),
    HeistClass(
        name="Contract",
        rarity=rarity_options.EPIC,
    ),
    HeistClass(
        name="Heist Target",
        rarity=rarity_options.COMMON,
    ),
    HeistClass(
        name="Heist Brooch",
        rarity=rarity_options.EPIC,
    ),
    HeistClass(
        name="Heist Cloak",
        rarity=rarity_options.EPIC,
    ),
    HeistClass(
        name="Heist Tool",
        rarity=rarity_options.EPIC,
    ),
    HeistClass(
        name="Heist Gear",
        rarity=rarity_options.EPIC,
    ),
    HeistClass(
        name="Trinket",
        rarity=rarity_options.LEGENDARY,
    ),
]
