from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

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

# Item Class: Quest Items
# Rarity: Quest
# Contract: The Wedding Dress
# --------
# Client: Tullina
# Heist Target: Merveil's Wedding Dress
# Area Level: 73
# Requires Agility (Level 1)
# Requires Tullina, the Catburglar
# --------
# "Let's just hope she wasn't wearing it when she wandered into the sea!"


rules = [
    # Remove quest-contracts
    Show(
        [
            Class("Quest Items"),
            BaseType("Contract", OPERATOR.CONTAINS),
            SetFontSize(1),
            SetBackgroundColor(RGB.TRANSPARENT),
            SetTextColor(RGB.TRANSPARENT),
            SetBorderColor(RGB.TRANSPARENT),
        ]
    ),
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
            ItemLevel(68),
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
        ]
    ),
]
