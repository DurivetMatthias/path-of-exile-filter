from app import categories, common, extensions, filter, rules

all_common_item_classes = [
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
    *[
        rules.Rule(
            instruction=extensions.Hide(),
            extensions=[extensions.ClassName(class_name=class_name)],
        )
        for class_name in all_common_item_classes
    ],
]

filter.generate(rules=rules, filter_name="righteous_fire")
