from app import categories, extensions
from app.rules import Rule

# Item Class: Jewels
# Rarity: Normal
# Large Cluster Jewel
# --------
# Item Level: 83
# --------
# Adds 8 Passive Skills (enchant)
# 2 Added Passive Skills are Jewel Sockets (enchant)
# Added Small Passive Skills grant: 12% increased Fire Damage (enchant)
# --------
# Place into an allocated Large Jewel Socket on the Passive Skill Tree. Added passives do not interact with jewel radiuses. Right click to remove from the Socket.

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
