from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *

rules = [
    Show(
        [
            AreaLevel(5),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            Class("One Hand Maces"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            Class("Talismans"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            Class("Shields"),
            PureArmour(),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(5),
            GearClasses(),
            ArmourAndHybrid(),
            TierStyle(TIER.RARE),
        ]
    ),
    Show(
        [
            GearClasses(),
            PureArmour(),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            JewelryClasses(),
            TierStyle(TIER.EPIC),
        ]
    ),
    # Hide the rest
    Hide([GearClasses()]),
    Hide([WeaponClasses()]),
    Hide([OffhandClasses()]),
    Hide([JewelryClasses()]),
]
