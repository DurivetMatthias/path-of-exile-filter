import itertools

import rule
import categories


class EssenceStyle(rule.Rule):
    def label(self) -> categories.LABEL:
        return categories.LABEL.WHITE_ON_BLUE

    def icon_shape(self) -> categories.SHAPE:
        return categories.SHAPE.MOON


class Essence(EssenceStyle):
    def __init__(self, type: str, tier: str, **kwargs):
        name = f"{tier} Essence of {type}"
        essence_value = 0

        if type in ["Greed", "Dread", "Zeal"]:
            essence_value += 3
        if type in ["Hatred", "Anger", "Sorrow", "Rage", "Wrath", "Spite", "Envy"]:
            essence_value += 2
        if tier == "Deafening":
            essence_value += 3
        if type in "Shrieking":
            essence_value += 2

        if essence_value >= 5:
            rarity = categories.RARITY.LEGENDARY
        elif essence_value >= 3:
            rarity = categories.RARITY.EPIC
        elif essence_value >= 2:
            rarity = categories.RARITY.RARE
        else:
            rarity = categories.RARITY.COMMON

        super().__init__(name=name, rarity=rarity, **kwargs)

    def filter(self):
        return f"""
            BaseType "{self.name}"
        """


essence_tiers = [
    "Whispering",
    "Muttering",
    "Weeping",
    "Wailing",
    "Screaming",
    "Shrieking",
    "Deafening",
]

# https://www.poewiki.net/wiki/Essence
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
]

product = [
    *itertools.product(group_a, essence_tiers[0:]),
    *itertools.product(group_b, essence_tiers[1:]),
    *itertools.product(group_c, essence_tiers[2:]),
    *itertools.product(group_d, essence_tiers[3:]),
    *itertools.product(group_e, essence_tiers[4:]),
]

rules = [
    *[
        Essence(
            type=essence_type,
            tier=essence_tier,
        )
        for (essence_type, essence_tier) in product
    ],
    *[
        EssenceStyle(
            name=special_essence,
            rarity=categories.RARITY.LEGENDARY,
        )
        for special_essence in special_essences
    ],
]
