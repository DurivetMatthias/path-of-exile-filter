from app.blocks import Hide
from app.conditions import MultiClass, AreaLevel
from app.categories import OPERATOR

hidden_gear = [
    "Sceptres",
    "Wands",
    "One Hand Maces",
    "Two Hand Maces",
    "One Hand Swords",
    "Thrusting One Hand Swords",
    "Two Hand Swords",
    "One Hand Axes",
    "Two Hand Axes",
    "Daggers",
    "Rune Daggers",
    "Bows",
    "Quivers",
    "Shields",
    "Claws",
    "Staves",
    "Warstaves",
    "Gloves",
    "Helmets",
    "Boots",
    "Body Armours",
    "Amulets",
    "Rings",
    "Belts",
    "Tinctures",
]

hidden_flasks = ["Mana Flasks", "Hybrid Flasks", "Life Flasks", "Utility Flasks"]

rules = [
    Hide(
        [
            MultiClass(hidden_gear),
            AreaLevel(30, OPERATOR.GTE),
        ]
    ),
    Hide(
        [
            MultiClass(hidden_flasks),
            AreaLevel(30, OPERATOR.GTE),
        ]
    ),
]
