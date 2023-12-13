from app import categories, classes, extensions
from app.rules import Rule

rules = [
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.ClassName(class_name=classes.MAPS),
            extensions.Beam(color=categories.COLOR.RED),
            extensions.Icon(
                color=categories.COLOR.RED,
                shape=categories.SHAPE.CIRCLE,
                size=categories.SIZE.SMALL,
            ),
            extensions.Border(rgb=categories.RGB.RED),
            extensions.Sound(
                file=categories.SOUND_FILE.LILY_SNIFF,
                volume=categories.VOLUME.LOUD,
            ),
            extensions.FontSize(size=categories.FONT_SIZE.LARGE),
        ],
    ),
]
