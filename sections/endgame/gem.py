from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

exceptional_gems = [
    "Empower Support",
    "Enlighten Support",
    "Enhance Support",
]
rules = [
    Show([MultiBaseType(exceptional_gems), TierStyle(TIER.LEGENDARY)]),
    Show(
        [
            Class("Support Gems"),
            BaseType("Awakened", OPERATOR.CONTAINS),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            Class("Support Gems"),
            BaseType("Greater", OPERATOR.CONTAINS),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show([MultiBaseType(["Righteous Fire", "Fire Trap"])]),
    Hide([Class("Support Gems")]),
    Hide([Class("Skill Gems")]),
]
