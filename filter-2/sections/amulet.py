from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *


class AMULET(StrEnum):
    ANY = "Any"
    MELEE_LEVEL = "Melee Level"
    MELEE_LEVEL_AND_RES = "Melee level and resistances"


active_rules = [
    # AMULET.ANY,
    # AMULET.MELEE_LEVEL,
    AMULET.MELEE_LEVEL_AND_RES,
]


rules = []

# Fallback Hide rule
rules.append(
    Hide([Class("Amulets")]),
)

# Show all during campaign
rules.append(
    Show(
        [
            InCampaign(),
            Class("Amulets"),
            TierStyle(TIER.EPIC),
        ]
    )
)

if AMULET.ANY in active_rules:
    rules.append(
        Show(
            [
                Rarity(RARITY.RARE, OPERATOR.LTE),
                Class("Amulets"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

good_bases = [
    "Jade Amulet",
    "Amber Amulet",
    "Lapis Amulet",
    "Stellar Amulet",
    "Solar Amulet",
    "Bloodstone Amulet",
]

if AMULET.MELEE_LEVEL in active_rules:
    rules.append(
        Show(
            [
                Rarity(RARITY.RARE, OPERATOR.LTE),
                ItemLevel(75),
                MultiBaseType(good_bases),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if AMULET.MELEE_LEVEL_AND_RES in active_rules:
    rules.append(
        Show(
            [
                Rarity(RARITY.RARE, OPERATOR.LTE),
                ItemLevel(82),
                MultiBaseType(good_bases),
                TierStyle(TIER.EPIC),
            ]
        )
    )
