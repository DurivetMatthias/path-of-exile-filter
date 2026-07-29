from app.blocks import *
from app.actions import *
from app.categories import *
from app.conditions import *

BEFORE_RF = 16
BEFORE_SIOSA = 30
BEFORE_MAPS = 67

rules = [
    # Sockets
    # Show(
    #     [
    #         MultiClass(["One Hand Maces"]),
    #         Sockets(3),  # Offhand Gem Leveling
    #         AreaLevel(24, OPERATOR.LTE),
    #         TierStyle(TIER.COMMON),
    #     ]
    # ),
    Show(
        [
            GearClasses(),  # Pick up anything for sockets early
            AreaLevel(5, OPERATOR.LTE),
        ]
    ),
    Show(
        [
            GearClasses(),
            PureArmour(),  # No links needed at this point
            AreaLevel(24, OPERATOR.LTE),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            GearClasses(),
            PureArmour(),  # Surely I'll find something with good sockets
            AreaLevel(BEFORE_MAPS, OPERATOR.LTE),
            Rarity(RARITY.RARE),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            Class("Body Armours"),
            LinkedSockets(5),
            AreaLevel(49, OPERATOR.LTE),
            AreaLevel(BEFORE_MAPS, OPERATOR.LTE),
            TierStyle(TIER.LEGENDARY),  # Finding the first 5-link is really strong
        ]
    ),
    Show(
        [
            Class("Body Armours"),
            LinkedSockets(6),
            AreaLevel(BEFORE_MAPS, OPERATOR.LTE),
            TierStyle(TIER.LEGENDARY),  # Finding the first 6-link is really strong
        ]
    ),
    # Bases
    Show(
        [
            MultiBaseType(["Jade Amulet", "Lapis Amulet", "Leather Belt", "Ruby Ring"]),
            AreaLevel(BEFORE_MAPS, OPERATOR.LTE),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            Class("Sceptres"),
            Rarity(RARITY.MAGIC),
            AreaLevel(59, OPERATOR.LTE),
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
