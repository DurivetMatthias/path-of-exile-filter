from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *


class HELMET(StrEnum):
    ANY = "Any"
    IMPERIAL = "Imperial"
    IMPERIAL_RES = "Imperial with Resistance"
    CONSTRICTING_COMMAND = "Constricting Command"


active_rules = [
    HELMET.ANY,
    HELMET.IMPERIAL,
    HELMET.IMPERIAL_RES,
    HELMET.CONSTRICTING_COMMAND,
]


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

if HELMET.ANY in active_rules:
    rules.append(
        Show(
            [
                PureArmour(),
                Class("Helmets"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if HELMET.IMPERIAL in active_rules:
    rules.append(
        Show(
            [
                BaseType("Imperial Greathelm"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if HELMET.IMPERIAL_RES in active_rules:
    rules.append(
        Show(
            [
                ItemLevel(82),
                BaseType("Imperial Greathelm"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if HELMET.CONSTRICTING_COMMAND in active_rules:
    rules.append(
        Show(
            [
                BaseType("Viper Cap"),
                Rarity(RARITY.UNIQUE),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if HELMET.CONSTRICTING_COMMAND in active_rules:
    rules.append(
        Show(
            [
                BaseType("Viper Cap"),
                Rarity(RARITY.NORMAL),
                TierStyle(TIER.EPIC),
            ]
        )
    )
