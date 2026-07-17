from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

influenced_bases = [
    "Giantslayer Helmet",
    "Colossal Tower Shield",
    "Pinnacle Tower Shield",
]

rules = [
    Show(
        [
            FracturedItem(),
            TierStyle(TIER.RARE),
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
    Show(
        [
            Influenced(),
            MultiBaseType(influenced_bases),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]
