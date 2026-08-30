from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *
from sections.toggles import *

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

if BOOTS_TOGGLES.ANY in active_boots_rules:
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

if BOOTS_TOGGLES.TASALIAN in active_boots_rules:
    rules.append(
        Show(
            [
                BaseType("Tasalian Greaves"),
                Rarity(RARITY.MAGIC, OPERATOR.LTE),
                TierStyle(TIER.EPIC),
            ]
        )
    )

if BOOTS_TOGGLES.FRACTURE in active_boots_rules:
    rules.append(
        Show(
            [
                ItemLevel(82),
                BaseType("Tasalian Greaves"),
                TierStyle(TIER.EPIC),
            ]
        )
    )
