from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *
from sections.toggles import *

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

if MACE_TOGGLES.ANY in active_mace_rules:
    rules.append(
        Show(
            [
                Class("One Hand Maces"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if MACE_TOGGLES.DAZE in active_mace_rules:
    rules.append(
        Show(
            [
                MultiBaseType(["Fortified Hammer", "Structured Hammer"]),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if MACE_TOGGLES.DAZE_4 in active_mace_rules:
    rules.append(
        Show(
            [
                ItemLevel(81),
                MultiBaseType(["Fortified Hammer", "Structured Hammer"]),
                TierStyle(TIER.EPIC),
            ]
        )
    )
