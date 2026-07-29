import textwrap

from typing import Sequence

from app.conditions import *
from app.blocks import *

TAB_WITH_SPACES = " " * 4


def format_header(header: str):
    return textwrap.dedent(header).strip("\n")


def format_condition(condition: Condition) -> str:
    return textwrap.dedent(str(condition)).strip("\n")


def format_conditions(conditions: Sequence[Condition]) -> str:
    condition_blocks = [format_condition(condition) for condition in conditions]
    return "\n".join(condition_blocks)


def format_rule(rule: Block):
    instruction_text = format_condition(rule.instruction)
    conditions_text = format_conditions(rule.conditions)
    conditions_text = textwrap.indent(conditions_text, prefix=TAB_WITH_SPACES)
    return "\n".join([instruction_text, conditions_text])


def format_rules(rules: Sequence[Block]):
    rule_blocks = [format_rule(rule) for rule in rules]
    return "\n\n".join(rule_blocks)


def format_filter(*, rules: list[Block], header: str):
    rules_text = format_rules(rules)
    header_text = format_header(header)

    filter_text = "\n\n".join([header_text, rules_text])
    return filter_text
