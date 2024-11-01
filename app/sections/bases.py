from app.blocks import Show
from app.conditions import BaseType, Rarity, MultiBaseType, MultiClass
from app.actions import TierStyle
from app.categories import TIER, RARITY

atlas_bases = [
    "Vermillion Ring",
    "Marble Amulet",
]

rules = [
    Show(
        [
            MultiBaseType(atlas_bases),
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
            Rarity(RARITY.RARE),
            MultiClass(
                [
                    "Helmets",
                    "Gloves",
                    "Boots",
                    "Body Armours",
                    "Sceptres",
                    "Shields",
                    "Rings",
                    "Amulets",
                    "Belts",
                ]
            ),
        ]
    ),
]
