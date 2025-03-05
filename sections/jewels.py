from app.blocks import Show, Hide
from app.conditions import MultiBaseType, Rarity
from app.actions import TierStyle
from app.categories import TIER, JEWEL, RARITY, OPERATOR

rules = [
    Show(
        [
            MultiBaseType([JEWEL.CRIMSON, JEWEL.MEDIUM_CLUSTER, JEWEL.LARGE_CLUSTER]),
            TierStyle(TIER.COMMON),
        ],
    ),
    Hide(
        [
            MultiBaseType(list(JEWEL)),
            Rarity(RARITY.RARE, operator=OPERATOR.LTE),
        ],
    ),
]
