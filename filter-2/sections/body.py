from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *
from sections.toggles import *

rules = []

# Fallback Hide rule
rules.append(
    Hide([Class("Body Armours")]),
)

# Show all during campaign
rules.append(
    Show(
        [
            InCampaign(),
            PureArmour(),
            Class("Body Armours"),
            TierStyle(TIER.EPIC),
        ]
    )
)

if BODY_TOGGLES.ANY in active_body_rules:
    rules.append(
        Show(
            [
                PureArmour(),
                Class("Body Armours"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BODY_TOGGLES.SOLDIER in active_body_rules:
    rules.append(
        Show(
            [
                BaseType("Soldier Cuirass"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BODY_TOGGLES.SOLDIER_RES in active_body_rules:
    rules.append(
        Show(
            [
                ItemLevel(82),
                BaseType("Soldier Cuirass"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BODY_TOGGLES.BRASS_DOME in active_body_rules:
    rules.append(
        Show(
            [
                BaseType("Champion Cuirass"),
                Rarity(RARITY.UNIQUE),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BODY_TOGGLES.BRASS_DOME in active_body_rules:
    rules.append(
        Show(
            [
                BaseType("Champion Cuirass"),
                Rarity(RARITY.NORMAL),
                TierStyle(TIER.EPIC),
            ]
        )
    )
