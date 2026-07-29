from app.blocks import *
from app.actions import *
from app.categories import *
from app.conditions import *

rules = [
    Show(
        [
            MultiBaseType(
                [
                    "Ambush Scarab",
                    "Ambush Scarab of Hidden Compartments",
                    "Ambush Scarab of Potency",
                    "Ambush Scarab of Discernment",
                    "Ambush Scarab of Containment",
                    # =================
                    "Domination Scarab",
                    "Domination Scarab of Apparitions",
                    "Domination Scarab of Evolution",
                    "Domination Scarab of Terrors",
                    # =================
                    "Cartography Scarab of Escalation",
                    "Cartography Scarab of Corruption",
                    "Cartography Scarab of the Multitude",
                    # =================
                    "Influencing Scarab of Interference",
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            BaseType("Scarab", OPERATOR.CONTAINS),
            TierStyle(TIER.EPIC),
        ],
    ),
]
