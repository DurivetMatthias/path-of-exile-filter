from app import categories, extensions
from app.rules import Rule

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
]

jewelry = [
    # Amulet
    "Jade Amulet",
    "Lapis Amulet",
    "Turquoise Amulet",
    "Onyx Amulet",
    "Simplex Amulet",
    "Focused Amulet",
    # Ring
    "Amethyst Ring",
    "Vermillion Ring",
    "Cogwork Ring",
    "Composite Ring",
    "Geodesic Ring",
    "Helical Ring",
    "Manifold Ring",
    "Ratcheting Ring",
]

flasks = [
    "Quartz Flask",
    "Amethyst Flask",
    "Granite Flask",
    "Jade Flask",
    "Quicksilver Flask",
    "Silver Flask",
    "Ruby Flask",
    "Sapphire Flask",
    "Topaz Flask",
]

rules = [
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.ItemLevel(item_level=85, operator=categories.OPERATOR.GTE),
                extensions.BaseDefencePercentile(
                    percentile=100,
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
                extensions.ItemLevel(item_level=85, operator=categories.OPERATOR.GTE),
                extensions.TierStyle(tier=categories.TIER.LEGENDARY),
            ],
        )
        for base_type in jewelry
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.ItemLevel(item_level=85, operator=categories.OPERATOR.GTE),
                extensions.TierStyle(tier=categories.TIER.LEGENDARY),
            ],
        )
        for base_type in flasks
    ],
]
