from app.blocks import Show
from app.actions import TierStyle
from app.conditions import Class, MapTier
from app.categories import TIER

rules = [
    Show(
        [
            Class("Map"),
            MapTier(17),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            Class("Map"),
            MapTier(16),
            TierStyle(TIER.EPIC),
        ],
    ),
    Show(
        [
            Class("Map"),
            TierStyle(TIER.RARE),
        ],
    ),
]
