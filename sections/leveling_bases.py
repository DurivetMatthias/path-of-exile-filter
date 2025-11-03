from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

BEFORE_RF = 16
BEFORE_SIOSA = 30
BEFORE_MAPS = 67

rules = [
    # Sockets
    Show(
        [
            AreaLevel(BEFORE_RF, OPERATOR.LTE),
            MultiClass(["Body Armours", "Gloves", "Boots", "Helmets"]),
            SocketGroup("GG"),  # Spectral Throw + Volley
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF, OPERATOR.LTE),
            MultiClass(["Body Armours", "Gloves", "Boots", "Helmets", "Shields"]),
            SocketGroup("RRB"),  # Lifetap + Shield Charge + Frost Blink
            TierStyle(TIER.RARE),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF, OPERATOR.LTE),
            MultiClass(["Body Armours", "Gloves", "Boots", "Helmets", "Shields"]),
            SocketGroup("BBR"),  # RF + Combustion + Lifetap
            TierStyle(TIER.RARE),
        ]
    ),
    # Bases
    Show(
        [
            AreaLevel(BEFORE_RF, OPERATOR.LTE),
            BaseType("Rustic Sash"),
            TierStyle(TIER.RARE),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF, OPERATOR.LTE),
            MultiBaseType(["Jade Amulet", "Lapis Amulet"]),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_RF, OPERATOR.LTE),
            BaseType("Iron Ring"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(40, OPERATOR.LTE),
            BaseType("Quartz Sceptre"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(60, OPERATOR.LTE),
            BaseType("Crystal Sceptre"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS, OPERATOR.LTE),
            BaseType("Opal Sceptre"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS, OPERATOR.LTE),
            BaseType("Void Sceptre"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS, OPERATOR.LTE),
            BaseType("Amethyst Ring"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_SIOSA, OPERATOR.LTE),
            BaseType("Leather Belt"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_MAPS, OPERATOR.LTE),
            BaseType("Quicksilver Flask"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]
