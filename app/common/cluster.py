from app import categories, extensions
from app.rules import Rule

cluster_jewels = [
    "Large Cluster Jewel",
    "Medium Cluster Jewel",
    "Small Cluster Jewel",
]

rules = [
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.MultiBaseType(base_types=cluster_jewels),
            extensions.ItemLevel(item_level=84, operator=categories.OPERATOR.GTE),
            extensions.TierStyle(tier=categories.TIER.LEGENDARY),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.MultiBaseType(base_types=cluster_jewels),
            extensions.ItemLevel(item_level=84, operator=categories.OPERATOR.LT),
            extensions.TierStyle(tier=categories.TIER.EPIC),
        ],
    ),
]
