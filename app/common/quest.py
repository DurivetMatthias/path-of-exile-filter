from app import categories, classes, extensions
from app.rules import Rule

rules = [
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.ClassName(class_name=classes.QUEST),
            extensions.Beam(color=categories.COLOR.GREEN),
            extensions.Icon(
                color=categories.COLOR.GREEN,
                shape=categories.SHAPE.CIRCLE,
                size=categories.SIZE.SMALL,
            ),
            extensions.Border(rgb=categories.RGB.GREEN),
            extensions.Sound(
                file=categories.SOUND_FILE.LILY_SNIFF,
                volume=categories.VOLUME.LOUD,
            ),
            extensions.FontSize(size=categories.FONT_SIZE.LARGE),
        ],
    ),
]
