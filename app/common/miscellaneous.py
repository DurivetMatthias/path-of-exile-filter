from app import categories, extensions, items
from app.rules import Rule

hidden = [
    *items.INCUBATORS,
    *items.DELIRIUM,
    *items.RITUAL,
    *items.EXPEDITION,
]
common = [
    *items.BREACH_SPLINTERS,
    *items.LEGION_SPLINTERS,
    *items.INCURSION,
    *items.VAAL_FRAGMENTS,
    *items.MORTAL_FRAGMENTS,
    *items.SCOUTING_REPORTS,
]
rare = [
    *items.LABYRINTH,
    items.DIVINE_VESSEL,
    *items.DELVE,
    *items.HARVEST,
    *items.TAINTED_CURRENCY,
]
epic = [
    *items.SCARABS,
    *items.BLIGHT,
    *items.CATALYST,
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
                extensions.TierStyle(tier=categories.TIER.COMMON),
            ],
        )
        for base_type in common
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
                extensions.TierStyle(tier=categories.TIER.LEGENDARY),
            ],
        )
        for base_type in legendary
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
