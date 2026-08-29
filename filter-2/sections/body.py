from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *


class BODY(StrEnum):
    ANY = "Any"
    SOLDIER = "Soldier Cuirass"
    SOLDIER_RES = "Soldier with Resistance"
    BRASS_DOME = "Brass Dome"


active_rules = [
    BODY.ANY,
    BODY.SOLDIER,
    BODY.SOLDIER_RES,
    BODY.BRASS_DOME,
]


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

if BODY.ANY in active_rules:
    rules.append(
        Show(
            [
                PureArmour(),
                Class("Body Armours"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BODY.SOLDIER in active_rules:
    rules.append(
        Show(
            [
                BaseType("Solider Cuirass"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BODY.SOLDIER_RES in active_rules:
    rules.append(
        Show(
            [
                ItemLevel(82),
                BaseType("Solider Cuirass"),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BODY.BRASS_DOME in active_rules:
    rules.append(
        Show(
            [
                BaseType("Champion Cuirass"),
                Rarity(RARITY.UNIQUE),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BODY.BRASS_DOME in active_rules:
    rules.append(
        Show(
            [
                BaseType("Champion Cuirass"),
                Rarity(RARITY.NORMAL),
                TierStyle(TIER.EPIC),
            ]
        )
    )
