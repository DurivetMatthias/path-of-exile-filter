from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *

shared_config = {
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
    # quality
    "Artificer's Orb": TIER.RARE,
    "Gemcutter's Prism": TIER.EPIC,
    # "Arcanist's Etcher": TIER.COMMON,
    "Armourer's Scrap": TIER.COMMON,
    # "Blacksmith's Whetstone": TIER.COMMON,
    "Glassblower's Bauble": TIER.COMMON,
    # Socket
    "Lesser Jeweller's Orb": TIER.EPIC,
    "Greater Jeweller's Orb": TIER.LEGENDARY,
    "Perfect Jeweller's Orb": TIER.LEGENDARY,
    # Tink
    "Orb of Chance": TIER.LEGENDARY,
    "Divine Orb": TIER.LEGENDARY,
    "Orb of Annulment": TIER.LEGENDARY,
    "Fracturing Orb": TIER.LEGENDARY,
    "Hinekora's Lock": TIER.LEGENDARY,
    "Mirror of Kalandra": TIER.LEGENDARY,
}

rules = []
rules.extend(
    Show([BaseType(currency), TierStyle(tier)])
    for currency, tier in shared_config.items()
)
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
                    "Blacksmith's Whetstone",
                    "Arcanist's Etcher",
                    "Artificer's Orb",
                    "Gemcutter's Prism",
                    "Armourer's Scrap",
                    "Glassblower's Bauble",
                ]
            )
        ]
    )
)
