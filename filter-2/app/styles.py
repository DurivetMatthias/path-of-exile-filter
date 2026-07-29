from app.actions import *


class VendorStyle(Condition):
    def __str__(self):
        return formatting.format_conditions(
            [
                PlayEffect(COLOR.YELLOW),
                MinimapIcon(SIZE.SMALL, COLOR.YELLOW, SHAPE.DIAMOND),
                SetFontSize(FONT_SIZE.LARGE),
            ]
        )


class AbyssStyle(Condition):
    def __str__(self):
        rgb = RGB.GREEN
        color = COLOR.GREEN
        return formatting.format_conditions(
            [
                PlayEffect(color),
                SetTextColor(RGB.WHITE),
                SetBorderColor(rgb),
                SetBackgroundColor(rgb),
                SetFontSize(FONT_SIZE.LARGE),
                MinimapIcon(SIZE.SMALL, color, SHAPE.RAINDROP),
                PlayAlertSound(BASIC_SOUND.ELECTRICITY, VOLUME.MEDIUM),
            ]
        )


class ExpeditionStyle(Condition):
    def __str__(self):
        rgb = RGB.BLUE
        color = COLOR.BLUE
        return formatting.format_conditions(
            [
                PlayEffect(color),
                SetTextColor(RGB.WHITE),
                SetBorderColor(rgb),
                SetBackgroundColor(rgb),
                SetFontSize(FONT_SIZE.LARGE),
                MinimapIcon(SIZE.SMALL, color, SHAPE.PENTAGON),
                PlayAlertSound(BASIC_SOUND.METRONOME, VOLUME.MEDIUM),
            ]
        )


class RitualStyle(Condition):
    def __str__(self):
        rgb = RGB.RED
        color = COLOR.RED
        return formatting.format_conditions(
            [
                PlayEffect(color),
                SetTextColor(RGB.WHITE),
                SetBorderColor(rgb),
                SetBackgroundColor(rgb),
                SetFontSize(FONT_SIZE.LARGE),
                MinimapIcon(SIZE.SMALL, color, SHAPE.TRIANGLE),
                PlayAlertSound(BASIC_SOUND.ROTATION, VOLUME.MEDIUM),
            ]
        )


class BreachStyle(Condition):
    def __str__(self):
        rgb = RGB.PURPLE
        color = COLOR.PURPLE
        return formatting.format_conditions(
            [
                PlayEffect(color),
                SetTextColor(RGB.WHITE),
                SetBorderColor(rgb),
                SetBackgroundColor(rgb),
                SetFontSize(FONT_SIZE.LARGE),
                MinimapIcon(SIZE.SMALL, color, SHAPE.HEXAGON),
                PlayAlertSound(BASIC_SOUND.NEEDLE, VOLUME.MEDIUM),
            ]
        )


class DeliriumStyle(Condition):
    def __str__(self):
        rgb = RGB.GREY
        color = COLOR.GREY
        return formatting.format_conditions(
            [
                PlayEffect(color),
                SetTextColor(RGB.WHITE),
                SetBorderColor(rgb),
                SetBackgroundColor(rgb),
                SetFontSize(FONT_SIZE.LARGE),
                MinimapIcon(SIZE.SMALL, color, SHAPE.SQUARE),
                PlayAlertSound(BASIC_SOUND.INVERTED_RIPPLE, VOLUME.MEDIUM),
            ]
        )


class VaalStyle(Condition):
    def __str__(self):
        rgb = RGB.RED
        color = COLOR.RED
        return formatting.format_conditions(
            [
                PlayEffect(color),
                SetTextColor(RGB.WHITE),
                SetBorderColor(rgb),
                SetBackgroundColor(rgb),
                SetFontSize(FONT_SIZE.LARGE),
                MinimapIcon(SIZE.SMALL, color, SHAPE.TRIANGLE),
                PlayAlertSound(BASIC_SOUND.PUNCH, VOLUME.MEDIUM),
            ]
        )
