from app.blocks import *
from app.styles import *
from app.actions import *
from app.conditions import *
from app.categories import *

bases = [
    "Heavy Belt",  # Headhunter
    "Utility Belt",  # Mageblood
    "Viper Cap",  # Constricting Command
]

rules = [
    Show([Rarity(RARITY.UNIQUE), TierStyle(TIER.EPIC)]),
    # Show everything while farming Viper Cap
    # Show([AreaLevel(40, OPERATOR.EXACT), BaseType("Gold", OPERATOR.NOT_EQUAL)]),
]
rules.extend(
    Show([Rarity(RARITY.NORMAL), TierStyle(TIER.LEGENDARY), BaseType(name)])
    for name in bases
)
rules.extend(
    Show([Rarity(RARITY.UNIQUE), TierStyle(TIER.LEGENDARY), BaseType(name)])
    for name in bases
)
