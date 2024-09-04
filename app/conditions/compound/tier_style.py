from app.formatting import format_extensions
from app.categories import *
from app.conditions.base_class import Extension
from app.conditions.standard.beam import Beam
from app.conditions.standard.icon import Icon
from app.conditions.standard.border import Border
from app.conditions.standard.sound import Sound
from app.conditions.standard.font_size import FontSize


class TierStyle(Extension):
    def __init__(self, tier: TIER):
        super().__init__()
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
            Beam(color),
            Icon(SIZE.SMALL, color, SHAPE.CIRCLE),
            Border(rgb),
            Sound(basic_sound, volume),
            FontSize(FONT_SIZE.LARGE),
        ]

        return format_extensions(child_extensions)
