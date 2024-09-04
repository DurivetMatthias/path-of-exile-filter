from app.blocks import Show
from app.conditions.compound import MultiClass, TierStyle
from app.conditions.standard import BaseType, StackSize
from app.categories import TIER

classes = [
    "Contracts",
    "Blueprints",
]

rules = [
    Show(
        [
            MultiClass(classes),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            BaseType("Rogue's Marker"),
            StackSize(1000),
            TierStyle(TIER.EPIC),
        ]
    ),
]
