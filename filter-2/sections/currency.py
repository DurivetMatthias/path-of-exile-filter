from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *

baseline_config = {
    "Orb of Transmutation": TIER.RARE,
    "Greater Orb of Transmutation": TIER.EPIC,
    "Perfect Orb of Transmutation": TIER.LEGENDARY,
    "Orb of Augmentation": TIER.RARE,
    "Greater Orb of Augmentation": TIER.EPIC,
    "Perfect Orb of Augmentation": TIER.LEGENDARY,
    "Regal Orb": TIER.EPIC,
    "Greater Regal Orb": TIER.LEGENDARY,
    "Perfect Regal Orb": TIER.LEGENDARY,
    "Exalted Orb": TIER.EPIC,
    "Greater Exalted Orb": TIER.LEGENDARY,
    "Perfect Exalted Orb": TIER.LEGENDARY,
    "Chaos Orb": TIER.EPIC,
    "Greater Chaos Orb": TIER.LEGENDARY,
    "Perfect Chaos Orb": TIER.LEGENDARY,
    "Orb of Alchemy": TIER.EPIC,
    "Vaal Orb": TIER.EPIC,
    # Shard
    "Chance Shard": TIER.EPIC,
    # Socket
    "Perfect Jeweller's Orb": TIER.LEGENDARY,
    # Tink
    "Divine Orb": TIER.LEGENDARY,
    "Orb of Chance": TIER.LEGENDARY,
    "Fracturing Orb": TIER.LEGENDARY,
    "Orb of Annulment": TIER.LEGENDARY,
    "Hinekora's Lock": TIER.LEGENDARY,
    "Mirror of Kalandra": TIER.LEGENDARY,
}

# Baseline rules
rules = []
rules.extend(
    Show([BaseType(currency), TierStyle(tier)])
    for currency, tier in baseline_config.items()
)
# Scrolls of Wisdom
rules.append(
    Show(
        [
            AreaLevel(15, OPERATOR.LTE),
            BaseType("Scroll of Wisdom"),
            TierStyle(TIER.COMMON),
        ]
    )
)
# Gold
rules.append(
    Show(
        [
            AreaLevel(15, OPERATOR.LTE),
            BaseType("Gold"),
            TierStyle(TIER.COMMON),
        ]
    )
)
rules.append(
    Show(
        [
            AreaLevel(65, OPERATOR.LT),
            BaseType("Gold"),
            StackSize(100),
            TierStyle(TIER.COMMON),
        ]
    )
)
rules.append(
    Show(
        [
            AreaLevel(65, OPERATOR.LT),
            BaseType("Gold"),
            StackSize(1000),
            TierStyle(TIER.COMMON),
        ]
    )
)
# Always in campaign
rules.append(
    Show(
        [
            AreaLevel(65, OPERATOR.LT),
            MultiBaseType(
                [
                    "Artificer's Orb",
                    "Armourer's Scrap",
                    "Gemcutter's Prism",
                    "Glassblower's Bauble",
                    "Lesser Jeweller's Orb",
                    "Greater Jeweller's Orb",
                ]
            ),
            TierStyle(TIER.EPIC),
        ],
    )
)
# Toggle as needed
rules.append(
    Show(
        [
            MultiBaseType(
                [
                    "Artificer's Orb",
                    "Armourer's Scrap",
                    "Gemcutter's Prism",
                    "Glassblower's Bauble",
                    "Lesser Jeweller's Orb",
                    "Greater Jeweller's Orb",
                ]
            ),
            TierStyle(TIER.EPIC),
        ],
    )
)
# Fallback Hide rule
rules.append(
    Hide(
        [
            MultiBaseType(
                [
                    "Gold",
                    "Regal Shard",
                    "Scroll of Wisdom",
                    "Lesser Jeweller's Orb",
                    "Greater Jeweller's Orb",
                    "Artificer's Orb",
                    "Armourer's Scrap",
                    "Arcanist's Etcher",
                    "Gemcutter's Prism",
                    "Glassblower's Bauble",
                    "Blacksmith's Whetstone",
                ]
            )
        ]
    )
)
