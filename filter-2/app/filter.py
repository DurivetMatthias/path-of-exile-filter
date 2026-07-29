"""
Programmatically generate item filter files.
This project aims to simplify the configuration of colors, sounds, effects etc.
This is done by adding tags to all items and then applying rules to those tags.
In doing so we avoid the many to many assignment of properties and try to
reduce it to one-to-one as much as possible
"""

import os
import datetime
from pathlib import Path

from app import formatting
from app.blocks import *
from app.actions import *
from app.categories import *

FILTER_EXTENSION = "filter"
FILTER_OUTPUT_PATH = Path().home() / "Documents" / "my games" / "Path of Exile 2"
if not FILTER_OUTPUT_PATH.exists():
    FILTER_OUTPUT_PATH = Path(".")


def sort_by_tierstyle(block: Block):
    """Sort by importance based on TierStyle"""
    tier = None
    for condition in block.conditions:
        if isinstance(condition, TierStyle):
            tier = condition.tier
            break

    tier_to_order = {
        TIER.LEGENDARY: 0,
        TIER.EPIC: 1,
        TIER.RARE: 2,
        TIER.COMMON: 3,
        None: 4,
    }

    return tier_to_order[tier]


def sort_rules(rules: list[Block]):
    """Put Show blocks first and Hide blocks last, within each group sort by TierStyle"""
    show_rules = [rule for rule in rules if isinstance(rule, Show)]
    hide_rules = [rule for rule in rules if isinstance(rule, Hide)]
    show_rules.sort(key=sort_by_tierstyle)
    hide_rules.sort(key=sort_by_tierstyle)
    return [*show_rules, *hide_rules]


def generate(rules: list[Block], name: str = "main"):
    header = f"""
        # The following item filter was automatically generated.
        # Created on {datetime.datetime.now().strftime("%A %B %d %Y, %H:%M:%S")}.
    """
    sorted_rules = sort_rules(rules)
    file_content = formatting.format_filter(
        rules=sorted_rules,
        header=header,
    )
    output_filepath = os.path.join(FILTER_OUTPUT_PATH, f"{name}.{FILTER_EXTENSION}")
    with open(output_filepath, mode="w", encoding="utf-8") as output_file:
        output_file.write(file_content)
    print("=" * len(output_filepath))
    print(output_filepath)
    print("=" * len(output_filepath))
