from app.base_types import SCROLL_OF_WISDOM, PORTAL_SCROLL
from app.blocks import Show, Hide
from app.conditions import (
    AreaLevel,
    MultiBaseType,
    StackSize,
)
from app.actions import TierStyle
from app.categories import TIER, OPERATOR


def level_to_stack_rule(area_level):
    if area_level < 68:
        return StackSize(1, operator=OPERATOR.GTE)

    if area_level < 75:
        return StackSize(4, operator=OPERATOR.GTE)

    if area_level < 80:
        return StackSize(6, operator=OPERATOR.GTE)

    return StackSize(8, operator=OPERATOR.GTE)


show_scrolls = [
    Show(
        [
            AreaLevel(area_level, operator=OPERATOR.LTE),
            MultiBaseType([SCROLL_OF_WISDOM, PORTAL_SCROLL]),
            TierStyle(TIER.COMMON),
            level_to_stack_rule(area_level),
        ]
    )
    for area_level in range(1, 100)
]
hide_scrolls = [Hide([MultiBaseType([SCROLL_OF_WISDOM, PORTAL_SCROLL])])]
rules = [
    *show_scrolls,
    *hide_scrolls,
]
