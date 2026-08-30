from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *


class BOOTS(StrEnum):
    ANY = "Any"
    TASALIAN = "Tasalian"
    FRACTURE = "Tasalian for fracturing"


active_rules = [
    # BOOTS.ANY,
    # BOOTS.TASALIAN,
    # BOOTS.FRACTURE,
]


rules = []

# Fallback Hide rule
rules.append(
    Hide([Class("Boots")]),
)

# Show early magic boots
rules.append(
    Show(
        [
            InActOne(),
            Rarity(RARITY.MAGIC, OPERATOR.GTE),
            MultiBaseType(
                [
                    "Rawhide Boots",
                    "Straw Sandals",
                    "Mail Sabatons",
                    "Padded Leggings",
                    "Frayed Shoes",
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
            Class("Boots"),
            TierStyle(TIER.EPIC),
        ]
    )
)

if BOOTS.ANY in active_rules:
    rules.append(
        Show(
            [
                PureArmour(),
                Class("Boots"),
                Rarity(RARITY.MAGIC, OPERATOR.LTE),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BOOTS.TASALIAN in active_rules:
    rules.append(
        Show(
            [
                BaseType("Tasalian Greaves"),
                Rarity(RARITY.MAGIC, OPERATOR.LTE),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BOOTS.FRACTURE in active_rules:
    rules.append(
        Show(
            [
                ItemLevel(82),
                BaseType("Tasalian Greaves"),
                TierStyle(TIER.EPIC),
            ]
        )
    )
