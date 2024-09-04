from app.blocks import Show
from app.conditions.compound import TierStyle
from app.conditions.standard import ClassName, MapTier
from app.categories import TIER

rules = [
    Show(
        [
            ClassName("Map"),
            MapTier(17),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            ClassName("Map"),
            MapTier(16),
            TierStyle(TIER.EPIC),
        ],
    ),
    Show(
        [
            ClassName("Map"),
            TierStyle(TIER.RARE),
        ],
    ),
]
