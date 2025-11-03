from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

rules = [
    Show(
        [
            BaseType("Stone Axe"),
            AreaLevel(8, OPERATOR.LTE),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            BaseType("Jade Chopper"),
            AreaLevel(12, OPERATOR.LTE),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]
