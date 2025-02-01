from app.base_types import *
from app.blocks import Show
from app.actions import TierStyle
from app.conditions import BaseType, MultiBaseType
from app.categories import TIER, OPERATOR

LEGENDARY = TIER.LEGENDARY
EPIC = TIER.EPIC

scarabs = {
    # Horny
    HORNED_SCARAB_OF_AWAKENING: LEGENDARY,
    # Ambush
    AMBUSH_SCARAB_OF_CONTAINMENT: LEGENDARY,
    AMBUSH_SCARAB: LEGENDARY,
    # Incursion
    INCURSION_SCARAB_OF_TIMELINES: LEGENDARY,
    # Beyond
    BEYOND_SCARAB_OF_RESURGENCE: LEGENDARY,
    BEYOND_SCARAB_OF_THE_INVASION: LEGENDARY,
    # Harvest
    HARVEST_SCARAB_OF_CORNUCOPIA: LEGENDARY,
    HARVEST_SCARAB_OF_DOUBLING: LEGENDARY,
    # Misc
    SCARAB_OF_MONSTROUS_LINEAGE: LEGENDARY,
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
            BaseType("Scarab", operator=OPERATOR.EQUAL),
            TierStyle(TIER.EPIC),
        ],
    ),
]
