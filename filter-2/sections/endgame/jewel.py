from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *

rules = [
    Show(
        [
            MultiBaseType(
                [
                    "Ruby",
                    # "Emerald",
                    # "Sapphire",
                ]
            ),
            TierStyle(TIER.RARE),
        ]
    ),
    Show(
        [
            MultiBaseType(
                [
                    "Time-Lost Ruby",
                    "Time-Lost Emerald",
                    "Time-Lost Sapphire",
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Hide([Rarity(RARITY.RARE, OPERATOR.LTE), Class("Jewels")]),
]
