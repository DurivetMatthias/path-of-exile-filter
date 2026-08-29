from app.blocks import *
from app.styles import *
from app.actions import *
from app.conditions import *
from app.categories import *

bases = [
    "Heavy Belt",  # Headhunter
    "Utility Belt",  # Mageblood
    "Viper Cap",  # Constricting Command
    "Champion Cuirass",  # Brass Dome
    "Golden Charm",  # Rite of Passage
]

rules = [
    # Show([Rarity(RARITY.UNIQUE), TierStyle(TIER.EPIC)]),
]
rules.extend(
    Show([Rarity(RARITY.NORMAL), TierStyle(TIER.LEGENDARY), BaseType(name)])
    for name in bases
)
rules.extend(
    Show([Rarity(RARITY.UNIQUE), TierStyle(TIER.LEGENDARY), BaseType(name)])
    for name in bases
)
