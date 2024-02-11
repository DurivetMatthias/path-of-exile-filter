from app import categories, extensions
from app.rules import Rule

utility_flasks = [
    "Amethyst Flask",
    "Basalt Flask",
    "Diamond Flask",
    "Gold Flask",
    "Granite Flask",
    "Jade Flask",
    "Quartz Flask",
    "Quicksilver Flask",
    "Ruby Flask",
    "Sapphire Flask",
    "Topaz Flask",
]

rules = [
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=flask_name),
                extensions.ItemLevel(item_level=85, operator=categories.OPERATOR.GTE),
                extensions.TierStyle(tier=categories.TIER.LEGENDARY),
            ],
        )
        for flask_name in utility_flasks
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=flask_name),
                extensions.ItemLevel(item_level=80, operator=categories.OPERATOR.GTE),
                extensions.TierStyle(tier=categories.TIER.COMMON),
            ],
        )
        for flask_name in utility_flasks
    ],
]
