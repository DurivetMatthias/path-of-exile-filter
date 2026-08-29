from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *

rules = []

# Fallback Hide rule
rules.append(
    Hide([MultiClass(["Uncut Skill Gems", "Uncut Spirit Gems", "Uncut Support Gems"])])
)

# Drop-only gems
rules.append(
    Show(
        [
            MultiClass(["Support Gems", "Spirit Gems", "Skill Gems"]),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
)

# Show all in campaign
rules.append(
    Show(
        [
            InCampaign(),
            MultiClass(["Uncut Skill Gems", "Uncut Spirit Gems", "Uncut Support Gems"]),
            TierStyle(TIER.COMMON),
        ]
    )
)

# Toggle as needed
rules.append(
    Show(
        [
            InEndgame(),
            Class("Uncut Support Gems"),
            BaseType("Level 5", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.COMMON),
        ]
    ),
)

# Toggle as needed
rules.append(
    Show(
        [
            InEndgame(),
            MultiClass(["Uncut Skill Gems", "Uncut Spirit Gems", "Uncut Support Gems"]),
            TierStyle(TIER.COMMON),
        ]
    ),
)

# Toggle as needed
rules.append(
    Show(
        [
            InEndgame(),
            MultiClass(["Uncut Skill Gems", "Uncut Spirit Gems"]),
            BaseType("Level 19", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
)

# Toggle as needed
rules.append(
    Show(
        [
            InEndgame(),
            MultiClass(["Uncut Skill Gems", "Uncut Spirit Gems"]),
            BaseType("Level 20", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
)
