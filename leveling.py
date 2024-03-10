"""
This file is intended to be changed often during leveling.
Add and remove rules depending on your current needs.
"""

from app import categories, common, extensions, filter, rules

armour_with_sockets = ["Body Armours", "Helmets", "Gloves", "Boots"]
weapon_classes = ["Sceptres", "Wands"]
rings_with_resistance = [
    "Ruby Ring",
    "Sapphire Ring",
    "Topaz Ring",
    "Two-Stone Ring",
    "Amethyst Ring",
]

rules = [
    rules.Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.MultiClass(class_names=armour_with_sockets),
            extensions.SocketGroup(sockets="3", operator=categories.OPERATOR.EXACT),
            extensions.TierStyle(tier=categories.TIER.RARE),
        ],
    ),
    rules.Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.MultiClass(class_names=armour_with_sockets),
            extensions.SocketGroup(sockets="4", operator=categories.OPERATOR.EXACT),
            extensions.TierStyle(tier=categories.TIER.EPIC),
        ],
    ),
    rules.Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.MultiClass(class_names=armour_with_sockets),
            extensions.SocketGroup(sockets="5", operator=categories.OPERATOR.GTE),
            extensions.TierStyle(tier=categories.TIER.LEGENDARY),
        ],
    ),
    rules.Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.MultiClass(class_names=weapon_classes),
            extensions.TierStyle(tier=categories.TIER.RARE),
        ],
    ),
    rules.Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.ClassName(class_name="boots"),
            extensions.Rarity(
                rarity=categories.RARITY.MAGIC, operator=categories.OPERATOR.GTE
            ),
            extensions.TierStyle(tier=categories.TIER.RARE),
        ],
    ),
    rules.Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.BaseType(base_type="Iron Ring"),
            extensions.TierStyle(tier=categories.TIER.COMMON),
        ],
    ),
    rules.Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.MultiBaseType(base_types=rings_with_resistance),
            extensions.TierStyle(tier=categories.TIER.RARE),
        ],
    ),
    rules.Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.ClassName(class_name="Jewels"),
            extensions.TierStyle(tier=categories.TIER.RARE),
        ],
    ),
    rules.Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.Sockets(sockets="WWW", operator=categories.OPERATOR.GTE),
            extensions.TierStyle(tier=categories.TIER.LEGENDARY),
        ],
    ),
    *common.rules,
]
filter.generate(rules=rules, filter_name="leveling")
