from app.blocks import *
from app.actions import *
from app.categories import *
from app.conditions import *

rules = [
    # Show(
    #     [
    #         BaseType("Void Sceptre"),
    #         # Rarity(RARITY.RARE),
    #         ItemLevel(85),
    #         TierStyle(TIER.EPIC),
    #     ]
    # ),
    # Show(
    #     [
    #         MultiClass(["Helmets", "Gloves", "Boots"]),
    #         PureArmour(),
    #         Rarity(RARITY.RARE),
    #         TierStyle(TIER.EPIC),
    #     ]
    # ),
    Show(
        [
            MultiBaseType(
                ["Leviathan Greaves", "Leviathan Gauntlets", "Colossal Tower Shield"]
            ),
            # Rarity(RARITY.RARE),
            ItemLevel(85),
            TierStyle(TIER.EPIC),
        ]
    ),
    # Show(
    #     [
    #         MultiBaseType(
    #             [
    #                 "Amethyst Ring",
    #                 "Jade Amulet",
    #                 "Turquoise Amulet",
    #                 "Onyx Amulet",
    #                 # "Leather Belt",
    #             ]
    #         ),
    #         Rarity(RARITY.UNIQUE, OPERATOR.LT),
    #         ItemLevel(84),
    #         TierStyle(TIER.EPIC),
    #     ]
    # ),
    Show(
        [
            BaseType("Talisman", OPERATOR.CONTAINS),
            TierStyle(TIER.EPIC),
        ]
    ),
    # Show(
    #     [
    #         MultiBaseType(["Divine Life Flask"]),
    #         TierStyle(TIER.COMMON),
    #     ]
    # ),
    Show(
        [
            MultiBaseType(
                [
                    "Quicksilver Flask",
                    "Quartz Flask",
                    "Silver Flask",
                    "Granite Flask",
                ]
            ),
            # ItemLevel(80),
            ItemLevel(85),
            TierStyle(TIER.EPIC),
        ]
    ),
]
