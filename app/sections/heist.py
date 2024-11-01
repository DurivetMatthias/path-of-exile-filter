from app.blocks import Show
from app.actions import TierStyle
from app.conditions import BaseType, StackSize, Class, MultiBaseType, MultiClass
from app.categories import TIER

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
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            Class("Blueprints"),
            TierStyle(TIER.LEGENDARY),
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
            StackSize(500),
            TierStyle(TIER.EPIC),
        ]
    ),
]
