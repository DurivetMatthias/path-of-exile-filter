from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

equiped_classes = [
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

fractured_classes = [
    "Sceptres",
    "Rune Daggers",
    "Shields",
    "Jewels",
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
    Show(
        [
            Influenced(),
            Class("Shields"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            Influenced(),
            Class("Helmets"),
            TierStyle(TIER.EPIC),
        ]
    ),
]
