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
from app.categories import TIER, RARITY

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
            AreaLevel(BEFORE_RF),
            Class("Currency"),
            TierStyle(TIER.RARE),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF),
            MultiClass(["Support Gems", "Skill Gems"]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF),
            Rarity(RARITY.MAGIC),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS),
            SocketGroup("bbbr"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS),
            SocketGroup("ggbb"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS),
            LinkedSockets(4),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS),
            Rarity(RARITY.RARE),
            MultiClass(
                [
                    "Helmets",
                    "Gloves",
                    "Boots",
                    "Body Armours",
                    "Sceptres",
                    "Shields",
                    "Rings",
                    "Amulets",
                    "Belts",
                ]
            ),
            TierStyle(TIER.COMMON),
        ]
    ),
    # TODO life flasks
]
