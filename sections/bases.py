from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

rules = [
    # Show(
    #     [
    #         ItemLevel(68),
    #         MultiBaseType(
    #             [
    #                 "Titan Greaves",
    #                 "Titan Gauntlets",
    #                 "Royal Burgonet",
    #                 "Eternal Burgonet",
    #             ]
    #         ),
    #         TierStyle(TIER.RARE),
    #     ]
    # ),
    Show(
        [
            ItemLevel(85),
            MultiBaseType(
                [
                    "Leviathan Gauntlets",
                    "Leviathan Greaves",
                ]
            ),
            TierStyle(TIER.RARE),
        ]
    ),
    Show(
        [
            ItemLevel(85),
            MultiBaseType(
                [
                    "Onyx Amulet",
                    "Turquoise Amulet",
                    "Enthalpic Ring",
                    # "Ruby Ring",
                    # "Leather Belt",
                ]
            ),
            TierStyle(TIER.RARE),
        ]
    ),
    Show(
        [
            ItemLevel(85),
            MultiBaseType(["Void Sceptre"]),
            TierStyle(TIER.RARE),
        ]
    ),
    Show(
        [
            MultiBaseType(["Scholar's Robe"]),
            TierStyle(TIER.RARE),
        ]
    ),
]
