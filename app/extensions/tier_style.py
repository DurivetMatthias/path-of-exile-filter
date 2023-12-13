from app import categories, extensions, formatting


class TierStyle(extensions.Extension):
    def __init__(self, *, tier: categories.TIER):
        super().__init__()
        self.tier = tier

    def __str__(self):
        # default for common
        categories.COLOR = categories.COLOR.WHITE
        categories.RGB = categories.RGB.WHITE
        file = categories.SOUND_FILE.LILY_OOH
        categories.VOLUME = categories.VOLUME.QUIET

        if self.tier == categories.TIER.RARE:
            categories.COLOR = categories.COLOR.BLUE
            categories.RGB = categories.RGB.BLUE
            file = categories.SOUND_FILE.LILY_AAH
            categories.VOLUME = categories.VOLUME.QUIET

        if self.tier == categories.TIER.EPIC:
            categories.COLOR = categories.COLOR.PURPLE
            categories.RGB = categories.RGB.PURPLE
            file = categories.SOUND_FILE.LILY_BING
            categories.VOLUME = categories.VOLUME.MEDIUM

        if self.tier == categories.TIER.LEGENDARY:
            categories.COLOR = categories.COLOR.ORANGE
            categories.RGB = categories.RGB.ORANGE
            file = categories.SOUND_FILE.LILY_WOMP
            categories.VOLUME = categories.VOLUME.LOUD

        child_extensions = [
            extensions.Beam(color=categories.COLOR),
            extensions.Icon(
                color=categories.COLOR,
                shape=categories.SHAPE.CIRCLE,
                size=categories.SIZE.SMALL,
            ),
            extensions.Border(rgb=categories.RGB),
            extensions.Sound(file=file, volume=categories.VOLUME),
            extensions.FontSize(size=categories.FONT_SIZE.LARGE),
        ]

        return formatting.format_extensions(child_extensions)
