from app import categories, classes, items, extensions
from app.rules import Rule

style_extensions = [
    extensions.Beam(color=categories.COLOR.GREEN),
    extensions.Icon(
        color=categories.COLOR.GREEN,
        shape=categories.SHAPE.CIRCLE,
        size=categories.SIZE.SMALL,
    ),
    extensions.Border(rgb=categories.RGB.GREEN),
]

rules = [
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=gem_name),
                extensions.TierStyle(tier=categories.TIER.LEGENDARY),
            ],
        )
        for gem_name in items.EXCEPTIONAL_GEMS
    ],
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.BaseType(base_type="Awakened", fuzzy=True),
            extensions.TierStyle(tier=categories.TIER.LEGENDARY),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.TransfiguredGem(),
            extensions.TierStyle(tier=categories.TIER.LEGENDARY),
        ],
    ),
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=gem_name),
                extensions.GemLevel(gem_level=20, operator=categories.OPERATOR.GTE),
                extensions.TierStyle(tier=categories.TIER.RARE),
            ],
        )
        for gem_name in items.FIRE_GEMS
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=gem_name),
                extensions.Quality(quality=1, operator=categories.OPERATOR.GTE),
                extensions.TierStyle(tier=categories.TIER.RARE),
            ],
        )
        for gem_name in items.FIRE_GEMS
    ],
    # Show gems on The Twilight Strand
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.ClassName(class_name=classes.GEMS, fuzzy=True),
            extensions.AreaLevel(area_level=1, operator=categories.OPERATOR.EXACT),
            extensions.TierStyle(tier=categories.TIER.COMMON),
        ],
    ),
    Rule(
        instruction=extensions.Hide(),
        extensions=[
            extensions.ClassName(class_name=classes.GEMS, fuzzy=True),
        ],
    ),
]
