from app.blocks import *
from app.actions import *
from app.categories import *
from app.conditions import *

tier_0 = [
    "Leather Belt",
    "Heavy Belt",
    "Ring",
    "Paua Amulet",
]
double_corrupt = [
    "Scholar's Robe",
    "Desert Brigandine",
    "Simple Robe",
]
rules = [
    Show(
        [
            Rarity(RARITY.UNIQUE),
            MultiBaseType(tier_0),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            Rarity(RARITY.UNIQUE),
            MultiBaseType(double_corrupt),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            Rarity(RARITY.UNIQUE),
            Class("Jewel"),
            Corrupted(False),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            Rarity(RARITY.UNIQUE),
            Class("Jewel"),
            Corrupted(True),
            TierStyle(TIER.COMMON),
        ],
    ),
    Show(
        [
            BaseType("Vaal Aspect"),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            MultiClass(["Ring", "Amulet"]),  # Disenchant Kingsmarch
            Rarity(RARITY.UNIQUE),
            TierStyle(TIER.COMMON),
        ],
    ),
    Show(
        [
            Rarity(RARITY.UNIQUE),
            Replica(),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(68, OPERATOR.LT),
            Rarity(RARITY.UNIQUE),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]
