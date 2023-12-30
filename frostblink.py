from app import categories, extensions, filter, items
from app.rules import Rule

from app import common

all_item_classes = [
    "One Hand Axes",
    "Claws",
    "Thrusting One Hand Swords",
    "Staves",
    "One Hand Swords",
    "Sceptres",
    "One Hand Maces",
    "Daggers",
    "Abyss Jewels",
    "Rune Daggers",
    "Shields",
    "Warstaves",
    "Wands",
    "Two Hand Axes",
    "Two Hand Maces",
    "Two Hand Swords",
    "Hybrid Flasks",
    "Life Flasks",
    "Mana Flasks",
    "Boots",
    "Body Armours",
    "Gloves",
    "Helmets",
    "Amulets",
    "Rings",
    "Belts",
    "Bows",
    "Quivers",
    "Jewels",
    "Utility Flasks",
]

rules = [
    *common.rules,
    # Bronn's lithe chancing
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.BaseType(base_type="Cutthroat's Garb"),
            extensions.Rarity(
                rarity=categories.RARITY.NORMAL,
                operator=categories.OPERATOR.EQUAL,
            ),
            extensions.TierStyle(tier=categories.TIER.RARE),
        ],
    ),
    *[
        Rule(
            instruction=extensions.Hide(),
            extensions=[extensions.ClassName(class_name=class_name)],
        )
        for class_name in all_item_classes
    ],
]

filter.generate(rules=rules, filter_name="frostblink")
