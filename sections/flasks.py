from app.blocks import Show, Hide
from app.conditions import MultiBaseType, ItemLevel, MultiClass
from app.actions import TierStyle
from app.categories import TIER

utility_flasks = [
    "Granite Flask",
    "Quartz Flask",
    "Quicksilver Flask",
    "Silver Flask",
    "Gold Flask",
    "Ruby Flask",
    "Topaz Flask",
    "Sapphire Flask",
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
            ItemLevel(80),
            TierStyle(TIER.EPIC),
        ],
    ),
    Show(
        [
            MultiBaseType(utility_flasks),
            TierStyle(TIER.RARE),
        ],
    ),
    Show(
        [
            MultiClass(["Life Flasks", "Mana Flasks"]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Hide([MultiClass(["Life Flasks", "Mana Flasks"])]),
]
