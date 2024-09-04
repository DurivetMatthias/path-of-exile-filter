from app.blocks import Show
from app.conditions.compound import MultiBaseType, TierStyle
from app.categories import TIER

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
]
