from app.blocks import *
from app.styles import *
from app.actions import *
from app.conditions import *
from app.categories import *

bases = [
    "Gold Ring",  # Ventor's Gamble
    "Heavy Belt",  # Headhunter
    "Utility Belt",  # Mageblood
    "Woven Focus",  # Threaded Light
    "Crimson Amulet",  # Idol of Uldurn
    "Topaz Ring",  # Call of the Brotherhood
]

rules = [
    Show([Rarity(RARITY.UNIQUE), TierStyle(TIER.EPIC)]),
]
rules.extend(
    Show([Rarity(RARITY.NORMAL), TierStyle(TIER.LEGENDARY), BaseType(name)])
    for name in bases
)
rules.extend(
    Show([Rarity(RARITY.UNIQUE), TierStyle(TIER.LEGENDARY), BaseType(name)])
    for name in bases
)
