from app.blocks import Show
from app.conditions import SocketGroup, LinkedSockets, BaseType, AreaLevel
from app.actions import TierStyle
from app.categories import TIER, OPERATOR

rules = [
    Show(
        [
            AreaLevel(16),
            BaseType("Iron Ring"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(16),
            BaseType("Lapis Amulet"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(40),
            BaseType("Quartz Sceptre"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(60),
            BaseType("Crystal Sceptre"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(67),
            BaseType("Opal Sceptre"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(67),
            SocketGroup("bbbr"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(67),
            SocketGroup("ggbb"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(67),
            LinkedSockets(4),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(67),
            BaseType("Amethyst Ring"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(67),
            BaseType("Quicksilver Flask"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]
