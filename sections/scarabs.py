from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

LEGENDARY = TIER.LEGENDARY
EPIC = TIER.EPIC

scarabs = {
    # Horny
    HORNED_SCARAB_OF_AWAKENING: LEGENDARY,
    # Ambush
    AMBUSH_SCARAB_OF_CONTAINMENT: LEGENDARY,
    AMBUSH_SCARAB: LEGENDARY,
}

legendary_scarabs = [scarab for scarab, tier in scarabs.items() if tier == LEGENDARY]
epic_scarabs = [scarab for scarab, tier in scarabs.items() if tier == EPIC]

rules = [
    Show(
        [
            MultiBaseType(legendary_scarabs),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            BaseType("Scarab", OPERATOR.CONTAINS),
            TierStyle(TIER.EPIC),
        ],
    ),
    Show(
        [
            BaseType("Allflame", OPERATOR.CONTAINS),
            TierStyle(TIER.EPIC),
        ],
    ),
]
