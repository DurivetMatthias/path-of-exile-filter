from app import categories, extensions
from app.rules import Rule

style_extensions = [
    extensions.Beam(color=categories.COLOR.YELLOW),
    extensions.Icon(
        color=categories.COLOR.YELLOW,
        shape=categories.SHAPE.CIRCLE,
        size=categories.SIZE.SMALL,
    ),
    extensions.Border(rgb=categories.RGB.YELLOW),
    extensions.FontSize(size=categories.FONT_SIZE.LARGE),
]

rules = [
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.VeiledPrefix(),
            *style_extensions,
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.VeiledSuffix(),
            *style_extensions,
        ],
    ),
]
