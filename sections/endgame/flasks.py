from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

rules = [
    Show(
        [
            AreaLevel(68, OPERATOR.LT),
            MultiClass(
                [
                    "Life Flasks",
                    "Mana Flasks",
                    "Hybrid Flasks",
                    "Utility Flasks",
                ]
            ),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            MultiBaseType(["Divine Life Flask"]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Hide(
        [MultiClass(["Life Flasks", "Mana Flasks", "Hybrid Flasks", "Utility Flasks"])]
    ),
]
