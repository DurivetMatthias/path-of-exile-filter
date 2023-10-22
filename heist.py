"""This file defines the rules for heist items."""

import categories
import rule


class HeistStyle(rule.Rule):
    def label(self) -> categories.LABEL:
        return categories.LABEL.WHITE_ON_RED

    def icon_shape(self) -> categories.SHAPE:
        return categories.SHAPE.UPSIDE_DOWN_HOUSE


class HeistItem(HeistStyle):
    def filter(self):
        return f"""
            BaseType "{self.name}"
        """


class HeistClass(HeistItem):
    def filter(self):
        return f"""
            Class "{self.name}"
        """


best_in_slot_items = [
    "Foliate Brooch",
    "Precise Arrowhead",
    "Whisper-woven Cloak",
    "Regicide Disguise Kit",
    "Grandmaster Keyring",
    "Thaumetic Flashpowder",
    "Thaumaturgical Sensing Charm",
    "Thaumaturgical Ward",
    "Silkweave Sole",
    "Thaumetic Blowtorch",
    "Steel Bracers",
    "Master Lockpick",
]

heist_item_classes = [
    "Heist Brooch",
    "Heist Cloak",
    "Heist Gear",
    "Heist Tool",
]

rules = [
    HeistItem(
        name="Rogue's Marker",
        rarity=categories.RARITY.COMMON,
        strictness=categories.STRICTNESS.STRICT,
    ),
    HeistItem(
        name="Tempering Orb",
        rarity=categories.RARITY.LEGENDARY,
    ),
    HeistItem(
        name="Tailoring Orb",
        rarity=categories.RARITY.LEGENDARY,
    ),
    HeistClass(
        name="Blueprint",
        rarity=categories.RARITY.LEGENDARY,
    ),
    HeistClass(
        name="Contract",
        rarity=categories.RARITY.EPIC,
    ),
    HeistClass(
        name="Heist Target",
        rarity=categories.RARITY.COMMON,
    ),
    *[
        HeistItem(
            name=item_name,
            rarity=categories.RARITY.EPIC,
        )
        for item_name in best_in_slot_items
    ],
    *[
        HeistClass(
            name=item_class,
            rarity=categories.RARITY.RARE,
            strictness=categories.STRICTNESS.STRICT,
        )
        for item_class in heist_item_classes
    ],
    HeistClass(
        name="Trinket",
        rarity=categories.RARITY.LEGENDARY,
    ),
]
