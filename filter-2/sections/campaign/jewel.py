from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *

rules = [
    Show(
        [
            MultiBaseType(["Ruby", "Emerald", "Sapphire"]),
            TierStyle(TIER.EPIC),
        ]
    ),
]
