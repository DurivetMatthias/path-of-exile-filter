"""This file defines the rules for veiled items."""

import categories
import rule


class VeiledStyle(rule.Rule):
    def label(self) -> categories.LABEL:
        return categories.LABEL.WHITE_ON_YELLOW

    def icon_shape(self) -> categories.SHAPE:
        return categories.SHAPE.TRIANGLE


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
            rarity=categories.RARITY.EPIC,
            strictness=categories.STRICTNESS.LESS_STRICT,
        )
        for class_name in prefix_classes
    ],
    *[
        VeiledSuffix(
            name=class_name,
            rarity=categories.RARITY.EPIC,
            strictness=categories.STRICTNESS.LESS_STRICT,
        )
        for class_name in suffix_classes
    ],
]
