from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *
from sections.toggles import *

rules = []

# Fallback Hide rule
rules.append(
    Hide([MultiClass(["Uncut Skill Gems", "Uncut Spirit Gems", "Uncut Support Gems"])])
)

# Drop-only gems
rules.append(
    Show(
        [
            MultiClass(["Support Gems", "Skill Gems"]),
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

# Toggles

if GEM_TOGGLES.SUPPORT in active_gem_rules:
    rules.append(
        Show(
            [
                Class("Uncut Support Gems"),
                BaseType("Level 5", operator=OPERATOR.CONTAINS),
                TierStyle(TIER.COMMON),
            ]
        ),
    )

if GEM_TOGGLES.ANY in active_gem_rules:
    rules.append(
        Show(
            [
                MultiClass(["Uncut Skill Gems", "Uncut Spirit Gems"]),
                TierStyle(TIER.COMMON),
            ]
        ),
    )

if GEM_TOGGLES._18 in active_gem_rules:
    rules.append(
        Show(
            [
                InEndgame(),
                MultiClass(["Uncut Skill Gems", "Uncut Spirit Gems"]),
                BaseType("Level 18", operator=OPERATOR.CONTAINS),
                TierStyle(TIER.LEGENDARY),
            ]
        ),
    )

if GEM_TOGGLES._19 in active_gem_rules:
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

if GEM_TOGGLES._20 in active_gem_rules:
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
