from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *

bases = [
    "Heavy Belt",  # Headhunter
    "Utility Belt",  # Mageblood
]
chance_bases = []

rules = [
    Show([Rarity(RARITY.UNIQUE), TierStyle(TIER.EPIC)]),
]
rules.extend(
    Show([Rarity(RARITY.UNIQUE), TierStyle(TIER.LEGENDARY), BaseType(name)])
    for name in bases
)
rules.extend(
    Show([Rarity(RARITY.NORMAL), TierStyle(TIER.LEGENDARY), BaseType(name)])
    for name in chance_bases
)
