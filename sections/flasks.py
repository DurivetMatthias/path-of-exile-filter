from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

utility_flasks = [
    "Granite Flask",
    "Quartz Flask",
    "Quicksilver Flask",
    "Silver Flask",
]

rules = [
    Show(
        [
            MultiBaseType(utility_flasks),
            ItemLevel(85),
            Rarity(RARITY.UNIQUE, OPERATOR.NOT_EQUAL),
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
    # Show(
    #     [
    #         MultiClass(["Life Flasks"]),
    #         TierStyle(TIER.COMMON),
    #     ]
    # ),
    # Show(
    #     [
    #         MultiBaseType(["Divine Life Flask"]),
    #         TierStyle(TIER.COMMON),
    #     ]
    # ),
    Hide(
        [MultiClass(["Life Flasks", "Mana Flasks", "Hybrid Flasks", "Utility Flasks"])]
    ),
]
