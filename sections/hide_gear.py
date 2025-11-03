from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

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

rules = [
    Hide(
        [
            MultiClass(hidden_gear),
        ]
    ),
]
