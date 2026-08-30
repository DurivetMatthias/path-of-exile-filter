from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *
from sections.toggles import *

rules = []

# Fallback Hide rule
rules.append(
    Hide([Class("Belts")]),
)

# Show all during campaign
rules.append(
    Show(
        [
            InCampaign(),
            Class("Belts"),
            TierStyle(TIER.EPIC),
        ]
    )
)

if BELT_TOGGLES.ANY in active_belt_rules:
    rules.append(
        Show(
            [
                Class("Belts"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BELT_TOGGLES.FINE in active_belt_rules:
    rules.append(
        Show(
            [
                BaseType("Fine Belt"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BELT_TOGGLES.FINE_RES in active_belt_rules:
    rules.append(
        Show(
            [
                ItemLevel(82),
                BaseType("Fine Belt"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BELT_TOGGLES.UNIQUE in active_belt_rules:
    rules.append(
        Show(
            [
                MultiBaseType(["Heavy Belt", "Utility Belt"]),
                Rarity(RARITY.UNIQUE),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BELT_TOGGLES.UNIQUE in active_belt_rules:
    rules.append(
        Show(
            [
                MultiBaseType(["Heavy Belt", "Utility Belt"]),
                Rarity(RARITY.NORMAL),
                TierStyle(TIER.EPIC),
            ]
        )
    )
