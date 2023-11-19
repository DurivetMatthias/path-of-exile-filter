"""This file defines the rules for currency items."""

import rule
import categories


class Currency(rule.Rule):
    def label(self) -> categories.LABEL:
        return categories.LABEL.BLACK_ON_WHITE

    def icon_shape(self) -> categories.SHAPE:
        return categories.SHAPE.CIRCLE


# TODO stack size for chaos shards


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
    "Orb of Binding",
    "Enkindling Orb",
    "Instilling Orb",
    "Orb of Horizons",
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

common_eldritch_currencies = [
    "Lesser Eldritch Ichor",
    "Lesser Eldritch Ember",
]

rare_eldritch_currencies = [
    "Greater Eldritch Ichor",
    "Greater Eldritch Ember",
]

epic_eldritch_currencies = [
    "Grand Eldritch Ichor",
    "Grand Eldritch Ember",
]

legendary_eldritch_currencies = [
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
    *scrolls,
    *socket_currencies,
    *common_shards,
    *common_basic_currencies,
    *common_quality_currencies,
    *common_niche_currencies,
    *common_eldritch_currencies,
]

rare = [
    *rare_shards,
    *rare_basic_currencies,
    *rare_quality_currencies,
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
    *legendary_currencies,
    *legendary_eldritch_currencies,
]

rules = [
    *[
        Currency(
            name=name,
            rarity=categories.RARITY.LEGENDARY,
        )
        for name in legendary
    ],
    *[
        Currency(
            name=name,
            rarity=categories.RARITY.EPIC,
        )
        for name in epic
    ],
    *[
        Currency(
            name=name,
            rarity=categories.RARITY.RARE,
            strictness=categories.STRICTNESS.STRICT,
        )
        for name in rare
    ],
    *[
        Currency(
            name=name,
            rarity=categories.RARITY.COMMON,
            strictness=categories.STRICTNESS.LESS_STRICT,
        )
        for name in common
    ],
]
