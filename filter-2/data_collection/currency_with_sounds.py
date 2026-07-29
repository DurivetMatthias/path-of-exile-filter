from app.blocks import *
from app.styles import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = []

for area_level in range(1, 100):
    rules.append(
        Show(
            [
                AreaLevel(area_level, operator=OPERATOR.EXACT),
                ItemLevel(area_level + 1, operator=OPERATOR.EXACT),
                CustomAlertSound("rare_monster_indicator.wav"),
                SetBackgroundColor(RGB.RED),
                SetFontSize(1),  # as small as possible
                MinimapIcon(SIZE.LARGE, COLOR.RED, SHAPE.CIRCLE),
            ]
        ),
    )

for item in list(CURRENCY):
    rules.append(
        Show(
            [
                BaseType(item),
                CustomAlertSound(f"{item}.wav"),
                SetBackgroundColor(RGB.WHITE),
                SetFontSize(FONT_SIZE.LARGE),
            ]
        ),
    )
