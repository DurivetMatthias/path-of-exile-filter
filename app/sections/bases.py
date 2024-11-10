from app.blocks import Show
from app.conditions import (
    BaseType,
    MultiBaseType,
    AreaLevel,
    MultiClass,
    BaseArmour,
    Class,
    Rarity,
)
from app.actions import TierStyle
from app.categories import TIER, RARITY

EARLY_MAPS = 82

rules = [
    Show(
        [
            MultiBaseType(["Vermillion Ring", "Marble Amulet"]),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            BaseType("Scholar's Robe"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(EARLY_MAPS),
            MultiClass(["Gloves", "Boots"]),
            BaseArmour(200),
            Rarity(RARITY.MAGIC),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(EARLY_MAPS),
            Class("Helmets"),
            BaseArmour(400),
            Rarity(RARITY.MAGIC),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(EARLY_MAPS),
            Class("Body Armours"),
            BaseArmour(800),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(EARLY_MAPS),
            BaseType("Void Sceptre"),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(EARLY_MAPS),
            Class("Shield"),
            BaseArmour(500),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(EARLY_MAPS),
            BaseType("Leather Belt"),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(EARLY_MAPS),
            BaseType("Amethyst Ring"),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(EARLY_MAPS),
            BaseType("Onyx Amulet"),
            TierStyle(TIER.COMMON),
        ]
    ),
]
