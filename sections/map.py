from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

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
