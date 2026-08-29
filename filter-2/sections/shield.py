from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *


class SHIELD(StrEnum):
    ANY = "Any"
    TAWHOAN = "Tawhoan Tower Shield"
    TAWHOAN_RES = "Tawhoan with res"


active_rules = [
    SHIELD.ANY,
    SHIELD.TAWHOAN,
    SHIELD.TAWHOAN_RES,
]


rules = []

# Fallback Hide rule
rules.append(
    Hide([OffhandClasses()]),
)

# Show all during campaign
rules.append(
    Show(
        [
            InCampaign(),
            PureArmour(),
            Class("Shields"),
            TierStyle(TIER.EPIC),
        ]
    )
)

if SHIELD.ANY in active_rules:
    rules.append(
        Show(
            [
                PureArmour(),
                Class("Shields"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if SHIELD.TAWHOAN in active_rules:
    rules.append(
        Show(
            [
                BaseType("Tawhoan Tower Shield"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if SHIELD.TAWHOAN_RES in active_rules:
    rules.append(
        Show(
            [
                ItemLevel(82),
                BaseType("Tawhoan Tower Shield"),
                TierStyle(TIER.EPIC),
            ]
        )
    )
