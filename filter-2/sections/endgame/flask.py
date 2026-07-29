from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *

rules = [
    Show(
        [
            # Rarity(RARITY.NORMAL),
            # ItemLevel(81),
            MultiBaseType(
                [
                    "Ultimate Mana Flask",
                    "Ultimate Life Flask",
                ]
            ),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            MultiBaseType(
                [
                    "Thawing Charm",
                    "Silver Charm",
                    "Staunching Charm",
                    "Dousing Charm",
                    "Antidote Charm",
                ]
            ),
            TierStyle(TIER.COMMON),
        ]
    ),
    Hide([MultiClass(["Life Flasks", "Mana Flasks", "Charms"])]),
]
