from app.blocks import Show
from app.conditions.standard import (
    Fractured,
)
from app.conditions.compound import TierStyle, MultiClass
from app.categories import TIER

fractured_classes = [
    # "Helmets",
    # "Gloves",
    # "Boots",
    "Sceptres",
    "Rune Daggers",
    # "Shields",
    "Rings",
    "Amulets",
]

influenced_bases = [
    "Giantslayer Helmet",
    "Colossal Tower Shield",
    "Pinnacle Tower Shield",
]

rules = [
    Show(
        [
            Fractured(),
            MultiClass(fractured_classes),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    # Show(
    #     [
    #         Influenced(),
    #         MultiBaseType(influenced_bases),
    #         TierStyle(TIER.LEGENDARY),
    #     ]
    # ),
]
