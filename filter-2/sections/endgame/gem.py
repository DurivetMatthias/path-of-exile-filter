from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *

rules = [
    Show(
        [
            MultiClass(
                [
                    "Uncut Skill Gems",
                    "Uncut Spirit Gems",
                    "Uncut Support Gems",
                ]
            ),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            MultiClass(["Uncut Support Gems"]),
            BaseType("Level 5", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.COMMON),
        ]
    ),
    # 19+ uncut gems
    Show(
        [
            MultiClass(["Uncut Skill Gems", "Uncut Spirit Gems"]),
            BaseType("Level 19", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiClass(["Uncut Skill Gems", "Uncut Spirit Gems"]),
            BaseType("Level 20", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    # Lineage Support
    Show(
        [
            Class("Support Gems"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Hide([MultiClass(["Uncut Skill Gems", "Uncut Spirit Gems", "Uncut Support Gems"])]),
]
