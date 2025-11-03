from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

BEFORE_RF = 16
BEFORE_SIOSA = 30
BEFORE_MAPS = 67


rules = [
    Show(
        [
            Class("Quest Items"),
            BaseType("Contract", OPERATOR.NOT_EQUAL),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(1, OPERATOR.CONTAINS),
        ]
    ),
    Show(
        [
            AreaLevel(6, OPERATOR.LTE),
            BaseType("Gold"),
        ]
    ),
    Show(
        [
            AreaLevel(6, OPERATOR.LTE),
            MultiClass(["Boots", "Gloves", "Helmets", "Body Armours"]),
        ]
    ),
    Show(
        [
            AreaLevel(6, OPERATOR.LTE),
            Rarity(RARITY.MAGIC),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF, OPERATOR.LTE),
            Rarity(RARITY.RARE),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS, OPERATOR.LTE),
            Class("Currency"),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF, OPERATOR.LTE),
            MultiClass(["Support Gems", "Skill Gems"]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS, OPERATOR.LTE),
            SocketGroup("bbbr"),
            TierStyle(TIER.LEGENDARY),
            MultiClass(["Helmets", "Gloves", "Body Armours"]),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS, OPERATOR.LTE),
            SocketGroup("ggbb"),
            TierStyle(TIER.LEGENDARY),
            MultiClass(["Helmets", "Gloves", "Body Armours"]),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS, OPERATOR.LTE),
            LinkedSockets(4),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS, OPERATOR.LTE),
            Rarity(RARITY.RARE),
            MultiClass(
                [
                    "Helmets",
                    "Gloves",
                    "Body Armours",
                    "Sceptres",
                    "Shields",
                ]
            ),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_SIOSA, OPERATOR.LTE),
            Rarity(RARITY.MAGIC),
            MultiClass(
                [
                    "Boots",
                ]
            ),
            TierStyle(TIER.EPIC),
        ]
    ),
]
