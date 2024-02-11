from app import categories, extensions
from app.rules import Rule


# TODO auto fetch top bases
armour = [
    # STR
    "Glorious Plate",
    "Titan Gauntlets",
    "Titan Greaves",
    "Royal Burgonet",
    # STR/DEX
    "Full Dragonscale",
    "Dragonscale Gauntlets",
    "Dragonscale Boots",
    "Nightmare Bascinet",
    # DEX
    "Zodiac Leather",
    "Lion Pelt",
    "Slink Gloves",
    "Slink Boots",
]


rules = [
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.ItemLevel(item_level=85, operator=categories.OPERATOR.GTE),
                extensions.BaseDefensePercentile(
                    percentile=90,
                    operator=categories.OPERATOR.GTE,
                ),
                extensions.TierStyle(tier=categories.TIER.LEGENDARY),
            ],
        )
        for base_type in armour
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.ItemLevel(item_level=84, operator=categories.OPERATOR.GTE),
                extensions.TierStyle(tier=categories.TIER.LEGENDARY),
            ],
        )
        for base_type in ["Vermillion Ring", "Marble Amulet"]
    ],
]
