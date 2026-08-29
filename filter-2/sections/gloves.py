from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *


class GLOVES(StrEnum):
    ANY = "Any"
    MASSIVE = "Massive Mitts"
    MASSIVE_RES = "Massive Mitts with res"


active_rules = [
    GLOVES.ANY,
    GLOVES.MASSIVE,
    GLOVES.MASSIVE_RES,
]


rules = []

# Fallback Hide rule
rules.append(
    Hide([Class("Gloves")]),
)

# Show all during campaign
rules.append(
    Show(
        [
            InCampaign(),
            PureArmour(),
            Class("Gloves"),
            TierStyle(TIER.EPIC),
        ]
    )
)

if GLOVES.ANY in active_rules:
    rules.append(
        Show(
            [
                PureArmour(),
                Class("Gloves"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if GLOVES.MASSIVE in active_rules:
    rules.append(
        Show(
            [
                BaseType("Massive Mitts"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if GLOVES.MASSIVE_RES in active_rules:
    rules.append(
        Show(
            [
                ItemLevel(82),
                BaseType("Massive Mitts"),
                TierStyle(TIER.EPIC),
            ]
        )
    )
