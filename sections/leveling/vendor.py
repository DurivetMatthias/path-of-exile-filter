from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *


class VendorStyle(Condition):
    def __str__(self):
        return formatting.format_conditions(
            [
                PlayEffect(COLOR.YELLOW),
                MinimapIcon(SIZE.SMALL, COLOR.YELLOW, SHAPE.DIAMOND),
                SetFontSize(FONT_SIZE.LARGE),
                SetBorderColor(RGB.YELLOW),
                SetTextColor(RGB.YELLOW),
            ]
        )


rules = [
    Show([AreaLevel(1, OPERATOR.EXACT), Rarity(RARITY.NORMAL), VendorStyle()]),
    Show([AreaLevel(16, OPERATOR.LTE), Rarity(RARITY.RARE), VendorStyle()]),
    Show([AreaLevel(16, OPERATOR.LTE), SocketGroup("RGB"), VendorStyle()]),
    Show(
        [
            AreaLevel(67, OPERATOR.LTE),
            Quality(),
            Class("Flasks"),
            VendorStyle(),
        ],
    ),
    Show([Sockets("6"), VendorStyle()]),
    Show([LinkedSockets("6"), VendorStyle()]),
    Show([BaseType("Amethyst Flask"), VendorStyle()]),
    Show([Class("Quest Items"), TierStyle(TIER.EPIC)]),
]
