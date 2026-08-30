from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *
from sections.toggles import *

rules = []

# Fallback Hide rule
rules.append(
    Hide([Class("Helmets")]),
)

# Show all during campaign
rules.append(
    Show(
        [
            InCampaign(),
            PureArmour(),
            Class("Helmets"),
            TierStyle(TIER.EPIC),
        ]
    )
)

if HELMET_TOGGLES.ANY in active_helmet_rules:
    rules.append(
        Show(
            [
                PureArmour(),
                Class("Helmets"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if HELMET_TOGGLES.IMPERIAL in active_helmet_rules:
    rules.append(
        Show(
            [
                BaseType("Imperial Greathelm"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if HELMET_TOGGLES.IMPERIAL_RES in active_helmet_rules:
    rules.append(
        Show(
            [
                ItemLevel(82),
                BaseType("Imperial Greathelm"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if HELMET_TOGGLES.CONSTRICTING_COMMAND in active_helmet_rules:
    rules.append(
        Show(
            [
                BaseType("Viper Cap"),
                Rarity(RARITY.UNIQUE),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if HELMET_TOGGLES.CONSTRICTING_COMMAND in active_helmet_rules:
    rules.append(
        Show(
            [
                BaseType("Viper Cap"),
                Rarity(RARITY.NORMAL),
                TierStyle(TIER.EPIC),
            ]
        )
    )
