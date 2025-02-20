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
    # Hide(
    #     [
    #         MultiBaseType(
    #             [
    #                 "Life Flask",
    #                 "Mana Flask",
    #             ]
    #         )
    #     ]
    # ),
]
