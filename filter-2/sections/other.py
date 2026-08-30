from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *
from sections.toggles import *

rules = []

# Quest items
rules.append(Show([Class("Quest Items"), TierStyle(TIER.EPIC)]))
rules.append(Show([Class("Instance Local Items"), TierStyle(TIER.EPIC)]))

# Abyss
rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Collarbone",
                    "Jawbone",
                    "Rib",
                    "Cranium",
                    "Abyss Tablet",
                    "Omen of Light",
                    "Omen of Putrefaction",
                    "Omen of Abyssal Echoes",
                    "Omen of the Liege",
                    "Essence of the Abyss",
                    "Omen of the Sovereign",
                    "Omen of the Blackblooded",
                    "Omen of Dextral Necromancy",
                    "Omen of Sinistral Necromancy",
                    "Kulemak's Invitation",
                ],
                OPERATOR.CONTAINS,
            ),
            AbyssStyle(),
            MultiBaseType(["Tribal Bow"], OPERATOR.NOT_EQUAL),
        ]
    )
)

# Expedition
rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Ore",
                    "Flux",
                    "Saga",
                    "Alloy",
                    "Crest",
                    "Expedition Tablet",
                    "Expedition Logbook",
                    "Shattered Triskelion",
                ],
                OPERATOR.CONTAINS,
            ),
            MultiBaseType(["Crest Shield", "Explorer Armour"], OPERATOR.NOT_EQUAL),
            ExpeditionStyle(),
        ]
    )
)

# Ritual
rules.append(Show([Class("Omen", OPERATOR.CONTAINS), RitualStyle()]))
rules.append(
    Show(
        [
            MultiBaseType(
                [
                    # "Sacred Bloom",
                    "Ritual tablet",
                    "Head of the King",
                    "Call of the Shadows",
                    "An Audience with the King",
                ],
            ),
            RitualStyle(),
        ]
    )
)

# Breach
rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Wombgift",
                    "Catalyst",
                    "Breachstone",
                    "Breach Ring",
                    "Breach Tablet",
                    "Breachlord Sac",
                    "Breach Splinter",
                    "Essence of the Breach",
                ],
                OPERATOR.CONTAINS,
            ),
            BreachStyle(),
        ]
    )
)

# Delirium
rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Liquid",
                    "Delirium Tablet",
                    "Simulacrum",
                    "Simulacrum Splinter",
                ],
                OPERATOR.CONTAINS,
            ),
            DeliriumStyle(),
        ]
    )
)

# Vaal Temple
rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Infuser",
                    "Temple Tablet",
                    "Vaal Siphoner",
                    "Architect's Orb",
                    "Orb of Sacrifice",
                    "Orb of Extraction",
                    "Core Destabiliser",
                    "Atziri's Medallion",
                    "Vaal Cultivation Orb",
                    "Crystallised Corruption",
                ],
                OPERATOR.CONTAINS,
            ),
            VaalStyle(),
        ]
    )
)

# Tablet
rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Overseer Tablet",
                    "Irradiated Tablet",
                ]
            ),
            TierStyle(TIER.EPIC),
        ]
    )
)

# Trial
if OTHER_TOGGLES.CHAOS in active_other_rules:
    rules.append(
        Show(
            [
                ItemLevel(75),
                BaseType("Inscribed Ultimatum"),
                TierStyle(TIER.COMMON),
            ]
        )
    )
# Trial
if OTHER_TOGGLES.SEKHEMA in active_other_rules:
    rules.append(
        Show(
            [
                ItemLevel(75),
                BaseType("Djinn Barya"),
                TierStyle(TIER.COMMON),
            ]
        )
    )
rules.append(
    Show(
        [
            ItemLevel(75),
            MultiBaseType(["Djinn Barya", "Inscribed Ultimatum"]),
            TierStyle(TIER.COMMON),
        ]
    )
)
rules.append(
    Show(
        [
            MultiBaseType(["Gold Key", "Silver Key", "Bronze Key"]),
            TierStyle(TIER.COMMON),
        ]
    ),
)

# Core drop pool
rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Essence",
                    "Cryptic Key",
                    "Reliquary Key",
                ],
                OPERATOR.CONTAINS,
            ),
            TierStyle(TIER.EPIC),
        ]
    )
)
rules.append(Show([Class(["Pinnacle Keys"]), TierStyle(TIER.EPIC)]))

# Augment
rules.append(Hide([Class("Augment")]))
rules.append(
    Show(
        [
            InCampaign(),
            MultiBaseType(
                [
                    "Iron Rune",
                    "Desert Rune",
                    "Storm Rune",
                    "Glacial Rune",
                ]
            ),
            TierStyle(TIER.RARE),
        ]
    )
)


if OTHER_TOGGLES.BASIC_AUGMENT in active_other_rules:
    rules.append(
        Show(
            [
                MultiBaseType(
                    [
                        "Greater Iron Rune",
                        "Greater Desert Rune",
                        "Greater Storm Rune",
                        "Greater Glacial Rune",
                    ]
                ),
                TierStyle(TIER.EPIC),
            ]
        )
    )

rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Greater Rune of Alacrity",
                    "Farrul's Rune of the Chase",
                    "Farrul's Rune of the Hunt",
                    "Courtesan Mannan's Rune of Cruelty",
                    "Masterwork Rune",
                    "Idol of Sirrius",
                    "Bear Idol",
                    "Fox Idol",
                    "Raven-Touched Shard",
                    "Passion of Aldur",
                    "Aldur's Legacy",
                    "Ancient Rune of Shattering",
                    "Cadigan's Epiphany",
                    "Astrid's Creativity",
                    "Soul Core of Tacati",
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ]
    )
)

# Exceptional items
rules.append(
    Show(
        [
            MultiClass(["Gloves", "Boots", "Helmets"]),
            Sockets(2),
            TierStyle(TIER.LEGENDARY),
        ]
    )
)
rules.append(
    Show(
        [
            MultiClass(["Body Armours"]),
            Sockets(3),
            TierStyle(TIER.LEGENDARY),
        ]
    )
)
rules.append(
    Show(
        [
            OffhandClasses(),
            Sockets(2),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
)
rules.append(
    Show(
        [
            TwoHandedWeaponClasses(),
            Sockets(3),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
)
rules.append(
    Show(
        [
            OneHandedWeaponClasses(),
            Sockets(2),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
)

# Leveling
rules.append(
    Show(
        [
            InActOne(),
            Rarity(RARITY.RARE),
            Height(3),
            VendorStyle(),
        ]
    ),
)
