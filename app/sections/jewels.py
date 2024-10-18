from app.blocks import Show
from app.conditions.compound import MultiBaseType
from app.conditions.standard import Rarity
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
        ],
    ),
]
