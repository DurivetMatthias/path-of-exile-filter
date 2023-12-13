from app.build.common import (
    altered_bases,
    card,
    currency,
    essence,
    gem,
    heist,
    map,
    miscellaneous,
    quest,
    unique,
    veiled,
    vendor,
)

rules = [
    *altered_bases.rules,
    *card.rules,
    *currency.rules,
    *essence.rules,
    *gem.rules,
    *heist.rules,
    *map.rules,
    *miscellaneous.rules,
    *quest.rules,
    *unique.rules,
    *veiled.rules,
    *vendor.rules,
]
