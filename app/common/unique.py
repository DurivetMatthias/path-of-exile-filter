from app import categories, extensions
from app.rules import Rule
from app.external_data.py.uniques import Unique, uniques

desirable_uniques = [
    # T0
    "Headhunter",
    "Mageblood",
    "Kalandra's Touch",
    "The Squire",
    "Rakiata's Dance",
    # T1
    "Abberath's Hooves",
    "Arakaali's Fang",
    "Defiance of Destiny",
    "Gruthkul's Pelt",
    "Ralakesh's Impatience",
    # T2
    "Aegis Aurora",
    "Ancestral Vision",
    "Astramentis",
    "Bloodnotch",
    "Death Rush",
    "Firesong",
    "Immutable Force",
    "Inspired Learning",
    "Intuitive Leap",
    "Lioneye's Fall",
    "Might of the Meek",
    "Seven-League Step",
    "Stormshroud",
    "Taste of Hate",
    "The Fourth Vow",
    "The Poet's Pen",
    "Unending Hunger",
    "Unnatural Instinct",
    "Utula's Hunger",
    "Witchbane",
    # T3
    "Asenath's Gentle Touch",
    "Berek's Respite",
    "Cloak of Flame",
    "Divination Distillate",
    "Dyadian Dawn",
    "Emberwake",
    "Heatshiver",
    "Lightning Coil",
    "Ming's Heart",
    "Profane Proxy",
    "Pyre",
    "Replica Dragonfangs Flight",
    "Tabula Rasa",
    "The Hungry Loop",
    "The Ivory Tower",
    # T4
    "Ambu's Charge",
    "Berek's Grip",
    "Berek's Pass",
    "Bronn's Lithe",
    "Eye of Malice",
    "Rise of the Phoenix",
    "Ventor's Gamble",
    # T5
    "Dying Breath",
    "Immortal Flesh",
    "Leer Cast",
    "Obliteration",
    "Southbound",
    # Other drops
    "Ashes of the Stars",
    "Brutal Restraint",
    "Contract: The Twins",
    "Darkness Enthroned",
    # "Dawnbreaker",
    "Elegant Hubris",
    "Forbidden Flame",
    "Forbidden Flesh",
    "Forbidden Shako",
    "Glorious Vanity",
    "Grand Spectrum",
    "Kingmaker",
    "Legacy of Fury",
    "Lethal Pride",
    "Megalomaniac",
    "Militant Faith",
    # "Nimis",
    "Oriath's End",
    # "Polaric Devastation",
    "Precursor's Emblem",
    "Skin of the Lords",
    "Skin of the Loyal",
    "Split Personality",
    # "The Adorned",
    # "The Devouring Diadem",
    "Watcher's Eye",
]


def match_by_name(unique: Unique):
    return unique.name in desirable_uniques


rules = [
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.Rarity(
                    rarity=categories.RARITY.UNIQUE,
                    operator=categories.OPERATOR.EQUAL,
                ),
                extensions.BaseType(base_type=unique.base_type),
                extensions.TierStyle(tier=categories.TIER.LEGENDARY),
            ],
        )
        for unique in filter(match_by_name, uniques)
    ],
]
