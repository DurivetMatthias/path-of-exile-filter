from app.blocks import Show
from app.conditions import (
    BaseType,
    MultiBaseType,
    AreaLevel,
    MultiClass,
    BaseArmour,
    Class,
    Rarity,
    ItemLevel,
)
from app.actions import TierStyle
from app.categories import TIER, RARITY, OPERATOR

EARLY_MAPS = 82

rules = [
    Show(
        [
            MultiBaseType(["Vermillion Ring", "Marble Amulet"]),
            ItemLevel(84),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiClass(["Boots"]),
            BaseArmour(359),
            ItemLevel(85),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    # Show(
    #     [
    #         MultiClass(["Helmets"]),
    #         BaseArmour(501),
    #         ItemLevel(85),
    #         TierStyle(TIER.LEGENDARY),
    #     ]
    # ),
    Show(
        [
            MultiClass(["Gloves"]),
            BaseArmour(359),
            ItemLevel(85),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    # Show(
    #     [
    #         MultiClass(["Shield"]),
    #         BaseArmour(467),
    #         ItemLevel(84),
    #         TierStyle(TIER.LEGENDARY),
    #     ]
    # ),
    Show(
        [
            MultiBaseType(["Amethyst Ring"]),
            ItemLevel(84),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiBaseType(["Onyx Amulet", "Jade Amulet"]),
            ItemLevel(84),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiClass(["Ring", "Amulet"]),
            Rarity(RARITY.RARE),
            TierStyle(TIER.COMMON),
        ]
    ),
]
