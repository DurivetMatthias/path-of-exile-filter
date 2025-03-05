from app.blocks import Show, Hide
from app.actions import TierStyle
from app.conditions import (
    BaseType,
    StackSize,
    Class,
    MultiBaseType,
    MultiClass,
    ItemLevel,
)
from app.categories import TIER, OPERATOR

best_in_slot_items = [
    "Foliate Brooch",
    "Whisper-woven Cloak",
    "Precise Arrowhead",
    # Tools
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
item_classes = [
    "Heist Brooch",
    "Heist Cloak",
    "Heist Gear",
    "Heist Tool",
    "Heist Target",
]

rules = [
    Show(
        [
            MultiBaseType(best_in_slot_items),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            MultiClass(item_classes),
            TierStyle(TIER.RARE),
        ]
    ),
    Show(
        [
            Class("Contracts"),
            ItemLevel(83),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            Class("Contracts"),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            Class("Blueprints"),
            ItemLevel(83),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            Class("Blueprints"),
            TierStyle(TIER.RARE),
        ]
    ),
    Show(
        [
            Class("Heist Target"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            Class("Trinkets"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiBaseType(["Tailoring Orb", "Tempering Orb"]),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            BaseType("Rogue's Marker"),
            StackSize(200),
            TierStyle(TIER.EPIC),
        ]
    ),
    Hide(
        [
            BaseType("Rogue's Marker"),
            TierStyle(TIER.EPIC),
        ]
    ),
]
