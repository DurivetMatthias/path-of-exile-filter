from app.blocks import Show
from app.conditions import (
    BaseType,
    AreaLevel,
    MultiClass,
    LinkedSockets,
)
from app.actions import TierStyle
from app.categories import TIER

BEFORE_RF = 16
BEFORE_SIOSA = 30
BEFORE_MAPS = 67

rules = [
    Show(
        [
            AreaLevel(BEFORE_RF),
            BaseType("Rawhide Tower Shield"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(8),
            MultiClass(
                [
                    "Two Hand Sword",
                    "Two Hand Axe",
                    "Two Hand Mace",
                ]
            ),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(12),
            BaseType("Jade Chopper"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF),
            BaseType("Woodsplitter"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(5),
            BaseType("Plate Vest"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(16),
            BaseType("Chestplate"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(6),
            BaseType("Iron Hat"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(17),
            BaseType("Cone Helmet"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(10),
            BaseType("Iron Gauntlets"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(15),
            BaseType("Plated Gauntlets"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(8),
            BaseType("Iron Greaves"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(19),
            BaseType("Steel Greaves"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF),
            BaseType("Rustic Sash"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF),
            BaseType("Jade Amulet"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF),
            BaseType("Lapis Amulet"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF),
            BaseType("Coral Ring"),
            TierStyle(TIER.RARE),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF),
            BaseType("Iron Ring"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(40),
            BaseType("Quartz Sceptre"),
            LinkedSockets(3),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(40),
            BaseType("Quartz Sceptre"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(60),
            BaseType("Crystal Sceptre"),
            LinkedSockets(3),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(60),
            BaseType("Crystal Sceptre"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS),
            BaseType("Opal Sceptre"),
            LinkedSockets(3),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS),
            BaseType("Opal Sceptre"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS),
            BaseType("Amethyst Ring"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS),
            BaseType("Leather Belt"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS),
            BaseType("Quicksilver Flask"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]
