from app import categories, extensions, filter
from app.rules import Rule

from app.build import common


weapons = [
    "Short Bow",
    "Broadhead Arrow Quiver",
]

armour = [
    "Dragonscale Boots",
    "Full Dragonscale",
    "Nightmare Bascinet",
    "Dragonscale Gauntlets",
    "Vermillion Ring",
    "Amethyst Ring",
    "Marble Amulet",
    "Leather Belt",
    "Crimson Jewel",
]

flasks = [
    "Quartz Flask",
    "Amethyst Flask",
    "Granite Flask",
    "Jade Flask",
    "Quicksilver Flask",
]

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
]

rules = [
    *common.rules,
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.Beam(color=categories.COLOR.PINK),
                extensions.Icon(
                    color=categories.COLOR.PINK,
                    shape=categories.SHAPE.CIRCLE,
                    size=categories.SIZE.SMALL,
                ),
                extensions.Border(rgb=categories.RGB.PINK),
                extensions.Sound(
                    file=categories.SOUND_FILE.LILY_SNIFF,
                    volume=categories.VOLUME.MEDIUM,
                ),
                extensions.FontSize(size=categories.FONT_SIZE.LARGE),
            ],
        )
        for base_type in [*weapons, *armour, *flasks]
    ],
    *[
        Rule(
            instruction=extensions.Hide(),
            extensions=[extensions.ClassName(class_name=class_name)],
        )
        for class_name in all_item_classes
    ],
]

filter.generate(rules=rules, filter_name="explosive-arrow")
