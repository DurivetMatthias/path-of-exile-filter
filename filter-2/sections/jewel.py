from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *

rules = []

# Fallback Hide rule
rules.append(Hide([Rarity(RARITY.RARE, OPERATOR.LTE), Class("Jewels")]))

# Show all in campaign
rules.append(
    Show(
        [
            InCampaign(),
            MultiBaseType(["Ruby", "Emerald", "Sapphire"]),
            TierStyle(TIER.EPIC),
        ]
    )
)

# Only Ruby in endgame
rules.append(
    Show(
        [
            InEndgame(),
            BaseType("Ruby"),
            TierStyle(TIER.EPIC),
        ]
    )
)

# Time-Lost Jewels
rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Time-Lost Ruby",
                    "Time-Lost Emerald",
                    "Time-Lost Sapphire",
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ]
    )
)

# Unique Jewels
rules.append(
    Show(
        [
            Class("Jewel"),
            Rarity(RARITY.UNIQUE),
            TierStyle(TIER.LEGENDARY),
        ]
    )
)
