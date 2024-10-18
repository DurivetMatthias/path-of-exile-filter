from app.filter import generate
from app.blocks import Show
from app.conditions.standard import BaseType, ClassName, Rarity, SocketGroup
from app.conditions.compound import TierStyle, MultiClass
from app.categories import TIER, RARITY

rules = [
    Show(
        [
            BaseType("Ruby Ring"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            SocketGroup("rgb"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            ClassName("currency"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            MultiClass(["Skill Gems", "Support Gems"]),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            Rarity(RARITY.MAGIC),
            TierStyle(TIER.RARE),
        ]
    ),
    Show(
        [
            Rarity(RARITY.RARE),
            TierStyle(TIER.EPIC),
        ]
    ),
]

generate(rules=rules, filter_name="ruthless", is_ruthless=True)
