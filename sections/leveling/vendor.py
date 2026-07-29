from app.blocks import *
from app.actions import *
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
    Show([AreaLevel(1, OPERATOR.EXACT), TierStyle(TIER.COMMON)]),
    Show([AreaLevel(16, OPERATOR.LTE), Rarity(RARITY.RARE), VendorStyle()]),
    Show([AreaLevel(16, OPERATOR.LTE), SocketGroup("RGB"), VendorStyle()]),
    Show(
        [
            AreaLevel(67, OPERATOR.LTE),
            Quality(),
            MultiClass(
                [
                    "Life Flasks",
                    "Mana Flasks",
                    "Hybrid Flasks",
                    "Utility Flasks",
                ]
            ),
            VendorStyle(),
        ],
    ),
    Show([AreaLevel(67, OPERATOR.LTE), Sockets("6"), VendorStyle()]),
    # Show([LinkedSockets("6"), VendorStyle()]),
    Show([MultiBaseType(["Amethyst Flask", "Quicksilver Flask"]), VendorStyle()]),
    Show([AreaLevel(16, OPERATOR.LTE), BaseType("Gold")]),
    Show([AreaLevel(67, OPERATOR.LTE), StackSize(100), BaseType("Gold")]),
    Show([StackSize(1000), BaseType("Gold")]),
    Show(
        [
            MultiClass(["Quest Items", "Atlas Upgrade Items"]),
            BaseType("Contract", OPERATOR.NOT_EQUAL),
            TierStyle(TIER.EPIC),
        ]
    ),
]
