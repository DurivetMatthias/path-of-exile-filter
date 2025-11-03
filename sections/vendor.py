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
            ]
        )


rules = [
    # Show(
    #     [
    #         SocketGroup("RGB"),
    #         VendorStyle(),
    #     ],
    # ),
    # Show(
    #     [
    #         Sockets("6"),
    #         VendorStyle(),
    #     ],
    # ),
    Show(
        [
            LinkedSockets(6),
            VendorStyle(),
        ],
    ),
    Show(
        [
            Quality(),
            MultiClass(list(FLASK)),
            VendorStyle(),
        ],
    ),
]
