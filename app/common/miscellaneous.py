from app import categories, extensions, items
from app.rules import Rule

hidden = [
    *items.PANTHEON,
    *items.LABYRINTH,
]
common = [
    *items.VAAL_FRAGMENTS,
    *items.MORTAL_FRAGMENTS,
    *items.RITUAL,
]
rare = [
    *items.HARVEST,
    *items.SANCTUM,
    *items.INCURSION,
    *items.DELIRIUM,
    *items.SCOUTING_REPORTS,
    *items.EXPEDITION,
    *items.INCUBATORS,
    *items.BREACH_SPLINTERS,
    *items.LEGION_SPLINTERS,
]
epic = [
    *items.DELVE,
    *items.TAINTED_CURRENCY,
    *items.SCARABS,
    *items.BLIGHT,
    *items.CATALYST,
    *items.AFFLICTION,
]
legendary = [
    *items.BREACH_BLESSINGS,
    *items.BREACHSTONES,
    *items.LEGION_EMBLEMS,
    *items.SHAPER_FRAGMENTS,
    *items.ELDER_FRAGMENTS,
    *items.UBER_ELDER_FRAGMENTS,
    *items.SIRUS_FRAGMENTS,
    *items.BOSSES,
    *items.MEMORIES,
    *items.KEYS,
]

rules = [
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type, fuzzy=True),
                extensions.TierStyle(tier=categories.TIER.LEGENDARY),
            ],
        )
        for base_type in legendary
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type, fuzzy=True),
                extensions.TierStyle(tier=categories.TIER.EPIC),
            ],
        )
        for base_type in epic
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type, fuzzy=True),
                extensions.TierStyle(tier=categories.TIER.RARE),
            ],
        )
        for base_type in rare
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type, fuzzy=True),
                extensions.TierStyle(tier=categories.TIER.COMMON),
            ],
        )
        for base_type in common
    ],
    *[
        Rule(
            instruction=extensions.Hide(),
            extensions=[
                extensions.BaseType(base_type=base_type, fuzzy=True),
            ],
        )
        for base_type in hidden
    ],
]
