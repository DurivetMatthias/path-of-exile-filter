from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

rules = [
    Show(
        [
            MultiBaseType([JEWEL.MEDIUM_CLUSTER]),
            EnchantmentPassiveNode("Fire Damage over Time"),
            TierStyle(TIER.EPIC),
        ],
    ),
    Show(
        [
            MultiBaseType([JEWEL.MEDIUM_CLUSTER]),
            EnchantmentPassiveNode("Fire Damage over Time"),
            EnchantmentPassiveNum(5, OPERATOR.LTE),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            MultiBaseType([JEWEL.LARGE_CLUSTER]),
            EnchantmentPassiveNode("Fire Damage"),
            EnchantmentPassiveNum(8, OPERATOR.LTE),
            TierStyle(TIER.COMMON),
        ],
    ),
    Show(
        [
            MultiBaseType(
                [
                    JEWEL.LARGE_CLUSTER,
                    JEWEL.MEDIUM_CLUSTER,
                    JEWEL.SMALL_CLUSTER,
                ]
            ),
        ],
    ),
    # Show(
    #     [
    #         MultiBaseType([JEWEL.CRIMSON]),
    #         TierStyle(TIER.COMMON),
    #     ],
    # ),
    Hide([MultiBaseType(list(JEWEL))]),
]
