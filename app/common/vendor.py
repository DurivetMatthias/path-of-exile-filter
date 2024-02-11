from app import categories, extensions
from app.rules import Rule

rules = [
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.SocketGroup(sockets="6", operator=categories.OPERATOR.GTE),
            extensions.TierStyle(tier=categories.TIER.LEGENDARY),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.Sockets(sockets="6", operator=categories.OPERATOR.GTE),
            extensions.Beam(color=categories.COLOR.GREY),
            extensions.FontSize(size=categories.FONT_SIZE.LARGE),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.SocketGroup(sockets="RGB", operator=categories.OPERATOR.GTE),
            extensions.Beam(color=categories.COLOR.GREY),
            extensions.FontSize(size=categories.FONT_SIZE.LARGE),
        ],
    ),
]
