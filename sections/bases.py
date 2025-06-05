from app.blocks import Show
from app.conditions import (
    BaseType,
    MultiBaseType,
    AreaLevel,
    MultiClass,
    BaseArmour,
    BaseEnergyShield,
    BaseEvasion,
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
            Rarity(RARITY.RARE),
            BaseArmour(),
            BaseEnergyShield(0, OPERATOR.EQUAL),
            BaseEvasion(0, OPERATOR.EQUAL),
            MultiClass(
                [
                    "Boots",
                    "Gloves",
                    "Helmets",
                    # "Body Armours",
                    "Shields",
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiBaseType(
                [
                    "Void Sceptre",
                    "Turquoise Amulet",
                    "Scholar's Robe",
                    "Amethyst Ring",
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]
