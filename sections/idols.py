from app.blocks import Show
from app.actions import TierStyle
from app.conditions import Class, MultiBaseType
from app.categories import TIER

rules = [
    Show(
        [
            Class("Idol"),
            MultiBaseType(
                [
                    "Minor Idol",
                    "Kamasan Idol",
                    "Totemic Idol",
                    "Noble Idol",
                    "Burial Idol",
                    "Conqueror Idol",
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
]
