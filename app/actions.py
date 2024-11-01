from app.extention import Extension
from app.categories import *
from app.formatting import format_extensions


class PlayAlertSound(Extension):
    def __init__(
        self,
        sound: BASIC_SOUND,
        volume: VOLUME = VOLUME.MEDIUM,
    ):
        self.sound = sound
        self.volume = volume

    def __str__(self):
        return f"""
            PlayAlertSound {self.sound} {self.volume}
        """


class MinimapIcon(Extension):
    def __init__(
        self,
        size: SIZE,
        color: COLOR,
        shape: SHAPE,
    ):
        self.size = size
        self.color = color
        self.shape = shape

    def __str__(self):
        return f"""
            MinimapIcon {self.size} {self.color} {self.shape}
        """


class PlayEffect(Extension):
    def __init__(
        self,
        color: COLOR,
    ):
        self.color = color

    def __str__(self):
        return f"""
            PlayEffect {self.color}
        """


class SetBorderColor(Extension):
    def __init__(
        self,
        rgb: RGB,
    ):
        self.rgb = rgb

    def __str__(self):
        return f"""
            SetBorderColor {self.rgb}
        """


class SetFontSize(Extension):
    def __init__(
        self,
        size: FONT_SIZE,
    ):
        self.size = size

    def __str__(self):
        return f"""
            SetFontSize {self.size}
        """


class TierStyle(Extension):
    def __init__(self, tier: TIER):
        self.tier = tier

    def __str__(self):
        # default for common
        color = COLOR.WHITE
        rgb = RGB.WHITE
        basic_sound = BASIC_SOUND.ELECTRICITY
        volume = VOLUME.QUIET

        if self.tier == TIER.RARE:
            color = COLOR.BLUE
            rgb = RGB.BLUE
            basic_sound = BASIC_SOUND.PUNCH
            volume = VOLUME.MEDIUM

        if self.tier == TIER.EPIC:
            color = COLOR.PURPLE
            rgb = RGB.PURPLE
            basic_sound = BASIC_SOUND.GUN
            volume = VOLUME.MEDIUM

        if self.tier == TIER.LEGENDARY:
            color = COLOR.ORANGE
            rgb = RGB.ORANGE
            basic_sound = BASIC_SOUND.TINK
            volume = VOLUME.LOUD

        child_extensions = [
            PlayEffect(color),
            MinimapIcon(SIZE.SMALL, color, SHAPE.CIRCLE),
            SetBorderColor(rgb),
            PlayAlertSound(basic_sound, volume),
            SetFontSize(FONT_SIZE.LARGE),
        ]

        return format_extensions(child_extensions)
