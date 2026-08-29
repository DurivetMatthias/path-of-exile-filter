from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *


class BOOTS(StrEnum):
    ANY = "Any"
    TASALIAN = "Tasalian"
    TASALIAN_MS = "Tasalian with 35% ms"


active_rules = [
    BOOTS.ANY,
    BOOTS.TASALIAN,
    BOOTS.TASALIAN_MS,
]


rules = []

# Fallback Hide rule
rules.append(
    Hide([Class("Boots")]),
)

# Show all during campaign
rules.append(
    Show(
        [
            InCampaign(),
            PureArmour(),
            Class("Boots"),
            TierStyle(TIER.EPIC),
        ]
    )
)

if BOOTS.ANY in active_rules:
    rules.append(
        Show(
            [
                PureArmour(),
                Class("Boots"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BOOTS.TASALIAN in active_rules:
    rules.append(
        Show(
            [
                BaseType("Tasalian Greaves"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BOOTS.TASALIAN_MS in active_rules:
    rules.append(
        Show(
            [
                ItemLevel(82),
                BaseType("Tasalian Greaves"),
                TierStyle(TIER.EPIC),
            ]
        )
    )
