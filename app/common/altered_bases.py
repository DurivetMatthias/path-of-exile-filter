from app import categories, extensions, items
from app.rules import Rule


style_extensions = [
    extensions.Beam(color=categories.COLOR.CYAN),
    extensions.Icon(
        color=categories.COLOR.CYAN,
        shape=categories.SHAPE.CIRCLE,
        size=categories.SIZE.SMALL,
    ),
    extensions.Sound(
        file=categories.SOUND_FILE.LILY_BAM,
        volume=categories.VOLUME.MEDIUM,
    ),
    extensions.FontSize(size=categories.FONT_SIZE.LARGE),
]

rules = [
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.CorruptedImplicit(),
                *style_extensions,
            ],
        )
        for base_type in items.JEWELS
    ],
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.Fractured(),
            extensions.TierStyle(tier=categories.TIER.LEGENDARY),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.Synthesised(),
            *style_extensions,
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.Influenced(),
            *style_extensions,
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.ItemLevel(item_level=86, operator=categories.OPERATOR.GTE),
            *style_extensions,
        ],
    ),
    # Rule(
    #     instruction=extensions.Show(),
    #     extensions=[
    #         extensions.Sockets(sockets="WWW", operator=categories.OPERATOR.GTE),
    #         *style_extensions,
    #     ],
    # ),
]
