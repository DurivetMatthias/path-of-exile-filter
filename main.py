from app.filter import generate
from app.sections import (
    altered_bases,
    bases,
    card,
    currency,
    essence,
    flasks,
    gem,
    heist,
    hide_gear,
    jewels,
    leveling,
    leveling_bases,
    map,
    scarabs,
    scrolls,
    unique,
    veiled,
    vendor,
)

rules = [
    *scrolls.rules,
    *vendor.rules,
    *leveling_bases.rules,
    *leveling.rules,
    *altered_bases.rules,
    *bases.rules,
    *card.rules,
    *currency.rules,
    *essence.rules,
    *flasks.rules,
    *gem.rules,
    *heist.rules,
    *jewels.rules,
    *map.rules,
    *scarabs.rules,
    *unique.rules,
    *veiled.rules,
    *hide_gear.rules,
]

generate(rules=rules, filter_name="main")
