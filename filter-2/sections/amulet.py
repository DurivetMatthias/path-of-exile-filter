from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *
from sections.toggles import *

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

if AMULET_TOGGLES.ANY in active_amulet_rules:
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

if AMULET_TOGGLES.MELEE_LEVEL in active_amulet_rules:
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

if AMULET_TOGGLES.MELEE_LEVEL_AND_RES in active_amulet_rules:
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
