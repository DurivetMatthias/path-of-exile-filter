from app.blocks import Show
from app.conditions import (
    SocketGroup,
    LinkedSockets,
    AreaLevel,
    Rarity,
    Class,
    MultiClass,
)
from app.actions import TierStyle
from app.categories import TIER, RARITY, OPERATOR

BEFORE_RF = 16
BEFORE_SIOSA = 30
BEFORE_MAPS = 67


rules = [
    Show(
        [
            Class("Quest Items"),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS, operator=OPERATOR.LTE),
            Class("Currency"),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF, operator=OPERATOR.LTE),
            MultiClass(["Support Gems", "Skill Gems"]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF, operator=OPERATOR.LTE),
            Rarity(RARITY.MAGIC),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS, operator=OPERATOR.LTE),
            SocketGroup("bbbr"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS, operator=OPERATOR.LTE),
            SocketGroup("ggbb"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS, operator=OPERATOR.LTE),
            LinkedSockets(4),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS, operator=OPERATOR.LTE),
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
            AreaLevel(BEFORE_SIOSA, operator=OPERATOR.LTE),
            Rarity(RARITY.MAGIC),
            MultiClass(
                [
                    "Boots",
                ]
            ),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show([AreaLevel(BEFORE_RF, operator=OPERATOR.LTE)]),
]
