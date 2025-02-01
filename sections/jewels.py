from app.blocks import Show
from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.categories import TIER, JEWEL

rules = [
    Show(
        [
            MultiBaseType(list(JEWEL)),
            TierStyle(TIER.COMMON),
        ],
    ),
]
