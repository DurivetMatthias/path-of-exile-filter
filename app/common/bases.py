from app import categories, extensions
from app.rules import Rule


# TODO auto fetch top bases
bis_armour_bases = [
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

endgame_jewelry_bases = [
    "Vermillion Ring",
    "Marble Amulet",
]


rules = [
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.MultiBaseType(base_types=bis_armour_bases),
            extensions.ItemLevel(item_level=85, operator=categories.OPERATOR.GTE),
            extensions.BaseDefensePercentile(
                percentile=90,
                operator=categories.OPERATOR.GTE,
            ),
            extensions.TierStyle(tier=categories.TIER.LEGENDARY),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.MultiBaseType(base_types=endgame_jewelry_bases),
            extensions.ItemLevel(item_level=84, operator=categories.OPERATOR.GTE),
            extensions.TierStyle(tier=categories.TIER.LEGENDARY),
        ],
    ),
]
