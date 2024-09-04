from app.base_types import *
from app.blocks import Show
from app.conditions.compound import MultiBaseType, TierStyle
from app.conditions.standard import BaseType
from app.categories import TIER, OPERATOR

LEGENDARY = TIER.LEGENDARY
EPIC = TIER.EPIC

scarabs = {
    # Horny
    HORNED_SCARAB_OF_AWAKENING: LEGENDARY,
    # Ambush
    AMBUSH_SCARAB_OF_CONTAINMENT: LEGENDARY,
    AMBUSH_SCARAB_OF_DISCERNMENT: LEGENDARY,
    AMBUSH_SCARAB: LEGENDARY,
    AMBUSH_SCARAB_OF_HIDDEN_COMPARTMENTS: LEGENDARY,
    # Misc
    SCARAB_OF_MONSTROUS_LINEAGE: LEGENDARY,
}

legendary_scarabs = [scarab for scarab, tier in scarabs.items() if tier == LEGENDARY]
epic_scarabs = [scarab for scarab, tier in scarabs.items() if tier == EPIC]

rules = [
    # Show(
    #     [
    #         MultiBaseType(epic_scarabs),
    #         TierStyle(TIER.EPIC),
    #     ],
    # ),
    Show(
        [
            MultiBaseType(legendary_scarabs),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            BaseType("Scarab", operator=OPERATOR.EQUAL),
            TierStyle(TIER.RARE),
        ],
    ),
]
