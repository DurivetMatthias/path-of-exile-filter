from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *
from sections.toggles import *

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

if RING_TOGGLES.ANY in active_ring_rules:
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

if RING_TOGGLES.GOOD_BASE in active_ring_rules:
    rules.append(
        Show(
            [
                Rarity(RARITY.MAGIC, OPERATOR.LTE),
                MultiBaseType(good_bases),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if RING_TOGGLES.RES in active_ring_rules:
    rules.append(
        Show(
            [
                ItemLevel(82),
                Rarity(RARITY.MAGIC, OPERATOR.LTE),
                MultiBaseType(good_bases),
                TierStyle(TIER.EPIC),
            ]
        )
    )
