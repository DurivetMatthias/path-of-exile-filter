from app.blocks import *
from app.actions import *
from app.categories import *
from app.conditions import *

rules = [
    Show(
        [
            AreaLevel(15, OPERATOR.LTE),
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
            AreaLevel(67, OPERATOR.LTE),
            MultiClass(
                [
                    "Life Flasks",
                    "Utility Flasks",
                ]
            ),
            TierStyle(TIER.COMMON),
        ]
    ),
    Hide(
        [MultiClass(["Life Flasks", "Mana Flasks", "Hybrid Flasks", "Utility Flasks"])]
    ),
]
