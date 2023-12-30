"""This file defines the rules for essences."""

import itertools

from app import categories, extensions
from app.rules import Rule


# https://www.poewiki.net/wiki/Essence
essence_tiers = [
    "Whispering",
    "Muttering",
    "Weeping",
    "Wailing",
    "Screaming",
    "Shrieking",
    "Deafening",
]
group_a = [
    "Greed",
    "Contempt",
    "Hatred",
    "Woe",
]
group_b = [
    "Fear",
    "Anger",
    "Torment",
    "Sorrow",
]
group_c = [
    "Rage",
    "Suffering",
    "Wrath",
    "Doubt",
]
group_d = [
    "Loathing",
    "Zeal",
    "Anguish",
    "Spite",
]
group_e = [
    "Scorn",
    "Envy",
    "Misery",
    "Dread",
]
special_essences = [
    "Essence of Insanity",
    "Essence of Horror",
    "Essence of Delirium",
    "Essence of Hysteria",
    "Remnant of Corruption",
]

product = [
    *itertools.product(group_a, essence_tiers[0:]),
    *itertools.product(group_b, essence_tiers[1:]),
    *itertools.product(group_c, essence_tiers[2:]),
    *itertools.product(group_d, essence_tiers[3:]),
    *itertools.product(group_e, essence_tiers[4:]),
]

essences = []
for essence_type, essence_tier in product:
    name = f"{essence_tier} Essence of {essence_type}"
    essence_value = 0
    if type in ["Greed", "Dread", "Zeal"]:
        essence_value += 3
    if type in ["Hatred", "Anger", "Sorrow", "Rage", "Wrath", "Spite", "Envy"]:
        essence_value += 2

    if essence_tier == "Screaming":
        essence_value += 1
    if essence_tier == "Shrieking":
        essence_value += 2
    if essence_tier == "Deafening":
        essence_value += 3

    tier = categories.TIER.COMMON
    if essence_value >= 5:
        tier = categories.TIER.LEGENDARY
    elif essence_value >= 3:
        tier = categories.TIER.EPIC
    elif essence_value >= 2:
        tier = categories.TIER.RARE

    essences.append(
        {
            "name": name,
            "tier": tier,
        }
    )

rules = [
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=essence["name"]),
                extensions.TierStyle(tier=essence["tier"]),
            ],
        )
        for essence in essences
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=name),
                extensions.TierStyle(tier=categories.TIER.LEGENDARY),
            ],
        )
        for name in special_essences
    ],
]
