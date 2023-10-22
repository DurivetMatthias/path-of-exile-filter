"""This file defines the rules for currency items."""

import categories
import rule


class GearStyle(rule.Rule):
    def label(self) -> categories.LABEL:
        return categories.LABEL.WHITE_ON_PINK

    def icon_shape(self) -> categories.SHAPE:
        return categories.SHAPE.KITE


class Gear(GearStyle):
    def __init__(self, level: str = "> 0", **kwargs):
        super().__init__(**kwargs)
        self.level = level

    def filter(self):
        return f"""
            BaseType == "{self.name}"
            ItemLevel {self.level}
        """


life_flasks = [
    "Divine Life Flask",
]

utility_flasks = [
    "Quicksilver Flask",
    "Granite Flask",
    "Ruby Flask",
    "Quartz Flask",
]

bodies = [
    "Glorious Plate",
]

belts = [
    "Stygian Vise",
]

gloves = [
    "Titan Gauntlets",
]

boots = [
    "Titan Greaves",
]

helmets = [
    "Royal Burgonet",
]

amulets = [
    "Turquoise Amulet",
]

rings = [
    "Vermillion Ring",
    "Amethyst Ring",
]

weapons = [
    "Void Sceptre",
]

jewels = [
    "Crimson Jewel",
    "Viridian Jewel",
    "Cobalt Jewel",
]

cluster_jewels = [
    "Small Cluster Jewel",
    "Medium Cluster Jewel",
    "Large Cluster Jewel",
]

lvl_86 = [
    *bodies,
    *belts,
]

lvl_85 = [
    *gloves,
    *boots,
    *helmets,
    *amulets,
    *utility_flasks,
]

lvl_84 = [
    *rings,
    *weapons,
]

lvl_1 = [
    *jewels,
    *cluster_jewels,
]

rules = [
    # Level 86 gear
    *[
        Gear(
            name=item_name,
            rarity=categories.RARITY.LEGENDARY,
            level=">= 86",
            strictness=categories.STRICTNESS.STRICT,
        )
        for item_name in lvl_86
    ],
    *[
        Gear(
            name=item_name,
            rarity=categories.RARITY.RARE,
            strictness=categories.STRICTNESS.LESS_STRICT,
        )
        for item_name in lvl_86
    ],
    # Level 85 gear
    *[
        Gear(
            name=item_name,
            rarity=categories.RARITY.EPIC,
            level=">= 85",
            strictness=categories.STRICTNESS.STRICT,
        )
        for item_name in lvl_85
    ],
    *[
        Gear(
            name=item_name,
            rarity=categories.RARITY.RARE,
            strictness=categories.STRICTNESS.LESS_STRICT,
        )
        for item_name in lvl_85
    ],
    # Level 84 gear
    *[
        Gear(
            name=item_name,
            rarity=categories.RARITY.EPIC,
            level=">= 84",
            strictness=categories.STRICTNESS.STRICT,
        )
        for item_name in lvl_84
    ],
    *[
        Gear(
            name=item_name,
            rarity=categories.RARITY.RARE,
            strictness=categories.STRICTNESS.LESS_STRICT,
        )
        for item_name in lvl_84
    ],
    # Life Flasks
    *[
        Gear(
            name=item_name,
            rarity=categories.RARITY.RARE,
            level=">= 80",
            strictness=categories.STRICTNESS.LESS_STRICT,
        )
        for item_name in life_flasks
    ],
    *[
        Gear(
            name=item_name,
            rarity=categories.RARITY.COMMON,
            strictness=categories.STRICTNESS.LESS_STRICT,
        )
        for item_name in life_flasks
    ],
    # Level 1 gear
    *[
        Gear(
            name=item_name,
            rarity=categories.RARITY.RARE,
            strictness=categories.STRICTNESS.STRICT,
        )
        for item_name in lvl_1
    ],
]
