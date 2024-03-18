from app import categories, extensions, items
from app.rules import Rule

common = [
    *items.PANTHEON,
    *items.LABYRINTH,
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
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.MultiBaseType(base_types=legendary, fuzzy=True),
            extensions.TierStyle(tier=categories.TIER.LEGENDARY),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.MultiBaseType(base_types=epic, fuzzy=True),
            extensions.TierStyle(tier=categories.TIER.EPIC),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.MultiBaseType(base_types=rare, fuzzy=True),
            extensions.TierStyle(tier=categories.TIER.RARE),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.MultiBaseType(base_types=common, fuzzy=True),
            extensions.TierStyle(tier=categories.TIER.COMMON),
        ],
    ),
]
