from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *

rules = [
    # Quest items
    Show([Class("Quest Items"), TierStyle(TIER.EPIC)]),
    Show([Class("Instance Local Items"), TierStyle(TIER.EPIC)]),
    # Custom Styles
    Show(
        [
            MultiBaseType(
                ["Gnawed Collarbone", "Gnawed Jawbone", "Gnawed Rib", "Gnawed Cranium"]
            ),
            AbyssStyle(),
        ]
    ),
    # Other
    Show(
        [
            MultiBaseType(["Djinn Barya", "Inscribed Ultimatum"]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            MultiBaseType(["Gold Key", "Silver Key", "Bronze Key"]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            Class("Augment"),
            TierStyle(TIER.COMMON),
        ]
    ),
    # Essence
    Show(
        [
            BaseType("Lesser Essence", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            BaseType("Essence", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.COMMON),
        ]
    ),
    # ===========================
    # Runes of Aldur / Expedition
    # ===========================
    Show(
        [
            MultiBaseType(
                [
                    "Alloy",
                    "Flux",
                    "Ore",
                    "Crest",
                    "Saga",
                ],
                OPERATOR.CONTAINS,
            ),
            ExpeditionStyle(),
        ]
    ),
    Show(
        [
            MultiBaseType(["Verisium", "Expedition Logbook", "Shattered Triskelion"]),
            ExpeditionStyle(),
        ]
    ),
]
