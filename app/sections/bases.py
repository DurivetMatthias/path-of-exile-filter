from app.blocks import Show
from app.conditions.standard import BaseType, Rarity
from app.conditions.compound import MultiBaseType, MultiClass, TierStyle
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
            TierStyle(TIER.RARE),
        ]
    ),
]
