import itertools

from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

HIDE = "Hide"
COMMON = "common"
RARE = "rare"
EPIC = "epic"
LEGENDARY = "legendary"


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

essences = {}
for essence_type, essence_tier in product:
    name = f"{essence_tier} Essence of {essence_type}"
    essence_value = 0

    if essence_tier == "Screaming":
        tier = RARE
    if essence_tier == "Shrieking":
        tier = EPIC
    if essence_tier == "Deafening":
        tier = LEGENDARY
    if essence_tier in ["Whispering", "Muttering", "Weeping", "Wailing"]:
        tier = COMMON

    essences[name] = tier

for name in special_essences:
    essences[name] = LEGENDARY

hidden = [name for (name, tier) in essences.items() if tier == HIDE]
common = [name for (name, tier) in essences.items() if tier == COMMON]
rare = [name for (name, tier) in essences.items() if tier == RARE]
epic = [name for (name, tier) in essences.items() if tier == EPIC]
legendary = [name for (name, tier) in essences.items() if tier == LEGENDARY]


rules = [
    # Hide(
    #     [
    #         MultiBaseType(hidden),
    #     ],
    # ),
    Show(
        [
            MultiBaseType(common),
            TierStyle(TIER.COMMON),
        ],
    ),
    Show(
        [
            MultiBaseType(rare),
            TierStyle(TIER.RARE),
        ],
    ),
    Show(
        [
            MultiBaseType(epic),
            TierStyle(TIER.EPIC),
        ],
    ),
    Show(
        [
            MultiBaseType(legendary),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
]
