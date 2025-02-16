from app.blocks import Show
from app.conditions import BaseType, AreaLevel
from app.actions import TierStyle
from app.categories import TIER, OPERATOR

BEFORE_RF = 16
BEFORE_SIOSA = 30
BEFORE_MAPS = 67

rules = [
    Show(
        [
            AreaLevel(5, operator=OPERATOR.LTE),
            BaseType("Plate Vest"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(16, operator=OPERATOR.LTE),
            BaseType("Chestplate"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(6, operator=OPERATOR.LTE),
            BaseType("Iron Hat"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(17, operator=OPERATOR.LTE),
            BaseType("Cone Helmet"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(10, operator=OPERATOR.LTE),
            BaseType("Iron Gauntlets"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(15, operator=OPERATOR.LTE),
            BaseType("Plated Gauntlets"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF, operator=OPERATOR.LTE),
            BaseType("Rustic Sash"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF, operator=OPERATOR.LTE),
            BaseType("Jade Amulet"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF, operator=OPERATOR.LTE),
            BaseType("Iron Ring"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(40, operator=OPERATOR.LTE),
            BaseType("Quartz Sceptre"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(60, operator=OPERATOR.LTE),
            BaseType("Crystal Sceptre"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS, operator=OPERATOR.LTE),
            BaseType("Opal Sceptre"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS, operator=OPERATOR.LTE),
            BaseType("Amethyst Ring"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_SIOSA, operator=OPERATOR.LTE),
            BaseType("Leather Belt"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS, operator=OPERATOR.LTE),
            BaseType("Quicksilver Flask"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]
