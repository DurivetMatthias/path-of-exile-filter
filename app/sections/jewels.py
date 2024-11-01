from app.blocks import Show
from app.conditions import Rarity, MultiBaseType
from app.actions import TierStyle
from app.categories import RARITY, OPERATOR

basic_jewels = [
    "Cobalt Jewel",
    "Crimson Jewel",
    "Viridian Jewel",
]

rules = [
    Show(
        [
            MultiBaseType(basic_jewels),
            Rarity(RARITY.RARE, operator=OPERATOR.LTE),
            TierStyle(RARITY.MAGIC),
        ],
    ),
]
