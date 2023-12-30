from app import categories, extensions, formatting


class TierStyle(extensions.Extension):
    def __init__(self, *, tier: categories.TIER):
        super().__init__()
        self.tier = tier

    def __str__(self):
        # default for common
        color = categories.COLOR.WHITE
        rgb = categories.RGB.WHITE
        file = categories.SOUND_FILE.DISABLED
        volume = categories.VOLUME.QUIET

        if self.tier == categories.TIER.RARE:
            color = categories.COLOR.BLUE
            rgb = categories.RGB.BLUE
            file = categories.SOUND_FILE.LILY_AAH
            volume = categories.VOLUME.QUIET

        if self.tier == categories.TIER.EPIC:
            color = categories.COLOR.PURPLE
            rgb = categories.RGB.PURPLE
            file = categories.SOUND_FILE.LILY_BING
            volume = categories.VOLUME.MEDIUM

        if self.tier == categories.TIER.LEGENDARY:
            color = categories.COLOR.ORANGE
            rgb = categories.RGB.ORANGE
            file = categories.SOUND_FILE.LILY_WOMP
            volume = categories.VOLUME.LOUD

        child_extensions = [
            extensions.Beam(color=color),
            extensions.Icon(
                color=color,
                shape=categories.SHAPE.CIRCLE,
                size=categories.SIZE.SMALL,
            ),
            extensions.Border(rgb=rgb),
            extensions.Sound(file=file, volume=volume),
            extensions.FontSize(size=categories.FONT_SIZE.LARGE),
        ]

        return formatting.format_extensions(child_extensions)
