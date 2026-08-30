from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *


class FLASK(StrEnum):
    ANY = "Any"
    GOOD_BASE = "Good base"
    GOOD_ILVL = "Good item level"
    UNIQUE = "Unique"


active_rules = [
    # FLASK.ANY,
    # FLASK.GOOD_BASE,
    FLASK.GOOD_ILVL,
    FLASK.UNIQUE,
]

rules = []

# Fallback Hide rule
rules.append(
    Hide([MultiClass(["Life Flasks", "Mana Flasks", "Charms"])]),
)

# Show all during campaign
rules.append(
    Show(
        [
            InCampaign(),
            MultiClass(["Life Flasks", "Mana Flasks", "Charms"]),
            TierStyle(TIER.COMMON),
        ]
    )
)

if FLASK.GOOD_BASE in active_rules:
    rules.append(
        Show(
            [
                InEndgame(),
                Rarity(RARITY.MAGIC, OPERATOR.LTE),
                MultiBaseType(
                    [
                        "Ultimate Life Flask",
                        "Ultimate Mana Flask",
                    ]
                ),
                TierStyle(TIER.COMMON),
            ]
        )
    )

if FLASK.GOOD_ILVL in active_rules:
    rules.append(
        Show(
            [
                ItemLevel(83),
                Rarity(RARITY.MAGIC, OPERATOR.LTE),
                MultiBaseType(["Ultimate Life Flask"]),
                TierStyle(TIER.LEGENDARY),
            ]
        )
    )

good_charms = [
    "Thawing Charm",
    "Silver Charm",
    "Staunching Charm",
    "Dousing Charm",
    "Antidote Charm",
]

if FLASK.GOOD_BASE in active_rules:
    rules.append(
        Show(
            [
                InEndgame(),
                MultiBaseType(good_charms),
                TierStyle(TIER.EPIC),
            ]
        ),
    )

if FLASK.GOOD_ILVL in active_rules:
    rules.append(
        Show(
            [
                ItemLevel(83),
                Rarity(RARITY.MAGIC, OPERATOR.LTE),
                MultiBaseType(good_charms),
                TierStyle(TIER.LEGENDARY),
            ]
        )
    )

if FLASK.UNIQUE in active_rules:
    rules.append(
        Show(
            [
                Rarity(RARITY.UNIQUE),
                MultiBaseType(
                    [
                        "Golden Charm",
                        "Antidote Charm",
                        "Silver Charm",
                    ]
                ),
                TierStyle(TIER.LEGENDARY),
            ]
        )
    )
