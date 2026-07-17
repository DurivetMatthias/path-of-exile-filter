from enum import StrEnum

from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *


class RULE(StrEnum):
    HIDE = "hide"
    COMMON = "common"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"


def map_to_rules(rule_map: dict):
    rules = []

    hidden = [name for (name, tier) in rule_map.items() if tier == RULE.HIDE]
    common = [name for (name, tier) in rule_map.items() if tier == RULE.COMMON]
    rare = [name for (name, tier) in rule_map.items() if tier == RULE.RARE]
    epic = [name for (name, tier) in rule_map.items() if tier == RULE.EPIC]
    legendary = [name for (name, tier) in rule_map.items() if tier == RULE.LEGENDARY]

    if len(hidden) > 0:
        rules.append(Hide([MultiBaseType(hidden)]))
    if len(common) > 0:
        rules.append(Show([MultiBaseType(common), TierStyle(TIER.COMMON)]))
    if len(rare) > 0:
        rules.append(Show([MultiBaseType(rare), TierStyle(TIER.RARE)]))
    if len(epic) > 0:
        rules.append(Show([MultiBaseType(epic), TierStyle(TIER.EPIC)]))
    if len(legendary) > 0:
        rules.append(Show([MultiBaseType(legendary), TierStyle(TIER.LEGENDARY)]))

    return rules
