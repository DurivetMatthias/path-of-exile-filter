from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *
from sections.toggles import *

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

if SHIELD_TOGGLES.ANY in active_shield_rules:
    rules.append(
        Show(
            [
                PureArmour(),
                Class("Shields"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if SHIELD_TOGGLES.TAWHOAN in active_shield_rules:
    rules.append(
        Show(
            [
                BaseType("Tawhoan Tower Shield"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if SHIELD_TOGGLES.TAWHOAN_RES in active_shield_rules:
    rules.append(
        Show(
            [
                ItemLevel(82),
                BaseType("Tawhoan Tower Shield"),
                TierStyle(TIER.EPIC),
            ]
        )
    )
