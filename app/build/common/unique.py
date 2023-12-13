from app import categories, extensions
from app.rules import Rule

rules = [
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.Rarity(
                rarity=categories.RARITY.UNIQUE, operator=categories.OPERATOR.GTE
            ),
            extensions.Beam(color=categories.COLOR.ORANGE),
            extensions.Icon(
                color=categories.COLOR.ORANGE,
                shape=categories.SHAPE.CIRCLE,
                size=categories.SIZE.SMALL,
            ),
            extensions.Sound(
                file=categories.SOUND_FILE.LILY_SNIFF, volume=categories.VOLUME.LOUD
            ),
            extensions.FontSize(size=categories.FONT_SIZE.LARGE),
        ],
    ),
]
