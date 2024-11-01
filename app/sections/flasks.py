from app.blocks import Show
from app.conditions import MultiBaseType, ItemLevel, Class, Quality
from app.actions import TierStyle
from app.categories import TIER, OPERATOR

utility_flasks = [
    "Granite Flask",
    "Quartz Flask",
    "Quicksilver Flask",
    "Silver Flask",
    "Sulphur Flask",
    "Jade Flask",
    "Gold Flask",
]

rules = [
    Show(
        [
            MultiBaseType(utility_flasks),
            ItemLevel(85),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            MultiBaseType(utility_flasks),
            TierStyle(TIER.EPIC),
        ],
    ),
    Show(
        [
            Class("Flask", OPERATOR.EQUAL),
            Quality(1),
            TierStyle(TIER.RARE),
        ],
    ),
]
