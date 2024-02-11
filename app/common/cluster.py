from app import categories, extensions
from app.rules import Rule

cluster_jewels = [
    "Large Cluster Jewel",
    "Medium Cluster Jewel",
    "Small Cluster Jewel",
]

rules = [
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=cluster_jewel),
                extensions.ItemLevel(item_level=84, operator=categories.OPERATOR.GTE),
                extensions.TierStyle(tier=categories.TIER.LEGENDARY),
            ],
        )
        for cluster_jewel in cluster_jewels
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=cluster_jewel),
                extensions.ItemLevel(item_level=84, operator=categories.OPERATOR.LT),
                extensions.TierStyle(tier=categories.TIER.EPIC),
            ],
        )
        for cluster_jewel in cluster_jewels
    ],
]
