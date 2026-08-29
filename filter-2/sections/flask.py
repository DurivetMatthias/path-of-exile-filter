from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *

rules = []

# Fallback Hide rule
rules.append(
    Hide([MultiClass(["Life Flasks", "Mana Flasks", "Charms"])]),
)

# Show all during campaign
rules.append(
    Show(
        [
            InCampaign(),
            MultiClass(["Life Flasks", "Mana Flasks", "Charms"]),
            TierStyle(TIER.COMMON),
        ]
    )
)

# Toggle as needed
rules.append(
    Show(
        [
            InEndgame(),
            Rarity(RARITY.MAGIC, OPERATOR.LTE),
            MultiBaseType(
                [
                    "Ultimate Life Flask",
                    "Ultimate Mana Flask",
                ]
            ),
            TierStyle(TIER.COMMON),
        ]
    )
)

# T1 reduced charges per use
rules.append(
    Show(
        [
            ItemLevel(83),
            Rarity(RARITY.MAGIC, OPERATOR.LTE),
            MultiBaseType(["Ultimate Life Flask"]),
            TierStyle(TIER.LEGENDARY),
        ]
    )
)

# Toggle as needed
rules.append(
    Show(
        [
            InEndgame(),
            MultiBaseType(
                [
                    "Thawing Charm",
                    "Silver Charm",
                    "Staunching Charm",
                    "Dousing Charm",
                    "Antidote Charm",
                ]
            ),
            TierStyle(TIER.EPIC),
        ]
    ),
)

# T1 reduced charges per use
rules.append(
    Show(
        [
            ItemLevel(83),
            Rarity(RARITY.MAGIC, OPERATOR.LTE),
            Class("Charms"),
            TierStyle(TIER.LEGENDARY),
        ]
    )
)
