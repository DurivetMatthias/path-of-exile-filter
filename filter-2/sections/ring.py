from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *


class RING(StrEnum):
    ANY = "Any"
    GOOD_BASE = "Good bases"
    RES = "Resistances"


active_rules = [
    RING.ANY,
    RING.GOOD_BASE,
    RING.RES,
]


rules = []

# Fallback Hide rule
rules.append(
    Hide([Class("Rings")]),
)

# Show all during campaign
rules.append(
    Show(
        [
            InCampaign(),
            Class("Rings"),
            TierStyle(TIER.EPIC),
        ]
    )
)

if RING.ANY in active_rules:
    rules.append(
        Show(
            [
                Class("Rings"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

good_bases = [
    "Ruby Ring",
    "Sapphire Ring",
    "Topaz Ring",
    "Amethyst Ring",
    "Prismatic Ring",
]

if RING.GOOD_BASE in active_rules:
    rules.append(
        Show(
            [
                MultiBaseType(good_bases),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if RING.RES in active_rules:
    rules.append(
        Show(
            [
                ItemLevel(82),
                MultiBaseType(good_bases),
                TierStyle(TIER.EPIC),
            ]
        )
    )
