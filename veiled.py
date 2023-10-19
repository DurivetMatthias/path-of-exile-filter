from rule import Rule
import rarity_options


class VeiledStyle(Rule):
    def label(self) -> str:
        """Black text on a yellow background"""
        return """
            SetFontSize 45
            SetTextColor 0 0 0
            SetBackgroundColor 255 255 0
            SetBorderColor 255 255 0
        """

    def sound(self) -> str:
        return """
            DisableDropSound
            CustomAlertSound "filter-sounds/lily-bam.mp3"
        """

    def icon(self) -> str:
        return "MinimapIcon 0 Yellow Triangle"


class VeiledPrefix(VeiledStyle):
    def filter(self):
        return f"""
            HasExplicitMod "Veiled"
            Class "{self.name}"
        """


class VeiledSuffix(VeiledStyle):
    def filter(self):
        return f"""
            HasExplicitMod "of the Veil"
            Class "{self.name}"
        """


life_regeneration = ["Flasks"]
fire_damage = ["Wands", "Daggers", "Sceptres"]
plus_gems = ["Helmets", "Gloves"]
prefix_classes = [
    *life_regeneration,
    *fire_damage,
    *plus_gems,
]
dual_resistance = ["Body Armours", "Gloves", "Boots", "Helmets"]
fire_multiplier = ["Wands", "Daggers", "Sceptres"]
suffix_classes = [
    *dual_resistance,
    *fire_multiplier,
]

rules = [
    *[
        VeiledPrefix(
            name=class_name,
            rarity=rarity_options.EPIC,
        )
        for class_name in prefix_classes
    ],
    *[
        VeiledSuffix(
            name=class_name,
            rarity=rarity_options.EPIC,
        )
        for class_name in suffix_classes
    ],
]
