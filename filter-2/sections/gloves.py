from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *
from sections.toggles import *

rules = []

# Fallback Hide rule
rules.append(
    Hide([Class("Gloves")]),
)


# Show early magic gloves
rules.append(
    Show(
        [
            InActOne(),
            Rarity(RARITY.MAGIC, OPERATOR.GTE),
            MultiBaseType(
                [
                    "Suede Bracers",
                    "Torn Gloves",
                    "Ringmail Gauntlets",
                    "Rope Cuffs",
                    "Gauze Wraps",
                ]
            ),
            TierStyle(TIER.EPIC),
        ]
    )
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

if GLOVES_TOGGLES.ANY in active_gloves_rules:
    rules.append(
        Show(
            [
                PureArmour(),
                Class("Gloves"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if GLOVES_TOGGLES.MASSIVE in active_gloves_rules:
    rules.append(
        Show(
            [
                BaseType("Massive Mitts"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if GLOVES_TOGGLES.MASSIVE_RES in active_gloves_rules:
    rules.append(
        Show(
            [
                ItemLevel(82),
                BaseType("Massive Mitts"),
                TierStyle(TIER.EPIC),
            ]
        )
    )
