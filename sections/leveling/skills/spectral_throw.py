from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *


class SpectralThrowStyle(Condition):
    def __str__(self):
        return formatting.format_conditions(
            [
                PlayEffect(COLOR.GREEN),
                SetTextColor(RGB.WHITE),
                SetFontSize(FONT_SIZE.LARGE),
                SetBackgroundColor(RGB.GREEN),
                SetBorderColor(RGB.WHITE),
            ]
        )


BEFORE_RF = 16
rules = [
    Show(
        [
            MultiBaseType(["Jade Chopper", "Tribal Maul"]),
            AreaLevel(12, OPERATOR.LTE),
            SpectralThrowStyle(),
        ]
    ),
    Show(
        [
            MultiBaseType(["Rustic Sash", "Iron Ring"]),
            AreaLevel(BEFORE_RF, OPERATOR.LTE),
            SpectralThrowStyle(),
        ]
    ),
]
