from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

rules = [
    Show(
        [
            MultiBaseType(["Medium Cluster Jewel"]),
            EnchantmentPassiveNode("Fire Damage over Time"),
            TierStyle(TIER.EPIC),
        ],
    ),
    Show(
        [
            MultiBaseType(["Medium Cluster Jewel"]),
            EnchantmentPassiveNode("Fire Damage over Time"),
            EnchantmentPassiveNum(5, OPERATOR.LTE),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            MultiBaseType(["Small Cluster Jewel"]),
            EnchantmentPassiveNode("Reservation Efficiency"),
            EnchantmentPassiveNum(3, OPERATOR.LTE),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            MultiBaseType(["Large Cluster Jewel"]),
            EnchantmentPassiveNode("Fire Damage"),
            EnchantmentPassiveNum(8, OPERATOR.LTE),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            MultiBaseType(
                [
                    "Small Cluster Jewel",
                    "Medium Cluster Jewel",
                    "Large Cluster Jewel",
                ]
            ),
        ],
    ),
    Show(
        [
            MultiBaseType(["Crimson Jewel"]),
            TierStyle(TIER.COMMON),
        ],
    ),
    Hide([Class("Jewels")]),
]
