from app.blocks import *
from app.actions import *
from app.categories import *
from app.conditions import *


def level_to_stack_rule(area_level):
    if area_level < 68:
        return StackSize(1, OPERATOR.GTE)

    if area_level < 75:
        return StackSize(3, OPERATOR.GTE)

    return StackSize(10)


show_scrolls = [
    Show(
        [
            AreaLevel(area_level, OPERATOR.LTE),
            MultiBaseType(["Scroll of Wisdom", "Portal Scroll"]),
            TierStyle(TIER.COMMON),
            level_to_stack_rule(area_level),
        ]
    )
    for area_level in range(1, 100)
]
rules = [
    *show_scrolls,
    Hide([MultiBaseType(["Scroll of Wisdom", "Portal Scroll"])]),
]
