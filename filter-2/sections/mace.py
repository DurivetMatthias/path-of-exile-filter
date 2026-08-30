from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *


class MACE(StrEnum):
    ANY = "Any"
    DAZE = "Fortified or Structured"
    DAZE_4 = "Fortified or Structured and +4"


active_rules = [
    # MACE.ANY,
    # MACE.DAZE,
    # MACE.DAZE_4,
]


rules = []

# Fallback Hide rule
rules.append(
    Hide([WeaponClasses()]),
)

# Show all during campaign
rules.append(
    Show(
        [
            InCampaign(),
            Class("One Hand Maces"),
            TierStyle(TIER.EPIC),
        ]
    )
)

if MACE.ANY in active_rules:
    rules.append(
        Show(
            [
                Class("One Hand Maces"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if MACE.DAZE in active_rules:
    rules.append(
        Show(
            [
                MultiBaseType(["Fortified Hammer", "Structured Hammer"]),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if MACE.DAZE_4 in active_rules:
    rules.append(
        Show(
            [
                ItemLevel(81),
                MultiBaseType(["Fortified Hammer", "Structured Hammer"]),
                TierStyle(TIER.EPIC),
            ]
        )
    )
