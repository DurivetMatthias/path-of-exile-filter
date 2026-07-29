from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *

rules = [
    # Tiering up maps
    Show(
        [
            Class("Shields"),
            PureArmour(),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            Class("One Hand Maces"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            GearClasses(),
            PureArmour(),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            # Rarity(RARITY.NORMAL),
            MultiBaseType(
                [
                    "Ruby Ring",
                    "Sapphire Ring",
                    "Topaz Ring",
                    "Amethyst Ring",
                    "Prismatic Ring",
                    "Solar Amulet",
                    "Stellar Amulet",
                    "Lapis Amulet",
                    "Amber Amulet",
                    "Jade Amulet",
                    "Pearlescent Amulet",
                ]
            ),
            TierStyle(TIER.EPIC),
        ]
    ),
    # Just good magic bases
    Show(
        [
            # BaseType("Massive Mitts"),
            Class("Gloves"),
            PureArmour(),
            Rarity(RARITY.MAGIC, OPERATOR.LTE),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            # BaseType("Tasalian Greaves"),
            Class("Boots"),
            PureArmour(),
            Rarity(RARITY.MAGIC, OPERATOR.LTE),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            BaseType("Imperial Greathelm"),
            # Class("Helmets"),
            # PureArmour(),
            Rarity(RARITY.MAGIC, OPERATOR.LTE),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            MultiBaseType("Soldier Cuirass", "Warlord Cuirass"),
            # Class("Body Armours"),
            # PureArmour(),
            Rarity(RARITY.MAGIC, OPERATOR.LTE),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            BaseType("Tawhoan Tower Shield"),
            # Class("Shields"),
            # PureArmour(),
            Rarity(RARITY.MAGIC, OPERATOR.LTE),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            BaseType("Tawhoan Tower Shield"),
            UnidentifiedItemTier(),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            # MultiBaseType(
            #     [
            #         "Fortified Hammer",
            #         "Structured Hammer",
            #     ]
            # ),
            Class("One Hand Maces"),
            Rarity(RARITY.MAGIC, OPERATOR.LTE),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    # Just the perfect item levels
    Show(
        [
            ItemLevel(82),
            MultiClass(["Gloves", "Boots", "Helmets"]),
            PureArmour(),
            # Rarity(RARITY.MAGIC, OPERATOR.LTE),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    # Hide the rest
    Hide([GearClasses()]),
    Hide([WeaponClasses()]),
    Hide([OffhandClasses()]),
    Hide([JewelryClasses()]),
]
