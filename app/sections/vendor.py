from app.blocks import Show
from app.conditions.standard import Sockets, SocketGroup
from app.conditions.compound import TierStyle
from app.categories import TIER

rules = [
    Show(
        [
            Sockets("6"),
            TierStyle(TIER.EPIC),
        ],
    ),
    Show(
        [
            SocketGroup("6"),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
]
