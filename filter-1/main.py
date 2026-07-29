from app import filter
from sections.endgame import (
    altered_bases,
    card,
    currency,
    essence,
    gem,
    heist,
    hide_gear,
    jewels,
    map,
    scarabs,
    scrolls,
    unique,
)
from sections.endgame.skills import righteous_fire
from sections.leveling import flasks, vendor
from sections.leveling.skills import spectral_throw
from sections.leveling.skills import righteous_fire as leveling_rf

rules = [
    *vendor.rules,
    *spectral_throw.rules,
    *leveling_rf.rules,
    *righteous_fire.rules,
    *scrolls.rules,
    *altered_bases.rules,
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
    *hide_gear.rules,
]

filter.generate(rules=rules, filter_name="main")
