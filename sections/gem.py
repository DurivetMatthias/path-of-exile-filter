from app.blocks import Show, Hide
from app.conditions import Class, BaseType, MultiBaseType
from app.actions import TierStyle
from app.categories import OPERATOR, TIER

exceptional_gems = [
    "Empower Support",
    "Enlighten Support",
    "Enhance Support",
]

rules = [
    Show(
        [
            MultiBaseType(exceptional_gems),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            Class("Support Gems"),
            BaseType("Awakened", operator=OPERATOR.EQUAL),
        ],
    ),
    Hide(
        [
            Class("Support Gems"),
        ]
    ),
    Hide(
        [
            Class("Skill Gems"),
        ]
    ),
]
