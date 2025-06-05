from app.blocks import Show
from app.conditions import (
    MultiBaseType,
    MultiClass,
    BaseArmour,
    BaseEnergyShield,
    BaseEvasion,
    Rarity,
)
from app.actions import TierStyle
from app.categories import TIER, RARITY, OPERATOR

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
                    "Body Armours",
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
