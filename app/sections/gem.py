from app.blocks import Show, Hide
from app.conditions.compound import MultiBaseType, TierStyle
from app.conditions.standard import ClassName, BaseType
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
            ClassName("Support Gems"),
            BaseType("Awakened", operator=OPERATOR.EQUAL),
        ],
    ),
    Hide(
        [
            ClassName("Support Gems"),
        ]
    ),
    Hide(
        [
            ClassName("Skill Gems"),
        ]
    ),
]
