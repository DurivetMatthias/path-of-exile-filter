from app.blocks import Hide
from app.conditions.compound import MultiBaseType

basic_jewels = [
    "Cobalt Jewel",
    "Crimson Jewel",
    "Viridian Jewel",
]

rules = [
    Hide(
        [
            MultiBaseType(basic_jewels),
        ],
    ),
]
