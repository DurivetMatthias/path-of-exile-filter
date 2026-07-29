from app import filter
from app.blocks import *
from app.styles import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    Show([BaseType("Gold"), StackSize(1000), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType("Gold"), StackSize(300), TierStyle(TIER.EPIC)]),
    Show([BaseType("Gold"), StackSize(100), TierStyle(TIER.COMMON)]),
    Show([MapTier(1, OPERATOR.GTE), TierStyle(TIER.EPIC)]),
    Show([MultiBaseType(["Tablet"], OPERATOR.CONTAINS), TierStyle(TIER.EPIC)]),
    Hide([]),
]

filter.generate(rules, name="goldfound")
