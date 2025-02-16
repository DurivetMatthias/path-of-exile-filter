from app.blocks import Show
from app.conditions import (
    BaseType,
    AreaLevel,
)
from app.actions import TierStyle
from app.categories import TIER, OPERATOR

rules = [
    Show(
        [
            BaseType("Stone Axe"),
            AreaLevel(8, operator=OPERATOR.LTE),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            BaseType("Jade Chopper"),
            AreaLevel(12, operator=OPERATOR.LTE),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            BaseType("Woodsplitter"),
            AreaLevel(16, operator=OPERATOR.LTE),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]
