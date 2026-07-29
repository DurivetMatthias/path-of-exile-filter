from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *

rules = [
    Show(
        [
            MultiClass(["Uncut Skill Gems", "Uncut Spirit Gems", "Uncut Support Gems"]),
            TierStyle(TIER.COMMON),
        ]
    ),
]
