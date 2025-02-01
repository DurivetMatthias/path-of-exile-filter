from app.blocks import Show
from app.actions import TierStyle
from app.conditions import BaseType, Rarity, MultiBaseType
from app.categories import TIER, RARITY

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
            TierStyle(TIER.COMMON),
        ],
    ),
]
