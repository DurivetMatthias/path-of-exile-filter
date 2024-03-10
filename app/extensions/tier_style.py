from app import categories, extensions, formatting


class TierStyle(extensions.Extension):
    def __init__(self, *, tier: categories.TIER):
        super().__init__()
        self.tier = tier

    def __str__(self):
        # default for common
        color = categories.COLOR.WHITE
        rgb = categories.RGB.WHITE
        basic_sound = categories.BASIC_SOUND.ELECTRICITY
        volume = categories.VOLUME.QUIET

        if self.tier == categories.TIER.RARE:
            color = categories.COLOR.BLUE
            rgb = categories.RGB.BLUE
            basic_sound = categories.BASIC_SOUND.PUNCH
            volume = categories.VOLUME.MEDIUM

        if self.tier == categories.TIER.EPIC:
            color = categories.COLOR.PURPLE
            rgb = categories.RGB.PURPLE
            basic_sound = categories.BASIC_SOUND.GUN
            volume = categories.VOLUME.MEDIUM

        if self.tier == categories.TIER.LEGENDARY:
            color = categories.COLOR.ORANGE
            rgb = categories.RGB.ORANGE
            basic_sound = categories.BASIC_SOUND.TINK
            volume = categories.VOLUME.LOUD

        child_extensions = [
            extensions.Beam(color=color),
            extensions.Icon(
                color=color,
                shape=categories.SHAPE.CIRCLE,
                size=categories.SIZE.SMALL,
            ),
            extensions.Border(rgb=rgb),
            extensions.BasicSound(sound=basic_sound, volume=volume),
            extensions.FontSize(size=categories.FONT_SIZE.LARGE),
        ]

        return formatting.format_extensions(child_extensions)
