from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

tier_0 = [
    "Leather Belt",
    "Heavy Belt",
    "Ring",
    "Paua Amulet",
    "Elegant Round Shield",
]
double_corrupt = [
    "Scholar's Robe",
    "Majestic Plate",
    "Colosseum Plate",
    "Desert Brigandine",
    "Devout Chainmail",
    "Saint's Hauberk",
    "Simple Robe",
    "Cobalt Jewel",
    "Crimson Jewel",
    "Viridian Jewel",
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
            BaseType("Vaal Aspect"),
            TierStyle(TIER.LEGENDARY),
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
            Rarity(RARITY.UNIQUE),
            Foulborn(),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]
