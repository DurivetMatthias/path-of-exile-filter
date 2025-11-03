from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *


def level_to_stack_rule(area_level):
    if area_level < 68:
        return StackSize(1, OPERATOR.GTE)

    if area_level < 75:
        return StackSize(4, OPERATOR.GTE)

    return StackSize(8, OPERATOR.GTE)


show_scrolls = [
    Show(
        [
            AreaLevel(area_level, OPERATOR.LTE),
            MultiBaseType(
                [
                    SCROLL_OF_WISDOM,
                    PORTAL_SCROLL,
                ]
            ),
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
