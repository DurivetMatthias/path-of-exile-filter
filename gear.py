from typing import Optional

import rarity_options
import strictness_options

from rule import Rule


class Gear(Rule):
    def __init__(self, level: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.level = level

    def label(self) -> str:
        """Gear is displayed as white text on a pink background"""
        return """
            SetFontSize 45
            SetTextColor 255 255 255
            SetBackgroundColor 255 100 200
            SetBorderColor 255 100 200
        """

    def sound(self) -> str:
        if self.rarity == rarity_options.COMMON:
            return """
                DisableDropSound
            """
        if self.rarity == rarity_options.RARE:
            return """
                DisableDropSound
                CustomAlertSound "filter-sounds/lily-bing-bing.mp3"
            """
        if self.rarity == rarity_options.EPIC:
            return """
                DisableDropSound
                CustomAlertSound "filter-sounds/lily-bam.mp3"
            """
        if self.rarity == rarity_options.LEGENDARY:
            return """
                DisableDropSound
                CustomAlertSound "filter-sounds/lily-ooh.mp3"
            """
        return "None"

    def icon(self) -> str:
        if self.rarity == rarity_options.COMMON:
            return "MinimapIcon 2 White Kite"
        if self.rarity == rarity_options.RARE:
            return "MinimapIcon 2 Blue Kite"
        if self.rarity == rarity_options.EPIC:
            return "MinimapIcon 1 Purple Kite"
        if self.rarity == rarity_options.LEGENDARY:
            return "MinimapIcon 0 Orange Kite"
        return "-1"

    def filter(self):
        if self.level is not None:
            return f"""
                    BaseType == "{self.name}"
                    ItemLevel {self.level}
            """

        return super().filter()


hide_overlapping = [
    Rule(name="Oiled Vest", rarity=rarity_options.COMMON, hide=True),
    Rule(name="Oiled Coat", rarity=rarity_options.COMMON, hide=True),
    Rule(name="Runic Crest", rarity=rarity_options.COMMON, hide=True),
    Rule(name="Fossilised Spirit Shield", rarity=rarity_options.COMMON, hide=True),
    Rule(name="Crested Tower Shield", rarity=rarity_options.COMMON, hide=True),
    Rule(name="Splintered Tower Shield", rarity=rarity_options.COMMON, hide=True),
    Rule(name="Serrated Foil", rarity=rarity_options.COMMON, hide=True),
    Rule(name="Spiraled Foil", rarity=rarity_options.COMMON, hide=True),
]

life_flasks = ["Divine Life Flask"]

utility_flask = [
    Gear(
        name="Quicksilver Flask",
        rarity=rarity_options.LEGENDARY,
        level=">= 85",
    ),
    Gear(
        name="Quicksilver Flask",
        rarity=rarity_options.EPIC,
    ),
    Gear(
        name="Granite Flask",
        rarity=rarity_options.LEGENDARY,
        level=">= 85",
    ),
    Gear(
        name="Granite Flask",
        rarity=rarity_options.EPIC,
    ),
    Gear(
        name="Ruby Flask",
        rarity=rarity_options.LEGENDARY,
        level=">= 85",
    ),
    Gear(
        name="Ruby Flask",
        rarity=rarity_options.EPIC,
    ),
    Gear(
        name="Quartz Flask",
        rarity=rarity_options.LEGENDARY,
        level=">= 85",
    ),
    Gear(
        name="Quartz Flask",
        rarity=rarity_options.EPIC,
    ),
]

armour = [
    Gear(
        name="Glorious Plate",
        rarity=rarity_options.LEGENDARY,
        level=">= 86",
    ),
    Gear(
        name="Glorious Plate",
        rarity=rarity_options.EPIC,
    ),
    Gear(
        name="Stygian Vise",
        rarity=rarity_options.LEGENDARY,
        level=">= 86",
    ),
    Gear(
        name="Stygian Vise",
        rarity=rarity_options.EPIC,
    ),
    Gear(
        name="Titan Gauntlets",
        rarity=rarity_options.LEGENDARY,
        level=">= 85",
    ),
    Gear(
        name="Titan Gauntlets",
        rarity=rarity_options.EPIC,
    ),
    Gear(
        name="Titan Greaves",
        rarity=rarity_options.LEGENDARY,
        level=">= 85",
    ),
    Gear(
        name="Titan Greaves",
        rarity=rarity_options.EPIC,
    ),
    Gear(
        name="Royal Burgonet",
        rarity=rarity_options.LEGENDARY,
        level=">= 85",
    ),
    Gear(
        name="Royal Burgonet",
        rarity=rarity_options.EPIC,
    ),
]

jewelry = [
    Gear(
        name="Turquoise Amulet",
        rarity=rarity_options.LEGENDARY,
        level=">= 85",
    ),
    Gear(
        name="Turquoise Amulet",
        rarity=rarity_options.EPIC,
    ),
    Gear(
        name="Vermillion Ring",
        rarity=rarity_options.LEGENDARY,
        level=">= 84",
    ),
    Gear(
        name="Vermillion Ring",
        rarity=rarity_options.EPIC,
    ),
    Gear(
        name="Amethyst Ring",
        rarity=rarity_options.LEGENDARY,
        level=">= 84",
    ),
    Gear(
        name="Amethyst Ring",
        rarity=rarity_options.EPIC,
    ),
]

weapon = [
    Gear(
        name="Void Sceptre",
        rarity=rarity_options.LEGENDARY,
        level=">= 84",
    ),
    Gear(
        name="Void Sceptre",
        rarity=rarity_options.EPIC,
    ),
]

jewel = [
    Gear(
        name="Crimson Jewel",
        rarity=rarity_options.RARE,
    ),
    Gear(
        name="Viridian Jewel",
        rarity=rarity_options.RARE,
    ),
    Gear(
        name="Cobalt Jewel",
        rarity=rarity_options.RARE,
    ),
    Gear(
        name="Small Cluster Jewel",
        rarity=rarity_options.RARE,
    ),
    Gear(
        name="Medium Cluster Jewel",
        rarity=rarity_options.RARE,
    ),
    Gear(
        name="Large Cluster Jewel",
        rarity=rarity_options.RARE,
    ),
]

rules = [
    *hide_overlapping,
    *[
        *[
            Gear(
                name=item_name,
                rarity=rarity_options.RARE,
                level=">= 80",
                strictness=strictness_options.LESS_STRICT,
            )
            for item_name in life_flasks
        ],
        *[
            Gear(
                name=item_name,
                rarity=rarity_options.COMMON,
                strictness=strictness_options.LESS_STRICT,
            )
            for item_name in life_flasks
        ],
    ],
    *armour,
    *jewelry,
    *weapon,
    *jewel,
]
