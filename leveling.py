"""
This file is intended to be changed often during leveling.
Add and remove rules depending on your current needs.
"""

from app import categories, common, extensions, filter, rules, hide

armour_with_sockets = ["Body Armours", "Helmets", "Gloves", "Boots"]
weapon_classes = ["Sceptres"]
rings_with_resistance = [
    "Ruby Ring",
    "Sapphire Ring",
    "Topaz Ring",
    "Two-Stone Ring",
    "Amethyst Ring",
]
offhand_gear = [
    "Claws",
    "Daggers",
    "One Hand Axes",
    "One Hand Maces",
    "Sceptres",
    "One Hand Swords",
    "Thrusting One Hand Swords",
    "Wands",
    "Shields",
]

rules = [
    # rules.Rule(
    #     instruction=extensions.Show(),
    #     extensions=[
    #         extensions.MultiClass(class_names=armour_with_sockets),
    #         extensions.SocketGroup(sockets="3", operator=categories.OPERATOR.EXACT),
    #         extensions.TierStyle(tier=categories.TIER.RARE),
    #     ],
    # ),
    # rules.Rule(
    #     instruction=extensions.Show(),
    #     extensions=[
    #         extensions.MultiClass(class_names=armour_with_sockets),
    #         extensions.SocketGroup(sockets="4", operator=categories.OPERATOR.EXACT),
    #         extensions.TierStyle(tier=categories.TIER.EPIC),
    #     ],
    # ),
    # rules.Rule(
    #     instruction=extensions.Show(),
    #     extensions=[
    #         extensions.MultiClass(class_names=armour_with_sockets),
    #         extensions.SocketGroup(sockets="5", operator=categories.OPERATOR.GTE),
    #         extensions.TierStyle(tier=categories.TIER.LEGENDARY),
    #     ],
    # ),
    # rules.Rule(
    #     instruction=extensions.Show(),
    #     extensions=[
    #         extensions.ClassName(class_name="boots"),
    #         extensions.Rarity(
    #             rarity=categories.RARITY.MAGIC, operator=categories.OPERATOR.GTE
    #         ),
    #         extensions.TierStyle(tier=categories.TIER.RARE),
    #     ],
    # ),
    # rules.Rule(
    #     instruction=extensions.Show(),
    #     extensions=[
    #         extensions.BaseType(base_type="Iron Ring"),
    #         extensions.TierStyle(tier=categories.TIER.COMMON),
    #     ],
    # ),
    # rules.Rule(
    #     instruction=extensions.Show(),
    #     extensions=[
    #         extensions.MultiBaseType(base_types=rings_with_resistance),
    #         extensions.TierStyle(tier=categories.TIER.RARE),
    #     ],
    # ),
    # rules.Rule(
    #     instruction=extensions.Show(),
    #     extensions=[
    #         extensions.ClassName(class_name="Jewels"),
    #         extensions.TierStyle(tier=categories.TIER.EPIC),
    #     ],
    # ),
    # rules.Rule(
    #     instruction=extensions.Show(),
    #     extensions=[
    #         extensions.Sockets(sockets="WWW", operator=categories.OPERATOR.GTE),
    #         extensions.MultiClass(class_names=offhand_gear),
    #         extensions.TierStyle(tier=categories.TIER.LEGENDARY),
    #     ],
    # ),
    # rules.Rule(
    #     instruction=extensions.Show(),
    #     extensions=[
    #         extensions.Sockets(sockets="GGG", operator=categories.OPERATOR.GTE),
    #         extensions.MultiClass(class_names=offhand_gear),
    #         extensions.TierStyle(tier=categories.TIER.LEGENDARY),
    #     ],
    # ),
    # rules.Rule(
    #     instruction=extensions.Show(),
    #     extensions=[
    #         extensions.Sockets(sockets="BBB", operator=categories.OPERATOR.GTE),
    #         extensions.MultiClass(class_names=offhand_gear),
    #         extensions.TierStyle(tier=categories.TIER.LEGENDARY),
    #     ],
    # ),
    # rules.Rule(
    #     instruction=extensions.Show(),
    #     extensions=[
    #         extensions.BaseType(base_type="Life Flask", fuzzy=True),
    #         extensions.TierStyle(tier=categories.TIER.RARE),
    #     ],
    # ),
    # rules.Rule(
    #     instruction=extensions.Show(),
    #     extensions=[
    #         extensions.MultiClass(class_names=weapon_classes),
    #         extensions.TierStyle(tier=categories.TIER.RARE),
    #     ],
    # ),
    # rules.Rule(
    #     instruction=extensions.Show(),
    #     extensions=[
    #         extensions.MultiClass(class_names=armour_with_sockets),
    #         extensions.TierStyle(tier=categories.TIER.EPIC),
    #     ],
    # ),
    # rules.Rule(
    #     instruction=extensions.Show(),
    #     extensions=[
    #         extensions.MultiClass(class_names=weapon_classes),
    #         extensions.TierStyle(tier=categories.TIER.EPIC),
    #     ],
    # ),
    # rules.Rule(
    #     instruction=extensions.Show(),
    #     extensions=[
    #         extensions.BaseType(base_type="Amethyst Ring"),
    #         extensions.TierStyle(tier=categories.TIER.EPIC),
    #     ],
    # ),
    *common.rules,
    *hide.rules,
]
filter.generate(rules=rules, filter_name="leveling")
