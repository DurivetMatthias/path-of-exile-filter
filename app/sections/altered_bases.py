from app.blocks import Show
from app.actions import TierStyle
from app.conditions import FracturedItem, Influenced, MultiClass, MultiBaseType
from app.categories import TIER

fractured_classes = [
    "Helmets",
    "Gloves",
    "Boots",
    "Sceptres",
    "Rune Daggers",
    "Shields",
    "Rings",
    "Amulets",
    "Jewels",
]

influenced_bases = [
    "Giantslayer Helmet",
    "Colossal Tower Shield",
    "Pinnacle Tower Shield",
]

rules = [
    Show(
        [
            FracturedItem(),
            MultiClass(fractured_classes),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            Influenced(),
            MultiBaseType(influenced_bases),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]
