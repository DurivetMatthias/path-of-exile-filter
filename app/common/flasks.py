from app import categories, extensions
from app.rules import Rule

# TODO fetch as external data
# TODO simplify as JSON
utility_flasks = [
    "Amethyst Flask",
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
                extensions.TierStyle(tier=categories.TIER.RARE),
            ],
        )
        for flask_name in utility_flasks
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=flask_name),
                extensions.ItemLevel(item_level=80, operator=categories.OPERATOR.LTE),
                extensions.TierStyle(tier=categories.TIER.COMMON),
            ],
        )
        for flask_name in utility_flasks
    ],
]
