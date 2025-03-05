from app.blocks import Show
from app.actions import TierStyle
from app.conditions import Sockets, LinkedSockets, SocketGroup
from app.categories import TIER

rules = [
    # Show(
    #     [
    #         SocketGroup("RGB"),
    #         TierStyle(TIER.EPIC),
    #     ],
    # ),
    # Show(
    #     [
    #         Sockets("6"),
    #         TierStyle(TIER.EPIC),
    #     ],
    # ),
    Show(
        [
            LinkedSockets(6),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
]
