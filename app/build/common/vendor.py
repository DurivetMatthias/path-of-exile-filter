from app import categories, extensions
from app.rules import Rule

rules = [
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.SocketGroup(sockets="6", operator=categories.OPERATOR.GTE),
            extensions.Beam(color=categories.COLOR.ORANGE),
            extensions.Icon(
                color=categories.COLOR.ORANGE,
                shape=categories.SHAPE.CIRCLE,
                size=categories.SIZE.SMALL,
            ),
            extensions.Border(rgb=categories.RGB.ORANGE),
            extensions.Sound(
                file=categories.SOUND_FILE.LILY_WOMP, volume=categories.VOLUME.LOUD
            ),
            extensions.FontSize(size=categories.FONT_SIZE.LARGE),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.Sockets(sockets="6", operator=categories.OPERATOR.GTE),
            extensions.Beam(color=categories.COLOR.YELLOW),
            extensions.Icon(
                color=categories.COLOR.YELLOW,
                shape=categories.SHAPE.CIRCLE,
                size=categories.SIZE.SMALL,
            ),
            extensions.Border(rgb=categories.RGB.YELLOW),
            extensions.FontSize(size=categories.FONT_SIZE.LARGE),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.SocketGroup(sockets="RGB", operator=categories.OPERATOR.GTE),
            extensions.Beam(color=categories.COLOR.GREY),
            extensions.Icon(
                color=categories.COLOR.GREY,
                shape=categories.SHAPE.CIRCLE,
                size=categories.SIZE.SMALL,
            ),
            extensions.Border(rgb=categories.RGB.GREY),
            extensions.FontSize(size=categories.FONT_SIZE.LARGE),
        ],
    ),
]
