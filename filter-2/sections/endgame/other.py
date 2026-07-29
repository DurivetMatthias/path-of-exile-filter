from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *

rules = [
    # Quest items
    Show([Class("Quest Items"), TierStyle(TIER.COMMON)]),
    Show([Class("Instance Local Items"), TierStyle(TIER.COMMON)]),
    # Custom Styles
    Show([Class("Omen"), RitualStyle()]),
    Show(
        [
            MultiBaseType(
                [
                    "Preserved Collarbone",
                    "Preserved Jawbone",
                    "Preserved Rib",
                    "Preserved Cranium",
                    "Ancient Collarbone",
                    "Ancient Jawbone",
                    "Ancient Rib",
                    "Altered Collarbone",
                ],
                OPERATOR.CONTAINS,
            ),
            AbyssStyle(),
        ]
    ),
    Show(
        [
            MultiBaseType(["Catalyst", "Breach Ring", "Wombgift"], OPERATOR.CONTAINS),
            BreachStyle(),
        ]
    ),
    Show([BaseType("Liquid", operator=OPERATOR.CONTAINS), DeliriumStyle()]),
    Show(
        [
            MultiBaseType(
                [
                    "Infuser",
                    "Vaal Siphoner",
                    "Vaal Cultivation Orb",
                    "Core Destabiliser",
                    "Architect's Orb",
                    "Orb of Extraction",
                    "Crystallised Corruption",
                ],
                OPERATOR.CONTAINS,
            ),
            VaalStyle(),
        ]
    ),
    # Other
    Show(
        [
            MultiBaseType(["Tablet"], OPERATOR.CONTAINS),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            ItemLevel(75),
            MultiBaseType(["Djinn Barya", "Inscribed Ultimatum"], OPERATOR.CONTAINS),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            MultiBaseType(["Gold Key", "Silver Key", "Bronze Key"]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show([MultiBaseType(["Splinter"], OPERATOR.CONTAINS), TierStyle(TIER.EPIC)]),
    Show(
        [
            MultiBaseType(["Reliquary Key"], OPERATOR.CONTAINS),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiBaseType(
                [
                    "Greater Iron Rune",
                    "Greater Desert Rune",
                    "Greater Storm Rune",
                    "Greater Glacial Rune",
                    "Greater Body Rune",
                ],
                OPERATOR.CONTAINS,
            ),
            TierStyle(TIER.RARE),
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
            BaseType("Greater Essence", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            BaseType("Perfect Essence", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            MultiBaseType(
                [
                    "Essence of Horror",
                    "Essence of Delirium",
                    "Essence of Insanity",
                    "Essence of Hysteria",
                    "Essence of the Abyss",
                    "Essence of the Breach",
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            Class("Map Fragments"),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            Class("Pinnacle Keys"),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    # Exceptional items
    Show(
        [
            Quality(21),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiClass(["Gloves", "Boots", "Helmets"]),
            Sockets(2),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiClass(["Body Armours"]),
            Sockets(3),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            OffhandClasses(),
            Sockets(2),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            TwoHandedWeaponClasses(),
            Sockets(3),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            OneHandedWeaponClasses(),
            Sockets(2),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    # ===========================
    # Runes of Aldur / Expedition
    # ===========================
    Show(
        [
            Class("Stackable Currency"),
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
