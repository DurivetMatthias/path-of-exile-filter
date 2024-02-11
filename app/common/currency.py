from app import categories, extensions
from app.rules import Rule

common_shards = [
    "Scroll Fragment",
    "Binding Shard",
    "Engineer's Shard",
    "Horizon Shard",
    "Transmutation Shard",
    "Alchemy Shard",
]

rare_shards = [
    "Alteration Shard",
    "Ancient Shard",
    "Chaos Shard",
    "Regal Shard",
    "Harbinger's Shard",
]

epic_shards = [
    "Annulment Shard",
    "Exalted Shard",
]

legendary_shards = [
    "Fracturing Shard",
    "Mirror Shard",
]

scrolls = [
    "Portal Scroll",
    "Scroll of Wisdom",
]

common_basic_currencies = [
    "Orb of Transmutation",
    "Orb of Augmentation",
    "Orb of Chance",
]

rare_basic_currencies = [
    "Orb of Alchemy",
    "Orb of Alteration",
]

epic_basic_currencies = [
    "Chaos Orb",
    "Regal Orb",
]

common_niche_currencies = [
    "Enkindling Orb",
    "Orb of Horizons",
]

rare_niche_currencies = [
    "Instilling Orb",
]

epic_niche_currencies = [
    "Ancient Orb",
    "Harbinger's Orb",
    "Vaal Orb",
    "Blessed Orb",
]

common_quality_currencies = [
    "Blacksmith's Whetstone",
    "Armourer's Scrap",
]

rare_quality_currencies = [
    "Engineer's Orb",
    "Glassblower's Bauble",
    "Gemcutter's Prism",
]

epic_quality_currencies = [
    "Cartographer's Chisel",
]

socket_currencies = [
    "Jeweller's Orb",
    "Orb of Fusing",
    "Chromatic Orb",
    "Orb of Binding",
]

undo_currencies = [
    "Orb of Scouring",
    "Orb of Regret",
    "Orb of Unmaking",
]

sextant_currencies = [
    "Surveyor's Compass",
    "Charged Compass",
    "Awakened Sextant",
    "Elevated Sextant",
]

legendary_currencies = [
    "Veiled Chaos Orb",
    "Orb of Annulment",
    "Exalted Orb",
    "Divine Orb",
    "Mirror of Kalandra",
    "Sacred Orb",
    "Fracturing Orb",
]

rare_eldritch_currencies = [
    "Lesser Eldritch Ichor",
    "Lesser Eldritch Ember",
]

epic_eldritch_currencies = [
    "Greater Eldritch Ichor",
    "Greater Eldritch Ember",
]

legendary_eldritch_currencies = [
    "Grand Eldritch Ichor",
    "Grand Eldritch Ember",
    "Exceptional Eldritch Ichor",
    "Exceptional Eldritch Ember",
    "Eldritch Chaos Orb",
    "Eldritch Exalted Orb",
    "Eldritch Orb of Annulment",
    "Orb of Conflict",
    "Orb of Dominance",
    "Awakener's Orb",
    "Crusader's Exalted Orb",
    "Hunter's Exalted Orb",
    "Redeemer's Exalted Orb",
    "Warlord's Exalted Orb",
    "Crescent Splinter",
    "The Maven's Writ",
]

common = [
    *socket_currencies,
    *common_shards,
    *common_basic_currencies,
    *common_quality_currencies,
    *common_niche_currencies,
]

rare = [
    *rare_shards,
    *rare_basic_currencies,
    *rare_quality_currencies,
    *rare_niche_currencies,
    *rare_eldritch_currencies,
]

epic = [
    *epic_shards,
    *epic_basic_currencies,
    *epic_quality_currencies,
    *epic_niche_currencies,
    *epic_eldritch_currencies,
    *sextant_currencies,
    *undo_currencies,
]

legendary = [
    *legendary_shards,
    *legendary_currencies,
    *legendary_eldritch_currencies,
]

rules = [
    *[
        Rule(
            instruction=extensions.Hide(),
            extensions=[
                extensions.BaseType(base_type=base_type),
            ],
        )
        for base_type in [
            "Orb of Transmutation",
            "Blacksmith's Whetstone",
            "Orb of Binding",
            "Orb of Alchemy",
            "Orb of Augmentation",
            "Armourer's Scrap",
            "Scroll of wisdom",
            # "Portal Scroll",
            "Orb of Horizons",
            "Instilling Orb",
            "Enkindling Orb",
            *common_shards,
        ]
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.DefaultStyle(),
                extensions.FontSize(size=categories.FONT_SIZE.LARGE),
            ],
        )
        for base_type in scrolls
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.TierStyle(tier=categories.TIER.COMMON),
            ],
        )
        for base_type in common
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.TierStyle(tier=categories.TIER.RARE),
            ],
        )
        for base_type in rare
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.TierStyle(tier=categories.TIER.EPIC),
            ],
        )
        for base_type in epic
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.TierStyle(tier=categories.TIER.LEGENDARY),
            ],
        )
        for base_type in legendary
    ],
]
