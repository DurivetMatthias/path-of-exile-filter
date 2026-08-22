from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *

rules = [
    Show(
        [
            ItemLevel(79),
            # Rarity(RARITY.NORMAL),
            Rarity(RARITY.MAGIC, OPERATOR.LTE),
            # Rarity(RARITY.RARE, OPERATOR.LTE),
            MultiBaseType(
                [
                    "Ruby Ring",
                    "Sapphire Ring",
                    "Topaz Ring",
                    "Amethyst Ring",
                    "Prismatic Ring",
                    "Fine Belt",
                ]
            ),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            ItemLevel(75),
            # Rarity(RARITY.NORMAL),
            # Rarity(RARITY.MAGIC, OPERATOR.LTE),
            Rarity(RARITY.RARE, OPERATOR.LTE),
            MultiBaseType(
                [
                    "Jade Amulet",
                    "Amber Amulet",
                    "Lapis Amulet",
                    "Stellar Amulet",
                    "Bloodstone Amulet",
                ]
            ),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            ItemLevel(75),
            Class("Amulets"),
            UnidentifiedItemTier(),
            TierStyle(TIER.EPIC),
        ]
    ),
    # Show(
    #     [
    #         ItemLevel(75),  # +3 level of melee skills
    #         Rarity(RARITY.RARE, OPERATOR.LTE),
    #         Class("Amulet"),
    #         TierStyle(TIER.EPIC),
    #     ]
    # ),
    Show(
        [
            ItemLevel(81),  # +4 level of melee skills
            MultiBaseType(["Fortified Hammer", "Structured Hammer"]),
            Class("One Hand Maces"),
            # Rarity(RARITY.MAGIC, OPERATOR.LTE),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            ItemLevel(79),
            BaseType("Massive Mitts"),
            Class("Gloves"),
            PureArmour(),
            Rarity(RARITY.MAGIC, OPERATOR.LTE),
            # Rarity(RARITY.NORMAL, OPERATOR.LTE),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            ItemLevel(82),  # +35% movement speed
            BaseType("Tasalian Greaves"),
            Class("Boots"),
            PureArmour(),
            Rarity(RARITY.MAGIC, OPERATOR.LTE),
            TierStyle(TIER.EPIC),
        ]
    ),
    # Show(
    #     [
    #         ItemLevel(79),
    #         BaseType("Imperial Greathelm"),
    #         Class("Helmets"),
    #         PureArmour(),
    #         Rarity(RARITY.MAGIC, OPERATOR.LTE),
    #         TierStyle(TIER.EPIC),
    #     ]
    # ),
    Show(
        [
            ItemLevel(79),
            MultiBaseType(["Soldier Cuirass"]),
            Class("Body Armours"),
            PureArmour(),
            Rarity(RARITY.MAGIC, OPERATOR.LTE),
            TierStyle(TIER.EPIC),
        ]
    ),
    # Hide the rest
    Hide([GearClasses()]),
    Hide([WeaponClasses()]),
    Hide([OffhandClasses()]),
    Hide([JewelryClasses()]),
]
