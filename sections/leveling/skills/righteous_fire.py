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
            MultiClass(["One-handed Maces", "Sceptres"]),
            Sockets(3),  # Offhand Gem Leveling
            AreaLevel(BEFORE_SIOSA, OPERATOR.LTE),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            GearClasses(),
            # PureArmour(),  # Allow all bases for 3-link
            LinkedSockets(3),
            AreaLevel(24, OPERATOR.LTE),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            GearClasses(),
            PureArmour(),
            LinkedSockets(4),
            AreaLevel(34, OPERATOR.LTE),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            GearClasses(),
            PureArmour(),
            LinkedSockets(5),
            AreaLevel(49, OPERATOR.LTE),
            TierStyle(TIER.LEGENDARY),  # Finding the first 5-link is really strong
        ]
    ),
    Show(
        [
            GearClasses(),
            PureArmour(),
            LinkedSockets(6),
            TierStyle(TIER.LEGENDARY),  # Finding the first 6-link is really strong
        ]
    ),
    # Bases
    Show(
        [
            MultiBaseType(["Jade Amulet", "Lapis Amulet"]),
            AreaLevel(BEFORE_MAPS, OPERATOR.LTE),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            BaseType("Quartz Sceptre"),
            AreaLevel(40, OPERATOR.LTE),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            BaseType("Crystal Sceptre"),
            AreaLevel(59, OPERATOR.LTE),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            BaseType("Opal Sceptre"),
            AreaLevel(BEFORE_MAPS, OPERATOR.LTE),
            TierStyle(TIER.EPIC),
        ]
    ),
]
