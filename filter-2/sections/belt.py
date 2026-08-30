from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *


class BELT(StrEnum):
    ANY = "Any"
    FINE = "Fine"
    FINE_RES = "Fine Resistance"
    UNIQUE = "Unique"


active_rules = [
    # BELT.ANY,
    # BELT.FINE,
    BELT.FINE_RES,
    BELT.UNIQUE,
]


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

if BELT.ANY in active_rules:
    rules.append(
        Show(
            [
                Class("Belts"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BELT.FINE in active_rules:
    rules.append(
        Show(
            [
                BaseType("Fine Belt"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BELT.FINE_RES in active_rules:
    rules.append(
        Show(
            [
                ItemLevel(82),
                BaseType("Fine Belt"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BELT.UNIQUE in active_rules:
    rules.append(
        Show(
            [
                MultiBaseType(["Heavy Belt", "Utility Belt"]),
                Rarity(RARITY.UNIQUE),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BELT.UNIQUE in active_rules:
    rules.append(
        Show(
            [
                MultiBaseType(["Heavy Belt", "Utility Belt"]),
                Rarity(RARITY.NORMAL),
                TierStyle(TIER.EPIC),
            ]
        )
    )
