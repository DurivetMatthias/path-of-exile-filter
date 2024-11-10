from app.base_types import SCROLL_OF_WISDOM, PORTAL_SCROLL
from app.blocks import Show, Hide
from app.conditions import (
    AreaLevel,
    MultiBaseType,
    StackSize,
)
from app.actions import TierStyle
from app.categories import TIER, OPERATOR


def level_to_stack_size(area_level):
    return area_level // 10


show_scrolls = [
    Show(
        [
            AreaLevel(area_level),
            MultiBaseType([SCROLL_OF_WISDOM, PORTAL_SCROLL]),
            TierStyle(TIER.COMMON),
            StackSize(level_to_stack_size(area_level)),
        ]
    )
    for area_level in range(10, 100, 10)
]
hide_scrolls = [
    Hide(
        [
            AreaLevel(area_level),
            MultiBaseType([SCROLL_OF_WISDOM, PORTAL_SCROLL]),
            StackSize(level_to_stack_size(area_level), operator=OPERATOR.LT),
        ]
    )
    for area_level in range(10, 100, 10)
]
rules = [
    *show_scrolls,
    *hide_scrolls,
]
